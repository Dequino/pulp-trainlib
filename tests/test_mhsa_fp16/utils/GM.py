"""
Copyright (C) 2021-2022 ETH Zurich and University of Bologna
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors: Francesco Conoscenti (francesco.conoscenti@studio.unibo.it), Alberto Dequino (alberto.dequino@unibo.it),
         Calin Diaconu (calin.diaconu@studio.unibo.it)
"""

import argparse
from copy import deepcopy

import numpy as np  # Matrix and vector computation package
import torch
import torch.nn as nn

import dump_utils as dump
import mhsa


class MyNet(nn.Module):
    def __init__(self, in_w, n_heads, att_dim, bf16_format):
        super().__init__()
        self.mhsa = mhsa.MultiHeadedSelfAttention(dim=in_w, num_heads=n_heads, att_dim=att_dim, bf16_format=bf16_format)

    def forward(self, x, tgt_len):
        return self.mhsa(x=x, tgt_len=tgt_len)


def hook_fn1(_, __, o):
    # Hook to write output gradients
    f = open("mhsa-grads.h", "w")

    print("------------Output Grad------------")
    for grad in o:
        try:
            output_grad = torch.transpose(grad, 0, 1)
            f.write('#define G_OUTPUT_SIZE '+str(output_grad.numel())+'\n')

            if bf16_format == 0:
                print(output_grad.half())
            else:
                print(output_grad.bfloat16())

            if current_step == 'BACKWARD_GRAD' or current_step == 'BACKWARD_ERROR':
                if bf16_format == 0:
                    f.write('PI_L2 fp16 OUTPUT_GRAD[G_OUTPUT_SIZE] = {' +
                            dump.tensor_to_string(output_grad.half()) +
                            '};\n')
                else:
                    f.write('PI_L2 fp16 OUTPUT_GRAD[G_OUTPUT_SIZE] = {' +
                            dump.tensor_to_string(output_grad.bfloat16()) +
                            '};\n')
            else:
                if bf16_format == 0:
                    f.write('PI_L2 fp16 OUTPUT_GRAD[G_OUTPUT_SIZE] = {' +
                            dump.tensor_to_string(output_grad.half()) +
                            '};\n')
                else:
                    f.write('PI_L2 fp16 OUTPUT_GRAD[G_OUTPUT_SIZE] = {' +
                            dump.tensor_to_string(output_grad.bfloat16()) +
                            '};\n')
        except AttributeError:
            print("None found for Gradient (output)")

    f.close()


def hook_fn2(_, __, o):
    # Hook for writing output to file
    cont = 0
    f = open("mhsa-output.h", "w")

    print("------------Output------------")
    for grad in o:
        try:
            if cont == 0:
                output_grad = grad
                f.write('#define OUTPUT_SIZE '+str(output_grad.numel())+'\n')

                if bf16_format == 0:
                    print(output_grad.half())
                    f.write('PI_L2 fp16 OUTPUT[OUTPUT_SIZE] = {'+dump.tensor_to_string(output_grad.half())+'};\n')
                else:
                    print(output_grad.bfloat16())
                    f.write('PI_L2 fp16 OUTPUT[OUTPUT_SIZE] = {'+dump.tensor_to_string(output_grad.bfloat16())+'};\n')

            cont += 1
        except AttributeError:
            print("None found for Output")

    f.close()


if __name__ == '__main__':
    # ~~~~~~~~~~ INTRO ~~~~~~~~~~
    # Set the seed for reproducibility
    np.random.seed(seed=1)  # <----- Sneed
    torch.manual_seed(0)

    # Visualize data with more precision
    torch.set_printoptions(precision=10, sci_mode=False)

    # Set up parser
    parser = argparse.ArgumentParser("MHSA Layer Test")
    parser.add_argument('--in_width', type=int, default=8)  # Token size
    parser.add_argument('--in_height', type=int, default=4)  # Sequence length
    parser.add_argument('--ch_in', type=int, default=1)
    parser.add_argument('--ch_out', type=int, default=1)
    parser.add_argument('--n_heads', type=int, default=8)
    parser.add_argument('--weight', type=float, default=0.1)
    parser.add_argument('--att_dim', type=int, default=8)
    parser.add_argument('--bf16_format', type=int, default=1)  # if == 1, data format if bfloat16, if 0 is float16
    # Possible steps: FORWARD, BACKWARD_GRAD, BACKWARD_ERROR
    parser.add_argument('--step', type=str, default='FORWARD')

    args = parser.parse_args()

    # Read arguments
    in_h = args.in_height
    in_w = args.in_width
    ch_in = args.ch_in
    ch_out = args.ch_out
    n_heads = args.n_heads
    current_step = args.step
    weight_init = args.weight
    att_dim = args.att_dim
    head_dim = int(att_dim / n_heads)
    bf16_format = args.bf16_format

    # Write net step to file
    f_step = open('step-check.h', 'w')
    f_step.write('#define ' + str(current_step) + '\n')
    f_step.close()

    # Write input/output weights to file
    f = open("init-defines.h", "w")

    f.write('#define Tin_C_l1 '+str(ch_in)+'\n')
    f.write('#define Tin_H_l1 '+str(in_h)+'\n')
    f.write('#define Tin_W_l1 '+str(in_w)+'\n')
    f.write('#define Tout_C_l1 '+str(ch_out)+'\n')
    f.write('#define Tn_heads_l1 '+str(n_heads)+'\n')
    f.write('#define Tatt_dim_l1 '+str(att_dim)+'\n')
    f.write('#define Thead_dim_l1 '+str(head_dim)+'\n')

    f.close()

    # Define network and add hook
    if bf16_format == 0:
        net = MyNet(in_w=in_w, n_heads=n_heads, att_dim=att_dim, bf16_format=bf16_format).half()
    elif bf16_format == 1:
        net = MyNet(in_w=in_w, n_heads=n_heads, att_dim=att_dim, bf16_format=bf16_format).bfloat16()
    net.zero_grad()

    gradsRnn = net.mhsa.register_full_backward_hook(hook_fn1)

    # ~~~~~~~~~~ MANAGE INPUT ~~~~~~~~~~
    # Generate random input data
    if bf16_format == 0:
        inp = torch.randn(ch_in, in_h, in_w).half()
    else:
        inp = torch.randn(ch_in, in_h, in_w).bfloat16()
    inp.requires_grad = True

    # Print input data to terminal
    print("------------Input sequence------------")
    print(inp)

    # Write transpose of input data to file
    if bf16_format == 0:
        inp_copy = torch.transpose(inp, -1, -2).half()
    else:
        inp_copy = torch.transpose(inp, -1, -2).bfloat16()

    f = open("input-sequence.h", "w")
    f.write("#define INPUT_SIZE "+str(inp.numel())+'\n')
    f.write('PI_L2 fp16 INPUT[INPUT_SIZE] = {'+dump.tensor_to_string(inp_copy)+'};\n')
    f.close()

    # ~~~~~~~~~~ MANAGE INPUT WEIGHTS ~~~~~~~~~~
    # Generate random input weights
    if bf16_format == 0:
        in_wgt_init_tensor = torch.randn(att_dim * 3, in_w).half()
    else:
        in_wgt_init_tensor = torch.randn(att_dim * 3, in_w).bfloat16()

    # Copy input weights to network
    with torch.no_grad():
        net.mhsa.proj_in.weight.data = deepcopy(in_wgt_init_tensor)

    # Print input weights to terminal
    print("Shape input weights:")
    print(net.mhsa.proj_in.weight.shape)
    print(net.mhsa.proj_in.weight.data)
    print("\n")

    # Write input weights to init file
    f = open("init-defines.h", 'a')
    f.write("\n\n// Input Projections Weight Initialization\n")
    f.write("#define INPUT_WGT_SIZE (3*Tatt_dim_l1*Tin_W_l1)\n")
    f.write('PI_L2 fp16 INPUT_WEIGHTS[INPUT_WGT_SIZE] = {'+dump.tensor_to_string(in_wgt_init_tensor)+'};\n')
    f.close()

    # ~~~~~~~~~~ MANAGE OUTPUT WEIGHTS ~~~~~~~~~~
    # Generate random output weights
    if bf16_format == 0:
        output_proj_wgt_init_tensor = torch.randn(in_w, att_dim).half()
    else:
        output_proj_wgt_init_tensor = torch.randn(in_w, att_dim).bfloat16()

    # Copy output weights to network
    with torch.no_grad():
        net.mhsa.proj_out.weight.data = deepcopy(output_proj_wgt_init_tensor)

    # Print output weights to terminal
    print("Shape output projection weights:")
    print(net.mhsa.proj_out.weight.data.shape)
    print(net.mhsa.proj_out.weight.data)
    print("\n")

    # Write output weights to init file
    f = open("init-defines.h", 'a')
    f.write("\n\n")
    f.write("#define OUTPUT_WGT_SIZE (Tatt_dim_l1*Tin_W_l1)\n")
    f.write('PI_L2 fp16 OUTPUT_WEIGHTS[OUTPUT_WGT_SIZE] = {'+dump.tensor_to_string(output_proj_wgt_init_tensor)+'};\n')
    f.close()

    # ~~~~~~~~~~ COMPUTE OUTPUT ~~~~~~~~~~
    if bf16_format == 0:
        label = torch.ones(in_h, in_w).half()
    else:
        label = torch.ones(in_h, in_w).bfloat16()
    criterion = nn.MSELoss()
    out = net(x=inp, tgt_len=in_h)

    # Print output to terminal
    print("out: ")
    print(out.size())
    print(label.size())
    print(out)

    # Compute loss
    loss = criterion(out.float(), label.float())

    # Write output to file
    if bf16_format == 0:
        out_copy = torch.transpose(out, -1, -2).half()
    else:
        out_copy = torch.transpose(out, -1, -2).bfloat16()

    f = open("mhsa-output.h", "w")
    f.write('#define OUTPUT_SIZE '+str(out.numel())+'\n')
    f.write('PI_L2 fp16 OUTPUT[OUTPUT_SIZE] = {'+dump.tensor_to_string(out_copy)+'};\n')
    f.close()

    # Compute gradients
    net.zero_grad()
    loss.backward()

    input_wgt_grad = net.mhsa.proj_in.weight.grad
    output_wgt_grad = net.mhsa.proj_out.weight.grad
    input_grad = inp.grad.transpose(1, 2)

    # Write gradients to file
    f = open("mhsa-grads.h", 'a')

    f.write('#define G_INPUT_WGT_SIZE '+str(input_wgt_grad.numel())+'\n')
    f.write("PI_L2 fp16 INPUT_WGT_GRAD[G_INPUT_WGT_SIZE] = {"+dump.tensor_to_string(input_wgt_grad)+"};\n")

    f.write('#define G_OUTPUT_WGT_SIZE '+str(output_wgt_grad.numel())+'\n')
    f.write("PI_L2 fp16 OUTPUT_WGT_GRAD[G_OUTPUT_WGT_SIZE] = {"+dump.tensor_to_string(output_wgt_grad)+"};\n")

    f.write("#define G_IN_SIZE "+str(input_grad.numel()) + '\n')
    f.write("PI_L2 fp16 INPUT_GRAD[G_IN_SIZE] = {"+dump.tensor_to_string(input_grad) + "};\n")

    f.close()

    # Write attention scores to file
    f = open("attention_scores.h", "w")
    f.write('#define ATTENTION_S_LENGTH '+str(net.mhsa.scores.numel())+'\n')
    f.write('PI_L2 fp16 ATTENTION_SCORES[ATTENTION_S_LENGTH] = {' +
            dump.tensor_to_string(torch.transpose(net.mhsa.scores, 0, 1)) +
            '};\n')
    f.close()

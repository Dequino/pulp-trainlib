#define G_OUTPUT_SIZE 32
PI_L2 float OUTPUT_GRAD[G_OUTPUT_SIZE] = {-0.061775416135787964f, -0.061581291258335114f, -0.06138716638088226f, -0.06119304150342941f, -0.06099891662597656f, -0.06080479174852371f, -0.06061066687107086f, -0.06041654199361801f, -0.061775412410497665f, -0.061581287533044815f, -0.061387162655591965f, -0.06119304150342941f, -0.06099891662597656f, -0.06080479174852371f, -0.06061066687107086f, -0.06041654199361801f, -0.061775412410497665f, -0.061581287533044815f, -0.061387162655591965f, -0.061193037778139114f, -0.060998912900686264f, -0.060804788023233414f, -0.06061066314578056f, -0.060416534543037415f, -0.06177540868520737f, -0.06158128380775452f, -0.061387158930301666f, -0.061193034052848816f, -0.06099890545010567f, -0.06080478057265282f, -0.060610655695199966f, -0.060416530817747116f};
#define G_INPUT_WGT_SIZE 192
PI_L2 float INPUT_WGT_GRAD[G_INPUT_WGT_SIZE] = {-3.0980402271341134e-11f, -3.0681075735561336e-11f, -2.978309612822194e-11f, -2.8286458245152524e-11f, -2.6191163821076557e-11f, -2.3497219794887947e-11f, -2.0204617492969312e-11f, -1.631336211949108e-11f, -4.5564177431067776e-11f, -4.5123946246228286e-11f, -4.380324575281591e-11f, -4.160207595083065e-11f, -3.852044030971946e-11f, -3.4558335360035386e-11f, -2.9715761101778426e-11f, -2.3992721004395534e-11f, -6.312128597585343e-11f, -6.251141965174511e-11f, -6.068181374052628e-11f, -5.7632475181090825e-11f, -5.336340397343875e-11f, -4.787459317867615e-11f, -4.1166042796803026e-11f, -3.323775976671328e-11f, -8.388877786869031e-11f, -8.307825261066881e-11f, -8.064668377549822e-11f, -7.659406442428462e-11f, -7.092040843481584e-11f, -6.362570192930406e-11f, -5.470993796885537e-11f, -4.417313390070454e-11f, -1.0810601025479372e-10f, -1.0706151243322637e-10f, -1.0392798427405481e-10f, -9.870544659396074e-11f, -9.139389245405027e-11f, -8.19933287932173e-11f, -7.050375561146183e-11f, -5.692515903099604e-11f, -1.3601138271202018e-10f, -1.346972533511348e-10f, -1.307549069018421e-10f, -1.2418428785299085e-10f, -1.1498545171573227e-10f, -1.0315836379559684e-10f, -8.870302409258457e-11f, -7.161945342337717e-11f, -1.6784169887262834e-10f, -1.662200377339218e-10f, -1.6135508207337779e-10f, -1.5324677637984507e-10f, -1.418951900422627e-10f, -1.2730026754947943e-10f, -1.0946203665707088e-10f, -8.838048348724925e-11f, -2.038341995191928e-10f, -2.0186480265138584e-10f, -1.9595655653681376e-10f, -1.8610950280883998e-10f, -1.7232361371188887e-10f, -1.5459891700153605e-10f, -1.329353849222059e-10f, -1.0733303135168626e-10f, -6.878032865476058e-12f, -6.878025926582154e-12f, -6.878032865476058e-12f, -6.878032865476058e-12f, -6.878025926582154e-12f, -6.878025926582154e-12f, -6.878032865476058e-12f, -6.878025926582154e-12f, -1.2335341081914919e-11f, -1.2335341081914919e-11f, -1.2335354959702727e-11f, -1.2335341081914919e-11f, -1.2335327204127111e-11f, -1.2335341081914919e-11f, -1.2335341081914919e-11f, -1.2335341081914919e-11f, -1.9707735443574848e-11f, -1.970772156578704e-11f, -1.9707735443574848e-11f, -1.970772156578704e-11f, -1.970772156578704e-11f, -1.9707735443574848e-11f, -1.9707735443574848e-11f, -1.9707735443574848e-11f, -2.9192648298703716e-11f, -2.9192648298703716e-11f, -2.9192648298703716e-11f, -2.919267605427933e-11f, -2.919267605427933e-11f, -2.919267605427933e-11f, -2.9192717687642755e-11f, -2.919273156543056e-11f, -4.098815731268246e-11f, -4.098815731268246e-11f, -4.0988185068258076e-11f, -4.0988185068258076e-11f, -4.098821282383369e-11f, -4.098824057940931e-11f, -4.098826833498492e-11f, -4.0988323846136154e-11f, -5.5292548317709134e-11f, -5.5292603828860365e-11f, -5.5292548317709134e-11f, -5.5292548317709134e-11f, -5.52924928065579e-11f, -5.5292548317709134e-11f, -5.5292603828860365e-11f, -5.5292548317709134e-11f, -7.23028859006547e-11f, -7.230277487835224e-11f, -7.230277487835224e-11f, -7.230283038950347e-11f, -7.230277487835224e-11f, -7.230283038950347e-11f, -7.230277487835224e-11f, -7.230271936720101e-11f, -9.221634567069259e-11f, -9.221656771529751e-11f, -9.221656771529751e-11f, -9.221645669299505e-11f, -9.221634567069259e-11f, -9.221640118184382e-11f, -9.221640118184382e-11f, -9.221634567069259e-11f, -0.00017621228471398354f, -0.0001745097542880103f, -0.00016940214845817536f, -0.00016088948177639395f, -0.00014897173969075084f, -0.00013364893675316125f, -0.00011492105841170996f, -9.278811194235459e-05f, -0.0002267997624585405f, -0.0002246084768557921f, -0.000218034561839886f, -0.00020707804651465267f, -0.0001917389454320073f, -0.00017201722948811948f, -0.00014791289868298918f, -0.00011942597484448925f, -0.0002773872693069279f, -0.0002747071848716587f, -0.0002666669897735119f, -0.0002532666258048266f, -0.0002345061511732638f, -0.00021038550767116249f, -0.00018090475350618362f, -0.0001460638304706663f, -0.00032797473249956965f, -0.0003248059074394405f, -0.0003152993740513921f, -0.00029945519054308534f, -0.0002772733278106898f, -0.00024875375675037503f, -0.00021389656467363238f, -0.0001727016642689705f, -0.00037856216658838093f, -0.0003749045717995614f, -0.00036393175832927227f, -0.0003456437261775136f, -0.0003200405044481158f, -0.0002871220640372485f, -0.0002468884049449116f, -0.00019933951261918992f, -0.0004291496588848531f, -0.0004250032943673432f, -0.0004125641717109829f, -0.0003918323200196028f, -0.00036280768108554184f, -0.0003254903422202915f, -0.0002798802452161908f, -0.00022597737552132457f, -0.0004797371511813253f, -0.000475102016935125f, -0.00046119658509269357f, -0.0004380208847578615f, -0.0004055749159306288f, -0.0003638586204033345f, -0.00031287208548747003f, -0.00025261525297537446f, -0.0005303245270624757f, -0.0005252007395029068f, -0.0005098289693705738f, -0.0004842094494961202f, -0.0004483420925680548f, -0.0004022268985863775f, -0.0003458638966549188f, -0.00027925308677367866f};
#define G_OUTPUT_WGT_SIZE 64
PI_L2 float OUTPUT_WGT_GRAD[G_OUTPUT_WGT_SIZE] = {-0.0008106170571409166f, -0.0008531185449101031f, -0.0008956200326792896f, -0.0009381214622408152f, -0.0009806230664253235f, -0.00102312455419451f, -0.0010656260419636965f, -0.0011081276461482048f, -0.0008080697734840214f, -0.0008504376746714115f, -0.0008928056340664625f, -0.0009351734770461917f, -0.0009775415528565645f, -0.0010199095122516155f, -0.0010622772388160229f, -0.0011046454310417175f, -0.0008055224316194654f, -0.00084775680443272f, -0.0008899911772459745f, -0.0009322254918515682f, -0.0009744599228724837f, -0.0010166943538933992f, -0.001058928668498993f, -0.0011011630995199084f, -0.0008029751479625702f, -0.0008450759341940284f, -0.0008871767786331475f, -0.0009292776230722666f, -0.0009713784093037248f, -0.0010134793119505048f, -0.001055580098181963f, -0.0010976808844134212f, -0.000800427864305675f, -0.0008423950639553368f, -0.0008843623218126595f, -0.0009263295796699822f, -0.0009682968375273049f, -0.0010102641535922885f, -0.0010522312950342894f, -0.0010941986693069339f, -0.000797880464233458f, -0.0008397142519243062f, -0.0008815479231998324f, -0.0009233815944753587f, -0.0009652153239585459f, -0.0010070489952340722f, -0.0010488827247172594f, -0.0010907164542004466f, -0.0007953332387842238f, -0.0008370333816856146f, -0.0008787335827946663f, -0.0009204336092807353f, -0.000962133810389787f, -0.0010038340697064996f, -0.0010455341544002295f, -0.0010872342390939593f, -0.0007927858969196677f, -0.0008343524532392621f, -0.0008759190095588565f, -0.0009174856240861118f, -0.0009590522386133671f, -0.0010006187949329615f, -0.0010421853512525558f, -0.0010837521404027939f};
#define G_IN_SIZE 32
PI_L2 float INPUT_GRAD[G_IN_SIZE] = {-1.3824706077575684f, -1.4507346153259277f, -1.5189987421035767f, -1.587262749671936f, -1.655526876449585f, -1.7237907648086548f, -1.7920548915863037f, -1.8603190183639526f, -1.3824723958969116f, -1.45073664188385f, -1.5190008878707886f, -1.587264895439148f, -1.655529260635376f, -1.7237932682037354f, -1.7920575141906738f, -1.8603215217590332f, -1.3824779987335205f, -1.450742483139038f, -1.5190069675445557f, -1.5872714519500732f, -1.6555359363555908f, -1.7238004207611084f, -1.792064905166626f, -1.860329508781433f, -1.3824870586395264f, -1.4507521390914917f, -1.519017219543457f, -1.5872821807861328f, -1.6555472612380981f, -1.7238123416900635f, -1.7920775413513184f, -1.8603425025939941f};

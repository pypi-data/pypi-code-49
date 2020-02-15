import json
import numpy as np

def process_data(data):
    with open('vistemp/attentions.json', 'w') as outfile:
        json.dump(data, outfile)


def process_transformer_data(encoder_self_attention,decoder_self_attention,decoder_encoder_attention):
    encoder_self_list=[]
    for item in encoder_self_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["source_sentence"]
        tmp_dict["lower_sentence"]=item["source_sentence"]

        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        
        encoder_self_list.append(tmp_dict)
    with open("vistemp/encoder_self_attention.json",'w') as outfile:
        json.dump(encoder_self_list,outfile)
    
    decoder_self_list=[]
    for item in decoder_self_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["target_sentence"]
        tmp_dict["lower_sentence"]=item["target_sentence"]

        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        
        decoder_self_list.append(tmp_dict)
    with open("vistemp/decoder_self_attention.json",'w') as outfile:
        json.dump(decoder_self_list,outfile)
    

    decoder_encoder_list=[]
    for item in decoder_encoder_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["source_sentence"]
        tmp_dict["lower_sentence"]=item["target_sentence"]

        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        
        decoder_encoder_list.append(tmp_dict)
    with open("vistemp/decoder_encoder_attention.json",'w') as outfile:
        json.dump(decoder_encoder_list,outfile)

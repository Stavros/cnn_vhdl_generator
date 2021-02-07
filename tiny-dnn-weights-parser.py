# Tiny-DNN model weights parser - tiny-dnn-weight-parser.py - @Stavros Kalapothas 2021

import json
import struct
import numpy as np
import math

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

with open('c:/Users/Stavros/Downloads/LeNet-model.json') as f:
  #data = json.loads(f.read())
  data = json.load(f)

count = 0   # debug counter
dict

for key, value in data.items():
    #print(key)
    if 'value' in key:
        if 'type' in data[key]:
            types = ('fully_connected', 'conv')
            if any(t in data[key]['type'] for t in types):
              count += 1  # debug
              #print(count)
              #for i in data[key]['value0']:
              #print(data[key]['value0'])
              dictd = data[key]['value0']
              print(dictd[count])
              dec, who = math.modf(dictd[count]) 
              #print('{:02b}'.format(who))
              #print('{:03b}'.format(dec))
              print(who,dec)
              #int32bits = np.asarray(dictd[count], dtype=np.float32).view(np.int32).item()  # .item() optional
              int_whole = np.asarray(who, dtype=np.int).view(np.int).item() 
              int_dec = np.asarray(dec, dtype=np.float32).view(np.int32).item() 
              print('{:02b}'.format(int_whole))
              print('{:016b}'.format(int_dec))
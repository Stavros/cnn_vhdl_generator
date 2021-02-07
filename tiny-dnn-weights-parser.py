# Tiny-DNN model weights parser - tiny-dnn-weight-parser.py - @Stavros Kalapothas 2021

import json

with open('./LeNet-model.json') as f:
  data = json.loads(f.read())

count = 0   # debug counter

for key, value in data.items():
    #print(key)
    if 'value' in key:
        if 'type' in data[key]:
            types = ('fully_connected', 'conv')
            if any(t in data[key]['type'] for t in types):
              #count +=1  debug
              #print(count)
              #for i in data[key]['value0']:
              print(data[key]['value0'])
import json

data = {}
data['dual_slider'] = {'hue': [30, 200],  
                    'saturation': [30, 200], 
                    'value': [30, 200], 
                    'target': [30, 200], 
                    'fullness': [30, 200], 
                    'aspect': [30, 200] }
data['slider'] = {'exposure': 211,  
                    'white_balance': 213, 
                    'erosion_steps': 214, 
                    'dilation_steps': 215, }


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['dual_slider']:
        print(p)
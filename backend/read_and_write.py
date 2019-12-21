
import json

def read_json(selector):
    with open('data.txt') as json_file:

        read = json.load(json_file)
        data = read[selector]
        
    return(data)
        

def write_json(selector, key, new_value):
    with open('data.txt') as json_file:

        read = json.load(json_file)
        
        read[selector][key] = new_value

    json_file.close()


    with open('data.txt', 'w') as outfile:
        json.dump(read, outfile)
    json_file.close()

print(read_json('dual_slider'))
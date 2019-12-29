
import json

def read_json(selector):
    with open('static/data.json') as json_file:

        read = json.load(json_file)
        data = read[selector]
    json_file.close()
    return(data)
        

def write_json(selector, key, new_value):
    with open('static/data.json') as json_file:

        read = json.load(json_file)
        try:
            read[selector][key] = new_value
        except:
            read[selector] = {key : new_value}
    json_file.close()


    with open('static/data.json', 'w') as outfile:
        json.dump(read, outfile)
    json_file.close()

def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)
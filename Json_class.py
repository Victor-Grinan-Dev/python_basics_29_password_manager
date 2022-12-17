import json

new_data = {
    'facebook': {
        'email': 'animal@gmail.com',
        'password': '123456'
    }
}

with open('data.json', 'r') as data_file:
    data = json.load(data_file)
    print(data)
    print(type(data))

with open('data.json', 'r') as data_file:
    # read old data
    data = json.load(data_file)
    # updating old data
    data.update(new_data)
    # saving updated data
    json.dump(data, data_file, indent=4)

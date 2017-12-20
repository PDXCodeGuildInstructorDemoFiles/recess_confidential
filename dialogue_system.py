import json

with open('dialogue_scratch.json', 'r') as f:
    data = json.load(f)

# def talk(who):
#     character = {}
#     for key, value in data[who]:
#         character[key] = value
#     return character



if __name__ == '__main__':
    print(data)

    # print(talk('PETA'))


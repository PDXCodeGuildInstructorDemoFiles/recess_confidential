import json

with open('dialogue_scratch.json', 'r') as f:
    data = json.load(f)


if __name__ == '__main__':
    print(data)

import json
import random

with open('trivia_json/science.json', 'r+') as f:
    data = json.loads(f.read())

new_dict_list = []

for i in data['results']:
    options = i['incorrect_answers']
    options.append(i['correct_answer'])
    random.shuffle(options)
    answer_index = options.index(i['correct_answer'])
    new_dict_list.append({
        'question': i['question'],
        'answer': answer_index+1,
        'options': options
    })
    
with open('trivia_json/science_formatted.json', 'w') as wf:
    wf.write(json.dumps(new_dict_list))
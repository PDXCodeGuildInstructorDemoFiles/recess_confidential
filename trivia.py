import sys
import json
import random

def trivia_game(genre):
    
    with open(f'trivia_json/{genre}_formatted.json', 'r') as f:
        data = json.loads(f.read())
        questions = []
        
        for ask in range(0,10):
            secure_random = random.SystemRandom()
            questions.append(secure_random.choice(data))

    score = 0
    for ask in questions:
        print (ask['question'] + '?')
        n = 1
        for options in ask['options']:
            print ("%d) %s" % (n, options))
            n = n + 1
        response = sys.stdin.readline().strip()
        if response not in ['1', '2', '3', '4']:
            print('wrong answer, buddy')
        elif int(response) == ask['answer']:
            print ('correct')
            score += 1
        else:
            print ('wrong')
    
    if score > 7:
        return True
    else:
        return False



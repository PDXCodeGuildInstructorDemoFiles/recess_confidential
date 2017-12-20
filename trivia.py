import sys

def science_quiz():
    questions = [
        {
            'question': 'What cloud type can described as wispy and thin',
            'answer': 2,
            'options': ['Nimbus', 'Cirrus', 'Cumulous', 'Stratus' ]
        },
        {
            'question': 'What weather tool is used to measure air pressure',
            'answer': 3,
            'options': ['Anemometer', 'Thermometer', 'Barometer', 'Seismometer']
        },
        {
            'question': 'Which travels faster in a lightning storm',
            'answer': 1,
            'options': ['Lightning', 'Thunder', 'Same', 'No way to tell']
        },
        {
            'question': 'What type of cloud appears almost as as a blanket of clouds in the sky?',
            'answer': 2,
            'options': ['Cirrus', 'Stratus', 'Cumulous', 'Nimbus']
        },
        {
            'question': 'What warm “conveyer belt” of water raises the average temerature of the Eastern Seaboard by as much as 15° F',
            'answer': 3,
            'options': ['The Jet Stream', 'The Main Stream', 'The Gulf Stream', 'The Easterlie winds']
        },
        {
            'question': 'While watching a barometer you noticed that the pressure has changed from low to high. What should the weather be like outside',
            'answer': 4,
            'options': ['Rainy','Cloudy','Stormy','Sunny']
        },

        {
            'question': 'Gusts of wind are caused by',
            'answer': 1,
            'options': ['Changes in Air Pressure from High to Low', 'Changes in Air Pressure from Low to High','Presence of Clouds', 'The movement of trees']
        },
        {
            'question': 'The westerlies are the prevailing winds which are caused predominantly by the',
            'answer': 1,
            'options': ['Jet Stream', 'Gulf Stream', 'Wind Stream', 'Water Stream']
        },
        {
            'question': 'High Atmospheric Pressure will result in',
            'answer': 3,
            'options': ['Thunderstorms', 'Cloudy', 'Clear blue skies', 'Rain']
        },
        {
            'question': 'If it is Summer in the United States, what season is it in Australia in the Southern Hemisphere',
            'answer': 1,
            'options': [ 'Winter', 'Spring', 'Fall', 'Summer']
        },
    ]


    score = 0
    for ask in questions:
        print (ask['question'] + '?')
        n = 1
        for options in ask['options']:
            print ("%d) %s" % (n, options))
            n = n + 1
        response = sys.stdin.readline().strip()
        if int(response) == ask['answer']:
            print ('correct')
            score += 1
        else:
            print ('wrong')
    
    if score > 7:
        return True
    else:
        return False
 
import pandas

data = pandas.read_csv('./squirrel_data.csv')
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
gray = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])


squirrel_dict = {
    "Fur Color": ['Cinnamon', 'Gray', 'Black'],
    "Count": [cinnamon, gray, black]
}

pandas.DataFrame(squirrel_dict).to_csv('squirrel_count.csv')



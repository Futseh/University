people = {
    
}

answer = input('Do you want to start input? (y/n) ')

while answer.lower() == 'y':
    info = input('Whaat is the name and age of the person? ')

    info = info.split(' ')

    name = info[0]
    age = int(info[1])

    people.update({name: age})
    
    answer = input('Do you want to add more names? (y/n) ')

letter = input('Give me any letter. ')

while len(letter) != 1:
    letter = input('Give me only 1 letter. ')

for person in people:
    if letter == person[0]:
        print(person, people[person])

"""
Terminal> python3 personer.py
    Do you want to start input? (y/n) y
    Whaat is the name and age of the person? jonas 20
    Do you want to add more names? (y/n) y
    Whaat is the name and age of the person? anet 10
    Do you want to add more names? (y/n) n
    Give me any letter. j
    jonas 20
"""
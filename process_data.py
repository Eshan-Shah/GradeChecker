from data import data


def find_correct_data(level, board, subject):
    newdata = []
    for item in data:
        if item[0] == level.upper() and item[1] == board and item[2] == subject.title():
            maxmark = item[3]

            if item[0] == 'GCSE':
                grades = ['Grade 9', 'Grade 8', 'Grade 7', 'Grade 6', 'Grade 5', 'Grade 4,', 'Grade 3', 'Grade 2', 'Grade 1']
            else:
                grades = ['A*', 'A', 'B', 'C', 'D', 'E,', 'U']    

            for n in range(4, len(item)):
                percentage = (item[n] / maxmark) * 100
                newdata.append([grades[n-4], percentage])


    if newdata != []:
        return newdata
    else:
        return 'Not defined'

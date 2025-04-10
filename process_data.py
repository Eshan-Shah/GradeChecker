from data import data


def find_correct_data(level, board, subject):
    newdata = []
    for item in data:
        if item[0] == level.upper() and item[1] == board.title() and item[2] == subject.title():
            maxmark = item[3]
            print(maxmark)
            for n in range(4, len(item)):
                print(item[n])
                percentage = (item[n] / maxmark) * 100
                newdata.append(percentage)


    if newdata != []:
        return newdata
    else:
        return 'Not defined'

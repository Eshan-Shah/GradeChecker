from data import data


def find_correct_data(level, board, subject):
    newdata = []
    for item in data:
        if item[0] == level.upper() and item[1] == board.title() and item[2] == subject.title():
            for n in range(3, len(item)):
                newdata.append(item[n])

    if newdata != []:
        return newdata
    else:
        return 'Not defined'

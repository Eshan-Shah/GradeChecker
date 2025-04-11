from data import data


def find_correct_data(level, board, subject, user_percentage):
    newdata = []
    for item in data:
        if item[0] == level.upper() and item[1] == board and item[2] == subject.title():
            maxmark = item[3]

            if item[0] == 'GCSE':
                grades = ['Grade 9', 'Grade 8', 'Grade 7', 'Grade 6', 'Grade 5', 'Grade 4', 'Grade 3', 'Grade 2', 'Grade 1']
            else:
                grades = ['A*', 'A', 'B', 'C', 'D', 'E', 'U']    

            for n in range(4, len(item)):
                boundary_percentage = round((item[n] / maxmark) * 100, 2)
                newdata.append([grades[n - 4], boundary_percentage])

            grade = find_your_grade(user_percentage, newdata)
            newdata = generate_html_table(newdata, grade)

            return newdata, grade  

    return 'Not defined', 'Grade not found'


def generate_html_table(grade_boundaries, user_grade):
    html = """
<table border="1" style="border-collapse: collapse; text-align: center; width: 300px;">
  <thead>
    <tr>
      <th>Grade</th>
      <th>Boundary (%)</th>
    </tr>
  </thead>
  <tbody>
"""
    for grade, boundary in grade_boundaries:
        if grade == user_grade:
            html += f"    <tr style='background-color: yellow;'><td>{grade.strip()}</td><td>{boundary:.2f}</td></tr>\n"
        else:
            html += f"    <tr><td>{grade.strip()}</td><td>{boundary:.2f}</td></tr>\n"

    html += "  </tbody>\n</table>"
    return html



def find_your_grade(percentage, gradeboundaries):
    percentage = float(percentage)
    for grade, boundary in gradeboundaries:
        if percentage >= boundary:
            return grade
    return "Grade not found..." 

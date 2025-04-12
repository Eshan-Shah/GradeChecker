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
<table border="1" style="border-collapse: collapse; text-align: center; width: 100%; margin: 20px auto; font-family: 'Roboto', sans-serif;">
  <thead>
    <tr style="background-color: #8787B7; color: white; text-transform: uppercase;">
      <th style="padding: 12px 15px; font-size: 1.5rem; border-radius: 5px;">Grade</th>
      <th style="padding: 12px 15px; font-size: 1.5rem; border-radius: 5px;">Boundary (%)</th>
    </tr>
  </thead>
  <tbody>
"""
    for grade, boundary in grade_boundaries:
        if grade == user_grade:
            html += f"""
    <tr style="background-color: rgba(126, 100, 182, 0.8); box-shadow: 0 0 10px rgba(106, 76, 156, 0.7); color: white;">
      <td style="padding: 12px 15px; font-size: 1.2rem; border-radius: 5px;">{grade.strip()}</td>
      <td style="padding: 12px 15px; font-size: 1.2rem; border-radius: 5px;">{boundary:.2f}</td>
    </tr>
"""
        else:
            html += f"""
    <tr style="background-color: rgba(48, 25, 63, 0.7); color: white;">
      <td style="padding: 12px 15px; font-size: 1.2rem; border-radius: 5px;">{grade.strip()}</td>
      <td style="padding: 12px 15px; font-size: 1.2rem; border-radius: 5px;">{boundary:.2f}</td>
    </tr>
"""
    html += "  </tbody>\n</table>"
    return html




def find_your_grade(percentage, gradeboundaries):
    percentage = float(percentage)
    for grade, boundary in gradeboundaries:
        if percentage >= boundary:
            return grade
    return "Grade not found..." 

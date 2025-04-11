from flask import Flask, request, render_template
from flask_cors import CORS
from process_data import find_correct_data

app = Flask(__name__)

# Enable CORS
origins = [
    'http://localhost:8000',
    'http://localhost:3000'
]
CORS(app, origins=origins, supports_credentials=True)

@app.route("/", methods=["GET"])
def display():
    return render_template("index.html")

@app.route("/gradeoutput.html", methods=["GET"])
def check():
    percentage = request.args.get("percentage", "")
    examboard = request.args.get("board", "")
    examlevel = request.args.get("level", "")
    subject = request.args.get("subject", "")

    data, grade = find_correct_data(examlevel, examboard, subject, float(percentage))
    if grade.upper() == 'GCSE':
        grade = grade.split(" ")[1]
    else:
        grade


    return render_template("gradeoutput.html", percentage=percentage, table=data, grade=grade)

@app.route("/userinputs.html", methods=["GET"])
def getInputs():
    return render_template("userinputs.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

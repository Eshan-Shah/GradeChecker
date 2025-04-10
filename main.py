from flask import Flask, request, render_template
from flask_cors import CORS
from process_data import convert_to_path, extract_gcse_aqa_data

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
    
    data_path = convert_to_path(examlevel, examboard)
    boundaries = extract_gcse_aqa_data(data_path, subject)

    return render_template("gradeoutput.html", percentage=percentage, data_path=data_path, boundaries=boundaries)

@app.route("/userinputs.html", methods=["GET"])
def getInputs():
    return render_template("userinputs.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

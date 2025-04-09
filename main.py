from flask import Flask, request, render_template
from flask_cors import CORS

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
    return render_template("gradeoutput.html", percentage=percentage)

@app.route("/userinputs.html", methods=["GET"])
def getInputs():
    return render_template("userinputs.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

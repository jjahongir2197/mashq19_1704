from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def bmi():

    if request.method == "POST":

        h = float(request.form["height"])
        w = float(request.form["weight"])

        bmi = w / (h*h)

        return f"BMI: {bmi}"

    return render_template("index.html")

app.run(debug=True)

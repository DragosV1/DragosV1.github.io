from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/auth/login", methods=["GET", "POST"])
def login():
    error = None
    success = "Password correct! Keep going! "
    if request.method == "POST":
        if request.form["userName"] != "admin" or request.form["userPassword"] != "WW91Q3JhY2tlZEl0":
            error = "Failed Login"
            
    return render_template("index.html", success=success, error=error)



if __name__ == "__main__":
    app.run(debug=True)
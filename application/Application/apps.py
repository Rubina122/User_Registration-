from flask import Flask,request
from flask import render_template
app=Flask(__name__)


@app.route("/user", methods=['GET', 'POST'])
def user():
    if request.method == "GET":
        return render_template("temp\ register.html")
    elif request.method == "POST":
        pass

if __name__ == "__main__":
    app.run(debug=True)



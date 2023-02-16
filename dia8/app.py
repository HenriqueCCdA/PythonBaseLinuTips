from flask import Flask, request, render_template


app = Flask(__name__)


@app.get("/")
@app.post("/")
def index():
    print(request.args)
    print(request.form)
    return render_template("index.html", name="Bruno")


@app.route("/pessoas")
def pessoas():
    pessoas = [
        {
            "name": "Bruno"
        },
        {
            "name": "Karla"
        }
    ]
    return render_template("pessoas.html", pessoas=pessoas)

from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route("/")
def index():
    users = (
        {'first_name': 'King', 'last_name': 'Jordan'},
        {'first_name': 'Wednesday', 'last_name': 'Gomez'},
        {'first_name': 'Lisa', 'last_name': 'Crank'},
        {'first_name': 'Kevin', 'last_name': 'Leo'}
    )
    return render_template("index.html", info=users)


if __name__ == "__main__":
    app.run(debug=True)
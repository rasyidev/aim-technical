from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", )
def welcome_page():
    return render_template("welcome_page.html")


if __name__ == '__main__':
    app.run(debug=True)
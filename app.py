from flask import Flask, render_template, request

app = Flask(__name__)


# PAGE: INDEX
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# PAGE: ABOUT
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


# MAIN FUNCTION
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

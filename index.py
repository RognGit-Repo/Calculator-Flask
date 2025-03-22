from flask import Flask, render_template, url_for

app=Flask(__name__)

#route==link==url

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate", methods=["post"])
def calculate():
    return "calculated"

if __name__=="__main__":
    app.run(debug=True)
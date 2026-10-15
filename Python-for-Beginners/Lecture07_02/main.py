from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="Nico")

@app.route("/hello")
def hello():
    return 'hello you!'

app.run()
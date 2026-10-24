from flask import Flask, render_template, request
from main_old import indeed_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="Nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = indeed_jobs(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run()
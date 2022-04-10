from flask import Flask,render_template

app = Flask(__name__,template_folder='templates',static_folder='D://PROJECTS/python projects/Tovice Website/website/static')
app.secret_key = 'tovice'

@app.route("/")
def hello_world():
    return render_template("home.html")




@app.route("/features")
def feature():
    return render_template("feature.html")



@app.route("/languages")
def lang():
    return render_template("lang.html")



@app.route("/about")
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)     
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods =["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
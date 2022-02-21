from fileinput import filename
import os
from flask import Flask, render_template, request, redirect, flash 
import pandas as pd 
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'json'}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



@app.route('/', methods =["GET","POST"])
def home():
    
    if request.method == "POST":
        
        if request.files:
            file = request.files["file"]
            
            file = pd.read_json(file).to_excel("changed_file.xlsx")
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(request.url) 
        
    return render_template("home.html")







@app.route('/about/')
def about():
    
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
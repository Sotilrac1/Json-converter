import os.path
from flask import Flask, render_template, request, redirect
import pandas as pd 




app = Flask(__name__)
save_path = "/static"
app.config["UPLOAD_FOLDER"] = save_path



@app.route('/', methods =["GET","POST"])
def home():
    t=''
    if request.method == "POST":
        
        if request.files:
           uploaded_file = request.files["uploaded_json"]
           name = str(uploaded_file)
           pd.read_json(uploaded_file).to_excel("changed.xlsx")
          
        return redirect(request.url) 
        
    return render_template("home.html", file=t)

@app.route('/about/')
def about():
    
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
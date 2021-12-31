from flask import Flask, render_template, request, redirect
import pandas as pd 




app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "/static"



@app.route('/', methods =["GET","POST"])
def home():
    
    if request.method == "POST":
        
        if request.files:
           uploaded_file = request.files["uploaded_json"]
           
           pd.read_json(uploaded_file).to_excel("New.xlsx")
           
           print("The file has been stored:  ", uploaded_file)
           
        return redirect(request.url) 
        
    return render_template("home.html")

@app.route('/about/')
def about():
    
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
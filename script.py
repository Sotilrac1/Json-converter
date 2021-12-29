from flask import Flask, render_template, request, redirect
import pandas as pd 
import os 



app = Flask(__name__)

app.config["UPLOAD PATH"] = ""



@app.route('/', methods =["GET","POST"])
def home():
    
    if request.method == "POST":
        
        if request.files:
           
           uploaded_file = request.files["uploaded_json"]
           
           converted_file = pd.read_json(uploaded_file).to_excel("converted_json_file.xlsx")
        #    converted_file.save(os.path.join(app.config["UPLOAD PATH"], converted_file.xlsx))
           
           print("The file has been stored:  ", uploaded_file)
           
           print("The file has been converted:  ", converted_file)
           
        return redirect(request.url) 
        
    return render_template("home.html")

@app.route('/about/')
def about():
    
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
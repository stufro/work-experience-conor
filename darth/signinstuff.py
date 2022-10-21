
# importing Flask and other modules
from flask import Flask, request, render_template
import pickle

pass_user = {}
# Flask constructor
app = Flask(__name__) 
ready = False 

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       user = request.form.get("fname")
       # getting input with name = lname in HTML form
       password = request.form.get("lname")
       pass_user[user]=password



    return render_template("index.html")

 
if __name__=='__main__':
   app.run()
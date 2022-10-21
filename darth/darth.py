
# importing Flask and other modules
from contextlib import nullcontext
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.sql import or_

# Flask constructor
pass_user = {}
db = SQLAlchemy()
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
db.init_app(app)

class Incident(db.Model):
    __tablename__ = 'dummy_incidents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    city = db.Column(db.String(210))
    country = db.Column(db.String(255))
    priority = db.Column(db.String(210))
    start_time = db.Column(db.String(210))
    end_time = db.Column(db.String(210))


    def __repr__(self):
        return '<Incident %r>' % self.title

# with app.app_context():
    # db.create_all()
@app.route('/', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       user = request.form.get("fname")
       # getting input with name = lname in HTML form
       password = request.form.get("lname")
       pass_user[user]=password
       if request.form['action1'] == 'Done':
            return redirect("/home")
    return render_template("loginpage.html.j2")

class data_keeper:
    def __init__(self):
        self.pri_req = ''
        self.cntry_req = ''
        self.city_req = ''

@app.route('/home', methods =["GET", "POST"])
def homepage():
    home = data_keeper()
    incidents = db.session.execute(db.select(Incident)).scalars()
    if request.method == "POST":
        home.pri_req=request.form.get('pri_input')
        home.cntry_req =request.form.get('cntry_input')
        home.city_req = request.form.get('city_input')

        incidents = db.session.execute(select(Incident).where((Incident.country.in_([home.cntry_req]) & (Incident.priority.in_([home.pri_req])) & (Incident.city.in_([home.city_req]))))).scalars()
        if home.pri_req == '' and home.city_req == '' and home.cntry_req == '':
            incidents = db.session.execute(db.select(Incident)).scalars()
   
    return render_template("homepage.html.j2", incidents=incidents)






    
if __name__=='__main__':
   app.run()
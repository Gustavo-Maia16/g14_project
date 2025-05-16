from flask import Flask, render_template, request, session
from classes.events import Events
from datafile import filename
from classes.attendees import Attendees
from classes.registrations import Registrations
from classes.venue import Venue
from classes.userlogin import Userlogin
from subs.apps_events import apps_events 
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Venue.read(filename + 'gestao_eventos.db')
Events.read(filename + 'gestao_eventos.db')
Attendees.read(filename + 'gestao_eventos.db')
Registrations.read(filename + 'gestao_eventos.db')
Userlogin.read(filename + 'gestao_eventos.db')
app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"), group = session.get('group', None))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    session.pop("group", None)
    return render_template("index.html", ulogin=session.get("user"), group= session.get("group"))    
@app.route("/chklogin", methods=["post","get"])
def chklogin(): 
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        session["group"] = Userlogin.obj[Userlogin.user_id].usergroup
        return render_template("index.html", ulogin=session["user"], group=session["group"])
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)
@app.route("/Events", methods=["post","get"])
def events():
    return apps_events()
@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()

    
    
from flask import Flask, render_template, request, session
from classes.events import Events
from datafile import filename

app = Flask(__name__)

Events.read(filename + 'gestao_eventos.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/", methods=["post","get"])
def index():
    global prev_option
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")
    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Events.current()
        Events.remove(obj.id)
        if not Events.previous():
            Events.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option == 'insert' and option == 'save':
        strobj = str(Events.get_id(0))
        strobj = strobj + ';' + request.form["name"] + ';' + \
        request.form["edate"]
        obj = Events.from_string(strobj)
        Events.insert(obj.id)
        Events.last()
    elif prev_option == 'edit' and option == 'save':
        obj = Events.current()
        obj.name = request.form["name"]
        obj.dob = request.form["edate"]
        Events.update(obj.id)
    elif option == "first":
        Events.first()
    elif option == "previous":
        Events.previous()
    elif option == "next":
        Events.nextrec()
    elif option == "last":
        Events.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"
    prev_option = option
    obj = Events.current()
    if option == 'insert' or len(Events.lst) == 0:
        id = 0
        id = Events.get_id(id)
        name = edate = ""
    else:
        id = obj.id
        name = obj.name
        edate = obj.edate
    return render_template("index.html", butshow=butshow, butedit=butedit, 
                    id=id,name = name, edate = edate, 
                    ulogin=session.get("user"))
        
if __name__ == '__main__':
    app.run()
from flask import session, render_template, request
from datetime import datetime, date
from classes.userlogin import Userlogin

# Map de classes usadas (ajusta conforme o teu projeto)
class_map = {
    'Events': __import__('classes.events', fromlist=['Events']).Events,
    'Attendees': __import__('classes.attendees', fromlist=['Attendees']).Attendees,
    'Registrations': __import__('classes.registrations', fromlist=['Registrations']).Registrations,
    'Venue': __import__('classes.venue', fromlist=['Venue']).Venue,
    'Userlogin': __import__('classes.userlogin', fromlist=['Userlogin']).Userlogin,
}

prev_option = ""

def obj_to_dict(obj, att):
    d = {}
    for key in att:
        if isinstance(obj, dict):
            d[key] = obj.get(key, "")
        else:
            d[key] = getattr(obj, key, "")
    return d

def apps_gform(cname=''):
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        group = Userlogin.obj[Userlogin.user_id].usergroup
        cl = class_map.get(cname)
        if cl is None:
            return render_template("index.html", ulogin=ulogin)  # ou página de erro

        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")

        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1, len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()

        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(1, len(cl.att)):
                setattr(obj, cl.att[i], request.form[cl.att[i]])
            cl.update(getattr(obj, cl.att[0]))

        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.id)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "cancel":
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"), group=session.get("group"))

        prev_option = option
        obj = cl.current()

        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            obj[cl.att[0]] = 0
            for i in range(1, len(cl.att)):
                obj[cl.att[i]] = ""

        obj_dict = obj_to_dict(obj, cl.att)

        # Define os tipos para o template
        types = {}
        for key in cl.att:
            val = obj_dict.get(key)
            if isinstance(val, (datetime, date)):
                types[key] = 'date'
            elif isinstance(val, int):
                types[key] = 'int'
            elif isinstance(val, float):
                types[key] = 'float'
            else:
                types[key] = 'str'

        return render_template("gform.html",
            butshow=butshow,
            butedit=butedit,
            cname=cname,
            obj=obj_dict,
            att=cl.att,
            des=cl.des,
            types=types,
            ulogin=ulogin,
            group=group
        )
    else:
        return render_template("index.html", ulogin=ulogin)

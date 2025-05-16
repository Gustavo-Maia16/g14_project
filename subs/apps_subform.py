from flask import Flask, render_template, request, session
from datetime import datetime, date
from classes.events import Events
from datafile import filename
from classes.attendees import Attendees
from classes.registrations import Registrations
from classes.venue import Venue
from classes.userlogin import Userlogin

prev_option = ""

def apps_subform(cname=""):
    global prev_option
    tlist = cname.split('_')
    cnames = tlist[0]
    scname = tlist[1]
    ulogin = session.get("user")
    if ulogin is not None:
        cl = eval(cnames)
        sbl = eval(scname)
        cl_header = cl.header
        sbl_header = sbl.header
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
                lines = sbl.getlines("events_id", getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line.id)
                cl.remove(obj.id)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines("events_id", getattr(obj, cl.att[0]))
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
                obj = cl.current()
                # Garantimos que strobj seja uma string desde o início
                strobj = str(getattr(obj, cl.att[0]))
                for i in range(1, len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                objl = sbl.from_string(strobj)
                code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                sbl.insert(objl.id)

        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()

        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            obj[cl.att[0]] = 0
            for i in range(1, len(cl.att)):
                obj[cl.att[i]] = ""
        else:
            for i in range(1, len(sbl.att)):
                headers.append(sbl.att[i][1:])
            lines = sbl.getlines("events_id", getattr(obj, cl.att[0]))
            for line in lines:
                objl.append(sbl.obj[line])

        types = {}
        for key in cl.att:
            val = getattr(obj, key, None)
            if isinstance(val, (datetime, date)):
                types[key] = 'date'
            elif isinstance(val, int):
                types[key] = 'int'
            elif isinstance(val, float):
                types[key] = 'float'
            else:
                types[key] = 'str'

        class NS:
            pass

        ns = NS()
        # Definimos o id numérico do evento atual, não o título do cabeçalho
        # Garantimos que seja um número inteiro
        ns.id_header = int(getattr(obj, cl.att[0])) if option != 'insert' and len(cl.lst) > 0 else 0

        return render_template(
            "subform.html",
            cl_header=cl_header,
            sbl_header=sbl_header,
            butshow=butshow,
            butedit=butedit,
            cname=cname,
            obj=obj,
            att=cl.att,
            des=cl.des,
            ulogin=ulogin,
            objl=objl,
            desl=sbl.des,
            attl=sbl.att,
            group=session.get("group"),
            types=types,
            ns=ns  # Passa o ns para o template
        )
    else:
        return render_template("index.html", ulogin=ulogin, group=session.get("group"))

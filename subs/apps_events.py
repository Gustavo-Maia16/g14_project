from flask import Flask, render_template, request, session
from classes.events import Events
from classes.userlogin import Userlogin

prev_option = ""

def apps_events():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        group = Userlogin.obj[Userlogin.user_id].usergroup
        butshow = "enabled"
        butedit = "disabled"
        butinsert = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Events.current()
            Events.remove(obj.id)
            if not Events.previous():
                Events.first()
        elif option == "insert":
            butshow, butedit, butinsert = "disabled", "enabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Events.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["edate"] + ';' + request.form["venue_id"]
            obj = Events.from_string(strobj)
            Events.insert(obj.id)
            Events.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Events.current()
            obj.name = request.form["name"]
            obj.edate = request.form["edate"]
            obj.venue_id = request.form["venue_id"]
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
            return render_template("index.html", ulogin=session.get("user"), group = session.get("group"))
        prev_option = option
        obj = Events.current()
        if option == 'insert' or len(Events.lst) == 0:
            id = 0
            id = Events.get_id(id)
            name = edate = venue_id = ""
        else:
            id = obj.id
            name = obj.name
            edate = obj.edate
            venue_id = obj.venue_id
        return render_template("events.html",
    butshow=butshow,
    butedit=butedit,
    butinsert=butinsert,
    id=id,
    name=name,
    edate=edate,
    venue_id=venue_id,
    ulogin=session.get("user"),
    group=group
)

    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-


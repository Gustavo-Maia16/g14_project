# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: Test classes based on generic class Gclass

"""""

#Uncomment to test class Events (select next 4 lines and press ctrl-1)
from classes.venue import Venue
Venue.read('data/gestao_eventos.db')
from classes.events import Events
test_class = Events
ob = '498;final;2025-02-06;19'
db = 'gestao_eventos.db'

#Uncomment to test class Venue (select next 4 lines and press ctrl-1)
# from classes.venue import Venue
# test_class = Venue
# ob = '19;Jackson Ltd;Carriechester;544'
# db = 'gestao_eventos.db'

#Uncomment to test class Attendees (select next 4 lines and press ctrl-1)
# from classes.attendees import Attendees
# test_class = Attendees
# ob = '639;Veronica Herman;dianavillanueva@example.com'
# db = 'gestao_eventos.db'

#Uncomment to test class Registrations (select next 4 lines and press ctrl-1)
# from classes.events import Events
# Events.read('data/gestao_eventos.db')
# from classes.attendees import Attendees
# Attendees.read('data/gestao_eventos.db')
# from classes.registrations import Registrations
# test_class = Registrations
# ob = '1;498;639;2025-01-14;Regular;p'
# db = 'gestao_eventos.db'



import datetime

#Reads the test_class.csv file
test_class.read('data/' + db)

op = ''
while op != 'q':
    print('')
    print('Choose one letter for select the option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort by attribute')
    print('f - find by attribute')
    print('---------------')
    print('q - quit')
    print('---------------')
    p = test_class.current()
    print(f'\n{p}')
    op = input('?')
    if op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        p1 = None
        if len(test_class.lst) == 0:
            p = eval('test_class.from_string("' + ob + '")')
            p1 = p
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        print('leave blank to auto-increment')
        id = input(f'{attrib[1:]} = ')
        if id == "":
            id = 0
        else:
            id = int(id)
        strarg = f'test_class({id}'
        for i in range(1, len(str_list)):
            attrib = str_list[i]
            atype = type(getattr(p, attrib))
            if atype == datetime.date or atype == str:
                value = input(f'{attrib[1:]} = ')
                strarg += f',"{value}"'
            else:
                value = atype(input(f'{attrib[1:]} = '))
                strarg += f',{value}'
        strarg += ')'
        if p1 != None:
            # test_class.lst = list()
            test_class.remove(getattr(p, str_list[0]))
        print(strarg)
        pobj = eval(strarg)
        attrib = str_list[0]
        code = getattr(pobj, attrib)
        obj=test_class.current(code)
        test_class.insert(code)

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Record {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj=test_class.current(id)
            print('Leave blank or new value to modify')
            for attrib in str_list[1:]:
                # attrib = str_list[i]
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.date.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        # id = getattr(obj, test_class.att[0][1:])
        test_class.update(id)
    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirm that you want to delete the record (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])
    elif op == 's':
        # Sort products by attribute in ascending order
        attrib = input('sort by attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverse (False):'):
                reverse = True
            codep = p.id         # Keep the position
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)
    elif op == 'f':
        # Find objects with a given value in an attribute
        attrib = input('Attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            if atype == datetime.date:
                value = datetime.date.fromisoformat(input('Value:'))
            else:
                value = atype(input('Value:'))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)


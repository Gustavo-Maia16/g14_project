"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""

import datetime

from classes.gclass import Gclass
from classes.events import Events
from classes.attendees import Attendees

class Registrations(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id', '_events_id','_attendees_id','_date', '_ticket_type', '_seat']
    header = 'Registrations'
    des = ['Id','Events_id','Attendees_id','Date', 'Ticket Type', 'Seat']

    def __init__(self, id, events_id, attendees_id, date, ticket_type, seat):
        super().__init__()
        events_id = int(events_id)
        attendees_id = int(attendees_id)
        if  events_id in Events.lst:
            if attendees_id in Attendees.lst:       
                id = Registrations.get_id(id)  # Gera um ID automaticamente
                self._id = id 
                self._events_id = events_id
                self._attendees_id = attendees_id
                self._date = datetime.date.fromisoformat(date) #if isinstance(date, str) else date
                self._ticket_type = ticket_type
                self._seat = seat
                
            else:
                print('Attendees ', attendees_id, ' not found')
        else:
            print('Events ', events_id, ' not found')

        # Armazena no dicionário de objetos
        Registrations.obj[id] = self
        Registrations.lst.append(id)

    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # name property getter method
    @property
    def events_id(self):
        return self._events_id
    @events_id.setter
    def events_id(self, events_id):
        if events_id in Events.lst:
            self._events_id = events_id
        else:
            print('Events ', events_id, ' not found') 
    # product property getter method
    @property
    def attendees_id(self):
        return self._attendees_id
    @attendees_id.setter
    def attendees_id(self, attendees_id):
        if attendees_id in Attendees.lst:
            self._attendees_id = attendees_id
        else:
            print('Attendees ', attendees_id, ' not found') 
    @property
    def date(self):
        return self._date
    # date property setter method
    @date.setter
    def date(self, date):
        self._date = date
    @property
    def seat(self):
        return self._seat
    @seat.setter
    def seat(self, seat):
        self._seat = seat
    # dob property getter method
    @property
    def ticket_type(self):
        return self._ticket_type
    # dob property setter method
    @ticket_type.setter
    def ticket_type(self, ticket_type):
        self._ticket_type = ticket_type
    
    
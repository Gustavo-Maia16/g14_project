"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
# from classes.gclass import Gclass
# import datetime
# class Registrations(Gclass):
#     obj = dict()
#     lst = list()
#     pos = 0
#     sortkey = ''
#     # Attribute names list, identifier attribute must be the first one and callled 'id'
#     att = ['_id','_seat','_ticket_type']
#     # Class header title
#     header = 'Registrations'
#     # field description for use in, for example, input form
#     des = ['Date','Seat', 'Type of ticket']
#     # Constructor: Called when an object is instantiated
#     def __init__(self, date, seat, ticket_type):
#         super().__init__()
#         # Object attributes
#         date = Registrations.get_id(date)
#         self._id = datetime.date.fromisoformat(date)
#         self._seat = seat
#         self._ticket_type = ticket_type
#         # Add the new object to the dictionary of objects
#         Registrations.obj[date] = self
#         # Add the id to the list of object ids
#         Registrations.lst.append(date)

from classes.gclass import Gclass
import datetime

class Registrations(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id', '_date', '_ticket_type', '_seat']
    header = 'Registrations'
    des = ['Date', 'Ticket Type', 'Seat']

    def __init__(self, id, date, ticket_type, seat):
        super().__init__()
        id = Registrations.get_id(0)  # Gera um ID automaticamente
        self._id = id 
        self._date = datetime.date.fromisoformat(date) #if isinstance(date, str) else date
        self._ticket_type = ticket_type
        self._seat = seat

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
    
    
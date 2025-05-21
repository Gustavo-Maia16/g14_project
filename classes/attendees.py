"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Attendees(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_email']
    # Class header title
    header = 'Attendees'
    # field description for use in, for example, input form
    des = ['Id','Name','Email']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name,email):
        super().__init__()
        # Object attributes
        id = Attendees.get_id(id)
        self._id = id
        self._email = email
        self._name = name
        # Add the new object to the dictionary of objects
        Attendees.obj[id] = self
        # Add the id to the list of object ids
        Attendees.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def email(self):
        return self._email
    # dob property setter method
    @email.setter
    def email(self, email):
        self._email = email
    

"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Events(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_edate']
    # Class header title
    header = 'Events'
    # field description for use in, for example, input form
    des = ['Id','Name','Date']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, edate):
        super().__init__()
        # Object attributes
        id = Events.get_id(id)
        self._id = id
        self._name = name
        self._edate = datetime.date.fromisoformat(edate)
        # lista = edate.split("-")
        # self._edate = datetime.date(int(lista[0]), int(lista[1]), int(lista[2]))
        # Add the new object to the dictionary of objects
        Events.obj[id] = self
        # Add the id to the list of object ids
        Events.lst.append(id)
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
    # edate property getter method
    @property
    def edate(self):
        return self._edate
    # edate property setter method
    @edate.setter
    def edate(self, edate):
        self._edate = edate



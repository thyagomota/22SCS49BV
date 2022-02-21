from datetime import datetime
import json 

def get_json(obj):
    """Returns a JSON from a given object."""
    return json.loads(json.dumps(obj, default=lambda o: getattr(o,'__dict__', str(o))))

class User:
    """Models a user object."""

    def __init__(self, email, name, creation, salt, password, token='', expiration=None): 
        self.email = email
        self.name = name 
        self.creation = creation
        self.salt = salt 
        self.password = password 
        self.token = token 
        self.expiration = expiration if expiration else ''

class Instructor: 
    """Models an instructor object."""

    def __init__(self, email, name, title='', office='', hours=''):
        self.email = email 
        self.name = name 
        self.title = title if title else ''
        self.office = office if office else ''
        self.hours = hours if hours else ''

class Section: 
    """Models a course section object."""

    def __init__(self, crn, section, semester, year, instructor, times='', start='', end='', location='', campus=''):
        self.crn = crn 
        self.section = section 
        self.semester = semester 
        self.year = year 
        self.instructor = instructor 
        self.times = times if times else ''
        self.start = start if start else ''
        self.end = end if end else ''
        self.location = location if location else ''
        self.campus = campus if campus else ''

class Course: 
    """Models a course object."""

    def __init__(self, prefix, number, title, description, credits, prereqs=''):
        self.prefix = prefix 
        self.number = number 
        self.title = title 
        self.description = description 
        self.credits = credits
        self.prereqs = prereqs if prereqs else ''
    
    def add_section(self, section):
        """Adds a section to the list of course sections."""
        if 'sections' not in self.__dict__:
            self.sections = []
        self.sections.append(section)

    def __eq__(self, other):
        """Returns true/false depending whether the (current) course is equal to a given one."""
        return self.prefix == other.prefix and self.number == other.number


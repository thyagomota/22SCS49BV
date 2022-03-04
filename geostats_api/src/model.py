import json 

def get_json(obj):
    """Returns a JSON from a given object."""
    return json.loads(json.dumps(obj, default=lambda o: getattr(o,'__dict__', str(o))))

class Region:
    """Models a Region object."""

    def __init__(self, code, name): 
        self.code = code
        self.name = name 

    def add_division(self, division):
        """Adds a division to a region."""
        if 'divisions' not in self.__dict__:
            self.divisions = []
        self.divisions.append(division)

    def __eq__(self, other):
        """Returns true/false depending whether the (current) region is equal to a given one."""
        return isinstance(other, Region) and self.code == other.code
        
class Division:
    """Models a Division object."""

    def __init__(self, code, name, region=None): 
        self.code = code
        self.name = name
        if region:
            self.region = region

    def add_state(self, state):
        """Adds a state to a divison."""
        if 'states' not in self.__dict__:
            self.states = []
        self.states.append(state)

    def __eq__(self, other):
        """Returns true/false depending whether the (current) division is equal to a given one."""
        return isinstance(other, Division) and self.code == other.code
        
class State: 
    """Models a State object"""

    def __init__(self, code, name, postal, population, division=None):
        self.code = code 
        self.name = name 
        self.postal = postal 
        self.population = population 
        if division: 
            self.division = division

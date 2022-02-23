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

    def __init__(self, code, name): 
        self.code = code
        self.name = name
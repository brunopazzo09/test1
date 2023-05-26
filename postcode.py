class Postcode:
    def __init__(self, code):
        self.code = code
        self.properties = set()

    def __eq__(self, other):
        if isinstance(other, Postcode):
            return self.code == other.code
        return False

    def __hash__(self):
        return hash(self.code)

    def __str__(self):
        return f"Postcode: {self.code}, Properties: {len(self.properties)}"

    def add_property(self, property):
        self.properties.add(property)
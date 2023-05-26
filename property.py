class Property:
    def __init__(self, property_type, old_new, paon, saon, street, locality, town_city, district, county, postcode):
        self.property_type = property_type
        self.old_new=old_new
        self.paon=paon
        self.saon=saon
        self.street=street
        self.locality=locality
        self.town_city=town_city
        self.district=district
        self.county=county
        self.postcode=postcode
        self.unique_id=f"{paon}_{saon}_{street}_{locality}_{town_city}_{district}"

    def __eq__(self, other):
        if isinstance(other, Property):
            return self.unique_id == other.unique_id
        return False

    def __hash__(self):
        return hash(self.unique_id)

    def __str__(self):
        return f"Property Type: {self.property_type}\n" \
               f"Old/New: {self.old_new}\n" \
               f"PAON: {self.paon}\n" \
               f"SAON: {self.saon}\n" \
               f"Street: {self.street}\n" \
               f"Locality: {self.locality}\n" \
               f"Town/City: {self.town_city}\n" \
               f"District: {self.district}\n" \
               f"Postcode: {self.postcode}\n" \
               f"County: {self.county}\n" \
               f"Unique ID: {self.unique_id}"
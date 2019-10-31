AMENITIES_LIST = ['Basketball', 'Play Field', 'Laundry Room', 'Store', 'Clubhouse', 'Playground', 'Exercise Equipment', 'Soccer Field', 'Swimming Pool', 'Community Room', 
                  'Convenience Store', 'Park', 'Fishing Pond', 'Gated Community']

class Utility:
  def __init__(self, included_in_rent, value, description):
    self.included_in_rent = included_in_rent
    self.value = value
    self.description = description

class Utilities:
  def __init__(self, water, sewer, trash, cable, lawn):
    self.water = water
    self.sewer = sewer
    self.trash = trash
    self.cable = cable
    self.lawn = lawn 

class Property:
  def __init__(self, name, address, city, state, zip_code, phone_number, email,
    age_range, ownership, jlt_notes, number_of_units, amenities, utilities, rents):
    self.name = name
    self.address = address
    self.city = city
    self.state = state
    self.zip = zip_code
    self.phone = phone_number
    self.email = email
    self.age_range = age_range
    self.ownership = ownership
    self.jlt_notes = jlt_notes
    self.number_of_units = number_of_units
    self.amenities = amenities
    self.utilities = utilities
    self.rents = rents
    

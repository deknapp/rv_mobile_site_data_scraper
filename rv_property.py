AMENITIES_LIST = ['Basketball', 'Play Field', 'Laundry Room', 'Store', 'Clubhouse', 'Playground', 'Exercise Equipment', 'Soccer Field', 'Swimming Pool', 'Community Room', 
                  'Convenience Store', 'Park', 'Fishing Pond', 'Gated Community']


class Property:
  def __init__(name, address, city, state, zip_code, phone_number, email,
    age_range, ownership, jlt_notes, number_of_units, amenities, utilities, market_rent, adjusted_rent):
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
    self.market_rent = market_rent
    self.adjusted_rent = adjusted_rent
    


class CatchmentLocation:
    location_id = ''
    location_name = ''
    parent_location = ''

    def __init__(self, location_id, location_name, parent_location):
        self.location_id = location_id
        self.location_name = location_name
        self.parent_location = parent_location

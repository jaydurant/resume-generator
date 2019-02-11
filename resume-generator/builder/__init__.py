class Resume(object):

    def __init__(self):
        self._document = None
        self._email = ''
        self._first_name = ''
        self._middle_name = ''
        self._last_name = ''
        self._address_street = ''
        self._address_state = ''
        self._address_suite = ''
        self._address_state = ''
        self._address_country=''
        self._address_zipcode=''
        self._summary=''
        self._experience=[]
        self._education=[]
        self._awards=[]

    def email(self, value):
        self._email = value
        return self

    def first_name(self, value):
        self._first_name = value
        return self
    
    def middle_name(self, value):
        self._middle_name = value
        return self

    def last_name(self, value):
        self._last_name = value
        return self
    
    def address_street(self, value):
        self._address_street = value
        return self
    
    def address_state(self, value):
        self._address_state = value
        return self
    
    def address_suite(self, value):
        self._address_suite = value
        return self
    
    def address_country(self, value):
        self._address_country = value
        return self

    def address_zipcode(self, value):
        self._address_zipcode = value
        return self
    
    def summary(self, value):
        self._summary = value
        return self
    
    def experience(self, value):
        self._experience = value
        return self
    
    def education(self, value):
        self._education = value
        return self
    
    def awards(self, value):
        self._awards = value
        return self
    
    def build(self):
        pass
    
    def save(self, file_name):
        self._document.save(file_name)

    def _build_name(self, first_name, middle_name, last_name):
        name = ''
        if self._first_name:
            name = self._first_name.capitalize()

        if self._middle_name:
            name = name + ' '  + self._middle_name.capitalize()
        
        if self._last_name:
            name = name + ' ' + self._last_name
        
        return name
        

builders = {}
class ResumeBuilder(object):
    
    def __init__(self, builder_type):

        if builder_type in builders:
            self.builder = builders[builder_type]
        else:
            self.builder = None
        

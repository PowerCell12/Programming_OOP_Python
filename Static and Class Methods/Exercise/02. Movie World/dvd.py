import calendar

class DVD:

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod #wrong
    def from_date(cls, id, name, date, age_restriction):

        dates = date.split(".")

        return cls(name, id, int(dates[2]), calendar.month_name[int(dates[1])], age_restriction)
    

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
class Course:
    def __init__(self, course_number=0, course_name="", credit_hrs=0, grades=0):
        self.course_number = course_number
        self.course_name = course_name
        self.credit_hrs = credit_hrs
        self.grades = grades

    def number(self):
        return int(self.course_number)

    def name(self):
        return str(self.course_name)

    def credit_hr(self):
        return float(self.credit_hrs)

    def grade(self):
        return float(self.grades)

    def __str__(self):
        return f"cs{self.course_number} {self.course_name} Grade: {self.grades:0.1f} " \
               f"Credit Hours: {self.credit_hrs:0.1f}"

    # needs next variable?

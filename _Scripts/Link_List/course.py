class Course:
    def __init__(self, course_number: int = 0, course_name: str = "",
                 credit_hrs: float = 0.0, grades: float = 0.0, next=None):
        if type(course_number) == int and course_number >= 0:
            self.course_number = course_number
        else:
            raise ValueError
        if type(course_name) == str:
            self.course_name = course_name
        else:
            raise ValueError
        if type(credit_hrs) == float and credit_hrs >= 0:
            self.credit_hrs = credit_hrs
        else:
            raise ValueError
        if type(grades) == float and grades >= 0:
            self.grades = grades
        else:
            raise ValueError

        self.next = next

    def number(self):
        return int(self.course_number)

    def name(self):
        return str(self.course_name)

    def credit_hr(self):
        return float(self.credit_hrs)

    def grade(self):
        return float(self.grades)

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return f"cs{self.course_number} {self.course_name} Grade: {self.grades:0.1f} " \
               f"Credit Hours: {self.credit_hrs:0.1f}"

from course import Course
from courselist import CourseList


def main():
    with open("data.txt") as DATA_FILE:
        data_lyst = [x.strip().split(",") for x in DATA_FILE.readlines()]
    course_list = CourseList()
    for i in data_lyst:
        current_course = Course(course_number=int(i[0]), course_name=i[1], credit_hrs=float(i[2]), grades=float(i[3]))
        course_list.insert(current_course)

    print(f"Current List: ({course_list.size()})")
    print(course_list)
    print("\n")
    gpa = course_list.calculate_gpa()
    print(f"Cumulative GPA: {gpa:.3f}")


if __name__ == "__main__":
    main()

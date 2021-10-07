from course import Course
from courselist import CourseList


def main():
    with open("data.txt") as DATA_FILE:
        data_lyst = [x.strip().split(",") for x in DATA_FILE.readlines()]
    course_list = CourseList()
    for i in data_lyst:
        current_course = Course(course_number=int(i[0]), course_name=i[1], credit_hrs=float(i[2]), grades=float(i[3]))
        course_list.insert(current_course)

    print("original")
    print(course_list)

    # course_list.remove(1400)
    #
    # print("remove 1400")
    # print(course_list)

    course_list.insert(Course(1400, "one", 1.0, 1.0))
    course_list.insert(Course(1400, "two", 1.0, 1.0))

    print("insert 2 1400")
    print(course_list)

    course_list.remove_all(1400)

    print("remove all 1400")
    print(course_list)


if __name__ == "__main__":
    main()

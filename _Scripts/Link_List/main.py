from course import Course
from courselist import CourseList


def main():
    with open("data.txt") as DATA_FILE:
        data_lyst = [x.strip().split(",") for x in DATA_FILE.readlines()]

    print(data_lyst[0][2])
    for i in data_lyst:
        Course(course_number=i[0])


if __name__ == "__main__":
    main()

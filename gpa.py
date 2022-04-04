def mark_to_gpa(mark):
    if mark >= 85:
        return 4
    elif (mark>=80 and mark <85):
        return 3.7
    elif (mark >= 77 and mark < 80):
        return 3.3
    elif (mark >=73 and mark <77):
        return 3.0
    elif (mark >=70 and mark <73):
        return 2.7
    elif (mark >=67 and mark <70):
        return 2.3
    elif (mark >=63 and mark <67):
        return 2.0
    elif (mark >=60 and mark <63):
        return 1.7
    elif (mark >=57 and mark <60):
        return 1.3
    elif (mark >=53 and mark <57):
        return 1.0
    elif (mark >=50 and mark <53):
        return 0.7
    else:
        return 0

def add_course_info(all_courses):
    course_name = input("Please enter a course: ")
    mark = int(input("Please enter your mark: "))
    gpa = mark_to_gpa(mark)
    all_courses.append([course_name, gpa])
    return all_courses

def calculate_avg_gpa(all_courses):
    total = 0

    courses = len(all_courses)
    for course in all_courses:
        total +=course[1]

    return total/courses

def ask_for_marks():
    all_courses = []
    num_courses = int(input("Please enter the number of courses you have: "))
    discipline = input("Please enter your discipline: ")
    for i in range(num_courses):
        all_courses = add_course_info(all_courses)

    avg_gpa = calculate_avg_gpa(all_courses)
    terminal_output(all_courses, discipline,avg_gpa)

def terminal_output(all_courses, discipline,avg_gpa):
    print("Discipline: ", discipline, "Average GPA:", avg_gpa)
    print("Mark Break Down:")
    for i in range (len(all_courses)):
        print("Course: ", all_courses[i][0], "GPA: ",all_courses[i][1])
    
if __name__ == "__main__":
    ask_for_marks()
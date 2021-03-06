import json


def load_breakdown_grades():
    with open('general_Setup.json') as data_file:
        course = json.load(data_file)
    breakdown = course['cSetup']['breakdown']
    return breakdown


def load_general_grades():
    try:
        new = open("general_grades.json", "r+")
        if new.readlines() == [ ]:
            new.write("( )")
            new.close()

        with open("general_grades.json") as data_file:
            general_grades = json.load(data_file)
    finally:
        new = open("general_grades.json", "w")
        new.write("( )")
        new.close()
    return general_grades


def user_input():
    student_name = raw_input("Student name?   ")
    return student_name


def ask(student_name, grades, student_grades):
    current_grades = {student_name: []}

    for key in grades:
        if student_name in student_grades.keys():
            if student_grades[student_name][key] > -1:
                response = raw_input("Your grade from " + key + " is " + str(student_grades[student_name][key]) + ". Change your grade for " + key + "?" + " Please write yes or no.")
            if response == 'yes':
                new_grade = input("please input new grade")
                if new_grade <= 100 and new_grade >= 0:
                    response['totalgrades'][key] = new_grade
                else:
                    response['totalgrades'][key] = input('Please input a grade between 0 and 100')

        else:
            theanswer = int(raw_input("please input your grade of " + key + " or type -1 (if no grade)"))
            if (theanswer >= 0) and (theanswer <= 100) or (theanswer == -1):
                current_grades[student_name][key] = theanswer
    return current_grades


def remember(updated_data):
    print (json.dumps(updated_data))
    file = open("general_grades.json", "w")
    file.write(json.dumps(updated_data))
    file.close()


def print_Current_Grade(grades, grade_now):
    grade = 0.0
    for key in grade_now["totalgrades"]:
        if grade_now["totalgrades"][key] != -1:
            total = float(grade_now["totalgrades"][key]) * grades[key] / 100
            grade = grade + total
    return grade


def load_conversion_matrix():
    with open('general_Setup.json') as data_file:
        general_Setup = json.load(data_file)
        conversionmatrix = general_Setup['cSetup']['conversionmatrix']
    return conversionmatrix


def print_message(grade,conversionmatrix):
    for z in range(len(conversionmatrix)):
        if int(conversionmatrix[z]["max"]) >= int(grade) and int(conversionmatrix[z]["min"]) <= int(grade):
            print "now your current grade is" + str(grade) + " & mark for it is " + str(conversionmatrix[z]["mark"])


def main():
    breakdown = load_breakdown_grades()
    general_grades = load_general_grades()
    student_name = user_input()
    updateddata = (general_grades)
    remember(updateddata)
    grade = print_Current_Grade(breakdown, updateddata)
    conversionmatrix = load_conversion_matrix()
    print_message(grade,conversionmatrix)


main()

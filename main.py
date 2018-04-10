import json


def load_breakdown_grades():
    with open('general_Setup.json') as data_file:
        course = json.load(data_file)
    breakdown = course['cSetup']['breakdown']
    return breakdown


def load_general_grades():
    with open('general_grades.json') as data_file:
        general_grades = json.load(data_file)
    return general_grades


def replacement(general_grades):
    for key in general_grades['totalgrades']:
        print"From now, your grade for " + key + 'has a value ' + str(general_grades['totalgrades'][key])
        x = raw_input('if change type yes, otherwise no')
        if x == 'yes':
            new_grade = input('So, what is your grade now???')
            if new_grade <= 100 and new_grade >= 0:
                general_grades['totalgrades'][key] = new_grade
            else:
                general_grades['totalgrades'][key] = input('Please input a grade between 0 and 100')
    return general_grades


def remember(updated_data):
    print (json.dumps(updated_data))
    file = open("general_grades.json")
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
    updateddata = replacement(general_grades)
    remember(updateddata)
    grade = printCurrentGrade(breakdown, updateddata)
    conversionmatrix = loadconversionmatrix()
    print_message(grade,conversionmatrix)
    
main()


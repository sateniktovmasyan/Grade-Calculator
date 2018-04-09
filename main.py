import json
def loadbreakdowngrades():


    with open ('general_Setup.json') as Data1:
        course = json.load(Data1)
    breakdown = course['cSetup']['breakdown']
    return breakdown

def loadgeneral_grades():
    with open ('general_grades.json') as Data2:
        general_grades = json.load(Data2)
        return general_grades

def replacement(general_grades):
    for key in general_grades['totalgrades']:
        print"From now, your grade for " + key + 'has a value '+ str(general_grades['totalgrades'][key])
        x = raw_input('if change type yes, otherwise no')
    if x == str('yes'):
                general_grades['totalgrades'][key] = input('So, what is your grade now???')
                return general_grades

def remember(updateddata):
    print (json.dumps(updateddata))
    file = open("general_grades.json")
    file.write(json.dumps(updateddata))
    file.close()

def printCurrentGrade(grades, grade_now):
    grade = 0
    for key in grade_now["totalgrades"]:
        if grade_now["totalgrades"][key] != -1:
            total = int(grade_now["totalgrades"][key]) * grades[key] / 100
            grade = grade + total
    return (grade)

def loadconversionmatrix():
    with open ('general_Setup.json') as Data:
        general_Setup = json.load(Data)
        conversionmatrix = general_Setup['cSetup']['conversionmatrix']
    return conversionmatrix

def printMessage(grade,conversionmatrix):
    for z in range(len(conversionmatrix)):
        if int(conversionmatrix[z]["max"]) >= int(grade) and int(conversionmatrix[z]["min"]) <= int(grade):
            print "now your current grade is" + str(grade) + " & mark for it is " + str(conversionmatrix[z]["mark"])

def main():
    breakdown = loadbreakdowngrades()
    general_grades = loadgeneral_grades()
    updateddata = replacement(general_grades)
    remember(updateddata)
    grade = printCurrentGrade(breakdown, updateddata)
    conversionmatrix = loadconversionmatrix()
    printMessage(grade,conversionmatrix)

main()

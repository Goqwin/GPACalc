#Godwin JB Mercado UCID:30087899 CPSC  217 T04
#Mini-Assignment 1

tg = float(input("Please input your term grade point (0-4.3):"))

def calculate_gpa(tg):
    if tg > 4.3 or tg < 0:
        print("Invalid grade point entered.")
    elif tg >= 4.04:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "A+"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 3.85:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "A"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 3.5:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "A-"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 3.15:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "B+"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 2.85:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "B"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 2.5:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "B-"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 2.15:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "C+"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 1.85:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "C"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 1.5:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "C-"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 1.15:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "D+"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    elif tg >= 0.85:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "D"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)
    else:
        format_gradepoint = "{:.1f}".format(tg)
        letter_grade = "F"
        print("Term GPA:", format_gradepoint, "Term letter:", letter_grade)

calculate_gpa(tg)
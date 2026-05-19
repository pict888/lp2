# Expert System - Hospital Diagnosis

print("=" * 50)
print("        HOSPITAL EXPERT SYSTEM")
print("=" * 50)

score = 0

# Inputs
temp = float(input("\nEnter Body Temperature: "))

oxygen = int(input("Enter Oxygen Level: "))

heart = int(input("Enter Heart Rate: "))

cough = input("Do you have cough? (yes/no): ")

breathing = input("Breathing problem? (yes/no): ")

headache = input("Do you have headache? (yes/no): ")

weakness = input("Do you feel weakness? (yes/no): ")


# Temperature
if temp >= 103:
    score += 30

elif temp >= 100:
    score += 15


# Oxygen
if oxygen < 90:
    score += 40

elif oxygen < 95:
    score += 20


# Heart Rate
if heart > 120:
    score += 25

elif heart > 100:
    score += 10


# Symptoms
if cough == "yes":
    score += 15

if breathing == "yes":
    score += 35

if headache == "yes":
    score += 10

if weakness == "yes":
    score += 10


print("\n" + "=" * 50)
print("Health Score =", score)
print("=" * 50)


# Diagnosis
if temp >= 100 and cough == "yes" and breathing == "yes":

    print("Possible Disease : COVID / Lung Infection")

    print("Advice : Visit Hospital Immediately")


elif temp >= 100 and headache == "yes":

    print("Possible Disease : Viral Fever")

    print("Advice : Take Medicines and Rest")


elif cough == "yes" and weakness == "yes":

    print("Possible Disease : Common Cold")

    print("Advice : Drink Warm Water and Rest")


elif oxygen < 90:

    print("Possible Disease : Respiratory Problem")

    print("Advice : Emergency Medical Attention Required")


else:

    print("Possible Disease : Mild Symptoms")

    print("Advice : Stay Hydrated and Monitor Health")

'''
# Expert System - Employee Performance Management
# Artificial Intelligence Practical

print("=" * 60)
print("     EXPERT SYSTEM : EMPLOYEE PERFORMANCE MANAGEMENT")
print("=" * 60)

# ----------------------------------------------------------
# THRESHOLDS
# ----------------------------------------------------------
# Score 0  - 25  : EXCELLENT
# Score 26 - 50  : GOOD
# Score 51 - 70  : AVERAGE
# Score 71 - 85  : POOR
# Score 86 - 100 : CRITICAL PERFORMANCE
# ----------------------------------------------------------

def get_verdict(score):

    if score <= 25:
        return (
            "EXCELLENT PERFORMANCE",
            "Employee is performing exceptionally well.\n"
            "Eligible for promotion and bonus."
        )

    elif score <= 50:
        return (
            "GOOD PERFORMANCE",
            "Employee performance is good.\n"
            "Minor improvements can increase productivity."
        )

    elif score <= 70:
        return (
            "AVERAGE PERFORMANCE",
            "Employee performance is average.\n"
            "Training and guidance are recommended."
        )

    elif score <= 85:
        return (
            "POOR PERFORMANCE",
            "Employee performance is below expectations.\n"
            "Performance improvement plan required."
        )

    else:
        return (
            "CRITICAL PERFORMANCE",
            "Employee performance is critically low.\n"
            "Immediate action and strict monitoring required."
        )

# ----------------------------------------------------------
# EMPLOYEE CHECK
# ----------------------------------------------------------

def employee_check():

    score = 0
    issues = []

    print("\n" + "-" * 60)
    print("           EMPLOYEE PERFORMANCE ANALYSIS")
    print("-" * 60)

    # Attendance
    attendance = int(input("\nEnter Attendance Percentage: "))

    if attendance < 50:
        score += 35
        issues.append("Very Low Attendance")

    elif attendance < 75:
        score += 20
        issues.append("Low Attendance")

    # Task Completion
    task = int(input("Enter Task Completion Percentage: "))

    if task < 40:
        score += 30
        issues.append("Very Low Task Completion")

    elif task < 70:
        score += 15
        issues.append("Low Task Completion")

    # Communication Skills
    communication = int(input("Enter Communication Skill Rating (1-10): "))

    if communication <= 3:
        score += 20
        issues.append("Poor Communication Skills")

    elif communication <= 6:
        score += 10
        issues.append("Average Communication Skills")

    # Teamwork
    teamwork = int(input("Enter Teamwork Rating (1-10): "))

    if teamwork <= 3:
        score += 20
        issues.append("Poor Teamwork")

    elif teamwork <= 6:
        score += 10
        issues.append("Average Teamwork")

    # Punctuality
    punctuality = int(input("Enter Punctuality Rating (1-10): "))

    if punctuality <= 3:
        score += 15
        issues.append("Poor Punctuality")

    elif punctuality <= 6:
        score += 8
        issues.append("Average Punctuality")

    score = min(score, 100)

    return score, issues

# ----------------------------------------------------------
# RESULT
# ----------------------------------------------------------

def show_result(score, issues):

    status, desc = get_verdict(score)

    print("\n" + "=" * 60)
    print("                  FINAL REPORT")
    print("=" * 60)

    print("Performance Score :", score, "/100")

    print("\nSTATUS :", status)

    print("\nDESCRIPTION :")
    print(desc)

    print()

    if issues:

        print("ISSUES DETECTED :")

        for i, issue in enumerate(issues, 1):
            print(str(i) + ".", issue)

    else:
        print("No issues detected.")

    print("=" * 60)

# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------

while True:

    print("\n1. Evaluate Employee")
    print("2. Exit")

    ch = input("\nEnter Choice : ")

    if ch == "1":

        score, issues = employee_check()

        show_result(score, issues)

    elif ch == "2":

        print("\nExiting Program...")
        break

    else:
        print("Invalid Choice")
        
'''

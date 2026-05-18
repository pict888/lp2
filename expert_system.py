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

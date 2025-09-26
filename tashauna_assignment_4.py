student_name = "Tashauna Ruffin"
current_gpa = 2.8
study_hours = 26
social_points = 10
stress_level = 65 

print(f"Welocme! \nName:{student_name} \nCurrent GPA: {current_gpa} \nStudy hours:{study_hours} \nSocial Points: {social_points} \nStress Level:{stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa < 2.5:
        study_hours += 5
        stress_level -= 5
    else:
        study_hours += 2
        stress_level -= 2
elif choice == "B":
    if current_gpa < 3.0:
        study_hours += 8
        stress_level += 10
    else:
        study_hours += 5
        stress_level += 5
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 10
    else:
        study_hours += 15
        stress_level += 20
else:
    print("Invalid input")


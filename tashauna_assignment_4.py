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


study_options = ["Programming", "Math", "English", "History"]

study_choice = input("Choose a subject to focus on: ")

if study_choice in study_options:
    if study_choice == "Programming" or study_choice == "programming":
        current_gpa += 0.3
        social_points -= 10
        print("You dived deep into Programming. GPA jumped up, but you missed social events.")
    elif study_choice == "Math" or study_choice == "math":
        current_gpa += 0.2
        social_points -= 5
        print("Math improved your logic and GPA, with a slight drop in social points.")
    elif study_choice == "English" or study_choice == "english":
        current_gpa += 0.1
        social_points += 10
        print("English improved your writing and helped your social engagement.")
    elif study_choice == "History" or study_choice == "history":
        if stress_level > 60:
            current_gpa += 0.05
            stress_level -= 10
            print("History helped you relax and reduce stress.")
        else:
            current_gpa += 0.1
            social_points += 5
            print("History added knowledge and boosted your social points.")
elif study_choice not in study_options:
    print("Invalid subject choice. Please pick from the list.")
    

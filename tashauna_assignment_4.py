student_name = "Tashauna Ruffin"
current_gpa = 3.2
study_hours = 26
social_points = 75
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

ending = ""
if type(current_gpa) is float and type(social_points)is not int:
    if current_gpa >= 3.5:
        if stress_level <= 50:
            ending = "You made Dean's list and stayed semi stress free!"
        else:
            ending = "You made Dean's list but was academically burnt out"
    elif current_gpa >= 2.0:
        if social_points >= 50:
            ending = "You passed! and had fun!"
        else:
            ending = "You passed! But missed all the fun"
    else:
        ending = "Something went wrong and you are on academic probation"
else:
    print("Error: GPA is not a float or social points is not a integer")

    

print("\n=== Final Results ===")
print(f"GPA:{round(current_gpa,2)}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print(f"Your ending: {ending}")
    

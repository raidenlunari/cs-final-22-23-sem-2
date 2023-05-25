def calculate_letter_grade(average_score):
    if average_score >= 97:
        return 'A+'
    elif average_score >= 93:
        return 'A'
    elif average_score >= 90:
        return 'A-'
    elif average_score >= 87:
        return 'B+'
    elif average_score >= 83:
        return 'B'
    elif average_score >= 80:
        return 'B-'
    elif average_score >= 77:
        return 'C+'
    elif average_score >= 73:
        return 'C'
    elif average_score >= 70:
        return 'C-'
    elif average_score >= 67:
        return 'D+'
    elif average_score >= 63:
        return 'D'
    elif average_score >= 60:
        return 'D-'
    else:
        return 'F'
#the function above makes my life a lot easier as it shows the students grade is (as a letter)
#below i am assigning variables
classes = ['class1', 'class2', 'class3']
students = ['student1', 'student2', 'student3', 'student4', 'student5']
assignments = ['assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6']
scores = [0] * len(assignments)

while True:
    class_choice = int(input("Which class would you like to access? (1-3) "))
    if class_choice < 1 or class_choice > 3:
         #the following happens when a teacher puts the wrong syntax and the program does nott understand
        print("Invalid selection. Please select a valid class.")
        continue

    class_name = classes[class_choice - 1]
#this lets the teacher decide which students grade tthey would like to view/edit/enter
    student_choice = int(input("Which student would you like to access? (1-5) "))
    if student_choice < 1 or student_choice > 5:
        print("Invalid selection. Please select a valid student.")
        continue

    student_name = students[student_choice - 1]

    action_choice = input("Would you like to enter, view, or edit? ")
    if action_choice == "enter":
        assignment_choice = int(input("Which assignment would you like to enter a score for? (1-6) "))
        if assignment_choice < 1 or assignment_choice > 6:
            #the following happens when a teacher puts the wrong syntax and the program does nott understand
            print("Invalid selection. Please select a valid assignment.")
            continue
        #this saves the score that the teacher puts in for the assignment
        score = int(input("Enter a score out of 100: "))
        scores[assignment_choice - 1] = score

    elif action_choice == "view":
        view_choice = input("Would you like to view an assignment or the average? ")
        #the following happens when the teacher chooses to see a specific assignment grade
        if view_choice == "assignment":
            assignment_choice = int(input("Which assignment would you like to view? (1-6) "))
            if assignment_choice < 1 or assignment_choice > 6:
                 #the following happens when a teacher puts the wrong syntax and the program does nott understand
                print("Invalid selection. Please select a valid assignment.")
                continue

            print("Score for", assignments[assignment_choice - 1] + ":", scores[assignment_choice - 1])
 #the following happens when the teacher chooses to see the overall grade
        elif view_choice == "average":
            average_score = sum(scores) / len(scores)
            #this uses the function at the top of the program to calculate the letter grade which is printed below.
            letter_grade = calculate_letter_grade(average_score)
            
            print("Average Score:", average_score)
            print("Letter Grade:", letter_grade)
    #this is for the edit option, so the teacher can change grades that have been inputted
    elif action_choice == "edit":
        edit_choice = int(input("Which assignment would you like to edit? (1-6) "))
         #the following happens when a teacher puts the wrong syntax and the program does nott understand
        if edit_choice < 1 or edit_choice > 6:
            print("Invalid selection. Please select a valid assignment.")
            continue

        new_score = int(input("Enter a new score out of 100: "))
        scores[edit_choice - 1] = new_score

        average_score = sum(scores) / len(scores)
        letter_grade = calculate_letter_grade(average_score)
        print("Average Score:", average_score)
        print("Letter Grade:", letter_grade)
        #the following happens when a teacher puts the wrong syntax and the program does nott understand
    else:
        print("Invalid selection. Please select a valid action.")
        #this continue is here so the teacher can try again
        continue

# i added this so that the teacher is actually prompted whether they want to stop or not, so the program doesnt keep looping and the teacher doesnt have to click the stop button
    done_choice = input("Are you done? (yes/no) ")
    if done_choice.lower() == "yes":
        break



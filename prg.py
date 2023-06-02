def chooseClass():
    '''
        This function is made to identify a class, and takes input from the user.
        It can: check if the class is part of a class list, take an input, and return this class if it's valid
        It does not: return an actual class ID, which will be in another function.
    '''

    global classList

    successChooseClass = 0  # While loop variable

    while successChooseClass == 0:
        classInput = input("Input Class to Enter: ")  # Enters the class from the user
        if classInput in classList:  # Ensures that the class is actually part of the class list
            successChooseClass += 1
            return classInput  # Returns the class which is requested
        else:
            print("Invalid Class. Try again.")  # The class wasn't part of the class list


def chooseDay():
    '''
        This function checks if a day is valid in the range which is specified.
        It can: Check the day, check the type, check the range, return a value
        It cannot: do anything with the day
    '''
    print("The day entered must be a day between 1-30, like day 1, day 2, day 3, day 6 (week 2, day 1), etc.")

    daySuccess = 0

    while daySuccess == 0:  # checks if the day is succeeding and loops if not
        day = input("Input the day: ")  # inputs the day
        if day.isnumeric():  # checks if it's an actual integer
            if int(day) <= 30:  # checks the range
                daySuccess += 1
                return day  # returns a value
            else:
                print("Invalid Day. Day must be between 1 and 30. Try again.")
        else:
            print("Invalid type. Try again.")


def chooseStudent(classInput):
    '''
        This function is made to identify a student, given a class, and takes input from a user
        It can: check if the student is part of a class, is part of the student list, take an input, and return this class if it is valid.
        It does not: return an actual class ID, which will be in another function.
    '''
    global students

    successChooseStudent = 0  # While loop variable
    print("The students which you can pick from are named Student1, Student2, Student3, Student4, and Student5.")

    while successChooseStudent == 0:

        studentInput = input("Input Student to Check: ")  # Enters the student from the user
        if studentInput.lower() in students:
            successChooseStudent += 1
            return studentInput
        else:
            print("Invalid student. Try again.")


def chooseStatus():
    '''
        This function is made to take a status, and takes an input from the user.
        It can: check if the status is part of the valid statuses, take an input, and return a value
        It does not: assign the status to any student
    '''

    successChooseStatus = 0  # While loop variable

    while successChooseStatus == 0:

        print('The attendance statuses are:')  # Informs the student of the different attendances
        print("Absent (A), and Present (P)")
        status = input("Input Status to Place: ")
        if status == "A" or status == "Absent" or status == "absent":  # Checks if input is a variation of absence
            successChooseStatus = 1
            return False  # returns the status
        elif status == "P" or status == "Present" or status == "present":  # Checks if input is a variation of presence
            successChooseStatus = 1
            return True  # returns the status
        else:
            print("Invalid Response. Try again.")  # Inputted attendance was not part of the attendance


def setStudentID(classInput, day, student):
    '''
        This function creates and finds and ID for a student based on the class, week, day, and student.
        It creates an ID such as 1323 in the order of class, week, day, and finally student.
        For example, above, this ID would mean 1st class (Precalculus), Week 3, Day 2, Student 3 (Precalc3)

        It can: take three different inputs, independently generate an ID, check for validity of inputs, return a value
        It cannot: find the three different inputs itself, do anything with the student ID
        It is: only capable of sorting through classInputs, days, and students which actually exist (will print error otherwise)
    '''

    def findFirstID():  # Finds the first ID of the student (class)
        if classInput == 'Precalculus':
            return '1'
        elif classInput == 'Biology':
            return '2'
        elif classInput == 'Chemistry':
            return '3'

    def findSecondID():  # Finds the second ID of the student (week + day)
        if int(day) > 5 and int(day) % 5 == 0:  # checks if the thing is valid and a special case
            week = (int(day) // 5)
            dayRem = 5
            return str(week)+str(dayRem)
        elif int(day) > 5:  # does the special thing but not for the special case
            week = (int(day) // 5) + 1
            dayRem = int(day) % 5
            return str(week)+str(dayRem)
        else:
            return "1"+str(day)  # if the thing is less than 5, nothing must be done

    def findThirdID():  # Finds the third ID of the student (actual student ID)
        return str(student[7])

    finalID = findFirstID()+findSecondID()+findThirdID()  # combines everything to make one final ID
    return finalID


def editStatus(studentID, status):
    '''
        This function is made to assign a status "status" to a student "studentID" on a certain day "day".
        It can: Take three different inputs, use them to assign a status, sort through days, return an output, sort through nested lists
        It cannot: Do any sorting by itself, find the students by itself, find the status by itself, find the day by itself
        It is: case-sensitive, requires inputs in specific order or else it will return an error print message
    '''

    global studentDetailsPreCalc, studentDetailsBiology, studentDetailsChemistry

    checkID = (int(studentID[3])+(((int(studentID[2])-1)+((int(studentID[1])-1)*5))*5))  # checks the location
    studentStatusPreCalc = studentDetailsPreCalc[checkID-1][1]  # status of the student in precalculus
    studentStatusBiology = studentDetailsBiology[checkID-1][1]  # status of the student in biology
    studentStatusChemistry = studentDetailsChemistry[checkID-1][1]  # status of the student in chemistry

    if studentID[0] == '1':  # checks if the student thing chosen to check was in precalc
        if studentStatusPreCalc:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    elif studentID[0] == '2':  # checks if the student thing chosen to check was in biology
        if studentStatusBiology:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    elif studentID[0] == '3':  # checks if the student thing chosen to check was in chemistry
        if studentStatusChemistry:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    print("The current status of this student on this day is", currentStatus+".")  # prints the status to make sure it should be changed
    doEdit = input("Would you like to change this to your chosen status? (yes/no) or (y/n): ")  # checks if the person wants to change it
    if doEdit == 'yes' or doEdit == 'y' or doEdit == 'Y':  # changes the status based on class
        if studentID[0] == '1':
            studentDetailsPreCalc[checkID-1][1] = status
        elif studentID[0] == '2':
            studentDetailsBiology[checkID-1][1] = status
        elif studentID[0] == '3':
            studentDetailsChemistry[checkID-1][1] = status
    else:  # does nothing if nothing is chosen to be done
        print("Did not do anything.")


def mainAttendance():  # the main function
    '''
        Runs the main function which is everything except finally viewing the details
        Can do: everything except viewing the details
        Cannot do: viewing the details
    '''

    print("This is a program to track the attendance of five students between three classes over 30 days.")
    print("This program will ask you for a class, a day, and a student to set the attendance for.")
    print("There are two types of attendance: present and absent, or True and False.")
    print("The program will tell you what the ID is, which will identify a combination of day, class, and student.")
    print("It will also print the current status of the student and ask you if you want to change it, allowing you to view.")
    print("")
    print("The classes are Precalculus, Biology, and Chemistry. Enter them as they are stated.")
    print("")
    satisfied = 0

    while satisfied == 0:
        classChoose = chooseClass()  # chooses the class
        print("")
        studentChoose = chooseStudent(classChoose)  # chooses the student
        print("")
        dayChoose = chooseDay()  # chooses the day
        print("")
        statusChoose = chooseStatus()  # chooses the status to set
        print("")

        studentID = setStudentID(classChoose, dayChoose, studentChoose)  # sets the student ID
        print("This action's ID is", studentID+".")  # sends the student ID
        editStatus(studentID, statusChoose)
        print("")
        satisfiedInput = input("Are you satisfied with all your decisions? (yes/no) or (y/n): ")  # checks if the person is done yet
        if satisfiedInput == 'yes' or satisfiedInput == 'y' or satisfiedInput == 'Y':
            satisfied += 1  # ends the main
            print("")
        else:
            print("Continuing.")  # continues if not
            print("")


def viewIndividualDetails(studentID):
    '''
        Checks the initial student ID which allows a thing to be printed which is the attendance
        Can: print out an attendance based on a student ID
        Cannot: make the student ID, change attendance, print more than one at once
    '''

    global studentDetailsPreCalc, studentDetailsBiology, studentDetailsChemistry

    checkID = (int(studentID[3])+(((int(studentID[2])-1)+((int(studentID[1])-1)*5))*5))  # basically checks the ID just like in the other function
    studentStatusPreCalc = studentDetailsPreCalc[checkID-1][1]
    studentStatusBiology = studentDetailsBiology[checkID-1][1]
    studentStatusChemistry = studentDetailsChemistry[checkID-1][1]

    if studentID[0] == '1':  # checks if the class is precalculus
        if studentStatusPreCalc:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    elif studentID[0] == '2':  # checks if the class is biology
        if studentStatusBiology:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    elif studentID[0] == '3':  # checks if the class is in chemistry
        if studentStatusChemistry:
            currentStatus = 'present'
        else:
            currentStatus = 'absent'

    print("The current status of this student on this day is", currentStatus+".") # prints the status


def viewDetails():
    '''
        Views the details, can view en masse or just one student
        Can: view the students
        Cannot: actually handle the details, change any more details of the attendance
    '''

    global studentDetailsPreCalc, studentDetailsBiology, studentDetailsChemistry

    satisfiedView = 0

    while satisfiedView == 0:
        doWhat = input("Input v for view individually or m for view all at once: ")  # asks for setting
        print("")
        if doWhat == 'm':
            print("In this output, there will be many brackets filled with two values; a number and a boolean.")  # cool little background info
            print("The number represents class (1, 2, or 3), week (1-6), day (1-5 in the week), and student (1-5)")
            print("Then, True means present, and False means absent.")
            print("By default, all students are absent until proven otherwise.")
            print("")
            print(studentDetailsPreCalc)  # literally just prints the entire precalc list
            print(studentDetailsBiology)  # literally just prints the entire bio list
            print(studentDetailsChemistry)  # literally just prints the entire chem list
            print("Before, each of your actions were given a code. The above is what this code means. Find the code to find the student status.")
            print("")
        elif doWhat == 'v':
            classInputted = chooseClass()  # asks for class
            print("")
            dayInputted = chooseDay()  # asks for day
            print("")
            studentInputted = chooseStudent(classInputted)  # asks for student
            print("")
            studentIDView = setStudentID(classInputted, dayInputted, studentInputted)  # sets the student ID as this
            viewIndividualDetails(studentIDView)  # views the student ID's status
        else:
            print("Invalid response.")  # bad response response

        satisfiedYet = input("Are you satisfied with your choices yet? (yes/no) or (y/n): ")
        if satisfiedYet == 'yes' or satisfiedYet == 'y':
            print("Finished.")
            satisfiedView += 1
        else:
            print("Continuing.")




classList = ('Precalculus', 'Biology', 'Chemistry')  # Class List
students = ('student1', 'student2', 'student3', 'student4', 'student5')

studentDetailsPreCalc = [['1111', False], ['1112', False], ['1113', False], ['1114', False], ['1115', False], ['1121', False], ['1122', False], ['1123', False], ['1124', False], ['1125', False], ['1131', False], ['1132', False], ['1133', False], ['1134', False], ['1135', False], ['1141', False], ['1142', False], ['1143', False], ['1144', False], ['1145', False], ['1151', False], ['1152', False], ['1153', False], ['1154', False], ['1155', False], ['1211', False], ['1212', False], ['1213', False], ['1214', False], ['1215', False], ['1221', False], ['1222', False], ['1223', False], ['1224', False], ['1225', False], ['1231', False], ['1232', False], ['1233', False], ['1234', False], ['1235', False], ['1241', False], ['1242', False], ['1243', False], ['1244', False], ['1245', False], ['1251', False], ['1252', False], ['1253', False], ['1254', False], ['1255', False], ['1311', False], ['1312', False], ['1313', False], ['1314', False], ['1315', False], ['1321', False], ['1322', False], ['1323', False], ['1324', False], ['1325', False], ['1331', False], ['1332', False], ['1333', False], ['1334', False], ['1335', False], ['1341', False], ['1342', False], ['1343', False], ['1344', False], ['1345', False], ['1351', False], ['1352', False], ['1353', False], ['1354', False], ['1355', False], ['1411', False], ['1412', False], ['1413', False], ['1414', False], ['1415', False], ['1421', False], ['1422', False], ['1423', False], ['1424', False], ['1425', False], ['1431', False], ['1432', False], ['1433', False], ['1434', False], ['1435', False], ['1441', False], ['1442', False], ['1443', False], ['1444', False], ['1445', False], ['1451', False], ['1452', False], ['1453', False], ['1454', False], ['1455', False], ['1511', False], ['1512', False], ['1513', False], ['1514', False], ['1515', False], ['1521', False], ['1522', False], ['1523', False], ['1524', False], ['1525', False], ['1511', False], ['1532', False], ['1533', False], ['1534', False], ['1535', False], ['1541', False], ['1542', False], ['1543', False], ['1544', False], ['1545', False], ['1551', False], ['1552', False], ['1553', False], ['1554', False], ['1555', False], ['1611', False], ['1612', False], ['1613', False], ['1614', False], ['1615', False], ['1621', False], ['1622', False], ['1623', False], ['1624', False], ['1625', False], ['1631', False], ['1632', False], ['1633', False], ['1634', False], ['1635', False], ['1641', False], ['1642', False], ['1643', False], ['1644', False], ['1645', False], ['1651', False], ['1652', False], ['1653', False], ['1654', False], ['1655', False]]
studentDetailsBiology = [['2111', False], ['2112', False], ['2113', False], ['2114', False], ['2115', False], ['2121', False], ['2122', False], ['2123', False], ['2124', False], ['2125', False], ['2131', False], ['2132', False], ['2133', False], ['2134', False], ['2135', False], ['2141', False], ['2142', False], ['2143', False], ['2144', False], ['2145', False], ['2151', False], ['2152', False], ['2153', False], ['2154', False], ['2155', False], ['2211', False], ['2212', False], ['2213', False], ['2214', False], ['2215', False], ['2221', False], ['2222', False], ['2223', False], ['2224', False], ['2225', False], ['2231', False], ['2232', False], ['2233', False], ['2234', False], ['2235', False], ['2241', False], ['2142', False], ['2243', False], ['2244', False], ['2245', False], ['2251', False], ['2252', False], ['2253', False], ['2254', False], ['2255', False], ['2311', False], ['2312', False], ['2313', False], ['2314', False], ['2315', False], ['2321', False], ['2322', False], ['2323', False], ['2324', False], ['2325', False], ['2331', False], ['2332', False], ['2333', False], ['2334', False], ['2335', False], ['2341', False], ['2342', False], ['2343', False], ['2344', False], ['2345', False], ['2351', False], ['2352', False], ['2353', False], ['2354', False], ['2355', False], ['2411', False], ['2412', False], ['2413', False], ['2414', False], ['2415', False], ['2421', False], ['2422', False], ['2423', False], ['2424', False], ['2425', False], ['2431', False], ['2432', False], ['2433', False], ['2434', False], ['2435', False], ['2441', False], ['2442', False], ['2443', False], ['2444', False], ['2445', False], ['2451', False], ['2452', False], ['2453', False], ['2454', False], ['2455', False], ['2511', False], ['2512', False], ['2513', False], ['2514', False], ['2515', False], ['2521', False], ['2522', False], ['2523', False], ['2524', False], ['2525', False], ['2511', False], ['2532', False], ['2533', False], ['2534', False], ['2535', False], ['2541', False], ['2542', False], ['2543', False], ['2544', False], ['2545', False], ['2551', False], ['2552', False], ['2553', False], ['2554', False], ['2555', False], ['2611', False], ['2612', False], ['2613', False], ['2614', False], ['2615', False], ['2621', False], ['2622', False], ['2623', False], ['2624', False], ['2625', False], ['2631', False], ['2632', False], ['2633', False], ['2634', False], ['2635', False], ['2641', False], ['2642', False], ['2643', False], ['2644', False], ['2645', False], ['2651', False], ['2652', False], ['2653', False], ['2654', False], ['2655', False]]
studentDetailsChemistry = [['3111', False], ['3112', False], ['3113', False], ['3114', False], ['3115', False], ['3121', False], ['3122', False], ['3123', False], ['3124', False], ['3125', False], ['3131', False], ['3132', False], ['3133', False], ['3134', False], ['3135', False], ['3141', False], ['3142', False], ['3143', False], ['3144', False], ['3145', False], ['3151', False], ['3152', False], ['3153', False], ['3154', False], ['3155', False], ['3211', False], ['3212', False], ['3213', False], ['3214', False], ['3215', False], ['3221', False], ['3222', False], ['3223', False], ['3224', False], ['3225', False], ['3231', False], ['3232', False], ['3233', False], ['3234', False], ['3235', False], ['3241', False], ['3142', False], ['3243', False], ['3244', False], ['3245', False], ['3251', False], ['3252', False], ['3253', False], ['3254', False], ['3255', False], ['3311', False], ['3312', False], ['3313', False], ['3314', False], ['3315', False], ['3321', False], ['3322', False], ['3323', False], ['3324', False], ['3325', False], ['3331', False], ['3332', False], ['3333', False], ['3334', False], ['3335', False], ['3341', False], ['3342', False], ['3343', False], ['3344', False], ['3345', False], ['3351', False], ['3352', False], ['3353', False], ['3354', False], ['3355', False], ['3411', False], ['3412', False], ['3413', False], ['3414', False], ['3415', False], ['3421', False], ['3422', False], ['3423', False], ['3424', False], ['3425', False], ['3431', False], ['3432', False], ['3433', False], ['3434', False], ['3435', False], ['3441', False], ['3442', False], ['3443', False], ['3444', False], ['3445', False], ['3451', False], ['3452', False], ['3453', False], ['3454', False], ['3455', False], ['3511', False], ['3512', False], ['3513', False], ['3514', False], ['3515', False], ['3521', False], ['3522', False], ['3523', False], ['3524', False], ['3525', False], ['3511', False], ['3532', False], ['3533', False], ['3534', False], ['3535', False], ['3541', False], ['3542', False], ['3543', False], ['3544', False], ['3545', False], ['3551', False], ['3552', False], ['3553', False], ['3554', False], ['3555', False], ['3611', False], ['3612', False], ['3613', False], ['3614', False], ['3615', False], ['3621', False], ['3622', False], ['3623', False], ['3624', False], ['3625', False], ['3631', False], ['3632', False], ['3633', False], ['3634', False], ['3635', False], ['3641', False], ['3642', False], ['3643', False], ['3644', False], ['3645', False], ['3651', False], ['3652', False], ['3653', False], ['3654', False], ['3655', False]]


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

def mainGrades():
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


#Start with empty note lists for all classes
class1_notes = [""] * 5
class2_notes = [""] * 5
class3_notes = [""] * 5

#Function to create a new note
def create_note():
    note_number = get_note_number_from_user()  #Get the note number from the user
    note_content = get_note_content_from_user()  #Get the note content from the user
    current_notes[note_number - 1] = note_content  #Update the note in the current_notes list
    print("Note added successfully.")

#Function to edit an existing note
def edit_note():
    note_number = get_note_number_from_user()  #Get the note number from the user
    current_note_content = current_notes[note_number - 1]  #Get the current note content
    print(f"Previous Note Content: {current_note_content}")  #Print previous note content
    note_content = get_note_content_from_user()  #Get the updated note content from the user
    current_notes[note_number - 1] = note_content  #Update the note in the current_notes list
    print("Note edited successfully.")

#Function to view an existing note
def view_note():
    note_number = get_note_number_from_user()  #Get the note number from the user
    note_content = current_notes[note_number - 1]  #Get the note content from the current_notes list
    print(f"Note {note_number}: {note_content}")

#Function to get the note number from the user
def get_note_number_from_user():
    while True:
        try:
            note_number = int(input("Enter note number (1-5): "))  #Prompt user for note number
            if note_number < 1 or note_number > 5:
                raise ValueError
            return note_number
        except ValueError:
            print("Invalid note number. Please try again.")

#Function to get the note content from the user
def get_note_content_from_user():
    note_content = input("Enter note content: ")  #Prompt user for note content
    return note_content

#Main program loop
def mainNotes():
    while True:
        class_choice = input("Select your class (1, 2, or 3): ")  #Prompt user for class choice
        
        if class_choice == "1":
            current_notes = class1_notes  #Set current_notes to class1_notes
            class_name = "Class 1"  
        elif class_choice == "2":
            current_notes = class2_notes  #Set current_notes to class2_notes
            class_name = "Class 2"  
        elif class_choice == "3":
            current_notes = class3_notes  #Set current_notes to class3_notes
            class_name = "Class 3"  
        else:
            print("Invalid class selection. Please try again.")
            continue
        
        print(f"Selected Class: {class_name}")
        
        action_choice = input("Select an action (create, edit, view): ")  #Prompt user for action choice
        
        if action_choice == "create":
            create_note()  #Call create_note function
        elif action_choice == "edit":
            edit_note()  #Call edit_note function
        elif action_choice == "view":
            view_note()  #Call view_note function
        else:
            print("Invalid action selection. Please try again.")
        
        quit_choice = input("Do you want to quit? (y/n): ")
        
        if quit_choice.lower() == "y":
            break  #End the program


def main():
    satisfied = 0
    while satisfied == 0:
        actionChoice = input("Input Attendance (1), Grades (2), Notes (3), or finish (4): ")
        if actionChoice == "1" or actionChoice.lower == "attendance":
            mainAttendance()
            viewDetails()
        elif actionChoice == "2" or actionChoice.lower == "grades":
            mainGrades()
        elif actionChoice == "3" or actionChoice.lower == "notes":
            mainNotes()
        elif actionChoice == "4" or actionChoice.lower == "finish":
            satisfied += 1
        else:
            print("Invalid answer. Try again.")

main()
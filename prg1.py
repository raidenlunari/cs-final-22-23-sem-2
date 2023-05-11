def chooseClass():
    '''
        This function is made to identify a class, and takes input from the user.
        It can: check if the class is part of a class list, take an input, and return this class if it's valid
        It does not: return an actual class ID, which will be in another function.
    '''

    global classList

    successChooseClass = 0  # While loop variable

    while successChooseClass == 0:
        global successChooseClass

        classInput = input("Input Class to Enter: ")  # Enters the class from the user
        if classInput in classList:  # Ensures that the class is actually part of the class list
            successChooseClass = 1
            return classInput  # Returns the class which is requested
        else:
            print("Invalid Class. Try again.")  # The class wasn't part of the class list


def chooseStudent(classInput):
    '''
        This function is made to identify a student, given a class, and takes input from a user
        It can: check if the student is part of a class, is part of the student list, take an input, and return this class if it is valid.
        It does not: return an actual class ID, which will be in another function.
    '''

    global chemStudent
    global bioStudent
    global preCalcStudent

    successChooseStudent = 0  # While loop variable

    while successChooseStudent == 0:
        global successChooseStudent

        studentInput = input("Input Student to Check: ")  # Enters the student from the user
        if classInput == 'Precalculus':  # Checks if the class is Precalculus
            if studentInput in preCalcStudent:  # Checks if the student is actually in Precalculus
                successChooseStudent = 1
                return studentInput  # Returns the student
            else:
                print("Invalid Student. Try again.")  # Student was not in Precalculus
        elif classInput == 'Biology':  # Checks if the class is Biology
            if studentInput in bioStudent:  # Checks if the student is actually in Biology
                successChooseStudent = 1
                return studentInput  # Returns the student
            else:
                print("Invalid Student. Try again.")  # Student was not in Biology
        elif classInput == 'Chemistry':  # Checks if the class is Chemistry
            if studentInput in chemStudent:  # Checks if the student is actually in Chemistry
                successChooseStudent = 1
                return studentInput  # Returns the student
            else:
                print("Invalid Student. Try again.")  # Studnet was not in Chemistry


def chooseStatus():
    '''
        This function is made to take a status, and takes an input from the user.
        It can: check if the status is part of the valid statuses, take an input, and return a value
        It does not: assign the status to any student
    '''

    successChooseStatus = 0  # While loop variable

    while successChooseStatus == 0:
        global successChooseStatus

        print('The attendance statuses are:')  # Informs the student of the different attendances
        print("Unexcused Absence (UA), Excused Absence (EA), Tardy (T), or Present (P)")
        status = input("Input Status to Place: ")
        if status == "UA" or "Unexcused" or "Unexcused Absence":  # Checks if input is a variation of UA
            successChooseStatus = 1
            return status  # returns the status
        elif status == "EA" or "Excused" or "Excused Absence":  # Checks if input is a variation of EA
            successChooseStatus = 1
            return status  # returns the status
        elif status == "T" or "Tardy":  # Checks if input is a variation of T
            successChooseStatus = 1
            return status  # returns the status
        elif status == "P" or "Present":  # Checks if input is a variation of P
            successChooseStatus = 1
            return status  # returns the status
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
        if day > 5:
            week = (day // 5) + 1
            dayRem = day % 5
            return str(week)+str(dayRem)
        else:
            return "1"+str(day)

    def findThirdID():  # Finds the third ID of the student (actual student ID)
        if "Precalc" in student:
            return student[7]
        if "Biology" in student:
            return student[7]
        if "Chemistry" in student:
            return student[9]

    finalID = findFirstID()+findSecondID()+findThirdID()
    return finalID


def editStatus(studentID, status, day):
    '''
        This function is made to assign a status "status" to a student "studentID" on a certain day "day".
        It can: Take three different inputs, use them to assign a status, sort through days, return an output, sort through nested lists
        It cannot: Do any sorting by itself, find the students by itself, find the status by itself, find the day by itself
        It is: case-sensitive, requires inputs in specific order or else it will return an error print message
    '''
    # edits the status for a certain student on a certain day


classList = ('Precalculus', 'Biology', 'Chemistry')  # Class List
preCalcStudent = ('Precalc1', 'Precalc2', 'Precalc3', 'Precalc4', 'Precalc5', 'Precalc6')  # Precalculus Students List
bioStudent = ('Biology1', 'Biology2', 'Biology3', 'Biology4', 'Biology5', "Biology6")  # Biology Students List
chemStudent = ('Chemistry1', 'Chemistry2', 'Chemistry3', 'Chemistry4', 'Chemistry5', 'Chemistry6')  # Chem Students List

studentDetailsPreCalc = ()
studentDetailsBio = ()
studentDetailsChemistry = ()
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

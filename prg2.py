# Initialize empty note lists for all classes
class1_notes = [""] * 5
class2_notes = [""] * 5
class3_notes = [""] * 5

# Function to create a new note
def create_note():
    note_number = get_note_number()  # Get the note number from the user
    note_content = get_note_content()  # Get the note content from the user
    current_notes[note_number - 1] = note_content  # Update the note in the current_notes list
    print("\033[94mNote added successfully.\033[0m")  # Print success message in blue

# Function to edit an existing note
def edit_note():
    note_number = get_note_number()  # Get the note number from the user
    current_note_content = current_notes[note_number - 1]  # Get the current note content
    print(f"Previous Note Content: {current_note_content}")  # Print previous note content
    note_content = get_note_content()  # Get the updated note content from the user
    current_notes[note_number - 1] = note_content  # Update the note in the current_notes list
    print("\033[94mNote edited successfully.\033[0m")  # Print success message in blue

# Function to view an existing note
def view_note():
    note_number = get_note_number()  # Get the note number from the user
    note_content = current_notes[note_number - 1]  # Get the note content from the current_notes list
    print(f"\033[94mNote {note_number}: {note_content}\033[0m")  # Print the note content in blue

# Function to get the note number from the user
def get_note_number():
    while True:
        try:
            note_number = int(input("\033[92mEnter note number (1-5): \033[0m"))  # Prompt user for note number
            if note_number < 1 or note_number > 5:
                raise ValueError
            return note_number
        except ValueError:
            print("\033[91mInvalid note number. Please try again.\033[0m")  # Print error message in red

# Function to get the note content from the user
def get_note_content():
    note_content = input("\033[92mEnter note content: \033[0m")  # Prompt user for note content
    return note_content

# Main program loop
while True:
    class_choice = input("\033[92mSelect a class (1, 2, or 3): \033[0m")  # Prompt user for class choice
    
    if class_choice == "1":
        current_notes = class1_notes  # Set current_notes to class1_notes
        class_name = "Period 1"  # Custom name for class 1
    elif class_choice == "2":
        current_notes = class2_notes  # Set current_notes to class2_notes
        class_name = "Period 2"  # Custom name for class 2
    elif class_choice == "3":
        current_notes = class3_notes  # Set current_notes to class3_notes
        class_name = "Period 3"  # Custom name for class 3
    else:
        print("\033[91mInvalid class selection. Please try again.\033[0m")  # Print error message in red
        continue
    
    print(f"\033[92mSelected Class: {class_name}\033[0m")  # Print selected class in green
    
    action_choice = input("\033[92mSelect an action (create, edit, view): \033[0m")  # Prompt user for action choice
    
    if action_choice == "create":
        create_note()  # Call create_note function
    elif action_choice == "edit":
        edit_note()  # Call edit_note function
    elif action_choice == "view":
        view_note()  # Call view_note function
    else:
        print("\033[91mInvalid action selection. Please try again.\033[0m")  # Print error message in red
    
    quit_choice = input("\033[92mQuit? (y/n): \033[0m")  # Prompt user if they want to quit
    
    if quit_choice.lower() == "y":
        break

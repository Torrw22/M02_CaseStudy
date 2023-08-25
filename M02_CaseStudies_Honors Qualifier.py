# Torrey Walls
# M02_CaseStudies_Honors Qualifier
# This app takes student entered data to decide if the student qualifies for the Dean's List or Honor Roll. Variables: last_name, first_name,and gpa

def main():
    print("Welcome to the Dean's List and Honor Roll Checker App!") # Welcome statement
    while True:
        last_name = input("Enter student's last name (enter 'ZZZ' to quit): ") # Collect students lastname
        
        if last_name == 'ZZZ': # Check to see if the user wants to quit
            print("Quitting the app.")
            break
        
        first_name = input("Enter student's first name: ") # Collect students first name
        gpa = float(input("Enter student's GPA: ")) # Collect students GPA
        
        if gpa >= 3.5: # Dean's list check
            print(f"{first_name} {last_name} has made the Dean's List!") # Print statement for Dean's List
        elif gpa >= 3.25: # Honor roll check
            print(f"{first_name} {last_name} has made the Honor Roll!") # Print statement for Honor roll
        else:
            print(f"Unfortunately, {first_name} {last_name} does not qualify for any honors.") # Print statement for non-catagory
        
        print()  # Print an empty line for better readability

if __name__ == "__main__":
    main()
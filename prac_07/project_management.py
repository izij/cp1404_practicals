"""
Project Management 
"""

FILENAME = "projects.txt"

def main():
    # display menu
    load_projects(FILENAME)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            # Load projects
        elif choice == 'S':
            # save projects
        elif choice == 'D':
            # display patterns
        elif choice == 'F':
            # filter projects by date
        elif choice == 'A':
            # add new project
        elif choice == 'U':
            # update project
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()
    # save files
    print("Thank you for using custom-built project management software")

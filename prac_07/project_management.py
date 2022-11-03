"""
Project Management 
"""

from project.py import Project

MENU_STRING = "- (L)oad projects\n" \
              "- (S)ave projects\n" \
              "- (D)isplay projects\n" \
              "- (F)ilter projects by date\n" \
              "- (A)dd new project\n" \
              "- (U)pdate project\n" \
              "- (Q)uit"
FILENAME = "projects.txt"


def main():
    """Project management software"""
    print(MENU_STRING)
    projects = load_projects(FILENAME)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("File: ")
            projects = load_projects(filename)
        elif choice == 'S':
            pass
            # save projects
        elif choice == 'D':
            pass
            # display patterns
        elif choice == 'F':
            pass
            # filter projects by date
        elif choice == 'A':
            pass
            # add new project
        elif choice == 'U':
            pass
            # update project
        else:
            print("Invalid choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    # save files
    print("Thank you for using custom-built project management software")


def load_projects(filename):
    """Loads project from file and adds to list"""
    projects = []
    in_file = open(filename, "r")
    for line in in_file:
        pieces = line.strip().split("\t")
        project = Project(pieces[0], pieces[1], int(pieces[2]), float(pieces[3]), int(pieces[4]))
        projects.append(project)
    in_file.close()
    return projects


main()

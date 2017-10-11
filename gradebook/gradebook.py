import classroom, student, menu, sys, os







''' generate a main menu with options for teacher to choose from '''
main_menu = menu.Menu("Main Menu")
main_menu.add_options(["Add Students", "Assign Work", "View Roster", "View Assignments"])

'''
def start_screen():
    os.system('clear')
    print('\nWelcome to your GradeBook! To get started, we first need to create a new Classroom\n')
    class_name = input("what is the name of the new class? >> ")
    new_classroom = classroom.Classroom(class_name)
    print("'{}' succesfully created".format(class_name))
    #return new_classroom

'''

program_in_use = True

while program_in_use:
    os.system('clear')
    print('\nWelcome to your GradeBook! To get started, we first need to create a new Classroom\n')
    class_name = input("what is the name of the new class? >> ")
    new_classroom = classroom.Classroom(class_name)
    print("'{}' succesfully created".format(class_name))
    main_menu.display_menu()
    main_menu.choose_menu_item()
    if main_menu.choice == "0":
        print("\n{}\n".format(main_menu.options(main_menu.choice)))


    break


''' ___Tests___ '''

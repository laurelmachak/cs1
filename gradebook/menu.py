class Menu(object):
    ''' generate a text based options menu '''
    def __init__(self, menu_name):
        self.menu_name = menu_name
        self.options = {}
        self.choice = ""
    def add_options(self, items_to_add):
        ''' items_to_add is array of strings that will be added to the
        dictionary of the menu options. With a number key and the option string
        as value '''
        i = len(self.options)
        for item in items_to_add:
            self.options[str(i)] = item
            i += 1
    def display_menu(self):
        print("\n{} Options\n".format(self.menu_name))
        for key in self.options.keys():
            print("\t {} - {}\n".format(key, self.options[key]))
    def choose_menu_item(self):
        self.choice = ""
        while self.choice not in self.options.keys():
            #self.display_menu()
            self.choice = input("What would you like to do? >> ")
            #os.system('clear')


    #def key_binding(self, key):
        #self.options[key] = 1;


''' ___TESTS___ '''

'''

main_menu = Menu("Main Menu")
print(main_menu.menu_name)
main_menu.add_options(["Add Students", "Assign Work", "View Roster", "View Assignments"])
main_menu.display_menu()
print(main_menu.options)

'''

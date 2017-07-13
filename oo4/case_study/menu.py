from oo4.case_study import auth as a

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = a.authenticator.login(username, password)
            except a.InvalidUsername:
                print("Sorry, username not exists")
            except a.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username


    def is_permitted(self, permission):
        try:
            a.authorizor.check_permission(permission, self.username)
        except a.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except a.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True


    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")


    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")


    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit              
                """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you!")




def main():
    a.authenticator.add_user("Huang", "huangpassword")
    a.authorizor.add_permission("test program")
    a.authorizor.add_permission("change program")
    a.authorizor.permit_user("test program", "Huang")
    Editor().menu()


if __name__ == "__main__":
    main()


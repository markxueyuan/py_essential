from oo3.extend_builtin import Contact


# Multiple inheritance is a touchy subject

############### mixin

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email + ": " + message)
        # Add email logic here


class EmailableContact(Contact, MailSender):
    pass


def main():
    e = EmailableContact("John Smith", "jsmith@example.net")
    Contact.all_contacts
    e.send_mail("hello, test e-mail here.")


if __name__ == "__main__":
    main()

################### Alternatives
# We could have used single inheritance and added the send_mail function
# to the subclass. The disadvantage here is that the e-mail functionality
# then has to be duplicated for any other classes that need e-mail


# We can create a standalone python function for sending an e-mail,
# with the email address as the parameter of the function

# Composition instead of inheritance.

# monkey-patch







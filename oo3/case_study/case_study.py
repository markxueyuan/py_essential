class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths


    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms. {}".format(self.num_baths))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)

# Static methods are associated only with a class, rather than a
# specific object instance, hence have no self argument
# Thus the super keyword won't work (there is no parent object,
# only a parent class)
# So we call the static method on the parent class directly
# [What does it exactly mean?]

class ApartmentO(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print()

    def prompt_init():
        parent_init = Property.prompt_init()

        laundry = ''
        while laundry.lower() not in \
            ApartmentO.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(ApartmentO.valid_laundries)
            ))

        balcony = ''
        while balcony.lower() not in \
            ApartmentO.valid_balconies:
            balcony = input(
                "Does the property have a balcony?"
                "({})".format(
                    ", ".join(ApartmentO.valid_balconies)
                )
            )
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def main():
    get_valid_input("what laundry?", ("coin", "ensuite", "none"))


# Let's simplify the code of Apartment using the newly defined function

class Apartment(ApartmentO):
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facility does "
            "the property have? ",
            Apartment.valid_laundries
        )
        balcony = get_valid_input(
            "Does the property have a balcony?",
            Apartment.valid_balconies
        )
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
        print()

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage?",
                                 House.valid_garage)
        num_stories = input("How many stories?")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)



class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes?")
        )
    prompt_init = staticmethod(prompt_init)


class Rental:
    valid_furnished = ("yes", "no")

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities
        ))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ",
                                        Rental.valid_furnished)
        )

    prompt_init = staticmethod(prompt_init)


# The above two classes don't have a super class, but we still call
# super__init__ because they are going to be combined with the
# other classes, and we don't know what the order the super calls
# will be made in.

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

# This is surprising, as the class on its own has neither an
# __init__ nor display method.

# Because both parent classes call super in these methods, we
# only have to extend those classes and those classes will
# behave in the correct order.

# while since the static method doesn't call super, we implement
# it explicitly.


def main2():
    init = HouseRental.prompt_init()
    print(init)
    house = HouseRental(**init)
    house.display()





# The order is important, the Rental.display()
# is not called only we exchange the position of Rental and House
# see page 91 for a thorough explanation


class HouseRental2(House, Rental):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

def main3():
    init = HouseRental2.prompt_init()
    print(init)
    house = HouseRental2(**init)
    house.display()


"""
    
Output:
________________________________________

PROPERTY DETAILS
================
square footage: 1
bedrooms: 2
bathrooms. 3

HOUSE DETAILS
# of stories: 4
garage: none
fenced yard: no    
    
"""

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


def main4():
    init = ApartmentRental.prompt_init()
    apt = ApartmentRental(**init)
    apt.display()

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

def main5():
    init = HousePurchase.prompt_init()
    hs = HousePurchase(**init)
    hs.display()

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

def main6():
    init = ApartmentPurchase.prompt_init()
    ap = ApartmentPurchase(**init)
    ap.display()

class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase
        # tuples can be keys of dictionary
        # the values of the dictionary are class objects.
    }

    def add_property(self):
        property_type = get_valid_input("What type of property?",
                                       ('house', 'apartment')).lower()
        payment_type = get_valid_input("What payment type?",
                                       ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init))

def main7():
    ag = Agent()
    ag.add_property()
    ag.add_property()
    print(ag.display_properties())

if __name__ == "__main__":
    main7()
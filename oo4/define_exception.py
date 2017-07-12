# Define an exception is easy
# just define a class inheriting Exception

# Think of a banking application:

class InvalidWithdrawal(Exception):
    pass

def main():
    try:
        raise InvalidWithdrawal("You don't have enough "
                                "money in your account")
    except InvalidWithdrawal as e:
        print(e.__class__.__name__)
        print(e.args)
        print(type(e.args))


# We are able to pass arbitrary number of arguments
# into the exception

# Exception.__init__ is designed to accept any arguments
# and store them as a tuple in an attribute name args


############# customize the initializer


class CustomizedInvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("Account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


def main2():
        try:
            raise CustomizedInvalidWithdrawal(25, 50)
        except CustomizedInvalidWithdrawal as e:
            print("I'm sorry, but your withdrawal is "
                  "more than your balance by "
                  "${}".format(e.overage()))


# The utility of custom exceptions truly comes to light
# when creating a framework, library or API that is intended
# for access by other programmers.

# The client programmer should easily see how to fix the error
# or handle the exception.


################### flow control

# The exception syntax is effective for flow control.
# Exceptions can be used for decision making, branching and
# message passing


# Therefore exceptions are not only suitable for exceptional
# circumstances

class Inventory:
    def lock(self, item_type):
        """Select the type of item that is going to be manipulated.
        This method will lock the item so nobody else can
        manipulate the inventory until it's returned.
        This prevents selling the same item to two different customers."""
        pass


    def unlock(self, item_type):
        """Release the given type so that other customers can
        access it."""
        pass


    def purchase(self, item_type):
        """If the item is not locked, raise an exception.
        If the item_type does not exist, raise an exception.
        If the item is currently out of stock, raise an
        exception.
        If the item is available, subtract one item and return
        the number of items left."""
        pass



class InvalidItemType(Exception):
    pass

class OutOfStock(Exception):
    pass


def main3():
    item_type = 'widget'
    inv = Inventory()
    inv.lock(item_type)
    try:
        num_left = inv.purchase(item_type)
    except InvalidItemType:
        print("Sorry, we don't sell {}".format(item_type))
    except OutOfStock:
        print("Sorry, that item is out of stock.")
    else:
        print("Purchase complete. There are "
              "{} {}s left".format(num_left, item_type))


    finally:
        inv.unlock(item_type)


# If we want to inform the customer as to what date the item
# is expected to be in stock again, we could ensure our
# OutOfStock object requires a back_in_stock parameter
# when it is constructed.
# Then, when we handle the exception, we can check that value
# and provide additional information to the customer.

if __name__ == "__main__":
    main3()
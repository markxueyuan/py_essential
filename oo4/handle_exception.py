from oo4.raise_exception import no_return

try:
    no_return()
except: # which will catch any error
    print("caught the error")
print("excuted after the exception")


########## catch multiple exceptions

def angry_division(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


def main():
    for val in (0, "hello", 50.0, 13):
        print("Testing {}:".format(val), end=" ")  # not new line
        print(angry_division(val))


############# stack except clauses

def angry_division2(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise # reraise the last exception

# Here raise is for the case when we want to do sth
# with the exception and then allow it to continue
# to bubble up to the parent function


def main2():
    for val in (0, "hello", 50.0, 13):
        print("Testing {}:".format(val), end=" ") # not new line
        print(angry_division2(val))



# reference to the exception object
# capture an exception as variable uses the as keyword

def main3():
    try:
        raise ValueError("This is an argument")
    except ValueError as e:
        print("The exception arguments were ", e.args)


########### finally and else

import random

def main4():
    some_exceptions = [ValueError, TypeError, IndexError, None]
    try:
        choice = random.choice(some_exceptions)
        print("raising {}".format(choice))
        if choice:
            raise choice("An error")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print("Caught some other error: %s" %
              (e.__class__.__name__)) # get the name of the error class
    else:
        print("There is no exception")
    finally:
        print("This cleanup code is always called.")



if __name__ == "__main__":
    main4()







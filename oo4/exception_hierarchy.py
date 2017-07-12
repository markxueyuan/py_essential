# All exceptions must extend the BaseException or
# one of its subclasses

#SystemExit and KeyboardInterrupt derive directly
# from BaseException instead of Exception

# SystemExit is raised whenever the program exits naturally

# We generally don't want it to be accidentally caught
# in generic clauses that catch all normal exceptions
# That is why SystemExit directly derives from BaseException

# KeyboardInterrupt is thrown when program execution is
# interrupted with key stroke like C-c

# Both SystemExit and KeyboardInterrupt should handle any
# cleanup tasks inside finally blocks


# except: captures all exceptions
# except: Exception catches Exception and all its subclasses



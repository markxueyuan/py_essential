principal = 1000  # Initial amount
rate = 0.05
numyears = 5

year = 1

while year <= numyears:
    principal *= 1 + rate
    print(format(year, "3d"), format(principal, "0.2f"))
    print("{0:s} {1:3d} {2:0.2f}".format("Try Format as Method",
                                         year,
                                         principal))
    year += 1

"""An example of a while loop statement."""

counter: int = 0
maximum = int = int(input("Count up to, but not including what?"))
while counter < maximum:
    counter_sqaured: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_sqaured))
    counter = counter + 1

print("Done!")
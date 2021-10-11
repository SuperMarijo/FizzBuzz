pick = int(input("Chose a number between 1 and 100 "))

counter = 0

while counter < pick:
    counter = counter + 1
    if counter % 3 == 0 and counter % 5 == 0:
        print("fizzbuzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else:
        print(counter)

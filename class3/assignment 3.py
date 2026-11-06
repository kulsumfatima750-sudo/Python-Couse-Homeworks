smallest = None
largest  = None
while True :
    number = input("enter a number: ")
    if number == "":
        break
    number = float(number)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    if smallest is not None:
        print("smallest number:", smallest)
        print("largest number:", largest)
else:
    print("no numbers were entered.")
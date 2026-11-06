while True:
    inches = float(input("enter inches: "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(centimeters)


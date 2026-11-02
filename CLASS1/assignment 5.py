onetalent = float(input("enter your talent:"))
onepound = float(input("enter your pound:"))
onelot = float(input("enter your lot:"))

total_lots = onetalent * 20 * 32 + onepound * 32 + onelot

total_grams = total_lots * 13.3

kilograms = int(total_grams //1000)
grams =total_grams % 1000

print ("the weight in modern units:")
print (kilograms,"kilogram and ",round(grams,2),"gram")



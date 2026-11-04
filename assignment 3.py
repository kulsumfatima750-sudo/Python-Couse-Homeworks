gender = input("Enter your gender (female/male): ")
hemoglobin = float(input("enter your hemoglobin level (g/l): "))
if gender =="female":
   if hemoglobin < 117:
     print("hemoglobin is low.")
   elif hemoglobin <=155 :
    print("hemoglobin is normal.")
   else:
       print("hemoglobin is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("hemoglobin is low.")
    elif hemoglobin <= 167:
         print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")

else:
    print("Invalid gender.")




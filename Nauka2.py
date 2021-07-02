age = input("Podaj wiek dziecka: ")
age = int(age)
if age == 5:
    print ("Idź do przedszkola!")
elif age >= 6 and age <=17:
    grade = age - 5
    print ("Idź do klasy {}".format(grade))
elif age >= 17:
    print ("Idź do collegu")


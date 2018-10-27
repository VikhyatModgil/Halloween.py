import  random
def factors(age, smoking, weight, excercise, food, gender):
    if(gender == 'Male'):
        age = 76 - age
    elif(gender == 'Female'):
        age = 82 - age
    else:
        print('"'+str(gender)+'"'+ ' is not a valid gender. Please fix your gender and try again')
    if(smoking == "yes"):
        age = age - random.randrange(0,7)
    if(weight == "yes"):
        age = age - random.randrange(0,10)
    if(excercise == "yes"):
        age = age + random.randrange(5,7)
    if(food == 1):
        age = age - random.randrange(0,6)
    return age

age = int(input('How old are you? '))
gender = input('Male or Female? ')
weight = input('Are you over weight (yes/no) ? ')
smoking = input('Do you smoke (yes/no) ? ')
excercise = input('Do u excercise regularly? (yes/no)')
food = input('Do you regularly 1) [eat out] or 2) [cook at home]  (1,2) ')

age = factors(age, smoking, weight, excercise, food, gender)
print("It has been prophesied that you will die in "+str(age)+' years in the month of '+ str(random.randint(1,12)) +' on the date of '+ str(random.randint(1,30))+'.')
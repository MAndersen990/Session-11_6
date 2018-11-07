import random
def main():
    first_name = str(input("Please enter your first name: "))

    middle_name = str(input("Please enter your middle name: "))

    last_name = str(input("Please enter your last name: "))

    house_number = int(input("Please enter your house number: "))

    street_name = str(input("Please enter your street name: "))

    state = str(input("Please enter what state you live in: "))

    zip_code = int(input("Please enter your zipcode: "))

    age = int(input("Please enter your age: "))

    if age >=18:
        print("You should already be registered")
    else:
        gender = str(input("Please enter your gender, (male, female, other): "))

        if gender == 'other':
            gender = str(input("What do you prefere enter here: "))
        elif gender == 'male' or gender =='female':
            driving_question = str(input("Do you drive, (y or n): "))
            if driving_question == 'y':
                how_long_driving = int(input("How many years have you been driving: "))
                if how_long_driving > 10:
                    print("Congrats on your lower insurance rate")
            elif driving_question =='n':
                print("You should check out Driving4You")
        else:
            print("That is not a valid option")
        marital_status = str(input("Are you married, (y or n): "))
        kids = str(input("Do you have children (y or n): "))
        if kids == 'y':
            number_of_kids = int(input("How many kids do you have: "))
        else:
            number_of_kids = 0
            vacation = str(input("Please enter your favorite vacation destination here: "))
            income = int(input("Please enter your rate of income: "))
            if income > 30000:
                print("Congratulations!")
                college = str(input("What college did you attend (enter none if you did not attend): "))
                if college == 'none':
                    print("What is your secret")
            else:
                college = 'none'


        print("First name: " + first_name)
        print("Middle name: " + middle_name)
        print("Last name: " + last_name)
        print("Address: " + str(house_number) + ' ' + street_name + ' ' +state + ',' + str(zip_code))
        print("Age: "+str(age))
        print("Gender: "+gender)
        print("Driving ability: "+driving_question)
        print("Driving duration: "+str(how_long_driving))
        print("Marital status: "+marital_status)
        print("Have kids: "+kids)
        print("Number of kids: "+str(number_of_kids))
        print("Vacation destination: "+vacation)
        print("Income/year: "+str(income))
        print("College: "+college)
main()
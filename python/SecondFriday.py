a = 1
while a == 1:
    try :
        # while operation == "1" or operation == "2" or operation == "3" or operation == "4" :
        operation =input ("Would you like to : \n add ---> 1 \n subtract ---> 2 \n multiply ---> 3 \n divide ---> 4 \n")    
        if operation == "2" or operation == "4" :
            print("You chose {}.".format(operation))
            print("Please keep in mind the the order of your numbers matter.")

        # print("Please Enter Number : ")
        num1 = input("What is the first number ? ")
        num2 = input("what is the second number ? ")
    except:
        print("Enter Only Valid Number ... ")
    try: 
            num1 , num2 = float(num1), float(num2)
            if operation == "1" :
                result = num1 + num2
                print("{} + {} = {}".format(num1, num2, result))
            elif operation == "2" :
                # print("You chose {}.".format(operation))
                # print("Please keep in mind the the order of your numbers matter.")
                result = num1 - num2
                print("{} - {} = {}".format(num1, num2, result))
            elif operation == "3" :
                result = num1 * num2
                print("{} * {} = {}".format(num1, num2, result))
            elif operation == "4" :
                # print("You chose {}.".format(operation))
                # print("Please keep in mind the the order of your numbers matter.")
                result = num1 / num2
                print("{} / {} = {}".format(num1, num2, result))
            else: 
                print("Sorry, but '{}' is not an option.".format(operation))
    except: 
            print("Error : Improper numbers used. Please try again.")

    
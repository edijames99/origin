try:
    time = int(input("Please Enter The Time Now :  "))
    if time < 1200 : 
        print("Good Morning")
    elif time >= 1200 and time < 1700 :
        print("Good Afternoon")
    else : 
        print("Good Evening")
except : 
    print("Please Enter Valid number Example : 1200")


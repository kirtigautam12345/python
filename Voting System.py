#voting system
name = input("Enter your name: ")
age = int(input("Enter your age: "))
id = int(input("Enter your Aadhar number: "))
if (age >= 18):
    print("You are eligible for vote.")
    choice = input("Enter your voting party from BJP, Congress, BSP, SAPA: ")
    if(choice == "BJP"):
        print("BJP")
    elif (choice == "Congress"):
        print("Congress")
    elif(choice == "BSP"):
        print("BSP")
    else:
        print("SAPA")
else:
    print("You are not eligible for vote.")
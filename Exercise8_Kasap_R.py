usernameInput = input("Username : ")
passwordInput = input("Password : ")
q_banana = 0
q_orange = 0
q_grape = 0
q_watermelon = 0

if usernameInput == "admin" and passwordInput == "789":
    print("Success")
    print("----- Welcome to Ice Shop -----")
    print("1.Banana 50B")
    print("2.Orange 20B")
    print("3.Grape 30B")
    print("4.Watermelon 40B")
    Select = int(input("Select : "))
    while Select != 0:
        if Select == 1:
            q_banana = int(input("Amount of Banana : "))
            Select = int(input("Select : "))
        elif Select == 2:
            q_orange = int(input("Amount of Orange : "))
            Select = int(input("Select : "))
        elif Select == 3:
            q_grape = int(input("Amount of Grape : "))
            Select = int(input("Select : "))
        elif Select == 4:
            q_watermelon = int(input("Amount of Watermelon : "))
            Select = int(input("Select : "))
        result = (50*q_banana)+(20*q_orange)+(30*q_grape)+(40*q_watermelon)
        print("Total Price : ",result,"THB")
else:
    print("Login Fail")



def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "789":
        return showmenu()
    else:
        return False
def showmenu():
    print("----- Ice Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuselect()
def menuselect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatcal()
    elif userSelected == 2:
        return pricecal()
def vatcal(price):
    price = int(input("Price (THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    return result
def pricecal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total = price2+price1
    return total

print(login())



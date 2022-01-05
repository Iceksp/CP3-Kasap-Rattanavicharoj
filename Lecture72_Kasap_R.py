menuList = []

def showbill():
    total = 0
    print("===== MY FOOD =====")
    for number in range(len(menuList)):
        print(menuList[number])
        total += int(menuList[number][1])
    print("ราคารวม :",total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

showbill()




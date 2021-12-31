tall = int(input("พีระมิดสูง : "))
blank = tall
for Hight in range(1):
    for piramid in range(tall):
        blank -= 1
        piramid += (1*(piramid+1))
        print(" "*blank,"*"*piramid)

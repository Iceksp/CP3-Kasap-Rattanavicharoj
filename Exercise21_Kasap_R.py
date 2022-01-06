from tkinter import *
import math

def leftClickButton(event):
    text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(text)
    if text > 30:
        labelResult.configure(text="อ้วนมาก")
    elif text <29.9 and text > 25:
        labelResult.configure(text="อ้วน")
    elif text <24.9 and text > 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif text <22.9 and text > 18.6:
        labelResult.configure(text="น้ำหนักปกติ")
    elif text <18.5:
        labelResult.configure(text="ผอมเกินไป")
MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()





def vatCal(total):
    result = total+(total*7/100)
    return result

i = int(input("กรุณากรอกจำนวนเงิน : "))
print(vatCal(i))
hours = input("Enter number of working hours:")
rate = input("Enter rate per hour:")
def pay(hours, rate):
    try:
        hrs = float(hours)
        r = float(rate)
    except:
        print ("Erro, please enter numeric input")
        hours = input("Enter hours:")
        rate = input("Enter rate:")

    if hrs > 40:
        pay = 40 *r + (hrs -40)*r*1.5
        print("Pay:",pay)
    else:
        pay = hrs * r
        print("Pay:",pay)
pay(hours,rate)

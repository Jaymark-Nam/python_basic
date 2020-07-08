hours = float(input("Enter Hours:")) #45
rate = float(input("Enter Rate:")) #10.50


def computepay(h,r):
    if h >40:
        return (h-40)*r*1.5 + 40*r
    else :
        return h*r

p = computepay(hours, rate)
print("Pay",p)



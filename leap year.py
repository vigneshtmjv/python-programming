a=input()
if (a%4==0):
    if (a%100==0):
        if (a%400==0):
            print "it is a leap year"
else:
    print "it is not a leap year"

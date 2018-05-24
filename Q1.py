yr = int(input('Enter the year'))
if (yr % 4) == 0:
    if (yr % 100 == 0):
        if (yr % 400 == 0):
            print("%d is a leap year" % (yr))
        else:
            print("%d is not a leap year" % (yr))
    else:
        print("%d is a leap year" % (yr))
else:
    print("%d is not a leap year" % (yr))

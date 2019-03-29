def is_leap(year):
    leap = False
    if (year%4) != 0:
        leap = False
    elif (year%100 != 0):
        leap = True
    elif (year%400 != 0):
        leap = False
    else:
        leap = True

    
    
    return leap


# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)





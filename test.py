import re
num = int(input())
while num > 0:
        string = input()
        p = re.match(r'([1-9][0-9][0-9][0-9])\-(1[0-2]|0[1-9])\-(0[1-9]|3[0-1]|1[0-9]|2[0-9])$',string)
        year = int(p.group(1))
        month = int(p.group(2))
        day = int(p.group(3))
        day -=  1
        if(day <= 0):
            month -= 1
            if(month <= 0):
                year -= 1
                month += 12
                if(month == 2):
                    if(((year%4 == 0 and year%100 != 0) or year % 400 == 0)):
                        day += 28
                    else:
                        day += 29
                elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                    day += 31
                else:
                    day += 30
            else:
                if(month == 2):
                    if(((year%4 == 0 and year%100 != 0) or year % 400 == 0)):
                        day += 28
                    else:
                        day += 29
                elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                    day += 31
                else:
                    day += 30


        print("%d-%02d-%02d"%(year,month,day))
        num = num -1





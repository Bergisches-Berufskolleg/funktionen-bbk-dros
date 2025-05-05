
def isLeapYear(year):
    if (year % 400 == 0):
        return True
    elif(year % 100 ==0 and year % 400 != 0):
        return False
    elif(year % 4 == 0 and year % 100 !=0 and year % 400 != 0):
        return True
    else:
         return False

def main():
    jahr = int(input("Gib ein jahr an:"))
    print(isLeapYear(jahr))

if __name__ == "__main__":
    main()

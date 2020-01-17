#!/usr/bin/env python3

from datetime import datetime, time

def main():
    choice = "y"
    while choice.lower() == "y":
        #welcome message
        print("Birthday Calculator")
        print()
  after_bday = tday.day - bday.day
        y = input("Enter Name:")
        x = input("Enter birthday (MM/DD/YY):")

        # find out if birthday is greater than or less than today
        

        # parse the birthday
        bday = datetime.strptime(x,"%m/%d/%y")
        tday = datetime.now()
        if bday.year > tday.year:
            new_year = bday.year - 100
            bday = datetime(new_year, bday.month, bday.day)

        # print the math
        b = bday.strftime("%A %B %d, %Y")
        print("Birthday:", b)
        t = tday.strftime("%A %B %d, %Y")
        print("Today:", t)

        age = tday.year - bday.year
        print(y, "is", age, "years old.")
        temp_bday = datetime(2020, bday.month, bday.day)
        until_bday = tday.day - bday.day
        if temp_bday > tday:
            print(y, "is", age - 1, "years old.")            
            print(y, "'s birthday is in", until_bday.days * 1, "days.")
        elif temp_bday < tday:
            print(y, "is", age, "years old.")
            if until_bday.days == 0:
                print(y, "'s birthday is today!")
            else:
                print(y, "'s birthday was", until_bday.days, "days ago.") 

        choice = input("Continue (y/n): ")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     19/07/2021
# Copyright:   (c) Kafonya Nora 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

gender = input("Enter your Gender")
gender = gender.lower()

age = int(input("Enter your Age"))

if gender == "female" and age <=17:
   print ("You are Welcome")

else:
   print("You are not welcome")
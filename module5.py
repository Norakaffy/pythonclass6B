#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     14/07/2021
# Copyright:   (c) Kafonya Nora 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


score = int(input("Enter Your Score"))



if score >100:
    print("Invalid")

elif score >=70:
    print("A")

elif score >=60:
    print ("B")

elif score >=50:
    print("C")

elif score >=45:
    print("D")

elif score >=40:
    print("E")

elif score >=0:
    print("F")

else:
    print("Invalid Score")
a = '3'

if a.isdigit():
    if int(a) < 10:
        # if int(a) !=9:
        #     print("!9")
        #     if int(a) !=7:
        #         print("!7")
        #         if int(a) !=8:
        #             print("!8")
        print("3 is less than 10")
    elif int(a) > 10:
        print("3 is greater than 10")
    elif int(a) == 3:
        print("3 is equal to 3")
    else:
        print("The error!")
else:
    print('a is not')
# Tab or 4 spaces make an indentation

print("The end of program")

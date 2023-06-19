# a = 4
#
# if a < 10:
#     print("Code was ran")
# else:
#     print("The error!")

# Tab or 4 spaces make an indentation
browser = 'chrome'

# if browser == 'chrome':
#     print("Code was ran")
# else:
#     print("The error!")
#
# print("The end of program")


user_input = input("Enter a number: ")
print(type(user_input))

if user_input.isdigit():
    print(int(user_input) + 5)
    # print(user_input + 5)
    print("Code was ran")
elif user_input.isalpha():
    print("The error!")
else:
    print("FAIL!")


# if type(user_input) == int:
#     print(int(user_input) + 5)
#     print("Code was ran")
# else:
#     print("The error!")
# Tab or 4 spaces make an indentation

# print("The end of program")

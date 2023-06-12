# from MyApp.Handlers.text_handler import handle_text
#
# input_text = "python package practices"
# handle_text(input_text) # PYTHON PACKAGE PRACTICES

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")
#
# print("Program continues.")
#
# try:
#     number = int("Not a number")
#     number1 = 5 + "Not a number"
# except ValueError:
#     print("Error: Invalid value")
# except TypeError:
#     print("Error: invalid type")
#
# class CustomException(Exception):
#     def __init__(self, message):
#         self.message = message
#
# try:
#     raise CustomException("This is a custom exception. ")
# except CustomException as e:
#     print(f"Error: {e.message}")

a = ['a1', 'a2', 'a3']
# 동일 결과 1
for i in range(len(a)):
    print(i, a[i])
# 동일 결과 2
i = 0
for v in a:
    print(i, v)
    i += 1
# 동일 결과 3
for i,v in enumerate(a):
    print(i, v)
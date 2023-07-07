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

# import pprint
# pprint.pprint(locals()) # pprint.pprint 하면 줄 바꿈되서 예쁘게 출력됨 pprint 하나하면 줄바꿈안됨

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letters = {}

for word in words:
    letter = word[0]
    if letter not in by_letters:
        by_letters[letter] = [word]
    else:
        by_letters[letter].append(word)

print(by_letters)      # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
print(by_letters['c']) # keyworkd 'c'가 없으므로 key error 나는게 맞음
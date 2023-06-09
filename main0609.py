# file_object = open('example.txt', 'r')
#
# position = file_object.tell()
# print("Current position: ", position)
#
# file_object.seek(7)
#
# position = file_object.tell()
# print("Changed position: ", position)
#
# file_object.close()

with open('example.txt', 'w') as file_object:
    content = """This is a multiline string.
Python is a versatile language.
It is easy to learn and use."""
    print(content)
    file_object.write(content)


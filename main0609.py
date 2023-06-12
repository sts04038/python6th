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

# with open('example.txt', 'w') as file_object:
#     content = """This is a multiline string.
# Python is a versatile language.
# It is easy to learn and use."""
#     print(content)
#     file_object.write(content)

# file_object = open('list_example.txt', 'w')
# content_list = ["Python", "Java", "C++", "Javascript"]
#
# for item in content_list:
#     file_object.write(item + '\n')
#
# file_object.close()

import os
current_directory = os.getcwd()
print(current_directory)

os.makedirs('parent_directory/child_directory/grandchild_directory')

for dirpath, dirnames, filenames in os.walk('parent_directory'):
    print(f"디렉터리 경로: {dirpath}")
    print(f"디렉터리 이름: {dirnames}")
    print(f"파일 이름: {filenames}")
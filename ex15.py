# from sys import argv
# script, filename = argv
#
# txt = open(filename)
# print(f"\nIt is your {filename}: ")
# print(txt.read())
# txt.close()
#
# print("\nType the filename again: ")
# file_again = input('> ')
# txt_again = open(file_again)
# print(f"It is your {file_again}: ")
# print(txt_again.read())
# txt_again.close()

from sys import argv

script, filename = argv
txt = open(filename)
print(f"\nIt is your {filename}: ")
print(txt.read())
txt.close()

print("\nType the filename again: ")
file_again = input("> ")
txt_again = open(file_again)
print(f"It is your {file_again}")
print(txt_again.read())
txt_again.close()

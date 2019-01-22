# file_open = open("file_to_open.txt", "r")  # (file, permissions)
# file_output = open("output.txt", "w")

# for line in file_open:
#     print("%s"%(line), file=file_output)

# file_open.(close)
# file_output.close()

from sys import argv
import os

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Au revoir!")
target.truncate()

print("Now I'm going to print lines.")
lines = int(input("How many lines? "))

print("I'll print %d lines." % lines)

i = 1
while i <= lines:
    print("Writing line %d..." % i)
    target.write("%d" % i)
    target.write("\n")
    i += 1

print("Closing the file.")
target.close()

size = os.path.getsize(filename)
print("The file is %d bytes." % size)

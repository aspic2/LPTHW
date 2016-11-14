from sys import argv

script, filename = argv

#Declares a variable that opens the argv filename
txt = open(filename)

#Message to reader, then print the document input from txt
print("Here's your file %r:" % filename)
print(txt.read())
txt.close()

#Takes a file name input from the user, opens the file in read-only mode,
#then prints the file contents to the screen.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

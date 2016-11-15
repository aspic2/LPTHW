from os.path import exists

from_file = input("What file would you like to copy?\n> ")
to_file = input("What would you like to title your new file?\n> ")

print("Making a copy of %s titled %s" % (from_file, to_file))

f = open(from_file)
to_copy = f.read()

p = open(to_file, 'w')
p.write(to_copy)

f.close()
p.close()

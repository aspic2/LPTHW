

def the_numerator(top):
    i = 0
    numbers = []
    if top > 50:
        print('number too big. must be < 50.')
        top = int(input("Please enter a smaller number.\n> "))
        the_numerator(top)
    else:
        while i < top:
            print("At the top i is %d" % i)
            numbers.append(i)

            i = i + 1
            print("Numbers now: ", numbers)
            print("At the bottom i is %d" % i)



the_numerator(60)



'''print("The numbers: ")

for num in numbers:
    print(num, end=' ')
'''

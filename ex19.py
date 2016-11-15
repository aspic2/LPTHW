#creating function that declares how much cheese and how many cracker boxes
#you have
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

#calls cheese_and_crackers function with written in number values
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#declares two variables, independent of function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#run function with two variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#run function with math operations as arguments
print("We can even do math inside, too:")
cheese_and_crackers(10 + 20, 5 + 6)

#run function with variables and math operations as arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

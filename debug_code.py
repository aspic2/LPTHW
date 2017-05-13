'''For the CFA exam:
    Already Paid
    Will need to take it Eventually


Against the CFA Exam:
    interfere with programming
    I still do not invest well
    Learn statistics
    Learn match
    GRE
    no discernable benefit from one extra test
'''
import random

example_dict = {
'a': "Value of A",
'b': 'Value of B',
'c': 'Value of C'
}

def listmaker(your_dictionary):
    newlist = []
    for x in your_dictionary:
        newlist.append(x)
    return newlist

example_list = listmaker(example_dict)

question = random.choice(example_list)
print(question)

answer = example_dict[question]
print(answer)

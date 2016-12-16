'''
All about inheritance. This lesson teaches three ways to use inheritance:
    1. Actions on the child imply an action on the parent
    2. Actions on the child override the action on the parent.
    3. Actions on the child alter the action on the parent.
'''
#Implicit inheritance
print("-" * 50, "\nHere's an example of implicit inheritance:")

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

#prints "PARENT implicit()", as expected
dad.implicit()
#prints "PARENT implicit()", since this calls the parent function
son.implicit()



#---------------------------------------------------------------
#Override Explicitly
print("\n\n\n")
print("-" * 50, "\nHere's an example of overriding a parent function:")

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad1 = Parent()
son1 = Child()


dad1.override()
#prints "CHILD override()", as child has its own instance of this func.
son1.override()



#-----------------------------------------------------------------
#Altered function
print("\n\n\n")
print("-" * 50, "\nHere's an example of using 'super' to alter functions:")

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad2 = Parent()
son2 = Child()

dad2.altered()
son2.altered()



#-----------------------------------------------------------------
#Inheritance: Implicit, Overriding, and Alteration (super)
print("\n\n\n")
print("-" * 50, "\nNow for all three together:")

class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD AFTER PARENT altered()")

dad3 = Parent()
son3 = Child()

dad3.implicit()
son3.implicit()

dad3.override()
son3.override()

dad3.altered()
son3.altered()


#-----------------------------------------------------------------
#Using Composition as an alternative
print("\n\n\n")
print("-" * 50, "\nYou can do the same thing with composition, as below:")

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son4 = Child()

son4.implicit()
son4.override()
son4.altered()

import mystuff

mystuff.apple()
print(mystuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


new_variable = MyStuff()
print("I have created a copy of class MyStuff")
new_variable.apple()
print(new_variable.tangerine)

print("\n\n", "-" * 10, "\nHere's Zed's Song class:")
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",\
                        "With pockets full of shells"])

america = Song(["Let us be lovers",
                "We'll marry our fortunes together.",
                "I've got some real estate",
                "here in my bag."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

america.sing_me_a_song()

print("-" * 10)
print("Here's my own song class:")
class BetterSong(object):

    def __init__(self, words):
        self.words = words

    def read_song(self):
        for line in self.words:
            print(line)
        print("That's it!\nI hope you liked it!")


being_in_trouble = "Now that you're gone", "It's been a long, lonely time.",\
"It's a long, cold, lonely time."

please_let_me_wonder = "Now here we are together.",\
"This would've been worth waiting forever.",\
"I always knew it'd feel this way."

umo = BetterSong(being_in_trouble)
beachboys = BetterSong(please_let_me_wonder)

umo.read_song()
print("\n\n")
beachboys.read_song()

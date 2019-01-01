
# VERSION 1

# import ex40_mystuff             #import library

# ex40_mystuff.apple()            #execute function apple()
# print(ex40_mystuff.mystuff['apple'])        #access an item in a list in module
# print(ex40_mystuff.tangerine)       #print variable tangerine in module

# VERSION 2


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)

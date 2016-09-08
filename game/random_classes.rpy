init -100 python:
    class RandomCharacter(object):
        def __init__(self,excludedCharacter=[]):
            global m #mayumi
            global s # sumiko
            global yuu #yuuko
            global ss #shunsuke
            characters = ["yuu","m","ss","s"]
            #characters = 
            if excludedCharacter:
                #will trigger error if anyhow type
                char_list = [x for x in characters if x not in excludedCharacter]
                character = renpy.random.choice(char_list)
            else:
                character = renpy.random.choice(characters)
            if character == "yuu":
                self.say = yuu
                self.person = "Yuuko"
                self.p = "yuu"
            elif character == "s":
                self.say = s
                self.person = "Sumiko"
                self.p = "s"
            elif character == "ss":
                self.say = ss
                self.person = "Shunsuke"
                self.p = "ss"
            else:
                self.say = m
                self.person = "Mayumi"
                self.p = "m"
        def remainingCharacters(self):
            characters = ["yuu","m","ss","s"]
            characters.remove(self.p)
            return characters
    
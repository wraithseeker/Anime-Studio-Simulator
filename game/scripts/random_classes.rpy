init -100 python:
    class RandomCharacter(object):
        def __init__(self,excludedCharacter=[]):
            global m #mayumi
            global s # sumiko
            global yuu #yuuko
            global ss #shunsuke
            global mayumi_stats
            global yuuko_stats
            global sumiko_stats
            global shunsuke_stats
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
                self.g = "her"
                self.stat = yuuko_stats
            elif character == "s":
                self.say = s
                self.person = "Sumiko"
                self.p = "s"
                self.g = "her"
                self.stats = sumiko_stats
            elif character == "ss":
                self.say = ss
                self.person = "Shunsuke"
                self.p = "ss"
                self.g = "him"
                self.stats = shunsuke_stats
            else:
                self.say = m
                self.person = "Mayumi"
                self.p = "m"
                self.g = "her"
                self.stats = mayumi_stats
        def remainingCharacters(self):
            characters = ["yuu","m","ss","s"]
            characters.remove(self.p)
            return characters
    
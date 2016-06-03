init -100 python:
    class Tasks(object):
        def __init__(self,title,description,**kwargs):
            self.title = title
            self.description = description
            self.selected = False
            for key, value in kwargs.items():
                setattr(self, key, value)

        def addStats(self,anime):
            for item in anime_stats:
                renpy.notify(item)
                if hasattr(self,item):
                    setattr(anime,item,getattr(anime,item) + getattr(self,item))

            #renpy.notify( "Some Message.")

        def removeStats(self,anime):
            for item in anime_stats:
                renpy.notify(item)
                if hasattr(self,item):
                    setattr(anime,item,getattr(anime,item) - getattr(self,item))

        def getStats(self):
            msg = ""
            priority = []
            attribute_string = []
            for index,item in enumerate(anime_stats):
                if hasattr(self,item):
                    if getattr(self,item) > 0:
                        attribute_number = "+" + str(getattr(self,item))
                        attribute_color = "{color=#27ae60}"
                        priority.append(True)
                    else:
                        attribute_number = str(getattr(self,item))
                        attribute_color = "{color=#c0392b}"
                        priority.append(False)
                    attribute_string.append("\n" + attribute_color + attribute_number + " " + item + "{/color}")

            return self.sortAttributes(attribute_string,priority)

        def sortAttributes(self,attributes,priorities):
            sorted_attribute_string = []
            # if it is adding stats, we want to put them to our string first
            for index,priority in enumerate(priorities):
                if priority is True:
                    sorted_attribute_string.append(attributes[index])
                else:
                    continue

            # next we get our negative stats
            for index,priority in enumerate(priorities):
                if priority is False:
                    sorted_attribute_string.append(attributes[index])
                else:
                    continue
            return sorted_attribute_string




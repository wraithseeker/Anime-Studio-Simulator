init -100 python:
    class Tasks(object):
        def __init__(self,title,description,**kwargs):
            self.title = title
            self.description = description
            self.selected = False
            for key, value in kwargs.items():
                setattr(self, key, value)

        def addStats(self,anime,stats_manager):
            for item in anime_stats:
                if hasattr(self,item):
                    #renpy.notify(str(item) + " added")
                    setattr(anime,item,getattr(anime,item) + getattr(self,item))

            for item in char_stats:
                if hasattr(self,item):
                    #renpy.notify(str(item) + " added")
                    setattr(stats_manager,item,getattr(self,item) + getattr(stats_manager,item))

        def removeStats(self,anime,stats_manager):
            for item in anime_stats:
                if hasattr(self,item):
                    #renpy.notify(str(item) + " removed")
                    setattr(anime,item,getattr(anime,item) - getattr(self,item))

            for item in char_stats:
                if hasattr(self,item):
                    #renpy.notify(str(item) + " added")
                    setattr(stats_manager,item,getattr(stats_manager,item) - getattr(self,item) )

        def getStats(self):
            msg = ""
            priority = []
            attribute_string = []
            for index,item in enumerate(anime_stats):
                if hasattr(self,item):
                    if getattr(self,item) > 0:
                        attribute_number = "{size=+10}+{/size}" #+ str(getattr(self,item))
                        attribute_color = "{color=#27ae60}"
                        priority.append(True)
                    else:
                        attribute_number = "{size=+10}-{/size}"#str(getattr(self,item))
                        attribute_color = "{color=#c0392b}"
                        priority.append(False)
                    item_title = item.replace("_"," ")
                    attribute_string.append("\n " + attribute_color + attribute_number + " " + "{font=fonts/Multicolore.otf}{size=25}" + item_title + "{/font}{/size}" 
                                            + "{/color}")

            for index,item in enumerate(char_stats):
                if hasattr(self,item):
                    if getattr(self,item) > 0:
                        attribute_number = "{size=+10}+{/size}"
                        attribute_color = "{color=#27ae60}"
                        priority.append(True)
                    else:
                        attribute_number = "{size=+10}-{/size}"
                        attribute_color = "{color=#c0392b}"
                        priority.append(False)
                    if item == "stress":
                        attribute_number = "{size=+10}-{/size}"
                    item_title = item.replace("_"," ")
                    attribute_string.append("\n " + attribute_color + attribute_number + " " + "{font=fonts/Multicolore.otf}{size=25}" + item_title + "{/font}{/size}" 
                                            + "{/color}")
           
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






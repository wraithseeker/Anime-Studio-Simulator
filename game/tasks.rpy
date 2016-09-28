init -100 python:
    class Tasks(object):
        def __init__(self,title,description,**kwargs):
            self.title = title
            self.description = description
            self.selected = False
            self.positive_stats = []
            self.negative_stats = []
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.sortStats()

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

        def sortStats(self):
            string_vertical_formatting = "\n"
            for index,item in enumerate(anime_stats):
                if hasattr(self,item):
                    item_title = item.replace("_"," ").replace("character","char.").replace("development","dev")
                    if getattr(self,item) > 0:
                        stat_text = GREEN_COLOR + POSITIVE_SIGN
                        self.positive_stats.append(string_vertical_formatting + stat_text + item_title)
                    else:
                        stat_text = RED_COLOR + MINUS_SIGN
                        self.negative_stats.append(string_vertical_formatting + stat_text + item_title)

            for index,item in enumerate(char_stats):
                if hasattr(self,item):
                    if getattr(self,item) > 0:
                        if item == "stress":
                            stat_text = RED_COLOR + POSITIVE_SIGN
                            item_title = item
                            self.negative_stats.append(string_vertical_formatting + stat_text + item_title)

                        else:
                            stat_text = GREEN_COLOR + POSITIVE_SIGN
                            item_title = item.replace("_"," ")
                            self.positive_stats.append(string_vertical_formatting + stat_text + item_title)

                    else:
                        if item == "stress":
                            stat_text = GREEN_COLOR + MINUS_SIGN
                            item_title = item
                            self.positive_stats.append(string_vertical_formatting + stat_text + item_title)
                        else:
                            stat_text = RED_COLOR + MINUS_SIGN
                            item_title = item.replace("_"," ")
                            self.negative_stats.append(string_vertical_formatting + stat_text + item_title)







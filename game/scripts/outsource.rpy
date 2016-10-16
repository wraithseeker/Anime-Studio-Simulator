init -100 python:
    #TO DO add hard limit for anime , tasks , stats so they can't go out of max limit
    class Outsource(object):
        #enum
        SELECTED = 0
        NOT_SELECTED = 1
        DISABLED = 2
        def __init__(self):
            #main variables, prev = previous week
            self.cost = 0
            self.value = 0
            self.selection_count = 0
            #db progress variables
            self.stats = ["plot","character_development","storyboard",
                                    "character_design","background","animation",
                                    "voice_acting","op_ed","ost","quality_check","marketing"]
            # Story
            self.plot = Outsource.NOT_SELECTED
            self.character_development = Outsource.NOT_SELECTED
            self.storyboard = Outsource.NOT_SELECTED
            # Art
            self.character_design = Outsource.NOT_SELECTED
            self.background = Outsource.NOT_SELECTED
            self.animation = Outsource.NOT_SELECTED
            #Music
            self.voice_acting = Outsource.NOT_SELECTED
            self.op_ed = Outsource.NOT_SELECTED
            self.ost = Outsource.NOT_SELECTED
            #Misc
            self.quality_check = Outsource.NOT_SELECTED
            self.marketing = Outsource.NOT_SELECTED

        def start(self):
            outsource_success = False
            global anime
            for i in range (0,len(self.stats)):
                current_stat = getattr(self,self.stats[i])
                if current_stat == Outsource.SELECTED:
                    setattr(self,self.stats[i],Outsource.DISABLED)
                    setattr(anime,self.stats[i],getattr(anime,self.stats[i]) + outsource.value)
                    outsource_success = True
            return outsource_success
        def reset(self):
            for i in range (0,len(self.stats)):
                setattr(self,self.stats[i],Outsource.NOT_SELECTED)


            




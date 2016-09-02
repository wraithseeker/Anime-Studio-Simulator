init -100 python:
    #TO DO add hard limit for anime , tasks , stats so they can't go out of max limit
    class Anime(object):
        def __init__(self,name):
            self.name = name
            #main variables, prev = previous week
            self._funds = 0
            #db progress variables
            self.db_stats = ["plot","character_development","storyboard",
                                    "character_design","background","animation",
                                    "voice_acting","op_ed","ost","quality_check","marketing","funds"]
            self.db_positive = []
            self.db_negative = []
            for i in range (0,len(self.db_stats)):
                setattr(self,"prev_" + self.db_stats[i],0)
            # Story
            self._plot = 0
            self._character_development = 0
            self._storyboard = 0
            self._story_bonus = 0
            self._story_progress = 0
            # Art
            self._character_design = 0
            self._background = 0
            self._animation = 0
            self._art_bonus = 0
            self._art_progress = 0
            #Music
            self._voice_acting = 0
            self._op_ed = 0
            self._ost = 0
            self._music_bonus = 0
            self._music_progress = 0

            #Misc
            self._quality_check = 0
            self._marketing = 0


        def storePreviousWeekValues(self):
            for i in range (0,len(self.db_stats)):
                setattr(self,"prev_" + self.db_stats[i],getattr(self,self.db_stats[i]))
            self.db_positive = []
            self.db_negative = []

        def getStatChanges(self,stat):
            current_stat = getattr(self,stat)
            prev_stats = getattr(self,"prev_" + stat)
            new_stats = current_stat - prev_stats
            if stat == "character_development":
                displayed_stat = "character dev"
            elif stat == "character_design":
                displayed_stat = "char. design"
            else:
                displayed_stat = stat.replace("_"," ")
            if (new_stats == current_stat):
                return
            positive = "{color=#27ae60}{font=fonts/Delius-Regular.ttf}{size=+15}+ {/size}{/font}"
            negative = "{color=#c0392b}{font=fonts/Delius-Regular.ttf}{size=+15}- {/size}{/font}"
            end_tag = "{/color}"
            if (new_stats > 0 ):
                #positive increase in stats
                text = positive + displayed_stat + end_tag
                self.db_positive.append(text)
            else:
                #negative increase in stats
                text = negative + displayed_stat + end_tag
                self.db_negative.append(text)

        def updateDashboard(self):
            for i in range (0,len(self.db_stats)):
                self.getStatChanges(self.db_stats[i])

        #story
        @property

        def plot(self):
            return self._plot

        @plot.setter
        def plot(self,value):
            if 0 <= value <= 5:
                self._plot = value
            elif value > 5:
                self._plot = 5
           

        @property

        def storyboard(self):
            return self._storyboard

        @storyboard.setter
        def storyboard(self,value):
            if 0 <= value <= 5:
                self._storyboard = value
            elif value > 5:
                self._storyboard = 5

        @property

        def character_development(self):
            return self._character_development

        @character_development.setter
        def character_development(self,value):
            if 0 <= value <= 5:
                self._character_development = value
            elif value > 5:
                self._character_development = 5

        @property

        def story_progress(self):
            return self._story_progress

        @story_progress.setter
        def story_progress(self,value):
            self._story_progress = value

        @property

        #art
        def character_design(self):
            return self._character_design

        @character_design.setter
        def character_design(self,value):
            if 0 <= value <= 5:
                self._character_design = value
            elif value > 5:
                self._character_design = 5

        @property

        def background(self):
            return self._background

        @background.setter
        def background(self,value):
            if 0 <= value <= 5:
                self._background = value
            elif value > 5:
                self._background = 5

        @property

        def animation(self):
            return self._animation

        @animation.setter
        def animation(self,value):
            if 0 <= value <= 5:
                self._animation = value
            elif value > 5:
                self._animation = 5

        @property

        def art_progress(self):
            return self._art_progress

        @art_progress.setter
        def art_progress(self,value):
            self._art_progress = value

        #music
        @property

        def voice_acting(self):
            return self._voice_acting

        @voice_acting.setter
        def voice_acting(self,value):
            if 0 <= value <= 5:
                self._voice_acting = value
            elif value > 5:
                self._voice_acting = 5


        @property

        def op_ed(self):
            return self._op_ed

        @op_ed.setter
        def op_ed(self,value):
            if 0 <= value <= 5:
                self._op_ed = value
            elif value > 5:
                self._op_ed = 5


        @property

        def ost(self):
            return self._ost

        @ost.setter
        def ost(self,value):
            if 0 <= value <= 5:
                self._ost = value
            elif value > 5:
                self._ost = 5


        @property

        def music_progress(self):
            return self._music_progress

        @music_progress.setter
        def music_progress(self,value):
            self._music_progress = value

        #others
        @property

        def funds(self):
            return self._funds

        @funds.setter
        def funds(self,value):
            self._funds = value

        @property

        def marketing(self):
            return self._marketing

        @marketing.setter
        def marketing(self,value):
            if 0 <= value <= 5:
                self._marketing = value

        @property

        def quality_check(self):
            return self._quality_check

        @quality_check.setter
        def quality_check(self,value):
            if 0 <= value <= 5:
                self._quality_check = value
            




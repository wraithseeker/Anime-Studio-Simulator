init -100 python:
    #TO DO add hard limit for anime , tasks , stats so they can't go out of max limit
    class Anime(object):
        #enums 
        CATEGORY_NONE = 0
        CATEGORY_POSITIVE = 1
        CATEGORY_NEGATIVE = 2
        HAREM = 0
        MYSTERY = 1
        ACTION = 2

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
            self.category = 0 #defaults to harem
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
                displayed_stat = "char.design"
            else:
                displayed_stat = stat.replace("_"," ")
            if (new_stats == 0):
                return
            positive = GREEN_COLOR + POSITIVE_SIGN
            negative = RED_COLOR + MINUS_SIGN
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
            self.story_progress = int((anime.plot + anime.storyboard + anime.character_development) / 15.0 * 100.0)
            self.art_progress = int((anime.character_design + anime.background + anime.animation) / 15.0 * 100.0)
            self.music_progress = int((anime.op_ed + anime.ost + anime.voice_acting) / 15.0 * 100.0)

        def checkCategory(self,category):
            #0 = none, 1 = positive, 2 = negative
            if category == "story":
                prev_progress = self.prev_plot + self.prev_character_development + self.prev_storyboard
                new_progress = self.plot + self.character_development + self.storyboard
                if (new_progress == prev_progress ):
                    return 0
                elif (new_progress - prev_progress > 0):
                    return 1
                elif (new_progress - prev_progress < 0):
                    return 2
            elif category == "art":
                prev_progress = self.prev_character_design + self.prev_background + self.prev_animation
                new_progress = self.character_design + self.background + self.animation
                if (new_progress == prev_progress ):
                    return 0
                elif (new_progress - prev_progress > 0):
                    return 1
                elif (new_progress - prev_progress < 0):
                    return 2
            else:
                #music
                prev_progress = self.prev_voice_acting + self.prev_op_ed + self.prev_ost
                new_progress = self.voice_acting + self.op_ed + self.ost
                if (new_progress == prev_progress ):
                    return 0
                elif (new_progress - prev_progress > 0):
                    return 1
                elif (new_progress - prev_progress < 0):
                    return 2
        #story
        @property

        def plot(self):
            return self._plot

        @plot.setter
        def plot(self,value):
            if 0 <= value <= 5:
                self._plot = value
            elif value >= 5:
                self._plot = 5
            elif value <= 0:
                self._plot = 0
           

        @property

        def storyboard(self):
            return self._storyboard

        @storyboard.setter
        def storyboard(self,value):
            if 0 <= value <= 5:
                self._storyboard = value
            elif value >= 5:
                self._storyboard = 5
            elif value <= 0:
                self._storyboard = 0

        @property

        def character_development(self):
            return self._character_development

        @character_development.setter
        def character_development(self,value):
            if 0 <= value <= 5:
                self._character_development = value
            elif value >= 5:
                self._character_development = 5
            elif value <= 0:
                self._character_development = 0

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
            elif value >= 5:
                self._character_design = 5
            elif value <= 0:
                self._character_design = 0

        @property

        def background(self):
            return self._background

        @background.setter
        def background(self,value):
            if 0 <= value <= 5:
                self._background = value
            elif value >= 5:
                self._background = 5
            elif value <= 0:
                self._background = 0

        @property

        def animation(self):
            return self._animation

        @animation.setter
        def animation(self,value):
            if 0 <= value <= 5:
                self._animation = value
            elif value >= 5:
                self._animation = 5
            elif value <= 0:
                self._animation = 0

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
            elif value >= 5:
                self._voice_acting = 5
            elif value <= 0:
                self._voice_acting = 0


        @property

        def op_ed(self):
            return self._op_ed

        @op_ed.setter
        def op_ed(self,value):
            if 0 <= value <= 5:
                self._op_ed = value
            elif value >= 5:
                self._op_ed = 5
            elif value <= 0:
                self._op_ed = 0


        @property

        def ost(self):
            return self._ost

        @ost.setter
        def ost(self,value):
            if 0 <= value <= 5:
                self._ost = value
            elif value >= 5:
                self._ost = 5
            elif value <= 0:
                self._ost = 0


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
            if value <= 0:
                renpy.jump("dead_no_funds")
            else:
                self._funds = value

        @property

        def marketing(self):
            return self._marketing

        @marketing.setter
        def marketing(self,value):
            self._marketing = value

        @property

        def quality_check(self):
            return self._quality_check

        @quality_check.setter
        def quality_check(self,value):
            self._quality_check = value
            




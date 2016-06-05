init -100 python:
    #TO DO add hard limit for anime , tasks , stats so they can't go out of max limit
    class Anime(object):
        def __init__(self,name):
            self.name = name
            #main
            self._funds = 0
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
            self._op_and_ed = 0
            self._ost = 0
            self._music_bonus = 0
            self._music_progress = 0

            #Misc
            self._quality_check = 0
            self._marketing = 0

        #story
        @property

        def plot(self):
            return self._plot

        @plot.setter
        def plot(self,value):
            self._plot = value

        @property

        def storyboard(self):
            return self._storyboard

        @storyboard.setter
        def storyboard(self,value):
            if value > 5:
                value -= value % 5
            self._storyboard = value

        @property

        def character_development(self):
            return self._character_development

        @character_development.setter
        def character_development(self,value):
            self._character_development = value


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
            self._character_design = value

        @property

        def background(self):
            return self._background

        @background.setter
        def background(self,value):
            self._background = value


        @property

        def animation(self):
            return self._animation

        @animation.setter
        def animation(self,value):
            self._animation = value


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
            self._voice_acting = value


        @property

        def op_and_ed(self):
            return self._op_and_ed

        @op_and_ed.setter
        def op_and_ed(self,value):
            self._op_and_ed = value


        @property

        def ost(self):
            return self._ost

        @ost.setter
        def ost(self,value):
            self._ost = value


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
            




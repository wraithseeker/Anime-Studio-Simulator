init -100 python:
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
            # Art
            self._character_design = 0
            self._background = 0
            self._animation = 0
            self._art_bonus = 0
            #Music
            self._voice_acting = 0
            self._op_and_ed = 0
            self._ost = 0
            self._music_bonus = 0

            #Misc
            self._quality_check = 0
            self._marketing = 0
        def AddSomeStats(self):
            self.plot = 1
            renpy.notify( "Some Message.")


        @property

        def plot(self):
            return self._plot

        @plot.setter
        def plot(self,value):
            self._plot = value
            




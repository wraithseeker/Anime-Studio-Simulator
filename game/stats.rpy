init -100 python:
    class Stats(object):
        def __init__(self,name):
            self.name = name
            self._management = 0
            self._stress = 2
            self._proficiency = 0
            self._happiness = 10

            
        @property

        def stress(self):
            return self._stress

        @stress.setter
        def stress(self,value):
            if 0 <= value <= 10:
                self._stress = value
            else:
                renpy.notify( "Stress must be between 0 to 10.")

        @property
        def happiness(self):
            return self._happiness

        @happiness.setter
        def happiness(self,value):
            if 0 <= value <= 10:
                self._happiness = value
            else:
               # renpy.notify( "Happiness must be between 0 to 10.")
               pass

        @property
        def proficiency(self):
            return self._proficiency

        @proficiency.setter
        def proficiency(self,value):
            if 0.0 <= value <= 10.0:
                self._proficiency = value
            else:
                #current_proficiency = self.proficiency
                renpy.notify( "Proficiency must be between 0 to 10. Value is " + str(self._proficiency))

        @property
        def management(self):
            return self._management

        @management.setter
        def management(self,value):
            if 0 <= value <= 10:
                self._management = value
            else:
                #renpy.notify( "Management must be between 0 to 10.")
                pass



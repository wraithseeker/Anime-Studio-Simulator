init -100 python:
    class Stats(object):
        DEFAULT_STRESS = 2
        DEFAULT_HAPPINESS = 10
        def __init__(self,name):
            self.name = name
            self._management = 0
            self._stress = Stats.DEFAULT_STRESS
            self._proficiency = 0
            self._happiness = Stats.DEFAULT_HAPPINESS
            self.db_stats = ["stress","proficiency","happiness","management"]
            self.db_displayed_stats = []
            for i in range (0,len(self.db_stats)):
                setattr(self,"prev_" + self.db_stats[i],0)
            self.prev_happiness = Stats.DEFAULT_HAPPINESS
            self.prev_stress = Stats.DEFAULT_STRESS

        def storePreviousWeekValues(self):
            for i in range (0,len(self.db_stats)):
                setattr(self,"prev_" + self.db_stats[i],getattr(self,self.db_stats[i]))
            self.db_displayed_stats = []

        def getStatChanges(self,stat):
            current_stat = getattr(self,stat)
            prev_stats = getattr(self,"prev_" + stat)
            new_stats = current_stat - prev_stats
            if (current_stat == prev_stats):
                return
            positive = GREEN_COLOR + POSITIVE_SIGN
            negative = RED_COLOR + MINUS_SIGN
            end_tag = "{/color}"
            if (new_stats > 0 ):
                #increase in stats
                if stat == "stress":
                    text = RED_COLOR + POSITIVE_SIGN + stat + end_tag
                else:
                    text = positive + stat + end_tag
                self.db_displayed_stats.insert(0,text)
            else:
                #decrease in stats
                if stat == "stress":
                    text = GREEN_COLOR + MINUS_SIGN + stat + end_tag
                else:
                    text = negative + stat + end_tag
                self.db_displayed_stats.append(text)

        def updateDashboard(self):
            for i in range (0,len(self.db_stats)):
                self.getStatChanges(self.db_stats[i])

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



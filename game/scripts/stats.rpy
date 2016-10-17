init -100 python:
    class Stats(object):
        DEFAULT_STRESS = 5
        DEFAULT_HAPPINESS = 5
        DEFAULT_PROFICIENCY = 0
        MINIMUM_HAPPINESS_TO_DIE = 0
        MAXIMUM_STRESS_TO_DIE = 10
        def __init__(self,name):
            self.name = name
            self._management = 0
            self._stress = Stats.DEFAULT_STRESS
            self._proficiency = Stats.DEFAULT_PROFICIENCY
            self._happiness = Stats.DEFAULT_HAPPINESS
            self.db_stats = ["stress","proficiency","happiness","management"]
            self.db_displayed_stats = []
            for i in range (0,len(self.db_stats)):
                setattr(self,"prev_" + self.db_stats[i],0)
            self.prev_happiness = Stats.DEFAULT_HAPPINESS
            self.prev_stress = Stats.DEFAULT_STRESS
        def setRandomStats(self):
            self.happiness = renpy.random.randint(5,10)
            self.stress = renpy.random.randint(3, 6)
            self.proficiency = renpy.random.randint(0, 2)
            if self.name == "Yukari":
                self.management = renpy.random.randint(1,3)

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
            if value >= Stats.MAXIMUM_STRESS_TO_DIE:
                if self.name != "Yukari":
                    renpy.call_in_new_context("dead_burnout",self)
                else:
                    renpy.call_in_new_context("dead_burnout_yukari")
            elif value <= 0:
                self._stress = 0
            elif 0 <= value <= Stats.MAXIMUM_STRESS_TO_DIE:
                self._stress = value 

        @property
        def happiness(self):
            return self._happiness

        @happiness.setter
        def happiness(self,value):
            if value <= Stats.MINIMUM_HAPPINESS_TO_DIE:
                if self.name != "Yukari":
                    renpy.call_in_new_context("dead_burnout",self)
                else:
                    renpy.call_in_new_context("dead_burnout_yukari")
            elif value >= 10.0:
                self._happiness = 10
            elif Stats.MINIMUM_HAPPINESS_TO_DIE <= value <= 10:
                self._happiness = value

        @property
        def proficiency(self):
            return self._proficiency

        @proficiency.setter
        def proficiency(self,value):
            if value <= 0:
                self._proficiency = 0
            elif value >= 10:
                self._proficiency = 10
            else:
                self._proficiency = value

        @property
        def management(self):
            return self._management

        @management.setter
        def management(self,value):
            if value <= 0:
                self._management = 0
            elif value >= 10:
                self._management = 10
            else:
                self._management = value



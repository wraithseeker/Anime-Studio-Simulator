init -1000 python:
    class RandomEventsHolder(object):
        def __init__(self):
            self.list = []
        def remove(self,item):
            for event in self.list:
                if item in event[:]:
                    event.remove(item)
                    #print("Removed " + str(item) + " from " + str(event))
        def calculateEvents(self):
            self.list = [self.wk_4_to_12,self.wk_10_to_12,self.all]
            self.choice_holder = self.wk_4_to_12 + self.wk_10_to_12 + self.all
        def random(self,included=None):
            if self.choice_holder:
                if included:
                    #additional filter conditions
                    events = []
                    for included_events in included:
                        events = events + included_events
                    filtered_event = [x for x in self.choice_holder if x in events]
                    choice = renpy.random.choice(filtered_event)
                    self.remove(choice)
                    self.calculateEvents()
                    return choice
                else:
                    choice = renpy.random.choice(self.choice_holder)
                    self.remove(choice)
                    self.calculateEvents()
                    return choice
            #print("No more Random Events, What are you doing?")
            return
        def remaining(self):
            self.calculateEvents()
            return self.choice_holder
        def emptyList(self,list):
            print(list)
            list[:] = []
        def singleRandom(self,list):
            if self.choice_holder:
                choice = renpy.random.choice(list)
                self.remove(choice)
                self.calculateEvents()
                return choice
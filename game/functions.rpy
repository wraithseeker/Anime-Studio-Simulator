﻿init -100 python:
    def getRandomCompany():
        global random_company
        company = renpy.random.choice(random_company)
        random_company.remove(company)
        return company
    def getRandomName():
        global random_names
        name = renpy.random.choice(random_names)
        random_names.remove(name)
        return name
        
    def nextDay():
        global current_day
        global current_date
        if current_day < 5:
            # if its not at the end of the week, cycle through days
            current_day += 1
        else:
            # revert back to monday
            current_day = 0
        current_date += datetime.timedelta(days=1)
    def currentDay():
        global current_day
        return days_array[current_day]

    def currentDate():
        global current_date
        #date = current_date.strftime('%m/%d')
        date = '{d.month}/{d.day}'.format(d=current_date)
        return date

    def EndTurn():
        global anime
        global outsource
        anime.storePreviousWeekValues()
        StorePreviousWeekValuesForStats()
        EndTasks()
        outsource.reset()
        ResetUpgrades()
    def ResetUpgrades():
        global yukari_upgrade
        global mayumi_upgrade
        global shunsuke_upgrade
        global sumiko_upgrade
        global yuuko_upgrade
        yukari_upgrade = Outsource.NOT_SELECTED
        mayumi_upgrade = Outsource.NOT_SELECTED
        shunsuke_upgrade = Outsource.NOT_SELECTED
        sumiko_upgrade = Outsource.NOT_SELECTED
        yuuko_upgrade = Outsource.NOT_SELECTED

    def StorePreviousWeekValuesForStats():
        yukari_stats.storePreviousWeekValues()
        yuuko_stats.storePreviousWeekValues()
        mayumi_stats.storePreviousWeekValues()
        sumiko_stats.storePreviousWeekValues()
        shunsuke_stats.storePreviousWeekValues()


    def AddTaskStats(person,stats):
        for i in range(0,len(person)):
            if person[i].selected:
                person[i].addStats(anime,stats)

    def EndTasks():
        global yukari_tasks
        global yuuko_tasks
        global sumiko_tasks
        global shunsuke_tasks
        global mayumi_tasks
        global task_ready
        global yukari_task_selected
        global yuuko_task_selected
        global sumiko_task_selected
        global shunsuke_task_selected
        global mayumi_task_selected
        AddTaskStats(yukari_tasks,yukari_stats)
        AddTaskStats(yuuko_tasks,yuuko_stats)
        AddTaskStats(sumiko_tasks,sumiko_stats)
        AddTaskStats(shunsuke_tasks,shunsuke_stats)
        AddTaskStats(mayumi_tasks,mayumi_stats)
        ResetCharacterTask(yukari_tasks)
        ResetCharacterTask(yuuko_tasks)
        ResetCharacterTask(sumiko_tasks)
        ResetCharacterTask(shunsuke_tasks)
        ResetCharacterTask(mayumi_tasks)
        yukari_task_selected = False
        yuuko_task_selected = False
        mayumi_task_selected = False
        shunsuke_task_selected = False
        sumiko_task_selected = False
        # for i in range(0,len(item)):
        #     item[i].selected = False

    def ResetCharacterTask(item):
        for i in range(0,len(item)):
            item[i].selected = False

    def UpdateProgressReport():
        anime.updateDashboard()
        yukari_stats.updateDashboard()
        mayumi_stats.updateDashboard()
        shunsuke_stats.updateDashboard()
        sumiko_stats.updateDashboard()
        yuuko_stats.updateDashboard()
       

    def UpgradeCharacters(yukari,mayumi,shunsuke,sumiko,yuuko):
        global upgrade_tooltip
        global upgrade_tooltip_color
        global upgrade_selection_count
        global yukari_upgrade
        global mayumi_upgrade
        global shunsuke_upgrade
        global sumiko_upgrade
        global yuuko_upgrade
        if anime.funds >= upgrade_proficiency_cost * upgrade_selection_count:
            message = "Proficiency successfully increased for"
            upgrade_success = False
            if yukari_upgrade == Outsource.SELECTED:
                setattr(yukari,"proficiency",getattr(yukari,"proficiency") + upgrade_proficiency_value)
                message = message + " \nYukari"
                upgrade_success = True
                yukari_upgrade = Outsource.DISABLED
            if mayumi_upgrade == Outsource.SELECTED:
                setattr(mayumi,"proficiency",getattr(mayumi,"proficiency") + upgrade_proficiency_value)
                message = message + " \nMayumi"
                upgrade_success = True
                mayumi_upgrade = Outsource.DISABLED
            if shunsuke_upgrade == Outsource.SELECTED:
                setattr(shunsuke,"proficiency",getattr(shunsuke,"proficiency") + upgrade_proficiency_value)
                message = message + " \nShunsuke"
                upgrade_success = True
                shunsuke_upgrade = Outsource.DISABLED
            if sumiko_upgrade == Outsource.SELECTED:
                setattr(sumiko,"proficiency",getattr(sumiko,"proficiency") + upgrade_proficiency_value)
                message = message + " \nSumiko"
                upgrade_success = True
                sumiko_upgrade = Outsource.DISABLED
            if yuuko_upgrade == Outsource.SELECTED:
                setattr(yuuko,"proficiency",getattr(yuuko,"proficiency") + upgrade_proficiency_value)
                message = message + " \nYuuko"
                upgrade_success = True
                yuuko_upgrade = Outsource.DISABLED

            if upgrade_success:
                upgrade_tooltip = "Success!"
                upgrade_tooltip_color = "#2ecc71"
                anime.funds -= upgrade_proficiency_cost * upgrade_selection_count
                upgrade_selection_count = 0
                ui.timer(2.0,SetVariable("upgrade_tooltip",""))
                renpy.restart_interaction()
        else:
            upgrade_tooltip = "Not enough funds!"
            upgrade_tooltip_color = "#c0392b"
            ui.timer(2.0,SetVariable("upgrade_tooltip",""))
            renpy.restart_interaction()
    def OutsourceAnime():
        global outsource_tooltip
        global upgrade_tooltip_color
        global outsource
        global anime
        if anime.funds >= outsource.cost * outsource.selection_count:
            outsource_success = outsource.start()
            if outsource_success:
                outsource_tooltip = "Success!"
                upgrade_tooltip_color = "#2ecc71"
                anime.funds -= outsource.cost * outsource.selection_count
                outsource.selection_count = 0
                ui.timer(2.0,SetVariable("outsource_tooltip",""))
                anime.story_progress = int((anime.plot + anime.storyboard + anime.character_development) / 15.0 * 100.0)
                anime.art_progress = int((anime.character_design + anime.background + anime.animation) / 15.0 * 100.0)
                anime.music_progress = int((anime.op_ed + anime.ost + anime.voice_acting) / 15.0 * 100.0)
                renpy.restart_interaction()      
        else:
            outsource_tooltip = "Not enough funds!"
            upgrade_tooltip_color = "#c0392b"
            ui.timer(2.0,SetVariable("outsource_tooltip",""))
            renpy.restart_interaction()
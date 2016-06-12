init -100 python:

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


       

    def UpgradeCharacters(yukari,mayumi,shunsuke,sumiko,yuuko):
        global upgrade_tooltip
        global upgrade_tooltip_color
        global upgrade_selection_count
        if anime.funds >= upgrade_proficiency_cost * upgrade_selection_count:
            message = "Proficiency successfully increased for"
            if yukari_upgrade_selected:
                setattr(yukari,"proficiency",getattr(yukari,"proficiency") + upgrade_proficiency_value)
                message = message + " \nYukari"
            if mayumi_upgrade_selected:
                setattr(mayumi,"proficiency",getattr(mayumi,"proficiency") + upgrade_proficiency_value)
                message = message + " \nMayumi"
            if shunsuke_upgrade_selected:
                setattr(shunsuke,"proficiency",getattr(shunsuke,"proficiency") + upgrade_proficiency_value)
                message = message + " \nShunsuke"
            if sumiko_upgrade_selected:
                setattr(sumiko,"proficiency",getattr(sumiko,"proficiency") + upgrade_proficiency_value)
                message = message + " \nSumiko"
            if yuuko_upgrade_selected:
                setattr(yuuko,"proficiency",getattr(yuuko,"proficiency") + upgrade_proficiency_value)
                message = message + " \nYuuko"

            if yukari_upgrade_selected or mayumi_upgrade_selected or shunsuke_upgrade_selected or sumiko_upgrade_selected or yuuko_upgrade_selected:
                upgrade_tooltip = "Success!"
                upgrade_tooltip_color = "#2ecc71"
                anime.funds -= upgrade_proficiency_cost * upgrade_selection_count
                ui.timer(2.0,SetVariable("upgrade_tooltip",""))
                renpy.restart_interaction()
        else:
            upgrade_tooltip = "Not enough funds!"
            upgrade_tooltip_color = "#c0392b"
            ui.timer(2.0,SetVariable("upgrade_tooltip",""))
            renpy.restart_interaction()
    def OutsourceAnime(anime):
        global outsource_tooltip
        global upgrade_tooltip_color
        selected_number = OutsourceGetSelectionCount()
        if anime.funds >= outsource_cost * selected_number:
            if outsource_plot_selected:
                setattr(anime,"plot",getattr(anime,"plot") + outsource_value)
            if outsource_character_dev_selected:
                setattr(anime,"character_development",getattr(anime,"character_development") + outsource_value)
            if outsource_storyboard_selected:
                setattr(anime,"storyboard",getattr(anime,"storyboard") + outsource_value)
            if outsource_character_design_selected:
                setattr(anime,"character_design",getattr(anime,"character_design") + outsource_value)
            if outsource_animation_selected:
                setattr(anime,"animation",getattr(anime,"animation") + outsource_value)
            if outsource_background_selected:
                setattr(anime,"background",getattr(anime,"background") + outsource_value)
            if outsource_op_ed_selected:
                setattr(anime,"op_ed",getattr(anime,"op_ed") + outsource_value)
            if outsource_ost_selected:
                setattr(anime,"ost",getattr(anime,"ost") + outsource_value)
            if outsource_voice_acting_selected:
                setattr(anime,"voice_acting",getattr(anime,"voice_acting") + outsource_value)
            if outsource_marketing_selected:
                setattr(anime,"marketing",getattr(anime,"marketing") + outsource_value)
            if outsource_quality_check_selected:
                setattr(anime,"quality_check",getattr(anime,"quality_check") + outsource_value)


            if (outsource_plot_selected or outsource_character_dev_selected or outsource_storyboard_selected
            or outsource_character_design_selected or outsource_animation_selected or outsource_background_selected
            or outsource_op_ed_selected or outsource_ost_selected or outsource_voice_acting_selected
            or outsource_marketing_selected or outsource_quality_check_selected):
                outsource_tooltip = "Success!"
                upgrade_tooltip_color = "#2ecc71"
                anime.funds -= outsource_cost * selected_number
                ui.timer(2.0,SetVariable("outsource_tooltip",""))
                renpy.restart_interaction()
        else:
            outsource_tooltip = "Not enough funds!"
            upgrade_tooltip_color = "#c0392b"
            ui.timer(2.0,SetVariable("outsource_tooltip",""))
            renpy.restart_interaction()

    def OutsourceGetSelectionCount():
        number = 0
        if outsource_plot_selected:
            number += 1
        if outsource_character_dev_selected:
            number += 1
        if outsource_storyboard_selected:
            number += 1
        if outsource_character_design_selected:
            number += 1
        if outsource_animation_selected:
            number += 1
        if outsource_background_selected:
            number += 1
        if outsource_op_ed_selected:
            number += 1
        if outsource_ost_selected:
            number += 1
        if outsource_voice_acting_selected:
            number += 1
        if outsource_marketing_selected:
            number += 1
        if outsource_quality_check_selected:
            number += 1
        return number


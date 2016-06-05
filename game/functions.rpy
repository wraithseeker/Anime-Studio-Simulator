init -100 python:

    def ResetTasksSelection():
        global yukari_tasks
        global yuuko_tasks
        global sumiko_tasks
        global shunsuke_tasks
        global mayumi_tasks
        ResetCharacterTask(yukari_tasks)
        ResetCharacterTask(yuukotasks)
        ResetCharacterTask(sumiko_tasks)
        ResetCharacterTask(shunsuke_tasks)
        ResetCharacterTask(mayumi_tasks)

    def ResetCharacterTask(item):
        for i in range(0,len(item)):
            item[i].selected = False
            

       

    def UpgradeCharacters(yukari,mayumi,shunsuke,sumiko,yuuko):
        global upgrade_tooltip
        global upgrade_tooltip_color
        selected_number = UpgradeGetSelectionCount()
        if anime.funds > upgrade_proficiency_cost * selected_number:
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
                upgrade_tooltip = "Upgrade Successful!"
                upgrade_tooltip_color = "#2ecc71"
                anime.funds -= upgrade_proficiency_cost * selected_number
                ui.timer(2.0,SetVariable("upgrade_tooltip",""))
                renpy.restart_interaction()
        else:
            upgrade_tooltip = "Not enough money!"
            upgrade_tooltip_color = "#c0392b"
            ui.timer(2.0,SetVariable("upgrade_tooltip",""))
            renpy.restart_interaction()

    def UpgradeGetSelectionCount():
        number = 0
        if yukari_upgrade_selected:
            number += 1
        if mayumi_upgrade_selected:
            number += 1
        if shunsuke_upgrade_selected:
            number += 1
        if sumiko_upgrade_selected:
            number += 1
        if yuuko_upgrade_selected:
            number += 1
        return number

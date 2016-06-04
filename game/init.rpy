init: 
    $_game_menu_screen = "navigation"
    $upgrade_proficiency_value = 0.5
    python:
        #A list of allowed stats to be modified during the game
        anime_stats = ["plot","storyboard","character_development",
                        "character_design","background","animation",
                        "voice_acting","op_and_ed","ost",
                        "quality_check","marketing","funds"]
        char_stats = ["stress","proficiency","happiness","human_relations"]
        anime = Anime("Anime Name")
        yukari_tasks = [Tasks("Marketing","Do some Marketing",storyboard = 3,plot=-1)
                        ,Tasks("Networking","Do some networking",plot=2)
                        ,Tasks("Practise","Do some practise",plot=3)
                        ,Tasks("Relax","Relax",plot=4)]

        yuuko_tasks = [Tasks("Sketch Character","Sketch Character",storyboard = 3,plot=-1)
                        ,Tasks("Doodle","Doodling",plot=2)
                        ,Tasks("Relax","Focus on relaxing",plot=3)]

        sumiko_tasks = [Tasks("Sketch Background","Sketch Character",storyboard = 3,plot=-1)
                        ,Tasks("Practise Drawing","Doodling",plot=2)
                        ,Tasks("Relax","Focus on relaxing",plot=3)]

        mayumi_tasks = [Tasks("Compose Music","Sketch Character",storyboard = 3,plot=-1)
                        ,Tasks("Practise","Doodling",plot=2)
                        ,Tasks("Relax","Focus on relaxing",plot=3)]

        shunsuke_tasks = [Tasks("Write Story","Sketch Character",storyboard = 3,plot=-1)
                        ,Tasks("Practise Writing","Doodling",plot=2)
                        ,Tasks("Relax","Focus on relaxing",plot=3)]
        yukari_stats = Stats("Yukari")
        mayumi_stats = Stats("Mayumi")
        sumiko_stats = Stats("Sumiko")
        yuuko_stats = Stats("Yuuko")
        shunsuke_stats = Stats("Shunsuke")


        def UpgradeCharacters(yukari,mayumi,shunsuke,sumiko,yuuko):
            global upgrade_tooltip
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
                ui.timer(2.0,SetVariable("upgrade_tooltip",""))
                renpy.restart_interaction()

    #game variables
    $game_casual = False
    $task_ready = False
    #upgrade screen
    $upgrade_tooltip_default = "Send your team for training!"
    $upgrade_tooltip_complete = "Upgrade successful!"
    $upgrade_tooltip = ""
    $yukari_upgrade_selected = False
    $yuuko_upgrade_selected = False
    $sumiko_upgrade_selected = False
    $mayumi_upgrade_selected = False
    $shunsuke_upgrade_selected = False
    #task screen

    #boolean to know whether they are selected
    $somenumber = False
    $yukari_task_selected = False
    $yuuko_task_selected = False
    $sumiko_task_selected = False
    $mayumi_task_selected = False
    $shunsuke_task_selected = False

    #positions for images
    $pos_farleft = Position(xalign = -0.045,yalign = 1.0)
    $pos_left = Position(xalign = 0.18,yalign = 1.0)
    $pos_middle = Position(xalign = 0.5,yalign = 1.0)
    $pos_middleright = Position(xalign = 0.65,yalign = 1.0)
    $pos_farright = Position(xalign = 1.1,yalign = 1.0)
    $pos_right = Position(xalign = 0.92,yalign = 1.0)


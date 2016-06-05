init: 
    $_game_menu_screen = "navigation"
    $upgrade_proficiency_value = 0.5
    $upgrade_proficiency_cost = 2
    python:
        #A list of allowed stats to be modified during the game
        anime_stats = ["plot","character_development","storyboard",
                        "character_design","background","animation",
                        "voice_acting","op_and_ed","ost",
                        "quality_check","marketing","funds"]
        char_stats = ["stress","proficiency","happiness","human_relations"]

        anime = Anime("Anime Name")
        anime.funds = 20
        anime.plot = 2.5
        anime.storyboard = 3
        anime.character_development = 0.5


        anime.character_design = 1.5
        anime.background = 2.5
        anime.animation = 3.5

        anime.ost = 5

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

    #game variables
    $game_casual = False
    $task_ready = False
    $upgrade_tooltip_color = "#2ecc71"
    #15 stars is the max number of stars we have, * 100 to convert it to percentage
    $anime_story_progress = int((anime.plot + anime.storyboard + anime.character_development) / 15 * 100)
    $anime_art_progress = int((anime.character_design + anime.background + anime.animation) / 15 * 100)
    $anime_music_progress = int((anime.op_and_ed + anime.ost + anime.voice_acting) / 15 * 100)

    #upgrade screen
    $upgrade_tooltip_default = "Send your team for training! This will increase their Proficiency stats."
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


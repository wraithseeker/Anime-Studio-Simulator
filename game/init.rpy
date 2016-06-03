init: 
    $_game_menu_screen = "navigation"

    python:
        anime_stats = ["plot","story"]
        anime = Anime("Some Anime Name")
        anime.plot = 1
        anime.story = 5
        yukari_tasks = [Tasks("Marketing","Do some Marketing",story = 3,plot=-1)
                        ,Tasks("Quality Check","Do some quality check",plot=2)
                        ,Tasks("Practise","Do some practise",plot=3)
                        ,Tasks("Doodling","Doodle",plot=4)]
        Yukari_stats = Stats("Yukari")
        Mayumi_stats = Stats("Mayumi")
        Sumiko_stats = Stats("Sumiko")
        Yuuko_stats = Stats("Yuuko")
        Shunsuke_stats = Stats("Shunsuke")
    #upgrade screen
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

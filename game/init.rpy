init: 
    $_game_menu_screen = "navigation"

    python:
        yukari_tasks = [Tasks("Marketing","Do some Marketing"),
                        Tasks("Report ","Do some Reporting"),
                        Tasks("Motivation Speech","Motivate People"),
                        Tasks("Quality Check", "Check on some anime work")]
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
    $yukari_task_selected = False
    $yuuko_task_selected = False
    $sumiko_task_selected = False
    $mayumi_task_selected = False
    $shunsuke_task_selected = False

    #to highlight selection for each choice
    $yukari_task_01_s = False
    $yukari_task_02_s = False
    $yukari_task_03_s = False
    $yukari_task_04_s = False
    $yukari_tasks_array = [False,False,False,False]
    $yuuko_task_01_s = False
    $yuuko_task_02_s = False
    $yuuko_task_03_s = False
    $yuuko_task_04_s = False

    $sumiko_task_01_s = False
    $sumiko_task_02_s = False
    $sumiko_task_03_s = False
    $sumiko_task_04_s = False

    $mayumi_task_01_s = False
    $mayumi_task_02_s = False
    $mayumi_task_03_s = False
    $mayumi_task_04_s = False

    $shunsuke_task_01_s = False
    $shunsuke_task_02_s = False
    $shunsuke_task_03_s = False
    $shunsuke_task_04_s = False

    #positions for images
    $pos_farleft = Position(xalign = -0.045,yalign = 1.0)
    $pos_left = Position(xalign = 0.18,yalign = 1.0)
    $pos_middle = Position(xalign = 0.5,yalign = 1.0)
    $pos_middleright = Position(xalign = 0.65,yalign = 1.0)
    $pos_farright = Position(xalign = 1.1,yalign = 1.0)
    $pos_right = Position(xalign = 0.92,yalign = 1.0)

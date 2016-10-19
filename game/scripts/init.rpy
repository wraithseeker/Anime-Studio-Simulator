label start:
    #initialize the class objects at runtime here instead of python init so object will be saved
    $anime = Anime("Herb and Fox")
    #stats for characters
    $yukari_stats = Stats("Yukari")
    $yukari_stats.management = 1
    $yukari_stats.prev_management = 1
    $mayumi_stats = Stats("Mayumi")
    $sumiko_stats = Stats("Sumiko")
    $yuuko_stats = Stats("Yuuko")
    $shunsuke_stats = Stats("Shunsuke")
    $anime.setProgress()
    #Anime final score here
    $anime_score_components = (anime.plot + anime.character_development + anime.storyboard + anime.character_design + anime.background + anime.animation + anime.voice_acting +anime.op_ed + anime.ost ) 
    $anime_score_multipliers = (1 + yukari_stats.management * 0.05 + anime.marketing * 0.05 + anime.quality_check * 0.3)
    $anime_score = anime_score_components * anime_score_multipliers

    $anime.funds = 50
    $anime.plot = 1
    $anime.prev_plot = 1
    $UpdateProgressReport()
   
    #Random Events
    $rd_e_holder = RandomEventsHolder()
    $rd_e_holder.wk_4_to_12 = ["random_2","random_4","random_5","random_6","random_12"]
    $rd_e_holder.wk_4 = ["random_26"]
    $rd_e_holder.wk_5_to_7 = ["random_20","random_22"]
    $rd_e_holder.wk_5_to_10 = ["random_3","random_14",]
    $rd_e_holder.wk_6_to_8 = ["random_7"]
    $rd_e_holder.wk_10_to_12 = ["random_37","random_27"]
    $rd_e_holder.all = ["random_1","random_8","random_9","random_10","random_11","random_13","random_15","random_16",
                "random_17","random_18","random_19","random_21","random_23","random_24","random_25",
                "random_28","random_31","random_32","random_33","random_34","random_35",
                "random_36"]
    $rd_e_holder.help = ["random_29","random_30"]
    $rd_e_holder.calculateEvents()

    $random_company = ["Wadaka","Sokono","Kirodo","Matsura","Enshu","Nosata"
                        ,"Zekoy","Inoshi","Pokomi","Takiza","Kibono","Koiga","Vozobi"
                        ,"Asozo","Noyoko","Kibachi","Tamaza","Kirodo","Shinu","Pokomi","Koiga"]
    #animation and recording director names
    $random_names = ["Hayate","Haruto","Kaito","Nobu","Yuuto","Yoshiro","Takeshi","Souta","Hiroyuki","Ryosei"]
    $random_va_female = ["Shina","Kaoru","Kagami","Yoshike","Shizue","Akemi"]
    $random_va_male = ["Ryuichi","Motoki","Naizen","Naosuke","Seinosuke","Akihisa"]
    $anim_studio_dir = getRandomName()
    $anim_studio_expensive = getRandomCompany() + " Studios"
    $anim_studio_cheap = getRandomCompany() + " Studio"
    $anim_studio = "Default Studios"
    $va_choice = "Talent Agency"
    #voice actor automatically defaults to harem
    $va_a = "Bradley"
    $va_b = getRandomFemaleName()
    $va_c = getRandomFemaleName()
    $va_studio = getRandomCompany() + " Studio"
    $va_director = getRandomName()
    $investor_marketing = True
    $guerilla_marketing = False #from week 2_3
    $week_7_people_choices = ["Yuuko","Sumiko","Shunsuke","Mayumi"]
    $week_7_current_choice = ""
    $week_8_cheap_studio_visited = False
    $trailer_choice = "Reuse"
    #Trailer choices include "Reuse" or "New"
    $wk_9_forgot_home = True
    $website_choice = "Professional"
    #available website choices = "Professional","Shunsuke","Free"

    #Engine stuff
    # current_date e.g '8/30'
    $current_week = 1
    $days_array = ["Mon","Tues","Wed","Thur","Fri","Sat","Sun"]
    $current_day = 5
    $current_date = datetime.date(2016,3,12) 
    #ends at 6/21, starts at 3/21, pregame = 3/12
    $game_casual = False
    $task_ready = False
    $side_nav_interaction = True
    $show_floating_buttons = True
    $initial_week = True
    $upgrade_tooltip_color = "#2ecc71"
    #Upgrade engine stuff
    $yukari_current_u_text = renpy.random.choice(yukari_upgrade_text)
    $yuuko_current_u_text = renpy.random.choice(yuuko_upgrade_text)
    $mayumi_current_u_text = renpy.random.choice(mayumi_upgrade_text)
    $sumiko_current_u_text = renpy.random.choice(sumiko_upgrade_text)
    $shunsuke_current_u_text = renpy.random.choice(shunsuke_upgrade_text)
    $yukari_upgrade = Outsource.NOT_SELECTED
    $yuuko_upgrade = Outsource.NOT_SELECTED
    $sumiko_upgrade = Outsource.NOT_SELECTED
    $mayumi_upgrade = Outsource.NOT_SELECTED
    $shunsuke_upgrade = Outsource.NOT_SELECTED
    $upgrade_tooltip = ""
    $upgrade_selection_count = 0
    #Outsource engine stuff
    $outsource_tooltip = ""
    $outsource.selection_count = 0
    #Task engine stuff
    #boolean to know whether they are selected
    $yukari_task_selected = False
    $yuuko_task_selected = False
    $sumiko_task_selected = False
    $mayumi_task_selected = False
    $shunsuke_task_selected = False

    #jump week_0_1
    #jump week_5_1
    jump week_12_5
    #jump random_10


init python:
    import datetime
    import copy
    GREEN_COLOR = "{color=#1E824C}"
    RED_COLOR = "{color=#C0392B}"
    MINUS_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}- {/size}{/font}"
    POSITIVE_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}+ {/size}{/font}"
    CLOSE_COLOR_TAG = "{/color}"

init: 
    $_game_menu_screen = "navigation"
    python:
        #A list of allowed stats to be modified during the game
        anime_stats = ["plot","character_development","storyboard",
                        "character_design","background","animation",
                        "voice_acting","op_ed","ost",
                        "quality_check","marketing","funds"]
        char_stats = ["proficiency","happiness","management","stress"]

        relax_task = Tasks("Relax","Take it easy today.",happiness=1,stress=-2)

        yukari_first_task = Tasks("Networking","Mingle with people in the anime industry.",marketing=0.5,management=1,stress=1)
        yukari_second_task = Tasks("Storyboards","Work on the storyboards for [anime.name].",storyboard=0.5,stress=1)
        yukari_third_task = Tasks("Networking","Make new connections to increase [anime.name]'s visibility.",marketing=0.5,management=1,stress=1)
        yukari_raise_funds = Tasks("Raise Funds","Raise money for [anime.name].",funds=2,stress=1,happiness=-1)
        yukari_read_books = Tasks("Read Books","Read books to learn more about making anime.",proficiency=1,happiness=-1)

        mayumi_first_task = Tasks("Compose Music","Work on ideas for the OST of [anime.name].",ost=0.5,stress=1)
        mayumi_second_task = Tasks("Compose Music","Compose tracks for the OST.",ost=0.5,stress=1)
        mayumi_third_task = Tasks("Voice Acting"," Find voice actors for [anime.name].",voice_acting=0.5,stress=1)
        mayumi_fourth_task = Tasks("OP & ED","Compose the opening & ending songs for [anime.name].",op_ed=0.5,stress=1)
        mayumi_fifth_task = Tasks("Compose Music","Finalize the soundtrack for [anime.name].",ost=0.5,stress=1)
        mayumi_practise = Tasks("Practice","Get inspiration from other composers and try new musical techniques.",proficiency=1,happiness=-1)

        yuuko_first_task = Tasks("Sketch Characters","Sketch potential character designs.",character_design=0.5,stress=1)
        yuuko_second_task = Tasks("Draw Characters","Finalize and improve character designs.",character_design=0.5,stress=1)
        yuuko_third_task =  Tasks("Animation","Work on the animation for [anime.name].",animation=0.5,stress=1)

        sumiko_first_task = Tasks("Sketch Backgrounds","Sketch potential locations and environments.",background=0.5,stress=1)
        sumiko_second_task = Tasks("Draw Backgrounds","Draw and improve the final backgrounds.",background=0.5,stress=1)
        sumiko_third_task =  Tasks("Animation","Work on the animation for [anime.name].",animation=0.5,stress=1)
        sumiko_practise = Tasks("Doodle","Doodle simple art while working.",proficiency=1,happiness=-1)

        shunsuke_first_task = Tasks("Writing","Work on the scenario for [anime.name].",plot = 0.5,stress=1)
        shunsuke_second_task = Tasks("Writing","Flesh out the character development of [anime.name]'s cast.",character_development=0.5,stress=1)
        shunsuke_third_task = Tasks("Writing","Work on the storyboards for [anime.name].",storyboard=0.5,stress=1)
        shunsuke_practise = Tasks("Practice","Hone your writing skills",proficiency=1,happiness=-1)

        yukari_tasks = [yukari_first_task,yukari_raise_funds,yukari_read_books,copy.deepcopy(relax_task)]
        yuuko_tasks = [yuuko_first_task,copy.deepcopy(sumiko_practise),copy.deepcopy(relax_task)]
        sumiko_tasks = [sumiko_first_task,copy.deepcopy(sumiko_practise),copy.deepcopy(relax_task)]
        mayumi_tasks = [mayumi_first_task,mayumi_practise,copy.deepcopy(relax_task)]
        shunsuke_tasks = [shunsuke_first_task,shunsuke_practise,copy.deepcopy(relax_task)]

    #upgrade screen
    $upgrade_tooltip_default = "Send your team out for training! This will increase their Proficiency stats."
    $upgrade_tooltip_complete = "Success!"
    $yukari_upgrade_text = ["Send Yukari to meet veterans in the anime industry and broaden her knowledge of the business."
                            ,"Popular anime directors are holding a panel discussion. Send Yukari to attend."
                            ,"Enroll Yukari in a short, intensive leadership course."
                            ,"Get permission for Yukari to observe other anime studios."]
    $yuuko_upgrade_text = ["Pair Yuuko with a professional artist in the anime industry"
                            ,"Ask an art circle to critique Yuuko's work."
                            ,"Send Yuuko to an advanced art class."
                            ,"Give Yuuko time to research specific artistic techniques."]
    $sumiko_upgrade_text = ["Give Sumiko time to meditate and trek in the nearby mountains."
                            ,"Ask a professional anime artist to critique Sumiko's work."
                            ,"Send Sumiko to an advanced art class. "
                            ,"Send Sumiko to browse local art museums for inspiration."]
    $mayumi_upgrade_text = ["Send Mayumi to a musical boot camp where she can hone her skills."
                            ,"Pair Mayumi with a professional musician in the anime industry."
                            ,"Enroll Mayumi in an advanced musical composition course."
                            ,"Give Mayumi a highly-recommended book on composing music."]
    $shunsuke_upgrade_text = ["Send Shunsuke to a writing workshop."
                            ,"Invite a veteran writer to review Shunsuke's writing."
                            ,"Convince Shunsuke to join a local critique group."
                            ,"Send Shunsuke to attend discussion panels held by published writers."]                      
    #outsource screen
    $outsource = Outsource()
    $outsource.cost = 5
    $outsource.value = 1
    $upgrade_proficiency_value = 1
    $upgrade_proficiency_cost = 12

    #positions for images
    $pos_farleft = Position(xalign = -0.045,yalign = 1.0)
    $pos_left = Position(xalign = 0.18,yalign = 1.0)
    $pos_middle = Position(xalign = 0.5,yalign = 1.0)
    $pos_middleright = Position(xalign = 0.65,yalign = 1.0)
    $pos_middleright_half = Position(xalign = 0.75,yalign = 1.0)
    $pos_farright = Position(xalign = 1.0,yalign = 1.0)
    $pos_right = Position(xalign = 0.92,yalign = 1.0)
    $pos_outerright = Position(xalign = 1.1,yalign = 1.0)
    $pos_textbox_right = Position(xalign = 0.85,yalign=1.0)
    $va_pos_a = Position(xalign=0.60,yalign=1.0)
    $va_pos_b = Position(xalign = 1.1,yalign = 1.0)
    $va_pos_c = Position(xalign=0.85,yalign=1.0)

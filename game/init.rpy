label start:
    #initialize the class objects at runtime here instead of python init so object will be saved
    $anime = Anime("Macross Delta")
    #stats for characters
    $yukari_stats = Stats("Yukari")
    $mayumi_stats = Stats("Mayumi")
    $sumiko_stats = Stats("Sumiko")
    $yuuko_stats = Stats("Yuuko")
    $shunsuke_stats = Stats("Shunsuke")
    #some placeholder values
    # $yukari_stats.proficiency = renpy.random.randint(1,10)
    # $yuuko_stats.proficiency = renpy.random.randint(1,10)
    # $sumiko_stats.proficiency = renpy.random.randint(1,10)
    # $mayumi_stats.proficiency = renpy.random.randint(1,10)
    # $shunsuke_stats.proficiency = renpy.random.randint(1,10)
    #15 stars is the max number of stars we have, * 100 to convert it to percentage
    $anime.story_progress = int((anime.plot + anime.storyboard + anime.character_development) / 15.0 * 100.0)
    $anime.art_progress = int((anime.character_design + anime.background + anime.animation) / 15.0 * 100.0)
    $anime.music_progress = int((anime.op_ed + anime.ost + anime.voice_acting) / 15.0 * 100.0)

    $anime.funds = 20
    $anime.plot = 2.5
    $anime.prev_plot = 2.5
    $anime.storyboard = 3
    $anime.character_development = 0.5
    $anime.prev_character_design = 1
    $anime.character_design = 1.5
    $anime.background = 2
    $anime.animation = 2
    $anime.prev_background = 3
    $anime.prev_animation = 3
    $UpdateProgressReport()

    #jump game_start
    jump week_11_6

init python:
    import datetime
    GREEN_COLOR = "{color=#1E824C}"
    RED_COLOR = "{color=#C0392B}"
    MINUS_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}- {/size}{/font}"
    POSITIVE_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}+ {/size}{/font}"
    CLOSE_COLOR_TAG = "{/color}"

init: 
    $_game_menu_screen = "navigation"
    $upgrade_proficiency_value = 0.5
    $upgrade_proficiency_cost = 2
    python:
        #A list of allowed stats to be modified during the game
        anime_stats = ["plot","character_development","storyboard",
                        "character_design","background","animation",
                        "voice_acting","op_ed","ost",
                        "quality_check","marketing","funds"]
        char_stats = ["proficiency","happiness","management","stress"]
        yukari_tasks = [Tasks("Raise Funds","Raise some money for [anime.name].",funds=1,stress=1)
                        ,Tasks("Networking","Mingle around with people in the anime industry.",marketing=1,management=3,stress=2)
                        ,Tasks("Read Books","Read books for knowledge.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

        yuuko_tasks = [Tasks("Sketch Character","Sketch some character designs.",character_design=1,stress=1)
                        ,Tasks("Doodle","Doodle on a piece of paper.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

        sumiko_tasks = [Tasks("Sketch Background","Sketch some backgrounds.",background=1,stress=-1)
                        ,Tasks("Doodle","Doodle on a piece of paper.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

        mayumi_tasks = [Tasks("Compose Music","Compose OST for [anime.name].",ost=1,stress=1)
                        ,Tasks("Practice","Get inspiration from other artists.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

        shunsuke_tasks = [Tasks("Writing","Work on the scenario for [anime.name].",storyboard = 1,stress=0)
                        ,Tasks("Practice","Hone your writing skills",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

    #Random Events
    $random_events_holder = RandomEventsHolder()
   
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
    $outsource.cost = 1
    $outsource.value = 1
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
    #$anim_studio_expensive_price = 
    #$$anim_studio_cheap_price = 
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
    $trailer_choice = "Reuse"
    #Trailer choices include "Reuse" or "New"
    $wk_9_forgot_home = True
    $website_choice = "Professional"
    #available website choices = "Professional","Shunsuke","Free"

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
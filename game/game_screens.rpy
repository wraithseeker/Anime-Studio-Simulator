screen task():
    tag menu
    use side_nav

    default task_tt_description = Tooltip("Sends Yukari to do marketing tasks") 
    default task_tt_stats = Tooltip("{color=#27ae60}+1 Marketing{/color}\n{color=#c0392b}-1 Happiness{/color}")
    window:
        style "task_window"

    frame:
        background None
        xysize(545,230)
        xalign 0.53
        yalign 0.22 
        vbox:
            spacing 30
            text task_tt_description.value style "task_tooltip" text_align 0.0
            text task_tt_stats.value style "task_stats_tooltip" text_align 0.0
    hbox:
        xalign 0.097
        yalign 0.232
        add "char_image/yukari.png" 
        text "Yukari" style "char_title_text"
        #SetDict is used to modify arrays, SetField is to modify the field of an object's value
        vbox:
            ypos 65
            xpos -130
            spacing 10
            for i in range(0,len(yukari_tasks)):
                if yukari_tasks[i].selected:
                    textbutton yukari_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action [SetField(yukari_tasks[i],"selected",False),
                                renpy.curry(yukari_tasks[i].removeStats)(anime),
                                SetVariable("yukari_task_selected",False)]
                else:
                    textbutton yukari_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action(yukari_tasks[i].getStats())
                                ,task_tt_description.Action(yukari_tasks[i].description)] 
                        action If ((yukari_task_selected == False),
                                [SetField(yukari_tasks[i],"selected",True),
                                renpy.curry(yukari_tasks[i].addStats)(anime),
                                SetVariable("yukari_task_selected",True)])  

    hbox:
        xalign 0.097
        yalign 0.55
        add "char_image/yuuko.png" 
        text "Yuuko" style "char_title_text"
        vbox:
            ypos 65
            xpos -130
            spacing 10
            for i in range(0,len(yuuko_tasks)):
                if yuuko_tasks[i].selected:
                    textbutton yuuko_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action [SetField(yuuko_tasks[i],"selected",False),
                                renpy.curry(yuuko_tasks[i].removeStats)(anime),
                                SetVariable("yuuko_task_selected",False)]
                else:
                    textbutton yuuko_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action(yuuko_tasks[i].getStats())
                                ,task_tt_description.Action(yuuko_tasks[i].description)] 
                        action If ((yuuko_task_selected == False),
                                [SetField(yuuko_tasks[i],"selected",True),
                                renpy.curry(yuuko_tasks[i].addStats)(anime),
                                SetVariable("yuuko_task_selected",True)])  

    hbox:
        xalign 0.097
        yalign 0.862
        add "char_image/mayumi.png" 
        text "Mayumi" style "char_title_text"
        vbox:
            ypos 65
            xpos -146
            spacing 10
            for i in range(0,len(mayumi_tasks)):
                if mayumi_tasks[i].selected:
                    textbutton mayumi_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action [SetField(mayumi_tasks[i],"selected",False),
                                renpy.curry(mayumi_tasks[i].removeStats)(anime),
                                SetVariable("mayumi_task_selected",False)]
                else:
                    textbutton mayumi_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action(mayumi_tasks[i].getStats())
                                ,task_tt_description.Action(mayumi_tasks[i].description)] 
                        action If ((mayumi_task_selected == False),
                                [SetField(mayumi_tasks[i],"selected",True),
                                renpy.curry(mayumi_tasks[i].addStats)(anime),
                                SetVariable("mayumi_task_selected",True)]) 

    hbox:
        xalign 0.576
        yalign 0.858
        add "char_image/shunsuke.png" 
        text "Shunsuke" style "char_title_text"
        vbox:
            ypos 65
            xpos -205
            spacing 10
            for i in range(0,len(shunsuke_tasks)):
                if shunsuke_tasks[i].selected:
                    textbutton shunsuke_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action [SetField(shunsuke_tasks[i],"selected",False),
                                renpy.curry(shunsuke_tasks[i].removeStats)(anime),
                                SetVariable("shunsuke_task_selected",False)]
                else:
                    textbutton shunsuke_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action(shunsuke_tasks[i].getStats())
                                ,task_tt_description.Action(shunsuke_tasks[i].description)] 
                        action If ((shunsuke_task_selected == False),
                                [SetField(shunsuke_tasks[i],"selected",True),
                                renpy.curry(shunsuke_tasks[i].addStats)(anime),
                                SetVariable("shunsuke_task_selected",True)]) 
    hbox:
        xalign 0.565
        yalign 0.55
        add "char_image/sumiko.png" ypos -5
        text "Sumiko" style "char_title_text"
        vbox:
            ypos 65
            xpos -145
            spacing 10
            for i in range(0,len(sumiko_tasks)):
                if sumiko_tasks[i].selected:
                    textbutton sumiko_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action [SetField(sumiko_tasks[i],"selected",False),
                                renpy.curry(sumiko_tasks[i].removeStats)(anime),
                                SetVariable("sumiko_task_selected",False)]
                else:
                    textbutton sumiko_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action(sumiko_tasks[i].getStats())
                                ,task_tt_description.Action(sumiko_tasks[i].description)] 
                        action If ((sumiko_task_selected == False),
                                [SetField(sumiko_tasks[i],"selected",True),
                                renpy.curry(sumiko_tasks[i].addStats)(anime),
                                SetVariable("sumiko_task_selected",True)]) 


transform grow_success_text:
    zoom 0 alpha 1
    on show:
        linear 0.2 zoom 1
        linear 1.8 alpha 0
    on hide:
        zoom 0 alpha 1

screen upgrade():
    tag menu
    use side_nav
    default upgrade_tt = Tooltip(upgrade_tooltip_default)
    
    window:
        style "upgrade_window"

    hbox:
        xalign 0.24
        yalign 0.25
        spacing 50
        if yukari_upgrade_selected:
            imagebutton:
                idle "char_image/upgrade/yukari_upgrade_selected.png"
                action SetVariable("yukari_upgrade_selected",False)
        else:
            imagebutton:
                idle "char_image/upgrade/yukari_upgrade_idle.png"
                action SetVariable("yukari_upgrade_selected",True)
                hovered upgrade_tt.Action("Send Yukari to meet veterans in the anime industry to broaden her knowledge of the industry.")

        if yuuko_upgrade_selected:
            imagebutton:
                idle "char_image/upgrade/yuuko_upgrade_selected.png"
                action SetVariable("yuuko_upgrade_selected",False)
        else:
            imagebutton:
                idle "char_image/upgrade/yuuko_upgrade_idle.png"
                action SetVariable("yuuko_upgrade_selected",True)
                hovered upgrade_tt.Action("Pair Yuuko up with professional artists in the anime industry.")

        if sumiko_upgrade_selected:
            imagebutton:
                idle "char_image/upgrade/sumiko_upgrade_selected.png"
                action SetVariable("sumiko_upgrade_selected",False)
        else:
            imagebutton:
                idle "char_image/upgrade/sumiko_upgrade_idle.png"
                action SetVariable("sumiko_upgrade_selected",True)
                hovered upgrade_tt.Action("Give Sumiko some time to meditate and trek in the nearby mountains.")

        if mayumi_upgrade_selected:
            imagebutton:
                idle "char_image/upgrade/mayumi_upgrade_selected.png"
                action SetVariable("mayumi_upgrade_selected",False)
        else:
            imagebutton:
                idle "char_image/upgrade/mayumi_upgrade_idle.png"
                action SetVariable("mayumi_upgrade_selected",True)
                hovered upgrade_tt.Action("Send Mayumi to musical bootcamps to hone her skills.")

        if shunsuke_upgrade_selected:
            imagebutton:
                idle "char_image/upgrade/shunsuke_upgrade_selected.png"
                action SetVariable("shunsuke_upgrade_selected",False)
        else:
            imagebutton:
                idle "char_image/upgrade/shunsuke_upgrade_idle.png"
                action SetVariable("shunsuke_upgrade_selected",True)
                hovered upgrade_tt.Action("Invite a veteran writer to review Shunsuke's writing.")

        add "ui/big_moneybag.png" xpos -650 ypos 649
        text str(upgrade_proficiency_cost) color "#000" size 65 xpos -680 ypos 678

    imagebutton:
        auto "ui/upgrade_screen/done_%s.png" 
        style "upgrade_button" 
        action [renpy.curry(UpgradeCharacters)(yukari_stats,mayumi_stats,shunsuke_stats,sumiko_stats,yuuko_stats)
                ]

    frame:
        background None
        xalign 0.18 yalign 0.6 
        xysize(1150,250)
        text upgrade_tt.value color "#000" size 40 text_align 0.0

    showif upgrade_tooltip != "":
        text upgrade_tooltip color upgrade_tooltip_color size 40 xalign 0.37 yalign 0.75 at grow_success_text

screen anime_status():
    tag menu
    use side_nav
    window:
        style "anime_status_window"

    #star_full.png, star_half.png,star_empty.png
    #story
    vbox:
        xalign 0.35 
        yalign 0.30
        spacing 10
        for i in range(0,3):
            hbox:
                spacing 5
                # quotient grabs the integer value, e.g plot = 4.5, grabs int 4
                # remainder grabs the remainder value, e.g plot = 4.5, grabs 0.5 and converts it to int
                # empty stars is how many empty star images we have to display
                python:
                    plot_value = getattr(anime,anime_stats[i])
                    remainder = int(plot_value % 1 / 0.5)
                    quotient = int(plot_value // 1)
                    empty_stars = 5 - quotient - remainder


                for p in range(0,quotient):
                    add "ui/anime_status/star_full.png"
                for h in range(0,remainder):
                    add "ui/anime_status/star_half.png"
                for e in range(0,empty_stars):
                    add "ui/anime_status/star_empty.png"
        #hbox:
            #add "ui/anime_status/diamond_full.png" ypos -125 xpos 340
        

    bar value StaticValue(anime_story_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/blue_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        xalign 0.2 yalign 0.205

    #art
    vbox:
        xalign 0.35 
        yalign 0.575
        spacing 10
        for i in range(3,6):
            hbox:
                spacing 5
                python:
                    plot_value = getattr(anime,anime_stats[i])
                    remainder = int(plot_value % 1 / 0.5)
                    quotient = int(plot_value // 1)
                    empty_stars = 5 - quotient - remainder


                for p in range(0,quotient):
                    add "ui/anime_status/star_full.png"
                for h in range(0,remainder):
                    add "ui/anime_status/star_half.png"
                for e in range(0,empty_stars):
                    add "ui/anime_status/star_empty.png"

    bar value StaticValue(anime_art_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/orange_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        xalign 0.2 yalign 0.459

    #music
    vbox:
        xalign 0.35 
        yalign 0.87
        spacing 10
        for i in range(6,9):
            hbox:
                spacing 5
                python:
                    plot_value = getattr(anime,anime_stats[i])
                    remainder = int(plot_value % 1 / 0.5)
                    quotient = int(plot_value // 1)
                    empty_stars = 5 - quotient - remainder


                for p in range(0,quotient):
                    add "ui/anime_status/star_full.png"
                for h in range(0,remainder):
                    add "ui/anime_status/star_half.png"
                for e in range(0,empty_stars):
                    add "ui/anime_status/star_empty.png"
    bar value StaticValue(anime_music_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/brown_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        xalign 0.2 yalign 0.715



screen member_status():
    tag menu
    use side_nav
    window:
        style "member_status_window"


    add "char_image/yukari.png" xalign 0.260 yalign 0.232
    text "Yukari" xalign 0.35 yalign 0.195 color "#000" size 40
    add "char_image/yuuko.png" xalign 0.075 yalign 0.546
    text "Yuuko" xalign 0.168 yalign 0.455 color "#000" size 40
    add "char_image/sumiko.png" xalign 0.413 yalign 0.545
    text "Sumiko" xalign 0.507 yalign 0.445 color "#000" size 40
    add "char_image/shunsuke.png" xalign 0.415 yalign 0.86
    text "Shunsuke" xalign 0.529 yalign 0.715 color "#000" size 40
    add "char_image/mayumi.png" xalign 0.075 yalign 0.863
    text "Mayumi" xalign 0.172 yalign 0.715 color "#000" size 40
    #yukari

    vbox:

        xalign 0.468 yalign 0.278
        spacing 13
        bar value StaticValue(yukari_stats.happiness,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(yukari_stats.stress,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(yukari_stats.proficiency,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(yukari_stats.human_relations,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_purple_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None

        #yuuko
    vbox:
        xalign 0.287 yalign 0.540
        spacing 13
        bar value StaticValue(yuuko_stats.happiness,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(yuuko_stats.stress,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(yuuko_stats.proficiency,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
    #sumiko
    vbox:
        xalign 0.623 yalign 0.540
        spacing 13
        bar value StaticValue(sumiko_stats.happiness,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(sumiko_stats.stress,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(sumiko_stats.proficiency,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None

    #mayumi
    vbox:
        xalign 0.287 yalign 0.815
        spacing 13
        bar value StaticValue(mayumi_stats.happiness,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(mayumi_stats.stress,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(mayumi_stats.proficiency,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
    #shunsuke
    vbox:
        xalign 0.623 yalign 0.815
        spacing 13
        bar value StaticValue(shunsuke_stats.happiness,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(shunsuke_stats.stress,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(shunsuke_stats.proficiency,10):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None

screen outsource():
    tag menu
    use side_nav
    window:
        style "outsource_window"
    frame:
        background None
        text "Produce 1" color "#000" xalign 0.5 yalign 0.10 size 55
        add "ui/anime_status/star_full.png" xalign 0.605 yalign 0.10
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.25
            imagebutton auto "ui/outsource/plot_%s.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/character_dev.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/storyboard.png" style "outsource_buttons"
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.40
            imagebutton idle "ui/outsource/character_design.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/animation.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/background.png" style "outsource_buttons"
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.55
            imagebutton idle "ui/outsource/op_ed.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/ost.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/voice_acting.png" style "outsource_buttons"
        hbox:
            spacing 25
            xalign 0.30
            yalign 0.70
            imagebutton idle "ui/outsource/quality_check.png" style "outsource_buttons"
            imagebutton idle "ui/outsource/marketing.png" style "outsource_buttons"
        hbox:
            xalign 0.35
            yalign 0.88
            add "ui/big_moneybag.png" xpos 92 ypos 24
            text "5" color "#000" size 65 xpos 112 ypos 52
            imagebutton auto "ui/outsource/done_%s.png" style "outsource_buttons_outsource" action Return()


screen side_nav():
    if yukari_task_selected and yuuko_task_selected and sumiko_task_selected and shunsuke_task_selected and mayumi_task_selected:
        $task_ready = True
    else:
        $task_ready = False
    frame:
        style "side_nav"
        #text anime.name style "anime_name"
        vbox:
            textbutton ("Week [current_week]") action NullAction()  text_style "sidenav_week" style "sidenav_week_button"
            textbutton ("Monday")  action NullAction()  text_style "sidenav_day" style "sidenav_day_button"
            #add "ui/money_bag.png" ypos 85 xpos 55
            text str(anime.funds) style "sidenav_money_text"
            vbox: 
                spacing 5
                ypos 20
                textbutton ("Anime Status")  action If(side_nav_interaction,ShowMenu("anime_status"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Member Status")  action If(side_nav_interaction,ShowMenu("member_status"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Tasks")  action If(side_nav_interaction,ShowMenu("task"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Outsource")  action If(side_nav_interaction,ShowMenu("outsource"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Upgrades")  action If(side_nav_interaction,ShowMenu("upgrade"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Options")  action If (side_nav_interaction,ShowMenu("preferences")) text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Monday")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
               
        vbox:
            if task_ready:
                imagebutton auto "ui/done_%s.png" style "sidenav_done" action [Return(),SetVariable("task_ready",True)]

screen start_game:
    use side_nav
    text str(task_ready)
    if task_ready:
        timer 0.2 action [Return(),SetVariable("task_ready",False)]

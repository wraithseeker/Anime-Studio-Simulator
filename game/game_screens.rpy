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
        vbox:
            ypos 65
            xpos -130
            spacing 10
            #     text yukari_tasks[i].title
            #     text yukari_tasks[i].description
            #     text str(yukari_tasks[i].selected)
            for i in range(0,len(yukari_tasks)):
                text str(yukari_tasks[i].selected)
                if yukari_tasks[i].selected:
                    textbutton yukari_tasks[i].title:
                        text_style "task_text_selected" 
                        style "task_button" 
                        action SetField(yukari_tasks[i],"selected",False)
                        #SetDict is used to modify arrays, SetField is to modify the field of an object's value
                else:
                    textbutton yukari_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_stats.Action("{color=#27ae60} +2 Proficiency{/color}\n{color=#c0392b} -1 Stress\n -1 Happiness{/color}")
                                ,task_tt_description.Action(yukari_tasks[i].description)]                                      
                        action SetField(yukari_tasks[i],"selected",True)


    hbox:
        xalign 0.097
        yalign 0.55
        add "char_image/yuuko.png" 
        text "Yuuko" style "char_title_text"
        vbox:
            ypos 65
            xpos -130
            spacing 10
            textbutton "Marketing":
                text_style "task_text" 
                style "task_button" 
                action NullAction()
            textbutton "Quality Check":
                text_style "task_text" 
                style "task_button" 
                action NullAction()
            textbutton "Team Bonding":
                text_style "task_text" 
                style "task_button" 
                action NullAction()

    hbox:
        xalign 0.097
        yalign 0.862
        add "char_image/mayumi.png" 
        text "Mayumi" style "char_title_text"
        vbox:
            ypos 65
            xpos -146
            spacing 10
            textbutton "Marketing" text_style "task_text" style "task_button"
            textbutton "Quality Check" text_style "task_text" style "task_button"
            textbutton "Team Bonding" text_style "task_text" style "task_button"

    hbox:
        xalign 0.561
        yalign 0.858
        add "char_image/shunsuke.png" 
        text "Shunsuke" style "char_title_text"
        vbox:
            ypos 65
            xpos -205
            spacing 10
            textbutton "Marketing" text_style "task_text" style "task_button"
            textbutton "Quality Check" text_style "task_text" style "task_button"
            textbutton "Team Bonding" text_style "task_text" style "task_button"
    hbox:
        xalign 0.533
        yalign 0.542
        add "char_image/sumiko.png" 
        text "Sumiko" style "char_title_text"
        vbox:
            ypos 65
            xpos -145
            spacing 10
            textbutton "Marketing" text_style "task_text" style "task_button"
            textbutton "Quality Check" text_style "task_text" style "task_button"
            textbutton "Team Bonding" text_style "task_text" style "task_button"



screen upgrade():
    tag menu
    use side_nav
    default upgrade_tt = Tooltip("Send your team for training!")
 
    window:
        style "upgrade_window"

    hbox:
        xalign 0.18
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
        text "5" color "#000" size 65 xpos -680 ypos 678
    imagebutton idle "ui/upgrade_button.png" style "upgrade_button"

    $number = 0
    if yukari_upgrade_selected:
        $number += 1
    if yuuko_upgrade_selected:
        $number += 1
    if sumiko_upgrade_selected:
        $number += 1
    if shunsuke_upgrade_selected:
        $number += 1
    if mayumi_upgrade_selected:
        $number += 1

    text str(number) xalign 0.2 yalign 0.9 color "#000"
    frame:
        background None
        xalign 0.18 yalign 0.6 
        xysize(1150,250)
        text upgrade_tt.value color "#000" size 40 text_align 0.0


screen anime_status():
    tag menu
    use side_nav
    window:
        style "anime_status_window"

    #star_full.png, star_half.png,star_empty.png
    #story
    vbox:
        xalign 0.35 
        yalign 0.28
        spacing 10
        for i in range(0,3):
            hbox:
                spacing 5
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
        hbox:
            add "ui/anime_status/diamond_full.png" ypos -125 xpos 340
        

    bar value StaticValue(60,100):
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
        for i in range(0,3):
            hbox:
                spacing 5
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"

    bar value StaticValue(100,100):
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
        for i in range(0,3):
            hbox:
                spacing 5
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
                add "ui/anime_status/star_full.png"
    bar value StaticValue(60,100):
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
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_blue_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
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
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
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
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
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
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
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
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_red_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
            xmaximum 168
            ymaximum 21
            left_bar Frame("ui/member_status/member_orange_bar_full.png")
            right_bar Frame("ui/member_status/member_bar_empty.png")
            thumb_shadow None
            thumb None
        bar value StaticValue(100,100):
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
            imagebutton idle "ui/outsource/plot.png" style "outsource_buttons"
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
            imagebutton idle "ui/outsource_button.png" style "outsource_buttons_outsource"


screen side_nav():
    frame:
        style "side_nav"
        vbox:
            textbutton ("Week 1") action NullAction()  text_style "sidenav_week" style "sidenav_week_button"
            textbutton ("Monday")  action NullAction()  text_style "sidenav_day" style "sidenav_day_button"
            #add "ui/money_bag.png" ypos 85 xpos 55
            text "25" style "sidenav_money_text"
            #add "ui/hline.png" ypos 55 xpos 45
            vbox: 
                spacing 5
                ypos 20
                textbutton ("Anime Status")  action ShowMenu("anime_status")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Member Status")  action ShowMenu("member_status")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Tasks")  action ShowMenu("task")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Outsource")  action ShowMenu("outsource")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Upgrades")  action ShowMenu("upgrade")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Options")  action ShowMenu("preferences") text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Monday")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
        vbox:
            imagebutton auto "ui/done_%s.png" style "sidenav_done" action Return()

screen start_game:
    use side_nav
    text "lol"

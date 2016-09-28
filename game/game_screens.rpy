screen task():
    tag menu
    use side_nav
    default task_tt_description = Tooltip("Select some tasks for your team members to do.") 
    default task_tt_positive_stats = Tooltip("")
    default task_tt_negative_stats = Tooltip("")
    window:
        style "task_window"

    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return()
    frame:
        background None
        xysize(545,230)
        xalign 0.53
        yalign 0.22 
        vbox:
            spacing 5
            text task_tt_description.value style "task_tooltip" text_align 0.0
            hbox:
                spacing 20
                frame:
                    background None
                    xysize(260,120)
                    text task_tt_positive_stats.value style "task_stats_tooltip" text_align 0.0
                frame:
                    background None
                    xysize(260,120)
                    text task_tt_negative_stats.value style "task_stats_tooltip"    text_align 0.0
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
                                SetVariable("yukari_task_selected",False)]
                else:
                    textbutton yukari_tasks[i].title:
                        text_style "task_text"
                        style "task_button"
                        hovered [task_tt_positive_stats.Action(yukari_tasks[i].positive_stats)
                                ,task_tt_negative_stats.Action(yukari_tasks[i].negative_stats)
                                ,task_tt_description.Action(yukari_tasks[i].description)] 
                        action If ((yukari_tasks[i].selected == False),
                                [renpy.curry(ResetCharacterTask)(yukari_tasks),SetField(yukari_tasks[i],"selected",True),
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
                                SetVariable("yuuko_task_selected",False)]
                else:
                    textbutton yuuko_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_positive_stats.Action(yuuko_tasks[i].positive_stats)
                                ,task_tt_negative_stats.Action(yuuko_tasks[i].negative_stats)
                                ,task_tt_description.Action(yuuko_tasks[i].description)] 
                        action If ((yuuko_tasks[i].selected == False),
                                [renpy.curry(ResetCharacterTask)(yuuko_tasks),SetField(yuuko_tasks[i],"selected",True),
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
                                SetVariable("mayumi_task_selected",False)]
                else:
                    textbutton mayumi_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_positive_stats.Action(mayumi_tasks[i].positive_stats)
                                ,task_tt_negative_stats.Action(mayumi_tasks[i].negative_stats)
                                ,task_tt_description.Action(mayumi_tasks[i].description)]  
                        action If ((mayumi_tasks[i].selected == False),
                                [renpy.curry(ResetCharacterTask)(mayumi_tasks),SetField(mayumi_tasks[i],"selected",True),
                                SetVariable("mayumi_task_selected",True)]) 

    hbox:
        xalign 0.526
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
                                SetVariable("shunsuke_task_selected",False)]
                else:
                    textbutton shunsuke_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_positive_stats.Action(shunsuke_tasks[i].positive_stats)
                                ,task_tt_negative_stats.Action(shunsuke_tasks[i].negative_stats)
                                ,task_tt_description.Action(shunsuke_tasks[i].description)]  
                        action If ((shunsuke_tasks[i].selected == False),
                                [renpy.curry(ResetCharacterTask)(shunsuke_tasks),SetField(shunsuke_tasks[i],"selected",True),
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
                                SetVariable("sumiko_task_selected",False)]
                else:
                    textbutton sumiko_tasks[i].title:
                        text_style "task_text" 
                        style "task_button" 
                        hovered [task_tt_positive_stats.Action(sumiko_tasks[i].positive_stats)
                                ,task_tt_negative_stats.Action(sumiko_tasks[i].negative_stats)
                                ,task_tt_description.Action(sumiko_tasks[i].description)]  
                        action If ((sumiko_tasks[i].selected == False),
                                [renpy.curry(ResetCharacterTask)(sumiko_tasks),SetField(sumiko_tasks[i],"selected",True),
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
    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return()
    hbox:
        xalign 0.19
        yalign 0.25
        spacing 50
        if yukari_upgrade == Outsource.SELECTED:
            imagebutton:
                idle "char_image/upgrade/yukari_upgrade_selected.png"
                action [SetVariable("yukari_upgrade",Outsource.NOT_SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count - 1)]
        elif yukari_upgrade == Outsource.NOT_SELECTED:
            imagebutton:
                idle "char_image/upgrade/yukari_upgrade_idle.png"
                action [SetVariable("yukari_upgrade",Outsource.SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count + 1)]
                hovered upgrade_tt.Action("Send Yukari to meet veterans in the anime industry to broaden her knowledge of the industry.")
        else:
            imagebutton:
                idle "char_image/upgrade/yukari_upgrade_transparent.png"

        if yuuko_upgrade == Outsource.SELECTED:
            imagebutton:
                idle "char_image/upgrade/yuuko_upgrade_selected.png"
                action [SetVariable("yuuko_upgrade",Outsource.NOT_SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count - 1)]
        elif yuuko_upgrade == Outsource.NOT_SELECTED:
            imagebutton:
                idle "char_image/upgrade/yuuko_upgrade_idle.png"
                action [SetVariable("yuuko_upgrade",Outsource.SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count + 1)]
                hovered upgrade_tt.Action("Pair Yuuko up with professional artists in the anime industry.")
        else:
            imagebutton:
                idle "char_image/upgrade/yuuko_upgrade_transparent.png"

        if sumiko_upgrade == Outsource.SELECTED:
            imagebutton:
                idle "char_image/upgrade/sumiko_upgrade_selected.png"
                action [SetVariable("sumiko_upgrade",Outsource.NOT_SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count - 1)]
        elif sumiko_upgrade == Outsource.NOT_SELECTED:
            imagebutton:
                idle "char_image/upgrade/sumiko_upgrade_idle.png"
                action [SetVariable("sumiko_upgrade",Outsource.SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count + 1)]
                hovered upgrade_tt.Action("Give Sumiko some time to meditate and trek in the nearby mountains.")
        else:
            imagebutton:
                idle "char_image/upgrade/sumiko_upgrade_transparent.png"

        if mayumi_upgrade == Outsource.SELECTED:
            imagebutton:
                idle "char_image/upgrade/mayumi_upgrade_selected.png"
                action [SetVariable("mayumi_upgrade",Outsource.NOT_SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count - 1)]
        elif mayumi_upgrade == Outsource.NOT_SELECTED:
            imagebutton:
                idle "char_image/upgrade/mayumi_upgrade_idle.png"
                action [SetVariable("mayumi_upgrade",Outsource.SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count + 1)]
                hovered upgrade_tt.Action("Send Mayumi to musical bootcamps to hone her skills.")
        else:
            imagebutton:
                idle "char_image/upgrade/mayumi_upgrade_transparent.png"

        if shunsuke_upgrade == Outsource.SELECTED:
            imagebutton:
                idle "char_image/upgrade/shunsuke_upgrade_selected.png"
                action [SetVariable("shunsuke_upgrade",Outsource.NOT_SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count - 1)]
        elif shunsuke_upgrade == Outsource.NOT_SELECTED:
            imagebutton:
                idle "char_image/upgrade/shunsuke_upgrade_idle.png"
                action [SetVariable("shunsuke_upgrade",Outsource.SELECTED),SetVariable("upgrade_selection_count",upgrade_selection_count + 1)]
                hovered upgrade_tt.Action("Invite a veteran writer to review Shunsuke's writing.")
        else:
            imagebutton:
                idle "char_image/upgrade/shunsuke_upgrade_transparent.png"

    add "ui/big_moneybag.png" xalign 0.35 yalign 0.86
    text str(upgrade_proficiency_cost * upgrade_selection_count ) color "#000" size 65 xalign 0.405 yalign 0.86

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
    window:
        style "anime_status_window"

    #star_full.png, star_half.png,star_empty.png
    #story
    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return() 
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
        

    bar value StaticValue(anime.story_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/blue_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        thumb_offset 0
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

    bar value StaticValue(anime.art_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/orange_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        thumb_offset 0
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
    bar value StaticValue(anime.music_progress,100):
        ymaximum 23
        xmaximum 407
        left_bar Frame("ui/anime_status/brown_bar_full.png")
        right_bar Frame("ui/anime_status/status_bar_empty.png")
        thumb_shadow None
        thumb None
        thumb_offset 0
        xalign 0.2 yalign 0.715



screen member_status():
    tag menu
    window:
        style "member_status_window"

    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return()

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
        bar value StaticValue(yukari_stats.management,10):
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

    default outsource_tt = Tooltip("")
    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return() 
    text str(outsource.selection_count) size 30
    frame:
        background None
        text "Produce 1" color "#000" xalign 0.5 yalign 0.10 size 55
        add "ui/anime_status/star_full.png" xalign 0.605 yalign 0.10
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.25
            if outsource.plot == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/plot_hover.png"
                    action [SetField(outsource,"plot",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.plot == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/plot_idle.png"
                    action [SetField(outsource,"plot",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                #disabled
                imagebutton:
                    idle "ui/outsource/plot_transparent.png"
                    style "outsource_buttons" 

            if outsource.character_development == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/character_dev_hover.png"
                    action [SetField(outsource,"character_development",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.character_development == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/character_dev_idle.png"
                    action [SetField(outsource,"character_development",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                #disabled
                imagebutton:
                    idle "ui/outsource/character_dev_transparent.png"
                    style "outsource_buttons"  
            if outsource.storyboard == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/storyboard_hover.png"
                    action [SetField(outsource,"storyboard",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.storyboard == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/storyboard_idle.png"
                    action [SetField(outsource,"storyboard",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/storyboard_transparent.png"
                    style "outsource_buttons"  
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.40
            if outsource.character_design == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/character_design_hover.png"
                    action [SetField(outsource,"character_design",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.character_design == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/character_design_idle.png"
                    action [SetField(outsource,"character_design",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/character_design_transparent.png"
                    style "outsource_buttons" 
            if outsource.animation == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/animation_hover.png"
                    action [SetField(outsource,"animation",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.animation == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/animation_idle.png"
                    action [SetField(outsource,"animation",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/animation_transparent.png"
                    style "outsource_buttons" 
            if outsource.background == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/background_hover.png"
                    action [SetField(outsource,"background",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.background == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/background_idle.png"
                    action [SetField(outsource,"background",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/background_transparent.png"
                    style "outsource_buttons"  
        hbox:
            spacing 25
            xalign 0.25
            yalign 0.55
            if outsource.op_ed == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/op_ed_hover.png"
                    action [SetField(outsource,"op_ed",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.op_ed == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/op_ed_idle.png"
                    action [SetField(outsource,"op_ed",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/op_ed_transparent.png"
                    style "outsource_buttons" 
            if outsource.ost == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/ost_hover.png"
                    action [SetField(outsource,"ost",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.ost == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/ost_idle.png"
                    action [SetField(outsource,"ost",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/ost_transparent.png"
                    style "outsource_buttons" 
            if outsource.voice_acting == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/voice_acting_hover.png"
                    action [SetField(outsource,"voice_acting",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.voice_acting == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/voice_acting_idle.png"
                    action [SetField(outsource,"voice_acting",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/voice_acting_transparent.png"
                    style "outsource_buttons"  
        hbox:
            spacing 25
            xalign 0.30
            yalign 0.70
            if outsource.marketing == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/marketing_hover.png"
                    action [SetField(outsource,"marketing",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.marketing == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/marketing_idle.png"
                    action [SetField(outsource,"marketing",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/marketing_transparent.png"
                    style "outsource_buttons" 
            if outsource.quality_check == Outsource.SELECTED:
                imagebutton:
                    idle "ui/outsource/quality_check_hover.png"
                    action [SetField(outsource,"quality_check",Outsource.NOT_SELECTED),SetField(outsource,"selection_count",outsource.selection_count - 1)]
                    style "outsource_buttons" 
            elif outsource.quality_check == Outsource.NOT_SELECTED:
                imagebutton:
                    idle "ui/outsource/quality_check_idle.png"
                    action [SetField(outsource,"quality_check",Outsource.SELECTED),SetField(outsource,"selection_count",outsource.selection_count + 1)]
                    style "outsource_buttons"
            else:
                imagebutton:
                    idle "ui/outsource/quality_check_transparent.png"
                    style "outsource_buttons"  
  
    add "ui/big_moneybag.png" xalign 0.35 yalign 0.86
    text str(outsource.selection_count * outsource.cost) color "#000" size 65 xalign 0.405 yalign 0.86
    imagebutton:
        auto "ui/outsource/done_%s.png" 
        style "upgrade_button" 
        action [renpy.curry(OutsourceAnime)()]
    showif outsource_tooltip != "":
        text outsource_tooltip color upgrade_tooltip_color size 40 xalign 0.37 yalign 0.78 at grow_success_text


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
                textbutton ("Anime Status")  action If(side_nav_interaction,ShowMenu("anime_status_sidenav"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Member Status")  action If(side_nav_interaction,ShowMenu("member_status_sidenav"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Tasks")  action If(side_nav_interaction,ShowMenu("task"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Outsource")  action If(side_nav_interaction,ShowMenu("outsource"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Upgrades")  action If(side_nav_interaction,ShowMenu("upgrade"))  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Progress")  action If (side_nav_interaction,ShowMenu("progress_report_sidenav")) text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Monday")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
               
        vbox:
            if task_ready:
                imagebutton auto "ui/done_%s.png" style "sidenav_done" action [Return(),SetVariable("task_ready",True)]

screen start_game:
    #use side_nav
    if not initial_week and not task_ready:
        use progress_report
    use side_nav
    if task_ready:
        timer 0.03 action [Return(),SetVariable("task_ready",False),renpy.curry(EndTurn)()]
    # else:
    #     use progress_report

screen anime_status_sidenav:
    tag menu
    use anime_status
    use side_nav

screen member_status_sidenav:
    tag menu
    use member_status
    use side_nav

screen progress_report_sidenav:
    tag menu
    use progress_report
    use side_nav
    imagebutton auto "ui/load/close_button_%s.png" xalign 0.665 yalign 0.10 action Return()

screen progress_report:
    tag menu
    default task_tt_description = Tooltip("Select some tasks for your team members to do.") 
    default task_tt_stats = Tooltip("")
    window:
        background "ui/progress_report.png"
    text "Week " + str(current_week) + " Progress Report" style "progress_title"
    frame:
        background None
        xysize(545,230)
        xalign 0.53
        yalign 0.232

        if anime.checkCategory("story") == Anime.CATEGORY_POSITIVE:
            text GREEN_COLOR + POSITIVE_SIGN color "#000" yalign 0.25 xalign 0.02 size 25
            text "Story" color "#1E824C" yalign 0.325 xalign 0.09 size 25
        elif anime.checkCategory("story") == Anime.CATEGORY_NEGATIVE:
            text RED_COLOR + MINUS_SIGN color "#000" yalign 0.25 xalign 0.02 size 25
            text "Story" color "#C0392B" yalign 0.325 xalign 0.09 size 25
        else:
            text "Story" color "#000" yalign 0.325 xalign 0.09 size 25

        if anime.checkCategory("art") == Anime.CATEGORY_POSITIVE:
            text GREEN_COLOR + POSITIVE_SIGN color "#000" yalign 0.460 xalign 0.02 size 25
            text "Art" color "#1E824C" yalign 0.5 xalign 0.085 size 25
        elif anime.checkCategory("art") == Anime.CATEGORY_NEGATIVE:
            text RED_COLOR + MINUS_SIGN color "#000" yalign 0.460 xalign 0.02 size 25
            text "Art" color "#C0392B" yalign 0.5 xalign 0.085 size 25
        else:
            text "Art" color "#000" yalign 0.5 xalign 0.085 size 25

        if anime.checkCategory("music") == Anime.CATEGORY_POSITIVE:
            text GREEN_COLOR + POSITIVE_SIGN color "#000" yalign 0.67 xalign 0.02 size 25
            text "Music" color "#1E824C" yalign 0.675 xalign 0.09 size 25
        elif anime.checkCategory("music") == Anime.CATEGORY_NEGATIVE:
            text RED_COLOR + MINUS_SIGN color "#000" yalign 0.67 xalign 0.02 size 25
            text "Music" color "#C0392B" yalign 0.675 xalign 0.09 size 25
        else:
            text "Music" color "#000" yalign 0.675 xalign 0.09 size 25

        textbutton "More Details" xalign 0.5 yalign 0.95 background None text_style "progress_details" action ShowMenu("anime_report")
        vbox:
            text "Anime Progress" style "char_title_text"
            ypos -7
            xpos 15
            vbox:
                spacing 12
                ypos 27
                xpos 145
                bar value StaticValue(anime.story_progress,100):
                    ymaximum 23
                    xmaximum 300
                    left_bar Frame("ui/anime_status/blue_bar_full.png")
                    right_bar Frame("ui/anime_status/status_bar_empty.png")
                    thumb_shadow None
                    thumb_offset 0
                    thumb None
                bar value StaticValue(anime.art_progress,100):
                    ymaximum 23
                    xmaximum 300
                    thumb_offset 0
                    left_bar Frame("ui/anime_status/orange_bar_full.png")
                    right_bar Frame("ui/anime_status/status_bar_empty.png")
                    thumb_shadow None
                    thumb None
                bar value StaticValue(anime.music_progress,100):
                    ymaximum 23
                    xmaximum 300
                    thumb_offset 0
                    left_bar Frame("ui/anime_status/brown_bar_full.png")
                    right_bar Frame("ui/anime_status/status_bar_empty.png")
                    thumb_shadow None
                    thumb None

            # text anime.getStatChanges("funds") style "progress_text"
            # text "{color=#c0392b}{font=fonts/Delius-Regular.ttf}{size=+15}-{/size}{/font} Marketing{/color}" style "progress_text"
            # text "{color=#c0392b}{font=fonts/Delius-Regular.ttf}{size=+15}-{/size}{/font} CHARA.DESIGN{/color}" style "progress_text"
    hbox:
        xalign 0.097
        yalign 0.232
        add "char_image/yukari.png" 
        text "Yukari" style "char_title_text"
        #SetDict is used to modify arrays, SetField is to modify the field of an object's value
        frame:
            xpos -130
            ypos 40
            xysize(320,180)
            background None
            vbox:
                spacing -15
                for i in range (0,len(yukari_stats.db_displayed_stats)):
                    text yukari_stats.db_displayed_stats[i] style "progress_text"
                if len(yukari_stats.db_displayed_stats) == 0:
                    text "No change" style "progress_text" ypos 15
                    


    hbox:
        xalign 0.097
        yalign 0.55
        add "char_image/yuuko.png" 
        text "Yuuko" style "char_title_text"
        frame:
            xpos -125
            ypos 40
            xysize(320,180)
            background None
            vbox:
                spacing -15
                for i in range (0,len(yuuko_stats.db_displayed_stats)):
                    text yuuko_stats.db_displayed_stats[i] style "progress_text" 
                if len(yuuko_stats.db_displayed_stats) == 0:
                    text "No change" style "progress_text" ypos 15

    hbox:
        xalign 0.10
        yalign 0.862
        add "char_image/mayumi.png" 
        text "Mayumi" style "char_title_text" xpos 27
        frame:
            xpos -140
            ypos 40
            xysize(320,180)
            background None
            vbox:
                spacing -15
                for i in range (0,len(mayumi_stats.db_displayed_stats)):
                    text mayumi_stats.db_displayed_stats[i] style "progress_text"
                if len(mayumi_stats.db_displayed_stats) == 0:
                    text "No change" style "progress_text" ypos 15

    hbox:
        xalign 0.585
        yalign 0.858
        add "char_image/shunsuke.png" 
        text "Shunsuke" style "char_title_text" xpos 15
        frame:
            ypos 45
            xpos -217
            xysize(320,180)
            background None
            vbox:
                spacing -15
                for i in range (0,len(shunsuke_stats.db_displayed_stats)):
                    text shunsuke_stats.db_displayed_stats[i] style "progress_text"
                if len(shunsuke_stats.db_displayed_stats) == 0:
                    text "No change" style "progress_text" ypos 15
    hbox:
        xalign 0.550
        yalign 0.55
        add "char_image/sumiko.png" ypos -5 
        text "Sumiko" style "char_title_text" xpos 15
        frame:
            ypos 40
            xpos -145
            xysize(320,180)
            background None
            vbox:
                spacing -15
                for i in range (0,len(sumiko_stats.db_displayed_stats)):
                    text sumiko_stats.db_displayed_stats[i] style "progress_text"
                if len(sumiko_stats.db_displayed_stats) == 0:
                    text "No change" style "progress_text" ypos 15

screen anime_report:
    tag menu
    frame:
        xysize(900,600)
        xalign 0.5
        yalign 0.35
        xpadding 25
        ypadding 72
        background Frame("ui/blank_screen_large.png")
        text "Anime Progress Report" size 50 color "#000" xpos 55
    frame:
        xalign 0.57
        yalign 0.35
        xysize (500,170)
        background None
        vbox:
            spacing -10
            for i in range (0,len(anime.db_positive)):
                text anime.db_positive[i] style "progress_anime_text"
            # for i in range (0,2):
            #     text RED_COLOR + MINUS_SIGN + "Marketing" style "progress_text"
    frame:
        xalign 0.57
        yalign 0.575
        background None
        xysize (500,170)
        vbox:
            spacing -10
            for i in range (0,len(anime.db_negative)):
                text anime.db_negative[i] style "progress_anime_text"
            # for i in range (0,5):
            #     text GREEN_COLOR + MINUS_SIGN + "VOICE ACTING" style "progress_text"

    imagebutton auto "ui/load/close_button_%s.png" xalign 0.69 yalign 0.22 action ShowMenu("progress_report_sidenav")


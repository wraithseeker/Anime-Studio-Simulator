﻿screen upgrade():
    tag menu
    use side_nav
    window:
        style "upgrade_window"

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

    #yukari
    add "char_image/yukari.png" xalign 0.27 yalign 0.24
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
            add "ui/money_bag.png"
            text "5" color "#000" size 50 ypos 10 xpos 20


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
                spacing 10
                textbutton ("Anime Status")  action ShowMenu("anime_status")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Member Status")  action ShowMenu("member_status")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                textbutton ("Outsource")  action ShowMenu("outsource")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Tasks")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Outsource")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Upgrades")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
                # textbutton ("Monday")  action ShowMenu("load")  text_style "sidenav_menu_buttons_text" style "sidenav_menu_buttons"
        vbox:
            imagebutton auto "ui/done_%s.png" style "sidenav_done" action Return()
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
transform float_btn_trans:
    on hover:
        linear 0.2 zoom 1.2
    on idle:
        linear 0.2 zoom 1.0   


screen say(who, what, side_image=None, two_window=False):
    # to do
    default tt = Tooltip("") 
    imagebutton auto "ui/float_buttons/anime_%s.png" style "float_anime" action ShowMenu("side_nav") at float_btn_trans hovered tt.Action("Anime Status")
    imagebutton auto "ui/float_buttons/member_%s.png" style "float_member" action MainMenu() at float_btn_trans hovered tt.Action("Member Status")
    # Decide if we want to use the one-window or two-window variant.
    frame:
        background None
        xalign 0.92
        yalign 0.1
        text tt.value style "tooltip_value"
    if not two_window:

        # The one window variant.
        window:
            #id "window"
            style "textbox_window"


            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what" color "#000" font "fonts/LiberationSans-Regular.ttf"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

# screen nvl(dialogue, items=None):

#     window:
#         style "nvl_window"

#         has vbox:
#             style "nvl_vbox"

#         # Display dialogue.
#         for who, what, who_id, what_id, window_id in dialogue:
#             window:
#                 id window_id

#                 has hbox:
#                     spacing 10

#                 if who is not None:
#                     text who id who_id

#                 text what id what_id

#         # Display a menu, if given.
#         if items:

#             vbox:
#                 id "menu"

#                 for caption, action, chosen in items:

#                     if action:

#                         button:
#                             style "nvl_menu_choice_button"
#                             action action

#                             text caption style "nvl_menu_choice"

#                     else:

#                         text caption style "nvl_dialogue"

#     add SideImage() xalign 0.0 yalign 1.0

#     use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

        add "logo.png" xalign 0.5 yalign 0.0
        add "ui/title_screen_notext.png" yalign 0.0 xalign 0.0

    # The main menu buttons.
    frame:
        background None
        xalign .98
        yalign .98
        xpadding 60
        has hbox
        #spacing 20
        style "mainmenu_frame"
        textbutton _("New") action Start() text_style "mainmenu_text" style "mainmenu_button"
        textbutton _("Load") action ShowMenu("load")  text_style "mainmenu_text" style "mainmenu_button"
        textbutton _("Options") action ShowMenu("preferences")  text_style "mainmenu_text" style "mainmenu_button"
        #textbutton _("Dashboard") action ShowMenu("game_dashboard")  text_style "mainmenu_text" style "mainmenu_button"
        #textbutton _("Help") action Help()  text_style "mainmenu_text" style "mainmenu_button"
        textbutton _("Exit") action Quit(confirm=False)  text_style "mainmenu_text" style "mainmenu_button"

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
# style navigation_return:
#     size 40
#     background "nav/return_idle.png"
screen navigation():
    tag menu
    # The background of the game menu.
    # window:
    #     style "gm_root"

    # The various buttons.
    frame:
        xalign .5
        yalign .5
        background None
        has hbox

        spacing 35
        imagebutton auto "ui/nav/return_%s.png" action Return()
        imagebutton auto "ui/nav/save_%s.png" action ShowMenu("save")
        imagebutton auto "ui/nav/load_%s.png" action ShowMenu("load")
        imagebutton auto "ui/nav/settings_%s.png" action ShowMenu("preferences")
        imagebutton auto "ui/nav/quit_%s.png" action MainMenu()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker_load():

    frame:  

        background "ui/load/load_screen.png"
        imagebutton auto "ui/load/close_button_%s.png" action Return() style "save_button_close" 

        # The buttons at the top allow the user to pick a
        # page of files.
        vbox:
            xalign 0.05
            yalign 0.9
            spacing 10
           # background "ui/load/load_screen.png"

            textbutton _("Auto") :
                action FilePage("auto") text_style "save_button_text"
                background None

            textbutton _("Quick"):
                action FilePage("quick") text_style "save_button_text"
                background None
        hbox:
            xalign 0.45
            yalign 0.9
            for i in range(1, 9):
                textbutton str(i) text_style "save_load_pagination":
                    style "save_load_pagination_button"
                    action FilePage(i)

        hbox:
            xalign 0.05
            yalign 0.5
            imagebutton auto "ui/load/back_%s.png" action FilePagePrevious() style "save_button_close" 

        hbox:
            xalign 0.95
            yalign 0.5
            imagebutton auto "ui/load/forward_%s.png" action FilePageNext() style "save_button_close" 


        $ columns = 3
        $ rows = 2

        # Display a grid of file slots.
        grid columns rows:
            xalign 0.5
            yalign 0.5
            spacing 30

            transpose True
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):
                #$ file_name = FileSlotName(i, columns * rows)
                $ save_name = FileSaveName(i)
                $ file_time = FileTime(i, empty=_("empty"))
            
                
                # Each file slot is a button.
                button:
                    
                    #background "ui/save/save_frame_box_empty.png"
                    top_padding 25
                    xpadding 35
                    bottom_padding 15
                    action FileAction(i)
                   # background None
                    has vbox
                    #show "ui/save/save_frame_box_empty.png"
                    # Add the screenshot. empty="ui/save/save_frame_box_empty.png" << empty box
                    add FileScreenshot(i)

                    

                    text "[file_time!t][save_name!t]" style "file_picker_text"

                    key "save_delete" action FileDelete(i)


screen file_picker_save():

     frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    style "file_picker_text"
                    has hbox
                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    # if "same" == "same"

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

  #  use navigation
    use file_picker_save

screen load():

    # This ensures that any other menu screen is replaced.

    tag menu
    #use navigation
    use file_picker_load

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text:
        size 30
        color "#000"
        yoffset 30
        xoffset 40
    style save_button_close:
        xalign 0.93
        yalign 0.1
    style file_picker_nav: 
        xalign 0.2
        yalign 0.2




##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    frame:
        background "bg/studio.png"
    window :
        style "custom_window"
        background "ui/settings_screen.png"


    tag menu

    imagebutton auto "ui/load/close_button_%s.png" action Return() style "save_button_close" 
    # Include the navigation.
    #use navigation
    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                background None
                xpos 360
                ypos 290
                has vbox
                textbutton _("Window") action Preference("display", "window") style "pref_button" text_style "pref_button_text"
                textbutton _("Fullscreen") action Preference("display", "fullscreen") style "pref_button"

            frame:
                background None
                xpos 380
                ypos 420
                has vbox
                spacing 10
                textbutton _("All") action Preference("transitions", "all") style "pref_button"
                textbutton _("None") action Preference("transitions", "none") style "pref_button"

            frame:
                background None
                xpos 130
                ypos 560
                has vbox

                bar value Preference("text speed") style "options_slider" 

        vbox:
            frame:
                background None
                xpos 300
                ypos 290
                has vbox
                spacing 10
                textbutton _("SEEN MSGS.") action Preference("skip", "seen") style "pref_button"
                textbutton _("ALL MSGS.") action Preference("skip", "all") style "pref_button"


            frame:
                background None
                xpos 300
                ypos 410
                has vbox
                spacing 10
                textbutton _("STOP SKIP") action Preference("after choices", "stop") style "pref_button"
                textbutton _("CONT. SKIP") action Preference("after choices", "skip") style "pref_button"

            frame:
                background None
                xpos 40
                ypos 560
                has vbox

                bar value Preference("auto-forward time") style "options_slider"

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                background None
                xpos -50
                ypos 300
                has vbox

                bar value Preference("music volume") style "options_slider"

            frame:
                background None
                xpos -50
                ypos 495
                has vbox

                bar value Preference("sound volume") style "options_slider"

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"


init -2:
 
    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    #tag menu
    modal True

    window:
        background None

    frame:
        style_group "yesno"
        background Frame("ui/alert_window.png")
        bottom_padding 70
        top_padding 20
       # xfill True
        xalign 0.5
        yalign 0.4

        has vbox:
            #xalign .5
           # yalign .5
            spacing 30

        label message:
            text_style "alert_text"
            top_padding 60
            xpadding 45
            xalign 0.7

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action text_style "alert_text_button" style "alert_box_style"
            textbutton _("No") action no_action text_style "alert_text_button" style "alert_box_style"

    # Right-click and escape answer "no".
    key "game_menu" action no_action


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style "quick_menu_box"


        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave() text_style "quick_menu_text" style "quick_menu_text_button"
        textbutton _("Q.Load") action QuickLoad() text_style "quick_menu_text" style "quick_menu_text_button"
        textbutton _("Auto") action Preference("auto-forward", "toggle") text_style "quick_menu_text" style "quick_menu_text_button"
        textbutton _("Skip") action Skip() text_style "quick_menu_text" style "quick_menu_text_button"
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

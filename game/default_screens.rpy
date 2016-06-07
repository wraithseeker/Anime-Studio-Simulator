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
    imagebutton auto "ui/float_buttons/anime_%s.png" style "float_anime" action ShowMenu("anime_status") at float_btn_trans hovered tt.Action("Anime Status")
    imagebutton auto "ui/float_buttons/member_%s.png" style "float_member" action ShowMenu("member_status") at float_btn_trans hovered tt.Action("Member Status")
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
                text who id "who" font "fonts/Multicolore.otf" bold False size 35

            text what id "what" color "#000" font "fonts/LiberationSans-Regular.ttf" size 30 #outlines [(0.5, "#C8F7C5", 0, 0)]
    

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
        yalign 0.45

        vbox:
            style "menu"
            spacing 25

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        ypadding 20
                        xpadding 35
                        style "menu_choice_button"
                        background Frame("ui/textbox.png",10,10)
                        text caption style "menu_choice" color "#000" size 35

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
    modal True
    window style "textbox_window":
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
        textbutton _("Load") action ShowMenu("load_mainmenu")  text_style "mainmenu_text" style "mainmenu_button"
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

screen file_picker():

    frame:  
        background None
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
                $ file_time = FileTime(i)
                
                
                # Each file slot is a button.
                button:
                    #background None
                    background "ui/save/save_frame_box_empty.png"
                    xpadding 70
                    ypos -10
                    action FileAction(i)
                   # background None
                    has vbox
                    spacing 50
                    #show "ui/save/save_frame_box_empty.png"
                    # Add the screenshot. empty="ui/save/save_frame_box_empty.png" << empty box
                    if file_time == "this ":
                        text "This [file_time]" size 60

                    add FileScreenshot(i) xpos -35 ypos 20
               
                
                    text "[file_time!t][save_name!t]" style "file_picker_text"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    window:
        background "ui/save/save_screen.png"

  #  use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    window:
        background "ui/load/load_screen.png"
    tag menu
    #use navigation
    use file_picker

screen load_mainmenu:
    tag menu
    window:
        background "bg/studio.png"
    use load

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
  




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

screen notify(message):
    zorder 100

    text message at _notify_transform size 35

    # This controls how long it takes between when the screen is
    # first shown, and when it begins hiding.
    timer 3.25 action Hide('notify')

transform _notify_transform:
    # These control the position.
    xalign .02 yalign .015

    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


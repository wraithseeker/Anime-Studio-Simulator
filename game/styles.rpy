## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1:
    style options_slider:
        xmaximum 455
        ymaximum 32
        xpos 50
        left_bar "ui/bar_full.png"
        right_bar "ui/bar_empty.png"
        thumb  "ui/bar_thumb.png"
        thumb_shadow None
        thumb_offset 16

    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        color "#000"
        size 40
        layout "subtitle"
    style pref_button:
        background None
        # xpadding 20
        # top_padding 15
        xysize (257,66)
        selected_background "ui/settings_button_hover.png"
        selected_hover_background "ui/settings_button_hover.png"
    style pref_button_text is text:
        color "#000"
        size 35
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style alert_text:
        color "#000"
        size 45
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style alert_text_button:
        color "#000"
        size 75
        xalign 0.5
        yalign 0.5
        text_align 0.5

    style alert_box_style:
        #bottom_margin 100
        background "ui/alert_button_hover.png"
        xysize(304,121)
    style mainmenu_frame:
        xfill True
        background None
    style mainmenu_text:
        color "#fff"
        size 60
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style mainmenu_button:
        xysize (304,121)
        background None
        hover_background "ui/title_screen_button.png"

    style custom_window:
        color "#000"
    style say_dialogue:
        color "#000"
        font "fonts/LiberationSans-Regular.ttf"
        size 30
        ypos -40
    style say_thought:
        color "#000"
        font "fonts/LiberationSans-Regular.ttf"
        size 30
    style say_label:
       # padding_top
       size 30
       ypos -40
       font "fonts/LiberationSans-Regular.ttf"
    # style say_vbox:

    style textbox_window:
        background Frame("ui/textbox.png",10,10)
        #background None
        left_margin 500
        right_margin 550
        top_margin 6
        bottom_margin 50
        left_padding 30
        right_padding 10
        top_padding 60
        bottom_padding 0
        yminimum 300
    style quick_menu_text:
        color "#77736F"
        hover_color "#000"
        selected_color "#000"
        font "fonts/LiberationSans-Regular.ttf"
    style quick_menu_text_button:
        background None
    style quick_menu_box:
        background None
        xalign 0.64
        yalign 0.77
    style save_button_text:
        size 35
        color "#000"
    style save_load_pagination is text:
        size 45
        color "#000"
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style save_load_pagination_button:
         background None
         xysize (74,79)
         selected_background "ui/load/filepicker_nav_button_selected.png"
    style float_date:
        # xalign 0.9
        # yalign 0.05
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style float_date_text:
        color "#000"
        size 42
        font 'fonts/FiraSans-Regular.ttf'
      
    style float_anime:
        xalign 0.925
        yalign 0.085
        #hover_background "ui/float_buttons/anime_status.png"
    style float_member:
        xalign 0.975
        yalign 0.085
    style tooltip_value is text:
        size 30
    style task_tooltip:
        size 30
        color "#000"
    style task_stats_tooltip:
        size 30
        color "#000"
        font 'fonts/LiberationSans-Bold.ttf'
    style anime_status_window:
        background "ui/anime_status/anime_status_screen.png"
    style side_nav:
        background "ui/nav_sidebar.png"
        xysize (400,900)
        xalign 0.92
        yalign 0.37
    style sidenav_week_button:
        background None
        ypos 25
        xpos 20
    style sidenav_week:
        size 65
        color "#000"
    style sidenav_day_button:
        background None
        ypos 30
        xpos 25
    style sidenav_day:
        size 35
        color "#000"
    style sidenav_money_text:
        xpos 125
        ypos 65
        size 60
        color "#000"
    style sidenav_menu_buttons:
        background None
        xysize(344,66)
        hover_background "ui/side_menu_button_hover.png"
        selected_background "ui/side_menu_button_hover.png"
        ypos 125
        xpos 45
    style sidenav_menu_buttons_text:
        size 35
        color "#000"
        hover_color "#000"
        xalign 0.5
        yalign 0.5
        text_align 0.5
    style member_status_window:
        background "ui/member_status_screen.png"
    style outsource_window:
        background "ui/outsource/outsource_screen.png"
    style outsource_buttons:
        xysize(300,125)
    style outsource_buttons_outsource:
        xysize(300,125)
        xalign 0.6
        yalign 0.88
    style upgrade_button:
        xysize(300,125)
        xalign 0.6
        yalign 0.88
        background None
    style sidenav_done:
        xysize(460,124)
        ypos 822
    style upgrade_window:
        background "ui/upgrade_screen.png"
    style task_window:
        background "ui/tasks_screen.png"
    style file_picker_text:
        size 35
        color "#000"
        text_align 0.5
        xpos 10
    style save_button_close:
        xalign 0.93
        yalign 0.1
    style file_picker_nav: 
        xalign 0.2
        yalign 0.2
    style task_text:
        size 25
        color "#000"
        hover_color "#27ae60"
        #selected_color "#27ae60"
    style task_text_selected:
        size 25
        color "27ae60"
    style task_button:
        background None
    style char_title_text:
        color "#000"
        size 40
        xpos 27
    style input_prompt:
        size 30
        color "#000"
        ypos -33
    style input_text:
        color "#000"
        font "fonts/LiberationSans-Regular.ttf"
        size 30
    style anime_name:
        color "#000"
        font "fonts/LiberationSans-Bold.ttf"
        size 30
        ypos 180
        xpos 210
        text_align 0.5
    style weekly_label_text:
        color "#000"
        size 40
    style skip_indicator:
        size 35
    style popup_text:
        color "#27ae60"
        size 60
        outlines [(1,"#000",0,0)]
        kerning 3
        font "fonts/LiberationSans-Bold.ttf"


init python:
    layout.MAIN_MENU = _("ARE YOU SURE YOU WANT TO QUIT?")
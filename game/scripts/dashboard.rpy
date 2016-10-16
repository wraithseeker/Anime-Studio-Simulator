style game_dashboard_window:
    background "bg/studio.png"

screen game_dashboard(): 
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "game_dashboard_window"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98
        has vbox

        textbutton "Back" action Return()
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character('Yukari', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define m = Character('Mayumi', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define s = Character('Sumiko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define yuu = Character('Yuuko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define ss = Character('Shunsuke', color="#000",ctc="ctc_fixed",ctc_position="fixed")

init: 
    $_game_menu_screen = "navigation"
    $yukari_upgrade_selected = False
    $yuuko_upgrade_selected = False
    $sumiko_upgrade_selected = False
    $mayumi_upgrade_selected = False
    $shunsuke_upgrade_selected = False
    #positions for images
    $pos_farleft = Position(xalign = -0.045,yalign = 1.0)
    $pos_left = Position(xalign = 0.18,yalign = 1.0)
    $pos_middle = Position(xalign = 0.5,yalign = 1.0)
    $pos_middleright = Position(xalign = 0.65,yalign = 1.0)
    $pos_farright = Position(xalign = 1.1,yalign = 1.0)
    $pos_right = Position(xalign = 0.92,yalign = 1.0)
    python:
        Yukari_stats = Stats("Yukari")
        Mayumi_stats = Stats("Mayumi")
        Sumiko_stats = Stats("Sumiko")
        Yuuko_stats = Stats("Yuuko")
        Shunsuke_stats = Stats("Shunsuke")

# The game starts here.
label start:
   
    scene bg restaurant
    show yukari laugh_eyes_closed at pos_left
    show yuuko at pos_right
    show sumiko at pos_farright behind yuuko
    show shunsuke at pos_middleright
    with dissolve
    y "I have great news to share with all of you regarding our anime project!"
    s "After planning for the past few weeks, I’m glad we finally have some news."
    ss "What’s the news? You look really excited, so I guess it's related to our funding?"
    show yukari happy
    y "That's right! I managed to secure enough funding from investors for us to start the anime project. I’ve also rented a studio for us to work in."
    show sumiko worry
    s  "That’s awesome! Although I'm curious as to how you convinced them, since we don't have any concrete work to show..."
    show yukari worry
    y "Well that's … complicated. It's a long story, but what's important is that we can finally get started on our dream, right?"
    "Directing her own anime is Yukari’s greatest dream. Funding puts her dream one step closer to reality. She can hardly breathe from excitement."
    show shunsuke laugh_eyes_closed
    show sumiko
    ss "I agree. Getting funded was one of our biggest hurdles."
    ss "If we take into account that only five of us will be working on the project, we’d probably never be able to finish it without funding."
    show yuuko worry
    yuu "Not to mention that we have to outsource the animation work too which can be very expensive even though the animators aren’t well paid…"
    show yukari
    y "For now, let's celebrate our funding!"
    y " We'll start working on the project next week. Our journey will be long and tough, but I believe we can pull through it together!"
    show mayumi happy at pos_farleft behind yukari with dissolve
    m "Yeah! The details can wait. Let’s celebrate! "
    show yuuko happy
    show sumiko happy
    "At Mayumi’s declaration, everyone cheers. Everyone excitedly discusses their hopes and dreams for the upcoming project. "
    jump pre_game
    return

label pre_game:
    $game_casual = False
    scene bg studio with dissolve
    "This is their new studio where they would be working hard to produce their own anime series within 3 months."
    "You'll be managing everyone, keeping track of their status to avoid stressing them out which would lower their productivity."
    "There are tasks you can assign the team members to do two times in a week."
    "You'll eventually have to outsource work outside and you can send them off to upgrade their skills too!"
    menu:
        "Do you prefer playing the game casually?"
        "I'm new to the game!":
            $game_casual = True
        "I'm fine by myself!":
            $game_casual = False

    "[game_casual]"
    if game_casual:
        " I am a casual"
    else:
        pass

    show screen start_game

label test:
    "We are at the end of the world"
    "Press enter to quit"
   # $Yukari_stats.human_relations += 3
   # "On a side node, [Yukari_stats.name]'s human relation is now [Yukari_stats.human_relations]"
    return

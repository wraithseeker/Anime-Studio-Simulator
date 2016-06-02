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
    $pos_1 = Position(xalign=0.1,yalign=1.0)
    $pos_2 = Position(xalign=0.2,yalign=1.0)
    $pos_3 = Position(xalign=0.3,yalign=1.0)
    $pos_4 = Position(xalign=0.4,yalign=1.0)
    $pos_5 = Position(xalign=0.5,yalign=1.0)
    $pos_6 = Position(xalign=0.6,yalign=1.0)
    $pos_7 = Position(xalign=0.7,yalign=1.0)
    $pos_8 = Position(xalign=0.8,yalign=1.0)
    $pos_9 = Position(xalign=0.9,yalign=1.0)
    $pos_10 = Position(xalign=1,yalign=1.0)
    python:
        Yukari_stats = Stats("Yukari")
        Mayumi_stats = Stats("Mayumi")
        Sumiko_stats = Stats("Sumiko")
        Yuuko_stats = Stats("Yuuko")
        Shunsuke_stats = Stats("Shunsuke")

# The game starts here.
label start:
   
   
    scene bg studio with dissolve
    show yukari at left
    show sumiko at pos_9
    y "I have great news to share with all of you regarding our anime project!"
    s "After planning for the past few weeks, I’m glad we finally have some news."
    show shunsuke at pos_6 with moveinright
    ss "What’s the news? You look really excited, so I guess it's related to our funding?"
    y "That's right! I managed to secure enough funding from investors for us to start the anime project. I’ve also rented a studio for us to work in."
    jump test
    return

label test:
    "We are at the end of the world"
    "Press enter to quit"
   # $Yukari_stats.human_relations += 3
   # "On a side node, [Yukari_stats.name]'s human relation is now [Yukari_stats.human_relations]"
    return

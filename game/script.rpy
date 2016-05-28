# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character('Yukari', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define m = Character('Mayumi', color="#fff")


# The game starts here.
label start:
    $_game_menu_screen = "navigation"
    python:
        Yukari_stats = Stats("Yukari")
        Mayumi_stats = Stats("Mayumi")
        Sumiko_stats = Stats("Sumiko")
        Yuuko_stats = Stats("Yuuko")
        Shunsuke_stats = Stats("Shunsuke")
    scene bg studio with dissolve
    show yukari at left
    y "That’s awesome! Although I'm curious as to how you convinced them, since we don't have any concrete work to show... "
    "Directing her own anime is Yukari’s greatest dream. Funding puts her dream one step closer to reality. She can hardly breathe from excitement."
    $Yukari_stats.UpgradeProficiency(5)
    "Yukari proficiency is [Yukari_stats.proficiency] "
    # $mynumber = renpy.random.randint(1,10)
    # "[mynumber]"
   # call screen game_dashboard
    $Yukari_stats.happiness += 15
    y "Once you add a story, pictures, and music, you can release it to the world!"
    y "My name is [Yukari_stats.name] and my current stress level is [Yukari_stats.stress]"

    $Yukari_stats.human_relations += 15
    y "My best friend is Mayumi, who has a stress level of [Mayumi_stats.stress]"
    jump test
    return

label test:
    "We are at the end of the world"
    "Press enter to quit"
   # $Yukari_stats.human_relations += 3
   # "On a side node, [Yukari_stats.name]'s human relation is now [Yukari_stats.human_relations]"
    return

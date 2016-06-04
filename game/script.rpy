# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character('Yukari', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define m = Character('Mayumi', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define s = Character('Sumiko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define yuu = Character('Yuuko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define ss = Character('Shunsuke', color="#000",ctc="ctc_fixed",ctc_position="fixed")
    
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

label pre_game:
    scene bg studio with dissolve
    $anime.name = renpy.input("Name of your anime?",default="",length=20)
    if anime.name == "":
        $anime.name = "Macross Delta"
    "[anime.name] sounds great! Let's go through the basics of the game."
    "This is their new studio where they would be working hard to produce [anime.name] within 3 months."
    "You'll be managing everyone, keeping track of their status to manage their stress level that could hinder the progress on [anime.name]."
    "Tasks can be assigned to each member two times a week. You'll eventually have to outsource work and it is a good idea to send your team members for training occasionally."
    
    menu:
        "Which difficulty level do you prefer?"
        "Casual":
            $game_casual = True
        "Normal":
            $game_casual = False

    if game_casual:
        "You have chosen to create [anime.name] under the casual mode."
    else:
        "You have chosen to create [anime.name] under the normal mode."

    show screen start_game
    "This is where you'll oversee the production of [anime.name]. The deadline for [anime.name] will be during {font=fonts/LiberationSans-Bold.ttf}Week 10{/font}."
    "The most important thing is to choose tasks for your team member under {font=fonts/LiberationSans-Bold.ttf}'Tasks'{/font}. After that you can end your turn by selecting the {font=fonts/LiberationSans-Bold.ttf}'Done'{/font} button."
    "Good luck with [anime.name]!"
    call screen side_nav
label test:
   
    "Press enter to quit"
    return

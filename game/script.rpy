# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character('Yukari', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define m = Character('Mayumi', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define s = Character('Sumiko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define yuu = Character('Yuuko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define ss = Character('Shunsuke', color="#000",ctc="ctc_fixed",ctc_position="fixed")

transform weekly_text_transform:
    xalign 0.5 yalign 0.42 alpha 0.0
    linear 2 alpha 1.0
    pause 3.0
    linear 2 alpha 0.0
# The game starts here.
label start:
    jump week_2_1
    scene bg restaurant
    show yukari laugh_eyes_closed at pos_left
    show yuuko at pos_right
    show sumiko at Position(xalign = 1.1,yalign = 1.0) behind yuuko
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
    $current_label = "scene_1"
    show screen start_game
    $side_nav_interaction = False
    "This is where you'll oversee the production of [anime.name]. The deadline for [anime.name] will be during {font=fonts/LiberationSans-Bold.ttf}Week 10{/font}."
    "The most important thing is to choose tasks for your team member under {font=fonts/LiberationSans-Bold.ttf}'Tasks'{/font}. After that you can end your turn by selecting the {font=fonts/LiberationSans-Bold.ttf}'Done'{/font} button."
    "Good luck with [anime.name]!"
    $side_nav_interaction = True
    hide screen start_game
    call screen start_game

label week_1_1:
    scene bg studio
    $renpy.show("weekly_popup_text",what=Text("Monday",style="weekly_label_text"),at_list=[weekly_text_transform])
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright
    show sumiko at Position(xalign = 1.1,yalign = 1.0) behind yuuko
    show yuuko at pos_right
    with dissolve
    "On Monday, Yukari gathers everyone together at the studio. It’s time to discuss and finalize the details about [anime.name]."
    show mayumi worry at pos_farleft
    m "So… what type of anime is [anime.name], again?"
    hide weekly_popup_text
    show sumiko sigh
    s "We’ve been talking about it for weeks, and you still don’t know?"
    show mayumi tsundere
    m " I was listening to music!"
    ss "Every time it came up?"
    m "I have a lot of music."
    y "Don’t worry about it. To clarify for Mayumi’s sake, [anime.name] is…"
    show sumiko
    menu:
        "Idol Anime":
            pass
        "Harem Anime":
            pass
        "Mystery Anime":
            pass
        "Shounen Anime":
            pass
        "Shoujo Anime":
            pass
    show mayumi happy
    show sumiko
    m "Okay! I can't wait!"
    show yukari happy
    y "Now that we have our studio, let's assign desks."
    y "Yuuko and Sumiko should take the two desks beside one another."
    show sumiko happy
    s "Because we’re sisters, right?"
    y "Well, I was thinking because you’re both working on the art."
    y "Yuuko will be designing the characters while Sumiko will be drawing the backgrounds."
    ss "You decided we should outsource the animation, correct?"
    show yukari worry
    y "Yeah, if we try to handle the animation ourselves…"
    show mayumi laugh_eyes_closed
    m "I bet it would turn out wonderful!"
    show sumiko angry_mouth_closed
    s " Is there anything you don’t think is wonderful?"
    m "Yes, thunderstorms… Although sometimes they’re so pretty!"
    show sumiko sigh
    s "I rest my case."
    show mayumi happy
    "Mayumi giggles and runs to a desk in the corner of the room."
    m "I’ll take this one! I suppose Shunsuke gets the desk on the other side of the room?"
    show yukari angry
    y "You two better take those desks, because the middle one is mine!"
    y "Also, Mayumi, since the sound director won’t have much to do in the planning phase, you can help me out with some paperwork for now."
    show yukari
    show mayumi
    m "Okay!"
    m "Shunsuke, how far along is the scenario for [anime.name]?"
    show shunsuke happy
    ss "I finished writing it a few weeks ago, actually. Last weekend, I completed the edits, so I’m pretty happy with it."
    show yukari happy
    y "Sweet! Let me have a look."
    "Shunsuke hands over his copy of the scenario. She smiles more with each page she reads."
    y "It's perfect! It’s exactly the way I envisioned it. What do the rest of you think?"
    "Yukari passes the draft to Sumiko. Yuuko reads over her shoulder, and Mayumi runs back from her desk to read it as well."
    show mayumi laugh_eyes_closed
    show yuuko laugh_eyes_closed
    show sumiko laugh_eyes_closed
    m "I love it!"
    s "Looks good to me."
    yuu "Yes, it’s very nice."
    y "Now, down to business."
    show shunsuke
    show yukari
    show mayumi
    show yuuko
    show sumiko
    y "At our current rate, and considering our funding, we'll probably last one or two months before we get kicked out of this room."
    y "That won’t exactly be a pleasant experience. Maybe we can finish up before then, but I think it’s a wise idea to raise additional funds."
    show mayumi happy
    m "It helps that we’re bootstrapping. Plus, none of us will get paid a single cent until the project comes to fruition!"
    s "Why do you sound so happy about not being paid?"
    m "Because it’s already reduced our costs by over 70\%!"
    m "Wow… can you imagine, in this day and age, getting a group of people to work on an anime project for free? It’s insane!"
    show sumiko tsundere
    s "You’re talking about US. We’re not insane!"
    yuu "If we were… would we know?"
    ss "It’s not insanity. We don't have any real living costs, since we all still live with our parents. Besides, we just graduated. We have nothing better to do."
    ss "If we didn’t have this, we’d probably just goof off until university starts. Working on this sounds a lot more exciting."
    y "All right, let’s not go too off-topic here. It’s time to get to work! What should we focus on today?"
    menu:
        "Sketching character designs & backgrounds":
            "Yuuko and Sumiko start sketching designs for [anime.name]. Yukari delegates tasks to the others, and everyone begins work."
        "Refine scenario":
            "Shunsuke takes another look at the scenario to tighten and polish the story. Yukari delegates tasks to the others, and everyone begins work."

# label start:
#     jump week_1_3
label week_1_2:
    scene bg studio with fade
    show yukari sad at pos_farleft
    $renpy.show("weekly_popup_text",what=Text("Tuesday",style="weekly_label_text"),at_list=[weekly_text_transform])
    "Although the others have their tasks set out for them, Yukari realizes there isn’t much she can do at this stage in the process. The same goes for Mayumi."
    "Yukari paces in frustration. She can’t sit around and do nothing."
    hide weekly_popup_text
    "After taking a moment to think of possible things she can do to help, Yukari decides to…"
    menu:
        "Read books about management":
            pass
        "Networking with people":
            pass
        "Supervise Yuuko & Sumiko":
            pass

label week_1_3:
    scene black with dissolve
    "A few days pass. It’s Friday."
    "When Yukari first gathered the team to work on [anime.name], she made a promise with them to meet up and have dinner together every Friday."
    "Ever since then, they’ve all made it to this recurring event without fail."
    scene bg restaurant
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at Position(xalign = 1.1,yalign = 1.0) behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    "What a stroke of luck that Sumiko and Yuuko’s family owns a classy restaurant like this. Yukari and the others can dine in style with good friends and a discounted bill."
    show yukari happy
    y "The tempura in this shop is always so good! Maybe it's just because I love tempura so much."
    show sumiko sigh
    s "Don't lie, you’re not fooling anyone."
    show yukari sad
    y "Huh?"
    s "We all know you only started eating it because you watched (insert random Anime Name)"
    s "You just want to be like your favorite character who loves tempura."
    show sumiko
    "Embarrassed, Yukari ducks her head."
    y "Well, that's kind of true, in a sense."
    s "There’s no “kind of” about it."
    show yukari laugh_eyes_closed
    y "Hey! <anime A character name> may have introduced me to tempura, but now I really love it!"
    show mayumi happy
    m "I wish my favorite characters introduced me to new foods…"
    "She stirs her spoon into her half-melted cup of ice cream and pouts for a moment, but then her expression brightens."
    show yukari
    m "Speaking of characters, are our characters almost done? How close are we?"
    y " I'd say we're quite close."
    show yuuko sad_angry
    yuu "We’re not close."
    show shunsuke sad_angry
    ss "You can’t both be right."
    show yukari worry
    y "They just need a few minor touches here and there and we should be good."
    show yuuko sad
    yuu "The character designs aren’t up to my standards yet… If only I was a better artist."
    show yukari
    y "Don't belittle yourself so much! They look great, and that’s what matters! I like them, and next week we’ll have everyone take another look."

label week_1_4:
    scene black with dissolve
    "When the weekend comes, Yukari finds some free time at last. She wonders if she should get more work done on [anime.name] or take it easy for now."
    menu:
        "Have some fun":
            pass
        "Work on [anime.name]":
            pass
    scene studio with dissolve
    $current_week = 2
    call screen start_game

transform flip:
    xzoom -1
label week_2_1:
    scene studio
    show yukari at pos_left
    show sumiko at Position(xalign = 1.1,yalign = 1.0)
    show shunsuke at pos_middleright_half
    show yuuko_f at pos_farleft behind yukari
    with dissolve
    $renpy.show("weekly_popup_text",what=Text("Monday",style="weekly_label_text"),at_list=[weekly_text_transform])
    "On Monday, Yukari spends some time going through the scenario for [anime.name]. Then she gathers everyone together to look at the character designs."
    y "I think they’re fine. I don’t see any major flaws. What do the rest of you think?"
    hide weekly_popup_text
    ss "Well…"
    s "Uh-oh. Dramatic pause from Shunsuke. Here comes trouble…"
    "Yukari fidgets silently and braces herself. There’s nothing wrong with constructive criticism, but if he presents his issues with the art poorly, it could cause their team’s first major disagreement."
    ss "Personally speaking, the character designs aren’t really what I had in my mind."
    ss "I'm not saying the design is bad, but the art style doesn't go well with the scenario I wrote for [anime.name]"
    ss "We should redo these designs so they display the characters’ traits and fit the story better."
    yuu "I know the designs need to be refined, but I can’t completely redo them all."
    yuu "It took me quite a while to get the designs right. I had a lot of trouble choosing the art style for [anime.name]."
    ss "The one you chose just doesn’t work."
    yuu "Art style and references have never been a problem for before, but I was usually drawing fan art. I guess I need to improve, fast."
    yuu "But if I have to re-do all the character designs, I’m scared we won’t meet our deadline!"
    ss "Yukari should be the one to decide. She’s in charge."
    y "Hmm…"
    "Each side has good points, but with a limited budget and limited time, Yukari has to make this decision carefully."
    menu:
        "Side with Yuuko":
            "Yuuko is right. They have a tight deadline to finish [anime.name], and they need to make 6 episodes."
            "They’ll need to touch up the designs, but Yukari decides re-doing them would cause more harm than good by setting their progress back so far."
        "Side with Shunsuke":
            "Shunsuke is right. While they may have a tight deadline to finish the 6 episodes of [anime.name], rushing things might not be the best."
            "Yukari decides it’s best to work with a firm foundation instead of a shaky one. The character designs need to be re-done to match the scenario, or else the project’s value will ultimately be lowered."



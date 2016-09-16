# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define y = Character('Yukari', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define m = Character('Mayumi', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define s = Character('Sumiko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define yuu = Character('Yuuko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define ss = Character('Shunsuke', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define bot = Character('Recorded Voice', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define unknown = Character('???', color="#000",ctc="ctc_fixed",ctc_position="fixed")

# The game starts here.

label game_start:
    $first_w_events = ["random_29"]#["rande_1","rande_2","rande_3","rande_4","rande_5","rande_6","rande_7"]

    #start of the game
    #jump week_3_2
    #scene black with dissolve
    # the command to move to next day
    #scene image "cg/flashback.png"
    $nextDay()
    $rand_choice = renpy.random.choice(first_w_events)
    $first_w_events.remove(rand_choice)
    call expression rand_choice from _call_expression
    scene bg studio_main
    stop music
    play music "music/normal_happy_ost.ogg" fadein 1.0
    y "this is some text"


    
    # $anime.prev_marketing = 2
    # $anime.marketing = 2

    # $anime.prev_voice_acting = 4
    # $anime.prev_ost = 0
    # $anime.prev_op_ed = 3

    # # $anime.voice_acting = 6
    # $anime.prev_funds = 10
    # $anime.funds = 10
    # $anime.prev_character_development = 1
    # $anime.character_development = 1
    # $anime.character_development += 2
    # $anime.character_design = 2
    # $anime.prev_character_design = 2
    # $anime.character_design -= 1
    # $anime.funds += 10
    # $anime.voice_acting = 1
    # $anime.op_ed = 1
    # $anime.marketing -= 0.5
    
    $yukari_stats.management = 3
    $yukari_stats.prev_management = 2
    $yukari_stats.stress = 2
    $yukari_stats.prev_stress = 3
    $yukari_stats.proficiency = 3
    $yukari_stats.prev_proficiency = 2
    $yukari_stats.happiness = 3
    $yukari_stats.prev_happiness = 1

    $yuuko_stats.stress = 2
    $yuuko_stats.prev_stress = 3
    $yuuko_stats.proficiency = 3
    $yuuko_stats.prev_proficiency = 4

    $sumiko_stats.stress = 4
    $sumiko_stats.prev_stress = 1
    $sumiko_stats.proficiency = 3
    $sumiko_stats.prev_proficiency = 2

    $shunsuke_stats.stress = 2
    $shunsuke_stats.prev_stress = 3
    $shunsuke_stats.proficiency = 3
    $shunsuke_stats.prev_proficiency = 2

    $mayumi_stats.stress = 4
    $mayumi_stats.prev_stress = 3
    $mayumi_stats.proficiency = 3
    $mayumi_stats.prev_proficiency = 2

    $UpdateProgressReport()
    y "previous value of marketing is [anime.prev_marketing]. Current value is [anime.marketing]"
    #call screen progress_report
    "Welcome to the demo version of Anime Studio Simulator. For our music, we have a few pieces composed for our OST while the rest of them are royalty free placeholders. Some scenes do not have an OST yet."
    "The demo version covers the events of the game up till week 3 with a total of 12 weeks planned for the game's release."
    "We hope you enjoy playing the demo version of Anime Studio Simulator!"


# label tester:
#     "lets test anime character design variable"
#     "[anime.character_design] value, let's add 2 to it"
#     $anime.character_design = anime.character_design + 2
#     "[anime.character_design] value"
#     "Now why doesn't object get saved?"

label week_0_1:
    scene black with dissolve
    "It’s the day after high school graduation. Yukari’s mind is already filled with plans for how she’ll spend vacation."
    "For many people, it’s a time to relax, prepare for higher education, or pursue jobs. For her, it’s a time to make her greatest dream come true."
    "She just needs to find the right group of people to help her."
    #scene cafe
    scene image "bg/office_fix2.jpg"
    show yukari happy at left
    show mayumi_f at right
    with dissolve
    y "Mayumi! Over here!"
    $nextDay()
    "She waves to her best friend, who crosses the room and joins her at the table."
    m "I got your message. What’s up?"
    y "I’ve found a character artist for our anime project."
    show mayumi_f laugh_eyes_closed
    m " That’s great! Before long we’ll have a whole team together!"
    show yukari laugh_eyes_closed
    "Yukari smiles. As her closest friend, Mayumi was the first person she asked to help her create an anime. With her love of music, she volunteered to be the sound director right away."
    show mayumi_f 
    m "Who is the artist?"
    show yukari
    y "Her name is Yuuko. I haven’t met her in person yet, but I’ll be seeing her tonight."
    m "Good luck! If you need anything, just give me a call."
    show yukari happy
    y "Thanks. We just need a few more people, and we’ll be ready to do this!"

label week_0_2:
    scene restaurant
    show yukari at left
    with fade
    "Yukari double-checks the address. She’s at the right place. A little nervous, she looks around the stylish restaurant."
    show sumiko at Position(xalign=0.8,yalign=1.0) with dissolve
    unknown "Hi! Yukari?"
    y "That’s right. Are you Yuuko?"
    show sumiko happy
    unknown "No, I’m her sister, Sumiko. It’s nice to meet you!"
    show yuuko at pos_outerright with dissolve
    unknown "I’m Yuuko."
    show yukari happy
    y " Good to meet both of you. Yuuko, your art is fantastic! I’d love it if you helped create the characters for my anime project."
    show yuuko laugh_eyes_closed
    "Yuuko blushes with a shy smile, and Sumiko shakes Yukari’s hand enthusiastically."
    show sumiko happy
    s " I can’t wait to work together!"
    y "You want to join the team?"
    s "Well, Yuuko said you need a background artist."
    y "You’re an artist too? That’s great! Let’s sit down, and I’ll tell you two a little about my ideas…"

label week_0_3:
    scene street with dissolve
    show yukari at left with dissolve
    "Yukari walks down the street, deep in thought. Three days have passed since she met Yuuko and Sumiko."
    "She already put them in touch with Mayumi, and they all met up once to discuss their ideas. Everyone is excited about the project."
    "Yukari almost has an entire team together. She’ll direct her own anime. It doesn’t seem real."
    unknown "Excuse me."
    "Soon, her dream will come true…"
    show shunsuke at right with dissolve
    ss "You’re Yukari, aren’t you? "
    "Lost in her thoughts, it takes Yukari a moment to realize the boy is talking to her. She blinks at him. She recognizes him from school, but they never spoke."
    y "Yes? You’re… Shunsuke, right?"
    ss " Yes. I heard a rumor you’re making your own anime."
    "Now he has her attention."
    y "That’s right! Why?"
    ss "I’ve mainly written fan fiction, but I’d love to work on an original anime story. Do you need a writer?"
    show yukari happy
    y "Absolutely! We're still searching for a writer for our anime."
    ss "Could you tell me more about your project?"
    y "Sure!"
    "As they discuss the anime, Yukari’s excitement grows. There are many details they’ll need to go over, but she has a feeling she’s found her writer."

label week_0_4:
    scene bg restaurant with fade
    show yukari laugh_eyes_closed at pos_left
    show yuuko at pos_right
    show sumiko at pos_outerright behind yuuko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "Everyone, I have great news to share about our anime project!"
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
    show mayumi happy
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
    $show_floating_buttons = False
    "This is where you'll oversee the production of [anime.name]. The deadline for [anime.name] will be during {font=fonts/LiberationSans-Bold.ttf}Week 10{/font}."
    "The most important thing is to select tasks for your team member under {font=fonts/LiberationSans-Bold.ttf}Tasks{/font}. After that you can end your turn by selecting the {font=fonts/LiberationSans-Bold.ttf}Done{/font} button."
    "In this demo, the choices you make in the game won't affect the stats for the characters or the anime. When the game is released, the choices will have an effect on the stats."
    "For now, I randomly generated stats for [anime.name] and your team's status, so you can get a good look around the features of the game."
    "Good luck with [anime.name]!"

    $side_nav_interaction = True
    $show_floating_buttons = True
    hide screen start_game
    play music "music/dashboard.mp3" fadein 1.0
    $renpy.retain_after_load()
    call screen start_game
    stop music

label week_1_1:
    $initial_week = False
    scene bg studio
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright
    show sumiko at pos_outerright behind yuuko
    show yuuko at pos_right
    with dissolve
    "On Monday, Yukari gathers everyone together at the studio. It’s time to discuss and finalize the details about [anime.name]."
    show mayumi worry at pos_farleft
    m "So… what type of anime is [anime.name], again?"
    show sumiko sigh
    s "We’ve been talking about it for weeks, and you still don’t know?"
    show mayumi tsundere
    m " I was listening to music!"
    ss "Every time it came up?"
    m "I have a lot of music."
    y "Don’t worry about it. To clarify for Mayumi’s sake, [anime.name] is…"
    show sumiko
    menu:
        "Harem Anime":
            pass
        "Mystery Anime":
            pass
        "Action Anime":
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
        "Sketch character designs & backgrounds":
            "Yuuko and Sumiko start sketching designs for [anime.name]. Yukari delegates tasks to the others, and everyone begins work."
        "Refine scenario":
            "Shunsuke takes another look at the scenario to tighten and polish the story. Yukari delegates tasks to the others, and everyone begins work."

# label start:
#     jump week_1_3
label week_1_2:
    scene bg studio with fade
    show yukari sad at pos_farleft
    "Although the others have their tasks set out for them, Yukari realizes there isn’t much she can do at this stage in the process. The same goes for Mayumi."
    "Yukari paces in frustration. She can’t sit around and do nothing."
    "After taking a moment to think of possible things she can do to help, Yukari decides to…"
    menu:
        "Read books about management":
            pass
        "Network with people":
            pass
        "Supervise Yuuko & Sumiko":
            pass

label week_1_3:
    scene bg studio with fade
    show yukari at left
    show mayumi_f at Position(xalign=0.85,yalign=1.0)
    with dissolve
    "It’s the third day of work on [anime.name]. Yukari looks around the studio and can’t help but grin. The team is hard at work. [anime.name] will be a reality. This is exactly what she’s always dreamed up."
    m "Hey Yukari, want to get lunch?"
    show yukari worry
    y "What? Now?"
    show mayumi_f sigh
    m "Yeah. I mean, the last two days you barely ate."
    y "Is it really okay for me to leave? I mean, I’m the director!"
    "Shunsuke looks up from his work."
    ss "The rest of us take lunch breaks. Logically, you can too."
    y "But..."
    show sumiko tsundere at pos_outerright behind mayumi_f with dissolve 
    s "Oh, go on! We promise not to burn down the studio!"
    "Their reassurances help her set aside her guilt."
    show yukari happy
    y "Well, all right!"
    scene bg cafe with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    "The café is crowded, but they’re still able to find a place to sit without much difficulty."
    m "So, what does it feel like?"
    y "Huh?"
    m "You’re an anime director now!"
    show yukari sigh
    y "Haha, yes, I guess I am... It still feels unreal. I have a lot of responsibilities if I want to make [anime.name] a success."
    m "Don’t forget to relax now and then."
    y "What makes you say that?"
    show yukari worry
    y "Hey, there’s no way they’d actually burn anything down, right?!"
    show mayumi_f sigh
    m "If you’re taking Sumiko’s jokes seriously, you definitely need to relax."
    show yukari 
    y "Maybe you’re right."
    "She leans back in her seat and puts her worries out of her mind. One thing is certain: she can always count on Mayumi to make her feel better."
    scene bg studio with fade
    show sumiko at pos_middleright_half
    show yukari at pos_left
    show mayumi at pos_farleft
    show shunsuke at pos_farright
    with dissolve 
    "When they return, the studio is quiet. The other three are still hard at work."
    show sumiko sigh
    s "See? Nothing burned!"
    m "Aren’t you going to have lunch, too?"
    show sumiko
    s "Yuuko and I brought food from home. As for Shunsuke..."
    "She lowers her voice to a stage whisper."
    show sumiko angry
    s "I think maybe he’s a vampire!"
    show shunsuke tsundere
    ss " I heard that!"
    s "And?"
    ss "I ate earlier."
    s "Sure you did."
    ss "You really don’t think I eat?"
    show sumiko
    s "I’ve never seen you eat."
    show shunsuke sigh
    ss "I eat!"
    s "Prove it."
    ss "You need proof? Well just you wait!"
    s "I’m waiting, but nothing’s happening..."
    "Yukari clears her throat. They cut off their argument and look at her. Both look sheepish, although not quite as much as they should."
    show shunsuke
    show sumiko
    show yukari tsundere
    y "We’ve got an anime to work on, remember?"
    ss "Aye, aye."
    s "Aw, fine..."
    show yukari
    "Ridiculous as it was, their argument gives the studio a lighthearted atmosphere." 
    "The rest of the day is punctuated by Sumiko waving crosses at Shunsuke and shoving her compact mirror in his face to check his reflection."
    "Even though he seems so serious and focused, he tolerates her jokes and gives only mock-angry comebacks."
    show yukari happy
    "Watching them makes Yukari smile. Shunsuke was the last member to join the team, so it’s good to see him fitting in."

label week_1_4:
    scene studio with fade
    "The next day, Shunsuke makes good on his promise to prove he actually eats, and brings enough food from home for everyone to share."
    show sumiko at pos_middleright_half
    show yukari at pos_left
    show mayumi happy at pos_farleft
    show shunsuke at pos_farright
    with dissolve
    m "Party time!"
    show yukari worry
    y "Wait, a party? What are we celebrating?"
    m "Our first week in the studio!"
    ss "Today’s only Thursday. We haven’t been here a full week yet."
    show sumiko laugh_eyes_closed
    show yukari
    s "Then I guess we’re celebrating you not being a vampire!"
    ss "What did I do to deserve this…?"
    show yukari happy
    y "All right, all right! We can have a party if you want."
    m "Yes!"
    show shunsuke happy
    "There’s no harm in it, after all. They’re making good progress on [anime.name] and a little celebration will help bolster the team’s spirits."
    "After a while, however, Yukari looks around in surprise. They’re missing one."
    show yukari worry
    y "What happened to Yuuko?"
    show sumiko
    s "Oh, she said she was going to the café."
    y "How strange…"
    menu:
        "Find Yuuko":
            scene cafe
            show yukari at left
            with dissolve
            "Yukari finds Yuuko in the café at a table by herself. She has some papers with her and is sketching character ideas for [anime.name]."
            y "Yuuko?"
            show yuuko at right with dissolve
            yuu "Oh! Is something wrong?"
            y "No, I just wondered why you left."
            yuu "Oh… It was a little too noisy in the studio, that’s all. I wanted to go somewhere quiet so I could concentrate."
            show yuuko happy
            "She returns to her sketching with a smile on her face. Yukari watches her for a moment."
            "She seems happy enough. When they first met, Yukari worried her withdrawn nature might mean she felt out of place, but maybe she’s just quiet."
            "Yuuko lifts her head."
            yuu "You don’t mind me working here today, do you?"
            y " No, not at all… as long as you know you’re a valued member of the team and a good friend."
            show yuuko laugh_eyes_closed
            yuu "Hehe, thank you."
            "Nothing to worry about, then. She’ll fit in with the team just fine."

        "Stay in the studio":
            "There’s no reason to worry. The team members can have lunch wherever they want. If Yuuko doesn’t want to eat with the others, that’s her business."
            "Yukari shrugs and turns her attention back to the impromptu party, happy to have such a fun group of friends as part of her team."




label week_1_5:
    scene black with dissolve
    "It’s Friday."
    "When Yukari first gathered the team to work on [anime.name], she made a promise with them to meet up and have dinner together every Friday."
    "Ever since then, they’ve all made it to this recurring event without fail."
    scene bg restaurant
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    "What a stroke of luck that Sumiko and Yuuko’s family owns a classy restaurant like this. Yukari and the others can dine in style with good friends and a discounted bill."
    show yukari happy
    play sound "music/eat_crunchy.ogg"
    y "The tempura in this shop is always so good! Maybe it's just because I love tempura so much."
    show sumiko sigh
    s "Don't lie, you’re not fooling anyone."
    show yukari sad
    y "Huh?"
    s "We all know you only started eating it because you watched that cooking anime!"
    s "You just want to be like your favorite character who loves tempura."
    show sumiko
    "Embarrassed, Yukari ducks her head."
    y "Well, that's kind of true, in a sense."
    s "There’s no “kind of” about it."
    show yukari laugh_eyes_closed
    y "Hey! <anime A character name> may have introduced me to tempura, but now I really love it!"
    show mayumi happy
    m "I wish my favorite characters introduced me to new foods…"
    play sound "music/stirring_ice_cream.ogg"
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

label week_1_6:
    scene black with dissolve
    "When the weekend comes, Yukari finds some free time at last. She wonders if she should get more work done on [anime.name] or take it easy for now."
    menu:
        "Have some fun":
            pass
        "Work on [anime.name]":
            pass
    scene studio with dissolve
    $current_week = 2
    play music "music/dashboard.mp3" fadein 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    #call screen progress_report
    call screen start_game
    stop music

transform flip:
    xzoom -1
label week_2_1:
    scene studio
    show yukari at pos_left
    show sumiko at pos_outerright
    show shunsuke at pos_middleright_half
    show yuuko_f at pos_farleft behind yukari
    with dissolve
    "On Monday, Yukari spends some time going through the scenario for [anime.name]. Then she gathers everyone together to look at the character designs."
    y "I think they’re fine. I don’t see any major flaws. What do the rest of you think?"
    show shunsuke sad
    ss "Well…"
    show sumiko angry
    s "Uh-oh. Dramatic pause from Shunsuke. Here comes trouble…"
    show yukari sad
    "Yukari fidgets silently and braces herself. There’s nothing wrong with constructive criticism, but if he presents his issues with the art poorly, it could cause their team’s first major disagreement."
    show shunsuke sad_angry
    ss "Personally speaking, the character designs aren’t really what I had in my mind."
    ss "I'm not saying the design is bad, but the art style doesn't go well with the scenario I wrote for [anime.name]."
    ss "We should redo these designs so they display the characters’ traits and fit the story better."
    show yuuko_f worry
    yuu "I know the designs need to be refined, but I can’t completely redo them all."
    yuu "It took me a long time to get the designs right. I had trouble choosing the art style for [anime.name]."
    show shunsuke angry
    ss "The one you chose just doesn’t work."
    show yuuko_f sigh
    yuu "Art style and references have never been a problem for me before, but I was usually drawing fan art. I guess I need to improve, fast."
    yuu "But if I have to re-do all the character designs..."
    "Yuuko falls silent."
    s "You’re worried about the deadline, aren’t you?"
    yuu "Yes. I don’t know if I can re-do them in time."
    ss "Yukari should be the one to decide. She’s in charge."
    show yukari sad
    y "Hmm…"
    "Each side has good points, but with a limited budget and limited time, Yukari has to make this decision carefully."
    menu:
        "Side with Yuuko":
            "Yuuko is right. They have a tight deadline to finish [anime.name], and they need to make 6 episodes."
            "They’ll need to touch up the designs, but Yukari decides re-doing them would cause more harm than good by setting their progress back so far."
        "Side with Shunsuke":
            "Shunsuke is right. While they may have a tight deadline to finish the 6 episodes of [anime.name], rushing things might not be the best."
            "Yukari decides it’s best to work with a firm foundation instead of a shaky one. The character designs need to be re-done to match the scenario, or else the project’s value will ultimately be lowered."

    $rand_choice = renpy.random.choice(first_w_events)
    $first_w_events.remove(rand_choice)
    call expression rand_choice from _call_expression
label week_2_2:
    scene studio with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show sumiko laugh_eyes_closed at pos_middleright_half
    show shunsuke at Position(xalign = 1.05,yalign = 1.0)
    with dissolve
    s "Now that we’ve straightened out the scenario and character designs for [anime.name], why don’t we try to do some pre-release marketing?"
    y "Pre-release marketing?"
    show sumiko happy
    s "You know, like how the other anime series always start marketing early to build up pre-release hype? Then we’ll have people shouting “We want [anime.name], we want [anime.name]!"
    show shunsuke sigh
    ss "Don’t forget, we don’t have a budget like those companies have."
    ss "We’re lucky enough to have the investments funds Yukari worked hard to get! We can’t squander that money until we have enough of a cash-flow to survive."
    show mayumi laugh_eyes_closed
    m "Right. We’re working for free, remember?"
    show shunsuke
    show sumiko tsundere
    s "That’s not something easy to forget."
    show mayumi happy
    m "Do you think you can do pre-release marketing without spending money? It’d be pretty neat if we could!"
    show sumiko
    s "Marketing without money? How?"
    ss "Hmm… What about social networks?"
    m "Do we have those?"
    ss "Not yet, but I can create pages for [anime.name] and start some guerilla marketing."
    show mayumi worry
    m "Guerilla marketing?"
    show shunsuke happy
    ss "Low-cost, unconventional marketing, like a viral campaign. It will take time and ingenuity, but not cost us money."
    ss "I’m not sure if it'll work, but it's worth a try."
    show sumiko laugh_eyes_closed
    s "Seems interesting. Let’s let Shunsuke try his guerilla whatever-it-is!"
    show mayumi worry
    m "We already have a lot to do already. Pre-release marketing was never in our plans, and we’re up against a deadline. Are you sure it’s okay to take on even more work? What do you think, Yukari?"
    "It’s a tricky decision. Yukari thinks through the argument each of her team members made and weighs the pros and cons of each option. She doesn’t want anything to go wrong with [anime.name]."
    menu:
        "Start pre-release marketing":
            ss "I’ll get right on it."
            "Shunsuke creates a number of pages on social networks for [anime.name]. He’ll post updates about the project to get the attention of the community."
        "Heed Mayumi's advice":
            show yukari worry
            y "Sorry, Shunsuke, but I agree with Mayumi. We’ve already got a lot on our plate, and we don’t want to cause feature creep for [anime.name]."
    $rand_choice = renpy.random.choice(first_w_events)
    $first_w_events.remove(rand_choice)
    call expression rand_choice from _call_expression_1
label week_2_3:
    scene bg street with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    "On Friday afternoon, Yukari meets up with Mayumi to do some research for [anime.name]. The two of them head over to the closest Animate store that they could locate."
    show yukari happy
    y "There! That’s Animate. They have a huge collection of anime merchandise for sale!"
    show mayumi_f worry
    m "Are you sure this is “research,” Yukari?"
    show yukari laugh_eyes_closed
    y " Of course. It’s all for the sake of [anime.name]."
    "Yukari checks out Animate and several other shops. She buys some figurines and goes shopping in the name of research."
    "Soon, her arms are loaded with bags of merchandise."
    show mayumi_f sigh
    m "Um, Yukari? What does this have to do with research?"
    show yukari happy
    y "Research?"
    show mayumi_f angry
    m "We’re here to do research for [anime.name], remember?"
    show yukari laugh_eyes_closed
    y "Oh, right! Oops. Hehe, well, uh… there’s nothing wrong with a little fun, right?"
    y "We can have fun and do research at the same time. It'll be a BLAST!"
    show yukari
    show mayumi_f
    y "Yukari and Mayumi spends some time looking around the store to try and figure out the latest anime trends, so they can appeal to the masses with [anime.name]."
    "As they head home afterwards, it occurs to Yukari that maybe she shouldn’t take money with her the next time she conducts research."

label week_2_4:
    scene bg restaurant
    show yukari at pos_left
    show yuuko at pos_right
    show sumiko at pos_outerright behind yuuko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with fade
    "It's time for the weekly dinner gathering again! Yukari meets up with her friends at the restaurant."
    show shunsuke happy
    ss "Have we gotten any additional investors yet?"
    show yukari worry
    y "No, I haven't been looking around because we don't have much of a product to pitch to them. It was hard enough the first time. We need to focus on creating [anime.name] first."
    show shunsuke sad
    ss "Hmm… right now, I think raising additional funds is more important."
    ss "Running out of money halfway through the project would be a nightmare."
    show sumiko sigh
    s "A “goodbye [anime.name]” sort of nightmare."
    show mayumi worry
    m "And we don’t want to wait too long. It’s so hard to get investors even interested in an idea. We tried so many times before without any luck!"
    show mayumi laugh_eyes_closed
    m "But don’t worry! If we start now and cast our net as wide as possible, we can complete [anime.name] with a comfortable budget."
    show yukari sigh
    "After listening to them, Yukari understands how important it is to get more funding."
    "While they do need a solid product to attract investors with, money won’t come to them on its own. Waiting for something to happen accomplishes nothing."
    y "You’re right. I’m sorry I didn’t realize it before."
    "Unfortunately, that means it’s time for her least favorite part of the job."
    y "Next week, I'll start sending out those dreadful proposals and try to set up meetings with potential investors. Ugh."
    "Writing the proposals is boring and meeting with investors is even worse."
    s "You don’t have to sound so gloomy about it."
    show yukari tsundere
    y "Want to trade places?"
    s "Not a chance. I have enough on my plate as it is."
    m "Oh? Then I’ll have your dessert!"
    play sound "music/stealing_a_plate_from_someone.ogg"
    s "Wait, what? No!"
    m "But you said..."
    "While they argue, Yuuko rolls her eyes and turns to Yukari."
    show yuuko happy
    show yuuko happy
    show shunsuke
    show sumiko
    yuu "Good luck. Remember, even though we can’t go with you, you have our support. We’re here for you."
    ss "We’ll help with any problems that come up."
    "He glances at Sumiko and Mayumi, who continue to argue over Sumiko’s dessert."
    show shunsuke sigh
    ss "...I’m sure they agree."
    "Yukari laughs. As crazy as her friends can be, just having them nearby makes her feel better."
    show yukari happy
    y "Thanks. You guys are the best."
label week_2_5:
    scene black with dissolve
    $week_2_5_choice = ""
    "When the weekend comes, Yukari decides to spend time with her friends to relax before for the tough week ahead."
    "She calls up…"
    menu:
        "Mayumi":
            $week_2_5_choice = "Mayumi"
        "Shunsuke":
            $week_2_5_choice = "Shunsuke"
        "Yuuko and Sumiko":
            $week_2_5_choice = "Yuuko and Sumiko"
    "Yukari spends part of the weekend with [week_2_5_choice]."
    "It’s a lot of fun. Thanks to [week_2_5_choice], she’s able to forget her worries for a while and de-stress. When the weekend ends, she feels confident."
    y "No matter how tough it is, I have to buckle down and get those funds!"
    scene studio with dissolve
    $current_week = 3
    play music "music/dashboard.mp3" fadein 1.0
    $renpy.retain_after_load()
    call screen start_game
    stop music

label week_3_1:
    scene studio
    show yukari at left
    show yuuko at right
    with dissolve
    y "Are you finished with the character designs yet?"
    yuu "Not yet, only the designs for the main cast is complete. I'm still working on the side characters."
    show yuuko worry
    yuu "I can't seem to get them right.. I feel like I'm in a creative block right now.."
    show yukari laugh_eyes_closed
    y "You’ll be fine! You’re a really talented artist to begin with. Did you know I was already a big fan of your art before we met? I loved it for a long time."
    y "Those views and likes on your artwork show the truth!"
    show yuuko sigh
    yuu "That’s only because I got lucky. What about the proposals to pitch to the investors?"
    y " I wrote a few of them on the weekend. Finding suitable investors was already challenging enough."
    show yukari
    y "I’ll be sending them out later today. Let’s hope my mailbox doesn’t remain a ghost town."
    "Her stomach tightens. If none of the investors are interested, it could be disastrous. Still, there’s no sense in worrying about it."
    "Yukari heads back to her desk and starts working, when a piece of anime news catches her eye. A recent anime release by one of the big shot studios appears to be going viral, possibly due to its unique premise."
    y "Maybe I should reach out to some of the staff there to get some guidance on how to run my anime studio. Right now I feel like a headless chicken trying to cross the road…"
    menu:
        "Contact the studio for advice":
            "The staff members are surprised to hear from Yukari, but not displeased. They give her some tips that'll be essential in the future."
        "Why bother?":
            "Nobody replies to Yukari’s email. Well, it can't be helped. They probably receive way too much spam and fan mail as it is, too much for them to bother responding."
    $rand_choice = renpy.random.choice(first_w_events)
    $first_w_events.remove(rand_choice)
    call expression rand_choice from _call_expression_2
label week_3_2:
    scene studio with fade
    show yukari sad_angry at left
    with dissolve
    y "Agh! This is taking forever. I wish I could write a generic email and send it to all the investors, instead of writing personalized ones."
    y "But everyone says generic emails are often ignored while personalized emails have a better chance of catching their interest."
    y "That greater chance is what we need right now, so I shouldn’t complain, I guess."
    y "It’s so boring, though. I’ll try calling some of them up instead."
    play sound "music/dialing_numbers.ogg"
    "She picks up her cell phone and dials the number for one of the potential investors."

    "It rings, and then.."
    scene black with dissolve
    bot "Thank you for calling ABC company."
    bot "Our office hours are from 9AM to 5 PM on weekdays and from 9 AM to 3 PM on Saturday. Our offices are closed on Sunday. For general inquiries, please press 1. For support issues, please press 2."
    y "Stupid automated software..."
    "The recorded voice lists several other options, none of which are any help to Yukari."
    bot "To speak with a customer service representative, please press 0 or remain on the line."
    "She glares at the phone and hits 0."
    play sound "music/dial_tone.ogg"
    "It rings again, and then the bot’s voice returns."
    bot "Please hold, as all our customer service operators are currently unavailable."
    play sound "music/annoying_ringtone.ogg"
    "High-pitched, somber chords fill the line."
    y "Great, now I have to listen to some weird music."
    "The music continues until Yukari worries she might fall asleep, and then the line finally comes to life with a human voice."
    stop sound fadeout 0.5
    unknown "Hello, thank you for calling. How may I help you?"
    "Yukari gives the operator a simple pitch, describing the basics of [anime.name] in the hopes she’ll transfer the call to someone higher up."
    unknown "[anime.name] sounds fantastic! How can we get in touch with you?"
    "Yukari quickly gives the operator her contact details."
    unknown "Is there anything else I can help you with?"
    y "No, thank you."
    unknown "All right, have a wonderful day. We’ll get back to you soon!"
    scene studio
    show yukari sigh at left
    with dissolve
    play sound "music/hanging_up_phone.ogg"
    y "Yukari hangs up the phone and sighs. They’ll get back to her. Sure. More likely, she failed her pitch once again and will never hear from them."
    y "Why can’t they just tell me they’re not interested instead of leaving me hanging?"
    "Yukari rubs her head. The pressure and stress is starting to get to her. She looks around the studio. Everyone else is hard at work."
    "As much as she wants to complain to them about what happens, she knows it’s better if she doesn’t distract them."

label week_3_3:
    scene studio with fade
    show yukari worry at left
    with dissolve
    "The next day, Yukari can’t help but worry about Sumiko. She doesn’t look well. She keeps coughing and works on her art half-slumped in her chair. When she looks up, her eyes are dull."
    "Yukari looks around."
    "Mayumi is intent on sorting the huge mountain of project files for [anime.name]. Shunsuke is also working with her on the script. Yuuko sits at her desk working on art."
    "Perhaps they didn’t notice yet… or it could just be Yukari’s imagination."
    menu:
        "It's just my imagination...":
            show yukari tsundere
            y "I must be imagining things. All this stress is getting to me."
        "Ask Sumiko if she's sick.":
            show yukari sad
            show sumiko at right with dissolve
            y "Sumiko, are you getting sick? You look like you should see a doctor."
            show sumiko sigh
            s " I’m fine! What makes you think I’m sick?"
            s "*cough cough*"
            show yukari angry
            y "Your body is honest, at least. We can’t have you falling sick right now when we have so much work to do. I’ll take you to the doctor!"
            show sumiko worry
            s "But what about my work?"
            y "Losing some progress now is better than coming down with a serious illness that could jeopardize the whole project!"
            s "Yes, ma’am..."
            "Yukari takes Sumiko to see a doctor. She is indeed sick. She’ll be recuperating at home for the rest of the week and won’t be able to work on [anime.name] for the next few days."
    $rand_choice = renpy.random.choice(first_w_events)
    $first_w_events.remove(rand_choice)
    call expression rand_choice from _call_expression_3

label week_3_4:
    scene studio with fade
    show yukari sad at left
    show shunsuke at right
    with dissolve
    ss "Here’s the script for the pilot episode. We can get started with the episode’s storyboard soon, too."
    ss "Let me know what you think!"
    "It takes Yukari a moment to realize he’s speaking to her."
    y "What? Oh, right, the script for episode 1.  I’ll take a look at it later."
    y "Who’s working on the storyboard? Me?"
    ss "If not you, who else? You’re the one in charge, so you have the clearest picture of what [anime.name] should be like."
    y "Yes, you’re right. Why did I even ask that question?"
    y "Yukari rubs her head. She feels like she’s going to explode any minute now. Should she tell the others her concerns about funding?"
    menu:
        "Raise the issue of funding":
            show yukari sad at pos_left
            show mayumi at pos_farleft behind yukari
            show shunsuke at pos_middleright
            show yuuko at pos_right
            show sumiko at pos_outerright behind yuuko
            with dissolve
            y "Hey, can I talk to everyone for a minute?"
            show mayumi worry
            m "What’s wrong?"
            y "I’m worried about the funding. I haven’t found any more investors. No one seems interested."
            ss "That’s not good."
            y "I know! What are we going to do?"
            show mayumi happy
            m "Maybe we could have a bake sale!"
            show shunsuke worry
            ss "A bake sale? How will we find time for baking?"
            show mayumi sad
            m "Oh, right…"
            show yuuko happy
            yuu "If we find people in the community who are interested, they might help fund us."
            show mayumi happy
            show shunsuke
            m "Yes! They won’t be able to give as much as investors, but if we get enough people interested, it could really help."
            ss "That will also take time, though."
            show yuuko
            show mayumi
            show yukari worry
            y "Still, it’s a possibility. Thanks, guys."
            "Even though they didn’t come to an answer, Yukari feels better just from talking about it. Between the four of them, maybe they can find a solution."
        "I'm fine.":
            "Yukari closes her eyes. She can handle this. No need to worry the others."
    show yukari sad at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright
    show yuuko worry at pos_right
    show sumiko at pos_outerright behind yuuko
    with dissolve
    yuu "Hey, everyone? Sumiko still needs more rest. She won’t be able to meet with us tonight for dinner."
    show shunsuke sad
    show mayumi sad
    m "Aw, that’s too bad."
    ss "She must really be sick."
    yuu "Yes. It was… difficult to get her to realize it, but I think I made her understand she needs time to recover."
    
label week_3_5:
    scene bg restaurant with fade
    show yukari worry at pos_left
    show shunsuke at pos_middleright_half
    show yuuko at Position(xalign = 1.0,yalign = 1.0)
    show mayumi at pos_farleft behind yukari
    with dissolve
    "For the first time, Yukari feels stressed, not happy, when she goes to the restaurant with her friends."
    show mayumi sad_angry
    m "Looks like we’re in a pretty tough spot now that Sumiko is ill."
    m "Yuuko, can you cover for your sister until she’s back, so we don’t fall too far behind?"
    m "If we don’t meet the deadline the investors set for [anime.name], it’s all over."
    show yuuko sad
    yuu "I’ll work twice as hard to cover for her! I feel bad for her. Sumiko was so excited for [anime.name]."
    yuu "She’d talk to me about her ideas all the time, even when we were back at home. I hope she listened to my advice about resting and isn’t secretly doing work now…"
    show yukari sad
    y "Sumiko’s art is only one of the issues we have to worry about. We still don’t have enough funding to finish [anime.name], and according to Mayumi, we’re currently behind schedule."
    y "I wonder if we’ll get everything sorted out..."
    "Right now, it doesn’t seem likely. A cold pit has formed in her stomach. Even the tempura no longer tastes good."
    ss "We’ll try our best. Don’t be too pessimistic."
    y "What if “our best” isn’t good enough?"
    show shunsuke worry
    ss "Are you feeling overworked? If you’re stressed, you can always talk to us. I could take on some more of the workload, and I’m sure Mayumi could, too."
    show mayumi
    show yuuko
    m "Of course! Just tell us what you need!"
    show yukari
    y "I’m fine."
    ss "I’m kind of worried about you. The past few days, you’ve seemed very busy and frustrated."
    y "Don’t worry about me. I can cope with my workload, and I’m not too stressed out. After all, it’s my role to take care of all these responsibilities."
    "She looks down at her food to avoid Shunsuke's gaze. He might realize she’s lying."
    "As she eats, though, she wonders if he’s right. Maybe she does need to talk to someone about her worries."
    "After everyone finishes dinner, Yukari glances at Mayumi."
    menu:
        "Confide in Mayumi":
            hide mayumi
            hide shunsuke
            hide yuuko
            show yukari at left
            show mayumi_f at right
            with dissolve
            "When dinner ends, everyone says their farewells and begins to leave. Yukari catches Mayumi’s arm before she can go out the door."
            y "Mind if we talk for a minute?"
            m "Not at all. What’s up?"
            "Yukari waits a moment to make sure the others get far enough away so they won’t overhear or double back for something."
            y "I’m really starting to worry about this. I’m not sure we can complete [anime.name]."
            m "Of course we can! Just because we’ve had a few setbacks doesn’t mean there’s no hope."
            y "But the deadline is approaching and we’re falling behind. This is my dream. It’s hard to watch my dream crumble to dust…"
            m "It’s not crumbling. Everything will be fine. You’ll see!"
            y "I hope you’re right."
            m "Have a little faith in my predictions! Have I ever been wrong?"
            y "Haha, okay. Thanks, Mayumi. Talking to you always makes me feel better."
        "I'm fine...":
            "Yukari shakes her head. She’s the director. She can handle this herself."

label week_3_6:
    scene black with dissolve
    "At last, the weekend arrives. Yukari debates about how she should spend it."
    menu:
        "Work on [anime.name]":
            "Yukari spends the weekend working on the storyboards for [anime.name]."
        "Ask her old friends out for a meal":
            "Yukari asks her old friends out for a meal to catch up and also to get their opinions on [anime.name]."
            #Depending on Yukari’s human relations variable, they either tell her they like <anime name> very much or they tell her they are not very fond of <anime name> 
        "Watch some anime.":
            "Yukari spends the weekend binge-watching her favorite anime series to relax."
    "End of demo.. for now"




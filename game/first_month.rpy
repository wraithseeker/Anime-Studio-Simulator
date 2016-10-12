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
define grandma = Character('Grandma', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define investor = Character('Investor', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define sisters = Character('Yuuko & Sumiko', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define staff = Character('Staff', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define anim_dir = Character("[anim_studio_dir]", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define va_dir = Character("[va_director]", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define everyone = Character("Everyone", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define va_a_char = Character("[va_a]", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define va_b_char = Character("[va_b]", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define va_c_char = Character("[va_c]", color="#000",ctc="ctc_fixed",ctc_position="fixed")


# The game starts here.

label game_start:
    stop music fadeout 1.0
    # $first_w_events = ["random_33"]#["rande_1","rande_2","rande_3","rande_4","rande_5","rande_6","rande_7"]
    # #call screen progress_report
    # "Welcome to the demo version of Anime Studio Simulator. For our music, we have a few pieces composed for our OST while the rest of them are royalty free placeholders. Some scenes do not have an OST yet."
    # "The demo version covers the events of the game up till week 3 with a total of 12 weeks planned for the game's release."
    # "We hope you enjoy playing the demo version of Anime Studio Simulator!"

label week_0_1:
    scene home with fade
    show yukari worry at left with dissolve
    "It’s the day after high school graduation. Yukari settles down to watch her favorite anime, but she can’t concentrate."
    "Her acceptance letter from the university she applied to sits on her desk. In a few months, she’ll be back in school. Usually, she spends vacation relaxing or working a part-time job. That’s what most of her classmates are doing."
    show yukari
    "But something about it doesn’t feel right. She doesn’t want to be like everyone else. She wants to do something special. Fulfill her secret dream. Maybe this vacation is the best time to do it."
    "Her mind made up, Yukari grabs her cell phone and sends a quick message to her best friend."
    #scene cafe
    scene cafe with fade
    show yukari happy at left
    show mayumi_f at right
    with dissolve
    #play music "music/ost/working_as_intended.ogg"
    "When Yukari arrives at the café, it only takes her a minute to spot Mayumi."
    "She sits alone with headphones on, smiling as she enjoys whatever music she’s currently listening to. Yukari sits down across from her, and Mayumi’s eyes open. A second later, she removes her headphones."
    show mayumi_f happy
    m "Hi! So what did you want to talk about?"
    show yukari laugh_eyes_closed
    y "Got any plans for vacation?"
    "The other girl glances down at the table."
    m "Oh, not really… I’ll visit my grandparents once or twice, but nothing special… The coffee here is great, by the way. You should order some!"
    "Yukari has known Mayumi her entire life. They’ve been friends since before they could walk. And when the normally-upbeat girl hedges and glosses over the subject, she’s hiding something."
    y "Come on, what’s the secret? Is it a boy?"
    show mayumi_f tsundere
    m "What? No!"
    y "Then what? You know I’ll find out eventually."
    show mayumi_f
    m "Well, I… I might try to compose some of my own music. I’ve been playing around with Vocaloid, and now that we’re on vacation, I want to try a song or two."
    y "That’s great! Why are you embarrassed?"
    show mayumi_f sigh
    m "People make faces when I say things like that and ask if I really think a teenage girl can compose anything worthwhile. You know how it is."
    show yukari
    "She does. Reactions like that are the main reason Yukari rarely shares her dream with anyone. She takes a deep breath."
    y "Speaking of which, do you remember what I told you I want to do more than anything in the world?"
    show mayumi_f
    m "You mean direct an anime?"
    y "Yeah. I… I want to try over vacation."
    show mayumi_f laugh_eyes_closed
    m "Really? That’s great!"
    "She lets out a sigh of relief. Her best friend never called her crazy before, but the fear lurked in the back of her mind that she might this time. Mayumi’s enthusiasm calms her worries, and she speaks up with more confidence."
    y "It won’t be anything big, just two episodes of my very own anime."
    m "Even a short anime is a step in the right direction. Can I help! You’ll need someone to handle the music and sound, right?"
    show yukari worry
    y "I don’t want to interfere with your plans…"
    show mayumi_f sigh
    m "Don’t be silly. I love anime, and this gives me a perfect project to compose music for."
    show yukari happy
    y "Great! Then as my new sound director, welcome to the team!"
    show mayumi_f
    m "Who else is on the team?"
    y "…Me."
    m "For a moment, they stare at each other in silence. Then Mayumi bursts into giggles."
    show mayumi_f laugh_eyes_closed
    m "Yukari, you have a lot of work to do…"
    scene home with fade
    show yukari at left with dissolve
    stop music fadeout 1.0
    "That night, Yukari goes online and browses art on Pixiv. Some of the artists are fantastic. She wishes she could draw that well, but she never had much talent there."
    y "I’ve just got to work up the nerve to contact some of these artists and ask if they’d be interested in working on an anime."
    "Will she sound professional enough? Will the artists take her seriously? Despite her worries, Yukari braces herself and contacts the artists whose work she likes the most."
    "Once she sends the messages, she feels as though a weight has been lifted from her shoulders."
    "It’s done, for better or worse. All she has to do is wait to see if anyone responds."
    "And suddenly, she’s confident someone will. It doesn’t have to be an idle daydream any longer. This summer, she’ll make her dream a reality."
    scene black with fade
    $fastForwardDays(2)
    "A few days later, Yukari once again goes to the café to meet with Mayumi. This time her friend is attentive and alert, no doubt due to excitement for their anime project."
    scene cafe with fade
    show yukari at left
    show mayumi_f worry at right
    with dissolve
    #play music "music/ost/working_as_intended.ogg" fadein 1.0
    m "Yukari! Are you all right? When you asked to meet with me, you sounded ready to pass out."
    "Then again, it could be concern rather than excitement."
    y "I’m just a little nervous. I think I found a character artist."
    show mayumi_f laugh_eyes_closed
    m "Really? That’s great!"
    y "Yukari smiles and tries to calm her nerves."
    y "Her name is Yuuko. We spoke online, and she seems interested. I’m supposed to meet with her in person tonight."
    m "Good luck! If you need anything, just give me a call."
    y "Thanks. I really hope she joins the team. Her art is fantastic. Here."
    show yukari happy
    "She pulls out her phone and browses to the Pixiv page where she discovered Yuuko’s art."
    y "Isn’t it great?"
    show mayumi_f surprised
    m "It is! Wait a minute… You said her name is Yuuko? And this is her art?"
    y "Yes, why?"
    m "She went to our school!"
    show yukari surprised
    y "What, really?"
    show mayumi_f
    m "Yes. I thought you knew her, actually."
    show yukari
    y "No, I don’t think so… but that makes me feel better, all the same."
    "The artist will still be a stranger to her, but at least they have some common ground. It gives her a better feeling for Yuuko’s age, too."
    "Meeting someone around her own age is a lot less stressful than meeting someone who could have been a professional artist for years."
    y "I better get going. I just wanted to let you know first."
    m "Good luck!"
    y "Thanks!"
    "Yukari takes a deep breath, checks her phone to see where Yuuko asked to meet, and leaves the café."
    scene street with fade
    show yukari at left with dissolve
    y "Okay, which way is it…?"
    "The artist asked to meet at a restaurant. Yukari’s never been there before, but she knows the city well enough to find it."
    "She starts down the street at a quick pace. The last thing she wants to do is arrive late and make a bad first impression."
    show shunsuke at right with dissolve
    unknown "Excuse me—"
    show yukari tsundere
    y "Sorry, no time!"
    #surprised_face
    "She steps past the boy who called out to her, thoughts fixed on her destination. If he’s lost or needs help with something, there are plenty of people around he can ask."
    show shunsuke sad
    unknown "Wait—"
    "Yukari leaves the stranger behind without another glance and hurries toward the restaurant. This is important."

label week_0_2:
    scene restaurant with fade
    show yukari at left with dissolve
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
    show yukari surprised
    y "You want to join the team?"
    s "Well, Yuuko said you need a background artist."
    show yukari laugh_eyes_closed
    y "You’re an artist too? That’s great! Let’s sit down so we can discuss it."
    "They sit down, and Yukari explains what she has in mind."
    "A short anime with only two episodes, something that can be handled by a small team. She already told Yuuko about it online, but she repeats it again for Sumiko’s benefit."
    "Sumiko is an eager participant in the conversation. She has questions, comments, and input of her own. In contrast, her sister says next to nothing, although she occasionally nods and smiles. Nevertheless, both agree to join the team."
    "Yukari gives them Mayumi’s email address so they can get in touch with her. She can hardly keep from giggling in glee."
    "She went to recruit a character artist and gained a background artist for her efforts. Everything is coming together perfectly."
    $nextDay()
    scene cafe with fade
    show yukari at pos_left
    show mayumi happy at pos_farleft behind yukari
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    with dissolve
    m "Hi, I’m Mayumi!"
    s "I’m Sumiko, and this is Yuuko. Don’t we know each other from school?"
    show mayumi laugh_eyes_closed
    m "I knew it!"
    show sumiko happy
    s "You’re handling the anime’s audio, right? I can’t wait to hear the music you come up with!"
    m "And I can’t wait to see your art!"
    "Pride surges through Yukari as she listens to them. It’s great to see the team members already hit it off so well. Or at least, as far as Mayumi and Sumiko are concerned. Yuuko hasn’t said a word, which is troubling."
    y "What about you, Yuuko?"
    "The other girl gives her a startled look, as if she didn’t expect to be addressed directly and isn’t entirely sure how to handle it."
    y "Are you excited about the project?"
    "She nods."
    show yukari happy
    y "Well… great!"
    "Beside them, Sumiko and Mayumi continue to chat happily. It’s a start. The rest can come with time. And if Yuuko doesn’t like to talk, that’s fine. What matters is that she’s a great artist on board with their project."
    "Piece by piece, their team will come together."

label week_0_3:
    $fastForwardDays(3)
    scene street with fade
    show yukari at left with dissolve
    "Three days have passed since Yuuko and Sumiko joined the group. Yukari walks down the street, deep in thought. She almost has an entire team together. All she needs is a writer."
    "Although she has her own ideas for the basic direction the anime should take, she isn’t good at fleshing out her ideas into full scripts."
    "But she’s optimistic. Everything’s gone so well so far, she’s sure she’ll find an excellent writer. Then they’ll be ready. She’ll direct her own anime. It doesn’t seem real."
    show shunsuke at right with dissolve
    unknown "Excuse me."
    "Soon, her dream will come true…"
    "Not only her dream, but her grandmother’s too. Yukari smiles as she imagines how happy her grandmother will be when she hears the news."
    unknown "You’re Yukari, aren’t you?"
    "Lost in her thoughts, it takes Yukari a moment to realize someone is talking to her. She blinks at him. It’s the same boy who tried to get her attention the other day. Now that she’s not in such a hurry, she has time to give him a closer look."
    "He’s familiar. It takes a moment, but then she recognizes him. He went to her school, although they never spoke."
    y "You’re… Shunsuke, right?"
    ss "Yes. I heard a rumor you’re making your own anime."
    "Now he has her full attention."
    y "That’s right! Why?"
    show shunsuke laugh_eyes_closed
    ss "I’ve mainly written fan fiction, but I’d love to work on an original anime story. Do you need a writer?"
    show yukari happy
    y "Absolutely! We're still searching for a writer for our anime."
    ss "Could you tell me more about your ideas?"
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
    y " Everyone, I have great news!"
    "It’s the first time she’s assembled everyone, although they don’t seem like a cohesive team yet. Yuuko remains quiet and Shunsuke hasn’t quite integrated himself into the group. In contrast, Mayumi and Sumiko talk every time they’re together."
    "Everyone looks up at Yukari’s announcement."
    ss "You look excited. Is this about our funding?"
    "Funding was the one sticking point that prevented them from starting immediately. Without money, they couldn’t rent a studio or get the equipment they’d need to make a proper anime."
    show yukari happy
    y "That's right! Thanks to an investor, I’ve secured funds for our project. I also rented a studio for us to work in."
    show sumiko worry
    s  "That’s awesome! Although I'm curious as to how you convinced an investor to fund us, since we don’t have any concrete work to show yet."
    show yukari worry
    y "It’s … complicated. Let’s just say this investor has a personal interest in our anime."
    show sumiko sigh
    s "Oh man, please tell me you haven’t indebted us to a crime lord or something."
    show yukari tsundere
    y "What?! Of course not!"
    show sumiko laugh_eyes_closed
    s "Just checking."
    show sumiko
    show yukari
    m "Will it be enough money for the entire anime?"
    y "No. This is just enough to get us started."
    ss " I see. So we’ll need to raise additional funds later on."
    yuu "We’re going to outsource the animation work, aren’t we? That will be very expensive."
    "It’s so rare to hear Yuuko speak, Yukari stares at her in astonishment. If she’s concerned enough to voice her worries out loud, it’d definitely something to keep in mind."
    "But they have their initial funding, and that’s what matters."
    show yukari laugh_eyes_closed
    y "We can figure that out later. For now, we should be happy."
    y "We'll start work next week. Our journey will be long and tough, but I believe we can pull through it together!"
    show mayumi happy
    m "Yeah! The rest can wait. Let’s celebrate!"
    "Everyone is in high spirits now that they have an investor, and they celebrate the good news until late in the evening."
    stop music fadeout 1.0
    scene home with fade
    show yukari happy at left with dissolve
    y "I can’t believe it… It’s finally happening. Next week, I’ll start work on my own anime. I’ll fulfill my dream. No… our dream."
    scene flashback with fade
    grandma "Yukari? It’s been so long! Did you travel all the way out here just to visit me?"
    y "Grandma! I was going to call you, but I changed my mind. I want to tell you this news in person."
    grandma "You’re getting married?"
    y "What?! No, that’s not it. Do you remember the secret I told you when I was a little girl?"
    grandma "You’re going to make your own anime?"
    y "Yes!"
    grandma "I’m so happy for you."
    y "A few friends are helping me. There aren’t many of us, but I’m sure we can do it."
    grandma "Have you started? How long will it take? I can’t wait to watch your show."
    y "We’ve discussed ideas, but we can’t start production until we have funding. It’s tough, since all we have is a concept, but I’m hoping to find investors soon."
    grandma "You just found one."
    y "Huh? What do you—"
    y "You mean yourself? I can’t take your money!"
    grandma "I have more money than I’ll ever need at my age."
    y "Aw, don’t say that…"
    grandma "Besides, this isn’t a gift. It’s an investment, and I expect something to come of it! Make me proud, Yukari!"
    y "I will!"
    scene home
    show yukari at left
    with fade
    y "Don’t worry, Grandma, I won’t let you down."
    jump pre_game

label pre_game:
    $nextDay()
    scene bg studio with dissolve
    menu:
        "What difficulty level would you like to choose?"
        "Casual":
            $game_casual = True
        "Normal":
            $game_casual = False
    if game_casual:
        "You have chosen casual mode."
    else:
        "You have chosen the default mode."
    "Let's go through the basics of the game."
    "This is Yukari’s new studio, where her team will work hard to produce their anime series within three months."
    show screen start_game
    $side_nav_interaction = False
    $show_floating_buttons = False
    "You'll oversee the production of [anime.name]. The deadline for [anime.name] is during {font=fonts/LiberationSans-Bold.ttf}Week 12{/font}."
    "The most important thing for you to do is choose daily {font=fonts/LiberationSans-Bold.ttf}Tasks{/font} for the team members to perform." 
    show image "ui/done_idle.png" at Position(xalign=0.96,yalign=0.929)
    "After you have assigned tasks to everyone, you can end your turn by selecting {font=fonts/LiberationSans-Bold.ttf}Done{/font}."
    hide image "ui/done_idle.png"
    "You can also see an overview of your actions each week under {font=fonts/LiberationSans-Bold.ttf}Progress{/font}, which should help you decide what to focus on."
    "You'll eventually have to {font=fonts/LiberationSans-Bold.ttf}Outsource{/font} work and it is a good idea to occasionally {font=fonts/LiberationSans-Bold.ttf}Upgrade{/font} your team members by sending them for training."
    "Good luck!"
    $side_nav_interaction = True
    $show_floating_buttons = True
    hide screen start_game
    play music "music/ost/scheduled_days.ogg" fadein 1.0
    $renpy.retain_after_load()
    call screen start_game
    stop music

label week_1_1:
    $initial_week = False
    $fastForwardDays(2)
    scene bg studio
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright
    show sumiko at pos_outerright behind yuuko
    show yuuko at pos_right
    with dissolve
    "On Monday, Yukari gathers everyone together at the studio. It’s time to discuss and finalize the details about their anime."
    show mayumi worry at pos_farleft
    m "So… what type of anime are we making, again?"
    show sumiko sigh
    s "We’ve been talking about it for weeks, and you still don’t know?"
    show mayumi tsundere
    m "I was listening to music!"
    ss "Every time it came up?"
    m "I have a lot of music."
    y "Don’t worry about it. To clarify for Mayumi’s sake, it’s…"
    show sumiko
    menu:
        "Harem Anime":
            $anime.category = Anime.HAREM
            $va_a = "Bradley" #male
            $va_b = "Sakura"
            $va_c = getRandomFemaleName()
        "Mystery Anime":
            $anime.category = Anime.MYSTERY
            $va_a = getRandomMaleName()
            $va_b = getRandomFemaleName()
            $va_c = getRandomMaleName()
        "Action Anime":
            $anime.category = Anime.ACTION
            $va_a = getRandomMaleName()
            $va_b = getRandomFemaleName()
            $va_c = getRandomMaleName()
    show mayumi happy
    show sumiko
    m "Okay! I can’t wait! Is the name for our anime finalized, too?"
    y "It's …"
    $anime.name = renpy.input("Name of your anime?",default="",length=20)
    if anime.name == "":
        $anime.name = "Macross Delta"
    show mayumi happy
    m "[anime.name] sounds great!"
    y "Now that we have our studio, let's assign desks."
    y "Yuuko and Sumiko should sit next to each other."
    show sumiko happy
    s "Because we’re sisters, right?"
    y "Well, I was thinking because you’re both working on the art."
    s "Good point."
    ss "Hmm, so we have a character artist and a background artist… but we’re going to outsource the animation work, correct?"
    show yukari worry
    y "Yeah, if we try to handle the animation ourselves…"
    show mayumi laugh_eyes_closed
    m "I bet it would turn out wonderful!"
    show sumiko angry_mouth_closed
    s "Is there anything you don’t think is wonderful?"
    m "Yes."
    s "Such as?"
    m "I don’t like thunderstorms. Well… even storms can be pretty sometimes…"
    show sumiko sigh
    s "I rest my case."
    show mayumi
    m "Anyway, where should I sit?"
    ss "Does it really matter? All the desks are the same…"
    "Yukari takes the centermost desk, where she can easily look around to see what everyone is doing. Mayumi and Shunsuke sit at the remaining two."
    y "All right, if anyone has a problem with this arrangement, let me know."
    "As for Mayumi, since you won’t have much to do in the planning phase, you can help me with some paperwork for now."
    show yukari
    show mayumi
    m "Okay!"
    m "Shunsuke, how far along is the scenario for [anime.name]?"
    show shunsuke happy
    ss "I finished writing it a few weeks ago, actually. Last weekend, I completed the edits, so I’m pretty happy with it."
    show yukari happy
    y "Sweet! Let me have a look."
    "Shunsuke hands over his copy of the scenario."
    if anime.category == Anime.HAREM:
        "It tells the story of a boy named Keiji who is the only male member of his high school’s science club."
        "Love triangles and science hijinks lead to wacky antics as he tries to sort out his feelings while also trying to keep their mad scientist tendencies from getting out of hand."
    elif anime.category == Anime.MYSTERY:
        "It tells the story of a Hideaki, young detective struggling to make ends meet after a disastrous case cast a shadow over his career."
        "When he learns about a murder so bizarre and twisted no other detective wants to touch it, he takes the case in the hopes it will restore his reputation."
    elif anime.category == Anime.ACTION:
        "It tells the story of Itaru, a young man who accidentally stumbles upon an age-old conspiracy hidden deep within the city."
        "He soon finds himself in a race against time to escape his newfound enemies before they silence him permanently."
    show yukari laugh_eyes_closed
    y "Perfect! It’s exactly the way I envisioned it. What do the rest of you think?"
    "Yukari passes the draft to Sumiko. Yuuko reads over her shoulder, and Mayumi wheels her chair forward to join them."
    show mayumi laugh_eyes_closed
    show yuuko laugh_eyes_closed
    show sumiko laugh_eyes_closed
    m "I love it!"
    s "Looks good to me."
    if anime.category == Anime.ACTION:
        s "I bet I get to design some car chase scenes, right? Please tell me there are car chase scenes."
        ss "I’m sure I can find a place for one."
    yuu "This scenario sounds very nice."
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
    show sumiko sigh
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
            "The two artists start sketching designs for [anime.name]."
            if anime.category == Anime.ACTION:
                "Sumiko appears to already be designing a car chase scene."
            "Yukari delegates tasks to the others, and everyone begins work."
        "Refine scenario":
            "Shunsuke takes another look at the scenario to tighten and polish the story. Yukari delegates tasks to the others, and everyone begins work."

# label start:
#     jump week_1_3
label week_1_2:
    $nextDay()
    scene bg studio with fade
    show yukari sad at pos_farleft
    "Although the others have their tasks set out for them, Yukari realizes there isn’t much she can do at this stage in the process. The same goes for Mayumi."
    "Yukari paces in frustration. She can’t sit around and do nothing."
    "After taking a moment to think of possible things she can do to help, Yukari decides to…"
    menu:
        "Read books about management":
            "Yukari has never been in charge of a team like this before, so she bought a few books on how to be a good leader."
            "She spends the day reading about team management and leadership tecnhiques."
        "Network with people":
            "A small team like theirs can’t function entirely on its own. Yukari visits several forums, both for anime fans and people in the anime industry, to get her name out there and make connections."
            "Knowing people involved or interested in anime could prove invaluable in the future."
        "Supervise Yuuko & Sumiko":
            scene studio_main with fade
            show yukari at left
            show yuuko at pos_outerright behind sumiko
            show sumiko at pos_right
            with dissolve
            "Yukari joins the two artists as they work on their early sketches."
            "Yuuko falters and seems uneasy with her watching over her shoulder, so she moves to see what Sumiko is doing instead."
            s "Oh, Yukari, I’m glad you’re here. What sort of aesthetic are we looking for in the backgrounds?"
            if anime.category == Anime.HAREM:
                y "It probably should be bright and fun, to match the mood of the story."
            elif anime.category == Anime.MYSTERY:
                y "I was actually imagining a sort of noir style, like in old detective stories."
                s "Cool, I can do noir."
            elif anime.category == Anime.ACTION:
                y "Hmm, something exciting and flashy!"
            show sumiko happy
            s "Great, thanks for the advice."

label week_1_3:
    $nextDay()
    scene bg studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    "It’s the third day of work on [anime.name]. Yukari looks around the studio and can’t help but grin. The team is hard at work. [anime.name] will be a reality. This is exactly what she’s always dreamed up."
    m "Hey Yukari, want to get lunch?"
    show yukari worry
    y "What? Now?"
    show mayumi_f sigh
    m "Yeah. I mean, the last two days you barely ate."
    y "Is it really okay for me to leave? I mean, I’m the director!"
    "Shunsuke looks up from his work."
    show mayumi at pos_farleft behind yukari
    show yukari at pos_left
    show shunsuke at pos_textbox_right
    show sumiko at pos_outerright
    hide mayumi_f
    with dissolve
    ss "The rest of us take lunch breaks. Logically, you can too."
    y "But..."
    show sumiko tsundere at pos_outerright 
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
    scene bg studio_main with fade
    show sumiko at pos_middleright_half
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_farright
    with dissolve 
    "When they return, the studio is quiet. The other three are still hard at work."
    show sumiko sigh
    s "See? Nothing burned!"
    m "Aren’t you going to have lunch, too?"
    show sumiko
    s "Yuuko and I brought food from home. As for Shunsuke..."
    "She lowers her voice to a stage whisper."
    show sumiko laugh_eyes_closed
    s "I think maybe he’s a vampire!"
    show shunsuke tsundere
    ss "…Seriously?"
    s "I’ve never seen you eat."
    ss "I assure you, I eat."
    show sumiko
    s "Prove it."
    show shunsuke sigh
    ss "Very well then, I will."
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
    $nextDay()
    scene studio_main with fade
    "The next day, Shunsuke makes good on his promise to prove he actually eats, and brings enough food from home for everyone to share."
    show sumiko at pos_middleright_half
    show yukari at pos_left
    show mayumi happy at pos_farleft behind yukari
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
    show shunsuke sigh
    ss "What did I do to deserve this…?"
    show yukari happy
    y "All right, all right! We can have a party if you want."
    m "Yes!"
    show shunsuke
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
    $nextDay()
    scene black with dissolve
    "It’s Friday."
    "When Yukari first gathered the team to work on [anime.name], she made a promise with them to meet up and have dinner together every Friday."
    "Ever since then, they’ve all made it to this recurring event without fail."
    scene bg restaurant with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
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
    s "We all know you only started eating it because you watched that cooking anime!"
    s "You just want to be like your favorite character Yusa who loves to eat tempura."
    show sumiko
    "Embarrassed, Yukari ducks her head."
    y "Well, that's kind of true, in a sense."
    s "There’s no “kind of” about it."
    show yukari laugh_eyes_closed
    y "Hey! Yusa may have introduced me to tempura, but now I really love it!"
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
    y "What are you talking about? You’re a great artist!"
    yuu "The characters don’t look natural yet. Something about their proportions is off, and their faces are wrong."
    y "They’re fine. I like them, and next week we’ll have everyone take another look."
    yuu "..."
    show yukari worry
    y "I-is that okay with you?"
    yuu "…Okay."
    "Despite her agreement, Yukari gets the feeling Yuuko still isn’t happy with her art. If she’s a perfectionist, that could be a problem, but they’ll deal with that when they get there."

label week_1_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "When the weekend comes, Yukari finds some free time at last. She wonders if she should get more work done on [anime.name] or take it easy for now."
    menu:
        "Have fun":
            "Yukari spends the weekend relaxing with some movies and anime. By the time the weekend ends, she feels refreshed and ready to face another week."
        "Work on [anime.name]":
            "As much as she’d like to take a break, Yukari doesn’t want to risk falling behind on work."
            "Now that she has a clearer idea of [anime.name]'s scenario, she’s able to translate that to the initial storyboard. She’s tired by the end of the weekend, but pleased with her progress."
    scene studio 
    $nextWeek()
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music
    $fastForwardDays(2)
    stop music 

label week_2_1:
    scene studio with fade
    show yukari at left
    with dissolve
    "On Monday, Yukari spends some time going through the scenario for [anime.name]."
    if anime.category == Anime.HAREM:
        "One of the girls’ personalities doesn’t seem as well thought out as the others, so she makes a mental note to discuss that with Shunsuke later."
    "Then she gathers everyone together to look at the character designs."
    if anime.category == Anime.HAREM:
        scene harem_sketch with fade
    elif anime.category == Anime.ACTION:
        scene action_sketch with fade
    elif anime.category == Anime.MYSTERY:
        scene mystery_sketch with fade
    y "I think they’re fine. I don’t see any major flaws. What do the rest of you think?"
    ss "Well…"
    s "Uh-oh. Dramatic pause from Shunsuke. Here comes trouble…"
    "Yukari fidgets silently and braces herself. There’s nothing wrong with constructive criticism, but if he presents his issues with the art poorly, it could cause their team’s first major disagreement."
    ss "Personally speaking, the character designs aren’t really what I had in my mind."
    ss "I'm not saying the design is bad, but the art style doesn't go well with the scenario I wrote for [anime.name]."
    if anime.category == Anime.HAREM:
        ss " I'm not saying it’s bad, but the girls look too… normal. Average. They’re kind of a crazy bunch in the story, you know, especially Kiko."
        yuu "They’re in high school. They can’t look too outlandish."
    elif anime.category == Anime.MYSTERY:
        ss "There’s nothing wrong with the art itself, but Hideaki is supposed to be down on his luck. He looks too slick here. And I can’t imagine his assistant looking so serious."
        yuu "You don’t want serious characters in the murder mystery?!"
    elif anime.category == Anime.ACTION:
        ss "I mean, you made Itaru look like a secret agent. Maybe he can reach that point eventually, but definitely not in the first season."
        yuu "Season? Aren’t you getting ahead of yourself?"
    scene studio with fade
    show yukari at pos_left
    show sumiko at pos_outerright
    show shunsuke sigh at pos_middleright_half
    show yuuko_f at pos_farleft behind yukari
    with dissolve
    ss "We should redo these designs so they display the characters’ traits and fit the story better."
    show yuuko_f sad
    yuu "I know the designs need to be refined, but I can’t completely redo them all."
    yuu "It took me a long time to get the designs right. I had trouble choosing the art style for [anime.name]."
    ss "The one you chose just doesn’t work."
    yuu "Art style and references have never been a problem for me before, but I was usually drawing fan art. I guess I need to improve, fast."
    yuu "But if I have to re-do all the character designs..."
    show yuuko_f angry_mouth_closed
    "Yuuko falls silent."
    s "You’re worried about the deadline, aren’t you?"
    yuu "Yes. I don’t know if I can re-do them in time."
    ss "Yukari should be the one to decide. She’s in charge."
    show yukari worried
    y "Hmm…"
    "Each side has good points, but with a limited budget and limited time, Yukari has to make this decision carefully."
    menu:
        "Side with Yuuko":
            "Yuuko is right. They have a tight deadline to finish [anime.name], and they need to make two episodes."
            "They’ll need to touch up the designs, but Yukari decides re-doing them would cause more harm than good by setting their progress back so far."
        "Side with Shunsuke":
            "Shunsuke is right. While they may have a tight deadline to finish the two episodes of [anime.name], Yukari decides it’s best to work with a firm foundation instead of a shaky one."
            "The character designs need to be re-done to match the scenario, or else the project’s value will ultimately be lowered."

    # $rand_choice = renpy.random.choice(first_w_events)
    # $first_w_events.remove(rand_choice)
    # call expression rand_choice from _call_expression
label week_2_3:
    $fastForwardDays(2)
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show sumiko laugh_eyes_closed at pos_middleright_half
    show shunsuke at Position(xalign = 1.05,yalign = 1.0)
    with dissolve
    play music "music/ost/Working Hard, Or... proof of concept.mp3" fadein 1.0
    s "Now that we’ve straightened out the scenario and character designs for [anime.name], why don’t we try to do some pre-release marketing?"
    y "Pre-release marketing?"
    show sumiko happy
    s "You know, like how the other anime series always start marketing early to build up pre-release hype? Then we’ll have people shouting “We want [anime.name], we want [anime.name]!"
    s "I remember one anime that had this cool Alternate Reality Game with clues all across the Internet, and when players finally found the last clue, it ended on a cliffhanger leading into the show!"
    show shunsuke sigh
    ss "Don’t forget, we don’t have a budget like those companies have."
    ss "We’re lucky enough to have the investments funds Yukari worked hard to get! We can’t squander that money until we have enough of a cash-flow to survive."
    show mayumi laugh_eyes_closed
    m "Right. We’re working for free, remember?"
    show shunsuke
    show sumiko tsundere
    s "That’s not something easy to forget."
    show sumiko
    ss "Could we do any sort of pre-release marketing without spending money?"
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
            $guerilla_marketing = True
            ss "I’ll get right on it."
            "He spends the rest of the day creating pages on social networks for [anime.name]."
            scene studio_main with fade
            show yukari at left
            show shunsuke at right
            with dissolve
            y "How is it going?"
            ss "I just finished one. What do you think?"
            "She looks over his shoulder at the screen. At the top of the page, he’s placed a header image showing the main characters in their current designs, along with the title."
            if anime.category == Anime.HAREM:
                "The first post announces the creation of [anime.name] and welcomes anime fans to the page. After that, he devoted posts to introducing Keiji and each of the girls."
            elif anime.category == Anime.MYSTERY:
                "The only post so far is written from the point of view of Hideaki, explaining his struggle to get new cases."
                "It hints at the case that destroyed his career, but doesn't go into detail. That's good. According to the scenario, viewers won’t learn the truth about that case until partway through the show."
            elif anime.category == Anime.ACTION:
                "There are several cryptic posts, each with only a few lines of text teasing the conspiracy eventually uncovered by Itaru."
                "From the looks of things, Shunsuke was more taken with Sumiko’s ARG idea than he let on."
                ##### MAYBE EDIT, CHECK BACK LATER ***
            "As we work on [anime.name], I’ll post updates here and to the other pages."
            y "Sounds great. Keep up the good work!"
        "Heed Mayumi's advice":
            show yukari worry
            y "Sorry, Shunsuke, but I agree with Mayumi. We’ve already got a lot on our plate, and we don’t want to cause feature creep for [anime.name]."
    # $rand_choice = renpy.random.choice(first_w_events)
    # $first_w_events.remove(rand_choice)
    # call expression rand_choice from _call_expression_1
label week_2_4:
    $nextDay()
    scene bg street with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    "On Friday afternoon, Yukari meets up with Mayumi to do some research for [anime.name]. The two of them head over to the nearest Animate store."
    scene animate with fade
    y "I can’t imagine a better place to learn about the current anime trends than Animate!"
    "Her attention is quickly drawn to a display case full of chibi figurines modeled after the main characters of a popular anime."
    y "Look at these!"
    m "Imagine if [anime.name] got to be big enough to have a toy line. Is that what you’re thinking, Yukari?"
    y "Ooh, this one is poseable!"
    m "Yukari?"
    y "Some of them come with props!"
    m "Are you sure this is “research”?"
    y "Of course. It’s all for the sake of [anime.name]."
    "For the sake of [anime.name], Yukari decides to buy two of the figures. After a moment, she picks up a third."
    y "Let’s check out the manga section."
    "The manga shelves are packed with the latest issues, and she picks up a couple to add to her pile. Then she another display of merchandise catches her eye, and she rushes over to it."
    y "This place is incredible."
    m "Um, Yukari? What does this have to do with research?"
    y "Research?"
    m "We’re here to do research for [anime.name], remember?"
    y "Oh, right! Oops. Hehe, well, uh… there’s nothing wrong with a little fun, right?"
    y "We can have fun and do research at the same time!"
    m "Oh dear… Don’t get too distracted, okay?"
    y " Good point. We need to stop shopping and start studying. What types of shows have the biggest displays? Which get the most merchandise? What are other customers buying?"
    "Several customers are shopping, so they observe their purchases. Then they browse the anime section."
    "Some shows definitely have more space devoted to them. Yukari looks at it all with a critical eye and determines the latest trends."
    if anime.category == Anime.HAREM:
        "It looks like moe girls are all the rage right now, so she makes a mental note to discuss that with Yuuko."
    elif anime.category == Anime.MYSTERY:
        "Mysteries seem to be diverging into two categories: the dark and gritty versus the quirky and lighthearted. [anime.name] has elements of both, which could be good or bad."
    elif anime.category == Anime.ACTION:
        "The current craze is mecha. That could be a problem, since the scenario for [anime.name] doesn’t really have a place for mecha, but maybe they can work something out."
    y "Do you think we have enough information, Mayumi?"
    "No reply comes. She looks around. She’s alone in the aisle."
    y "Mayumi?"
    "Puzzled, she leaves the anime section and finds her friend browsing the collection of anime music. Her arms are already loaded with CDs."
    m "Look! They have the OSTs from all my favorite shows!"
    y " Now who’s getting distracted?"
    m "Oops, ehehe. Well, it’s still research, because the music will inspire me!"
    "Yukari nods. That’s a good point. And while they’re at it, there’s a recent anime she’s been meaning to check out which will surely inspire her. Research!"
    "They end the day with a little bit of information and a lot of merchandise. As they head home, it occurs to Yukari that maybe she shouldn’t take money with her the next time she conducts research."
label week_2_5:
    $nextDay()
    scene restaurant with fade
    show yukari at pos_left
    show yuuko at pos_right
    show sumiko at pos_outerright behind yuuko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
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
    show sumiko
    show mayumi laugh_eyes_closed
    m "But don’t worry! If we start now and cast our net as wide as possible, we can complete [anime.name] with a comfortable budget."
    show yukari sigh
    show shunsuke
    "After listening to them, Yukari understands how important it is to get more funding."
    "While they do need a solid product to attract investors with, money won’t come to them on its own. Waiting for something to happen accomplishes nothing."
    y "You’re right. I’m sorry I didn’t realize it before."
    "Unfortunately, that means it’s time for her least favorite part of the job."
    show yukari
    y "Next week, I'll start sending out those dreadful proposals and try to set up meetings with potential investors. Ugh."
    "Writing the proposals is boring and meeting with investors is even worse."
    s "You don’t have to sound so gloomy about it."
    show yukari tsundere
    y "Want to trade places?"
    s "Not a chance. I have enough on my plate as it is."
    show mayumi happy
    show yukari
    m "Oh? Then I’ll have your dessert!"
    show sumiko sad
    s "Wait, what? No!"
    m "But you said..."
    "While they argue, Yuuko rolls her eyes and turns to Yukari."
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
label week_2_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "When the weekend comes, Yukari decides to spend time with her friends to relax before for the tough week ahead."
    "She calls up…"
    menu:
        "Mayumi":
            $week_2_5_choice = "Mayumi"
            scene home with fade
            show yukari happy at left
            show mayumi_f happy at right
            with dissolve
            "They spend their time watching anime, listening to music, and chatting about old times."
            "The one thing they don’t bring up is [anime.name]. This is a time for relaxation, not work. "
        "Shunsuke":
            $week_2_5_choice = "Shunsuke"
            scene black with dissolve
            "She has her doubts about how good of company he’ll be, and when they meet up, she can tell he has similar doubts about her."
            "After a few awkward moments, he suggests a game of chess and offers to teach her when she admits she’s never played."
        "Yuuko and Sumiko":
            $week_2_5_choice = "Yuuko and Sumiko"
            scene black with dissolve
            "The three of them have lunch at the restaurant, and then Sumiko suggests they go see a movie. They buy tickets for a new comedy that just entered theaters."
            "Not only does it distract Yukari from the week ahead, but Yuuko even laughs out loud, the most emotion she’s ever displayed in front of her."
            "It’s a lot of fun. Thanks to the sisters, Yukari is able to forget her worries for a while and de-stress. When the weekend ends, she feels confident."
    y "No matter how tough it is, I have to buckle down and get those funds!"
    scene studio 
    $nextWeek()
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music
    $fastForwardDays(2)
    stop music 

label week_3_1:
    scene studio_main with fade
    show yukari at left
    show yuuko at right
    with dissolve
    y "Are you finished with the character designs yet?"
    yuu "Not yet, only the designs for the main cast is complete. I'm still working on the side characters."
    if anime.category == Anime.HAREM:
        y "That reminds me, do you think the girls are cute enough?"
        yuu "Yes…"
        y "See, I was researching current anime trends, and moe characters are really popular."
        show yuuko worry
        yuu "We can’t keep redesigning the main cast…"
        y "I know! I just want to make sure [anime.name]’s harem appeals to fans as much as possible."
        ss "Why don’t you talk to Shunsuke about it? He can write cuter dialogue for them."
        show yukari happy
        y "Good idea! So how are the side characters coming along?"

    show yuuko sad
    yuu "I can't seem to get them right.. I feel like I'm in a creative block right now.."
    show yukari laugh_eyes_closed
    y "You’ll be fine! You’re a really talented artist to begin with. Those views and likes on your artwork show the truth!"
    show yuuko sigh
    yuu "That’s only because I got lucky."
    y "Not true. Take it from me! Did you know I was already a big fan of your art before we met? I loved it for a long time."
    "Yuuko slumps and stares down at her hands."
    show yukari worry
    y "What’s wrong? That was a compliment."
    yuu "You liked my art… before we met?"
    show yukari laugh_eyes_closed
    y "Yeah. I couldn’t believe it when Mayumi said you went to our school! I wish I knew sooner."
    show yuuko sad
    yuu "Oh..."
    "For some reason, this seems to depress her further."
    show yukari
    y "Did I say something wrong?"
    show yuuko
    yuu "No, never mind… What about the proposals to pitch to the investors? How are they going?"
    "Her attempt to change the subject is obvious, but Yukari decides to go along with it. If Yuuko doesn’t want to talk about what’s bothering her, that’s her business."
    y "I wrote a few proposals on the weekend. Finding suitable investors was already challenging enough."
    y "I’ll send them out later today. Let’s hope my mailbox doesn’t remain a ghost town."
    "Her stomach tightens. If none of the investors are interested, it could be disastrous. Still, there’s no sense in worrying about it, especially when there’s more work to be done."
    "She leaves Yuuko’s desk and approaches Shunsuke, who is writing furiously. He stops and looks up."
    show yukari at left
    show shunsuke at right
    hide yuuko
    with dissolve
    ss "Yes?"
    y "How’s it going?"
    ss "Good. I’m finishing up the script for the pilot episode. Do you want to read it?"
    y "Not right now. Actually, I wanted to ask you about something."
    ss "What is it?"
    if anime.category == Anime.HAREM:
        y "Can you make sure the girls are really sweet and innocent?"
        ss "Well, they’re supposed to be. A lot of the humor comes from the unintended consequences of their science experiments. They’re very smart, but also somewhat naïve."
        y "And shy?"
        ss "Natsume is, but—"
        y "Maybe they should all be shy."
        ss "No, they need to be distinct. So one is shy, one wears cat ears…"
        show yukari laugh_eyes_closed
        y "I just want to make sure the audience finds them loveable!"
        ss "Don’t worry, Yukari. They will."
    elif anime.category == Anime.MYSTERY:
        y "What tone are we going for with [anime.name]?"
        y "I did some research on the current anime trends, and a lot of people seem to like grim mysteries, with lots of blood, death, and really sick villains."
        y "Other people gravitate toward mysteries that don’t take themselves seriously, with goofy characters and wacky situations."
        y "And [anime.name] does a little of both. I’m afraid the fans of dark mysteries will be put off by the humor, and the fans of lighthearted mysteries will be scared away by the darkness."
        ss "[anime.name] is meant to appeal to both."
        show yukari worry
        y "Are you sure that will work?"
        ss "First, a lot of the humor is morbid. Many people love black comedy and gallows humor. Second, most of the darker elements are implied or occur off-screen."
        ss "If we achieve the balance I hope for, we’ll win both types of fans. Some will enjoy the humor, others will dwell on the dark implications, and everyone will be happy."
    elif anime.category == Anime.ACTION:
        y "Do you think we can add mecha to the scenario?"
        show shunsuke worry
        "His head snaps toward her and he stares as if he’s never seen anything like her before. He stares for a long time. His mouth moves and nothing comes out. When he finally speaks, his tone is bewildered."
        ss "Did you say mecha?"
        show yukari laugh_eyes_closed
        y "Mecha battles are really popular with anime fans right now. People will go crazy if they hear [anime.name] is a new mecha show!"
        ss "Except [anime.name] is not a mecha show. At all. You read the scenario. Where could we possibly add mecha?"
        y "Maybe some of the conspirators are trying to build—"
        show shunsuke sigh
        ss "No."
        show yukari sad
        y "But—"
        ss "We can’t chase every trend, Yukari. Shoehorning in mecha will only hurt [anime.name]. Trust me."
        y "All right, if you say so."
    hide shunsuke with dissolve
    show yukari
    "She isn’t wholly satisfied with his answer, but she can’t micromanage every aspect of the anime."
    "She heads back to her desk and starts working, when a piece of anime news catches her eye. A recent anime release by one of the big shot studios appears to be going viral, possibly due to its unique premise."
    "Maybe I should reach out to some of the staff there to get some guidance on how to run my anime studio. Right now I feel like a headless chicken trying to cross the road…"
    menu:
        "Contact the studio for advice":
            "The staff members is surprised to hear from Yukari, but not displeased. They give her some tips that'll be essential in the future."
            #unsuccessful
            #Nobody replies to Yukari’s email. Well, it can't be helped. They probably receive way too much spam and fan mail as it is, too much for them to bother responding. 
        "Don't contact the studio":
            pass
    # $rand_choice = renpy.random.choice(first_w_events)
    # $first_w_events.remove(rand_choice)
    # call expression rand_choice from _call_expression_2
label week_3_2:
    $nextDay()
    scene studio_main with fade
    show yukari sad_angry at left
    with dissolve
    y "Agh! This is taking forever. I wish I could write a generic email and send it to all the investors, instead of writing personalized ones."
    y "But everyone says generic emails are often ignored while personalized emails have a better chance of catching their interest."
    y "That greater chance is what we need right now, so I shouldn’t complain, I guess."
    show yukari sigh
    y "It’s so boring, though. I’ll try calling some of them up instead."
    play sound "music/sfx/dialing_numbers.ogg"
    "She picks up her cell phone and dials the number for one of the potential investors."
    "It rings, and then.."
    scene black with dissolve
    $random_company = getRandomCompany()
    bot "Thank you for calling [random_company]."
    bot "Our office hours are from 9AM to 5 PM on weekdays and from 9 AM to 3 PM on Saturday. Our offices are closed on Sunday. For general inquiries, please press 1. For support issues, please press 2."
    y "Stupid automated software..."
    "The recorded voice lists several other options, none of which are any help to Yukari."
    bot "To speak with a customer service representative, please press 0 or remain on the line."
    "She glares at the phone and hits 0."
    play sound "music/sfx/dial_tone.ogg"
    "It rings again, and then the bot’s voice returns."
    bot "Please hold, as all our customer service operators are currently unavailable."
    play sound "music/sfx/annoying_ringtone.ogg"
    "High-pitched, somber chords fill the line."
    y "Great, now I have to listen to some weird music."
    "The music continues until Yukari worries she might fall asleep, and then the line finally comes to life with a human voice."
    stop sound fadeout 1.0
    unknown "Hello, thank you for calling. How may I help you?"
    "Yukari gives the operator a simple pitch, describing the basics of [anime.name] in the hopes she’ll transfer the call to someone higher up."
    if anime.category == Anime.HAREM:
        "She includes just enough details about the science themes and comedy to distinguish it from similar shows."
    elif anime.category == Anime.MYSTERY:
        "With any luck, her description will make the operator want to watch the anime to find out who the murderer is."
    elif anime.category == Anime.ACTION:
        "If she goes into too much detail about the conspiracy, it will get complicated, so she focuses on the main character’s struggle and the action scenes."
    unknown "[anime.name] sounds fantastic! How can we get in touch with you?"
    "Yukari quickly gives the operator her contact details."
    unknown "Is there anything else I can help you with?"
    y "No, thank you."
    unknown "All right, have a wonderful day. We’ll get back to you soon!"
    scene studio_main with fade
    show yukari sigh at left
    with dissolve
    play sound "music/sfx/hanging_up_phone.ogg"
    y "Yukari hangs up the phone and sighs. They’ll get back to her. Sure. More likely, she failed her pitch once again and will never hear from them."
    y "Why can’t they just tell me they’re not interested instead of leaving me hanging?"
    "Yukari rubs her head. The pressure and stress is starting to get to her. She looks around the studio. Everyone else is hard at work."
    "As much as she wants to complain to them about what happens, she knows it’s better if she doesn’t distract them."

label week_3_3:
    $nextDay()
    scene studio_main with fade
    show yukari worry at left
    show sumiko sad at right
    with dissolve
    "The next day, Yukari can’t help but worry about Sumiko. She doesn’t look well. She keeps coughing and works on her art half-slumped in her chair."
    "When she looks up, her eyes are dull."
    "Yukari looks around."
    "Mayumi intently sorts through the huge mountain of project files for [anime.name]. Shunsuke is developing the script further."
    "Yuuko sits at her desk working on designs for the side characters."
    "Perhaps they didn’t notice yet… or it could just be Yukari’s imagination."
    menu:
        "It's just my imagination...":
            show yukari sigh
            $week_3_3_doctor = False
            y "I must be imagining things. All this stress is getting to me."
            "However, Sumiko continues to cough throughout the day, and her work on [anime.name] is slow."
            "When she leaves with her sister in the evening, Yukari can’t help but feel another pang of worry and wonder if she should have said something."
        "Ask Sumiko if she's sick.":
            $week_3_3_doctor = True
            show yukari sad
            y "Sumiko, are you getting sick? You look like you should see a doctor."
            show sumiko sigh
            s "I’m fine! What makes you think I’m sick?"
            s "*cough cough*"
            show yukari angry
            y "Your body is honest, at least. We can’t have you falling sick right now when we have so much work to do. I’ll take you to the doctor!"
            show sumiko worry
            s "But what about my work? We only have a few backgrounds complete!"
            y "Losing some progress now is better than coming down with a serious illness that could jeopardize the whole project!"
            s "Yes, ma’am..."
            "Yukari takes Sumiko to see a doctor. She is indeed sick. She’ll be recuperating at home for the rest of the week and won’t be able to work on [anime.name]."
    # $rand_choice = renpy.random.choice(first_w_events)
    # $first_w_events.remove(rand_choice)
    # call expression rand_choice from _call_expression_3

label week_3_4:
    $nextDay()
    $week_3_3_doctor = True
    scene studio_main with fade
    if not week_3_3_doctor:
        show yukari sad at pos_left
        show mayumi at pos_farleft behind yukari
        show shunsuke at pos_middleright_half
        show yuuko at pos_outerright
    else:
        show yukari at left
        show shunsuke at right
    with dissolve
    if not week_3_3_doctor:
        show yuuko sad
        yuu "I’m afraid Sumiko can’t make it today."
        y "What’s wrong?"
        yuu "She didn’t feel well last night, and she woke up really sick this morning."
        show mayumi worry
        m "Oh no!"
        y "Darn it… I thought she seemed sick yesterday. I should have said something! Will she be okay?"
        yuu "She scheduled an appointment with a doctor later today, but she won’t be able to work today… which has her pretty upset."
        show yukari sad
        y "Tell her not to worry about it. It’s more important that she recover."
        ss "And if that doesn’t convince her, tell her she’ll set back [anime.name]’s progress even more if she doesn’t take care of herself."
        show yuuko
        yuu "Thank you."
        "Yukari tries to stifle her own guilt over not saying something to Sumiko. Now she’s sick, her art will be delayed, and [anime.name] is still at risk for a funding crisis."
        "There’s too much to worry about all at once…"
        ss "Yukari, if you have a minute, I’d like to talk to you… "
    scene studio_main
    show yukari at left
    show shunsuke at right
    with dissolve
    ss "Here’s the script for the pilot episode. We can get started with the episode’s storyboard soon, too."
    ss "Let me know what you think!"
    "It takes Yukari a moment to realize he’s speaking to her."
    y "What? Oh, right, the script for Episode 1.  I’ll take a look at it later."
    y "Who’s working on the storyboard? Me?"
    show shunsuke sigh
    ss "If not you, who else? You’re the one in charge, so you have the clearest picture of what [anime.name] should be like. "
    y "Yes, you’re right. Why did I even ask that question?"
    y "Yukari rubs her head. She feels like she’s going to explode any minute now. Should she tell the others her concerns about funding?"
    menu:
        "Raise the issue of funding":
            scene studio_main with fade
            show yukari at pos_left
            show mayumi at pos_farleft behind yukari
            show shunsuke at pos_middleright_half
            show yuuko at pos_outerright
            with dissolve
            y "Hey, can I talk to everyone for a minute?"
            "The others look up from their work."
            m "What’s wrong?"
            y "I’m worried about the funding. I haven’t found any more investors. No one seems interested."
            show shunsuke sad
            ss "That’s not good."
            show yukari sigh
            y "I know! What are we going to do?"
            show mayumi happy
            m "Maybe we could have a bake sale!"
            ss "A bake sale? How will we find time for baking?"
            show mayumi sad
            m "Oh, right…"
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
    scene studio_main with fade
    show yukari sad at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright_half
    show yuuko worry at pos_outerright
    with dissolve
    "A few hours later in the studio..."
    yuu "Hey, everyone? Sumiko still needs more rest. She won’t be able to meet with us tonight for dinner."
    show shunsuke sad
    show mayumi sad
    m "Aw, that’s too bad."
    ss "She must really be sick."
    yuu "Yes. It was… difficult to get her to realize it, but I think I made her understand she needs time to recover."
    
label week_3_5:
    $nextDay()
    scene bg restaurant with fade
    show yukari worry at pos_left
    show shunsuke at pos_middleright_half
    show yuuko at pos_outerright
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
            scene restaurant
            show yukari at left
            show mayumi_f at right
            with dissolve
            "When dinner ends, everyone says their farewells and begins to leave. Yukari catches Mayumi’s arm before she can go out the door."
            y "Mind if we talk for a minute?"
            m "Not at all. What’s up?"
            "Yukari waits a moment to make sure the others get far enough away so they won’t overhear or double back for something."
            show yukari worry
            y "I’m really starting to worry about this. I’m not sure we can complete [anime.name]."
            m "Of course we can! Just because we’ve had a few setbacks doesn’t mean there’s no hope."
            y "But the deadline is approaching and we’re falling behind. This is my dream. It’s hard to watch my dream crumble to dust…"
            m "It’s not crumbling. Everything will be fine. You’ll see!"
            y "I hope you’re right."
            show mayumi_f laugh_eyes_closed
            m "Have a little faith in my predictions! Have I ever been wrong?"
            show yukari happy
            y "Haha, okay. Thanks, Mayumi. Talking to you always makes me feel better."
        "I'm fine...":
            "Yukari shakes her head. She’s the director. She can handle this herself."

label week_3_6:
    $nextDay()
    scene home with fade
    "At last, the weekend arrives. Yukari debates about how she should spend it."
    menu:
        "Work on [anime.name]":
            "Yukari spends the weekend working on the storyboards for [anime.name]."
        "Ask her old friends out for a meal":
            "Yukari asks her old friends out for a meal to catch up and also to get their opinions on [anime.name]."
            scene cafe with fade
            show yukari
            #Depending on Yukari’s human relations variable
            # good
            # "Her friends seem excited and ask her to keep them updated on her progress."
            # "Their conversation leaves her feeling more enthusiastic than ever about [anime.name]."

            # bad
            # "Her friends wish her luck, but admit [anime.name] doesn’t really appeal to them."
            # "She can’t help but feel unhappy, not to mention worried more people might feel the same way…"

        "Watch some anime.":
            "Yukari spends the weekend binge-watching her favorite anime series to relax."
    scene studio 
    $nextWeek()
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music
    $fastForwardDays(2)
    stop music 
label week_4_1:
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    play music "music/ost/Unavoidable Delays rough mix.ogg"
    y "At our current rate, we won't have enough money to outsource the animation work. This is a huge problem. It could stall the entire project."
    y "And according to our current schedule, we need to hire animators within the next two weeks or we won’t make it in time."
    show yukari sad
    y "Not to mention our art assets were delayed when Sumiko fell sick."
    m "Maybe we should hire freelancers so we can complete it on time."
    m "It'll be a hassle, but it might be worth it. I’ll look online for new investors, too."
    scene sumiko_walk_in with fade
    #door sound
    s "I’m sorry… This is all my fault. If I’d taken better care of my health, I wouldn’t have gotten sick and we wouldn’t be in this situation."
    "With a gloomy look on her face, Sumiko apologizes repeatedly to Yukari and Mayumi until Shunsuke interrupts her."
    ss "It's not your fault, Sumiko. You were only trying to work hard on [anime.name]. Maybe we share the blame for not noticing you were overworked."
    ss "We’re all responsible for the current situation, so don’t be too hard on yourself."
    ss "Pessimism will be our undoing. We should focus on what we can do now, not what we can’t."
    y "I agree. Worrying all day won’t accomplish anything. Let’s get some work done!"
    "Despite Yukari and Shunsuke’s words, tension lingers in the air. No matter what they say, the problems remain."
    show studio_main with fade
    show yukari at left with dissolve
    "She rubs her head. If they don’t relax, it will start to affect their work. Then they’ll have an even bigger problem."
    "There must be a way to put them at ease."
    "Yukari thinks about it and decides to focus on…"
    menu:
        "Raising funds":
            "Funding will solve their problem quicker than anything else. Yukari spends the rest of the day trying to contact investors to pitch [anime.name] to them and hopefully raise additional funds."
        "Drawing storyboards for the anime":
            "The anime itself is the top priority. Yukari spends the rest of the day drawing storyboards for [anime.name]."
        "Cheering everyone up":
            "Although there’s a lot of work to do, brightening the mood is more important. But how? Yukari considers it for a moment, and then leaves the studio to visit a nearby bakery."
            "She returns with enough cookies for everyone to have some. It isn’t a permanent solution, but the tension in the air eases as she passes around the cookies."

label week_4_3:
    $fastForwardDays(2)
    scene studio with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    y "Mayumi, could you spare a few minutes tonight? I need to talk to you."
    m "Of course! Actually I was hoping we’d talk soon. It’ll be good for you to open up to someone about what’s bothering you."
    show yukari sigh
    y "You’re right. It’s getting to be too much."
    y "This gloomy atmosphere is unbearable. I feel like it’s impossible to be optimistic."
    m "Think of it as a test of our strength. Other people, maybe even people who created popular anime, probably faced similar issues in the past. They made it, and we will too."
    show yukari
    y "I hope so."
    m "I’m certain of it."
    y "Can you spread your optimism to Yuuko and Sumiko? They seem really stressed out."
    y "If we let things continue like this, I’m afraid everything will fall to pieces."
    m "Don’t worry. We’ll discuss everything tonight."
    "That promise sustains Yukari through a stressful day at the studio. When night comes, she meets up with Mayumi so they can talk over dinner."
    scene cafe with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    m "So what did you want to talk about?"
    y "A few things, but mainly the morale of the group."
    show yukari worry
    y "I don't quite understand why Yuuko and Sumiko still seem so down. It’s not their fault. We even told Sumiko outright not to blame herself."
    y "Am I missing something?"
    m "It's pretty simple. Even if they know we don’t blame them, they still feel responsible. The delayed art assets and Sumiko’s sickness put us behind schedule."
    m "They’re as enthusiastic about [anime.name] as any of us. Imagine how you’d feel if your role in the project was what delayed us."
    y "Yeah, I’d feel horrible."
    m "Anyone would. I’ll talk to them. Maybe I can cheer them up."
    show yukari sad
    y "Sounds like an awesome idea. I’d talk to them with you, but I probably wouldn’t be any good at it."
    y "I'm too stressed out about raising funds. I haven’t even done enough work on the storyboards, because I can’t stop worrying."
    y "I keep thinking, what if we don't raise enough money? Will we have to shut down the project even after all the work we put into it?"
    m "You're overthinking it. Don’t worry. In the worst case scenario, we'll use our savings to stay afloat until we get investments."
    m "We aren’t going to give up that easily."
    show yukari happy
    y "Thanks. That makes me feel a lot better."
    show mayumi_f laugh_eyes_closed
    m "Anytime."
    y "And thanks for always being there for me. I wouldn’t know what to do without you."
    m "That's what best friends are for, right?"
    "Yukari smiles. Talking to Mayumi has lifted a weight from her shoulders. She can breathe easier now."
    show mayumi_f
    show yukari
    m "By the way, if we want to start animating the characters next week, we’ll need to ask Yuuko to increase the pace of her work."
    m "I checked our art assets, and there’s quite a bit of work untouched."
    show mayumi_f sad_angry
    m "I know this is a bad time to pressure her, but…."
    y "I understand. We need to do what’s best for [anime.name]."
    y "I’ll tell her tomorrow. Be sure to talk to her and Sumiko soon. If they’re already feeling down, it might be hard for them to cope with extra pressure."
    m "Don’t worry, I will."
    y "I know I can count on you."

label week_4_4:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show yuuko at right
    with dissolve
    y "Yuuko, what's the status on the character designs?"
    yuu "The side characters are almost done. We only have a few left to go. Then they’ll need some minor touchups here and there."
    y "How long do you think it'll take to finish everything?"
    yuu "They should be ready next week."
    show yukari worry
    y "Is there any way you can finish them sooner? We have to start outsourcing the animation next week." 
    y "It’ll take time to set things up with the studio, so we need to have the characters ready."
    y "I know it’s a lot to ask, especially since you covered Sumiko’s work when she was sick, but I need you to work harder."
    yuu "I understand. I’ll take care of it."
    show yukari
    y "Just don't neglect your health due to work, okay? We have to pull through this together."
    show yuuko sad
    yuu "I won’t. I wouldn’t want to delay us by getting sick."
    y "No, I didn’t mean it like that. I meant for your own sake."
    "Yuuko nods, but Yukari can tell she’s only disheartened her further. Yukari sighs and returns to her desk. Maybe Mayumi can salvage that situation."
    "As Yukari gets back to work, an email notification pops up. She checks it, and her heart leaps. It’s from one of the investors she contacted… and he’s interested in [anime.name]."
    show yukari laugh_eyes_closed
    show yuuko
    y "YES!"
    "Yukari’s exclamation attracts Shunsuke's attention."
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    ss "What is it? Did we secure new investors?"
    y "Not yet, but one of the investors I tried to get in touch with replied to me."
    y "He's from a notable company, too. If we manage to clinch this deal, we won’t have to worry about money anymore!"
    show shunsuke laugh_eyes_closed
    ss "See? All your hard work paid off in the end. I'm sure you'll convince him and bring him on board with us."
    y "I hope so. He seems really interested. He asked to meet up with me so we can discuss [anime.name]."
    "She beams at the team, hardly able to contain her excitement."
    y "I think this is the moment we’ve been waiting for."
    "As the others talk about how exciting it is to finally have a new source of funding within sight, Yukari gathers up all the documents she’ll need to show the investor."
    "With any luck, they’ll convince them [anime.name] is worth it."
    show yukari happy
    y "It's do or die!"
    "Once she has the documents packed up, she replies to the email and asks him if they can meet for lunch to discuss [anime.name]."
    hide shunsuke with dissolve
    "She holds her breath as she hits “send,” and then she waits."
    "And waits."
    "Since it took him so long to reply to her initial email, she tries not to get too impatient. Instead, she practices in her mind what she wants to say to him."
    "After work, Mayumi approaches Yuuko and Sumiko. Yukari tosses her a relieved smile, and then leaves so they can speak in private."
    "A few hours later, Yukari receives two messages. The first is from Mayumi, about the outcome of her chat with Yuuko and Sumiko."
    "She cleared up their concerns, and both sisters left the studio feeling recharged, energized, and ready to finish the art for [anime.name]."
    "The second is from the investor, asking if they can meet up on Friday."

label week_4_5:
    $nextDay()
    scene studio_main with fade
    show yukari worry at left
    show mayumi_f at Position(xalign = 0.80,yalign = 1.0)
    show shunsuke at pos_outerright
    with dissolve
    y "My heart's pounding. Do you think I should offer to foot the bill for lunch?"
    m "Those things don’t matter. Remember why you’re going there. You need to convince him it's a great idea to invest in [anime.name]."
    y " I want to make a good impression."
    show mayumi_f sigh
    m "You're overthinking this. You'd be much better off thinking about the kinds of questions he’ll ask."
    m "After all, it’ll be really awkward if you can't answer his questions!"
    show yukari sigh
    show mayumi_f
    y "Why didn't I think of that?"
    "But her mind goes blank. With the meeting so close, she can’t focus on anything. All she can think about is how [anime.name] might be doomed if she messes this up."
    "Lightheaded, she grips the edges of her desk and tries to breathe. She needs to focus on the questions so things don’t go wrong, but she can’t. What will the investor ask? What if things go wrong?"
    ss "He’ll probably ask the basic questions:"
    ss "What differentiates [anime.name] from all the other anime out there?"
    ss "Do we have a roadmap?"
    ss "How much experience do we have?"
    "His calm voice steadies Yukari, and she takes a deep breath. She can answer those questions."
    ss "Don't forget to stay calm, and try not to stutter when you talk to him. Make sure you sound confident!"
    show yukari
    y  "Thanks. I'll keep that in mind."
    ss "Preparation is half the battle."
    y "What do you mean?"
    ss "If you’re well-prepared for this meeting, it’ll be that much easier to convince him."
    m "Everything will be fine!"
    m "Thank you. I’ll start preparing now."
    "She grabs a notebook and writes down the answers to the questions Shunsuke suggested. She adds a few more things to mention about [anime.name] and thinks about other potential questions."
    y "I hope he doesn't ask anything too difficult…"
    "Nerves threaten to overtake her again, but her team members toss encouraging smiles her way. With another deep breath, she rehearses the answers in her mind. Confidence. Preparation. She can do this."
    scene cafe with fade
    show yukari at left with dissolve
    play music "music/ost/nervous.ogg" fadein 1.0
    y "There's still about 20 minutes before we’re supposed to meet… Maybe I arrived too early."
    y "Better to be early than late, though. That would give him a bad impression of me from the start."
    "She finds a seat. Thoughts of the upcoming meeting still have her on edge, so she checks through all the materials she brought to make sure she didn’t forget something."
    "Everything is there. She runs over the questions again in her mind, and then checks her social media networks to relax."
    "After a little while, a man dressed in a business suit and carrying a briefcase enters the restaurant. Yukari’s mouth goes dry. It must be him."
    "She waves, and he approaches her table."
    show investor at right with dissolve
    investor "Yukari?"
    y "Yes."
    "He takes the seat across from her and smiles. She breathes a little easier."
    show investor little_happy
    investor "It’s good to meet you. How is the development of [anime.name] going?"
    "Although her heart hammers against her chest, her practiced answer spring to her lips."
    y "We're doing great. Next week, we’re going to start the animation work."
    y "However, we'll soon run out of funds, which is why I’ve been looking for investors."
    investor "Well, the idea of [anime.name] intrigues me. I discussed it with my company last week and we might be interested in investing in it."
    investor " Could you tell me more details about [anime.name]?"
    y "Of course."
    if anime.category == Anime.HAREM:
        y "[anime.name] follows the only male member of a high school science club. In addition to the romantic elements, we’ve placed a strong emphasis on comedy."
        y "The female characters all love science, and they like to conduct experiments. Unfortunately, their experiments tend to lead to trouble."
        investor "Interesting. Stories involving science are popular right now, you know, especially if they encourage girls to enter scientific fields."
        show yukari happy
        y "Really? Then [anime.name] should be great! Although they get into a lot of trouble, the girls’ interest in science is inevitably shown as a good thing."
    elif anime.category == Anime.MYSTERY:
        y "[anime.name] is about a detective who is out of work, so he takes on a case no one else wants."
        y "Solving that case is the main focus of the plot, but flashbacks and hints will gradually reveal why his previous case ruined his reputation."
        investor "Are the two cases connected?"
        y "Y-yes, actually! How did you know?"
        show investor smile
        investor " I asked because that’s a good twist that will make the overall plot more solid. I’m glad you already had it in mind."
    elif anime.category == Anime.ACTION:
        y "The main character of [anime.name] has a normal life until an article in an old newspaper leads him to discover an underground chamber."
        y "What he doesn’t know is that he’s on the edge of an ancient conspiracy, and the conspirators will kill him rather than risk a witness."
        investor "Would you say your focus is more on action scenes or the conspiracy itself?"
        y "Definitely action. We want it to be the sort of anime where anyone watching can follow along, but fans who really care will be able to dig deeper into the conspiracy and lore."
    investor "What's your current progress?"
    "Yukari makes a mental note to thank Shunsuke again if this works out. Most of these are the questions she went over in her mind. Nothing too difficult so far."
    y "We’re currently in between writing scenarios for the episodes and working on production for [anime.name]. The art is coming along nicely, and we’ll begin outsourcing the animation soon."
    investor "Do you have a schedule drafted up?"
    y "Yes, I brought our schedule with me."
    "Yukari opens her bag and finds the documents she brought. She passes them to the investor."
    "He scans the documents and smiles."
    show investor smile
    investor "It looks like you’ve planned things out very well for [anime.name]. It looks promising."
    "He opens his briefcase and pulls out a paper, which he hands to Yukari. Her breath catches in her throat as she takes it."
    scene investor_yukari with fade
    investor "I had a hunch I’d be pleased with your team, so I brought the contract along with me."
    investor "Take your time to read it. You can sign it now or later, whichever you prefer."
    "YES! They did it! They got an investor interested! Yukari can barely contain her excitement. She wants to scream and jump in the air for joy."
    "However, she still needs to appear professional, so she clears her throat and speaks in a voice much calmer than how she feels."
    y "Thank you. I’ll look it over now."
    "She reads the contract carefully. It seems like a pretty good deal, with nothing she needs to think about or consult the team on."
    "When she reaches the end, she gives it one final scan and then signs it."
    investor "Wonderful. I expect to see great things from [anime.name]. I'll check on your progress from time to time. It’s been a pleasure doing business with you."
    y "Thank you. I’m happy to work with you, too. We'll make [anime.name] an experience people won't forget."
    scene cafe with fade
    show yukari happy at left
    show investor little_happy at right
    with dissolve
    investor " I have a meeting soon, so I’ll need to leave now unless there’s something else you wanted to discuss."
    y "That’s everything for now. Have a good day!"
    investor "You as well. Goodbye."
    hide investor with dissolve
    "The moment he’s out the door, Yukari pulls out her phone and texts her friends to let them know what happened."
    "Replies come almost immediately. Everyone wants to celebrate with a feast."
    "She certainly can’t argue with that."
    scene studio with fade
    show yukari at pos_left
    show sumiko laugh_eyes_closed at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    s "All right, Yukari! That was amazing! Now we can focus on producing [anime.name]."
    show yuuko happy
    yuu "Congratulations."
    s "How did you convince him?"
    show mayumi happy
    m "Were the questions hard? Were you nervous?"
    show yukari laugh_eyes_closed
    y "Honestly, I was pretty nervous, but the questions he asked me weren’t too difficult. From there, everything worked out."
    "She looks at Shunsuke."
    y "Thank you again for suggesting questions he might ask."
    show shunsuke happy
    ss "Any time."
    m "And now we have funding! What did it feel like when he handed you the contract?"
    y "Very surreal."
    "She laughs."
    y "Part of me still can’t believe it really happened."
    m "Not everyone gets a chance to talk with investors like you did, especially not as young as you are!"
    m "I knew you could do it!"
    show yukari
    y "Let’s not get ahead of ourselves, though. We’ve solved our funding problem, but we still have other important issues to take care of. It’s not over yet."
    "Still, with the afternoon’s success, she feels like she can handle anything."
    y "Mayumi, Shunsuke, we need to discuss outsourcing work for [anime.name]. Yuuko and Sumiko, you should continue working on the art so we’ll meet our schedule for [anime.name]."
    show yuuko
    yuu "What will you be talking about?"
    y "Delegating tasks and going over any potential concerns."
    yuu "Sounds interesting... I wish I could help."
    y "Just because you aren’t involved with this doesn’t mean you can’t help. Your art is one of the most important things we need right now."
    "Yuuko nods. She and Sumiko head back to their desks to work on the art for [anime.name]. Yukari returns her attention to the other two."
    scene studio
    show yukari at left
    show mayumi_f at Position(xalign = 0.80,yalign = 1.0)
    show shunsuke at pos_outerright
    with dissolve
    y "Have either of you had experience with hiring freelancers? "
    "Silence."
    show yukari sigh
    y "Right… So we’re all greenhorns. That makes it more likely things will go wrong without us noticing."
    m "Aw, I’m sure it won’t be that bad."
    ss "But there’s nothing wrong with preparing for the worst."
    y "For now, let's delegate tasks. Mayumi, as the sound editor, you should be in charge of everything related to our audio."
    y "In particular, we need to hire voice actors and find a suitable studio where we can record our script, as well as the opening and ending songs."
    show mayumi_f happy
    m "Okay, I can do that."
    y "That leaves animation work and handling matters at the studio."
    ss "I don’t have any expertise when it comes to animation, so I’ll manage the studio."
    ss "I'll let you know if anything important happens."
    show yukari laugh_eyes_closed
    y "Okay, then I’ll supervise the outsourced animation work. This arrangement seems pretty good."
    show mayumi_f
    m "Once I start composing the music for [anime.name], though, I’ll need some help."
    m "Composing takes a lot of time, so I won’t be able to supervise all the recording sessions after that."
    show yukari
    y "Hmm… who do you think should take over supervising?"
    m "You."
    show yukari worry
    y "Me? But I don’t know a lot about music. How will I know if it’s going well or not?"
    m "Don’t worry. You can attend a few recording sessions with me, and I’ll make sure you learn what to listen for."
    m "Besides, you have the clearest picture of what [anime.name] should be like. You’ll know if the music doesn’t sound right."
    if anime.category == Anime.HAREM:
        m "Just remember, it should be quirky and upbeat."
    elif anime.category == Anime.MYSTERY:
        m "Just remember, we need a mix of upbeat songs and tense songs."
    elif anime.category == Anime.ACTION:
        m "Just remember, this is action. If your heart pounds, that’s good. If you feel drowsy, that’s bad."
    show yukari laugh_eyes_closed
    "Yukari smiles."
    y "All right. Is there anything else we need to discuss?"
    ss "Not that I know of."
    m "Nope."
    y "Great. Then I’ll see everyone tonight for dinner!"
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi happy at pos_farleft behind yukari
    with dissolve
    m "I hereby call tonight’s “We Got Funded” Celebration to order!"
    "Everyone laughs."
    "For once, no one talks about problems or worries. They have an investor, and [anime.name] seems closer to becoming a reality than ever before. It’s a night for celebration and relaxation."
    "As Yukari looks around at her team members, she feels better than she has in weeks."
    show sumiko laugh_eyes_closed
    s "Oh! I almost forgot, want to hear what happened to me the other day?"
    m "No, what?"
    yuu "Sumiko, they don’t want to hear this story."
    show sumiko tsundere
    s "Yes they do!"
    show yuuko sigh
    yuu "No they don’t."
    s "Look at them! They’re practically on the edge of their seats!"
    yuu "Everyone, trust me, you don’t want to hear this story."
    show yukari happy
    y "Now you’re making me curious."
    s "Hah! See?"
    "She shoots her sister a triumphant look. Yuuko just shakes her head and turns her attention to her meal as the story begins."
    show sumiko
    s "Yuuko and I went shopping for groceries on our way home. Since we had a lot to buy, we took the bus instead of walking home."
    s "Well, the bus was really crowded, so we couldn’t find two seats together. Guess who I sat by?"
    m "A celebrity?"
    y "Someone who knew about [anime.name]?"
    ss "An old friend you haven’t seen in years?"
    show sumiko happy
    s "Wrong, wrong, and wrong. An interplanetary traveler!"
    "For a long moment, no one speaks. They just stare at Sumiko while Yuuko covers her face and looks like she wants to disappear."
    "Yukari runs over the words in her mind and tries to make sense out of them. At last, Shunsuke breaks the silence with a tentative guess."
    ss "So… an astronaut?"
    s " Not exactly. See, he was abducted by aliens a few months ago, but they became his friends. Now he gets to go on trips through space! Underwater, too. Have you ever heard of USOs?"
    show yuuko sad_angry
    yuu " It was the worst bus trip of my entire life. Everyone was quiet except for this conspiracy theorist guy… and my sister. I wanted to pretend I didn’t know her."
    s "But she couldn’t, because I still had half of our groceries."
    show yuuko happy
    "They exchange glances and laugh."
    m "So, you believe in aliens, Sumiko? And you don’t, Yuuko?"
    sisters "Right."
    ss "It’s good to know one of you has common sense."
    show shunsuke sigh
    s "Thanks!"
    ss "I wasn’t talking about you."
    y "You two are very different, aren’t you?"
    show sumiko
    s "It took you this long to figure it out?"
    y "No, but you’re so close. It’s nice to see people who don’t let their differences drive them apart."
    show yuuko laugh_eyes_closed
    show shunsuke
    yuu "We are sisters, after all. I’d do anything for Sumiko."
    yuu "…Even if she does get into embarrassing conversations on the bus."
    ss "Now, Sumiko, let me explain to you why aliens can’t possibly exist."
    s "Oh brother, this ought to be good."
    "As they debate, Yukari leans back in her seat and smiles to herself. Their group has come a long way since the beginning."
    "At first, she worried they might clash when they worked together, but they’ve turned into a cohesive team. Someday, she hopes they all have a bond as strong as the one shared by Sumiko and Yuuko."
label week_4_6:
    scene home with fade
    show yukari at left
    with dissolve
    "Another weekend arrives, and Yukari decides to…."
    menu:
        "Raise additional funds":
            "Just because they have one investor doesn’t mean they can relax completely. Yukari runs through her meeting with the investor and writes down the aspects of [anime.name] he seemed the most pleased with."
            "She spends the rest of the weekend contacting more potential investors with a rewritten pitch highlighting the project’s greatest strengths."
        "Read books on management":
            "Yukari knows her management style isn’t always ideal, so she stops by the library and checks out three books on successfully managing a business."
            "Although the reading is dry, she forces herself through all three before the weekend ends."
        "Relax":
            "With the progress they’ve made, Yukari feels comfortable taking some time off from [anime.name]."
        "Polish up the storyboards":
            "The storyboard drafts are finished, and Yukari has already gone through the first episode again to make changes."
            "Over the weekend, she polishes it up until she’s satisfied enough to consider the first episode’s storyboard complete."
    scene studio 
    $nextWeek()
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music
    $fastForwardDays(2)
    stop music 
    jump week_5_1

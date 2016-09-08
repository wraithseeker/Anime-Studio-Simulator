define fourth_w = Character('Fourth Place Winner', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define manager = Character('Manager', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define office_l = Character('Office Lady', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define police_o = Character('Police Officer', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define mother = Character("Boy's Mother", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define boy = Character("Little boy", color="#000",ctc="ctc_fixed",ctc_position="fixed")

label random_1:
    $rd_c = RandomCharacter(["m"])
    $company = getRandomCompany()
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p== "ss":
        show shunsuke at right
    elif rd_c.p == "s":
        show sumiko at right
    with dissolve

    rd_c.say "Yukari, there’s something I have to tell you."
    y "What is it, [rd_c.person]? You can tell me anything."
    rd_c.say " I’ve been scouted by [company]."
    if rd_c.p == "yuu":
        show yuuko sad
        rd_c.say "I visited their studio, and I really feel at home there… N-not that I don’t feel at home here, but…"
    elif rd_c.p == "s":
        rd_c.say "They need an artist and my style works perfectly with theirs."
    else:
        rd_c.say "[company] is well-established and offers excellent chances for career advancement."
    rd_c.say "I just wanted to let you know that I am considering the offer."
    show yukari worry
    y "(Thinking to herself) Oh no! We can’t finish [anime.name] if [rd_c.person] takes another job!"
    y "What should I do?"
    menu:
        "Assume [rd_c.person] will get over it":
            "check if lose condition stuff"
        "Address [rd_c.person]'s concerns this weekend":
            "Can't do anything this weekend"
        "Offer [rd_c.person] money from [anime.name] funds":
            show yukari sad_angry
            y "I understand that [company] is a great company to work with, but won't you consider staying with us?"
            y " I can pay you some money for your work, if that'll change your mind?"
            if rd_c.p == "yuu" or rd_c.p == "s":
                if rd_c.p == "yuu":
                    show yuuko laugh_eyes_closed
                elif rd_c.p == "s":
                    show sumiko laugh_eyes_closed
                rd_c.say "That'll do, honestly it was mostly because of my parents nagging at me to find a real job to earn money, which has reached a tipping point because I currently don't earn any money."
            else:
                rd_c.say "Yes that just changed my mind. Having pocket money sounds great, considering that my parents wanted me to get a part time job to 'learn' how to survive in society."
                rd_c.say "With that sum of money, I'll be able to convince my parents that I'm learning life skills through this project."
    "end"
    return

label random_2:
    scene cafe with fade
    $rd_c = RandomCharacter()
    show yukari worry at left
    if rd_c.p == "m":
        show mayumi_f sad at right
    elif rd_c.p == "s":
        show sumi sad at right
    elif rd_c.p == "yuu":
        show yuuko sad at right
    else:
        show shunsuke sad at right
    with dissolve
    y "Hey [rd_c.person], is something wrong? You seem troubled today."
    if rd_c.p == "m":
        rd_c.say "Thanks, Yukari, I’m glad you noticed. I’m in a bit of financial trouble…"
        rd_c.say "My uncle had a stroke and our family can’t afford the healthcare costs."
        rd_c.say "Do you have any ideas on how I can get some money?"
    elif rd_c.p == "yuu":
        rd_c.say "O-oh, I didn’t think you’d notice…"
        rd_c.say "My grandfather is in the hospital and we’re struggling to pay for his treatment…"
        rd_c.say "I want to get money to help out, but I don’t know how…"
    elif rd_c.p == "s":
        rd_c.say "If I told you my secret plan for world domination was in jeopardy, would you believe me?"
        rd_c.say "Sorry. I’ve tried to joke to keep my spirits up, but it’s not working. See, my grandfather is undergoing expensive medical treatments, and I’m afraid we’ll run out of money."
        rd_c.say "Any ideas?"
    else:
        rd_c.say "I didn’t intend to trouble you with this, but if it’s that obvious, I suppose I should explain."
        rd_c.say "My cousin was in a bad car accident. She’s alive, but the medical bills are exorbitant."
        rd_c.say "If I’ve been distracted, it’s because I’m trying to think of a way to get the money to help her."
    y "Oh no! Thank you for telling me. Let me think…"
    menu:
        "Tell [rd_c.person] to approach their bank for loans":
            y "Have you tried getting a loan from your bank?"
            rd_c.say " Not yet…"
            y "I’ve heard that bank loans are pretty reasonable nowadays. Give it a try."
            rd_c.say "Okay…"
        "Give [rd_c.person] money from the project funds":
            y "Here."
            rd_c.say "What? But this money is meant for [anime.name]!"
            y "Take it. You’re a friend and part of the team, so we should help you out. Besides, your family’s health is more important than an anime."
            rd_c.say "Thank you so much…"
    return

label random_3:
    $rd_c = RandomCharacter()
    scene studio_main with fade
    show mayumi at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p == "s":
        show sumiko at right
    else:
        show shunsuke at right
    with dissolve
    m "Hey guys! Check out the new OST I wrote for [anime.name]!"
    "The team listens as Mayumi plays the OST for everyone to hear."
    if rd_c.p == "yuu":
        show yuuko worry
        rd_c.say "W-wait, the OST’s title… is this the leitmotif for the antagonist? But it doesn’t fit his style at all…"
    elif rd_c.p == "s":
        show sumiko sad_angry
        rd_c.say "It’s a little bland, isn’t it? Can’t you improve it? Maybe change the rhythm?"
    else:
        show shunsuke angry
        rd_c.say "No, no, no, this song’s tone doesn’t fit the scene at all!"
    show mayumi sad_angry
    m "Do you have to be so critical? I spent a long time working on it!"
    rd_c.say "You did ask for opinions."
    m "Yeah, but I didn’t think you’d say that…"
    rd_c.say "So you wanted me to lie?"
    m "I’d like to see you come up with a better OST!"
    show yukari at pos_left 
    show mayumi at pos_farleft
    with dissolve 
    y "Guys, please calm down!"
    menu:
        "Agree with [rd_c.person]":
            "asdasd"
        "Agree with Mayumi":
            "asdasd"
        "Try to distract them by changing the topic":
            show yukari happy
            y "Have you guys listened to the new song released by Love Live? It's selling like hotcakes right now and must be really good."


label random_4:
    $rd_c = RandomCharacter()
    $company = getRandomCompany()
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p == "s":
        show sumiko at right
    elif rd_c.p == "m":
        show mayumi_f at right
    else:
        show shunsuke at right
    with dissolve
    y "Wow, [anime.name] is getting quite a lot of attention online!"
    y "[company] invited me to an interview for aspiring anime producers!"
    if rd_c.p == "yuu":
        show yuuko happy
    elif rd_c.p == "s":
        show sumiko happy
    elif rd_c.p == "m":
        show mayumi_f happy
    else:
        show shunsuke happy
    rd_c.say "Really? That's awesome! You should go!"
    rd_c.say "Think of the publicity this interview will bring. [company] is very well regarded in the anime industry."
    y "I don't know… The last interview conducted by [company] ruined an aspiring producer because the focus shifted from anime to his private life."
    menu:
        "Attend the interview":
            "abc"
        "Do not attend the interview":
            y " I’m going to decline the offer."
            if rd_c.p == "yuu":
                show yuuko sad
            elif rd_c.p == "s":
                show sumiko sad
            elif rd_c.p == "m":
                show mayumi_f sad
            else:
                show shunsuke sad
            rd_c.say "What?"
            y "It looks good on the surface, but it’s way too risky."
            rd_c.say "Aw, I thought it was a good idea…"
        "Send [rd_c.person] to be interviewed instead.":
            y "Why don’t you go?"
            if rd_c.p == "yuu":
                show yuuko worry
            elif rd_c.p == "s":
                show sumiko worry
            elif rd_c.p == "m":
                show mayumi_f worry
            else:
                show shunsuke worry
            rd_c.say "M-Me?"
            y "Yes, since you think it’s such a good idea."
            rd_c.say "Well, all right."

label random_5:
    scene studio_main with fade
    show yukari at pos_left
    show mayumi sigh at pos_farleft behind yukari
    show sumiko sad at pos_middleright_half
    show shunsuke at Position(xalign = 1.05,yalign = 1.0) behind sumiko
    with fade
    m "What in the world is this? Have you guys checked the inbox recently?"
    s "Oh gross, not again! Who’s been sending all this ridiculous mail?"
    ss "Yukari, what do you make of this?"
    y "(Thinking to herself) These messages are pretty awful… How should I handle this?"
    menu:
        "good stats":
            show yukari happy
            show mayumi sad
            y " Come on, guys, don’t let some stupid emails get you down!"
            m "Did you read the things they said about us?"
            y "Yes, but I don’t care. This guy is clearly just a troll."
            m "You mean he’s waiting under a bridge to grab us when we cross?"
            s "Thank you in advance for my upcoming nightmares."
            y " I mean he’s trying to rile us. Don’t fall for it! We’re not going to let a bunch of spammy messages ruin our dream, are we? Of course not!"
            ss "Hah, the joke will be on him when [anime.name] is a hit."
            m "Yeah! Let’s get to work and show him what we’re capable of!"
        "bad stats":
            hide mayumi
            hide shunsuke
            hide sumiko
            show yukari sad at left
            show mayumi_f worry at right
            with dissolve
            "She can’t focus. Every time she tries to think of a solution, the discouraging comments from the email run through her mind."
            "What if they’re right? What if their team really is awful and [anime.name] is doomed to failure?"
            y "Ugh…"
            m "Yukari?"
            y "Leave me alone. I want to be by myself for a little bit…"
            "She can tell her attitude makes the others even more disheartened, but she’s too upset by the emails to care. "

label random_6:
    $rd_c = RandomCharacter(["s","yuu"])
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "m":
        show mayumi_f at right
    elif rd_c.p == "s":
        show sumiko at right
    with dissolve
    rd_c.say "Yes, I agree with you completely, sir, this advertising will help our project greatly!"
    rd_c.say "I’ll get back to you soon with the good news."
    "[rd_c.person] hangs up the phone."
    y "Who was that?"
    rd_c.say "An advertiser interested in working with us! He has a sure-success advertising program that can lift our publicity sky-high. It’s pretty expensive, but it’ll be worth it."
    y "Are you sure he can be trusted?"
    rd_c.say "Of course! He says he worked with many companies before!"
    y "I don’t know… it sounds kind of shady to me."
    menu:
        "Accept the advertising deal":
            "what"
        "Refuse the advertising deal":
            y "This isn’t a risk worth taking."
            if rd_c.p == "m":
                show mayumi_f sad_angry
            elif rd_c.p == "s":
                show sumiko sad_angry
            rd_c.say "But… but…"
            y "Eventually you’ll learn to judge when something sounds too good to be true."
            rd_c.say "I guess you’re right… I’m sorry."
            y "Don’t apologize! Anyone could be fooled by a conman."
            rd_c.say "Sure…"

label random_7:
    $rd_c = RandomCharacter()
    scene cafe with fade
    show yukari at left
    if rd_c.p == "s":
        show sumiko happy at right
    elif rd_c.p == "m":
        show mayumi_f happy at right
    elif rd_c.p == "ss":
        show shunsuke happy at right
    else:
        show yuuko happy at right
    with dissolve
    rd_c.say "Guess what, guys? I won VIP tickets to AnimeFest next week!"
    if rd_c.p == "s":
        show sumiko sad at right
    elif rd_c.p == "m":
        show mayumi_f sad at right
    elif rd_c.p == "ss":
        show shunsuke sad at right
    else:
        show yuuko sad at right
    rd_c.say "Oh no... there are only 4 tickets in this envelope."
    rd_c.say "That means one of us can’t go…"
    y "That's unfortunate that one of us will miss out on AnimeFest."
    y "But back to the main point, since we are VIPs, will we be able to interact with anime industry professionals?"
    if rd_c.p == "s":
        show sumiko at right
    elif rd_c.p == "m":
        show mayumi_f at right
    elif rd_c.p == "ss":
        show shunsuke at right
    else:
        show yuuko at right
    rd_c.say "Yes, that's an exclusive privilege for VIPs!"
    "Who should stay behind?"
    $rd_remaining_c = rd_c.remainingCharacters()
    $rd_stay_behind = False
    menu:
        "Tell Yuuko she won't be going" if "yuu" in rd_remaining_c:
            if rd_c.p == "s":
                hide sumiko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "ss":
                hide shunsuke
            show yuuko sad_angry at right with dissolve
            y  "Yuuko, I’d like you to stay here."
            yuu "Oh..."
            show yukari worry
            y "Don’t look so sad! It’s not anything against you. But since the character designs are pretty much completed, there’s not a lot of reason for you to go, right?"
            yuu "I understand…"
            y "Do you really?"
            yuu "Sure, I guess…"
        "Tell Sumiko she won't be going" if "s" in rd_remaining_c:
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "ss":
                hide shunsuke
            show sumiko worry at right with dissolve
            s "Whoa, whoa, why are you looking at me like that? You… no way, are you thinking I should stay behind?"
            y "Someone has to."
            s "Yeah, but why does “someone” have to be me?"
            y "Well, we have two artists. Yuuko can tell you what she learns from the professionals there. You wouldn’t argue that your sister should stay behind instead, would you?"
            s "Ugh, you sure know how to make a girl feel guilty."
        "Tell Shunsuke she won't be going" if "ss" in rd_remaining_c:
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "s":
                hide sumiko
            show shunsuke at right with dissolve
            y "Shunsuke, I think it’s best if you stay behind."
            ss "Why me?"
            y "How much can you really benefit from talking to industry professionals? Your writing style is your own, not theirs."
            ss "Yes, but—"
            y "Whereas the rest of us will benefit a lot more."
            ss "I could still—"
            y "Someone has to stay behind."
            ss "Oh, fine. I’ll do it for the team."
        "Tell Mayumi she won't be going" if "m" in rd_remaining_c:
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "s":
                hide sumiko
            elif rd_c.p == "ss":
                hide shunsuke
            y "Sorry, Mayumi, but would you mind staying behind?"
            show mayumi_f sigh at right with dissolve
            m "Aw, do I have to?"
            y "Only four of us can go, and I think the others need the experience more than you. Think of it as a compliment!"
            m "Sure… If you say so…"
        "Stay behind and let the rest go":
            hide shunsuke
            show mayumi_f at pos_outerright
            show yuuko at pos_right
            show sumiko at pos_middleright
            with dissolve
            y "You four go and have a good time. I’ll stay."
            show mayumi_f sigh
            m "Aw, Yukari, but—"
            y "No buts. I’ve made up my mind."
            show sumiko happy
            show yuuko happy
            s "See, that’s the sign of a good leader, everyone. Thanks, Yukari!"
            yuu "Yes, thank you."
            y "You better! I’m counting on you!"
            $rd_stay_behind = True    
    if rd_stay_behind:
        "Yukari stays at home during AnimeFest although she feels sad thinking of the others having fun without her. It’s balanced by the happiness she feels when she remembers their smiles and Sumiko calling her a good leader."
    else:
        "AnimeFest is both fun and informative, although Yukari can’t help but feel a little bad that she made one of the team members miss it all."

label random_8:
    scene studio_main with fade
    show yukari at left
    show sumiko angry at right
    with dissolve
    "Yukari, do you hear that noise? It's been bugging me all day."
    menu:
        "Investigate the noise":
            show yukari worry
            y "Hmm… where is it coming from?"
            s "The ceiling, I think. It sounds like it’s right above my head."
            "Yukari frowns up at the ceiling for a moment and then climbs onto a chair so she can reach it. She pushes up on one of the ceiling tiles so she can remove it."
            s "Wow, I didn’t know they came out like that!"
            y "Someone get me a flashlight."
            show mayumi_f at pos_middleright_half behind sumiko with dissolve 
            m "Here!"
            "Yukari shines the flashlight into the space above the ceiling."
            y "I don’t see anything."
            "She replaces the tile and steps down from the chair."
            y "Let me know if you still hear it, okay?"
            s "All right."
        "Ignore the noise":
            show yukari tsundere
            y "I don’t hear anything."
            show sumiko sad_angry
            s "Well I can!"
            y "It’s probably just your imagination. Try to ignore it."
            s "Ugh…"

label random_8_end:
    scene studio_main with fade
    show sumiko sad_angry at right
    show yukari at left
    with dissolve
    s "Yukari! Maybe I’m imagining things, but that annoying sound is back!"
    menu:
        "Investigate the noise":
            show yukari sigh
            y "Oh, fine, I’ll take a look."
            s "I think it’s coming from the ceiling."
            "Even though she still can’t hear anything, Yukari grabs a flashlight and climbs onto a chair. She pushes the nearest ceiling tile up and removes it. Then she shines the light into the darkness."
            y "Hmm…"
            s "Do you see anything?"
            y "Looks like some animal droppings."
            show sumiko sigh
            s "Ew!"
            show yukari
            y "No sign of the animal, though. Maybe it left."
            "She replaces the ceiling tile and steps down from the chair."
            show sumiko
            y "Let me know if the noise continues, and we’ll call in an exterminator."
            s "All right."
        "Tell Sumiko  that it's just her imagination":
            show yukari tsundere
            y "I still don’t hear anything."
            show sumiko angry
            s "That’s not my problem! This noise is so annoying."
            y "You must be imagining it. Take a walk or something and try to forget about it."
            s "Seriously?"
            "She folds her arms and stares up at the ceiling."
            s "You hear that, mysterious noise? Yukari says if I take a walk, you have to stop!"
            "Yukari shakes her head and goes back to work."
            scene studio_main with fade
            "Later that day..."
            show yukari at left
            show sumiko worry at right
            with dissolve
            s "Yukari… it’s getting louder."
            y "What are you talking about?"
            s "That noise. It’s—"
            "missing sound effect"
            "Both of their cases snap to the ceiling. The tile above them breaks and a dark shape drops onto Sumiko’s desk."
            s "EEK!"
            show yukari
            y "Don’t panic! It’s just a rat."
            show sumiko tsundere
            s "JUST a rat?!"
            "The rat lifts its head and stares at them. Then it jumps down to the floor and scampers away from the desk."
            s "Agh! Darn it, Yukari, why couldn’t you just listen to me?!"
            "Yukari chases after the rat and manages to get it out of the studio, but the damage has already been done."
            hide sumiko
            hide yukari
            show yukari at left
            show sumiko at pos_middleright
            show shunsuke at pos_outerright
            show yuuko at pos_right
            with dissolve
            ss "You realize we’ll probably need to get in an exterminator now, just in case there are more?"
            show sumiko angry
            s "More? MORE?"
            show yuuko worry
            yuu "Sis, are you okay?"
            s "No, I am not okay!"
            "Yukari glances away in embarrassment and makes a mental note to take her team members’ concerns more seriously from now on."







# label random_1:
#     scene street with fade
#     show yukari at left with dissolve
#     "I wonder what all the commotion is about?"
#     "She squeezes through the crowd and reaches the arcade. They’re holding a “Dance Revolution” competition."
#     y "Wow, those people warming up are really good."
#     show yukari happy
#     y "Wait a minute… Isn't that the ultra-rare Miku figurine?! And it’s only Fourth Prize?"
#     y "Hmm, it looks like registration is still open…"
#     show yukari worry
#     "She hasn’t played in a long time, and she knows she doesn’t stand a chance against the major competitors. Fourth place, though, might be feasible."
#     menu:
#         "Register for the competition":
#             "Yukari enters the competition."
#             show yukari sigh
#             y "Oh gosh, I haven't played this in forever!"
#             y "What was I thinking?"
#             y "Forget fourth place, I guess I'll have to settle for being the comic relief."

#         "Cheer on the competitors":
#             show yukari happy
#             "It’s been too long since she played. Yukari stays with the crowd and cheers." 
#             "The contestants are all fantastic. When the competition ends, she claps for the winners."
#             fourth_w "Thanks for cheering me on. It really boosted my confidence!"
#             fourth_w "To be honest, I don't really want this figurine I won. I'd like you to have it."
#             show yukari laugh_eyes_closed
#             y "No way! Really? Thank you so much!"
#             y "Wow, I wasn't even cheering for him in particular…"
#     return

# label random_2:
#     scene cafe with fade
#     show yukari at left
#     show sumiko at pos_right
#     show yuuko at pos_outerright
#     show shunsuke at pos_middleright
#     with dissolve
#     show shunsuke sigh
#     ss "Yukari, could you try to act more ladylike?"
#     show yukari angry_mouth_closed
#     y "What's your problem?!"
#     ss "This isn’t how you behave at a nice café like this."
#     show yuuko sigh
#     yuu "Please, let’s just make our orders."
#     s "This stuff happens way too often when we’re out together…"
#     "Mayumi ignores her friends’ arguments and checks her texts."
#     show mayumi at left
#     hide yukari
#     hide sumiko
#     hide yuuko
#     hide shunsuke
#     with dissolve
#     "Advertisement: 1-for-1 Gachapon! Get your tickets now!"

#     m "This is too good to be true!"
#     "She stares at the advertisement and decides to…"
#     menu:
#         "Buy some tickets":
#             "When will she ever get another opportunity like this? Mayumi jumps on the deal and ends the day with 10 tickets for the price of 5."
#             "Next week, she’s watching the news when they cover the story of a recent Gachapon scam."
#             "Hundreds have lodged complaints about XYZ company…"
#             show mayumi sad_angry
#             m "What… but that’s the company I bought from! They were closing down, and…?"
#             m "It was all a scam?! They cheated me? Oh no, my money…"
#         "Ask her friends to buy tickets together":
#             show mayumi happy at left
#             show yukari_f at pos_middleright
#             show shunsuke at pos_right
#             with dissolve
#             m "Everyone, look at this! It’s a 1-for-1 Gachapon sale! Want to get in on the deal with me?"
#             show shunsuke sigh
#             ss "C'mon, Mayumi , that's obviously a scam."
#             show mayumi worry
#             m "It is?"
#             show yukari_f tsundere
#             y "If it sounds too good to be true, you should always be cautious. And there’s something fishy about this deal."
#             ss "Everything about it looks shady."
#             show mayumi worry
#             m "Yukari and Shunsuke agree on something? That’s so rare, they’re probably right."
#             m "All right, I’ll trust you guys on this."
#             "When news of a Gachapon scam emerges a week later, she’s glad she did."
#     return
# label random_3:
#     scene street with fade
#     show sumiko_f laugh_eyes_closed at pos_left
#     show yuuko_f at pos_farleft
#     with dissolve
#     s "Wow, do you smell that?"
#     yuu "What is it? It's amazing…"
#     manager "Hello!"
#     "Sumiko and Yuuko stop. The sign behind the man announces the grand opening of a new café, and the delicious smells waft from inside the building."
#     manager "We're holding a special promotion to celebrate our grand opening."
#     manager "Would you like to try a sample from our breakfast menu?"
#     s "Yes, please! These look mouth-watering!"
#     show yuuko_f happy
#     yuu "Mm, they're really delicious too!"
#     manager "Come on inside. There's plenty more on the menu."
#     "The two girls exchange glances. After all, they’re on their way to the studio."
#     menu:
#         "Head into the cafe":
#             scene cafe
#             show sumiko_f at left
#             show yuuko at right
#             with dissolve
#             "A little relaxation won’t hurt. They follow the manager into the café."
#             show yuuko happy
#             yuu "It’s beautiful in here."
#             show sumiko_f happy
#             s " Look at how many things are listed on the menu!"
#             manager "Let me serve you today's breakfast special."
#             s "Thank you!"
#             "Two hours later…"
#             show yuuko
#             s "That was the best breakfast I've had in a long while!"
#             "Yuuko nods, and then looks at the clock on the wall."
#             show yuuko worry
#             yuu "We're going to be so late… I hope Yukari isn’t angry."
#             show sumiko_f
#             s "We’ll just tell her about the café. A tip about great food like this should make up for anything!"

#         "Continue to work":
#             scene studio
#             show yukari happy at left
#             show sumiko at pos_middleright_half
#             show yuuko at pos_farright
#             with dissolve
#             y "Hey, you guys are here early!"
#             yuu "Good morning."
#             y "Since you're here, can you help me tidy up the studio?"
#             "Sumiko glances at Yuuko and leans close so she can whisper."
#             show sumiko sad_angry
#             s "We should’ve gone for that breakfast…"
#             show yuuko sad
#             "Yuuko gives her sister a sad nod, but it’s too late now. They trudge forward to help Yukari clean."
#     return
# label random_4:
#     scene street with fade
#     show mayumi at left
#     with dissolve
#     "After lunch, Mayumi walks back toward the studio when a sign makes her freeze. “Clearance Sale”?"
#     show mayumi sigh
#     "No way! ABC store is closing down?"
#     "Everything’s half-price or cheaper…"
#     "She looks at the jewelry on display. She’s had her eye on it for quite some time, but it was always too expensive before."
#     show mayumi
#     "True, her lunch break isn’t long enough for a shopping spree, but…"
#     "A chance like this will probably never come again."
#     menu:
#         "Go in and browse":
#             "She can’t let an opportunity like this go to waste. Mayumi rushes inside."
#             show mayumi laugh_eyes_closed
#             m "Look at that necklace! And those bangles! Wow!"
#             m "One basket won’t be enough!"
#             "One hour later…"
#             "As she leaves the store, she checks the time."
#             show mayumi worry
#             m "Oh no! I'm super late!"
#             "Clinging tightly to her purchases, Mayumi runs down the street."
#             scene studio
#             show mayumi at left
#             show yukari_f at pos_right
#             show yuuko at pos_outerright behind yukari_f
#             with dissolve
#             y "Where have you been, Mayumi? We were all waiting for you."
#             m "Um… Well…"
#             show yukari_f worry
#             yuu "What's in all those bags you’re carrying?"
#             show mayumi sad
#             m "Eheheh…"
#             "She sets down the bags and tries to look innocent."
#             y " Oh Mayumi…"
#         "Return to the office":
#             scene studio
#             show mayumi at left
#             show yukari_f at right
#             with dissolve
#             "Mayumi reluctantly returns back to the office."
#             y "Hey, did you see ABC store is going out of business?"
#             y "They’re having an epic sale!"
#             show yukari_f happy
#             y " I got this bangle for just $5!"
#             m "Aw, I should have gone in…"
#     return
# label random_5:
#     scene studio with fade
#     show yukari at left with dissolve
#     y "ABC store is having a discount on scents this week!"
#     y "Hmm… our studio doesn’t really have that “fresh” smell anymore. We could use a nice air freshener. What kind, though?"
#     y "Grapefruit's obviously the best choice, but I wonder if the others will think so…"
#     "She racks her brain, but although she’s sure the topic of favorite scents has come up at least with Mayumi, she can’t remember what any of her team members like."
#     y "Oh well. I'm paying, so nobody should have a problem with what I pick."
#     menu:
#         "Tropical Grapefruit air freshener":
#             show yukari happy
#             "Ahhh… Grapefruit's so refreshing! No one has complained, so I’m glad I picked it."

#         "Ocean Breeze air freshener":
#             show shunsuke at right
#             hide yukari
#             show mayumi at left
#             with dissolve
#             ss "Hmm, the office smells pretty good today."
#             m "You noticed, too? I thought it was just me! Feels like I'm on the beach."
#             "The two of them smile as they head to their desks. Mayumi is even more upbeat than usual and Shunsuke seems more relaxed. The air freshener is a hit!"
#         "Classic Rosemary air freshener":
#             hide yukari
#             show yuuko_f at left
#             show sumiko at right
#             with dissolve
#             s "Hmm?"
#             s "This scent, it’s so…"
#             yuu "Familiar."
#             s "It makes me feel at peace."
#             yuu "Kind of reminds me of a garden we used to play in. Do you remember?"
#             "The sisters reminisce as they sit at their desks, but it doesn’t take away from their work. Instead, both seem more at ease and inspired."
#             "A fresher atmosphere in the studio is just what they needed."
#     return

# label random_6:
#  scene street with fade
#  show shunsuke_f at left with dissolve
#  "Shunsuke is deep in thought as he walks to the meeting with the advertising company. He doesn’t even notice the stranger near him on the street until the man bumps into him."
#  show shunsuke_f angry
#  ss "Watch where you're goi-"
#  "The stranger rushes past without a word."
#  ss "Huh. Someone’s in a hurry…"
#  office_l "Help! That man stole my purse!"
#  show shunsuke_f worry
#  ss "Wait a second, where's my phone?!"
#  menu:
#     "Chase the thief":
#         show shunsuke_f angry
#         ss "No way am I letting him get away like that!"
#         "Shunsuke dashes after the thief. Although the man is fast, Shunsuke is faster. The distance between them shrinks, and finally he tackles him to the ground."
#         ss "You're not getting away!"
#         "He pins the man until the woman gets in touch with the authorities. Once the thief has been taken into custody and the stolen items returned, the woman smiles at Shunsuke."
#         office_l "Thank you so much! The police would never have gotten here in time!"
#         show shunsuke_f happy
#         ss "Thank you, Miss. I'm glad to have been of service."
#         ss "I have to go for a meeting now. Thanks again!"

#     "Ask the lady to call the police":
#         office_l "Is this the police? We've just been robbed!"
#         ss "Yes, right along ABC Street."
#         police_o "We'll send the nearest patrol to your location."
#         ss "My phone has information saved on it that I planned to use at the meeting…"
#         ss "How can I go to the meeting if I don’t have my phone?"
#         "One hour later…"
#         police_o " I'm sorry. We have yet to apprehend the culprit. Please give us your contact details, and we will inform you as soon as we make progress."
#         show shunsuke_f sad
#         ss "No way!"
#         "He looks at the clock."
#         ss "Not only do I not have my phone, but I’m going to be late for the meeting."
#         office_l "Oh no… my purse…"
#         ss "This will be hard to explain to Yukari…"
# return
# label random_7:
#     scene cafe with fade
#     show yukari at left
#     show mayumi_f at right
#     with dissolve
#     y "So I was thinking we can improve the studio’s atmosphere if we--"
#     "A little boy suddenly pops up beside them. He climbs into the seat next to Mayumi."
#     m "Hi there. Where did you come from?"
#     show yukari tsundere
#     y "Ugh, not now. We have important things to discuss. Hey kid, shoo! Go bother your mommy."
#     show mayumi_f sigh
#     m "Come on, Yukari, have a heart. I know you’re stressed out--"
#     y "And this kid isn’t helping."
#     menu:
#         "Get the child to leave":
#             show yukari sigh
#             y "We're having an important talk."
#             y "Boy, go and find your parents!"
#             "The little boy was stunned by her raising her voice and hurried away. In the process, he slipped on the just-mopped floor and burst into tears."
#             show mayumi_f sad
#             m "Yukari, that wasn’t nice."
#             y "I didn’t know he’d fall. Besides, he’s not our problem. So as I was saying, I think--"
#             "The boy continues to cry, and then a woman enters the café. She looks frantic."
#             "Uwahh! Mommy!"
#             mother "Takumi! There you are!"
#             mother " I've been looking for you for so long! Are you all right? What happened?"
#             show yukari sad
#             m "Oh no, he was lost?"
#             "Aw man, now I feel bad..."
#         "Entertain the child":
#             show mayumi_f happy
#             m "Here here, Onee-san will play with you!"
#             show yukari
#             y "Yukari rolls her eyes, but doesn’t object. The little boy rushes to Mayumi and plays with the frills on her shirt."
#             y "Seems like you're a natural with kids."
#             m "I like kids. I often babysit my neighbors’ children."
#             "Just then, the door to the café opens, and a woman enters. She looks frantic."
#             mother "Takumi?"
#             "She spots them and hurries over to their table."
#             mother "Oh, thank you two so much for taking care of Takumi!"
#             mother "I've been looking all over for him."
#             mother "Say thank you to the nice ladies."
#             boy "Thank you Onee-san!"
#             show mayumi_f laugh_eyes_closed
#             m "Aw, isn't he cute?"
#             show yukari happy
#             y "Yukari rolls her eyes again, but smiles. She’s glad she didn’t chase the kid away after all."
#     return



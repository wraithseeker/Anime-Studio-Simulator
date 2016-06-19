define fourth_w = Character('Fourth Place Winner', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define manager = Character('Manager', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define office_l = Character('Office Lady', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define police_o = Character('Police Officer', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define mother = Character("Boy's Mother", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define boy = Character("Little boy", color="#000",ctc="ctc_fixed",ctc_position="fixed")

label rande_1:
    scene street with fade
    show yukari at left with dissolve
    "I wonder what all the commotion is about?"
    "She squeezes through the crowd and reaches the arcade. They’re holding a “Dance Revolution” competition."
    y "Wow, those people warming up are really good."
    show yukari happy
    y "Wait a minute… Isn't that the ultra-rare Miku figurine?! And it’s only Fourth Prize?"
    y "Hmm, it looks like registration is still open…"
    show yukari worry
    "She hasn’t played in a long time, and she knows she doesn’t stand a chance against the major competitors. Fourth place, though, might be feasible."
    menu:
        "Register for the competition":
            "Yukari enters the competition."
            show yukari sigh
            y "Oh gosh, I haven't played this in forever!"
            y "What was I thinking?"
            y "Forget fourth place, I guess I'll have to settle for being the comic relief."

        "Cheer on the competitors":
            show yukari happy
            "It’s been too long since she played. Yukari stays with the crowd and cheers." 
            "The contestants are all fantastic. When the competition ends, she claps for the winners."
            fourth_w "Thanks for cheering me on. It really boosted my confidence!"
            fourth_w "To be honest, I don't really want this figurine I won. I'd like you to have it."
            show yukari laugh_eyes_closed
            y "No way! Really? Thank you so much!"
            y "Wow, I wasn't even cheering for him in particular…"
    return

label rande_2:
    scene cafe with fade
    show yukari at left
    show sumiko at pos_right
    show yuuko at pos_outerright
    show shunsuke at pos_middleright
    with dissolve
    show shunsuke sigh
    ss "Yukari, could you try to act more ladylike?"
    show yukari angry_mouth_closed
    y "What's your problem?!"
    ss "This isn’t how you behave at a nice café like this."
    show yuuko sigh
    yuu "Please, let’s just make our orders."
    s "This stuff happens way too often when we’re out together…"
    "Mayumi ignores her friends’ arguments and checks her texts."
    show mayumi at left
    hide yukari
    hide sumiko
    hide yuuko
    hide shunsuke
    with dissolve
    "Advertisement: 1-for-1 Gachapon! Get your tickets now!"

    m "This is too good to be true!"
    "She stares at the advertisement and decides to…"
    menu:
        "Buy some tickets":
            "When will she ever get another opportunity like this? Mayumi jumps on the deal and ends the day with 10 tickets for the price of 5."
            "Next week, she’s watching the news when they cover the story of a recent Gachapon scam."
            "Hundreds have lodged complaints about XYZ company…"
            show mayumi sad_angry
            m "What… but that’s the company I bought from! They were closing down, and…?"
            m "It was all a scam?! They cheated me? Oh no, my money…"
        "Ask her friends to buy tickets together":
            show mayumi happy at left
            show yukari_f at pos_middleright
            show shunsuke at pos_right
            with dissolve
            m "Everyone, look at this! It’s a 1-for-1 Gachapon sale! Want to get in on the deal with me?"
            show shunsuke sigh
            ss "C'mon, Mayumi , that's obviously a scam."
            show mayumi worry
            m "It is?"
            show yukari_f tsundere
            y "If it sounds too good to be true, you should always be cautious. And there’s something fishy about this deal."
            ss "Everything about it looks shady."
            show mayumi worry
            m "Yukari and Shunsuke agree on something? That’s so rare, they’re probably right."
            m "All right, I’ll trust you guys on this."
            "When news of a Gachapon scam emerges a week later, she’s glad she did."
    return
label rande_3:
    scene street with fade
    show sumiko_f laugh_eyes_closed at pos_left
    show yuuko_f at pos_farleft
    with dissolve
    s "Wow, do you smell that?"
    yuu "What is it? It's amazing…"
    manager "Hello!"
    "Sumiko and Yuuko stop. The sign behind the man announces the grand opening of a new café, and the delicious smells waft from inside the building."
    manager "We're holding a special promotion to celebrate our grand opening."
    manager "Would you like to try a sample from our breakfast menu?"
    s "Yes, please! These look mouth-watering!"
    show yuuko_f happy
    yuu "Mm, they're really delicious too!"
    manager "Come on inside. There's plenty more on the menu."
    "The two girls exchange glances. After all, they’re on their way to the studio."
    menu:
        "Head into the cafe":
            scene cafe
            show sumiko_f at left
            show yuuko at right
            with dissolve
            "A little relaxation won’t hurt. They follow the manager into the café."
            show yuuko happy
            yuu "It’s beautiful in here."
            show sumiko_f happy
            s " Look at how many things are listed on the menu!"
            manager "Let me serve you today's breakfast special."
            s "Thank you!"
            "Two hours later…"
            show yuuko
            s "That was the best breakfast I've had in a long while!"
            "Yuuko nods, and then looks at the clock on the wall."
            show yuuko worry
            yuu "We're going to be so late… I hope Yukari isn’t angry."
            show sumiko_f
            s "We’ll just tell her about the café. A tip about great food like this should make up for anything!"

        "Continue to work":
            scene studio
            show yukari happy at left
            show sumiko at pos_middleright_half
            show yuuko at pos_farright
            with dissolve
            y "Hey, you guys are here early!"
            yuu "Good morning."
            y "Since you're here, can you help me tidy up the studio?"
            "Sumiko glances at Yuuko and leans close so she can whisper."
            show sumiko sad_angry
            s "We should’ve gone for that breakfast…"
            show yuuko sad
            "Yuuko gives her sister a sad nod, but it’s too late now. They trudge forward to help Yukari clean."
label rande_4:
    scene street with fade
    show mayumi at left
    with dissolve
    "After lunch, Mayumi walks back toward the studio when a sign makes her freeze. “Clearance Sale”?"
    show mayumi sigh
    "No way! ABC store is closing down?"
    "Everything’s half-price or cheaper…"
    "She looks at the jewelry on display. She’s had her eye on it for quite some time, but it was always too expensive before."
    show mayumi
    "True, her lunch break isn’t long enough for a shopping spree, but…"
    "A chance like this will probably never come again."
    menu:
        "Go in and browse":
            "She can’t let an opportunity like this go to waste. Mayumi rushes inside."
            show mayumi laugh_eyes_closed
            m "Look at that necklace! And those bangles! Wow!"
            m "One basket won’t be enough!"
            "One hour later…"
            "As she leaves the store, she checks the time."
            show mayumi worry
            m "Oh no! I'm super late!"
            "Clinging tightly to her purchases, Mayumi runs down the street."
            scene studio
            show mayumi at left
            show yukari_f at pos_right
            show yuuko at pos_outerright behind yukari_f
            with dissolve
            y "Where have you been, Mayumi? We were all waiting for you."
            m "Um… Well…"
            show yukari_f worry
            yuu "What's in all those bags you’re carrying?"
            show mayumi sad
            m "Eheheh…"
            "She sets down the bags and tries to look innocent."
            y " Oh Mayumi…"
        "Return to the office":
            scene studio
            show mayumi at left
            show yukari_f at right
            with dissolve
            "Mayumi reluctantly returns back to the office."
            y "Hey, did you see ABC store is going out of business?"
            y "They’re having an epic sale!"
            show yukari happy
            y " I got this bangle for just $5!"
            m "Aw, I should have gone in…"

label rande_5:
    scene studio with fade
    show yukari at left with dissolve
    y "ABC store is having a discount on scents this week!"
    y "Hmm… our studio doesn’t really have that “fresh” smell anymore. We could use a nice air freshener. What kind, though?"
    y "Grapefruit's obviously the best choice, but I wonder if the others will think so…"
    "She racks her brain, but although she’s sure the topic of favorite scents has come up at least with Mayumi, she can’t remember what any of her team members like."
    y "Oh well. I'm paying, so nobody should have a problem with what I pick."
    menu:
        "Tropical Grapefruit air freshener":
            show yukari happy
            "Ahhh… Grapefruit's so refreshing! No one has complained, so I’m glad I picked it."

        "Ocean Breeze air freshener":
            show shunsuke at right
            hide yukari
            show mayumi at left
            with dissolve
            ss "Hmm, the office smells pretty good today."
            m "You noticed, too? I thought it was just me! Feels like I'm on the beach."
            "The two of them smile as they head to their desks. Mayumi is even more upbeat than usual and Shunsuke seems more relaxed. The air freshener is a hit!"
        "Classic Rosemary air freshener":
            hide yukari
            show yuuko_f at left
            show sumiko at right
            with dissolve
            s "Hmm?"
            s "This scent, it’s so…"
            yuu "Familiar."
            s "It makes me feel at peace."
            yuu "Kind of reminds me of a garden we used to play in. Do you remember?"
            "The sisters reminisce as they sit at their desks, but it doesn’t take away from their work. Instead, both seem more at ease and inspired."
            "A fresher atmosphere in the studio is just what they needed."

label rande_6:
 scene street with fade
 show shunsuke_f at left with dissolve
 "Shunsuke is deep in thought as he walks to the meeting with the advertising company. He doesn’t even notice the stranger near him on the street until the man bumps into him."
 show shunsuke_f angry
 ss "Watch where you're goi-"
 "The stranger rushes past without a word."
 ss "Huh. Someone’s in a hurry…"
 office_l "Help! That man stole my purse!"
 show shunsuke_f worry
 ss "Wait a second, where's my phone?!"
 menu:
    "Chase the thief":
        show shunsuke_f angry
        ss "No way am I letting him get away like that!"
        "Shunsuke dashes after the thief. Although the man is fast, Shunsuke is faster. The distance between them shrinks, and finally he tackles him to the ground."
        ss "You're not getting away!"
        "He pins the man until the woman gets in touch with the authorities. Once the thief has been taken into custody and the stolen items returned, the woman smiles at Shunsuke."
        office_l "Thank you so much! The police would never have gotten here in time!"
        show shunsuke_f happy
        ss "Thank you, Miss. I'm glad to have been of service."
        ss "I have to go for a meeting now. Thanks again!"

    "Ask the lady to call the police":
        office_l "Is this the police? We've just been robbed!"
        ss "Yes, right along ABC Street."
        police_o "We'll send the nearest patrol to your location."
        ss "My phone has information saved on it that I planned to use at the meeting…"
        ss "How can I go to the meeting if I don’t have my phone?"
        "One hour later…"
        police_o " I'm sorry. We have yet to apprehend the culprit. Please give us your contact details, and we will inform you as soon as we make progress."
        show shunsuke_f sad
        ss "No way!"
        "He looks at the clock."
        ss "Not only do I not have my phone, but I’m going to be late for the meeting."
        office_l "Oh no… my purse…"
        ss "This will be hard to explain to Yukari…"
label rande_7:
    scene cafe with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    y "So I was thinking we can improve the studio’s atmosphere if we--"
    "A little boy suddenly pops up beside them. He climbs into the seat next to Mayumi."
    m "Hi there. Where did you come from?"
    show yukari tsundere
    y "Ugh, not now. We have important things to discuss. Hey kid, shoo! Go bother your mommy."
    show mayumi_f sigh
    m "Come on, Yukari, have a heart. I know you’re stressed out--"
    y "And this kid isn’t helping."
    menu:
        "Get the child to leave":
            show yukari sigh
            y "We're having an important talk."
            y "Boy, go and find your parents!"
            "The little boy was stunned by her raising her voice and hurried away. In the process, he slipped on the just-mopped floor and burst into tears."
            show mayumi_f sad
            m "Yukari, that wasn’t nice."
            y "I didn’t know he’d fall. Besides, he’s not our problem. So as I was saying, I think--"
            "The boy continues to cry, and then a woman enters the café. She looks frantic."
            "Uwahh! Mommy!"
            mother "Takumi! There you are!"
            mother " I've been looking for you for so long! Are you all right? What happened?"
            show yukari sad
            m "Oh no, he was lost?"
            "Aw man, now I feel bad..."
        "Entertain the child":
            show mayumi_f happy
            m "Here here, Onee-san will play with you!"
            show yukari
            y "Yukari rolls her eyes, but doesn’t object. The little boy rushes to Mayumi and plays with the frills on her shirt."
            y "Seems like you're a natural with kids."
            m "I like kids. I often babysit my neighbors’ children."
            "Just then, the door to the café opens, and a woman enters. She looks frantic."
            mother "Takumi?"
            "She spots them and hurries over to their table."
            mother "Oh, thank you two so much for taking care of Takumi!"
            mother "I've been looking all over for him."
            mother "Say thank you to the nice ladies."
            boy "Thank you Onee-san!"
            show mayumi_f laugh_eyes_closed
            m "Aw, isn't he cute?"
            show yukari happy
            y "Yukari rolls her eyes again, but smiles. She’s glad she didn’t chase the kid away after all."



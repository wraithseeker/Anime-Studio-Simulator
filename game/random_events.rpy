
define fourth_w = Character('Fourth Place Winner', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define manager = Character('Manager', color="#000",ctc="ctc_fixed",ctc_position="fixed")
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

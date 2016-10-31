label week_9_1:
    scene studio_main with fade
    show yukari laugh_eyes_closed at left
    show yuuko at right
    with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    y "Hey Yuuko! Are you getting along well with the members from [anim_studio]?" 
    show yuuko laugh_eyes_closed
    yuu "Yes, they’re very friendly. I’ve learned a lot from them, too, especially about animating characters." 
    y "That’s great!" 
    yuu "I'm glad to be here with you as part of this team. If I was at home on vacation, I doubt I’d have learned much about animation… or made new friends." 
    show yukari
    y "It's nice to know you're enjoying yourself. What about Sumiko?"
    show yuuko
    yuu "She feels the same way." 
    show yuuko happy
    yuu "At first, it was tough for us to adapt and learn while working with [anim_studio], but we motivated each other to stick with it." 
    y "What made it so difficult?" 
    show yuuko sigh
    yuu "For me, drawing the key frames was the hardest part. It’s complicated. You need to decide each position and expression a character should have." 
    yuu "The director helped me with that. With his guidance and constant practice, I finally improved."
    show yukari surprised 
    y "Wow, so you started out working on the key frames?"
    yuu "Haha, of course not. I started out working on in-between animations before I progressed to the key frames. It’s pretty rare for someone like me to be allowed to work on key frames at all." 
    y "Really? Then why did they let you do it?" 
    "After she says it, she realizes it could be taken as an insult."
    show yukari worry
    y "Not that I doubt you or anything! I just meant, since it’s so rare—"
    show yuuko laugh_eyes_closed 
    yuu "Don’t worry, I understand. It’s because our team is [anim_studio]’s client. If I worked for them, I’d definitely only draw in-between animations for quite some time."
    yuu "As it is, our relationship with them means I was allowed to try."
    show yukari 
    y "I see, I see. So what’s your current progress?" 
    yuu "I started coloring the key frames today. Coloring them is much easier than drawing them!" 
    show yukari happy
    y "I’m glad to hear it. Keep up the good work!" 
    "Yukari gets back to work, happy to know [anim_studio] is nurturing the sisters’ talents and helping them improve, and happier still to see how relaxed and satisfied Yuuko is with the situation." 
    "Motion catches her eye, and she glances up. Mayumi is dancing in her seat." 
    scene studio_main
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show sumiko at Position(xalign=0.82,yalign=1.0)
    show shunsuke at pos_outerright
    with dissolve
    s "You seem to be in a good mood." 
    m "Hmm? Oh, I was listening to some Vocaloid songs to see if I could get some inspiration for the soundtrack of [anime.name]." 
    show mayumi laugh_eyes_closed
    m "This one’s pretty catchy. Want to hear it?" 
    s "Sure, why not?" 
    "Mayumi takes off her headphones and passes them to Sumiko, who puts them on. After a few minutes, she takes them off again." 
    s "Well, it’s all right." 
    show mayumi tsundere
    m "What do you mean, “all right”? It's amazing! Millions of people love this song. It’s even been included in live Vocaloid concerts around the world!" 
    show yukari surprised
    y "Live Vocaloid concerts?" 
    "Yukari has gone to concerts before. During live concerts, the singer performs on the stage. Vocaloid songs, however, have no singers. Users compose them by using voice banks." 
    y "How do you have a concert without a singer?"
    show mayumi
    m "They have a live band playing and the character’s image is projected onto the stage. It’s really cool! You should come to one of their concerts next time!" 
    show yukari
    y "I see. That sounds awesome."
    show shunsuke sigh
    ss "And strange. People really go to concerts for a virtual singer?"
    show sumiko laugh_eyes_closed 
    s "Take us to the concert, Mayumi, but leave him here." 
    show shunsuke
    ss "Hmph. Indeed." 
    show sumiko
    y "Speaking of music, though, didn’t you promise to let us listen to the soundtrack for [anime.name]?" 
    m "That’s right! Give me a second. I’ll unplug the headphones so everyone can hear. Yukari, I’d like your opinion on which of these songs best fits [anime.name]’s mood." 
    y "Okay." 
    if anime.category == Anime.HAREM:
        play music "music/anime/Harem/Slice of Lifey Sample.ogg" fadein 1.0 noloop
        pause 5.0
        m "Should I continue with that mood for the anime’s more serious moments, or…" 
        play music "music/anime/Mystery/Investigation Sample.ogg" fadein 1.0 noloop
        pause 5.0
        m "That one? Or…" 
        play music "music/anime/Action/Sinister and Mysterious but not that Sinister sample.ogg" fadein 1.0 noloop
        pause 5.0
        y "Hmm…" 
        menu:  
            #best choice 1st
            "The first song":
                $choice_9_1_correct()
                y "The first song. [anime.name] has a light tone throughout, so even the “serious” music should have a happy feeling." 
            "The second song":
                $choice_9_1_wrong()
                y "I like the second song better. The first one didn’t sound serious enough to me." 
            "The third song":
                $choice_9_1_wrong()
                y "Let’s try the third one. I feel like it has a good mood for the science club." 

    elif anime.category == Anime.ACTION:
        play music "music/anime/Harem/Harem Shenanigans Sample.ogg" fadein 1.0 noloop 
        pause 5.0
        m "That’s one possibility for the exciting scenes, or…" 
        play music "music/anime/Action/Actiony Tension Sample.ogg" fadein 1.0 noloop
        pause 5.0
        m "That one. I’ve also considered a tone like this." 
        play music "music/anime/Mystery/Mysterious Tension 2nd sample.ogg" fadein 1.0 noloop
        pause 5.0
        y "Hmm…" 
        menu:
           #best choice 2st
            "The first song":
                $choice_9_1_wrong()
                y "The first song really makes me feel energized. That’s what the mood should be like." 
            "The second song":
                $choice_9_1_correct()
                y "Since there’s a lot of action, let’s go with the second song. The first one sounded too happy for [anime.name]."  
            "The third song":
                $choice_9_1_wrong()
                y "The third song feels great as a theme for the conspiracy. Let’s go with that."   
    elif anime.category == Anime.MYSTERY:
        play music "music/anime/Action/Very Sinister sample.ogg" fadein 1.0 noloop
        pause 5.0
        m "We could go with this mood for the darker moments of [anime.name], or…" 
        play music "music/anime/Harem/Calm Happy Music Sample.ogg" fadein 1.0 noloop
        m "Music like this. Or maybe…" 
        play music "music/anime/Mystery/Uneasiness or Investiogation Sample.ogg" fadein 1.0 noloop
        y "Hmm…" 
        menu:
           #best choice 3rd
            "The first song":
                $choice_9_1_wrong()
                y "I like the first one. It will really drive home those dark moments."  
            "The second song":
                $choice_9_1_wrong()
                y "Well, it may not be the darkest song, but I can’t help but like the second song’s tone for [anime.name]."   
            "The third song": 
                $choice_9_1_correct()
                y "The third song is perfect. It’s ominous without being too dark for [anime.name]’s mood."   
        
    m "Okay. Thanks for your feedback."
    show sumiko laugh_eyes_closed 
    s "The music sounds great!"
    ss "Listening to this soundtrack makes much more sense than going to a concert with a virtual singer." 
    show sumiko angry_mouth_closed
    s "Mayumi, I changed my mind—drag him to the next concert to make him understand." 
    m "Sure!"
    show shunsuke sigh
    ss "Wait, don’t I get a say in this?" 
    "He and Sumiko argue a little further, but then everyone gets back to work."
    "Yukari offers Mayumi a little more input on the music throughout the day, and by the end, she’s satisfied with the current progress of the OST for [anime.name]." 
label week_9_2:
    $nextDay()
    scene studio_main with fade
    show sumiko laugh_eyes_closed at right
    show yukari at left
    with dissolve
    play music happy_music fadein 2.0 fadeout 2.0
    s "Hey Yukari, look at this!" 
    "Yukari hurries to her desk, expecting to see something about [anime.name]. Instead, there’s a blue plush toy of some sort displayed on Sumiko’s computer screen." 
    s "Isn’t it the cutest thing ever?!"
    y "It’s certainly… uh…" 
    "She stares at the fluffy doll, at a loss for words."
    show sumiko sigh 
    s "Wait, don’t tell me you’re not a fan."
    show yukari sad_angry
    y "I have no idea what it is, to be honest."
    show sumiko 
    s "Oh nothing much—just the mascot for the hottest new anime around! But hey, if you’re not a fan, that’s fine. Less competition." 
    show yukari surprised
    y "Competition?" 
    s "These toys are pretty rare. You can only get them as prizes from certain crane machines, and you know how tough it is to win those! I haven’t won yet, but I WANT ONE." 
    show yukari happy
    y "Oh, I see…" 
    s "Hey, Shunsuke!" 
    show shunsuke_f at pos_farleft
    show yukari at pos_left
    with dissolve
    ss "Yeah?" 
    "For a moment, Yukari is afraid she’s going to show him the doll, too. To her relief, she closes the window as she turns to face him." 
    s "When do we get to see our website?" 
    ss "It’s not ready yet." 
    show sumiko tsundere
    s "Huh? I thought you started working on one last week!" 
    show shunsuke_f angry
    ss "Making a website is difficult. It takes time." 
    s "Can’t we use one of those website templates you can find online?" 
    show shunsuke_f sigh
    ss "We could, but that might portray a bad image of [anime.name]. A professional-looking website will help us market [anime.name] and keep fans updated on its progress." 
    ss "Try searching for some anime websites. They look great, right?" 
    ss "I can assure you that they aren't built with those templates you mentioned. Templates don't allow as much creative freedom as companies like to have." 
    y "Shunsuke's right. I did some research on web development, and it was overwhelming." 
    show sumiko sad
    s "Aw, okay. I thought you could build a website by dragging and dropping elements on the page."
    show shunsuke_f 
    ss "You're not entirely wrong. It’s possible to build a website using drag and drop, but that wouldn’t be a good fit for [anime.name] since our webpage’s layout will be more complex."
    show sumiko 
    m "Does it have to be complex? Some people prefer simple websites, you know." 
    y "Hmm... Why don’t we vote on which kind of website we should make for [anime.name]?" 
    y "Better late than never." 
    ss "Fair enough." 
    "Yukari asks everyone for their opinion. Sumiko joins Shunsuke in favoring a professional website, while Mayumi thinks it’ll be better to create a website using templates for now to keep costs low." 
    "As for Yuuko, she's fine with both options." 
    y "Hmm…" 
    ss "By the way, if we want a truly professional site, we should hire someone else to do it. I’m still a beginner, after all." 
    s "Oh come on, we don’t have to go that far." 
    ss "Why don’t you decide, Yukari?" 
    y "Well, okay…" 
    "She considers the options and decides to go with a..." 
    menu:
        "Professional Website {space=15}{image=small_moneybag.png} [PROFESSIONAL_WEBSITE_VALUE]":
            $choice_9_2_1()
            ss "Excellent decision. Since we’re an unknown studio, we want everything about [anime.name] to be as professional as possible. I’ll look into hiring someone to make our website."
            $website_choice = "Professional" 
        "Website made by Shunsuke {space=15}{image=small_moneybag.png} [SHUNSUKE_WEBSITE_VALUE]":
            $choice_9_2_2()
            ss "Thank you for your confidence in my skills. I hope I can live up to it. I’ll get back to work, then."
            $website_choice = "Shunsuke"
        "Free Website":
            $choice_9_2_3()
            ss "Since we have limited funds to work with, I suppose we shouldn’t spend too much on the website. I’ll look online for a suitable template." 
            $website_choice = "Free"
    show yukari happy
    y "Thanks, Shunsuke!" 
    "With their plan for the website decided, everyone gets back to work. Yukari contacts Sumiko’s friends to check on their progress."
    "To her delight, they’re almost done with their work on the first episode already, and they ask if they can meet with her the next morning about it." 
    "For once, everything is going well."
    $rd_e_holder.emptyList(rd_e_holder.wk_6_to_8)
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10])
    call expression random_game_event from _call_expression_14
label week_9_3:
    $nextDay()
    scene black with fade
    "Yukari meets up with Sumiko’s friends in the morning and they head to [anim_studio] together."
    "There, she’s relieved to find everything in order. The animation work for Episode One of [anime.name] is complete." 
    scene studio_main with fade
    show yukari laugh_eyes_closed at left
    show mayumi_f at right
    with dissolve
    y "Mayumi! Come take a look at the completed animation work for Episode One. It’s so cool!" 
    m "Oh, it's finished already? Let me have a look." 
    "Yukari shows Mayumi a few sections of the animation. She can barely contain her happiness, but it’s nothing compared to Mayumi, who jumps up and down in excitement." 
    m "It’s so surreal to see our characters come to life. Sumiko! Yuuko!" 
    show yukari happy at pos_left
    show sumiko at pos_textbox_right
    show yuuko at pos_outerright behind sumiko
    hide mayumi_f
    show mayumi at pos_farleft behind yukari
    with dissolve
    s "What is it?" 
    show mayumi laugh_eyes_closed
    m "Come see, come see!" 
    yuu "Is something wrong?" 
    m "Yukari brought the animation files for Episode One!" 
    "As the sisters hurry to Yukari’s desk, a puzzled Shunsuke joins the group."
    show shunsuke at pos_middleright
    with dissolve 
    ss "What’s all the commotion about?" 
    m "Take a look!" 
    "Yukari shows them all a few sections of Episode One’s animation." 
    show sumiko happy
    s "Wow!" 
    show yuuko laugh_eyes_closed
    yuu "These animations are much better than the previous ones." 
    ss "Very nice." 
    show yukari laugh_eyes_closed
    y "We owe it to your friends, Sumiko. They totally smashed my expectations." 
    y "Not only were they efficient, but they were also able to match our anime’s art style within a short period of time." 
    s "I told you they’d be great, didn’t I?" 
    y "Still, I expected some hiccups along the way, but it went so smoothly." 
    s "When we worked on our manga together, my friends were great. That’s why I recommended them." 
    y "Yeah, I'm really grateful to them." 
    ss "I’d say this puts us in a good position, doesn’t it?" 
    show yukari
    y "Yep! We can probably finish the remaining animation work within two weeks at our current pace. After that we can start filming!" 
    show shunsuke surprised
    ss "Filming?" 
    y "In other words, editing and digitizing the frames on the computer." 
    y  "After that, it’ll be time for post-production editing: adding the music, advertisements, and so on. We’re almost there, guys! The end is in sight!" 
    show mayumi sigh
    show shunsuke
    scene studio_main
    show yukari at left
    show mayumi_f at right
    with dissolve
    m "I’m glad we’re doing so well, Yukari, but aren’t you forgetting something?" 
    show yukari worry
    y "I am?" 
    m "You mean you don't remember? My goodness." 
    y "Huh?" 
    m "It’s Wednesday…" 
    show yukari surprised
    y "Wednesday… oh!" 
    "In all her excitement about the animations, Yukari almost forgot the next recording session was scheduled for today." 
    show yukari
    y "I'll get my things ready and head to the studio right now. Thanks for reminding me!" 
    m "Any time." 
    "Sorry. I’ll be singing in today’s recording session." 
    scene recording_studio with fade
    show yukari at left 
    show va_dir at right
    with dissolve
    play music cafe_music fadein 2.0 fadeout 2.0
    "Yukari can’t help but feel nervous when she arrives at the recording studio."
    "They’re almost done with the recording for [anime.name]. If anything goes wrong today, it will be a major setback." 
    va_dir "Oh good, you’re here early. Here are the lyrics for the opening and ending themes."
    "If there’s anything you think should be changed, let me know now. We’ll start recording as soon as you’re ready." 
    y "All right." 
    "She takes the pages from him and looks them over. It feels surreal to read lyrics written for [anime.name]." 
    "She’s read anime theme songs many times before, but always as a consumer. Still, everyone is counting on her, so she’ll do her best."
    if anime.category == Anime.HAREM:
        "Both songs seem to be written from the protagonist’s point of view, with the same lighthearted tone used throughout the show." 
        hide va_dir
        show va_a laugh_eyes_closed at right
        with dissolve
        va_a_char "Aren’t they great?" 
        y "Oh, I didn’t see you there!"
        show va_a 
        va_a_char "Sorry. I’ll be singing in today’s recording session." 
        show yukari happy
        y "Wow, really?" 
        va_a_char "I’m new to voice acting, but I’ve had some success with a small pop group in my free time. When the director found out, he asked me if I’d be willing to sing for [anime.name]."
        y "That’s really cool." 
        va_a_char "If [anime.name] is a hit, this could help give my group exposure, too." 
        y "I hope so! Well, I’m ready to begin if you are." 
    elif anime.category == Anime.ACTION:
        "From the lyrics alone, she can’t quite imagine the beat, but it certainly looks like it should be fast-paced music perfect for an action anime."
        "She turns to tell the director she’s ready and collides with someone." 
        hide va_dir
        show va_c at right
        with dissolve
        va_c_char "……" 
        show yukari worry
        y "Ack! I’m sorry!" 
        va_c_char "No need to apologize. It was my fault." 
        show yukari
        y "I didn’t expect to see you today. Aren’t we done recording lines for [anime.name]?" 
        va_c_char "Indeed. I’ve come to perform the opening and ending themes." 
        y "Perform?" 
        va_c_char "You were just reading the lyrics." 
        show yukari surprised
        y "You… sing…?" 
        va_c_char "Indeed, though it may surprise you, I’m capable of many tasks." 
        show yukari
        y "I didn’t mean… Uh… Maybe we should get started…" 
    elif anime.category == Anime.MYSTERY:
        "The lyrics focus more on symbolism than a literal interpretation of [anime.name], but that does give them a more mysterious tone." 
        y "I wonder how the singer handles them."
        hide va_dir
        show va_b at right
        with dissolve
        va_b_char "The opening has a soft, wistful feeling at first, but it becomes sharper near the song’s climax. The ending theme is faster all the way through." 
        y "Oh, hello!" 
        va_b_char "Sorry. I didn’t mean to interrupt. I’ll be singing the lyrics." 
        y "I didn’t know you sang." 
        show va_b laugh_eyes_closed
        va_b_char "I’m so excited! You know how the opening starts with the image of a moonlight-shrouded mountaintop? I climbed a mountain during the last full moon to get into the right mood." 
        y "Did it help?" 
        va_b_char "Oh yes! I understand the heart of the lyrics much better now." 
        y "I see."
        show va_b
        "She doesn’t actually see, but she decides it’s better not to press for a deeper explanation." 
        y "If you’re ready, let’s get started."
    scene recording_studio
    show yukari at left
    show va_dir at right
    with dissolve
    va_dir "Before we begin, I was looking through the audio files again, and there’s a concern we need to address." 
    show yukari worry
    y "What is it?" 
    "Her heart pounds. She doesn’t want anything to go wrong today." 
    va_dir "The opening song is 2 minutes long. The ending song is about 1 minute and 30 seconds long."
    va_dir "Judging by the previous recording sessions and the typical commercial breaks, your episodes will go over their allotted time by about 30 seconds if something isn’t cut." 
    y "We don’t want that, and we can’t cut out time from the episodes themselves." 
    menu:
        "Shorten the OP":
            y "Let’s cut 30 seconds from the opening. It’s a little too long, and we don’t want viewers to have to wait too long for the episode to start." 
        "Shorten the ED":
            y "Some people don’t even listen to ending themes. We can afford to make it 30 seconds shorter." 
        "Shorten both": 
            y "Let’s shorten each song by a little bit, instead of taking a full 30 seconds away from either one."
    show yukari
    va_dir "All right. Let’s see… if we remove the final repeat of the chorus… and change this musical interlude…" 
    "He talks quietly under his breath as he works, and then returns the lyrics to Yukari for a final approval." 
    va_dir "That should do it." 
    show yukari laugh_eyes_closed
    y "Perfect!"
    "They make the final changes to the music and head into the recording studio. Yukari holds her breath in anticipation as the musicians start recording."
    scene recording_studio
    if anime.category == Anime.HAREM:
        show va_a_f at left
    elif anime.category == Anime.ACTION:
        show va_c_f at left
    elif anime.category == Anime.MYSTERY:
        show va_b_f at left
    with dissolve
    "The opening sounds good, and when the voice actor begins singing, Yukari leans forward on the edge of her seat." 
    if anime.category == Anime.HAREM:
        "[va_a] was the perfect choice for their singer. He puts so much emotion into the lyrics, it really brings them to life, and he goes from romantic to quirky without missing a beat." 
    elif anime.category == Anime.ACTION:
        "[va_c]’s singing is intense and slightly terrifying… and she has to admit, it perfectly captures the tone of [anime.name]."
        "They couldn’t have made a better choice." 
    elif anime.category == Anime.MYSTERY:
        "[va_b]’s clear voice fills the studio. Even though Yukari already knows all about [anime.name], hearing the lyrics sung by Sakura gives her a sense of wonder and anticipation." 
    "They finish recording without any problems. She can barely contain her excitement."
    scene recording_studio
    show yukari laugh_eyes_closed at left
    show va_dir at va_pos_b
    if anime.category == Anime.HAREM:
        show va_a at va_pos_c
    elif anime.category == Anime.ACTION:
        show va_c at va_pos_c
    elif anime.category == Anime.MYSTERY:
        show va_b at va_pos_c
    with dissolve
    y "Thank you, everyone. You did a wonderful job, and it’s been great working with you." 
    if anime.category == Anime.HAREM:
        y "Thanks. And good luck with both your band and your voice acting career."
        show va_a happy
        va_a_char "Who knows, [anime.name] could be my big break!" 
        y "I hope so!" 
    elif anime.category == Anime.ACTION:
        show va_c at va_pos_c
        va_c_char "Has it?" 
        y "Y-yes!" 
        show va_c laugh_eyes_closed
        va_c_char "Hahaha, well, I look forward to watching [anime.name]." 
        show yukari happy
        y "You do? Well, thank you!" 
    elif anime.category == Anime.MYSTERY:
        show va_b at va_pos_c
        va_b_char "I hope we can work together again in the future." 
        y "That would be great."
        show va_b laugh_eyes_closed
        va_b_char "Maybe we should celebrate [anime.name]’s premiere by watching it from the office of an actual PI!" 
        y "Um, no, that’s okay…" 
        show va_b
        va_b_char "Oh. In that case, I’ll watch it on TV with everyone else." 
    scene recording_studio
    show yukari at left
    show va_dir at right
    with dissolve
    va_dir "All we need to do now is edit the voice tracks to prepare them for the show. Can you come by next Thursday to get them? " 
    y "Yes, that’s fine." 
    "She copies the current audio files to her USB drive, bids everyone farewell, and leaves the recording studio satisfied with the day’s work." 
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10])
    call expression random_game_event from _call_expression_15

label week_9_4:
    $nextDay()
    scene home with fade
    show yukari at left
    with dissolve
    stop music fadeout 2.0
    "Today is a national holiday. Yukari wonders what she should do with her free time." 
    menu:
        "Visit Grandma":
            scene grandma with fade
            y "Hello, Grandma!" 
            grandma "Yukari, it’s good to see you again. How have you been? How’s everything going?" 
            y "Great! And here, I brought something to show you." 
            "She opens her bag and takes out the assets for [anime.name] she brought along: art of the main characters and one of the storyboard drafts." 
            y "What do you think?" 
            grandma "This looks wonderful! Thank you for showing it to me." 
            y "It wouldn’t be right to not give our first investor an update." 
            grandma "Your anime is going well, then?" 
            y "Yes! We ran into a few problems, but we overcame all of them…" 
            "Hours pass as Yukari tells her grandmother all about the other team members, their difficulties and triumphs, and [anime.name] itself." 
            y "…and once we have our website ready, we’ll—wow, it’s late! Did I really talk that long? I’m sorry." 
            grandma "Don’t apologize. I love hearing about your anime. It sounds like it will be quite entertaining." 
            y "I hope so." 
            grandma "Once you know when it will air on TV, please tell me so I can watch!" 
            y "Don’t worry, Grandma, I will." 
            grandma "Are you going to make more anime after this?" 
            y "I definitely want to. If [anime.name] is a big hit, we could even expand it into a full show!" 
            grandma "I wish you the best of success." 
            y "Aw, thanks." 
            "They eat dinner together, and Yukari returns home feeling happier than ever about [anime.name]."
        "Ask Mayumi out for shopping":
            "She decides to call up Mayumi." 
            m "Hello?" 
            y "Hi, it’s me. Feel like shopping?" 
            m "Always! I’ll be ready in 10 minutes." 
            y "Great!" 
            scene street with fade
            show yukari at left
            show mayumi_f surprised at right
            with dissolve
            m "Y-Yukari! I can’t believe you bought so much stuff."
            show yukari tsundere
            y "You didn’t exactly save your money either."
            show mayumi_f sigh 
            m "At least I didn’t… spend… it… all…?"
            show yukari
            y "Mayumi?" 
            show mayumi_f laugh_eyes_closed
            m "Look at those figurines! They’re the cutest things I’ve ever seen! I want one. I need one!"
            show yukari sigh 
            y "So much for not spending it all." 
            "They both go home having spent more than they expected to, but at least it was a fun day." 
        "Sleepover with Mayumi and the sisters":
            "She calls Mayumi first." 
            m "Hello?" 
            y "Hi, it’s me. Wasn’t it fun when we stayed all night in the studio?" 
            m "…If you want us to work overtime on the holiday, just say so." 
            y "No, no, that’s not it! Actually, I thought maybe we could all have a sleepover again, just for fun this time." 
            m "Oh, okay! I’d love to." 
            y "Yay! I’ll ask Sumiko and Yuuko. Should we have it at my place?" 
            m "Sounds good to me." 
            "Yukari calls the sisters next, and they agree it sounds like a good idea. That evening, they all meet at her house for a sleepover." 
            scene home_night with fade
            show yukari sigh at pos_left
            show mayumi at pos_farleft behind yukari
            show sumiko at pos_textbox_right
            show yuuko at pos_outerright
            with dissolve
            y "Yuuko, that’s not… work… you have with you, is it?" 
            show yuuko laugh_eyes_closed
            yuu "Huh? Oh, no, haha! This is my personal sketchbook. I like having it with me." 
            show yukari
            show yuuko
            m "I’m more concerned about what Sumiko brought. Don’t tell me it’s another collection of awful movies." 
            s "It is." 
            show mayumi sad_angry
            m "I asked you not to—" 
            show sumiko laugh_eyes_closed
            s "I’m telling you, it’s fun to watch bad movies!" 
            show yukari happy
            y "I picked out some movies we can watch, too. Come on, we’ll work it out while the popcorn’s getting ready." 
            "In the end, they alternate between Yukari and Sumiko’s movie choices."
            "They stay up past midnight, and then Yukari reminds everyone that they need to be at the studio the next morning."
            "As they settle down to sleep, she thinks about how fortunate she is to have such good friends."   
     
label week_9_5:
    $nextDay()
    scene studio_main with fade
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    show sumiko at va_pos_c
    show yuuko at pos_outerright
    with dissolve
    play music restaurant_music fadein 2.0 fadeout 2.0
    ss "We completed the voice recordings for [anime.name] on Wednesday right?" 
    y "That's right. Once they edit the audio, they’ll send us the completed voice tracks." 
    ss "How did it go?" 
    y "Good, but it was difficult to decide if the voice actors were in character. I also had to make some decisions about our OP and ED songs." 
    show yukari sigh
    y "I wish you could have been there with me." 
    s "So do I. It sounded like so much fun when Mayumi described it to me." 
    yuu "Sadly, we’re still busy." 
    show sumiko sad_angry
    s "Yeah, filming is more difficult than I thought. Actually, we won’t be able to meet up at the restaurant tonight, either." 
    show yukari surprised
    y "What? You can’t come to dinner?" 
    show yuuko sigh
    yuu "I wish we could… but we want to finish coloring the animation frames."
    show yuuko surprised 
    show shunsuke_f surprised
    ss "Wait, are you guys handling [anime.name]’s filming by yourself? I thought it was pretty difficult and you’d need a whole team working on it with specialized software!" 
    show sumiko happy
    s "Ah, don’t worry, [anim_studio] is processing the animations and all the other hard stuff. We just need to paint the animation frames." 
    show shunsuke_f
    show yukari sad
    y "I’m sorry you have so much work to do…" 
    show sumiko laugh_eyes_closed
    s "Don't worry about it, we enjoy doing this. Besides, it’s just one week." 
    show yuuko
    yuu "That’s right. We’ll be there for dinner next time." 
    y "Well, if you say so." 
    "Nevertheless, as everyone gets back to work, Yukari can’t stop thinking about what they said."
    "Throughout the entire process, Sumiko and Yuuko have had to work more than the others. Overtime, extra sessions… now they even need to skip the weekly get-together." 
    "It bothers her for the rest of the day." 
    scene restaurant with fade
    show yukari sigh at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    y "It sure feels strange, meeting up without Sumiko and Yuuko." 
    ss "I know. It doesn’t seem right." 
    show mayumi worry
    m "They really have a lot to do, don’t they? I feel like they’ve put more work into [anime.name] than any of us." 
    y "Art requires a lot of time and effort. Add in their contribution to the animation work, and you’re absolutely right." 
    ss "If I had any artistic skills, I’d offer to help them." 
    m "Me too." 
    show yukari laugh_eyes_closed
    y "I know! Maybe we don’t have the skills to lighten their workload, but we could still do something to show our appreciation for all they do." 
    show mayumi
    m "Like what?" 
    y "Why don’t we get them a gift?" 
    show mayumi happy
    m "That’s a great idea!" 
    ss "We can go shopping over the weekend and present it to them on Monday." 
    y "Let’s do it!" 
    "As they eat, they finalize their shopping plans. The conversation makes Yukari feel better about the sisters not being able to join them for dinner." 

label week_9_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "When the weekend arrives, Yukari tries to decide the best use of her time." 
    menu:

        "Shop for a gift for the sisters":
            $choicewe_9_1_1()
            "That’s right, she promised Mayumi and Shunsuke they’d buy a gift for Sumiko and Yuuko! Yukari gets ready and heads out to meet them."
            scene street with fade
            show yukari at left
            show mayumi_f at right
            with dissolve 
            m "Hi, Yukari!" 
            y "Hi! Is Shunsuke here yet?" 
            m "He’ll be back in a minute. He said he needed to get something important." 
            y "Hmm, I wonder what that’s all about." 
            "After a few minutes, Shunsuke appears at the corner and hurries to join them."
            scene street
            show yukari at pos_left
            show mayumi at pos_farleft behind yukari
            show shunsuke at right
            with dissolve
            ss "Sorry about that. I left my map at home, so I bought a new one." 
            show yukari sigh
            y "You bought a…"
            show mayumi surprised 
            m "…map?!" 
            ss "Yes. It shows this entire shopping area and all of the stores." 
            "He unfolds the map and holds it out to them." 
            show mayumi
            y "We come here all the time. Why would we need a map?"
            ss "So we can decide which stores to visit and efficiently plot out our course."
            show yukari 
            "Yukari exchanged a bewildered look with Mayumi, who bursts out laughing." 
            show shunsuke tsundere
            ss "What?" 
            y "We should have known you’d have some strange, methodical way to shop. Let’s take a look at this map, then."
            show shunsuke 
            "With his map as a guide, they walk from shop to shop in search of something the sisters would like."
            "However, nothing seems like a good choice. They finally stop in frustration." 
            ss "This is getting us nowhere. Let’s narrow down the type of item we want to get them first." 
            y "Maybe we could get them each a nice bracelet or necklace?" 
            m "No… I was talking to them about jewelry once, and neither of them is a big fan of wearing accessories." 
            y "Darn…" 
            ss "If only we had an idea of what they’d like." 
            y "Wait a minute! The other day, Sumiko was talking about anime, and she mentioned a plush toy she wants. It’s a rare prize found in certain crane machines." 
            "Shunsuke pulls out his map again and points to a store." 
            ss "This shop had a crane machine. Do you think it’s there?" 
            show mayumi laugh_eyes_closed
            m "It’s worth a try!" 
            "They head to the shop in question and peer into the crane machine. It’s filled with all sorts of toys, some anime-themed and others not." 
            show yukari happy
            y "There! Those fluffy blue things! That’s what Sumiko told me about." 
            "She points. Mayumi clasps her hands together and bounces in place." 
            m "Those? Yuuko was telling me about them, too!" 
            ss "That settles it, then. We need to win at least one of them." 
            "Yukari pays to use the machine first. She stares at the toy and carefully positions the claw over it."
            "However, although the claw clasps the edge of the doll’s arm, it loses its grip and returns empty." 
            y "Darn it!" 
            show mayumi
            m "My turn!" 
            "She tries next, eyes narrowed in concentration." 
            ss "A little more to the left." 
            show yukari sad_angry
            y "What? She’ll miss it entirely if she does that." 
            "Mayumi gets the crane into position and lowers it, but again, the toy slips away before she can pull it up."
            show yukari sad 
            y "Aw man. Maybe I should try again. " 
            ss "Excuse me. I happen to be highly skilled at crane games." 
            show yukari surprised
            y "I-is it even possible to be good at these?!" 
            show shunsuke laugh_eyes_closed
            ss "Watch and learn." 
            show yukari
            "He steps up to the machine. They watch in bafflement as he steers the claw toward the left of the doll, rather than above it."
            "The claws close over nothing but air, although they knock the doll to a lower level." 
            y "Let me—" 
            show shunsuke
            ss "I’m not finished." 
            "He pays to try the game again without a pause. Yukari steps close to Mayumi and lowers her voice to a whisper." 
            y "How long should we let him try?" 
            m "It’s his money. If he wants to keep playing, does it matter?" 
            y "Yes, because we’ll need to think of an alternate gift idea." 
            m "Oh…" 
            "Behind them, Yukari hears the sound of the crane returning to its original position."
            "She glances back. Still nothing. And Shunsuke is putting more money into the machine." 
            "She turns back to Mayumi." 
            y "Maybe we could get them each a new sketchbook." 
            m "Not a bad idea. I wish we could make the gift more personal, though." 
            y "Yeah. Anyone can buy a sketchbook…" 
            ss "Ahem." 
            "They turn. He holds out two of the fluffy plush toys." 
            show mayumi surprised
            show yukari surprised
            m "Ehhh?!" 
            y "TWO?!" 
            ss "One for each of them, right?" 
            m "But… but…" 
            y "How did… When I looked, you…" 
            ss "You know why these dolls are such rare prizes? They’re slender. That makes it difficult to keep them within the claw."
            ss "I used my first two games to push this one next to the other, and then I was able to pick them both up at once." 
            "They stare at him." 
            show shunsuke sigh
            ss "I told you, I’m good at crane games." 
            show yukari laugh_eyes_closed
            y "Well… I think it’s safe to say today was a success!" 
            show mayumi happy
            m "Definitely. We got presents for Sumiko and Yuuko AND learned a new strategy for crane games from a true master!" 
            y "Should we call you the Crane Master from now on?" 
            ss "Please don’t."
            "They laugh and leave the shop with the two plush dolls. Yukari is sure the sisters will love them."
            "Maybe it won’t make up for all the extra work they did, but at least they’ll know the rest of the team cares."
            $wk_9_forgot_home = False
        "Read some marketing books":
            $choicewe_9_1_2()
            "With [anime.name] almost completely, they’ll need to begin marketing in full force."
            "Yukari spends the weekend reading marketing books and taking notes on possible strategies to try." 
            $wk_9_forgot_home = True
        "Relax": 
            $choicewe_9_1_3()
            "Yukari relaxes over the weekend. Working on [anime.name] takes a lot of effort, and it’s nice to have some time to just sit back and not worry about anything."
            $wk_9_forgot_home = True
    if wk_9_forgot_home:
        scene home_night with fade
        show yukari at left with dissolve
        "At the end of the weekend, Mayumi calls her." 
        y "What’s up?" 
        m "Did you forget?"
        y "Forget what?" 
        m "We were going to buy something for Sumiko and Yuuko this weekend!" 
        show yukari sad
        y "Oh! I’m sorry. I got caught up with something else and forgot all about it… Did you go without me?" 
        m "Yes, but we couldn’t find anything." 
        y "Maybe we can try again another time, then. I’m really sorry." 
        m "It’s okay." 
        "Yukari makes a mental note to be especially nice to the sisters at work the next week, since she didn’t get them a gift like she intended."
        scene studio 
    scene studio 
    $nextWeek()
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_10_1:
    scene studio_main with fade
    show yukari at left
    with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    $wk_9_forgot_home = True
    play sound "music/sfx/phone_ringing.ogg" fadeout 1.0
    "Yukari answers her phone." 
    scene black with fade
    stop sound fadeout 1.0
    y "Hello?" 
    if anim_studio == anim_studio_expensive:
        anim_dir "Hello, Yukari. How have you been?" 
        y "I'm doing great." 
        "She's surprised by the call. The director of [anim_studio] isn't the sort of person to call up just to chat, so it must be something related to [anime.name]." 
        anim_dir "Excellent. I'm calling to ask what kind of trailer you want for [anime.name]." 
        "With all the work she's done for [anime.name], she hasn't had time to think much about the trailer."
        y "I'm not sure. Do you have any suggestions?" 
        anim_dir "There are two ways we could produce the trailer. The first possibility is to reuse important scenes from [anime.name], while the second is to create new animations tailored specifically to the trailer." 
        if anime.category == Anime.ACTION or anime.category == Anime.MYSTERY:
            if anime.category == Anime.ACTION:
                $genre_text = "Action"
            elif anime.category == Anime.MYSTERY:
                $genre_text = "Mystery"
            anim_dir "Personally, I think the second choice is better. The [genre_text] genre has had good results with custom trailers in the past." 
            y "But creating new animations means additional costs, right?" 
            anim_dir "Yes, but since you've been a great partner, we're willing to give you a discount."  
        elif anime.category == Anime.HAREM:
            anim_dir "Personally, my experience in the industry has led me to believe fans of harem anime don't usually care as much about trailer details, so reusing scenes from [anime.name] would be fine."  
        "Yukari considers the two options." 
        menu: 
            "Reuse scenes from [anime.name] for the trailer.":
                $choice_10_1_1()
                y "Let's reuse scenes from [anime.name]." 
                "With their budget, it doesn't feel right to go the more expensive route, even at a discount."
                "Besides, as long as they pick good scenes, it should still appeal to their target audience." 
                $trailer_choice = "Reuse"
            "Create new animations for the trailer. {space=15}{image=small_moneybag.png} [ANIM_STUDIO_VALUE_10_2]": 
                $choice_10_1_2()
                y "Let's create new animations for the trailer." 
                "She wants [anime.name] to be as professional as possible, and a trailer with custom animations sounds like perfect way to do that." 
                anim_dir "All right. Can you drop by the studio on Friday to discuss the trailer in more detail?" 
                $trailer_choice = "New"
        y "Sure." 
        anim_dir "I'll see you then." 
    elif anim_studio == anim_studio_cheap:
        anim_dir "Hi, Yukari. How are you?" 
        y "I'm doing well. Is something wrong?" 
        "She can't imagine why the director of [anim_studio] would call unless something important came up. She only hopes it's not another disaster." 
        anim_dir "No, nothing's wrong. I just wanted to call because we should begin work on the trailer for [anime.name] soon." 
        y "Oh!" 
        "She's been so busy working, she forgot all about the trailer." 
        anim_dir "If we use some of the important scenes from [anime.name], we should be able to put together a great trailer. Could you come by on Friday to discuss it?" 
        y "Okay, that sounds fine." 
        anim_dir "Great! See you then." 
    y "Bye." 
    "She hangs up the phone."
    scene studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    m "Important news?" 
    y "That was just the animation director calling about the trailer. They'll begin working on it at the end of the week." 
    m "Oh, I see." 
    if not wk_9_forgot_home:
        "She gives Yukari a meaningful look." 
        show mayumi_f laugh_eyes_closed
        m "Now that you're off the phone, isn't there something else you wanted to do today?"
        show yukari happy 
        y "…Oh, right!" 
        "She opens her bag and takes out the two wrapped packages, then signals Shunsuke. The three of them walk together to Sumiko and Yuuko's desks." 
        scene studio_main with fade
        show yukari at pos_left
        show sumiko surprised at pos_right
        show yuuko at Position(xalign=1.12,yalign=1.0) behind sumiko
        show shunsuke_f at Position(xalign=0.42,yalign=1.0) behind yukari
        show mayumi at pos_farleft behind yukari
        with dissolve
        s "Uh-oh, are we in trouble? Why are you all staring at us? Yuuko, what did you do?" 
        yuu "Me?!" 
        show yukari laugh_eyes_closed
        y "Haha, no one's in trouble. It's just that we realized you two have worked more on [anime.name] than anyone."
        y "Between the art and the animation, you've really been busy." 
        show sumiko
        s "I told you not to worry about it." 
        y "Well, we decided to give you something to show our appreciation." 
        "She holds out the two boxes, one for each of them."
        yuu "Aw, you didn't have to do that…" 
        show mayumi happy
        m "Open them, open them!" 
        "Sumiko tears her present open. She pulls out the plush doll and stares at it in apparent shock." 
        show sumiko happy
        s "You actually got one? For me?!" 
        "Yuuko opens hers as well and lets out a squeal of delight. She holds up the second doll." 
        show yuuko laugh_eyes_closed
        yuu "Thank you so much!" 
        s "Two?!" 
        m "We all helped, but you really should thank Shunsuke." 
        show yukari happy
        y "The Crane Master." 
        show shunsuke_f sigh
        ss "No, no, I refuse to respond to that nickname." 
        m "You should have seen him dominate that crane game! Wow!" 
        y "I hope you like them." 
        yuu "We do. I can't thank the three of you enough." 
        s "Thank you Yukari, thank you Mayumi, and thank you Mr. Crane Master." 
        ss "No!" 
        s "Hahaha, this is fantastic!" 
        show shunsuke_f
        "Yukari smiles, happy they like the presents so much. A lighthearted mood fills the studio for the rest of the day." 
    else: 
        "Yukari spends the rest of the day handling small details for [anime.name] and taking notes on ideas for the trailer."  

label week_10_2:
    $nextDay()
    scene studio_main with fade
    show yukari at pos_left
    show mayumi laugh_eyes_closed at pos_farleft behind yukari
    show sumiko at pos_textbox_right
    show shunsuke at pos_outerright
    with dissolve
    m "Okay, who wants to hear some sound effects?" 
    show sumiko happy
    s "I do!" 
    y "Ooh, the sound effects are ready?" 
    show sumiko
    m "Not all of them, but I have a sample of [anime.name]'s soundboard for you to hear." 
    s "Is there an explosion?"
    if anime.category == Anime.HAREM:
        ss "There are explosions in the script."
        s "Good! What would a science club be without things exploding?" 
        ss "That is a very alarming question." 
        m "How's this?" 
        play sound "music/sfx/anime/harem/flask_explosion.ogg" 
        show sumiko laugh_eyes_closed
        s "I like it." 
    elif anime.category == Anime.ACTION:
        show yukari sigh
        y "Not every story needs explosions."
        show sumiko sad_angry
        s "But there's tons of action!" 
        m "I don't have an explosion, but I have some gunshots." 
        play sound "music/sfx/anime/action/gunshot.ogg" 
        ss "That sounds pretty good." 
    elif anime.category == Anime.MYSTERY:
        show shunsuke sigh
        ss "Where would there possibly be an explosion in [anime.name]'s story?" 
        s "Isn't there a scene where the protagonist hears a loud noise?" 
        play sound "music/sfx/anime/mystery/dropping_boxes.ogg" 
        m "That loud noise isn't an explosion, though. It's made by boxes falling on the ground." 
        ss "Much more fitting for the story." 
    show shunsuke
    show yukari
    show sumiko
    y "What other sound effects do you have ready?" 
    m "Here are two more." 
    if anime.category == Anime.HAREM:
        play sound ["music/sfx/anime/harem/mix_flask.ogg","music/sfx/anime/harem/flask_drop.ogg"] 
    elif anime.category == Anime.ACTION:
        play sound ["music/sfx/anime/action/car_engine.ogg","music/sfx/anime/action/tire screech.ogg"] 
    elif anime.category == Anime.MYSTERY:
        play sound ["music/sfx/anime/mystery/footsteps.ogg","music/sfx/anime/mystery/knife_stab.ogg"] 
    show yukari laugh_eyes_closed
    y "Sounds like things are coming together nicely." 
    show sumiko happy
    s "Nice pun!"
    show yukari
    y "Pun?" 
    s "You know… it sounds like things are coming together nicely, and we're talking about sound effects?" 
    y "Oh, uh… that was unintentional." 
    show sumiko
    ss "They sound very nice, Mayumi." 
    m "Thanks!" 
    ss "Is the audio work almost finished, then?" 
    m "Yep! Once we get the edited voice tracks from the recording studio, we'll be almost done." 
    y "And that'll be on Thursday. We're almost there, everyone! Hang in there." 
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_10_to_12])
    call expression random_game_event from _call_expression_16
label week_10_3:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    with dissolve
    y "I should get in touch with Sumiko's friends to see how they're doing." 
    "So far, their work on the in-between animation frames has been superb, but there's no reason not to ask for updates."
    "After what happened with [anim_studio], she knows it's important to stay on top of things." 
    "She contacts them, and they inform her everything is going well. They should be able to finish up their work on [anime.name] within the next two weeks."
    "That's what she expected, but hearing it directly from them makes her feel much better." 
    show yukari sigh
    y "Worrying about details and keeping track of everything… I guess that's part of what it means to be a director." 
    show yukari
    "Unfortunately, she doesn't have much else to do today, since everything's on track. Nothing is lined up on her schedule." 
    y "Maybe I should help Shunsuke with the website for [anime.name]… but I might be more of a hindrance to him." 
    "She has ideas for the website's design, but he might already have better ones. After all, he's proven himself to be a reliable member of the team. Yukari can trust him to do a good job." 
    y "Could I help Sumiko and Yuuko?" 
    "But since they're coloring the animation frames for [anime.name], she's not sure she can help. Her artistic skills leave much to be desired." 
    y "Maybe Mayumi needs my help…" 
    "Mayumi is still working on the OST and sound effects for [anime.name]. She seems to have things fairly well in hand, but additional opinions might be welcome." 
    y "I suppose I could take today off, haha. Hmm…" 
    menu: 
        "Help Mayumi":
            $choice_10_2_1()
            show mayumi_f at right with dissolve
            "Yukari walks to Mayumi's desk." 
            y "Can I help you with anything?"
            show mayumi_f laugh_eyes_closed
            m "Sure! I've been finishing up some of the songs for [anime.name]. You can give me some advice on them." 
            y "Well, I’m no expert…" 
            m "Doesn’t matter. I need you to give me your thoughts as if you’re a fan hearing the music while watching [anime.name]."
            show yukari happy 
            y "Okay!" 
            "For the rest of the day, Mayumi plays music samples for Yukari and asks for advice on the direction a particular song should take."
            "By the end, Yukari is confident she made a positive contribution to the soundtrack of [anime.name]." 
        "Help Shunsuke":
            $choice_10_2_2()
            show shunsuke at right with dissolve
            "Yukari hesitates, but decides there's no harm in at least suggesting her ideas. If Shunsuke has a better one, he'll say so. She walks to his desk." 
            ss "Yes?" 
            y "What's the status of our website?" 
            if website_choice == "Professional":
                ss "I've hired someone to make it. We've been discussing details about the site's design." 
                show yukari happy
                y "I had a few ideas." 
                ss "Let's hear them." 
                "She explains some thoughts she had on the site's layout, and they go over different options together. He writes down their final decisions to send to the site designer." 
            elif website_choice == "Shunsuke":
                ss "Take a look." 
                "He gestures to a block of code on his computer screen." 
                show yukari worry
                y "Um… so… all is well, then?" 
                ss "I've just coded a basic framework for the site so far." 
                y "What about its design?" 
                ss "I haven't made up my mind about that yet." 
                show yukari
                y "Well, I had some ideas…" 
                "They discuss various possibilities for the website's design. Shunsuke is amenable to her suggestions, although he presents his own ideas as well."
                "Once they reach agreement, he makes a note so he won't forget."
            elif website_choice == "Free": 
                ss "I've narrowed it down to a few templates. I'll show you." 
                "He turns to his computer, which has a template site open in the Internet browser. He clicks on several website templates for Yukari to get a better look."
                show yukari sad 
                y "Hmm… I had some ideas, but none of these match perfectly." 
                ss "Since we're going with a free template, that's to be expected." 
                show yukari
                "Together, they look through the templates and finally settle on one." 
                ss "Great! Now that we've picked our template, I'll be able to set it up and start adding content." 
                "Yukari is happy she was able to help with the website. She can't wait to see it when it's finished."
        "Help the sisters":
            $choice_10_2_3()
            show sumiko at pos_textbox_right
            show yuuko at pos_outerright
            with dissolve
            "Guilty over not having anything to do while Yuuko and Sumiko still have so much work ahead of them, Yukari joins them at their desks." 
            y "Hi. How's it going?" 
            yuu "Not bad." 
            show sumiko laugh_eyes_closed
            s "Great!" 
            "She takes a moment to show Yukari the latest frames they finished, and then returns to work. Yukari lingers awkwardly, uncertain what she should do." 
            yuu "Is something wrong?" 
            y "No, I just thought maybe I could help." 
            s "Want to color a frame?" 
            show yukari sad_angry
            y "Probably not a good idea. I'm not good at stuff like that." 
            s "So… you're helping in an advisory role?" 
            show yukari happy
            y "Yes! I'll advise you!" 
            "The sisters exchange glances and continue working. Yukari watches and occasionally comments on their progress, but at the end of the day, she admits to herself she didn't actually help them much at all."
            "On the other hand, she has a better appreciation for their jobs. At least it's something." 
        "Relax":
            $choice_10_2_4()
            "Yukari walks around the studio. She cleans her desk. She reads a book. At last, she gives up and settles back in her chair for a nap." 
            scene black with fade
            unknown "…ari? Yukari?" 
            scene studio_main with fade
            with hpunch
            show yukari at left
            show mayumi_f at right
            with dissolve
            "Yukari jerks awake."
            show yukari surprised
            y "Huh?" 
            m "Yukari?" 
            show yukari 
            y "I'm here!"
            m "…Were you asleep?" 
            y "I didn't have anything to do…" 
            m "Well, the day's over. It's time to go home. You must have slept for hours." 
            y "Oops…" 
            "She laughs sheepishly as Mayumi shakes her head. She'll make up for it by working extra hard the rest of the week."
     
label week_10_4:
    $nextDay()
    show black with fade 
    "On Thursday, Yukari heads to the recording studio in the morning to get the edited voice tracks for [anime.name]." 
    scene recording_studio with fade
    show yukari at left
    show va_dir at right
    with dissolve
    "It feels strange to be in the studio without [anime.name]'s voice actors there." 
    show va_dir happy
    va_dir "Ah, Yukari. The voice tracks are ready." 
    show yukari laugh_eyes_closed
    y "Great! Were there any problems?" 
    va_dir "None that I noticed, but you can preview the edited tracks before you leave, if you wish." 
    y "Okay, that sounds good."
    show yukari
    "They sit down and listen to the full tracks for both episodes. Everything sounds fine to Yukari."
    "She wished they could have finished the animation first to watch the scenes while listening to the dialogue, but she's sure it will be fine." 
    "The director gives her the audio files for both episodes." 
    va_dir "Is there anything else you need?" 
    show yukari
    y "Not as far as I know." 
    va_dir "Feel free to get in touch if anything comes up. You've been a good client to work with." 
    y "Thanks!" 
    scene studio_main with fade
    show yukari happy at left
    show mayumi_f at right
    with dissolve 
    y "I've got the audio files for [anime.name]. Want to look them over, Mayumi?" 
    m "Definitely." 
    "She sets aside her current work and goes through the audio with Yukari." 
    show mayumi_f laugh_eyes_closed
    m "This is perfect. See, Yukari? I knew you'd be fine."
    show yukari sigh 
    y "It still was stressful to handle it myself. But since everything worked out, I can't complain."  
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_10_to_12])
    call expression random_game_event from _call_expression_17 

label week_10_5: 
    $nextDay()
    scene black with fade 
    "As promised, Yukari visits the animation studio on Friday to meet with the director about the trailer." 
    if anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari at left
        with dissolve
        staff "It's good to see you again, Yukari. [anim_studio_dir] is expecting you. I'll let him know you're here." 
        y "Okay." 
        "The receptionist leaves and returns a moment later with the director." 
        show anim_dir at right with dissolve
        anim_dir "All right, let's talk about this trailer. Above all else, the trailer should be a tool to attract an audience for [anime.name]."
        anim_dir "It should be interesting and highlight [anime.name]'s strong points, without giving everything away." 
        y "Right." 
        if trailer_choice == "Reuse":
            anim_dir "I have a list of [anime.name]'s scenes, which should help us narrow it down." 
        elif trailer_choice == "New":
            anim_dir "Since we're making new animations for the trailer, we can decide exactly what to include." 
        y "I already have a few ideas of how I'd like the trailer to go." 
        show anim_dir smile
        anim_dir "Great! Let's sit down and work it out, then." 
        "They discuss various directions the trailer could take."
        "He has many suggestions to offer based on his experience in the industry and recommends a 3-act structure for the trailer to introduce the premise, show complications, and conclude with an exciting hook for [anime.name]." 
        if anime.category == Anime.HAREM:
            "Yukari decides to include a lot of humor in the trailer. It won't have all of [anime.name]'s funniest moments, but enough to make viewers laugh and highlight the humor style of everyone in the science club." 
            "The trailer will end with a short romantic moment, followed by final gag to close it out." 
        elif anime.category == Anime.ACTION: 
            "That feels like the best format to go with. Yukari decides the trailer should start with the protagonist's normal life, transition into his discovery of the conspiracy, and run through a montage of chase scenes and dangerous encounters."
            "Finally it'll end on the cliffhanger of Norio holding him hostage." 
        elif anime.category == Anime.MYSTERY:
            "A mystery makes it particularly tricky since they can't give too much away. After they debate several possibilities, Yukari decides to include only brief glimpses of the protagonist's past in the trailer and focus on the current murder." 
            "The final scene of the trailer will have him realize the mystery is far deeper than they first assumed."  
            anim_dir "Wonderful. We'll get to work on this immediately." 
        y "Great! Let me know if you need anything else." 
    elif anim_studio == anim_studio_cheap:
        scene animation_studio with fade
        show yukari at left
        with dissolve
        "Yukari looks around the empty lobby and sighs. The director asked to meet her, so hopefully he hasn't forgotten…" 
        "She waits for a while, and then walks to the door that leads deeper within the studio." 
        show anim_dir at right with hpunch
        y "Agh!" 
        anim_dir "Oops!" 
        "He opened the door right as she approached it and nearly collided with her on his way out." 
        anim_dir "Sorry about that." 
        y "It's okay. I'm here to talk about the trailer." 
        anim_dir "Right, let's go." 
        "They sit down, and he turns to her with an expectant smile." 
        anim_dir "What did you have in mind?" 
        y "Well… we want the trailer to attract fans to [anime.name]." 
        anim_dir "I recommend showing the most exciting scenes." 
        y "I don't think that's a good idea." 
        anim_dir "Really? That's how we made the trailer for our last anime." 
        "Yukari saw that trailer and knows how unsuccessful the anime was."
        "She considers mentioning that out loud, but decides to take a more polite approach instead." 
        y "I'd like to save the biggest moments for the anime itself. I've come up with a few ideas of what to include in the trailer…" 
        "She explains her thoughts on the best scenes to reuse for the trailer. After a few minutes, the director gets out a notebook and marks down the scenes she mentions." 
        if anime.category == Anime.HAREM:
            "They're going to use the introduction of the science club, a few scenes from the middle that show off [anime.name]'s sense of humor, and end with one of its strongest jokes." 
        elif anime.category == Anime.ACTION:
            "It's difficult to decide on which moments to include, but Yukari decides a strong focus on the action is good since that's what viewers will get in the anime itself." 
        elif anime.category == Anime.MYSTERY:
            "The murder investigation will be a focal point of the trailer, although they'll also use one of the brief flashback scenes and hint at the plot twists to come." 
    anim_dir "Sounds good!" 
    y "So you know what I want in the trailer?" 
    "He holds up his notebook, where he wrote every scene she mentioned. Every scene. Even the ones that came up in the context of scenes not to use, or sections she changed her mind about." 
    "Yukari holds out her hand for the notebook and crosses out all the scenes she doesn't want. She makes a few more notes until the trailer structure is clearly described." 
    y "There." 
    anim_dir "Perfect." 
    y "And please, if there's anything you're unsure about, contact me." 
    anim_dir "Don't worry, I will." 
    scene studio with fade
    show yukari laugh_eyes_closed at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    play music restaurant_music fadein 2.0 fadeout 2.0
    y "Well, we finally worked out the details for the trailer!" 
    show mayumi happy
    m "Yay!" 
    y "How are things here?" 
    s "Good, except Shunsuke is a spoilsport." 
    show shunsuke sad_angry
    ss "I am not, I just have self-restraint." 
    show sumiko tsundere
    s "Oh, so I don't have self-restraint, huh?" 
    ss "You said it, not me." 
    show shunsuke
    show yukari sigh
    "Yukari stares at them as they argue and looks around for help." 
    show yuuko sigh
    yuu "It's been like this for a while now." 
    y "What are they arguing about?" 
    yuu "I… don't remember. Mayumi, do you remember?" 
    show mayumi
    m "Hmm… It started after our lunch break. I think Sumiko accused Shunsuke of having a lousy lunch and no taste in dessert." 
    show yuuko
    yuu "But wasn't there something about shoes in there, too?" 
    m "Oh yeah, and a time travel debate…" 
    show yukari
    "Yukari claps her hands together to get Sumiko and Shunsuke's attention and interrupt the argument." 
    y "Okay, what's the problem?" 
    show sumiko sigh
    s "It's his fault."
    show yukari worry 
    y "What is?" 
    s "What we're arguing about." 
    y "Which is…?" 
    show sumiko 
    s "Um…" 
    ss "…Don't look at me." 
    show mayumi tsundere
    m "You mean you two don't remember either?" 
    show sumiko laugh_eyes_closed
    s "Nope. Oh well. No hard feelings then!"
    ss "Indeed. No hard feelings." 
    show yukari sad_angry
    y "……Seriously?" 
    "Well, at least they aren't arguing anymore."  
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    y "It's good to see everyone here this week." 
    show sumiko sigh
    s "It's good to BE here instead of spending Friday evening doing more work." 
    show yukari sad_angry
    y "What happened to 'we enjoy doing this'?" 
    show sumiko
    s "A mild stretch. We enjoy our work. Skipping the weekly dinner together, not so much." 
    show yukari
    show yuuko happy
    yuu "But you know… it's not so bad to work overtime and stay late to finish things up." 
    s "Speak for yourself."
    show mayumi surprised 
    m "What do you mean, Yuuko?" 
    show yuuko
    yuu "It may not be enjoyable, but it's taught me a lot. I've learned how I react when I'm up against deadlines, and I know how to cope with it better." 
    show mayumi
    s "It's taught me a lot, too. Namely how much I hate deadlines. From now on, I'm going to get a head start on everything!" 
    y "Deadlines can definitely be stressful, but I see Yuuko's point. I understand myself better because of the obstacles we've had to overcome." 
    show yuuko laugh_eyes_closed
    yuu "And even though it's been a struggle, I have more confidence now." 
    show yukari happy
    y "Because we DID overcome those obstacles, so we know what we're capable of." 
    show sumiko happy
    s "Sounds like making anime is a great learning experience, haha!" 
    ss "I wish I could contribute something philosophical to this conversation… but honestly, my learning has been of a more concrete nature."
    ss "I'm a better writer now. [anime.name] is my first major original project, and having people critique it and offer suggestions… and just seeing it brought to life as an anime… has helped me improve." 
    m "I'm with Shunsuke. I'd like to say I've changed as a person, but what I've really noticed is that I'm better at composing music. I'm starting to develop my own style." 
    y "Didn't you already have your own style?" 
    "She shakes her head and laughs."
    show mayumi sigh
    m "I cringe when I listen to my old stuff now. Half of it sounds like a knock-off of Madoka Magica."
    show yuuko 
    yuu "Is that your favorite?" 
    show mayumi
    m "It's one of them, and it definitely influenced my music early on. But now that I've had to compose music for specific scenes and moods, I've branched out a lot." 
    show yukari laugh_eyes_closed
    y "That's great!"
    show sumiko laugh_eyes_closed
    s "Just think… someday, a group of kids will be talking like this, and one of them will mention how [anime.name]'s OST is their favorite." 
    show mayumi happy
    m "Haha!" 
    s "I'm serious. And some silly logical writer will be there…"
    show shunsuke sad_angry 
    ss "Excuse me?" 
    s "…and he'll be like 'This is my first original story. Before, all I wrote was fanfiction for [anime.name].'"
    s "And then there'll be all the artists making [anime.name] fan art, though of course they can't draw the characters as good as Yuuko can…" 
    show yuuko sigh
    show shunsuke
    yuu "Oh, stop." 
    show sumiko
    s "I'm serious here! It's going to happen." 
    y "You might be aiming a little too high there, Sumiko… but who knows? We'll make [anime.name] the best it can be!" 
label week_10_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "When Yukari checks her email on the weekend, she finds a request from the media. A journalist who covers anime news would like to interview her." 
    "Yukari thinks it over and decides to…" 
    menu:
        "Accept the offer": 
            scene black with fade
            if choicewe_10_1_1():
                "The next day, she meets with the journalist to discuss [anime.name]. She prepared for possible questions ahead of time, and none of the questions are too tricky."
                "Yukari leaves the interview feeling satisfied with how it turned out." 
                "By evening, she has a few emails from people who already read the interview and are excited for [anime.name]."
                "It's causing a stir on a few anime forums, too. It seems like media coverage was just what they needed to give [anime.name] a nice boost in publicity." 
            else: 
                "The next day, she meets with the journalist to discuss [anime.name]. The questions aren't too bad, and Yukari handles herself well." 
                "Unfortunately, even though the interview is online by evening, it doesn't seem to attract much interest."  
          
        "Decline the offer":
            $choicewe_10_1_2()
            "An interview could have helped [anime.name]'s publicity, but Yukari isn't ready to deal with the media just yet."
            "Instead, she spends the weekend researching other potential ways to promote [anime.name] and going over their schedule to see what they still need to do before the deadline." 
    scene studio 
    $nextWeek()
    $mayumi_tasks[0] = mayumi_fifth_task
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_11_1:
    scene studio with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    stop music fadeout 2.0
    ss "There's only a few weeks left before the deadline for [anime.name]. I'm curious about what still needs to be done before it'll be ready." 
    y "There's a fair amount of work we still have to do for post-production, since our production phase just ended not long ago." 
    ss "Like what?"  
    y "To explain it in simple terms, it consists of three core components: editing, dubbing, and the final quality assurance check." 
    show shunsuke surprised
    ss "Dubbing? You can't possibly mean you're adding English voices for the characters!" 
    show yukari sigh
    y "Of course not! It's already too late to do that even if I wanted to. You're confused by the term 'dubbing.'" 
    y "In the context of post-production, dubbing means to mix the audio and music tracks into the episodes of [anime.name]." 
    y "That means we have to ensure the voice tracks are in sync with the characters' animations and that the music plays at the right time." 
    show yukari
    show shunsuke
    ss "Thank you. Now I understand what you mean. So, since you're talking about the post-production phase, does that mean we're done working with [anim_studio]?" 
    y "Not yet. They're in charge of filming [anime.name]. In fact, I'm about to go there and pick up episode one of [anime.name] right now." 
    show shunsuke happy
    ss "Nice! I can't wait to see it." 
    show yukari laugh_eyes_closed
    y "Same. I'll be back soon." 
    if anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari happy at left with dissolve
        y "Hello!" 
        staff "It's good to see you again, Yukari. Are you here to pick up the first episode of [anime.name]?" 
        y "That's right." 
        staff "I'll let [anim_studio_dir] know you're here." 
        show yukari
        "As Yukari waits for the director, she can't help but marvel at how far along [anime.name] has come." 
        show anim_dir at right with dissolve
        anim_dir "Sorry to keep you waiting." 
        y "No need to apologize. It wasn't long." 
        anim_dir "Here is the disc that contains Episode One of [anime.name]." 
        show yukari laugh_eyes_closed
        y "Great! When do you think Episode Two will be ready?" 
        show anim_dir smile
        anim_dir "It should be finished soon, most likely next week, depending on when we get the remaining animations. I'll keep you updated." 
        y "Thank you." 
        "She turns to leave with the disc, but pauses and looks back at the director."
        y "I'm thinking of holding a small celebration once [anime.name] airs. Would you and the members of [anim_studio] be interested in joining us?" 
        y "It would be great to have everyone who contributed to [anime.name] come!" 
        show anim_dir disappointed
        anim_dir "I'd love to attend, and I'm sure my co-workers would too… but I'm afraid we're currently swamped with work." 
        anim_dir "Sorry, we have to decline your invitation." 
        show yukari sad
        y "Okay, I understand. It's a pity, though." 
        show anim_dir
        anim_dir "Perhaps we'll make it after your next anime…" 
        show yukari laugh_eyes_closed
        y "Haha, I hope that day comes!" 
        show yukari
        y "Well, if there's nothing else, then I'll head back to my studio." 
        anim_dir "I'll be in touch to let you know when Episode Two is ready." 
        y "Great! See you later!" 
        anim_dir "Goodbye." 
    elif anim_studio == anim_studio_cheap:
        scene animation_studio with fade
        show yukari at left
        show anim_dir happy at right
        with dissolve
        anim_dir "Hi Yukari!"
        show yukari surprised
        y "Whoa! You scared me!" 
        "On the majority of her visits to [anim_studio], she's entered an empty lobby. She wasn't expecting to find the director waiting for her." 
        anim_dir "I knew you'll be around to pick up Episode One of [anime.name], so I thought I'd surprise you. And it worked!" 
        "He seems inordinately pleased with himself." 
        show yukari
        y "Uh-huh…"
        show anim_dir smile 
        anim_dir "Here. Episode One is on this disc. We should have Episode Two ready sometime next week, after we get the remaining animation work." 
        show yukari happy
        y "Okay, that's great! You'll let me know when it's ready?" 
        anim_dir "Yep, don't worry." 
        y "Thank you." 
        show yukari
        "She turns to leave with the disc, but pauses. Although they had some difficulties, [anim_studio] wasn't so bad to work with after all. Everything worked out in the end." 
        show yukari laugh_eyes_closed
        y "I'm thinking of holding a small celebration once [anime.name] airs. Would you and the members of [anim_studio] be interested in joining us?" 
        y "It would be great to have everyone who contributed to [anime.name] come!" 
        anim_dir "That sounds fun! One of my major rules of life is 'Never turn down a chance to party!'" 
        y "(thinking to self): Is that really the sort of thing he should tell a client?"
        show anim_dir disappointed
        anim_dir "But… unfortunately, my new financial advisor told me to put business before pleasure from now on. And since we have a lot of work piling up…"  
        anim_dir "Well, I'm afraid I'll have to decline on behalf of the studio." 
        y "It's okay. It would have been nice to have you there, but I understand." 
        show anim_dir
        anim_dir "Keep us in mind for future parties, though!" 
        y "I'll, um, do that. Well, if there's nothing else, then I'll head back to my studio." 
        anim_dir "Okay. I'll contact you when Episode Two is ready." 
        y "Great! See you then." 
        anim_dir "Bye!" 
    scene studio_main with fade
    show yukari laugh_eyes_closed at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    play music casual_music fadein 2.0 fadeout 2.0
    y "Here it is!" 
    ss "Episode One?" 
    y "Yep!" 
    show sumiko happy
    s "What? Where? I want to see it!" 
    show mayumi laugh_eyes_closed
    m "Me too! I'm nervous about how it'll be…" 
    y "Give me a minute to set it up, and then we can all watch it together!" 
    "She puts the disc into her computer. Everyone gathers around to watch the video." 
    scene first_anime with fade
    "Everyone watches with excitement and anticipation as the episode begins. After all, this is the result of their hard work over the past few months." 
    m "Oooh, it looks so good! Yukari, you did a fantastic job!" 
    y "I'm just the director. Everyone here and at [anim_studio] helped make this possible." 
    yuu "The animation looks smooth. That's a relief." 
    s "It feels really weird watching an anime and seeing backgrounds I designed. It's a good feeling, but… so surreal…" 
    ss "Just wait until it's on TV." 
    s "Oh man, that THAT will be surreal." 
    m "Look, Yuuko! It's your characters!" 
    yuu "Y-yes…" 
    y "Is something wrong?" 
    yuu "I just look at my own art and wonder if it's really good enough…" 
    s "What are you talking about? Look at it! It's great!" 
    yuu "Well…" 
    ss "She's right, Yuuko. Your art looks fine." 
    yuu "If you all think so, then… okay! I accept it." 
    m "Now that that's settled, shh… let's watch!" 
    "They watch in silence until the video reaches its end." 
    scene studio_main with fade
    show yukari laugh_eyes_closed at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    y "Well? What did you think?" 
    show mayumi laugh_eyes_closed
    m "It looks great!" 
    if anime.category == Anime.HAREM:
        show sumiko happy
        s "I love how science-y everything is." 
        ss "Is this a subtle way to praise your own backgrounds?" 
        show sumiko tsundere
        s "Hey! I mean it. Everything really came together in the right way to create the right atmosphere." 
        ss "Hmm, well, I can't argue there." 
        show sumiko
        m "I agree. And it seems so much fun, too!" 
    elif anime.category == Anime.ACTION: 
        show yuuko laugh_eyes_closed
        yuu "I'm happy to see how well the animations work in the faster-paced scenes. I was worried about that."
        show sumiko happy 
        s "Yeah, me too." 
        y "Right, I had my concerns that it might be hard to follow, but everything looked as smooth and logical as I imagined it when I set up the storyboards." 
        yuu "Seeing it in action makes me feel bad for our protagonist, though. He has to run so much!" 
        s "As long as the animation looks good while he's doing it, that's the important thing." 
        yuu "Yes." 
    elif anime.category == Anime.MYSTERY:
        ss "I'm relieved we've captured the proper tone for the story. It was a tricky balance, but we achieved it." 
        m "And didn't our detective look so cool when he investigated the crime scene?" 
        ss "He did. Credit for that goes to Yuuko and Sumiko for designing both him and the crime scene environment so well." 
        show yuuko sigh
        yuu "Aw, don't mention it…" 
        show sumiko laugh_eyes_closed
        s "It's good to know all that work paid off!"
    y "Just wait until the audio is added. Then [anime.name] will really be great!" 
    m "I can't wait!"

label week_11_2: 
    $nextDay()
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    m "The music and sound for [anime.name] is almost complete. The audio mastering shouldn't take too long, since we're storing it digitally." 
    show yukari laugh_eyes_closed
    y "That's great!" 
    ss "I have good news, too. Our website is coming along well. It should be finished before the end of the week." 
    y "Awesome. Let me know when it's ready." 
    scene studio_main
    show yukari at left
    show sumiko at pos_textbox_right
    show yuuko at pos_outerright
    with dissolve
    "As they return to their desks, Yukari checks on Sumiko and Yuuko. They're hard at work painting the final animation frames for Episode Two." 
    s "Something wrong?" 
    y "No, I just wanted to know how things are going." 
    show sumiko laugh_eyes_closed
    s "Great!" 
    yuu "Yes, everything should be finished soon." 
    y "I'm glad to hear it." 
    scene studio_main
    show yukari at left
    with dissolve
    "Back at her own desk, Yukari begins to compile all of their assets for [anime.name]." 
    show shunsuke at right with dissolve
    ss "Need a hand?" 
    y "Sure, if you have time." 
    play sound "music/sfx/phone_ringing.ogg" fadeout 1.0
    y "Just a minute." 
    hide shunsuke with dissolve
    "She steps away from the desks so she can answer the phone without disturbing anyone. The caller is one of Sumiko's friends, and she braces herself."
    stop sound fadeout 1.0
    "Any unexpected call could mean bad news. However, the news is good for a change! They've finished all of their tasks." 
    show yukari happy
    y "Good work! I'll drop by on Thursday to collect it. By the way, we're going to have a party after [anime.name] airs…" 
    "Once she tells Sumiko's friend about the party, she hangs up and returns to her desk."
    show yukari at left
    show shunsuke at right with dissolve
    ss "Something important?" 
    show yukari happy
    y "Our freelance animation work is complete!" 
    play sound "music/sfx/phone_ringing.ogg" fadeout 1.0
    show yukari surprised
    y "Another call, already?" 
    ss "Maybe they forgot something." 
    stop sound fadeout 1.0
    "But when Yukari steps away to take the call, she sees it's from their primary investor this time." 
    scene studio with fade
    show yukari at left with dissolve
    y "Hello?" 
    investor "Hello. How is everything going with [anime.name]?" 
    y "We're now at the post-production stage. [anime.name] is on track to meet its deadline." 
    investor "Excellent! Anyway, I'm calling because I have good news. Could we meet up to discuss it?" 
    y "All right. Same place as before?" 
    investor "That sounds perfect. I can be there in ten minutes." 
    "Yukari takes a moment to tell the team where she's going and then heads for the café, curious about what this good news might be." 
    scene cafe with fade
    show yukari at left
    show investor at right
    with dissolve
    "When Yukari arrives, she spots the investor seated at a table and joins him." 
    y "I hope I didn't keep you waiting." 
    investor "Not at all. Let me get right to the point. We've managed to secure a booth for [anime.name] at Anime Rising." 
    show yukari surprised
    y "Y-you did?!" 
    "Anime Rising has become quite a popular anime convention over the past few years, despite only lasting two days."
    "Yukari has attended as a guest, but never dreamed she'd have her own booth —- especially not when the convention is only a week away!" 
    show investor smile
    investor "It was pretty last-minute, but I think it's a great opportunity to showcase [anime.name]." 
    y "I… see." 
    "Her shock must show on her face, because the investor leans forward with a concerned look." 
    show investor
    investor "Is everything all right? If you can't attend the convention, that's fine." 
    show yukari
    "She hesitates. They already have a lot to do this week. Running a booth at Anime Rising means even more to prepare for. They'll be even busier, and it will be trickier than ever to keep things on schedule." 
    "On the other hand, many startup studios would need to fight for such an excellent opportunity. Extra work or not, it would be unwise to turn down the offer." 
    y "No, I was just surprised. Thank you so much! We'll definitely be there." 
    investor "In that case, I'll see you at Anime Rising." 

label week_11_3:
    $nextDay()
    scene studio with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "I have news." 
    ss "I thought you might. You seemed pretty distracted after that second phone call yesterday." 
    y "Sorry about that." 
    "After she finished talking to their investor the previous day, she spent the rest of her time at the studio getting in touch with other investors to let them know [anime.name]'s status, as well as looking up information about Anime Rising." 
    m "So what's up?" 
    show yukari
    y "Our investor got us a booth at Anime Rising."
    show sumiko surprised
    s "Whoa, really?! No joke?" 
    y "No joke." 
    show sumiko laugh_eyes_closed
    s "That's awesome!" 
    m "What's Anime Rising?" 
    y "It's a two-day convention held next Tuesday and Wednesday."
    s "Why don't you look happier about it, Yukari? It's a great opportunity for us!" 
    show yuuko happy
    yuu "Yes, it should be a very special experience." 
    show mayumi laugh_eyes_closed
    m "I agree! When will we ever get another chance like this?"
    show shunsuke worry 
    ss "It's a good opportunity, but… did you say it starts next Tuesday? We can't go in unprepared, but we don't want to fall behind on [anime.name], either…" 
    show yukari sigh
    y "Exactly why I have mixed feelings about it. I'm not sure if we have enough time to keep [anime.name] on track and prepare our materials for the booth." 
    ss "We will if we work this weekend. Unfortunately, that will be pretty stressful… Can we handle it?" 
    m "Come on, have a little more faith in us. Of course we can!" 
    show shunsuke sad_angry
    ss "It's not a question of faith. It's a valid concern that we might burn ourselves out." 
    m "We've come so far already. This isn't the first time we've had to work overtime, and now we're in the final stretch. Don't worry, Shunsuke, a little extra work isn't enough to stop us!" 
    s "Yeah!" 
    yuu "Well said. We have the resolve to do this for sure!"
    show shunsuke happy
    ss "Hmm… Now I see how far we've come."
    show yukari
    y "What do you mean?" 
    ss "At the beginning, something like this could have shattered us. But now? Everyone has the will to succeed. Don't worry, Yukari. We'll be fine." 
    show yukari laugh_eyes_closed
    y "All right, then! In that case, we should get back to work. We have a lot to do and only a limited time to do it in. Let's do this!" 
    $rd_e_holder.emptyList(rd_e_holder.wk_5_to_10)
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_10_to_12])
    call expression random_game_event from _call_expression_18
label week_11_4:
    $nextDay()
    show studio_main with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "Hey everyone." 
    show mayumi sigh
    m "You're here! We were starting to worry you were sick or something."
    y "Sorry. I went to meet Sumiko's friends this morning to get their remaining work and take it to [anim_studio]." 
    yuu "Did everything go all right?" 
    y "Yes, I just ended up running a little late." 
    show sumiko happy
    s "Well while you were gone, I had an amazing idea for the con!"
    show shunsuke sigh 
    ss "No. No she didn't." 
    if anime.category == Anime.HAREM:
        s "We should all cosplay as the characters of [anime.name]. Shunsuke can be the protagonist, and the rest of us can be the members of the science club!" 
        ss "No." 
        show sumiko tsundere
        s "Excuse me, I'm talking to Yukari. Well, what do you think?" 
        y "Ahaha… let's save the cosplaying for another time. We need to appear professional." 
    elif anime.category == Anime.ACTION:
        s "We should rent out a building near Anime Rising and fill it with props so it looks like the conspirators' hideout found in [anime.name]."
        s "Then, we lure people over there somehow, and just when they're really starting to wonder what's going on, we reveal it's all a huge promotional stunt!" 
        show yuuko sad_angry
        yuu "That really sounds like a lot of work…" 
        y "I agree. We're pressed for time as it is without attempting 'a huge promotional stunt.'" 
    elif anime.category == Anime.MYSTERY:
        s "We'll stage the crime scene from [anime.name] behind our booth to attract attention. Shunsuke can pretend to be the dead body." 
        ss "……" 
        m "Don't we have a voice actor who does stuff like this?" 
        y "It's probably best if we don't do anything too crazy at our first convention."
    show sumiko sad
    show yuuko
    show shunsuke
    s "Aw…" 
    scene studio_main with dissolve
    "With Yukari back, everyone returns to work after a few minutes."
    "Soon, a serious atmosphere descends over the studio. [anime.name] might be almost complete, but with Anime Rising less than a week away, they need to work extra hard." 
    "When the time for their usual lunch break arrives, no one gets up." 
    show yukari worry at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "…Guys? It's time for lunch." 
    m "Oh, is it?" 
    yuu "I thought I'd skip lunch today and keep working." 
    s "I filled my pockets with energy bars." 
    "Sure enough, she pulls a handful of wrapped energy bars from each pocket." 
    ss "Since we have so much work to do, we shouldn't spend too much time on lunch. Maybe a shorter break than usual is in order." 
    show yukari
    "Yukari stares at them. Their devotion is admirable, but skipping or rushing lunch is a good way for them to burn themselves out or get sick." 
    show yukari laugh_eyes_closed
    y "I have an idea. How about I order us a pizza? That way we can eat right here in the studio and work at the same time." 
    show mayumi happy
    m "That's a great idea!" 
    "Everyone else agrees, so Yukari quickly looks up the phone number of the closest pizza place and dials." 
    y "Hi, I'd like to order one large pizza with teriyaki chicken…" 
    show sumiko tsundere
    s "One? That's not even two slices for everyone!" 
    y "Sorry, I'd like to order two large pizzas…"
    m "Potato and mayonnaise, please!" 
    show shunsuke worry
    ss "Not on mine. I'd like a triple cheese pizza, with no sauce."
    s "No sauce? What kind of maniac are you? I'd like traditional Italian toppings: tomato sauce, cheese, and pepperoni." 
    yuu "Could I have mine with onions, pepperoni, and jalapeno peppers, please?" 
    show mayumi sad_angry
    m "Waaah! Don't let Yuuko's toppings get near my pizza!"
    show yukari sigh
    "Yukari takes a moment to try to sort through everything they just said, and takes a deep breath before returning her attention to the phone." 
    y "Sorry for the delay. Okay, two large pizzas. One should be divided into three types: potato and mayonnaise, triple cheese without sauce, and tomato sauce with cheese and pepperoni. The other—" 
    show sumiko sad_angry
    s "Wait a minute. Does that mean we have to split a pizza three ways, while you and Yuuko get the second one? Not fair!" 
    show shunsuke
    ss "Let's look at this logically. Pizzas are traditionally cut into eight slices. With two pizzas, that means we have 16 slices. There are five of us. Everyone gets three slices, and there will be one extra." 
    y "…I'd like to order two large pizzas. That's 16 slices, right?"
    y "Okay, three slices with teriyaki chicken, three with potato and mayonnaise, three with triple cheese and no sauce, three with tomato sauce, cheese and pepperoni, and three with onions, pepperoni, and jalapeno peppers." 
    m "Make sure they know to keep mine away from the spicy one." 
    show yukari
    y "The potato and jalapeno orders have to be on separate pizzas."
    ss "Don't forget about the extra slice. Maybe it should be whoever's order is split across pizzas." 
    y "Okay, when you decide which topping to put on both pizzas, we'd like four slices of that kind." 
    show sumiko
    s "That reminds me, I'd like my pizza to be separate from Yuuko's, too. That jalapeno flavor gets into everything." 
    y "Keep the tomato and cheese pizza with the potato—" 
    show mayumi worry
    m "Wait! Is there pepperoni on Sumiko's? I don't want any pepperoni near mine, please!" 
    show yukari sigh
    y "…………I'd like to order 5 small pizzas." 
label week_11_5:
    $nextDay()
    scene studio_main with fade
    show yukari worry at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke laugh_eyes_closed at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music cafe_music fadein 2.0 fadeout 2.0
    ss "Gather round, everyone. The time has come!" 
    m "Melodrama from Shunsuke? This must be important." 
    ss "I'm ready to unveil the website for [anime.name]."
    show yukari happy 
    y "Oh!" 
    "Everyone gathers around his computer to see." 
    if website_choice == "Professional":
        show mayumi surprised
        m "Whoa, it looks so… so…" 
        yuu "Professional." 
        show mayumi happy
        m "Yes!" 
        ss "Well it better, since we paid good money to have a professional design it." 
        "The website is sleek, with different pages for news, a description of their studio, the story and characters of [anime.name], and a contact form."
        " Best of all, everything from the background to the text itself shares [anime.name]'s style." 
    elif website_choice == "Shunsuke": 
        show sumiko surprised
        s "Wow, you made this yourself?" 
        ss "Yes." 
        show sumiko laugh_eyes_closed
        s "That's incredible!" 
        ss "Ahaha… thank you." 
        "Although it has a fairly simple appearance, with the characters of [anime.name] arranged at the top of the screen by the logo and a plain background behind everything else, it gets the job done."
        "Links next to the logo scroll the page down to explanations about the story, the characters, and the studio itself, along with a section for news updates." 
    elif website_choice == "Free": 
        y "Great job, Shunsuke."
        ss "Well, I didn't do too much. It's a template, after all…" 
        "The website has a basic blog format, with an introduction to [anime.name] as the first post. Other pages describe the story and characters and tell viewers about the studio."
        "It's fairly bare-bones, but it contains the information a potential viewer of [anime.name] needs." 

    if guerilla_marketing:
        "Social media icons in the corner lead to [anime.name]'s social pages." 
    ss "So, is this suitable?"
    show yukari laugh_eyes_closed
    show sumiko
    show mayumi
    y "Definitely." 
    show shunsuke
    ss "In that case, I'm pretty much finished with my work on [anime.name], aside from marketing and keeping the website update." 
    y "That's great to hear. What about everyone else?" 
    s "Yuuko and I only have a little bit left to do." 
    m "I'm almost done, too." 
    y "I have an idea. Since everyone is so close to the end, why don't we skip dinner tonight and keep working to finish everything up?" 
    m "Okay!" 
    show yuuko happy
    yuu "That sounds good." 
    ss "That will put us in a perfect position to prepare for Anime Rising." 
    show sumiko laugh_eyes_closed
    s "Hey, why don't you order pizza again, Yukari?" 
    show yukari sigh
    y "……" 
    s "Kidding."
    show yukari tsundere 
    y "Good, because if we go through that again, I think we'll be blacklisted. Do you know how embarrassing it would be to be blacklisted by a pizza parlor?" 
    ss "If anyone could do it, it would be us…" 
    s "Anyway, I'm on board with getting this done tonight!" 
    show yukari happy
    y "Great! Also, I'll be dropping by the studio over the weekend to do some of the final checks on [anime.name]. If anyone wants to join me, feel free." 
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_10_to_12])
    call expression random_game_event from _call_expression_19

label week_11_6:
    $nextDay()
    scene studio_main with fade
    show yukari at left with dissolve
    "When the weekend arrives, Yukari heads to the studio and gathers all of the assets for [anime.name] they compiled earlier in the week. As she sits down at her desk, the studio door opens." 
    show sumiko happy at pos_textbox_right
    show yuuko at pos_outerright
    with dissolve
    s "Hi!" 
    yuu "I thought this would be a good time to work on the promotional art." 
    s "And I can finish up Episode Two's filming." 
    show yukari happy
    y "Sounds good." 
    scene studio_main
    show yukari at left 
    with dissolve
    "They sit down and get to work. Yukari resumes looking over the anime's finished work."
    "With any luck, Episode Two will be completed soon. They're on pace to meet the deadline, but it will be tight… especially since they need to prepare for Anime Rising, too."  
    "She takes a break to think through what they still need to finish, and the door opens again. Shunsuke walks into the studio." 
    show yukari at left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke laugh_eyes_closed at pos_middleright
    with dissolve
    s "Hey, Shunsuke!" 
    ss "Anything I can do to help?" 
    "Yukari casts him a grateful look." 
    y "Could you print out the materials we'll need for our booth at the con? I planned to do it, but I really need to check all this stuff over." 
    ss "No problem." 
    show sumiko surprised
    s "Wow, I guess the whole gang's here except for Mayumi." 
    show yukari at pos_left
    show mayumi laugh_eyes_closed at pos_farleft behind yukari 
    with dissolve
    m "Guess again!" 
    "She appears in the doorway and enters with a happy wave." 
    m "I decided to drop by to finalize the soundtrack." 
    show mayumi 
    show yukari laugh_eyes_closed
    y "Wow, I didn't expect everyone to come. It almost feels like a regular day at the studio now!" 
    scene studio_main with fade
    show yukari at left 
    show sumiko happy at pos_textbox_right 
    show yuuko at pos_outerright
    with dissolve
    "At the end of the day, she walks around to check everyone's progress. To her surprise, Yuuko has already drawn a huge amount of promotional art for [anime.name]."
    "It's crisp and clear, as high quality as the main art for the anime despite how quickly she must have made it." 
    show yuuko worry
    yuu "Is something wrong?" 
    show yukari happy
    y "No, I'm just impressed." 
    s "Regular art is easy compared to what we've been doing." 
    show yuuko
    yuu "I wouldn't call it 'easy,' but… yes, this was a nice change of pace." 
    y "I'm glad to hear it. Keep up the good work!" 
    scene studio_main with fade
    "On Sunday, everyone returns to the studio again. Yuuko finishes the art and helps Shunsuke prepare for their booth. Yukari checks everything they have completed so far."
    "At the end of the day, she heaves a sigh of relief. Working on the weekend has given them a buffer. They're no longer so pressed for time." 
    "If they can keep this up, everything will work out after all." 
    scene studio 
    $nextWeek()
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_12_1:
    scene studio_main with fade
    show yukari at left with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    $achievement.grant("ACH_3")
    "As soon as she gets to the studio on Monday, Yukari calls up the director of [anim_studio] to check on their current status."
    "After all, time is short… and since they'll be busy with Anime Rising soon, she needs to know immediately if any problems have come up." 
    scene black with fade
    if anim_studio == anim_studio_expensive:
        anim_dir "Hello?" 
        y "Hello, this is Yukari." 
        anim_dir "Ah, Yukari, it's good to hear from you. I was going to get in touch later today. According to our current schedule, Episode Two of [anime.name] will be ready by Wednesday." 
        y "That's fantastic! We'll be at Anime Rising, but I can drop by after it ends to pick up the episode." 
        anim_dir "Anime Rising? That sounds like a fantastic opportunity for your team. I wish you the best of luck, and I'll see you on Wednesday." 
        y "Thanks!" 
    elif anim_studio_expensive == anim_studio_cheap: 
        anim_dir "Hello?" 
        y "Hello, this is Yukari." 
        anim_dir "Uh-oh, I wasn't supposed to call you about something, was I?" 
        y "Oh, no. I just wanted to find out how things are going." 
        anim_dir "Don't worry, everything's on track." 
        y "When can I expect the animation work for Episode Two to be completed?" 
        anim_dir "Seems like it'll be Wednesday, if nothing comes up." 
        y "Great! We'll be at Anime Rising, but I can drop by after it ends to pick up the episode." 
        anim_dir "That's an anime con, right? That should be fun." 
        y "We have a booth there." 
        anim_dir "Oh! In that case, good luck! See you on Wednesday." 
        y "All right, thanks!" 
    "Yukari hangs up the phone." 
    scene studio_main with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    m "Well?" 
    y "We should have the next episode on Wednesday."
    m "Wow, that's so soon!"
    show sumiko laugh_eyes_closed 
    s "This really is the home stretch, huh? After so much work and so much pressure to finish everything on time, it feels weird to not have a massive schedule ahead of us." 
    y "I know. But it's not over yet! Anime Rising is the best opportunity we have to promote [anime.name] to potential fans. We need to work as hard to prepare for it as we did to create the show itself." 
    ss "Of course, we can't lose sight of our remaining tasks for [anime.name], either. All the promotion in the world won't help if we don't have a finished product." 
    show sumiko sigh
    s "Talk about bringing the mood down…" 
    y "He's right. Most of the work is done, but we still need to compile all the legal files to send to our investors and the television company that will be producing [anime.name]…" 
    "Even as she says it, her stomach twists. They don't have enough time, do they? Not with Anime Rising taking up the next two days." 
    show yuuko worry
    yuu "What's wrong?" 
    show yukari sad_angry
    y "As the director, I should handle all of that. But I'm not sure how I can do that and still attend Anime Rising. It wouldn't be right for the director to not be at our booth…" 
    show mayumi laugh_eyes_closed
    m "I can handle the legal documents." 
    show yukari surprised
    y "Really? You don't mind?" 
    show mayumi laugh_eyes_closed
    m "Just show me what I need to do." 
    show yukari
    s "Aw, but won't you have to skip Anime Rising, then?" 
    m "That depends on how much work there is. I might just be late. Besides, it's much more important for the four of you to be at the booth." 
    show yukari happy
    y "You're the best, Mayumi!" 
    "Over the course of the afternoon, Yukari goes over everything with Mayumi so she'll know what to do. Mayumi picks up on it almost immediately." 
    scene studio_main with fade
    show yukari laugh_eyes_closed at left
    show mayumi_f at right
    with dissolve
    y "Wow!" 
    m "Hmm?" 
    y "It took me a lot longer. You must be a genius, Mayumi!"
    show mayumi_f happy
    m "Haha, I'm just better with legal matters than you are. Remember when you needed my help reading over the contract with [anim_studio]?" 
    y "Oh, right." 
    m "Now that I know what I'm doing, you better get to work on our Anime Rising preparations!" 
    y "Okay. Let me know if you need any help." 
    "She leaves Mayumi to the paperwork and walks to Sumiko and Yuuko's desks to see how their work is coming along. As she approaches them, Sumiko spins around in her chair." 
    scene studio_main
    show yukari at left
    show sumiko happy at pos_textbox_right
    show yuuko at pos_outerright
    with dissolve
    s "Done!" 
    y "You are?" 
    yuu "Yes, the promotional art we need for our booth are completed." 
    show yukari happy
    y "Great! Let's get them printed and packed up so we can take them over to the convention center. Shunsuke, give us a hand!" 
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    with dissolve
    "While the sisters print the materials, Yukari and Shunsuke retrieve a few boxes to carry it all in. The four of them work together to get everything neatly packed away."
    show sumiko sad_angry
    s "Phew, this is exhausting!" 
    show yuuko sigh
    yuu "Sumiko… all you've done is put promotional art into a box." 
    show sumiko tsundere
    s "So? My arms are killing me!" 
    show yukari laugh_eyes_closed
    y "Haha, if you think this is tiring, you're going to love carrying it to the convention center." 
    show sumiko surprised
    s "Wait, WHAT?! You expect us to carry these boxes ourselves?"
    show yukari tsundere 
    y "Um… what did you expect?" 
    show sumiko sad_angry
    s "Come on, hire a delivery service to transport them!"
    show yukari sigh 
    y "A delivery service for these little boxes?" 
    s "They're heavy!" 
    yuu "You just don't like to carry things." 
    "To prove her point, Yuuko picks up one of the boxes and gives her sister an expectant look." 
    yuu "See?" 
    show sumiko sad
    s "Ugh…" 
    show yukari happy
    y "On the other hand, maybe Shunsuke should carry the boxes for us." 
    s "Good idea!" 
    show shunsuke_f surprised
    ss "What?!" 
    y "You're a guy. It just makes sense for you to carry them, since you're stronger than us." 
    show shunsuke_f angry_mouth_closed
    ss "This is a suspiciously convenient time for you to announce less progressive views, Madam Director."
    show sumiko laugh_eyes_closed 
    s "Come on, Shunsuke, what sort of gentleman makes the ladies carry everything?"
    show yuuko laugh_eyes_closed
    yuu "It would be the chivalrous thing to do." 
    ss "But…" 
    y "Mayumi, we're taking this stuff to the convention center." 
    m "Okay!" 
    y "Shunsuke, grab the boxes." 
    "She walks to the door empty-handed, and Yuuko follows with an amused smile. Sumiko and Shunsuke stare at each other over the boxes." 
    show sumiko tsundere
    s "Well? Are you going to be a gentleman?"
    show shunsuke_f sad_angry 
    ss "……" 
    s "I mean, my arms are aching, but I suppose I can endure the pain if you're unwilling to do even this tiny act of kindness…"
    show shunsuke_f sigh 
    ss "Oh for crying out loud…" 
    "He stacks the boxes and gathers them all into his arms, then joins the others at the studio door." 
    ss "Fine. Let's go." 
label week_12_2:
    $nextDay()
    scene anime_con with fade
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    show sumiko happy at pos_textbox_right
    show yuuko at pos_outerright
    with dissolve 
    s "I'm so excited!" 
    show yuuko laugh_eyes_closed
    yuu "Me too. I'm a little nervous, though. I've never done anything like this before." 
    y "Neither have I, but we'll be fine. Don't worry too much about it." 
    yuu "I'll try not to." 
    y "Well, let's get set up. We've been given a spot over here for our booth. Follow me." 
    show sumiko
    show yuuko
    "Shunsuke retrieves the boxes from a locker where they put them the previous evening, while the sisters help Yukari carry a table to their assigned spot in the convention center."
    "Several other participants are also setting up, with a few booths already in place." 
    show shunsuke_f laugh_eyes_closed
    ss "Now that I think about it, this poster of ours is amazing." 
    yuu "You really think so?" 
    ss "Definitely. It showcases [anime.name] perfectly, so I think it will catch a lot of attention." 
    s "Well, we'll find out soon enough."
    scene anime_con
    show yukari at left 
    with dissolve
    "As the others unpack the materials and arrange the booth, Yukari checks in with the people in charge of Anime Rising." 
    "Everything goes smoothly, and by the time she returns, their booth is almost ready to go." 
    scene anime_con
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    show sumiko happy at pos_textbox_right
    show yuuko at pos_outerright
    with dissolve
    y "Anime Rising begins in about thirty minutes." 
    s "Don't worry, we'll be all set up by then." 
    y "Shunsuke, can you help me pass out these flyers to people who arrive?" 
    ss "All right." 
    "Each flyer contains a basic overview of [anime.name] and its characters, along with important information like the URL for their website."  
    "Within a few minutes, they finish setting up the booth. The remaining time passes slowly, but then the doors fly open." 
    show yuuko surprised
    play music dashboard_music fadein 2.0 fadeout 2.0
    yuu "Aaah… look at all those people…"
    show sumiko surprised
    s "It's a mob!"
    "The horde of attendees, however, doesn't descend upon their booth. Instead, most people run straight to the booths set up by major anime studios."
    "The smaller studios could be invisible for all the attention they pay to them."
    show sumiko 
    show yuuko
    s "Maybe we should try shouting." 
    show yukari sigh
    y "Like they'd hear us." 
    "Excited fans rave about the merchandise being sold at the larger booths and the trailers being shown for the big studios' latest shows. It's so loud, Yukari and her team members have to raise their voices just to hear each other." 
    show yukari
    y "This was to be expected, though. No one's going to run to an unknown studio's booth right away." 
    show sumiko worry
    s "Ugh, but we went through all this work to prepare! What if it was for nothing?"
    yuu "Relax. It will be fine. Once they get bored, they'll start looking around at the smaller booths." 
    show sumiko
    s "Okay, okay…" 
    attendee "Excuse me…"
    show yuuko laugh_eyes_closed
    yuu "See?" 
    attendee "Do you, uh, know where the restrooms are?" 
    show yuuko
    yuu "……"
    show yukari
    y "Just go out the door over there and make a right at the end of the hall." 
    attendee "Thanks!"
    show yukari happy
    y "Here, take a flyer about [anime.name]." 
    attendee "Oh, sure, thanks!"
    show sumiko sigh
    show yukari
    "Once he leaves, Sumiko throws her hands in the air with an exasperated sigh." 
    s "The one visitor we get just wants directions."
    y "I read that people might ask questions like that, so I made sure to find out the layout of the building in advance. Sure, he didn't care about [anime.name], but we gave him a flyer and now he has a positive impression of us." 
    ss "Ah, and when he thinks about [anime.name], he'll remember how helpful we were and be more inclined to give it a chance. Clever." 
    s "Okay, but I hope some people who are actually interested show up soon…" 
    yuu "They will. Don't worry." 
    "They wait patiently at their booth as person after person walks by without a glance. Yukari smiles at everyone who passes anyway, determined to at least give [anime.name] a positive presence." 
    "Finally, one attendee slows down, his gaze fix on their poster as he draws closer." 
    attendee "[anime.name]…" 
    show yukari laugh_eyes_closed
    y "Hi!" 
    "She hands him a flyer." 
    y "We're a new studio, and [anime.name] is our debut project."  
    attendee "It looks interesting. What's it about?" 
    "Shunsuke steps in to explain the plot. While they talk, a small group of people joins the first attendee. Before long, more and more people are visiting their booth." 
    if anime.category == Anime.HAREM:
        scene expo_harem with fade
    elif anime.category == Anime.ACTION:
        scene expo_action with fade
    elif anime.category == Anime.MYSTERY:
        scene expo_mystery with fade 
    attendee "That poster is amazing! Who drew it?" 
    yuu "I… I did…" 
    attendee "You're an incredible artist!" 
    yuu "Th-thank you!" 
    m "Hi guys, how's it going?" 
    y "Mayumi! Things just started picking up." 
    m "Oh good, I'm glad I didn't miss all the excitement." 
    "She takes a stack of the flyers and joins them at the booth, as more and more people stop by." 
    attendee "[anime.name]? What's it about?" 
    attendee "Is this merchandise for sale?" 
    attendee "Can I take one of these?" 
    attendee "What time will [anime.name] air?" 
    "It's a rush of questions, but a welcome one. Yukari lets Mayumi and Shunsuke hand out flyers while she tells people about [anime.name] in more detail, although he jumps in from time to time with more specific details about the story." 
    "Sumiko and Yuuko handle sales of the merchandise they brought. Since they didn't have much time to prepare, they didn't have time for anything special, but even the CDs and small art books prove to be a hit." 
    "Before long, the booth is packed with people. Some have questions, some want merchandise, and some are just curious."
    "Each person who leaves is one more potential fan… and someone who can spread the word about [anime.name] to other Anime Rising guests." 
    scene anime_con with fade
    show yukari at pos_left
    show sumiko surprised at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    s "Holy crap, there's a lot of people coming! Never in my wildest dreams did I think it would be like this." 
    show yukari happy
    y "I know." 
    show sumiko laugh_eyes_closed
    s "All the obstacles and bad luck along the way… it doesn't seem like it matters anymore." 
    y "I agree. It was all worth it!" 
    "By the end of the day, all five of them are exhausted. They pack everything up and leave the convention center without much conversation, all knowing they'll need to get a good night's sleep to be ready for the second day of Anime Rising." 
     
label week_12_3: 
    $nextDay()
    play music cafe_music fadein 2.0 fadeout 2.0
    scene anime_con with fade
    show yukari happy at pos_left
    show sumiko surprised at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "Everyone ready for the last day of the con?" 
    show mayumi laugh_eyes_closed
    m "Definitely!" 
    s "I wonder if it will be as hectic as it was yesterday." 
    ss "Unlikely. Yesterday was the primary day for Anime Rising. The main reason it's held today as well is for people who couldn't make it then." 
    y "And some people enjoy conventions enough to come both days." 
    ss "True, but there shouldn't be nearly as many." 
    show yuuko laugh_eyes_closed
    yuu "Well, even if it's a smaller crowd, we can still spread the word to more people." 
    y "Of course!" 
    "When the doors open this time, attendees enter in smaller groups rather than as a massive crowd. It's a decent turnout, but noticeably less busy than it was the day before." 
    "However, many people still stop by the booth for [anime.name]. Yukari tells everyone about it, Shunsuke and Mayumi pass out flyers, and Sumiko and Yuuko sell merchandise. All of them answer questions from interested attendees." 
    play sound "music/sfx/phone_ringing.ogg" fadeout 1.0
    y "Huh? Who could be calling me now?" 
    "She glances at her phone. It's the director of [anim_studio]." 
    stop sound fadeout 1.0
    y "Can you guys handle the booth without me for a few minutes?" 
    m "No problem." 
    scene anime_con
    show yukari at left 
    with dissolve
    "Yukari hurries away to a quieter section of the convention center to take the call." 
    y "Hello?" 
    if anim_studio == anim_studio_expensive:
        anim_dir "Hello, Yukari. I just wanted to let you know that Episode Two of [anime.name] is ready." 
        y "Great! I'll be by later today to pick it up." 
        anim_dir "Perfect. How are things going at Anime Rising?" 
        y "Really well. Much better than I expected, in fact. A lot of people have stopped by our booth." 
        anim_dir "I'm happy to hear it. Well, I'll see you later." 
    elif anim_studio == anim_studio_cheap:
        anim_dir "Hi, Yukari. I hope I'm not interrupting." 
        y "It's fine. What's up?" 
        anim_dir "First, don't panic." 
        "A comment like that is a surefire way to make Yukari panic. She grits her teeth and braces herself." 
        y "Okay…" 
        anim_dir "We ran into trouble with one of our other projects, and as a result, Episode Two of [anime.name] isn't finished yet. But don't worry! We're going to work overtime and have it ready for you tomorrow morning." 
        y "All right, I understand." 
        "The delay is regrettable, but at least it's not a big one. She wouldn't have been able to pick up the material until after Anime Rising ends, anyway." 
        y "I'll be by tomorrow morning, then." 
        anim_dir "Okay, see you then. Thanks for understanding!"
    scene anime_con
    show yukari at pos_left
    show sumiko surprised at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    "Yukari ends the call and returns to [anime.name]'s booth, where Yuuko is showing off some of the character designs to an excited group of potential fans." 
    ss "Anything wrong?" 
    y "No, just an update on our animation status." 
    "There's no time to talk about it in further detail, as more attendees arrive at the booth. Yukari resumes describing the basic premise and themes of [anime.name]." 
    scene anime_con
    show yukari at left
    show investor smile at right
    with dissolve
    investor "You seem to be attracting a fair amount of attention. That's good to see."
    show yukari laugh_eyes_closed 
    y "Yes! It's been great!" 
    investor "I apologize for not being here yesterday. Something came up, and I couldn't make it."
    show yukari 
    y "Oh, that's quite all right." 
    "Sumiko leans close to Yuuko, but her whisper is loud enough for Yukari to hear." 
    s "Do we know this guy?" 
    y "Haha, sorry everyone. This is our investor." 
    investor "It's nice to finally meet all of you. Well, I better move on. I don't want to take up your time when you could be winning over more fans. Good luck!" 
    y "Thanks!" 
    hide investor with dissolve
    "The rest of the afternoon passes quickly, and Anime Rising is over before they know it. They gave out an impressive amount of flyers and told more people about [anime.name] than Yukari can count." 
    scene anime_con
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    s "Phew. What a day." 
    show yukari happy
    y "Good work, everyone. I'd say Anime Rising was a success!" 
    show shunsuke laugh_eyes_closed
    ss "And I have hard data to back that up." 
    show mayumi surprised
    m "You do?" 
    ss "I just checked our website's stats. Its traffic has increased significantly over these past two days. While it could be a coincidence, it's most likely related to Anime Rising." 
    y "Awesome!"
    show mayumi
    if guerilla_marketing:
        ss "Our social media followers have also increased." 
    show sumiko laugh_eyes_closed
    s "I knew our preparations would pay off!"
    show yuuko sigh
    yuu "Really? I seem to remember you saying something like… 'What if it was for nothing?' when we started out yesterday." 
    show sumiko tsundere
    s "I said 'what if.' I never said I believed it." 
    ss "None of us could guarantee success. The important thing is that it WAS successful." 
    show mayumi happy
    m "Yeah!" 
    y "To celebrate our success at Anime Rising, I think a little vacation would be nice. You've all worked hard, so take tomorrow to relax and savor how far we've come."  
    s "Woohoo! Holiday!" 

label week_12_4:
    $nextDay()
    scene black with fade
    if anim_studio == anim_studio_expensive:
        "After they take their remaining materials back to the studio, Yukari heads to [anim_studio] to pick up Episode Two. Tomorrow may be a holiday for the others, but her work isn't finished yet." 
    elif anim_studio == anim_studio_cheap:
        "In the morning, Yukari visits [anim_studio]. To her relief, there haven't been any further delays. Episode Two is ready. Once she has it, she heads to the studio. It may be a holiday for the others, but she still has work to do." 
    scene studio_main with fade
    show yukari at left
    with dissolve
    "It feels strange to be in the studio alone. Nevertheless, she sits down at her computer so she can check over the episodes." 
    y "Huh?" 
    play sound [sfx_anim_d_open,sfx_anim_d_close]
    "She looks up as the studio door opens." 
    show mayumi_f laugh_eyes_closed at right with dissolve
    m "Hi!" 
    y "Mayumi? I said everyone could have the day off, remember?" 
    show mayumi_f
    m "I know, but I don't mind working today. I'm so invested in [anime.name] now, I won't be able to really relax until it's finished." 
    y "Fair point." 
    m "So what do you need help with?"
    show yukari sigh
    y "What? Didn't you come here with a plan?" 
    m "No, I wanted to help you." 
    show yukari
    y "How did you know I'd be here…?" 
    show mayumi_f laugh_eyes_closed
    m "Hahaha, we've been friends for so long, did you think I wouldn't realize you planned to come in anyway?" 
    show yukari surprised
    y "I'm that transparent?" 
    m "Only because I know you so well. So, what should I do?" 
    show yukari
    y "Hmm… can you check the dubbing of [anime.name]?" 
    "It's important to make sure all of the audio is properly in sync with the animation. Poor timing and misplaced audio would definitely disturb viewers." 
    y "I just picked up Episode Two from [anim_studio], as well, so we can finish up the final stages for that." 
    m "Sure, no problem." 
    "Yukari had expected to handle everything herself today, but with Mayumi there, she has a choice of what to focus on…" 
    menu:
        "Quality Assurance":
            $choice_12_1_1()
            "Yukari goes through everything they've already finished to run another quality assurance test. She checks it for any mistakes like errors in the art, out-of-sync audio, missing animations, or problems with the editing."
            "To her relief, there is very little they have to fix." 
        "Dubbing":
            $choice_12_1_2()
            "She helps Mayumi check over Episode One's dubbing and finish up the dubbing of Episode Two. In addition to making sure the dialogue is in-sync with the characters' animations, they also make sure the sound effects and music tracks play at the right moments."
            "Fortunately, everything looks pretty good." 
        "Marketing":
            $choice_12_1_3()
            "Anime Rising was a major boost for their marketing efforts, but this is the time when they need to promote [anime.name] as much as possible. Yukari works on a press release to send to popular anime websites before [anime.name] airs." 

    scene studio_main with fade
    show yukari at left
    show mayumi_f happy at right
    with dissolve
    m "I'm finished!" 
    show yukari laugh_eyes_closed
    y "Me too. This was a good day's work." 
    m "Does this mean… we're done?" 
    y "I'll want everyone to do a final check, but aside from that, yes. [anime.name] is complete."

label week_12_5:
    $nextDay()
    scene studio_main with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
    play music happy_music fadein 2.0 fadeout 2.0
    "The next day, excitement fills the air. Everyone knows this is it." 
    y "Okay, I know we've looked through these files a thousand times, but I'd like you all to take another look." 
    "She paces back and forth while her team members check over the files for [anime.name]'s episodes. One by one, they report their satisfaction with the final product." 
    s "What now? We burn it to a DVD?" 
    y "That's right… except I think I'll check it over once more myself."
    show mayumi laugh_eyes_closed 
    m "Are you feeling a little nervous, Yukari?" 
    show yukari sigh
    y "Of course I am! Aren't you?" 
    show mayumi
    m "Yes, but there's a point where you have to let it go and trust your judgment." 
    y "I know… I just want to do one more check." 
    show yukari
    "She runs through both episodes once more and finds nothing that needs to be changed. With a deep breath, she burns them to a DVD." 
    show yukari happy
    y "Well, this is it. [anime.name] is done!" 
    show sumiko surprised
    s "You know, it's pretty incredible that we managed to make an anime. And you know what's even more amazing? That we all became such good friends! There were times when I thought we'd kill each other instead."
    show yuuko happy 
    yuu "No matter what happens with [anime.name] after this, I'll always consider you my best friends. I may not show my feelings well all the time, but I truly treasure each and every one of you." 
    show sumiko laugh
    s "Hmph, you show your feelings fine. It's Mr. Logical who struggles in that department."
    ss "Excuse me? I'll have you know this was a fantastic, wonderful journey for me as well, and I also consider you my friends." 
    m "We know. She's just trying to needle you." 
    ss "Anyway, what we really should do is thank Yukari. Her vision is what brought us all together." 
    show yukari
    y "Aw, thanks…" 
    m "Haha, yeah, Yukari… even though you screwed up a few times, we couldn't have done this without you." 
    show yukari sigh
    y "I'm not sure if I should feel complimented or insulted…" 
    m "It's a compliment! You're the strongest pillar of our team, always willing to push forward despite any obstacles. Even when you caused those obstacles…"
    show yukari 
    y "Oh, stop, haha." 
    "She knows her friend is just teasing her, and it even makes her feel a little better than if everyone thanked her without remembering the problems they encountered." 
    y "Well, I want to thank all of you, as well. Maybe I was the 'strongest pillar,' but I couldn't have done this on my own. It's your hard work and perseverance that made this possible."  
    s "That's what a team does, right? And more importantly, that's what friends are for." 
    y "Right!" 
    "For a moment, the team stands together in silence." 
    ss "I guess there isn't much else for us to do today." 
    y "Yep, there's no need for us to hang around the studio. But we're still meeting up for dinner, right?" 
    m "We wouldn't miss it for the world." 
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve  
    "There's a strange mood over their table as they gather for dinner."
    "It's celebratory, because they've accomplished their goal… but also sad, since the days of working together on [anime.name] are over. And of course, no one can escape a little nervousness with [anime.name]'s premiere on the horizon." 
    "Yukari looks around the table, and a pang of sorrow strikes her. She'll miss these weekly meetings. For that matter, she'll miss seeing her friends in the studio every day, too." 
    m "What's wrong, Yukari? You don't look like someone who just fulfilled her dream."
    show yukari sad_angry 
    y "Oh… I was just thinking that I'll miss all of you…"
    s "Miss us? Where are you going?" 
    y "No, I mean…" 
    ss "Did you think you could get rid of us that easily?" 
    y "No, no, I just thought…" 
    yuu "I hope we can still get together some weeks for dinner."
    show mayumi sigh
    m "Yeah! Why does this have to be the end?" 
    "Yukari's heart leaps."
    show yukari laugh_eyes_closed
    y "I'd love that!" 
    ss "And as I recall, you all but promised me the chance to write a sequel if [anime.name] is a success. You'll have to try much harder to disband this team, Yukari." 
    y "I'm glad. I wouldn't disband our group for anything in the world." 
    "She looks around the table at her friends, and happiness replaces her sorrow. This may be the end of their first project, but their time together is far from over." 
    show yukari
    y "You know, when I started this, I just wanted to direct an anime. That would be how I'd judge my success, whether I completed an anime or not. But now… I'm happy I directed [anime.name], but I'm even happier I met all of you." 
    "She pauses." 
    y "Most of you, I mean. I already knew Mayumi." 
    m "And?" 
    y "Huh?" 
    "Mayumi and Yuuko exchange a meaningful look while Yukari watches in confusion, and then the artist shyly clears her throat." 
    yuu "We, um… we met before this project, Yukari." 
    show yukari surprised
    y "We did?!" 
    yuu "It was at school. You protected me from a group of bullies, and then we ran across town to escape them." 
    "The memory slowly returns to Yukari, and she stares at Yuuko in astonishment." 
    y "That was you? I didn't even remember…" 
    yuu "I noticed." 
    show yukari
    y "Aw, I'm sorry…" 
    show yuuko laugh_eyes_closed
    yuu "Don't apologize. It's fine. We're friends now, and that's what matters, right?" 
    y "I suppose… I just feel bad that I completely forgot you after that day." 
    m "If it happened now, you'd remember. You've become much more of a people person than you used to be." 
    yuu "It probably stood out in my memory more because of the impression you left on me. You were my hero, who saved me without a second thought… and they left me alone after that." 
    y "I can't take credit for that last part. Someone else scared them straight after we ran away."
    show mayumi surprised 
    m "What? You mean there really WAS a hero lurking in the shadows?!"
    y "I don’t know about that, but now I remember what I heard. After we left, the bullies were going to chase us, but someone warned them that if they ever bothered anyone again, they'd get a lot worse than a punch in the nose." 
    yuu "Really? Who was it?"
    show mayumi
    y "No one knows. But from the rumors, it was someone terrifying." 
    show sumiko surprised
    ss "Wait… the rumors say the person was terrifying?" 
    y "Yeah!" 
    show sumiko
    "She leans forward, really getting into the story now that her memories of the event have returned." 
    y "People say the leader of the group kept muttering about the person's cold, dead eyes and maniacal smile…" 
    m "Wow!" 
    ss "Cold, dead eyes? Maniacal smile?" 
    y "Yep!" 
    show shunsuke sigh
    ss "Stop exaggerating the story for dramatic effect!"
    show sumiko surprised
    s "Whoa, what's gotten into you?" 
    ss "I just find it incredibly hard to believe that he was a sinister guy with cold, dead eyes and a maniacal smile, that's all!" 
    s "Hang on… how do you know it was a 'he'?" 
    show shunsuke
    ss "Because it… That is… Because I guessed, that's all!" 
    show yuuko surprised
    yuu "Wait a minute, was it you, Shunsuke?" 
    show yukari surprised
    y "Whoa, was it?"
    show shunsuke sigh
    ss "I… might have said a few words to them. But I certainly didn't have dead eyes or a maniacal anything!"
    show yuuko 
    show yukari
    show sumiko laugh_eyes_closed
    s "Hahaha, wow. This is perfect! So Yukari, who is friends with Mayumi, rescued my sister, and then they were secretly aided by Shunsuke? You know what that means?" 
    show yukari
    y "What?" 
    s "It was destiny for us to meet up again like this! Right?" 
    show shunsuke
    ss "Wrong." 
    s "Huh?!" 
    ss "We met up because we all fill the roles needed for an anime studio. It had nothing to do with 'destiny.'"
    show sumiko sigh 
    s "Oh, don't tell me you don't believe in destiny." 
    ss "It's not very logical." 
    s "Logical schmogical! You need to lighten up." 
    ss "I am perfectly lighthearted, thank you very much." 
    s "Your cold, dead eyes say otherwise." 
    show shunsuke sad_angry
    ss "I do NOT have cold, dead eyes!" 
    "Yukari exchanges glances with the other two as the argument rages across the table." 
    m "Well, it's not like this is anything new." 
    yuu "I wonder if they'll ever stop…" 
    "Yukari smiles and closes her eyes. She meant what she said earlier. By the end, creating [anime.name] wasn't the best part of the past few months. Creating new friendships was." 
    "In a few days, the first episode of [anime.name] will air."
    "They'll finally learn what an audience thinks of it. It could be a success, and they'll have to plan their next move, maybe even make plans for a sequel. Or it could be a flop, and she'll be forced to accept that she might not be ready to direct her own anime yet."
    "But the thought of failure no longer terrifies her." 
    "Come what may, Yukari has a group of friends—a team—that won't ever let her down."

label epilogue:
    $fastForwardDays(3)
    $anime_score_components = (anime.plot + anime.character_development + anime.storyboard + anime.character_design + anime.background + anime.animation + anime.voice_acting +anime.op_ed + anime.ost ) 
    $anime_score_multipliers = (1 + yukari_stats.management * 0.05 + anime.marketing * 0.05 + anime.quality_check * 0.25)
    $anime_score = anime_score_components * anime_score_multipliers 
    scene studio_main with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music tension_music fadein 2.0 fadeout 2.0
    "At last, the day of [anime.name]'s premiere arrives." 
    "Yukari and her team gather in the studio once again, with a wide-screen TV brought in special so they can watch the episode." 
    show yukari worry
    y "I'm so nervous…" 
    show yuuko worry
    yuu "M-me too…" 
    m "Relax, everyone. It'll be fine." 
    y "I hope you're right…" 
    show sumiko laugh_eyes_closed
    s "I brought popcorn!" 
    show shunsuke sigh
    ss "Popcorn? But the celebration isn't until after the episode airs." 
    s "So? Nothing like a bowl of popcorn with a good anime!" 
    y "I hope [anime.name] IS a good name…" 
    m "Stop worrying so much!" 
    "But everyone is a bit nervous as the time draws closer. At last, it's time. Sumiko makes popcorn for everyone, and they sit down in front of the TV to watch [anime.name] on the big screen." 
    "For Yukari, it's exhilarating to see her months of hard work brought to life, and she can tell from the looks on their faces that the others feel the same. Still, she can't help but worry about whether or not audiences will enjoy it." 
    "The episode ends all too soon, and then it's time to face the Internet. Yukari visits a popular anime site to see what people are saying about it." 
    show shunsuke
    show sumiko
    show yuuko
    if anime_score < ANIME_MIN_POOR_VALUE:
        m "Well?" 
        y "I'm looking… give it time…" 
        "Time passes with no reactions on the site. She eventually gives up and checks another anime site. And another. Finally, she finds people talking about it." 
        y "…Oh." 
        ss "What's wrong?" 
        show yukari sad_angry
        play music sad_music fadein 1.5 fadeout 1.5
        "She takes a deep breath and relays the news to the team as gently as she can."
        "Hardly anyone watched [anime.name], and those few who did were unimpressed. Reading the harsh words from viewers hurts, but not as much as seeing how many people didn't bother to watch at all." 
        show mayumi sad
        m "People… didn't like it…?" 
        show sumiko
        s "Aw, what do they know? We'll get them next time!" 
        "With a reception like this, Yukari doubts very much there will be a next time. She feels as though the world is about to fall out from under her. She fulfilled her dream and made her own anime… and it was an utter failure." 
        play sound "music/sfx/phone_ringing.ogg"
        "The sound of her phone jolts Yukari from her horrified reverie, but one look at the caller's number makes her feel even worse. It's their investor." 
        y "Urgh…"
        show shunsuke sad
        ss "You can't just ignore the call." 
        y "I know…" 
        "She answers with great reluctance." 
        stop sound fadeout 1.0
        y "Hello…" 
        investor "…Ah. From your tone of voice, I gather you know how it went?" 
        y "Yeah… I'm sorry…" 
        "He's understandably disappointed, but she can't focus on his words. All she can do is apologize, think over everything that happened, and wonder what she can do from here." 
        "No one actually comes to the party, but that's fine, since no one on the team feels like celebrating anyway."
        "They talk a little to try to cheer each other up, but Yukari barely hears them. When it's time to leave the studio, she feels like she might burst into tears." 
        y "Before you go… I'd like to apologize…" 
        m "Yukari…" 
        y "Our anime was a failure, and as the director… I feel it's my responsibility."
        show shunsuke sad_angry 
        ss "That's not true. We all share in the blame." 
        y "Still, you wasted months of your lives for my dream…"
        show yuuko worry 
        yuu "It wasn't a waste!" 
        y "I'm so sorry…" 
        s "Keep your chin up, Yukari! It's not the end of the world, and we're all still friends. They can't take that away from us." 
        "Yukari nods, but while they may be friends, she doubts they'll ever work on another anime together."
        scene home with fade
        show yukari at left with dissolve
        "She breaks the news to her grandmother the next day. Although her grandmother shares her disappointment, she reminds her that at least she learned many valuable lessons about how to manage a team and produce an anime."
        "In the end, she encourages Yukari to learn from her mistakes and try again when she's more prepared." 
        "Yukari's greatest dream has always been to create her own anime. [anime.name] failed, but that doesn't mean her dream needs to die. She isn't ready to direct her own anime yet." 
        "But someday, she will be." 
    elif ANIME_MIN_POOR_VALUE <= anime_score < ANIME_MIN_AVERAGE_VALUE:
        show yukari sad
        play music sad_music fadein 1.5 fadeout 1.5
        "Unfortunately, the reactions are pretty negative."
        "Some viewers already knew about [anime.name] because of its marketing, while others just tuned in to see what it was, but almost none of them enjoyed it. Only a handful of people seem interested in watching Episode Two when it airs." 
        m "Yukari? You've gone all pale." 
        y "It's…" 
        yuu "Bad news?" 
        show yukari sad_angry
        y "Viewers… didn't enjoy [anime.name]…" 
        show sumiko worry
        s "What? Why not?!" 
        "Although it hurts, Yukari reads some of the criticisms out loud to them." 
        ss "It's all right. We can recover from this."
        y "Are you serious?" 
        ss "Perfectly. Those are valid criticisms. We can learn from them." 
        m "He's right!" 
        "How can they sound so calm? Their anime failed. Yukari feels like crying. She finally fulfilled her dream and made an anime… and people don't like it." 
        y "I don't know, guys…" 
        play sound "music/sfx/phone_ringing.ogg" 
        "She checks her phone when it rings, and her stomach drops. It's their investor." 
        y "I guess I better answer it, huh?" 
        s "Hiding won't do any good." 
        "Yukari sighs and answers the phone." 
        stop sound fadeout 1.0
        y "Hello." 
        investor "Hello, Yukari. It seems like [anime.name] isn't as popular as we hoped." 
        y "I know. I'm really sorry." 
        investor "You don't need to apologize. I knew the risks when I invested in a new team." 
        "Putting it that way almost makes it sound like he expected them to fail. On the other hand, at least he isn't angry. That makes Yukari feel slightly better." 
        "Once she finishes talking to the investor, they begin a lackluster celebration for completing [anime.name]."
        show sumiko 
        s "See, it's good we had the popcorn ahead of time. We wouldn't feel like it now!" 
        show yukari sad
        y "Heh…" 
        m "It's not a total loss, Yukari. At least we made an anime." 
        yuu "And we learned many valuable things." 
        ss "There ARE a couple people online who have positive things to say." 
        y "Really?" 
        ss "Yes. Not many, but here's one who says…"
        "'It's a shame [anime.name] turned out the way it did, because you can tell the team loved making it. Even if the second episode doesn't fix the first episode's flaws, at least we have a promising studio to keep an eye on.'" 
        y "Huh? They expect us to make more anime?" 
        s "Aren't we going to?" 
        y "W-well…" 
        m "Think about it, Yukari. This doesn't have to be the end." 
        y "……" 
        scene home_night with fade
        show yukari at left
        with dissolve
        "No one else comes to celebrate with them, so they pack up and leave early. All night long, Yukari thinks about what Mayumi said." 
        "The next time she talks to her grandmother, she's calm enough to tell her the unfortunate news without breaking down."
        "Although both of them are disappointed, they know this isn't the end. It will be difficult for Yukari to try again after this. She won't be able to do it right away." 
        "But one day in the future, she'll make another anime. And this time, it will be a success." 
    elif ANIME_MIN_AVERAGE_VALUE <= anime_score < ANIME_MIN_GOOD_VALUE:
        "People's reactions are pretty mixed. Some enjoyed the episode, but many people point out flaws in it."
        "There are even a couple debates about whether certain aspects of [anime.name] are justified or not. More than one person points out that it was made by a tiny new studio, and Yukari isn't sure if that should make her feel better or worse." 
        m "Well?" 
        show yukari worry
        y "Just a minute." 
        "She checks a few more sites. All show a similar mix of reactions from viewers." 
        y "I have good news and bad news." 
        show sumiko worry
        s "Give us the bad news first." 
        show yukari sigh
        y "The bad news is a lot of people disliked the episode." 
        show sumiko sad
        s "Aw…" 
        yuu "And the good news?" 
        show yukari
        y "Quite a few people liked it, too!" 
        show mayumi happy
        m "Ah! That's not so bad, then." 
        ss "Let me take a look… Yes, it looks like we're getting mixed reviews all over the place." 
        s "So… is this just because different views like different things?" 
        ss "Well, partly, but they're also making valid criticisms. Several people cut us a little slack since it's our first project." 
        ss "We should pay close attention to critical reviews so we know what to fix next time." 
        show yukari surprised
        y "N-next time? Are you sure—" 
        play sound "music/sfx/phone_ringing.ogg"
        "The ringing of her phone cuts her off. It's their investor calling. She quickly answers it and hopes he isn't too disappointed with what happened." 
        stop sound fadeout 1.0
        show yukari
        y "Hello?" 
        investor "Hello, Yukari. What do you think of [anime.name]'s premiere?" 
        show yukari sad
        y "I'd hoped it would be better-received. I'm sorry…" 
        investor "Nonsense, you've all done quite well for a studio of your size and inexperience." 
        "In her heart, Yukari knows how unlikely it is that a group of fans making their first anime over the span of three months would create the latest hit."
        "But it's still a little irritating to hear these frequent comments on how this lukewarm reception was to be expected." 
        investor "Of course, I understand that you wanted it to go better. Anyone would. I wanted to reassure you, though, that I would be happy to see a pitch from your studio about your next project." 
        y "Th-thank you…" 
        "Next project? He's as bad as Shunsuke. She finishes the conversation in a daze."
        "Do they really think it will be that easy to pick up and try again? Even if they do, it could be more difficult to get attention, since dissatisfied viewers will be wary of their studio." 
        show mayumi
        m "Cheer up, Yukari. We have a few fans, after all!" 
        show yukari
        y "Yeah, I guess…" 
        show sumiko laugh_eyes_closed
        stop music fadeout 2.0
        s "Let's celebrate!" 
        y "…You're right. We made an anime and people actually watched it! Let's celebrate that, if nothing else."  
        "Partway into their celebration, a knock at the door heralds the arrival of Sumiko's friends."
        "Yukari almost forgot she invited them after they completed their work on the animation, but now she's delighted to see them—especially since they seem thrilled at how [anime.name] turned out." 
        "It's a small party, but it boosts Yukari's spirits. They're right. This is no time to give up. By the time the celebration winds down, she feels motivated again." 
        y "So, can I count on all of you to help with my next anime idea?" 
        show mayumi laugh_eyes_closed
        m "Haha, that's the Yukari I know!" 
        s "We're in this all the way!" 
        show yuuko happy
        yuu "How could we let you down?" 
        show shunsuke happy
        ss "Don't worry, Yukari. Whenever you're ready, we'll be there to help." 
        show yukari laugh_eyes_closed
        y "Thanks. You four are the best friends anyone could hope for!" 
        "She looks over fan reactions to [anime.name] one more time before she leaves the studio, and this time they don't depress her so much. Instead, they inspire her." 
        scene home with fade
        show yukari at left with dissolve
        "A few days later, she visits her grandmother and tells her about [anime.name]'s mixed reception… and her ideas for how they can avoid making the same mistakes in the future." 
        "Yukari and her friends aren't ready to leap into a new project right away, especially since their vacation is almost over. But everyone on the team is willing to try again." 
        "[anime.name] didn't turn out as well as they hoped, but Yukari will do everything in her power to make her next anime a success." 
    elif ANIME_MIN_GOOD_VALUE <= anime_score < ANIME_MIN_GREAT_VALUE:
        show yukari surprised
        play music dashboard_music fadein 1.5 fadeout 1.5
        y "Wow!" 
        m "What is it, what is it?" 
        show yukari laugh_eyes_closed
        y "People… liked it!" 
        "[anime.name] isn't getting as much attention as the big names, but quite a few people are talking about Episode One and their hopes for Episode Two." 
        s "Why do you sound so shocked?" 
        y "I was so worried… but they like it, they actually like it!" 
        "The moment she says it, her gaze lands on a detractor who lists several criticisms of the episode. He's joined by another, and then another." 
        show yukari sad
        y "Aw…" 
        "Shunsuke glances over her shoulder." 
        show shunsuke sigh
        ss "Did you really expect 100\% positive feedback?"
        show yukari
        y "I can dream, can't I?" 
        show yuuko laugh_eyes_closed
        yuu "I think it's wonderful that so many people enjoyed it."
        show mayumi happy 
        m "Yeah!" 
        play sound "music/sfx/phone_ringing.ogg" 
        y "Hmm? I wonder who that could be."
        show sumiko happy
        s "Probably a fan!" 
        y "With my personal number?" 
        "She takes out her phone. To her surprise, it's the director of [anim_studio]! She answers it right away." 
        stop sound fadeout 1.0
        y "Hello?" 
        if anim_studio == anim_studio_expensive: 
            anim_dir "Hello, Yukari! I wasn't able to watch [anime.name], and we're still too busy to make it to your celebration, but I wanted to congratulate you." 
            y "Oh! Thanks!" 
            anim_dir "It seems like the overall reception is good." 
            y "Yes!" 
            anim_dir "I need to get back to work now, but let me say it once more: Congratulations!" 
            y "Thank you!" 
        elif anim_studio == anim_studio_cheap:
            anim_dir "Yukari! I watched Episode One of [anime.name], and I think it turned out great!" 
            y "Oh, thank you!" 
            "But didn't he say they had a lot of work to do at the studio? How did he find time to watch an anime?" 
            anim_dir "I thought we might be able to come to your party after all, but we've somehow fallen behind on our work again…" 
            y "I wonder how that happened." 
            anim_dir "I know, right? But anyway, congratulations!" 
            y "Thank you!"
        "She hangs up the phone." 
        y "That was the director of [anim_studio]. He wanted to congratulate us." 
        show yuuko
        yuu "Aw, that's very nice of him."
        show shunsuke
        ss "You know, reading these comments on [anime.name] is fascinating. It really shows me where we can improve for the future." 
        show sumiko happy
        s "Oh yeah, if they think [anime.name] is good, they haven't seen anything yet!" 
        m "That's the spirit!" 
        play sound "music/sfx/phone_ringing.ogg" 
        show yukari sigh
        y "Another call so soon?" 
        "She checks her phone. This time, it's their investor!" 
        stop sound fadeout 1.0
        show yukari
        y "Hello?" 
        investor "Hello, Yukari. It looks as though [anime.name] is doing well." 
        y "Yes, a lot of viewers liked it!" 
        investor "Congratulations. Do you intend to make more anime after this?" 
        y "We've talked about it, although we haven't made any solid plans." 
        investor "Well, if you do, you can count on me to back you again." 
        y "Thank you!" 
        "Once she finished the conversation and hangs up, she relays his message to the rest of the team. Everyone seems excited at the prospect of making another anime, and they begin their post-premiere celebration in earnest." 
        "Sumiko's friends arrive after a short while, all bubbling with excitement over [anime.name]."
        "Part of it is due to their own work on the project, but a lot is because they just enjoyed watching it. It's a lively party, and Yukari is a little disappointed when it ends." 
        m "So what next? Are we going to work on another anime?" 
        show shunsuke laugh_eyes_closed
        ss "Of course we are. I was promised a sequel, remember?"
        y "Haha, I think we all could use a rest before we do this again." 
        yuu "Yes, definitely…"  
        show yukari happy
        y "But after that? I'd love to make another anime with you guys!" 
        s "Woohoo!" 
        "As they leave the studio together, Yukari can hardly contain her excitement."
        scene home with fade
        show yukari at left with dissolve 
        "The next day, she visits her grandmother to tell her how she made her dream come true. It feels like so long ago her grandmother offered to help, and now Yukari has created her own anime… and a successful one, at that." 
        "But even though she fulfilled her dream… it's only the beginning."  
    elif ANIME_MIN_GREAT_VALUE <= anime_score < ANIME_MIN_AMAZING_VALUE: 
        "For a moment, she just stares at the screen in shock, unable to form words." 
        play music dashboard_music fadein 1.5 fadeout 1.5
        show mayumi surprised
        m "Earth to Yukari…" 
        show shunsuke worry
        ss "Is everything all right?" 
        show yukari laugh_eyes_closed
        $achievement.grant("ACH_8")
        y "People… liked it a lot!" 
        show mayumi
        show sumiko happy
        s "Yes!" 
        show yuuko happy
        yuu "Oh, I'm glad!" 
        "She continues to read through comments, growing more excited by the minute."
        "It feels like a dream, but she knows she's awake. She'd hoped [anime.name] would see a decent reception… but this is better than she ever expected!" 
        y "Listen to this: 'I was skeptical of an anime from such a new studio, but [anime.name] held my interest from start to finish. I can't wait for the second episode, and I'm only disappointed there won't be more.'" 
        s "Don't you worry, Mr. Random Internet Commenter, we'll make more!" 
        m "I think it's to begin our celebration!" 
        y "Yeah, we—" 
        play sound "music/sfx/phone_ringing.ogg" 
        y "Who could that be?" 
        "She gets out her phone and takes a look. It's the director of [anim_studio]! Yukari feels like she's on top of the world as she answers it."
        stop sound fadeout 1.0
        show yukari happy 
        y "Hello!" 
        if anim_studio == anim_studio_expensive: 
            anim_dir "Congratulations!" 
            y "Thank you!" 
            anim_dir "I made sure to check on [anime.name]'s initial reception. Things are looking really good!" 
            y "I know! I'm so excited!" 
            anim_dir "Our partnership was definitely worthwhile. I hope you'll consider working with us again in the future." 
            y "Definitely." 
            anim_dir "Well, I need to get back to work now, and I'm sure you want to celebrate. Once again, congratulations!" 
        elif anim_studio == anim_studio_cheap: 
            anim_dir "Wow, [anime.name] was great!" 
            y "You watched?" 
            "She thought he said the studio was pretty busy. How could the director find enough free time to watch an anime episode?" 
            anim_dir "We're swamped with work here, but I just couldn't resist. Congratulations!" 
            y "Haha, thanks." 
            anim_dir "I visited a few anime forums, and it looks like a lot of people agree." 
            "He's browsing the Internet when they're so busy, too?" 
            anim_dir "I really need to get back to work now, but I hope you'll work with us again on your next project. Oh, and enjoy your party!" 
        y "Thank you!" 
        "She ends the call and returns her attention to the others." 
        show yukari
        y "That was the director of [anim_studio] calling to congratulate us." 
        yuu "Aw, that was nice of him." 
        show shunsuke laugh_eyes_closed
        ss "Guess what?" 
        "While she was on the phone, he'd gone online to see how other people had reacted to [anime.name]." 
        y "What?" 
        ss "A couple big anime sites already put up reviews of [anime.name]." 
        show sumiko surprised
        s "Whoa!" 
        show sumiko
        "Everyone crowds around his computer screen to see. Indeed, professional reviewers decided to cover [anime.name]. The reviews do point out a few flaws, but the overall tone is positive." 
        show mayumi happy
        m "Wow… this is so cool…" 
        play sound "music/sfx/phone_ringing.ogg" 
        y "Again?" 
        "Given their success, she wonders if it might be their investor, but when she checks her phone, the caller is the director of the voice acting studio." 
        stop sound fadeout 1.0
        y "Hello?" 
        va_dir "Hello, Yukari. Have you seen what people are saying about [anime.name]?" 
        y "Yes! I can hardly believe it!" 
        va_dir "I watched the episode too, and the praise is well-deserved. Good job, Yukari. Congratulations!" 
        y "Thank you!" 
        va_dir "Please extend my congratulations to the rest of your team, as well. Oh, and when you're ready to record audio for your next project, please keep us in mind." 
        y "I will. Thank you again!" 
        "She relays his kind words to the others and takes a deep breath." 
        show yukari laugh_eyes_closed
        y "This is both exhausting and exciting."
        play sound sfx_rs_door_open
        yuu "That must be Sumiko's friends coming to celebrate with us." 
        scene studio_main
        show yukari at left
        show investor smile at right
        with dissolve
        investor "Close." 
        "They turn toward the door in surprise as their investor enters the studio." 
        investor "I was going to call, but when I saw how well people were reacting to [anime.name], I had to come over to congratulate you all in person." 
        y "Thank you!" 
        "Sumiko's friends arrive a moment later and nearly trip over the investor trying to get into the studio. They're all talking at once, too excited over [anime.name] to wait."
        "Yukari can understand their excitement. Not only did they get to watch something they contributed to on TV, but it's actually a success." 
        "Everyone is in high spirits. Yukari sets out food, and everyone spends the next hour celebrating the success of [anime.name] and their work together."
        "The bright atmosphere is punctuated by Shunsuke reading praise from reviews at regular intervals." 
        "At last, evening arrives, and the celebration winds down."
        investor "Well, I should be on my way. I look forward to Episode Two… and whatever you have in store next, of course." 
        s "Does this mean you'll invest in our next anime, too?" 
        yuu "Sumiko!" 
        show investor happy
        investor "Hahaha, I certainly hope to." 
        "After he leaves, Sumiko's friends follow, and Yukari turns to her team members." 
        scene studio_main with fade
        show yukari happy at pos_left
        show sumiko at pos_middleright
        show yuuko at pos_right behind sumiko
        show shunsuke at pos_outerright
        show mayumi at pos_farleft behind yukari
        with dissolve
        y "It sounds like we're set on making another anime, then?" 
        ss "Did you or did you not promise to let me write a sequel if things went well?" 
        y "Did I?" 
        ss "More or less." 
        show mayumi laugh_eyes_closed
        m "And Yukari would never break a promise!" 
        show sumiko laugh_eyes_closed
        s "Or let down all our new fans!" 
        show yuuko laugh_eyes_closed
        yuu "Or disappoint our investor." 
        show yukari happy
        y "Calm down, everyone, you don't have to convince ME. Creating anime is my dream, after all." 
        m "Then we're going to do it?" 
        y "…Yes. Absolutely." 
        "She knows it isn't as simple as all that—they'll need time to rest, for one thing, and they'll have to decide what to do once their vacation ends — but with how she feels now, Yukari sees a bright future ahead for her team." 
        scene home_night with fade
        show yukari at left with dissolve
        "As soon as she gets home, she calls her grandmother on the phone. After all, it was her grandmother who gave them the boost they needed by becoming their first investor." 
        "Her grandmother enjoyed Episode One of [anime.name], and Yukari is thrilled to tell her that the majority of people who watched it agree. However, while that was the dream she set out to fulfill, Yukari knows it isn't finished yet." 
        "Ever since she was a child, she dreamed of becoming an anime director. Now it's come true. She made [anime.name], and people love it. Now it's time for the next step." 
        "She doesn't want only a single anime credit to her name. Once they work out the details, she can start planning her next anime. And the next." 
        "Come what may, Yukari and her anime studio will press forward until they make their mark on the anime industry." 
    elif anime_score >= ANIME_MIN_AMAZING_VALUE:
        show yukari surprised
        "Her eyes widen, and she stares at the screen in shock." 
        m "What is it?"
        play music casual_music fadein 1.5 fadeout 1.5
        y "S-so… many people…" 
        yuu "So many people what?" 
        $achievement.grant("ACH_8")
        $achievement.grant("ACH_9")
        "Wordlessly, Yukari waves her hand at the computer. Everyone online is talking about [anime.name]."
        "Lots of people tuned in to check out the first episode, and almost all of them loved it. Fans are abuzz with speculation on where the story will go in the second episode and whether or not more will follow if [anime.name] does well." 
        show sumiko laugh_eyes_closed
        s "Whoa! We're famous!"
        ss "I wouldn't go that far, but we've definitely created a stir. Hmm… I wonder if there are any full reviews out yet."
        show yukari
        y "I'll check."
        play sound "music/sfx/phone_ringing.ogg" 
        y "Or not." 
        ss "You handle the phone, I'll look for reviews." 
        "Yukari takes out her phone. The call is from the director of [anim_studio]. Of course! He must have heard the news already. She feels as though she's on top of the world as she answers it." 
        stop sound fadeout 1.0
        y "Hello?" 
        if anim_studio == anim_studio_expensive: 
            anim_dir "Congratulations!" 
            y "Thank you!" 
            anim_dir "We've already received messages about [anime.name], even though we just handled the animation, so your own fan mail should begin arriving soon." 
            show yukari surprised
            y "F-fan mail? Really?" 
            show mayumi laugh_eyes_closed
            m "Ah! He's right, Yukari! Look at all these emails!" 
            "Yukari stares at the computer screen Mayumi indicates and feels like she might pass out. They are indeed getting fan mail." 
            y "Whoa…" 
            anim_dir "I regret being unable to celebrate with you at a time like this, but I wanted to at least call and congratulate you. It's safe to say [anime.name] is a major success." 
            show yukari
            y "I'm still a little dazed…" 
            anim_dir "I understand. Anyway, I'm sure you'll continue to work on anime after this. I hope you'll keep our studio in mind when you're ready to begin your next project." 
            y "Oh! Yes, absolutely!" 
            anim_dir "Congratulations again, Yukari, and pass it on to the rest of your team." 
        elif anim_studio == anim_studio_cheap:
            anim_dir "Have you seen what people are saying about [anime.name]?" 
            y "Yes! I'm still a bit shocked, to tell you the truth." 
            anim_dir "Me too! Err, not that I had any doubts. I mean… congratulations!" 
            y "Thank you!" 
            anim_dir "No, thank YOU. This will do wonders for our image! Brace yourself, world, [anim_studio] is back! Ahahaha! Now I don't even regret taking a break from my work to watch the episode today." 
            y "Oh, you watched?" 
            anim_dir "Yep, and now we're further behind than ever, but don’t worry. I can tell things are about to turn around for us." 
            y "I hope so." 
            show mayumi laugh_eyes_closed
            m "Aah! Yukari! Your email is filling up with messages from fans!" 
            "Yukari looks at the computer screen her friend is pointing to and feels like she might pass out. She's right. Several emails have already arrived filled with praise for [anime.name]." 
            anim_dir "Sounds like your party's already begun." 
            y "Well, not exactly." 
            anim_dir "I wish I could be there… but I won't hold you up any longer. Keep us in mind for your next anime, Yukari!" 
            y "Oh! I will." 
            anim_dir "Congratulations again to you and your team!"
        show mayumi 
        y "Thank you!" 
        "She ends the phone call and turns to the others." 
        y "That was the director of [anim_studio]. He wanted to congratulate us all on [anime.name]." 
        yuu "Aw, it was nice of him to call." 
        y "Yes, and—" 
        play sound "music/sfx/phone_ringing.ogg"
        show sumiko happy 
        s "I be that's a fan!" 
        y "Fans shouldn't have this number. Let me see…" 
        stop sound fadeout 1.0
        "With how successful the first episode appears to be so far, she expects to hear from their investor, but instead, it's their voice acting director on the phone." 
        y "Hello?" 
        va_dir "Congratulations! [anime.name] is a hit!" 
        y "Thank you! I can hardly believe people love it so much." 
        va_dir "I watched the episode, and I'm not surprised at all. It turned out fantastic. Good work." 
        y "Thanks." 
        va_dir "Have you considered continuing the story with a sequel? We should be able to get the voice actors back together." 
        y "We don't have any immediate plans, but I'll keep that in mind." 
        va_dir "Great! Congratulations again, and please extend my congratulations to the rest of your studio." 
        y "I will. Thank you!" 
        "She hangs up and tells the others what he said." 
        s "With all this talk of a sequel, I'm fired up already!"
        yuu "Oh… we need a little rest before jumping straight into another project, don't we?" 
        m "Of course we do. Besides, we need to look ahead and see how we want to plan out our futures. We shouldn't rush into anything." 
        s "Huh. I expected Shunsuke to be the one to say things like that." 
        show shunsuke laugh_eyes_closed
        ss "Listen to this!" 
        "From his sudden outburst, it's clear he didn't hear what Sumiko said at all." 
        ss "This is from a major anime site. Ahem. '[anime.name] could be the surprise hit of the season. From its writing to its art direction, everything about it oozes style.'"
        show yukari happy 
        y "Wow! A major anime site, you said?" 
        ss "Yes, many sites have already covered it. Here's another: 'A new anime from an untried studio started by teenagers sounds like the recipe for disappointment. However, the first episode of [anime.name] was a joy from start to finish."
        "The only thing disappointing is that only one other episode is slated to air.'" 
        show mayumi laugh_eyes_closed
        m "This is so exciting!" 
        "While he continues to read excerpts from reviews, Yukari checks through the fan emails that arrived. Dozens of people want to know if the show will continue after its initial two episodes." 
        y "Wow… people really… love [anime.name]!" 
        s "You know what this means? Time to party! My friends will be here any minute." 
        y "Oh, right!" 
        "In all the excitement, she almost forgot she invited Sumiko's friends to celebrate with them in recognition of their animation work." 
        play sound sfx_rs_door_open
        yuu "That must be them."
        scene studio_main
        show yukari at left
        show investor at right
        with dissolve
        investor "Actually, it's me." 
        "They turn toward the door in surprise as their investor enters the studio. Yukari expected a call from him, but an in-person visit?" 
        show investor happy
        investor "I knew I made the right call when I invested in [anime.name]. One episode in, and it's already a runaway hit. Congratulations!" 
        y "Thank you!" 
        "She's already thanked so many people, she's starting to feel tired… but her exhilaration at having created a successful anime balances it." 
        investor "Do you intend to make a sequel?" 
        m "Wow, everyone wants to know about the sequel!" 
        investor "If you do, I plan to support it." 
        s "Aha, so you think [anime.name] will be pretty profitable, eh?" 
        yuu "Sumiko!" 
        investor "Hahaha. Well, I have another motive, too… I also watched the first episode, and I don't want to say goodbye to these characters after just one more." 
        y "We don't have any concrete plans yet, but we'll be in touch as soon as we know." 
        investor "I look forward to it." 
        "The studio door opens again and Sumiko's friends arrive. They barely glance at the investor in their excitement to discuss [anime.name]."
        "Some of them already received calls from former classmates and other acquaintances who saw their names in the credits. They also watched the episode themselves and love how it turned out." 
        y "I guess it's time to start celebrating!" 
        "She sets out food, but just as she finishes, a voice comes from the other side of the studio door." 
        unknown "Did you start the party without us?"
        show yukari surprised
        y "Huh? More people?" 
        m "The animation team from [anim_studio] couldn't make it, right? Who else did you invite?" 
        "After everything that happened, Yukari honestly can't remember who she mentioned the celebration to and who she didn't, so instead of answering, she goes to the door." 
        "To her shock, their three main voice actors stand waiting."
        if anime.category == Anime.HAREM:
            scene studio_main
            show yukari at left
            show va_a laugh_eyes_closed at pos_middleright
            show va_b laugh_eyes_closed at pos_outerright
            show va_sakura happy at pos_right
            with dissolve
            va_a_char "Surprise! Isn't this exciting?!" 
            va_b_char "Did you really think we could hear of [anime.name]'s success and not want to wish you well?" 
            va_c_char "People love the first episode so much! Congratulations!" 
            "Their happiness makes Yukari even happier than she was before. She steps back and waves a hand toward the studio." 
            show yukari laugh_eyes_closed
            y "Come on in, we were just about to start celebrating!" 
        elif anime.category == Anime.ACTION:
            scene studio_main
            show yukari at left
            show va_a laugh_eyes_closed at Position(xalign=0.55,yalign=1.0)
            show va_b laugh_eyes_closed at va_pos_b
            show va_c at va_pos_c
            with dissolve
            va_a_char "Congratulations on an excellent first episode!" 
            va_b_char "Is it all right if we join your celebration?" 
            va_c_char "I warned you I would watch [anime.name]." 
            "Even he doesn't startle Yukari for once, with how happy she is, and she waves them into the studio with a laugh." 
            show yukari laugh_eyes_closed
            y "Of course you're all welcome. We were just about to start." 
        elif anime.category == Anime.MYSTERY:
            scene studio_main
            show yukari at left
            show va_c happy at va_pos_c
            show va_b laugh_eyes_closed at va_pos_b
            show va_a shocked at Position(xalign=0.55,yalign=1.0)
            with dissolve
            va_a_char "I can't believe I play the lead role in the latest and greatest anime sensation!" 
            va_c_char "I prepared for this possibility by walking out onto stage during a rock concert, but this is even better!" 
            va_b_char "Congratulations! We watched the episode together and wanted to stop by right away." 
            "Their enthusiasm is infectious, and Yukari is happier than ever as she waves them toward the studio." 
            show yukari laugh_eyes_closed
            y "Thank you! We were just about to start celebrating, so you're just in time." 
        "She leads the three voice actors inside and introduces them to Sumiko, Yuuko, Shunsuke, the investor, and Sumiko's friends, since only Mayumi met them previously." 
        "After that, their celebration begins in earnest with food, soda, and a selection of bad movies Sumiko puts on despite fervent protests."
        "Once the party gets going, Yukari slips out to make a phone call. After all, there's one more person who made [anime.name] possible." 
        scene studio with fade
        show yukari at left with dissolve 
        grandma "Hello?" 
        y "Hi, Grandma. It's me, Yukari." 
        grandma "Yukari! I just watched the first episode of [anime.name]. That was wonderful!"
        grandma "I'm so proud of how far you've come. What happened to that little girl who used to share her secrets with me? How did that little girl create something so impressive?" 
        y "Haha, aw, it wasn't just me. I had a lot of help." 
        grandma "Yes, and I hope you introduce me to these friends of yours someday. I've met Mayumi, but none of the others." 
        y "I will." 
        grandma "Now, I'm sure you didn't call me just to find out if I watched the episode or not." 
        y "Nope. I wanted to tell you the good news. [anime.name] is a hit! People are talking about it all across the Internet, and they love it!" 
        grandma "That's wonderful!" 
        y "We want to keep going and make more. This is it, Grandma. I'm an anime director. My dream is coming true." 
        grandma "I'm so happy for you, Yukari." 
        y "We could never have done it without you. You gave us our start and made [anime.name] possible. Thank you." 
        "She promises to visit her grandmother soon to discuss [anime.name] in more detail, and then she returns to the studio."
        "The celebration lasts into the evening, and by the time the guests begin trickling back out of the studio, Yukari feels like she might drop from exhaustion at any moment." 
        "Still, whenever she thinks about [anime.name]'s success, she's so excited she feels she won't be able to sleep a wink." 
        scene studio_main with fade
        show yukari at pos_left
        show sumiko at pos_right
        show yuuko at pos_outerright behind sumiko
        show shunsuke laugh_eyes_closed at pos_middleright
        show mayumi at pos_farleft behind yukari
        with dissolve
        y "We did it, everyone. We really did it."
        show mayumi happy
        m "I knew we could!" 
        ss "Unless something goes wrong with the second episode, I suspect we will have much greater support for our future endeavors." 
        y "We're continuing on, then?" 
        s "Huh? Was it ever in doubt?" 
        y "This was a long and tiring journey for all of us. Making anime is my dream, but I can't drag you back into this if you aren't ready." 
        show yuuko laugh_eyes_closed
        yuu "Don't worry, Yukari. We need a little time, but after that… I know I'd love to make another anime with you." 
        s "Yeah, you can't get rid of us that easily!" 
        ss "I have an outline for the sequel's storyline already prepared." 
        m "What do you say, Yukari?" 
        "Yukari looks at her four friends and feels more joy than when she saw the viewer reactions to [anime.name]. She has the best friends in the world… and the best team anyone could ask for. She couldn't have done it without them." 
        show yukari laugh_eyes_closed
        y "I say, let's do this! [anime.name] is a hit, and our next anime will be even better!" 
        "It was a difficult journey, but they overcame every obstacle ahead of them. And as long as she has these four on her side, Yukari knows she can overcome anything the future holds. Her dream of being an anime director has only just begun." 
        "Over the next few days, positive feedback continues to pour in. [anime.name] is a runaway hit, with people talking about it all across the Internet. It even spawns a meme." 
        "They begin discussing the details of their next project sooner than Yukari expected. Shunsuke has more story ideas than he knows what to do with. Yuuko starts sketching potential character designs in her spare time."
        "Sumiko presents Yukari with a new background, 'just in case' they need one soon. Mayumi cuts straight to the chase and asks when they can begin work." 
        "Three months earlier, Yukari wasn't sure they could handle the stress and pressure of creating an anime. Now she knows they can." 
        "This is the start of a bright future for Yukari… and her anime studio." 
    ### BETA TESTING ###
    # menu:
    #     "Beta Testing, remember to inform me about what anime score you got and Screenshot It)":
    #         pass
    # "Anime score is [anime_score]"
    # "Remember to let me know of your final score, since this is a beta test!"
    ######################
    $achievement.grant("ACH_4")
    if anime.category == Anime.HAREM:
        $achievement.grant("ACH_5")
    elif anime.category == Anime.ACTION:
        $achievement.grant("ACH_6")
    elif anime.category == Anime.MYSTERY:
        $achievement.grant("ACH_7")
              
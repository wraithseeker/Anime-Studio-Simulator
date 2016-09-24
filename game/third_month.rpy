label week_9_1:
    scene studio_main with fade
    show yukari laugh_eyes_closed at left
    show yuuko at right
    with dissolve
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
                y "The first song. [anime.name] has a light tone throughout, so even the “serious” music should have a happy feeling." 
            "The second song":
                y "I like the second song better. The first one didn’t sound serious enough to me." 
            "The third song":
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
                y "The first song really makes me feel energized. That’s what the mood should be like." 
            "The second song":
                y "Since there’s a lot of action, let’s go with the second song. The first one sounded too happy for [anime.name]."  
            "The third song": 
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
                y "I like the first one. It will really drive home those dark moments."  
            "The second song":
                y "Well, it may not be the darkest song, but I can’t help but like the second song’s tone for [anime.name]."   
            "The third song": 
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
    scene studio_main with fade
    show sumiko laugh_eyes_closed at right
    show yukari at left
    with dissolve
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
        "Professional Website":
            ss "Excellent decision. Since we’re an unknown studio, we want everything about [anime.name] to be as professional as possible. I’ll look into hiring someone to make our website." 
        "Website made by Shunsuke":
            ss "Thank you for your confidence in my skills. I hope I can live up to it. I’ll get back to work, then."
        "Free Website":
            ss "Since we have limited funds to work with, I suppose we shouldn’t spend too much on the website. I’ll look online for a suitable template." 
    show yukari happy
    y "Thanks, Shunsuke!" 
    "With their plan for the website decided, everyone gets back to work. Yukari contacts Sumiko’s friends to check on their progress."
    "To her delight, they’re almost done with their work on the first episode already, and they ask if they can meet with her the next morning about it." 
    "For once, everything is going well."
label week_9_3:
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

label week_9_4:
    scene home with fade
    show yukari at left
    with dissolve
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
    scene studio_main with fade
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    show sumiko at va_pos_c
    show yuuko at pos_outerright
    with dissolve
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
    scene home with fade
    show yukari at left with dissolve
    "When the weekend arrives, Yukari tries to decide the best use of her time." 
    menu:

        "Shop for a gift for the sisters":
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
            "With [anime.name] almost completely, they’ll need to begin marketing in full force."
            "Yukari spends the weekend reading marketing books and taking notes on possible strategies to try." 
            $wk_9_forgot_home = True
        "Relax": 
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
       
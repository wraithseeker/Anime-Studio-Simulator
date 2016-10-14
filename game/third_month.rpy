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
    $nextDay()
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
            $website_choice = "Professional" 
        "Website made by Shunsuke":
            ss "Thank you for your confidence in my skills. I hope I can live up to it. I’ll get back to work, then."
            $website_choice = "Shunsuke"
        "Free Website":
            ss "Since we have limited funds to work with, I suppose we shouldn’t spend too much on the website. I’ll look online for a suitable template." 
            $website_choice = "Free"
    show yukari happy
    y "Thanks, Shunsuke!" 
    "With their plan for the website decided, everyone gets back to work. Yukari contacts Sumiko’s friends to check on their progress."
    "To her delight, they’re almost done with their work on the first episode already, and they ask if they can meet with her the next morning about it." 
    "For once, everything is going well."
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
    $nextDay()
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
    $nextDay()
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
        scene studio 
    scene studio 
    $nextWeek()
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_10_1:
    scene studio_main with fade
    show yukari at left
    with dissolve
    $anim_studio = anim_studio_cheap
    $anime.category = Anime.ACTION
    $wk_9_forgot_home = True
    #phone ringing sound
    "Yukari answers her phone." 
    scene black with fade
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
                y "Let's reuse scenes from [anime.name]." 
                "With their budget, it doesn't feel right to go the more expensive route, even at a discount."
                "Besides, as long as they pick good scenes, it should still appeal to their target audience." 
                $trailer_choice = "Reuse"
            "Create new animations for the trailer.": 
                #($$) (If Harem, no effect)  
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
        #[explosion sound effect] 
        show sumiko laugh_eyes_closed
        s "I like it." 
    elif anime.category == Anime.ACTION:
        show yukari sigh
        y "Not every story needs explosions."
        show sumiko sad_angry
        s "But there's tons of action!" 
        m "I don't have an explosion, but I have some gunshots." 
        ss "That sounds pretty good." 
    elif anime.category == Anime.MYSTERY:
        show shunsuke sigh
        ss "Where would there possibly be an explosion in [anime.name]'s story?" 
        s "Isn't there a scene where the protagonist hears a loud noise?" 
        m "That loud noise isn't an explosion, though. It's made by boxes falling on the ground." 
        ss "Much more fitting for the story." 
    show shunsuke
    show yukari
    show sumiko
    y "What other sound effects do you have ready?" 
    m "Here are two more." 
    if anime.category == Anime.HAREM:
        pass
        # [mixing liquids sound effect] 
        # [flask breaking sound effect] 
    elif anime.category == Anime.ACTION:
        pass
        # [car driving/engine sound effect] 
        # [tires squealing sound effect] 
    elif anime.category == Anime.MYSTERY:
        pass
        # [mysterious footsteps sound effect] 
        # [stabbing sound effect] 
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
     #[random event] 

label week_10_5: 
    $nextDay()
    scene black with fade 
    $anim_studio = anim_studio_cheap
    $anime.category = Anime.MYSTERY
    "As promised, Yukari visits the animation studio on Friday to meet with the director about the trailer." 
    if anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari at left
        with dissolve
        staff "It's good to see you again, Yukari. [anim_studio_dir] is expecting you. I'll let him know you're here." 
        y "Okay." 
        #door sound
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
        #[door sound] 
        show anim_dir at right with dissolve
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
    #----- 
    scene studio with fade
    show yukari laugh_eyes_closed at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve 
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
    scene home with fade
    show yukari at left with dissolve
    "When Yukari checks her email on the weekend, she finds a request from the media. A journalist who covers anime news would like to interview her." 
    "Yukari thinks it over and decides to…" 
    menu:
        "Accept the offer": 
            scene black with fade
            #If (1) and the anime marketing level + yukari proficiency & management level high, 
            "The next day, she meets with the journalist to discuss [anime.name]. She prepared for possible questions ahead of time, and none of the questions are too tricky."
            "Yukari leaves the interview feeling satisfied with how it turned out." 
            "By evening, she has a few emails from people who already read the interview and are excited for [anime.name]."
            "It's causing a stir on a few anime forums, too. It seems like media coverage was just what they needed to give [anime.name] a nice boost in publicity." 
            #If (1) and anime marketing levels and such are not high enough,  
            #"The next day, she meets with the journalist to discuss [anime.name]. The questions aren't too bad, and Yukari handles herself well." 
            #"Unfortunately, even though the interview is online by evening, it doesn't seem to attract much interest."  
          
        "Decline the offer":
            "An interview could have helped [anime.name]'s publicity, but Yukari isn't ready to deal with the media just yet."
            "Instead, she spends the weekend researching other potential ways to promote [anime.name] and going over their schedule to see what they still need to do before the deadline." 
    scene studio 
    $nextWeek()
    $mayumi_tasks[0] = mayumi_fifth_task
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_11_1:
    scene studio with fade
    show yukari at left
    show shunsuke at right
    with dissolve
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
    $anim_studio = anim_studio_cheap
    if anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari happy at left with dissolve
        y "Hello!" 
        staff "It's good to see you again, Yukari. Are you here to pick up the first episode of [anime.name]?" 
        y "That's right." 
        staff "I'll let [anim_studio_dir] know you're here." 
        #[door sound] 
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
    y "Here it is!" 
    ss "Episode One?" 
    y "Yep!" 
    show sumiko happy
    s "What? Where? I want to see it!" 
    show mayumi laugh_eyes_closed
    m "Me too! I'm nervous about how it'll be…" 
    y "Give me a minute to set it up, and then we can all watch it together!" 
    "She puts the disc into her computer. Everyone gathers around to watch the video." 
    #[a cg of everyone staring at the computer screen (anime episode) ] 
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
    #[end CG]
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
    #[phone ringing] 
    y "Just a minute." 
    hide shunsuke with dissolve
    "She steps away from the desks so she can answer the phone without disturbing anyone. The caller is one of Sumiko's friends, and she braces herself."
    "Any unexpected call could mean bad news. However, the news is good for a change! They've finished all of their tasks." 
    show yukari happy
    y "Good work! I'll drop by on Thursday to collect it. By the way, we're going to have a party after [anime.name] airs…" 
    "Once she tells Sumiko's friend about the party, she hangs up and returns to her desk."
    show yukari at left
    show shunsuke at right with dissolve
    ss "Something important?" 
    show yukari happy
    y "Our freelance animation work is complete!" 
    #[phone ringing] 
    show yukari surprised
    y "Another call, already?" 
    ss "Maybe they forgot something." 
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
     #[random event]  
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
     #[random event] 
# [weekend] 
label week_11_6:
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
    play music "music/ost/scheduled_days.ogg" fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    call screen start_game
    stop music fadeout 1.0
    $fastForwardDays(2)
               
label week_5_1:
    scene studio with fade
    show yukari at pos_left
    show sumiko happy at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    s "I just realized it's been one month since we started working on [anime.name]!"
    s "We still have about two more months left to go before our deadline."
    yuu "I can't wait for the day we can see [anime.name] on air."
    s "I know, right? It’ll be crazy!"
    m "Before the two of you drift off to dreamland, remember we still have plenty of work to do."
    m "Yukari, have you started looking at which studio we'll work with yet?"
    y "I narrowed the list down to a couple of studios, but I'm not sure how I should get in touch with them."
    y "Should I email them or visit their offices?"
    m "Why not both? You could email them first and then set up a meeting."
    ss "Yes, it might confuse them if you walk in randomly. I wouldn’t recommend it."
    m "Plus, if you plan it with them first, you’ll have an agenda set for the meeting."
    y "Good idea, I'll get started on it right away."
    scene home_night with fade
    show yukari at left with dissolve
    "That night, Yukari checks her email and notices some of the animation studios have sent replies. She shortlists the two most promising ones."
    "[anim_studio_expensive] is renowned for high production quality, but hiring them will come at a steep price."
    "If they hire [anim_studio_expensive], [anime.name] will definitely have great animations, but it might not be worth it."
    "It’s a lot of money to devote to a single aspect of production, and the budget isn’t exactly huge." 
    "On the other hand, [anim_studio_cheap] is relatively new in the industry. Although they’ve produced a number of hit titles, their price is quite affordable."
    "The lower price is probably due to their decline this year, after their recent works weren’t well-received by the public."
    "It could be an ideal, affordable opportunity for [anime.name], but [anim_studio_cheap] has developed a reputation for low production quality and missed deadlines. Many fans believe it will close down soon."
    "It's a difficult decision for Yukari to make, and not one she should make alone. She sends text messages to the other team members asking which studio they think she should pick."
    "Unfortunately, when the votes come in, it’s a tie."
    "Mayumi and Yuuko want to go with [anim_studio_cheap] out of concern for their budget."
    "Shunsuke and Sumiko think it’s safer to pick [anim_studio_expensive] for its high quality and stability."
    "Yukari didn’t want to decide, but she has no choice. Hers is the deciding vote."
    "Which studio should she get in touch with?"
    menu:
        "[anim_studio_expensive] {space=15}{image=small_moneybag.png} [EXPENSIVE_STUDIO_FUNDS_VALUE]":
            $choice_5_1_1()
            "Yukari decides to get in touch with [anim_studio_expensive]."
            "Working with a studio renowned for its production quality will help save them a lot more money in the long run."
            "They will have proper procedures and guidelines during the production process which will definitely be a great help to the inexperienced team."
            "Best of all, it will ensure [anime.name] has top-notch animation."
            $anim_studio = anim_studio_expensive
        "[anim_studio_cheap] {space=15}{image=small_moneybag.png} [CHEAP_STUDIO_FUNDS_VALUE]":
            $choice_5_1_2()
            "Yukari decides to get in touch with [anim_studio_cheap]."
            "Despite the studio’s recent slump, her research suggests it’s only due to poor management. If she manages the team effectively, she’ll be able to turn things around for everyone."
            "The main selling point, of course, is the competitive price." 
            "[anim_studio_cheap]’s quality can be hit-and-miss, so Yukari will need to pay extra attention to them if she wants things to go smoothly."
            $anim_studio = anim_studio_cheap
    $rd_e_holder.emptyList(rd_e_holder.wk_4)
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10])
    call expression random_game_event from _call_expression

label week_5_2:
    $nextDay()
    scene studio with fade 
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    ss "So which animation studio did you pick?"
    y "[anim_studio]. I'll be heading over there later with Mayumi for a consultation."
    show mayumi surprised
    m "Ehh?? I thought we were only picking which studio to work with. No one told me anything about going to visit them."
    y "I was planning to tell you later."
    show mayumi sigh
    m "Why do you want me to go there with you? What difference does it make?"
    show yukari tsundere
    y "Isn't it obvious? I feel more at ease when you're with me."
    m "I thought you were getting good at this stuff. Look at how you clinched the deal with the investor last week!"
    show yukari
    y "That was an exception. I got lucky, and this time it involves dealing with a lot more people. I’ll feel a lot better if you come with me."
    show yukari sad
    y "Please?"
    m "Okay, okay, I'll go with you if it makes you more confident."
    show yukari
    y "While we’re gone, it’ll be a good time for Sumiko and Yuuko to familiarize themselves with the storyboards."
    y "Can I leave that up to you, Shunsuke? You should have a good idea of how things should flow, since we worked on the storyboards for [anime.name] together."
    show shunsuke laugh_eyes_closed
    ss "Of course. You just focus on making sure the meeting with [anim_studio] is a success."
    ss "Remember not to panic."
    show yukari sad_angry
    y "That’s not as easy as you think... but I'll try my best."
    "Yukari gathers the documents she wants to take to [anim_studio], double-checks that everyone knows what they’re doing, and heads out with Mayumi."
    scene street with fade
    show mayumi_f at right
    show yukari at left
    with dissolve
    m "So where is the studio, anyway?"
    y "Hmm?"
    m "The studio. Where is it?"
    show yukari worry
    y "Oh, it’s…"
    "She trails off. She’d rather not admit that she was so nervous about setting up the meeting and preparing for it, it she forgot to check the address."
    "She looks around for inspiration, and her gaze lands on the café doors."
    show yukari happy
    y "Hey, do you want to grab a bite to eat on the way?"
    m "Huh? Um, sure, if we have time…"
    y "Wait here!"
    "Yukari leaves her on the sidewalk and runs into the café."
    scene cafe with fade
    show yukari at left with dissolve
    manager "Ah, one of my best customers! What can I do for you?"
    y "I’d like to order something quick we can take on the go, but that’s not important right now. Do you know how to get to [anim_studio]?"
    manager "Yes, actually. Make a left at the corner, and then—"
    show mayumi_f at right with dissolve
    m "Yukari!"
    show yukari surprised
    y "Agh! W-when did you get here? I thought I told you to wait!"
    m "You were acting weird, so I followed you."
    show yukari sad
    y "Right, well I was just… uh…"
    "She raises her voice and gives the café manager a meaningful look."
    show yukari laugh_eyes_closed
    y "That’s right, we’d love to try your newest flavor of doughnuts!"
    manager "What about the directions to [anim_studio]?"
    "Some people don’t know how to take a hint."
    show mayumi_f sigh
    m "Oh, Yukari…"
    scene street with fade
    show yukari happy at left
    show mayumi_f at right
    with dissolve
    y "Look at it this way. We know where we’re going, AND we have food. What could be better?"
    show mayumi_f tsundere
    m "Knowing where to go from the start..."
    y "Come on, it’s this way."
    m "Are you sure? You aren’t going to suddenly bolt into a store shouting that you need to buy something?"
    show yukari sigh
    y "Very funny. Let’s go."
    scene animation_studio with fade
    if anim_studio == anim_studio_expensive:
        show yukari at left
        show mayumi_f at right
        with dissolve
        y "That's weird, why isn’t anyone at the reception desk?"
        "She looks around for any sign of life and can’t help but be impressed."
        y "This place is exquisite. Our studio looks dull in comparison!"
        m "Well, they have enough funds to splurge on designing their workplace. It’s not like we can…"
        "She trails off."
        y "Mayumi?"
        show mayumi_f happy
        m "Wait… Look at THOSE NENDOROIDS!"
        "She runs to the reception desk, where five Nendoroid figurines sit."
        m "They’re so adorable!"
        y "I don’t know… They look pretty generic to me."
        show mayumi_f tsundere
        m "Are you crazy?"
        show yukari sigh
        y "Let me guess, you’ll buy them on the Internet later. Old habits die hard."
        y "This is why your room doesn't have enough space!"
        m "Pffft... You don't appreciate Nendoroids enough."
        "Footsteps echo from deeper within the studio. Someone must finally be coming. A few seconds later, the door behind the reception desk opens."
        play sound sfx_anim_d_open
        scene animation_studio
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        with dissolve
        staff "Hello! What brings you to [anim_studio_expensive] today?"
        staff "Oh! I see you’ve taken a liking to those Nendoroids. They’re from Grim Grim, which is our most popular anime series so far."
        show mayumi laugh_eyes_closed
        m "Yes, I love them!"
        staff "This is a special set produced for us, so they’re not for sale, in case you were hoping to purchase them."
        show mayumi sad
        m "Aw, what a letdown."
        staff "Back to the matter at hand, what brings the two of you here today? Do you have an appointment with someone?"
        show mayumi
        y "My name is Yukari. We’re here to discuss a potential partnership with [anim_studio_expensive], as mentioned in the email I sent you yesterday."
        staff "Ah! So you’re the one who emailed us. I expected someone older."
        staff "Both of you look like you got out of high school not too long ago."
        y "We did graduate recently, but we decided to take some time to work on an anime called [anime.name]."
        staff "Unusual though it may be, you seem to know your stuff well despite your age. Please give me a moment while I call [anim_studio_dir]. He’ll discuss the details with you."
        show anim_dir smile at right with dissolve
        anim_dir "Well, hello there! I’ve been expecting you, Yukari!"
        anim_dir "My name is [anim_studio_dir] and I'm the director of [anim_studio_expensive]."
        "He reaches out, and Yukari shakes his hand."
        y "Nice to meet you! My team is currently producing an anime series, and we’d like to work with you on the animation."
        anim_dir "Ah, yes"
        "He leads her to a small table where they can sit and talk."
        anim_dir "I’m looking forward to learning about your project."
        y "Here is a general outline of [anime.name] and what we’ll need from you."
        "Yukari unzips her bag and takes out the relevant documents. She passes them to [anim_studio_dir], who takes a brief look through the pages."
        anim_dir "Very clear and concise. I like the way your team works."
        show yukari happy
        y "Thank you."
        anim_dir "Do you have any animation samples that we can use as a reference?"
        show yukari worry
        y "Um, yes… aren’t they in the documents I gave you?"
        "The director looks through the pages again."
        anim_dir "I can’t find them."
        "Yukari’s breath hitches. If she somehow forgot them… but no, she couldn’t have. She remembers picking them up before she left."
        y "Hold on, let me check my bag."
        "She searches her bag and finds another stack of papers. With a sigh of relief, she straightens and holds them out."
        y "Here are the animation samples. Sorry about that."
        "[anim_studio_dir] looks them over."
        anim_dir "Perfect, this will do as a reference. However, if you choose to work with us, I’d like you to make your storyboards clearer."
        anim_dir " At the moment, they feel vague. We’ll need a better idea of the direction the episode should take."
        show yukari
        y "Got it. No problem."
        anim_dir "Now, are there any questions you’d like to ask us?"
        y "Nothing at the moment. We’ll get in touch soon with our decision. Thank you for your time!"
        scene street with fade
        show yukari at left
        show mayumi_f sigh at right
        with dissolve
        m "So… tell me again why you needed me to come along?"
        y "I felt better just knowing you were by my side."
        m "Seriously? Sometimes I wonder about you…"
    elif anim_studio == anim_studio_cheap:
        show yukari worry at left
        show mayumi_f at right
        with dissolve
        y "That's weird, why isn’t there anyone at the reception desk?"
        m "Maybe they’re out for lunch."
        y "That doesn’t make sense. It’s not lunch time."
        m "So? Maybe their lunch break is at an unusual time."
        y 'Why?'
        m "Don’t ask me. It doesn’t even matter, does it? Let’s try calling for someone."
        show yukari
        "Yukari looks around for a bell or some other way to call, but Mayumi has her own idea. Before Yukari can stop her, she cups her hands around her mouth."
        m "Hey, is anyone from [anim_studio_cheap] here right now?"
        m "Mayumi!"
        play sound sfx_anim_d_open
        "The door behind the reception desk opens and a casually-dressed man steps out."
        scene animation_studio
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        show anim_dir at right 
        with dissolve
        unknown "Hello! What brings you here today?"
        "We have an appointment scheduled with [anim_studio_cheap] today to discuss a potential partnership."
        unknown "Oh! Is that so? My bad, I totally forgot about it. I’m [anim_studio_dir], the director of [anim_studio_cheap]."
        "Yukari tries not to cringe at the fact that the director forgot about their meeting. She reminds herself that working with [anim_studio_cheap] is the best option for their team."
        anim_dir "Could you tell me more about your project?"
        y "Sure! Here is a general outline of [anime.name] and what we’ll need from you."
        y "Yukari unzips her bag and takes out the relevant documents. She passes them to [anim_studio_dir], who glances through them."
        anim_dir "Looks good. So, we probably should have some animation samples to use as a reference."
        show yukari worry
        y "Aren’t they in the documents I just gave you?"
        show anim_dir frustrated
        anim_dir "Oops, did I overlook something again?"
        y "(thinking to self): Again?!"
        show anim_dir
        "The director looks through the pages more closely."
        anim_dir "Actually, it’s not me for once. They’re not here."
        "Yukari’s breath hitches. If she somehow forgot them… but no, she couldn’t have. She remembers picking them up before she left."
        y "Hold on, let me check my bag."
        "She searches her bag and finds another stack of papers. With a sigh of relief, she straightens and holds them out."
        show yukari
        y "Here they are. Sorry about that."
        anim_dir "No worries. This will be fine."
        y "Is there anything else you’ll need from us if we work together?"
        anim_dir "Hmm… Could you make the storyboards clearer? We might be able to work with them like this, but they’re a little too vague right now."
        y "I’ll take care of it."
        anim_dir "Great! Do you have any questions for us?"
        y "Nothing at the moment. We'll get in touch soon with our decision. Thank you for your time!"
        scene street with fade
        show yukari at left
        show mayumi_f sigh at right
        with dissolve
        y "Well, he seems nice."
        m "Yeah… I’m not sure he’s the most organized person, though…"
        y "Don’t worry, I plan to keep a close eye on things."

label week_5_3:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    "The next day, Yukari takes a look at the storyboards. They seem fine to her."
    y "Shunsuke, do you have a minute?"
    ss "Sure, what is it?"
    y "The director from [anim_studio] said I need to make the storyboards clearer. What do you think is wrong with them? "
    if anime.category == Anime.HAREM:
        scene storyboard_harem with fade
    elif anime.category == Anime.ACTION:
        scene storyboard_action with fade
    elif anime.category == Anime.MYSTERY:
        scene storyboard_mystery with fade
    ss "Hmm… I don't see a problem with them, either, but then again we're looking at it from our perspective."
    y "What do you mean?"
    ss "We know everything about [anime.name], so we know exactly what we’re looking at. He doesn’t, because he’s seeing it for the first time."
    ss "Include more details so it’s clear without prior knowledge of [anime.name]."
    ss "If you need to write some notes on the storyboard to get your idea across, go ahead and do it."
    y "Just… write on the storyboards?"
    ss "Why not? That should clear up his confusion."
    scene studio_main with fade
    show yukari laugh_eyes_closed at left
    show shunsuke at right
    with dissolve
    y "Nice, I like the way you think! I’ll start editing the storyboards now. Thanks!"
    ss "Anytime."
    "Yukari spends some time working on the storyboard. Between Shunsuke’s advice and some input from Mayumi, she feels she’s on the right track."
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10])
    call expression random_game_event from _call_expression_1

label week_5_4:
    $nextDay()
    scene studio_main with fade
    show yukari at left with dissolve
    y "Well, unless anyone objects to working with [anim_studio], I guess I should head over there."
    "She glances at Mayumi."
    show mayumi_f at right with dissolve
    m "Yes, I guess you should."
    y "Want to come with me?"
    m "You’ll be fine."
    show yukari sad
    y "But—"
    m "You were fine last time. Don’t worry so much!"
    y "Okay, I guess you’re right."
    "She checks to make sure no one on the team needs her for anything before she leaves, and then she heads to the animation studio."
    play music cafe_music fadein 2.0 fadeout 2.0
    if anim_studio == anim_studio_cheap:
        scene animation_studio with fade
        show yukari at left with dissolve
        "The reception desk is empty again when Yukari arrives, but before she can worry too much or consider calling out to see if anyone is around, the door opens and the director steps out."
        show anim_dir smile at right with dissolve
        anim_dir "Hello, Yukari! So, have you guys decided on who to work with to produce animation work for your team?"
        "It’s an unexpected question since Yukari never reached out to any other studios besides [anim_studio_cheap]. Then again, he’d have no way of knowing that."
        y "Yes, we’d like to work with [anim_studio_cheap]."
        anim_dir "Great! Just give me a moment while I have my assistant print out the contract for our work."
        play sound [sfx_anim_d_open,sfx_anim_d_close]
        hide anim_dir with dissolve
        "He disappears behind the door again. Yukari can hear faint voices, but they aren’t clear enough for her to make out the words."
        show yukari worry
        "A little nervous now that their partnership is about to become official, she paces back and forth in front of the reception desk."
        "Is [anim_studio_cheap] the right choice? Will she be able to make things work out?"
        y "(thinking to self): If something goes wrong, what am I supposed to do?"
        play sound sfx_anim_d_open
        show anim_dir at right with dissolve 
        anim_dir "Sorry to keep you waiting. Here is the contract."
        "He hands the contract over to Yukari. She stares at it, overwhelmed."
        "She doesn’t know much about the legal side of things, but if she doesn’t look over the contract carefully, she could miss something that comes back to haunt them in the future."
        anim_dir "Just let me know when you’re ready."
        hide anim_dir with dissolve
        show yukari
        play sound sfx_anim_d_close
        "As the director leaves, Yukari reads through the contract. After she goes through it once, she decides to call Mayumi. Her friend knows more about legal matters than she does."
        play sound "music/sfx/dialing_numbers.ogg"
        "Yukari gets out her phone and dials Mayumi’s number."
        m "Hello?"
        y "I’m at [anim_studio_cheap] now. Mind if I go over the contract with you?"
        m "Go ahead."
        "She reads the contact out loud, with particular attention to the sections she’s most unsure about. Mayumi explains them to her and points out one or two they might want to have changed."
        show yukari surprised
        y "Changed? Can you do that?"
        m "Of course. You’re negotiating!"
        "She carefully goes over what Yukari should say to the director."
        show yukari 
        y "Thanks, Mayumi. You’re a life saver."
        m "Don’t mention it. Good luck!"
        "Yukari hangs up and approaches the door behind the reception desk. A little uncertain, she knocks."
        play sound sfx_anim_d_open
        show anim_dir at right with dissolve 
        anim_dir "Are you finished?"
        y "Yes, but there are a few matters I’d like to discuss with you first…"
        "The director is amenable to all the changes Mayumi suggested, but the process tires Yukari."
        "She can already telling working with [anim_studio_cheap] might be exhausting. At last, she signs the contract and returns it to the director."
        y "I'll be back tomorrow with the revised storyboards and all the documents you'll need to start working on [anime.name]."
        anim_dir "Sounds good. I'll see you tomorrow then."
    elif anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari at left
        with dissolve
        "This time, the staff member sits waiting at the reception desk. He smiles when Yukari enters."
        staff "One moment. I’ll let [anim_studio_dir] know you’re here."
        "Yukari clasps her hands in front of her and admires the Nendoroids Mayumi liked so much to calm her nerves. She only has to wait a minute."
        play sound [sfx_anim_d_open,sfx_anim_d_close]
        show anim_dir smile at right with dissolve
        anim_dir "Hello, Yukari! Well then, has your team decided upon a studio to work with for [anime.name]’s animation?"
        "It’s an unexpected question since Yukari never reached out to any other studios besides [anim_studio_expensive]. Then again, he’d have no way of knowing that."
        y "Yes, we’ve decided to work with [anim_studio_expensive]."
        anim_dir "I’m happy to hear that. If you’ll wait here a minute, I’ll get the contract for our work."
        hide anim_dir with dissolve
        play sound [sfx_anim_d_open,sfx_anim_d_close]
        "For the brief moment the door is open, Yukari hears faint voices, but once the door closes behind him, it’s as silent as when she and Mayumi first visited."
        "She can’t help but question her decision to work with [anim_studio_expensive]. High quality comes with a high price."
        "She definitely needs to make sure there aren’t extra revisions for the animation work, or they’ll be out on the streets in no time. Even the initial work will push the budget."
        show anim_dir smile at right with dissolve
        anim_dir "Sorry to keep you waiting. Here is the contract for our partnership."
        anim_dir "I recommend you take a good look at it, since you’re new to the anime business. You don’t want to miss critical details in the contract."
        "He hands over the contract to Yukari. She stares at it, overwhelmed. It’s a huge contract and it looks complicated. The director is right, she can’t afford to overlook important details."
        anim_dir "Read it over carefully and let my receptionist know when you’re ready."
        y "Thank you."
        hide anim_dir with dissolve
        "Yukari begins to read the contract. Partway through, she decides to call Mayumi. Her friend knows more about legal matters than she does."
        play sound "music/sfx/dialing_numbers.ogg"
        "Yukari gets out her phone and dials Mayumi’s number."
        m "Hello?"
        y "I’m at [anim_studio_expensive] now. Mind if I go over the contract with you?"
        m "Go ahead."
        "She reads the contract out loud. Mayumi asks her to repeat a few of the more complicated clauses, which makes the process take even longer than expected."
        "Along the way, she clarifies some of the language and calms Yukari’s concerns."
        m "Is that the end of the contract?"
        y "Yes, finally."
        "Her mouth is dry from speaking so much about the contract to Mayumi."
        m " Okay! It sounds like [anim_studio_expensive] has offered us a really good contract. Good luck, and go ahead and sign the papers."
        show yukari laugh_eyes_closed
        y "Thanks. You’re a life saver!"
        show yukari
        "She hangs up and approaches the reception desk."
        y "Would you let the director know I’m ready to sign the contract?"
        staff "Yes, one minute."
        play sound sfx_anim_d_open
        staff "Sir, Yukari is ready."
        show anim_dir happy at right with dissolve
        anim_dir "Wonderful! Is everything in order, then?"
        show yukari happy
        y "Yes. I’m quite happy with the contract."
        "She signs it and returns it to the director."
        show yukari
        y "Thank you. I'll be back tomorrow with the revised storyboards and all the documents you'll need to start working on [anime.name]."
        anim_dir "That sounds fine. I’ll see you tomorrow, then."

label week_5_5:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show sumiko at Position(xalign=0.87,yalign=1.0)
    show yuuko at pos_outerright behind sumiko
    with dissolve
    y "In case anyone forgot, I went back to [anim_studio] yesterday to sign the contract."
    y "I'll be heading over there later to provide them with the storyboards they need to start animating the first episode of [anime.name]."
    y "Yuuko, Sumiko, since they’ll be sharing the workload with you, do you have any questions about the arrangements?"
    s "Well, I mostly draw static backgrounds and am fine with those."
    s "But for complex animated backgrounds, I’ll need their help. I’m not too experienced with those kind of scenes."
    y "Okay, got it. What about you, Yuuko?"
    yuu "Is it possible for me to check their completed work? I want to make sure the animation is consistent throughout the episodes."
    yuu "I’d also like to communicate with them directly to make sure we’re on the right track."
    show yuuko laugh_eyes_closed
    yuu "Plus, it will be cool to talk to people in the industry. Maybe I'll pick up new skills from them!"
    yuu "I really liked one of the series they animated last season. It provided me with a lot of inspiration."
    "Her enthusiasm surprises Yukari. It’s rare to hear Yuuko talk so much."
    show yukari happy
    y "Of course I'll let you check their work. After all, you're our character designer! You have the best eye for picking out any inconsistencies."
    y "As for direct communication, I'll talk to them about it. Don’t get your hopes up too high, though, since I’m not sure whether they’ll like the idea."
    show yuuko
    yuu "Ahh… Right. I didn’t think about that. I was too excited."
    y "Don’t worry about it. I’ll ask anyway."
    hide sumiko
    hide yuuko
    with dissolve
    "The sisters head back to their desks and return to work while Yukari gathers up the documents she’ll need to take to [anim_studio] later."
    "Attempting to find and organize everything gives her a headache."
    show yukari sigh
    y "What a mess. I need to clean up all our files for [anime.name] soon. It takes so much time just to find the character designs."
    y "I better show them to Yuuko for a final check. Better safe than sorry!"
    "Yukari files them neatly into a folder and hurries over to Yuuko's desk."
    play sound "music/sfx/paper_thud.ogg"
    scene yukari_bump with fade
    "Yukari bumps into Sumiko and the folder falls from her hands. The papers fall out all across the floor."
    y "Nooo! It took me so long to arrange them properly. Now I have to organize them again, and I was just about to head to [anim_studio]…"
    s "I’m sorry!"
    "No, I’m not blaming you. You were standing still, after all. It’s my fault for not paying attention to where I was walking."
    s "You’re so clumsy sometimes… Come on, I’ll help you."
    yuu "Me too."
    "The three of them work together to pick up the scattered pieces of paper and file them again."
    scene studio_main with fade
    show yukari at left
    show sumiko at Position(xalign=0.87,yalign=1.0)
    show yuuko at pos_outerright behind sumiko
    with dissolve
    show yukari sad_angry
    y "This is exhausting. I hate paperwork!"
    s "No one here likes it. It's a necessary evil."
    show yukari
    y "Do you want to take a look at the documents I’m going to send to [anim_studio]? That’s what I was going to ask about."
    s "Didn't we all check it together a few days ago? It'll be fine."
    y "Well, if you say so."
    "She turns to Yuuko in case the artist disagrees with her sister, but stops in surprise when she sees Yuuko’s computer screen."
    show yukari surprised
    y "What are these?"
    "Yukari points to the thumbnail images displayed at the side of Yuuko's screen."
    y "They look similar to our characters."
    show yuuko sigh
    yuu "What?! That’s nothing!"
    "Yuuko blush diminishes her attempt to sound casual."
    show yukari laugh_eyes_closed
    y "Now I’m even more curious."
    "Yuuko dives for her computer chair, but Yukari beats her to it and grabs the mouse. She opens the mysterious images."
    y "These are… sketches of the protagonist? But there are so many! I didn't know he was that difficult to design. Here are the side characters, too!"
    y "I thought it just took a few iterations to get the proper designs."
    yuu "There’s no point in showing my work to you if I’m not satisfied with it. And I always show it to Sumiko for a second opinion, too."
    yuu "If a design doesn’t pass our standards, I put it in this folder in case I need to use it again."
    yuu "Usually they stay here. I was checking them out again to see how much progress I’ve made."
    show yuuko tsundere
    yuu "Now stop looking at them! They should never appear in public!"
    show yukari happy
    y "Haha, don't worry. I was just curious, that’s all."
    "She doesn’t get why it’s such a big deal. The early sketches aren’t that bad. Nevertheless, she stands up and surrenders the computer to Yuuko, who quickly closes the folder."
    scene animation_studio with fade
    show yukari at left with dissolve
    if anim_studio == anim_studio_expensive:
        y "Hello. Is [anim_studio_dir] here? I’ve brought the storyboards for our first episode."
        staff "One moment."
        show anim_dir at right with dissolve
        anim_dir "Hello, Yukari. The adjustments for the storyboard are finished, I presume?"
        y "Yes. They’re more detailed now and the direction of the scenes should be clearer, too."
        "She takes the storyboards out from her bag and passes them to the director."
        anim_dir "That sounds perfect. All we’ll need now are the remaining details—the character designs, the scenario, the script, and anything else you think will help us."
        y "Is it all right if I bring those things by on Monday?"
        anim_dir "That will be fine."
        y "Great! See you then."
    elif anim_studio == anim_studio_cheap:
        "When Yukari enters the studio, she almost collides with the director."
        show anim_dir frustrated at right with dissolve
        anim_dir "Oops, sorry about that. I was just on my way out. Can I help you with something?"
        show anim_dir
        y "I’ve fixed the storyboards. They’re more detailed now and the direction of the scenes should be clearer, too."
        "She takes the storyboards out from her bag and passes them to the director."
        anim_dir "Great! Let’s see, we’ll still need a few things… character designs, the script… it would probably help to see the scenario, too…"
        y "I can bring everything by on Monday, if that works for you."
        anim_dir "Sure, no problem."
        y "All right, I’ll see you then!"
    play music restaurant_music fadein 2.0 fadeout 2.0
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi happy at pos_farleft behind yukari
    with dissolve
    "It's dinner time again! Once again, everyone is in high spirits as they gather together."
    show yukari happy
    y "We celebrated last week, but I think a second celebration is in order!"
    y "Not only do we have an investor, but now we’ve made a deal with [anim_studio]!"
    yuu "It’s almost overwhelming."
    y "I know. [anime.name] has gone from a dream to something that’s really happening."
    m "Have you guys thought about what you’ll do if [anime.name] is successful?"
    y "I… Honestly I’ve spent too much time worrying about what I’ll do if it fails."
    yuu "Me too."
    show mayumi laugh_eyes_closed
    m "Well it’s time you two imagined a positive future instead! Yukari, you’ll want to keep directing anime, right?"
    y "Well, yes. It’s my dream."
    show sumiko happy
    s "So if [anime.name] is a hit, we start working on the sequel. I get it! [anime.name] franchise, here we come!"
    show yukari
    y "Would a sequel be possible?"
    s "Don’t ask me, ask the writer."
    "Everyone looks toward Shunsuke, who folds his arms."
    show shunsuke sigh
    "Everyone looks toward Shunsuke, who folds his arms."
    ss "What sort of ridiculous question is that? Of course a sequel is possible!"
    m "Do you already have ideas for one?"
    show shunsuke
    ss "I always have ideas for sequels. That’s why I started writing fanfiction, you know. My favorite series ended, and I wanted to know what happened next."
    ss "If no one official was going to write it, I decided to do it myself."
    yuu "I know what you mean. That’s one of the reasons I started drawing."
    show sumiko surprised
    s "Huh?! Since when?"
    yuu "Sumiko and her friends were working on a manga, but some of the most interesting moments were off-panel. That frustrated me, so I drew those scenes myself."
    show sumiko
    s "I thought that was your way of saying you wanted to join us. That’s why I invited you to help."
    show yuuko sigh
    yuu "I did. The missed potential in your manga was driving me crazy."
    s "Pfft, whatever…"
    m "So what are your sequel ideas, Shunsuke?"
    ss "Well, since [anime.name] is only two episodes long, I consider it more like a two-part pilot."
    if anime.category == Anime.HAREM:
        ss "If the story continues, the school administration will threaten to shut down the science club for unknown reasons."
    elif anime.category == Anime.MYSTERY:
        ss "The “sequel” will move on to another case, of course, although I have my suspicions it’s tied to the current cases."
        m "Suspicions? You make it sound like you’re discovering the story, not writing it."
        ss "That’s often how it feels."
    elif anime.category == Anime.ACTION:
        ss "Really, there’s no way this ancient conspiracy is so small it can be confined to two episodes. This is just the tip of the iceberg."
    y "You have big hopes for our future."
    ss "Don’t you?"
    y "I suppose I do."
    "She lifts her glass."
    y "Come on, everyone. Let’s make Shunsuke’s sequels possible!"

label week_5_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "What shall Yukari do this weekend?"
    menu:
        "Spend the weekend with your friends":
            $choicewe_5_1_1()
            "Yukari calls up some of her friends from high school."
            "For part of the weekend, they go to the park to enjoy the nice weather, and then they spend the rest of it catching up with one another."
        "Raise Funds":
            $choicewe_5_1_2()
            "On her way home from the studio on Friday, Yukari noticed a local store that needed temporary help over the weekend due to a promotional event."
            "She took the opportunity to sign up."
            "Now that the weekend has arrived, she spends it working in the store to raise additional funds for [anime.name]."
        "Attend a workshop on life skills":
            $choicewe_5_1_3()
            "The workshop largely goes over stuff Yukari has heard time and time again, but on the other hand, it gives her a few new ideas for managing the team’s time and resources and for being an effective leader."
        "Relax":
            $choicewe_5_1_4()
            "She stays at home all weekend, reading books and watching anime. It’s a nice, stress-free way to recharge for the next week."
    scene studio 
    $nextWeek()
    $mayumi_tasks[0] = mayumi_third_task
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_6_1:
    $achievement.grant("ACH_2")
    scene studio with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music happy_music fadeout 2.0 fadein 2.0
    y "Today I’ll make a trip to [anim_studio] to give them the assets they need for [anime.name]."
    y "Before I go, I want to know everyone’s plans for the next few days."
    m "I’m trying to figure out the right method to hire voice actors. We could hire them through a talent agency, freelancers, or agents."
    m "It's difficult to strike a balance between price and quality. I’ve also started composing music for [anime.name], but it's more or less in the planning stage at the moment."
    show yukari worry
    y "Is finding good voice actors that difficult? How bad could it be?"
    if anime.category == Anime.HAREM:
        m "We’ve got a quirky cast of characters thanks to the way Shunsuke has them balanced between “sweet high school girls” and “future mad scientists.”"
        ss "You know you love them."
        m "Those personalities could be difficult to pull off. Go too far one way and they’ll sound crazy. Go too far the other way and their antics won’t be believable."
    elif anime.category == Anime.MYSTERY:
        m "It’s casting Shin I’m most concerned about. Since he’s the antagonist, we need a [va_c]apable of sounding sinister, without being obvious from the start."
        s "Why not have him sound completely sweet and innocent?"
        m "Because if he still sounds that way when the truth comes out, either the audience won’t believe his confession or he’ll come across as more psychopathic than Shunsuke intended."
    elif anime.category == Anime.ACTION:
        m "As the protagonist, Itaru needs a strong [va_b]ecause of the stressful situations he’s put into."
        "We don’t want him to sound like he’s talking about the weather when he describes people trying to kill him."
        s "Dull surprise!"
        m "But we don’t want over-the-top screaming, either, or no one will take him seriously."
    y "Yikes. I didn’t know casting voice actors was so intense."
    show mayumi laugh_eyes_closed
    m "Haha, don’t worry about it. I’ll figure it out."
    show yukari
    show mayumi
    y "Good luck. All right, what’s everyone else working on?"
    s "I’ll handle the key backgrounds for [anime.name] along with the animation team at [anim_studio]."
    if anime.category == Anime.HAREM:
       s "In particular, I want to take care of the school exterior, the classroom, the chemistry lab, and the biology lab."
       s "That’s where the majority of [anime.name] takes place, so we want them to be as detailed as possible."
    elif anime.category == Anime.MYSTERY:
       s "The detective agency and the crime scene are the most important ones because of the amount of detail they need."
       s "Noir can be a tricky style to get right, especially since [anime.name]’s tone isn’t completely serious."
    elif anime.category == Anime.ACTION:
       s "Since we have so many action scenes, there will be a lot of fast-moving environments."
       s "And of course, the scene where we first learn about the conspiracy needs to have a lot of impact, with a very striking background."
    y "Sounds good to me. Yuuko?"
    yuu "Since we’re done with the character designs, I’d like to work on the key animations."
    yuu "Once the animation and backgrounds for each episode are complete, I’ll move on to the filming and editing."
    y "Remember to talk to the animation director before you start drawing any key animations."
    y "We're still new to this, while they’ve shipped anime titles. It’s best not to get too ahead of ourselves."
    yuu "Definitely, for sure."
    if anime.category == Anime.HAREM:
        yuu "The character interactions are such an important part of this anime, and I don’t want anything to look weird or awkward."
    elif anime.category == Anime.MYSTERY:
        yuu "The noir art style, especially in the flashback scene, makes me worried about how to handle the animations. It’s the first time I’ve worked with this style."
    elif anime.category == Anime.ACTION:
        yuu "I’ve never drawn fight scenes before, and [anime.name] has a lot of them. I need to be very careful with the battles—and the chase sequences, too."
    show yukari laugh_eyes_closed
    y "You’ll be fine."
    yuu "Thank you. I’m just taking notes on my ideas for now. I’ll wait to hear from the animation director before I go further."
    y "While I’m at the studio, I’ll be sure to ask about you working with them."
    yuu "Thank you."
    show yukari
    ss "As for me, I'm still working on the storyboard for the second episode. You’ve done a lot of good work on it, Yukari, but we’re not finished yet."
    ss "We have all the scenes and cuts identified, but now I’m adding directions to explain the scenes in as much detail as possible."
    show yukari sigh
    y "I thought it was pretty clear already."
    ss "From a bigger-picture perspective, yes."
    if anime.category == Anime.HAREM:
        ss "However, there are smaller details to take care of. For example, when the science club announces its new experiment, the camera pans across each character before zooming in on our startled protagonist."
    elif anime.category == Anime.MYSTERY:
        ss "Nevertheless, it’s fairly complex. Due to the flashbacks, we have a lot of cuts, more cuts than anime episodes usually have."
        ss "It could get chaotic. I’m adding a little more organization and clarification so we don’t confuse the animation studio… or our viewers."
    elif anime.category == Anime.ACTION:
        ss "I know you’re the director and this is ultimately your project, Yukari, but I wrote the dialogue."
        ss "Especially in a story with a lot of action like this one, the dialogue needs to match up well with what’s on-screen."
    y "Well… all right. But if you make any big changes, be sure to ask me, okay?"
    show yukari
    ss "Always."
    ss "I’ll also work on our marketing, as well as managing the studio when you’re too busy."
    show yukari happy
    y "Sounds great."
    "She looks around at her team members."
    y "I guess that’s that. I'll head over to [anim_studio] now. I should be back in about an hour or so."
    m "Good luck!"
    "Yukari gathers all the assets they need to start animating Episode One of [anime.name] and leaves the studio."
    scene street with fade
    show yukari at left with dissolve
    y "Luckily, [anim_studio] isn’t far away. Her commute back and forth won’t take too much time."
    scene animation_studio with fade
    if anim_studio == anim_studio_expensive:
        show yukari at left with dissolve
        y "Hello, I’m here to see [anim_studio_dir]."
        staff "Ah yes, he’s been expecting you."
        show anim_dir smile at right with dissolve
        anim_dir "Hello again, Yukari."
        y "Hello, sir. Here are the assets for episode one of [anime.name]."
        anim_dir "Wonderful! I'll take a look at them later and let you know if I have any questions or concerns."
        y "There are a couple things I’d like to clarify as well."
        y "Would it be okay if two of my team members, Sumiko and Yuuko, handled some parts of the key animation and backgrounds once they get the hang of things?"
        anim_dir "They’re your artists, correct?"
        y "Right. They should have a good idea of how things should flow in each episode, and I believe your expertise will be able to guide them along."
        show anim_dir happy
        anim_dir "That sounds fine to me. It's nice to see youngsters taking the initiative to learn more."
        show anim_dir smile
        anim_dir "Can I have their email addresses? I'll get in touch with them so we can make further arrangements."
        "Yukari takes her phone out of her pocket and sends Sumiko and Yuuko's email addresses to the director."
        anim_dir "Anything else?"
        y "Yuuko was also hoping to be in direct communication with the animation team."
        anim_dir "That can be arranged. No problem. My team will be able to teach both of them the skills they need to succeed in their fields."
        show yukari happy
        y "Thank you for being so helpful."
        anim_dir "Any time. Working together on [anime.name] will be a pleasure."
        "Yukari leaves the animation studio and returns to her own studio, where she still has work left to do."
    elif anim_studio == anim_studio_cheap:
        show yukari worry at left with dissolve
        y "Hello? Is anyone here?"
        "Why does the studio always seem deserted whenever she arrives?"
        play sound sfx_anim_d_open
        show yukari
        show anim_dir at right with dissolve
        anim_dir "Ah, hello, Yukari! Is there something I can do for you?"
        y "Hello, sir. Here are the assets for episode one of [anime.name]."
        anim_dir "Great! We’ll get started right away."
        y "If you have any questions, please let me know."
        anim_dir "Of course, of course."
        y "There are a couple things I’d like to clarify as well."
        y "Would it be okay if two of my team members, Sumiko and Yuuko, handled some parts of the key animation and backgrounds once they get the hang of things?"
        anim_dir "Hmm, we usually prefer to handle things ourselves…"
        "Yukari thinks about the dismal reception of Kogu Studio’s recent projects and bites her lip before she can sarcastically comment on how well handling it themselves has gone lately."
        y "Sumiko and Yuuko are our artists, so they should have a good idea of how things should flow in each episode."
        y "You and your team will guide them with your expertise, of course."
        anim_dir "Well, all right. I’ll need a way to get in touch with them."
        y "I’ll give you their email addresses."
        y "She takes her phone out of her pocket and sends Sumiko and Yuuko's email addresses to the director."
        y "Yuuko was also hoping to be in direct communication with the animation team, so she can learn more."
        anim_dir "That sounds like the best way to handle things if we’ll be working together. I’ll get in touch with both of them later."
        y "Great! Thank you."
        "As she leaves the animation studio, she reminds herself again to keep an eye on Kogu Studio to make sure everything goes smoothly."
        "For now, though, she still has work to do at her own studio."
    scene studio_main with fade
    show yukari laugh_eyes_closed at left with dissolve
    show sumiko at Position(xalign=0.87,yalign=1.0)
    show yuuko at pos_outerright behind sumiko
    with dissolve
    y "Yuuko and Sumiko! I’ve got good news for you."
    y "I discussed the possibility of you two handling key animations and backgrounds with the director of [anim_studio], and he thinks it's fine."
    y "The animation team will probably teach you the skills you’ll need first. He’ll be in touch with you through email to set things up."
    show sumiko happy
    s "Wow, fantastic! I never expected to be given that privilege right away."
    s "Sounds like a great learning experience! Right, Yuuko?"
    show yuuko laugh_eyes_closed
    yuu "Yes. Thank you, Yukari."
    y "Aw, don’t mention it."
    hide sumiko
    hide yuuko
    with dissolve
    "What would you like to focus on for the rest of the day?"
    menu:
        "Storyboards":
            $choice_6_1_1()
            "Yukari takes into account what Shunsuke said earlier and joins him to look over his changes and polish the storyboards further."
        "The Plot for [anime.name]":
            $choice_6_1_2()
            if anime.category == Anime.HAREM:
                "Shunsuke’s hopes for a sequel stand out in Yukari’s mind. She works with him to seed a few hints of foreshadowing into the story."
                "If [anime.name] never goes beyond the first two episodes, it will stand on its own, but if it does continue, the larger plot will appear to have been planned from the start."
            elif anime.category == Anime.MYSTERY:
                "Most of the story is solid, but Yukari goes over the clues again to find a balance between subtlety and obviousness."
                "They don’t want the audience to figure out the murderer’s identity too soon, but it shouldn’t come out of nowhere. Ideally, the final revelation will make all the pieces fall into place."
            elif anime.category == Anime.ACTION:
                "With only two episodes, they have a limited amount of time to explain the conspiracy."
                "Yukari adjusts the most important scenes to make sure they convey the necessary details without being exposition dumps. The viewers should have enough information to not be confused."
        "Character Development":
            $choice_6_1_3()
            if anime.category == Anime.HAREM:
                "As it stands, Keiji is the dullest member of the cast. Since he’s the main character, that’s not good."
                "Yukari gives him a pet cat, a paperclip collection, and a dream of becoming an astronaut to flesh out his personality more."
                "Then she makes a note for Shunsuke to double-check the changes, in case anything is out of line with his plans."
            elif anime.category == Anime.MYSTERY:
                "Mayumi’s concerns about Shin’s voice acting made Yukari realize their antagonist needs to be handled with exceptional care."
                "She runs through all of his dialogue to make sure everything he says fits his personality, and that his lies don’t sound out-of-place."
                "She makes a note asking Shunsuke to clarify Shin’s background and motivations for her."
            elif anime.category == Anime.ACTION:
                "Since [anime.name] focuses so much on running and fighting, with most of the remaining time devoted to the conspirators’ machinations, they haven’t done much with character development."
                "Yukari marks each spot in the script where they can add personal details to make their characters feel more like people."
    "By the end of the day, she’s satisfied with her progress."

label week_6_2:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    $va_choice = "none"
    "Yukari decides to wait a few days before making another trip to [anim_studio] to check on their progress. For now, she believes it's best to focus on their current work."
    y "Mayumi, how is the voice actor problem coming along?"
    show mayumi_f sad
    m "Well, I still can’t decide how we should hire them. Since you’re the director, I think you should make the final decision."
    y "Are you sure?"
    m "Yes. I researched the pros and cons of the various methods and took notes."
    show mayumi_f
    "Mayumi walks to her desk and picks up a piece of paper from alongside her stack of sheet music. She hands it to Yukari."
    m "Take a look and tell me which option you think we should go with."
    "The paper lists the three methods Mayumi mentioned earlier: talent agencies, agents, and freelancers, along with her notes on each."
    "Talent Agency – An expensive option, but it guarantees quality. The agents will locate a pool of qualified voice actors for us."
    "Agents – Similar to hiring actors through a talent agency, but less expensive. Agents will seek out freelance voice actors and facilitate communication between the actors and us."
    "Freelancers – The cheapest option, where we skip the middleman and look for freelancers ourselves."
    "This will take more time to find the right voice actors, since we’ll have no initial screen for quality."
    "Yukari reads over the three options multiple times."
    m "Well? Which sounds best for [anime.name]?"
    menu:
        "Talent Agency {space=15}{image=small_moneybag.png} [TALENT_AGENCY_FUNDS_VALUE]":
            $choice_6_2_1()
            y "The talent agency is the best way for us to ensure we get quality voice acting."
            y "Yes, it costs more, but it will also free up our time to work on other things."
            $va_choice = "Talent Agency"
        "Agent {space=15}{image=small_moneybag.png} [AGENT_FUNDS_VALUE]":
            $choice_6_2_2()
            y "Working through agents is the ideal middle ground."
            y "We won’t have to search for the voice actors ourselves, but we won’t have to deal with a talent agency’s high prices either."
            $va_choice = "Agent"
        "Freelancers {space=15}{image=small_moneybag.png} [FREELANCER_FUNDS_VALUE]":
            $choice_6_2_3()
            y "We need to look for freelance voice actors ourselves."
            y "It’ll take a lot of time and could be risky, but our budget can’t handle too much of a strain."
            $va_choice = "Freelancers"
    m "All right."
    y "One more thing: I’ll leave choosing the actual voice actors up to you. You’re the one best-qualified to judge which voices are suitable for [anime.name]."
    show mayumi_f laugh_eyes_closed
    m "That’s fine. I’ll put my knowledge to the test!"
    if va_choice == "Talent Agency" or va_choice == "Agent":
        m "I'll get in touch with the [va_choice] soon."
    elif va_choice == "Freelancers":
        m "I'll look for freelancers and shortlist the most promising ones. Then I’ll hold auditions to make the final decision."

    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_2
label week_6_3:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    ss "Is our current pace all right, Yukari? We just completed the storyboards for episodes 1 a few days ago."
    ss "When do we need to send the storyboards for episode 2 over to [anim_studio]?"
    y "By the end of next week."
    show shunsuke worry
    ss "Hmm… so our pacing…"
    show yukari sad_angry
    y "It isn’t that great. We’re barely on schedule for the storyboards."
    y "If we don't send them by the end of next week, it'll slow down the animation team’s progress, so we need to make sure this is done right."
    show shunsuke
    ss "Thanks for clarifying. I thought our pacing was good, but it seems I was wrong."
    y "We need to step things up."
    ss "What is the animation process like, anyway? I always assumed it was simple, since so much anime is produced each season, but now I’m not so sure."
    y "There’s actually a lot that goes into it. Layouts, key frames, in-between animation…"
    "Shunsuke holds up his hand."
    ss "Slow down. Mind explaining these things? It should help me with the storyboards if I understand the process better."
    y "Well, layouts are what we’ve been doing with the storyboards. The director decides how to present the scenes, what angles to use, etc."
    ss "Right. I knew that part. That’s why we needed to include so many details."
    y "Yuuko is going to help the team with the key frames, which means she’ll sketch out what the animation itself should look like."
    ss "In other words, the movements—how one pose leads into another, for example?"
    y "Yes, but it also includes color, shadows, and highlights. It’s the most critical part of the process."
    ss "If all that’s included, it sounds like a full animation to me."
    y "Well… hang on a minute."
    "She turns toward the desk where Yuuko sits, hard at work on her art."
    scene studio_main
    show yukari at pos_left
    show shunsuke_f at pos_farleft behind yukari
    show yuuko at right
    with dissolve
    y "Yuuko, do you have any of the key animation sketches done?"
    yuu "I’ve only just begun working with the animation team… I drew a few for practice, but—"
    show yukari happy
    y "They’ll do! Can I borrow them?"
    yuu "Oh, sure…"
    "She hands Yukari a few sketches and watches curiously as Yukari holds them up."
    y "Okay, these sketches show how the animation should go. But imagine how it would look if it went straight through these frames, with nothing else."
    ss "It would be awkward and jerky."
    y "Exactly. These are the key frames, but they’re missing frames in between. That’s why the animators need to take care of the in-between animation."
    "She hands the sketches back to Yuuko."
    y "Thank you."
    show yukari
    yuu "No problem. Do you want to get involved in animation work, Shunsuke?"
    ss "I’m trying to understand it better."
    y "Anyway, after that, the final step will be to paint the animations onto cels—"
    show shunsuke_f surprised
    ss "Cells…?"
    yuu "Cels. It’s short for celluloids. A cel is a transparent sheet used for hand-drawn animations."
    yuu "Computer animation is more common now, but for [anime.name], we’re using cels."
    y "That’s right. The outlines are painted first in black, and then the color is added."
    show yuuko laugh_eyes_closed
    yuu "Then we’ll add the special effects!"
    show shunsuke_f sigh
    ss "This all sounds… much more complicated than I expected."
    show yuuko happy
    yuu "It’s not really so bad. Come on, I’ll tell you more."
    hide shunsuke_f
    hide yuuko
    show yukari happy at left
    with dissolve
    "As Shunsuke follows Yuuko back to her desk to discuss the animation process in further detail, Yukari watches them with a hint of pride."
    "When they first started working on [anime.name], she’d have never pictured those two engaged in excited conversation the way they are now."
    show mayumi_f at Position(xalign=0.85,yalign=1.0)
    show sumiko at pos_outerright
    with dissolve
    m "You look happy."
    y "I love this team so much."
    s "You’re not going to start spouting greeting card clichés, are you?"
    "Yukari laughs."
    y "Don’t worry, I’m not at that point yet."
    show sumiko sigh
    s "It’s that “yet” that worries me."
    s "You’re all just such wonderful team members. I’d be lost without a single one of you."
    s "We’re definitely veering into greeting card territory."
    show yukari laugh_eyes_closed
    y "It’s the truth!"
    show mayumi_f happy
    m "Aw, Yukari, you’ve come so far."
    show yukari surprised
    y "Huh? What’s that supposed to mean?"
    m "You’re so much better with people now."
    show yukari tsundere
    y "But I’ve always been a people person!"
    m "You’ve always been social and outgoing, but I used to worry you focused so much on the bigger picture, you missed seeing people as individuals."
    show sumiko
    s "That explains a few things…"
    show yukari surprised
    y "Huh? It explains what? What do you mean?"
    s "Never mind. I should get back to work, anyway."
    scene studio_main
    show yukari at left
    show mayumi_f at right
    with dissolve
    y "Yukari frowns after her and opens her mouth to ask again, but then Mayumi taps on her shoulder."
    show mayumi_f laugh_eyes_closed
    m "By the way, we’re one step closer to having voice actors."
    show yukari happy
    y "Really? That’s great!"
    if va_choice == "Talent Agency":
        m "I got in touch with a talent agency this morning and spent the rest of the day making arrangements and explaining what we need."
        m "They’ll contact me soon."
    elif va_choice == "Agent":
        m "I spent all day talking to agents. We’ve already got a few promising candidates lined up."
    elif va_choice == "Freelancers":
        m "I talked to freelance voice actors all day long, and I’ve finally make a list of people to invite to auditions."
    y "That’s fantastic! Keep me updated, okay?"
    show mayumi_f
    m "Of course. And, Yukari?"
    show yukari
    y "Yeah?"
    m "Don’t worry about what we said earlier. I think you’ve grown as a person, that’s all."
    y "Um, thanks?"
    m "Actually, I think our whole team is much stronger than when we started."
    show yukari laugh_eyes_closed
    y "That I definitely agree with!"

label week_6_4:
    $nextDay()
    scene studio_main with fade
    show yukari surprised at left 
    show sumiko at right
    with dissolve
    play sound "music/sfx/phone_ringing.ogg"
    y "Who could that be?"
    y "It’s our investor! What should I do?"
    show sumiko sigh
    s "Answer it, of course!"
    "Yukari stares at the phone, frozen with dread. Why would the investor call?"
    s "Ignoring our investor is probably a terrible idea. My guess is that he wants to check up on our progress on [anime.name]. Just talk to the man!"
    show yukari
    stop sound fadeout 1.0
    y "Okay, I'll be right back."
    scene black with fade
    "She leaves the studio and heads toward the staircase so her phone conversation won’t disturb the rest of the team as they work."
    "Then she braces herself and answers."
    y "Hello?"
    investor "Hello, Yukari. Are you free to meet up for tea this afternoon?"
    y "Yes, I'm free. Should we meet at the usual place?"
    investor "That sounds fine. I'll see you later, then."
    play sound "music/sfx/hanging_up_phone.ogg"
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show sumiko at right
    with dissolve
    s "So, what did he want?"
    y "He wants to meet up for afternoon tea."
    s "See? He’ll ask for some updates on the project. Don’t worry about it. We’ve made a lot of progress on the art and storyboards."
    m "Plus you can tell him about our deal with [anim_studio]! I bet he’ll be thrilled to know that."
    show yukari laugh_eyes_closed
    y "You know, now that you mention it, things have been moving along smoothly, haven’t they? Let’s try to maintain this status quo!"
    s "Hear Hear!"
    show yukari
    y "And that means we shouldn’t waste time chitchatting. Back to work, everyone."
    play music cafe_music fadeout 2.0 fadein 2.0
    scene cafe with fade
    show yukari at left
    show investor at right
    with dissolve
    "During the afternoon, Yukari heads to the café for her appointment with the investor. This time, he’s already there when she arrives."
    y "Hello! Sorry to keep you waiting."
    investor "Not at all. I only arrived a few moments ago."
    show investor frustrated
    investor "I can't stay for long though, as I have an appointment later, so we'll have to cut this meeting short."
    show investor smile
    investor "How's the production going for [anime.name]?"
    show yukari happy
    y " We're doing decently. We clinched a deal with [anim_studio] last week, and we’ve made good progress in regards to the art and storyboards."
    investor "That's great. I thought you might need my help to outsource the animation work, since it's pretty complicated. May I give you some advice?"
    y "Of course!"
    show yukari
    if anim_studio == anim_studio_expensive:
        investor "[anim_studio] is a great choice, but you’ll need to watch and control your budget closely."
        investor "As per our contract, we won’t be able to help you if you run out of funds. That’s a situation you don’t ever want to get yourself into."
        investor "It could mean the end of your project."
        y "Don’t worry, we’re monitoring the budget. Working with [anim_studio] was a risk, but I think it will pay off in the long run."
    elif anim_studio == anim_studio_cheap:
        investor "[anim_studio]? The last I heard of them, they were in the gutter due to the failure of their most recent anime."
        y "I heard about that. It was an adaptation of a light novel, right?"
        investor "Yes, and fans on the Internet were in an uproar over [anim_studio] “destroying” the story. Quite frankly, it was a train wreck, and no studio will touch the series now."
        investor "I’d recommend you steer clear of [anim_studio], but since you already signed the contract, I suppose there’s no choice."
        y "They’ve produced a number of hit titles, too, and their prices are competitive compared to other studios."
        investor "You're right, but if I were in your shoes, I wouldn't take such a big risk."
        y "Don’t worry, I’m keeping a close eye on [anim_studio] to make sure nothing goes wrong. We can handle it."
        investor "I’ll leave that up to your judgment, then."
    investor "Anyway, there’s one more reason I called you here. I think this is a good time to start marketing [anime.name] to hype it up."
    y "Yes, our writer was interested in that."
    if guerilla_marketing:
        y "We’ve also done a little pre-release marketing through social networks."
        investor "That only goes so far. A larger push will help [anime.name] receive the attention it needs."
    else:
        y "We haven’t done any marketing yet,though."
    investor "Remember, a small studio like yours won’t have the name recognition to attract fans to [anime.name] from the start."
    investor "With a proper marketing campaign, you can catch people’s attention."
    "Yukari nods. They’ll need to work hard to win an audience for [anime.name]."
    "On the other hand, not only will they have to dip into their funds, but they’ll also need to put in the time and effort to promote it."
    investor "It’s just my advice. What do you think?"
    menu:
        "Listen to your investor's advice and start marketing {space=15}{image=small_moneybag.png} [INVESTOR_FUNDS_MARKETING_6_3_1]":
            $choice_6_3_1()
            $investor_marketing = True
            y "You’re right. We need to start marketing, and this is the best time to do it. We’ll get started immediately."
            show investor happy
            investor "I’m glad to hear it. Contact me if you need any help."
        "Reject the offer and say you're busy with your current workload":
            $choice_6_3_2()
            $investor_marketing = False
            y "I’m afraid our current workload is too much for us to add a new task now."
            y "Until [anime.name] is complete, we’ll need to make do with minor marketing efforts."
            investor "Well, that’s your decision."
    investor "I look forward to hearing more about your progress in the future. However, I need to leave now. Good luck, Yukari."
    "She shakes his hand."
    y "Thank you."
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_3

label week_6_5:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    with dissolve
    play music restaurant_music fadeout 2.0 fadein 2.0
    if investor_marketing:
        show shunsuke at right with dissolve
        y "Shunsuke, do you have a minute?"
        ss "Yes?"
        y "When I spoke to our investor yesterday, he suggested we begin a marketing campaign for [anime.name]."
        ss "That’s a great idea."
        y "Do you want to handle it? I know you were interested in marketing."
        show shunsuke laugh_eyes_closed
        ss "Absolutely. I’ll step up our Internet advertising, run some online campaigns, and look into prices for marketing managers."
        ss "Once the animation is far enough along, we can even create a trailer!"
        show yukari happy
        y "Sounds like you’ve put a lot of thought into this already."
        ss "I have. Marketing is critical to [anime.name]’s success, after all."
        y "Great! Let me know if you need anything."
        show yukari
        hide shunsuke with dissolve
        "She returns to her desk, satisfied that she’s left the task in capable and enthusiastic hands."
    show mayumi_f laugh_eyes_closed at right with dissolve
    m "Hey Yukari, I hired our major voice actors!"
    y "Awesome! Who are they?"
    if anime.category == Anime.HAREM:
        m "A guy named [va_a] will voice Keiji. He’s new in the industry, but his audition was perfect for our protagonist. He really captured the tone of [anime.name]."
        m "I’ve also picked [va_b] for Natsume."
        m "She did a really good job in her audition, especially since Natsume is one of the more mild-mannered members of the science club."
        m " Finally, I hired [va_c] as Kiko. Her acting has the right mix of “adorable” and “crazy” we need for our nutty chemist."
    elif anime.category == Anime.MYSTERY:
        m "[va_a] will voice Hideaki. What he lacks in experience, he makes up for in enthusiasm. It’s like he’s waited all his life to play a detective."
        m "Meanwhile, [va_b] gave a stellar audition for Megumi’s part. She has perfect chemistry with [va_a] to play Hideaki’s assistant."
        m "I also cast [va_c] as Shin."
        m "Just to warn you, when he gets in-character, he REALLY gets in-character. It feels like our antagonist leaped out of the script into reality."
    elif anime.category == Anime.ACTION:
        m "[va_a] will voice Itaru. He read his lines with the perfect balance we need for the hero—stressed and upset, but not over the top."
        m "[va_b] is going to be Chie. She has the sort of quality we want for Itaru’s friend and confidant."
        m "And [va_c] is a perfect fit for Norio."
        "Yukari thinks about Norio’s role as the primary villain of [anime.name] and tries to imagine what a “perfect fit” must be like."
        show yukari surprised
        y "That sounds rather scary."
        show mayumi_f happy
        m "Yes, it was an intense audition. I hired him on the spot."
    show mayumi_f
    show yukari
    m "Of course, this isn’t the full cast, but they’re the most critical roles right now."
    show mayumi_f
    m "Now that we have voice actors, they’ll need to record their lines. I think next Friday is a good time to head to the recording studio. What do you think?"
    y "Friday sounds great to me. Which recording studio did you pick?"
    show mayumi_f happy
    m "[va_studio]. They're quite close to our office and their equipment is brand new!"
    m "I researched their studio and the reviews are overwhelmingly positive!"
    show yukari happy
    y "Cool! I’ve never been to a recording studio before, so this should be an eye-opening experience for me."
    m "You betcha!"
    hide mayumi_f with dissolve
    "She returns to her desk, and Yukari looks over her own work. Today’s focus should be on…"
    show yukari
    menu:
        "Storyboard":
            $choice_6_4_1()
            "As she told Shunsuke, it’s critical to finish the storyboards."
            "Yukari spends the rest of the day working on the storyboard for the second episode."
        "Animation":
            $choice_6_4_2()
            "While she doesn’t have direct involvement with the animation process, Yukari looks over everything [anim_studio] has done so far to make sure it’s on track with her vision for [anime.name]."
        "Backgrounds":
            $choice_6_4_3()
            "Yukari joins Sumiko to look over the final backgrounds they’ll use for [anime.name]."
        "Relax":
            $choice_6_4_4()
            "After a moment, she leans back in her chair and closes her eyes."
            "Work on [anime.name] is coming along nicely. She can afford a little time to relax."
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    "Once again, everyone gathers at the restaurant in the evening. It’s become a comfortable part of their routine."
    if anim_studio == anim_studio_cheap:
        s "Hey Yukari, mind if we talk business for a minute?"
        y "Sure. What’s up?"
        s "You know [anim_studio_cheap] had some problems in the past, right?"
        y "Yeah. Our investor brought it up, too."
        show sumiko sad_angry
        s "A couple years ago, I was a fan of an anime series that went downhill and was eventually cancelled."
        s "The problem? Bad management at the outsourced animation studio. We can’t let that happen to [anime.name], okay?"
        y "Don’t worry, we won’t."
        "Despite her confident words, she can’t help but feel worried. Maybe she’ll keep an even closer eye on [anim_studio_cheap] than she planned."
        show sumiko happy
        s "Great! Sorry to bring it up now. Enough business, let’s focus on dinner!"
    show sumiko laugh_eyes_closed
    "Sumiko claps her hands together and smiles at the group."
    s "All right, who’s looking forward to the new episode of JoJo’s Bizarre Adventure tonight? Hint, if you aren’t, you’re wrong!"
    show yuuko sigh
    yuu "Don’t mind her, she gets obsessive over her favorite anime."
    show sumiko tsundere
    s "You’re one to talk."
    yuu "Huh?"
    s "If you draw any more Berserk fan art, our house will hit the quota for “most Berserk fan art allowed under one roof.”"
    show shunsuke surprised
    ss "You’re a Berserk fan too, Yuuko? I wouldn’t have guessed."
    show yuuko happy
    yuu "I love it! Wait, too? You’re a fan?"
    ss "Yes, but the manga is far superior."
    show shunsuke
    show sumiko
    y "Why am I not surprised to hear the writer say that?"
    s "Hey, he’s writing our anime—he better not be TOO biased toward manga."
    ss "I’m not biased at all. The manga is better. It’s a simple fact."
    yuu "I’ll have to read it sometime."
    ss "Yes. You will."
    show yuuko surprised
    yuu "Is that an order?"
    ss "Maybe."
    yuu "Wow."
    show shunsuke sigh
    ss "Cut me some slack. Back in school I was always recommending books and shows to people, and most of them ignored me."
    ss "Even other members of the literature club ignored me!"
    yuu "Wait… were you the one who tried to start a new club to analyze the influence of classic writers and mythology on popular anime?"
    show shunsuke sad_angry
    ss "Yes, and you know how many members the club had? One. Me."
    show yuuko
    yuu "I was interested, but…"
    ss "But?"
    show yuuko sad
    yuu "I didn’t want to be the first person to join…"
    "Shunsuke throws his hands in the air, and Yukari can’t help but laugh."
    show yukari laugh_eyes_closed
    y "Imagine if there were a dozen other people all waiting for someone else to join Shunsuke’s crazy little club first?"
    show shunsuke
    show yuuko
    ss "I’ll try it again, once [anime.name] is popular."
    show sumiko surprised
    s "What does that have to do with anything?"
    ss "People will be eager to join a discussion club hosted by the lead writer of [anime.name]. First up, we’ll analyze Death Note and Steins;Gate."
    yuu "Ah!!"
    show sumiko sigh
    s "Now you’ve done it. She likes Steins;Gate even more than Berserk."
    ss "The visual novel is superior, though."
    show sumiko surprised
    s "Your bias extends to visual novels, too?!"
    show shunsuke tsundere
    ss "It is NOT bias. Again, it’s a simple fact!"
    show mayumi happy
    m "I wanted to start a similar club in school. I thought it would be neat to analyze the use of musical themes in anime stories."
    y "You really loved that musical piano thing, didn’t you?"
    show sumiko surprised
    s "“Musical piano thing”?"
    show mayumi laugh_eyes_closed
    m "What? Oh, you mean Your Lie in April? Yes!"
    s "Musical piano thing.” Really, Yukari?"
    show yukari sigh
    show sumiko
    y "I couldn’t remember the name! Anyway, what’s with you guys wanting to analyze everything? Doesn’t anyone but me watch anime just for fun?"
    s "Me! I do!"
    yuu "You can analyze things and have fun at the same time."
    y "You know how I got into anime originally? Pokémon. Just try to analyze that."
    show shunsuke laugh_eyes_closed
    ss "I think that can be arranged. What do you think, Yuuko?"
    yuu "Definitely. Third anime lined up for our discussion club?"
    ss "Sounds perfect. Thanks for the suggestion, Yukari."
    y "Agh! Okay, lately I’ve become a fan of Food Wars! There’s no way you can—"
    ss "Delving into the deeper themes of that show should be quite interesting."
    y "You people drive me crazy."
    "But even as she says it, she knows there’s no place she’d rather be than with her team."

label week_6_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "It's the weekend! What will you do?"
    menu:
        "Visit [anim_studio]":
            $choicewe_6_1_1()
            scene street with fade
            show yukari surprised at left with dissolve
            y "Huh? The door’s locked…"
            "She frowns at the closed studio and then notices a sign on the door that lists its hours."
            y "It’s closed on the weekends? Aw man…"
        "Raise Funds":
            $choicewe_6_1_2()
            "After browsing online for fundraising ideas, Yukari creates a page where fans interested in [anime.name] will be able to make small donations."
            "It might not produce too many results, but a passive way to increase their funds is exactly what they need."
        "Read Books":
            $choicewe_6_1_3()
            "Yukari reads a variety of books, some about the anime production process and others just for fun."
            "By the time the weekend ends, she feels inspired and ready to proceed."
        "Relax":
            $choicewe_6_1_4()
            "Yukari sleeps in on the weekend, watches some anime, and de-stresses to prepare for the week ahead."
    scene studio 
    $nextWeek()
    $sumiko_tasks[0] = sumiko_third_task
    $yuuko_tasks[0] = yuuko_third_task
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2) 
           
label week_7_1_1:
    scene studio_main with fade
    show yukari at left 
    show mayumi_f at right
    with dissolve
    play music studio_music fadein 2.0 fadeout 2.0
    y "I'll be heading over to [anim_studio] now to get some updates on their progress."
    "The prospect thrills her. She'll finally be able to see her storyboards come to life."
    "What will the key frames look like? Will the animation be like she imagined it? She can barely breathe from anticipation."
    show mayumi_f sigh
    m "I wish I could come, but I'm swamped with work right now."
    m "I’ve been experimenting with composing music by using the storyboards as a reference. Between that and handling the voice actors, it looks like I’ll be busy for a while."
    m "I won't have a chance to visit [anim_studio] with you any time soon."
    y "I should be fine myself, even though it's nicer to have you with me."
    m "All right, if no one needs anything, I'm heading over now. Bye!"
    m "Bye!"

    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_4

    scene animation_studio with fade
    show yukari at left
    show anim_dir at right
    with dissolve
    "Yukari informed the director in advance of her visit, so this time he’s waiting for her when she arrives."
    y "Hello! I'm here to check up on the current progress for [anime.name]. Do you have anything new to show me?"
    if anim_studio == anim_studio_expensive:
        show anim_dir smile
        anim_dir "Of course! Let's sit down at the table over there while I set up the laptop to show you the new key frames."
        anim_dir "By the way, would you like coffee or tea?"
        y "I'll have some tea, thank you."
        "He looks toward the reception desk."
        anim_dir "Could you get some tea for Yukari?"
        "The staff member nods and disappears into the studio."
        show anim_dir happy
        anim_dir "Here are the finished key frames for the first episode of [anime.name]. What do you think?"
    elif anim_studio == anim_studio_cheap:
        anim_dir "I can show you the key frames for the first episode, if you like."
        y "That sounds good."
        anim_dir "Sit down at the table over there, and I’ll be right back with a laptop so we can look at them."
        hide anim_dir with dissolve
        "As he departs to get the laptop, Yukari can’t help but wonder why he didn’t have it with him already. Surely he could have guessed she wanted to see the key frames."
        play sound sfx_anim_d_open
        show anim_dir at right with dissolve
        anim_dir "All right, here we go. What do you think?"
    if anime.category == Anime.HAREM:
        "Everything looks fine until Keiji attends the first meeting of the science club."
        "It’s a critical scene to set up the plot and introduce the characters, but the introductions have so little personality to them, Yukari can’t help but wonder if they skipped some key frames."
    elif anime.category == Anime.MYSTERY:
        "In theory, it’s [anime.name]. Yukari recognizes Itaru, Chie, Norio, and everyone else who appears in the first episode."
        "The plot follows the correct order of events. The basic story is there."
        "Yet everything about it is so far from the way she envisioned it, she wonders if the director paid attention to her instructions at all."
    elif anime.category == Anime.ACTION:
        "The story setup is correct, but the presentation is too grim, which in turn makes the lighthearted moments feel awkward and out of place."
        "Later scenes jump around so much, it gives Yukari a headache trying to follow the story—and she made the storyboards! Something is definitely wrong."
    show yukari worry
    play music tension_music fadeout 2.0 fadein 2.0
    y "Wait a minute… This doesn’t look like what I gave you. Are you sure this is the right thing?"
    "She doesn’t know what answer he can possibly have to make this better."
    "It’s not like the animation studio would work on something completely different just for fun, and it’s too close to be from a different show. What in the world is going on?"
    if anim_studio == anim_studio_expensive:
        show anim_dir disappointed
        anim_dir "Of course I am. We used your storyboards as a reference down to the very last detail."
        anim_dir "However, they weren’t entirely clear at times. Didn’t we discuss this when you came in for your consultation?"
        y "That’s right."
        "Sweat beads on the back of her neck."
        show yukari surprised
        y "I fixed up the storyboards and brought them back. They shouldn’t look like this!"
        show anim_dir frustrated
        anim_dir "Calm down. I can get the storyboards for you to look at, and then we’ll figure out what went wrong."
        show yukari
        y "Yes, please do. Perhaps it’s a case of miscommunication."
        show anim_dir
        anim_dir "Give me a moment while I head back to my desk to grab the files."
        hide anim_dir with dissolve
        "He walks to the door behind the reception desk and disappears inside."
    elif anim_studio == anim_studio_cheap:
        show anim_dir disappointed
        anim_dir "Of course I’m sure! You gave us the storyboards, didn’t you?"
        "Yes, but even with Kogu Studio’s reputation, she expected the animation team to follow them a little better than this."
        "She stares at the key frames and tries to keep her emotions in check. Disaster or not, she can’t cry in front of the director."
        y "Can I see the storyboards?"
        "Sure, it’ll just take me a few minutes to find them."
        hide anim_dir with dissolve
    play sound [sfx_anim_d_open,sfx_anim_d_close]
    show yukari
    hide anim_dir with dissolve
    "Once the director leaves, Yukari takes a few deep breaths to calm down."
    "No matter whose fault the problem is, she’s in trouble. They can’t use those key frames for [anime.name]. Some will be salvageable, but most of [anim_studio]’s work was in vain."
    "It’ll set them a whole week behind schedule, and probably force them to dip into their funds even further."
    show yukari sad
    y "If only I checked up with the studio more last week, maybe I could have prevented this…"
    y "What could have happened? Maybe one of the others has an idea."
    "She pulls out her phone and tries to decide who to ask."
    jump week_7_choice

label week_7_choice:
    if not week_7_people_choices:
        jump week_7_1_2
    else:
        if week_7_current_choice == "Mayumi":
            $choice_7_1_1()
            m "Hello!"
            y "Mayumi? I'm at [anim_studio] right now, and we have a problem. I just saw the key frames for Episode One, and they’re wrong."
            m "Oh no!"
            y "The director says the team followed our storyboards, so do you have any idea what could have happened?"
            m "Hmm....."
            m "Sorry, I can't think of anything. Maybe you should try asking the others."
            y "Okay. Thanks anyway."
            $week_7_people_choices.remove("Mayumi")
        elif week_7_current_choice == "Yuuko":
            $choice_7_1_2()
            yuu "Hello?"
            y "Yuuko, we have a bit of a problem over here. The key frames for Episode One weren’t done properly."
            yuu "What?? Oh no…"
            y "The director says they followed our storyboards, but the animations don’t fit at all. Are you aware of anything that might have caused this?"
            yuu "Let me think."
            "Shock and alarm is apparent in Yuuko’s voice, even though she tries to sound calm. It’s no surprise. After all, she’s heavily involved in animation [anime.name]."
            yuu "I’m sorry. I can’t think of anything…"
            y "Don't worry. I'll figure it out and get back to you soon. Maybe someone else knows."
            $week_7_people_choices.remove("Yuuko")
        elif week_7_current_choice == "Sumiko":
            $choice_7_1_3()
            s "Hi, this is Sumiko!"
            y "I’m at the animation studio, but something’s gone wrong. The key frames for Episode One aren’t right."
            s "What? How could that happen?"
            y "I was hoping you had an idea. The director says they followed our storyboards, so I don’t know what could have happened."
            s "Maybe he’s lying!"
            y "No, I don’t think so."
            s "Oh. Well, that was my only idea. Sorry I couldn’t help more."
            y "Don’t worry about it. I’ll try calling someone else on the team."
            $week_7_people_choices.remove("Sumiko")
        menu:
            "Mayumi" if "Mayumi" in week_7_people_choices:
                $week_7_current_choice = "Mayumi" 
                jump week_7_choice
            "Yuuko" if "Yuuko" in week_7_people_choices:
                $week_7_current_choice = "Yuuko"
                jump week_7_choice
            "Sumiko" if "Sumiko" in week_7_people_choices:
                $week_7_current_choice = "Sumiko"
                jump week_7_choice
            "Shunsuke" if "Shunsuke" in week_7_people_choices:
                $week_7_current_choice = "Shunsuke"
                $del week_7_people_choices[:]
                jump week_7_1_2

label week_7_1_2:
    ss "Yes?"
    y "Hey Shunsuke, I'm in a bit of a bind over here. We seem to have had a case of miscommunication between us and [anim_studio]."
    ss "What sort of miscommunication?"
    y "They produced the wrong key frames, but the director says they followed the storyboards. Do you have any idea how this could have happened?"
    ss "All right, try to calm down. Give me a moment to think this through."
    y "Okay."
    "She tries to compose herself, but the silence on the other end is deafening. Her heart feels like it’s going to explode. How can Shunsuke sound so calm?"
    ss "Are the differences drastic? Could you have somehow given them the draft storyboards instead of the finalized ones?"
    y "I don’t know…"
    "She takes a deep breath and tries to concentrate."
    y "It’s possible. If they worked from a draft without my instructions, I can see it resulting in the key frames they made. But how?"
    ss "Try to recall everything that happened in between finishing the storyboards and taking them to the studio. Did anything significant occur? Anything unusual?"
    "It’s difficult to focus over the pounding of her heart, but Yukari forces herself to."
    "She worked on the storyboards on Wednesday. On Thursday, she signed the contract with the studio."
    " On Friday, she spoke to Yuuko and Sumiko about their questions for the director, gathered the files she needed to take to the studio, and…"
    show yukari sigh
    y "Damn."
    ss "What is it?"
    y "Right before I went to the studio that day, I knocked into Sumiko near her desk. The papers I was carrying fell everywhere. We must have gotten our files mixed up."
    ss "But how?"
    y "When we started the storyboards, we asked Yuuko and Sumiko for feedback, remember? If they left some of the draft storyboards on their desk…"
    ss "I see what you mean. What a mess. I hope you can resolve this issue with [anim_studio]. Let us know if you need any help."
    show yukari sad
    y "Thanks. I'll see what I can do."
    "Just as she finishes her conversation with Shunsuke, the director returns."
    show anim_dir at right with dissolve
    if anim_studio == anim_studio_expensive:
        anim_dir "Here are the storyboards. While the directions were a bit vague, we tried to follow them exactly."
    elif anim_studio == anim_studio_cheap:
        anim_dir "Sorry for the delay. I finally found them. Here, the storyboards match the key animations, don’t they?"
    show yukari surprised
    "Yukari takes a look at them, and to her horror, her suspicion was right."
    "Not only do they lack her painstaking notes and instructions, they aren’t even the version she showed the director during the consultation."
    "She mixed up the storyboards when she collided with Sumiko that day."
    show yukari worry
    "She opens her mouth to explain, but she can’t find the words. How can they solve this problem?"
    "They can’t go with the key frames as they are currently. That would be a disaster."
    "Deadlines can’t be adjusted, so they’ll have to either increase the production speed at [anim_studio] or find freelancers instead."
    "Either solution will require them to spend even more funds on animation. Maybe they’ll run of funds and not be able to produce [anime.name] at all."
    show yukari
    "Yukari takes a few deep breaths to try to calm down and sound as though she has the situation under control, even though she feels like screaming, crying, or both."
    y "I’m… I’m afraid there’s been a mistake. I accidentally gave you the draft storyboards, which are totally different from the main storyboards. We can’t use these key frames."
    y "Since we’re on a tight deadline to finish [anime.name], would it be possible for your team to speed up the animation work once I get you the proper storyboards?"
    y "Otherwise, I’m afraid we won’t make it in time to air the show on television."
    "Her voice sounds distant, as if it’s coming from far away. She’s almost impressed at how calm she sounds."
    if anim_studio == anim_studio_expensive:
        anim_dir "That explains why the storyboards seemed so unclear. We can speed up the animation work, although we’ll have to charge an additional fee."
        y "How much?"
        anim_dir "{space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS]."
        "She almost accepts, but bites her tongue. It’s a large sum of money, and while she can’t see another solution, it isn’t the sort of decision she should make on her own."
        "She’s caused enough problems already."
        y "Okay, I’ll have to discuss this with my team members first."
        anim_dir "I understand. Is there anything else you’d like to discuss now?"
        y "No. Thank you for showing me the storyboards. I’m really sorry this happened, but we’ll find a way to work it out."
    elif anim_studio == anim_studio_cheap:
        show anim_dir frustrated
        anim_dir "Does it really look that bad as it is? We can probably work with this."
        y "No."
        "Although she hates to reject the easy way out, she won’t let [anime.name] be ruined by low production values like going with the key frames in their current state."
        anim_dir "In that case, yes, we can work faster, for a fee."
        y "How much?"
        anim_dir "{space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS]."
        "She almost accepts, but stops. It’ll be hard enough to tell the others how she messed up, let alone admit she sacrificed a large chunk of their funds as well."
        "Even if it’s the only answer, she doesn’t have the right to make that decision alone."
        y "Okay, I’ll have to discuss this with my team members first."
        anim_dir "Let me know what you decide. Is there anything else you need?"
        y "Not right now. Thank you for showing me the storyboards. I’ll be in touch soon. We’ll find a way to fix this situation."
    show yukari sad
    hide anim_dir with dissolve
    "The words ring hollow in her ears. Find a way? What way? There’s no good way out of this, and she has no one to blame but herself."
    "She trudges out of [anim_studio] with a heavy heart. Each step weighs her down further."
    "How can she face her team after this? How can she look them in the eyes and tell them [anime.name] might be doomed because of her mistake?"
    "Yukari sighs. Maybe she doesn’t have the right to be the director of [anime.name] at all…"
    scene studio_main with fade
    show yukari at left with dissolve
    "When Yukari arrives at the studio, her friends greet her at the door."
    "She walks inside with a sigh."
    show yukari sad at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    "Their anxious questions bounce off her as she struggles to find a way to explain the situation. Maybe she can say it in a way that doesn’t sound so bad."
    show sumiko worry
    s "So... how did it go?"
    "All of Yukari’s hopes for a neat, tidy explanation vanish."
    y "It's a disaster. We're one week behind schedule due to my stupidity."
    show sumiko surprised
    s "What? What happened?!"
    ss "Your guess was right, then?"
    show yukari sad_angry
    y "She nods mutely, once again feeling like she might cry. She let them all down."
    show sumiko
    y "I’m sorry, everyone… I gave [anim_studio] the draft storyboards by mistake. All the animation work they did last week was for nothing, and now…"
    "She trails off and shakes her head."
    y "It won’t happen again, I promise…"
    show yukari sad
    "She sighs. How can she convince them when she doesn’t believe it herself?"
    "Between voice acting, music and marketing, there's so many ways she could screw up. She has no grounds to promise them anything now."
    m "Okay, when you want to make sure you don’t repeat a mistake, you have to understand the cause."
    m "How did this happen in the first place?"
    "Yukari can’t answer. The incident that day replays in her mind over and over."
    "If she just paid attention to where she was going, they wouldn’t be in this mess."
    "The silence stretches on until Shunsuke intervenes to explain."
    ss "Right before Yukari took the storyboards to the studio, there was a mix-up. The papers were accidentally shuffled."
    show sumiko surprised
    s "Wait… you don’t mean when we ran into each other, do you?!"
    y "Yes…"
    show sumiko sad
    s "Oh no! I’m so sorry!"
    y "It’s not your fault. We went through this, remember? You were standing still. I just zoned out and crashed into you."
    "Nevertheless, Sumiko seems distraught."
    show sumiko sad_angry
    s "But don’t you remember? You wanted to go through the pages one last time!"
    s "And I said… I said we already checked them not too long ago, so there was no point. If I’d let you check…"
    y "I’m the director. I should have looked things over again anyway. I should have trusted my instincts."
    show yuuko sad_angry
    yuu "Oh no… This is my fault, too..."
    "Yuuko already-quiet voice drops to almost a whisper."
    yuu "I filed the “drafts” on Monday. If I’d looked more closely at them, I’d have realized they weren’t the right ones."
    yuu "But I didn’t, because I thought I knew what they were. I’m sorry…"
    y "No, don’t blame yourself."
    y "Now both artists look depressed, which makes Yukari feel even worse. The brunt of the error rests on her. She didn’t mean to make them feel guilty."
    m "Okay, everyone, enough of this. There’s no sense in moping around the studio! Yukari, what can we do?"
    show yukari worry
    y "I discussed it with the director of [anim_studio]. We’ll have to fork out a large sum of money in order to finish [anime.name] on time."
    "She takes a deep breath."
    y "And… even if we pay the extra fee, I’m not sure we’ll make it on time unless Yuuko and Sumiko work overtime until [anime.name] is back on schedule."
    y "I'm really sorry about this..."
    "Yukari bows her head and apologizes profusely to everyone."
    "No matter who shares in the blame, she’s mostly responsible. A director shouldn’t make oversights that lead to her team members working overtime."
    "And it’s not like she can compensate them, either."
    "They never had enough funds for salaries, which feels especially painful when she asks them to work extra."
    show sumiko
    s "Cheer up, Yukari. Nobody expected things to end up this way. We’ll be fine working overtime to catch up."
    show yuuko
    yuu "Yeah, don't be so hard on yourself. If I’d checked—"
    show yukari sigh
    y "But I’m the director! I handed over files to the animation studio without knowing for sure what they were! How could I have been so stupid?!"
    show mayumi angry
    m "Didn’t any of you hear me? We can’t change what happened. It’s no use crying over spilt milk, as they say."
    show yukari surprised
    "Yukari jumps, startled by her friend’s sudden shout."
    "Mayumi isn’t as quiet as Yuuko, but it’s rare to hear her raise her voice in frustration."
    m "Stop it, all of you. Let’s look on the bright side."
    show yukari
    s "What bright side?!"
    m "We haven't encountered any major obstacles since we started working on [anime.name]. This is the first one."
    show sumiko happy
    s "You’re right! It’s almost like we were due. So let’s not be too disheartened. We’ll make it work out!"
    ss "Indeed. And as for the cost you mentioned, did you negotiate with the director about it?"
    y "No, why?"
    ss "Most of the time, companies state a higher price than what they actually expect to get, to leave room for negotiation."
    ss "We should be able to seal the deal at about 20\% off the price he told you."
    show mayumi happy
    m "Wow, if what you’re saying is true, then it’s worth a try! We haven’t finalized the deal yet, right, Yukari?"
    "Yukari nods, relieved she didn’t accept the offer right away."
    y "We can try, but how do I negotiate with them? I’m clueless about things like this."
    ss "I can help you. I'll teach you the skills you need to successfully negotiate a better deal."
    y "You're a life saver."
    show sumiko
    s "We better get back to work. We don’t have time to waste."
    "Especially not now. Yukari cringes and wishes again she checked the storyboards one last time before handing them over."
    "At least Yuuko safely filed them away. If she was in the habit of discarding drafts instead, it would have been a nightmare."
    "On the other hand, the old drafts wouldn’t have been there to mix up with the final storyboards…"
    ss "Let me know when you’re ready, Yukari. Don’t rush. Take some time to compose yourself."
    "Yukari bites back an irritated retort. He’s right. While she doesn’t want to waste time, she’s not in any sort of state to learn about negotiating."
    "She doesn’t want to negotiate, she wants to turn back the clock to undo this mistake before it happens."
    y "Not an option, unless someone built a time machine since yesterday..."
    "She half-expects the comment to prompt a story from Sumiko about time travel rumors or a lecture from Shunsuke about the infeasibility of such a thing, but no one says anything."
    scene studio_main
    show yukari at left
    with dissolve
    "The studio is silent and tense as everyone works. Yukari sits down at her desk and tries to focus on the positives."
    "[anime.name] hasn’t completely fallen apart yet. Well, that’s something."
    scene studio_main with fade
    show yukari at left with dissolve
    "By afternoon, she feels a little better and marches to Shunsuke’s desk."
    show shunsuke at right with dissolve
    y "I’m ready."
    show shunsuke worry
    ss "Are you sure?"
    y "I’m as ready as I’m going to be, and the only thing that’ll make me feel better is a sense of progress, which right now means learning how to get us a better deal!"
    show shunsuke
    ss "One of the most important rules of negotiating is to keep a cool head. In other words, don’t yell like that."
    "He sounds as infuriatingly calm as ever."
    "Yukari resists the urge to grab him and shake him until he shows an appropriate level of distress over the situation."
    y "…Okay. I’m calm."
    "Shunsuke teaches Yukari some basic negotiation skills."
    "She needs to find a good balance for the price so the director won't reject her offer outright, while putting it in a comfortable range for their budget."
    "Ideally, her price will leave room for him to give a counter-offer."
    ss "Persuasive speech is also important. Numbers aren’t everything. You need to sound confident and self-assured."
    show yukari worry
    y "So basically the exact opposite of how I feel right now."
    ss "Yes, you still need to calm down before you try to make a deal. Relax. It’s not the end of the world."
    y "But it might be the end of [anime.name]."
    show shunsuke sigh
    ss "Stop that. You’ll doom the deal if you go in with a bad attitude."
    y "I’ll probably doom it anyway…"
    ss "No you won’t. Come on, think positively!"
    y "I just can’t be optimistic right now. I’m sorry. I don’t think I can pull this off."
    "Yukari shrugs listlessly and returns to her desk."
    y "Sure…"
    scene studio_main with fade
    show yukari at left with dissolve
    "In the silence that follows, a gloomy atmosphere falls over the studio."
    "What should Yukari focus on today?"
    menu:
        "Raise funds":
            $choice_7_2_1()
            "With the additional expenses of having the studio redo the animation work at a faster pace, funding is a more critical issue than usual."
            "Yukari spends the day calling up local institutes and community figures with an interest in art and entertainment, to see if they’d be willing to help the production of [anime.name]."
            "Unfortunately, everyone declines. By the time she hangs up the phone after the last call, she feels even more depressed than when she started."
        "Relax":   
            $choice_7_2_2()
            "After what happened, Yukari can’t concentrate on anything. Instead, she closes her eyes and takes deep breaths to try to relax."
            "Guilt nags at her when she thinks about the work waiting for her, but then again, Shunsuke told her to calm down."
            "By the end of the day, she feels slightly less stressed, although the mistake with the key frames still haunts her mind."
        "Cheer everyone up":
            "Yukari takes a few minutes to compose herself."
            "No matter how she feels, she needs to boost the team’s spirits. Low morale will have a terrible effect on their productivity—and they’re also her friends. She doesn’t want to see them sad."
            "Despite their optimistic words, Mayumi and Sumiko are visibly gloomy."
            "Yuuko looks depressed, hunched over her desk without even a trace of a smile. As for Shunsuke, who can say for sure, but he certainly doesn’t look happy."
            scene studio_main  
            show yukari laugh_eyes_closed at pos_left
            show sumiko at pos_middleright
            show yuuko at pos_right behind sumiko
            show shunsuke at pos_outerright
            show mayumi at pos_farleft behind yukari
            with dissolve
            y "All right everyone, let’s not focus on what went wrong. The past is the past. What’s done is done. All we can do is press forward and look to the future."
            if choice_7_2_3():
                show sumiko worry
                s "It does?"
                show yukari happy
                "Yukari suppresses the urge to glare at her and smiles instead."
                y "It does! We’re stronger than this. Besides, think of this like… a test!"
                show sumiko surprised
                s "A test?"
                "Now everyone’s gazes are on her."
                y "Anime production isn’t easy. If we crumble in the face of this setback, how would we ever make it in the anime industry?"
                y "We’ll overcome this and prove we’re ready!"
                show mayumi laugh_eyes_closed
                m "Yeah!"
                show sumiko
                y "Are we going to let ourselves be defeated this easily?"
                show sumiko laugh_eyes_closed
                s "No!"
                y "Who’s going to make it to the end?"
                show yuuko happy
                yuu "We are!"
                y "Why?"
                ss "Because [anime.name] is awesome!"
                "Everyone cheers as though they’ve already overcome all their obstacles, and for a moment Yukari wonders if she overdid it a little."
                "Nevertheless, at least everyone’s smiling again."
            else:
                "Silence greets Yukari’s words. Everyone stares down at their desks. No one meets her gaze."
                y "It does!"
                "Once again, no one responds. At last, Shunsuke looks up."
                ss "I’m sure Yukari has worked through everything to figure out why we should be optimistic about the future."
                "Yukari gives him a grateful smile."
                ss "Go on, Yukari, explain it."
                "Her smile fades."
                y "Uh… well…"
                m "You do have a reason, don’t you?"
                show yukari happy
                y "Y-yeah, it’s… well, I just think everything will be fine if we stay focused!"
                "She injects as much confidence into her voice as possible, but it falls flat."
                "The others look at her for a moment longer and then return to their work. If anything, the studio’s atmosphere feels even gloomier than before."
label week_7_2:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show shunsuke at Position(xalign=0.82,yalign=1.0)
    show yuuko at Position(xalign=1.15,yalign=1.0)
    with dissolve
    ss "Yukari, are you ready to work out a new deal for the animation work?"
    "From the tone of his voice, he worries she still isn’t in a good state of mind to handle negotiations."
    y "Almost there... Give me a moment."
    "She takes a deep breath and tries to get her act together. If she heads to [anim_studio] feeling as depressed as she does currently, it could lower their chances of getting a better price."
    "Shunsuke said confidence was important, and she knows she doesn’t look confident at all."
    ss "Remember, the perfect deal is one where both parties feel they’ve “won” the negotiation. Stay calm, and you can do this."
    show yuuko sad
    yuu "Here. These are the finished storyboards I accidentally filed that time..."
    "She checks them over to make sure they’re correct and then heads to the studio."
    if anim_studio == anim_studio_expensive:
        scene animation_studio with fade
        show yukari at left with dissolve
        y "Hello, I’m here to see [anim_studio_dir]."
        staff "He’s been expecting you."
        "Yukari turns and sees the director seated at the table where they’ve held their previous discussions."
        show anim_dir at right with dissolve
        y "Oh! Hello."
        anim_dir "Hello. I assume you’ve discussed the situation with your team members?"
        y "Yes. In order to keep [anime.name] on schedule, we need the animation team to work faster."
        anim_dir "I understand. As I said yesterday, we’ll need to add an additional fee of {space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS]."
        $negotiation_buffer_high = NEGOTIATE_SUCCESS_FUNDS - 3
        y "My team and I think {space=15}{image=small_moneybag.png} [negotiation_buffer_high] should be more than enough to cover it."
        "She puts on a valiant look in the hopes that perceived confidence will convince him to accept her offer."
        "Deep in her heart, however, she can’t help but picture the worst possible outcome—the director walking away from the deal completely."
        anim_dir "Hmm..."
        "Her heart hammers. “Hmm”? Is that a good sign or a bad one?"
        "It feels like an eternity as Yukari waits for his response. All she can do is silently pray for success."
        $dice_number = renpy.random.randint(0,100)
        if dice_number <= choice_raise_funds_formula():
            anim_dir "Since [anime.name] is a smaller project than many we deal with, I can see how a lower price would be acceptable. However…"
            "Yukari holds her breath."
            anim_dir "I propose a price of {space=15}{image=small_moneybag.png} [NEGOTIATE_SUCCESS_FUNDS] instead."
            "She feels like she might pass out, but she reminds herself that Shunsuke told her to expect a counter-offer once she named her price. So far so good."
            y "Well…"
            "Their negotiations continue for a while longer, with each of them suggesting prices until at last they reach an amount they both can agree on."
            anim_dir " Very well then. I’ll prepare a new contract to speed up the animation work for [anime.name] at an additional fee of {space=15}{image=small_moneybag.png} [NEGOTIATE_SUCCESS_FUNDS]."
            y "Thank you, sir!"
            anim_dir "I’ll be right back with the contract."
            hide anim_dir with dissolve
            show yukari happy
            "Yukari lets out a long breath and leans back. She did it."
            "Despite all her fears, she pulled off a successful deal with Asahi Studio."
            "Her blunder with the storyboards could have been disastrous, but she managed to minimize the damage it caused."
            $negotiate_success()
        else:
            anim_dir "I’m sorry. I’m afraid it isn’t in our best interests to accept your offer."
            show yukari surprised
            y "What? Why?"
            anim_dir "We have several other projects to work on besides [anime.name]. Accepting a lower fee could compromise them."
            "Yukari’s heart sinks, but she knows she has no choice but to accept his original offer now."
            "It will hurt their budget a fair bit. She needs to raise more funds for [anime.name] as soon as possible."
            show yukari sad
            y "In that case, we’ll accept your original offer."
            anim_dir "Very well then. This morning I had a new contract prepared to speed up the animation work for [anime.name] at an additional fee of {space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS]."
            anim_dir "I’ll be right back with it."
            hide anim_dir with dissolve
            "As he leaves to get the contract, Yukari puts her head in her hands."
            "Telling the team about this won’t be easy, but at least her blunder with the storyboards hasn’t cost [anime.name] its future."
            $negotiate_default()
    elif anim_studio == anim_studio_cheap:
        scene animation_studio with fade
        show anim_dir smile at right
        show yukari at left
        with dissolve
        anim_dir "Hello. I thought I might be seeing you today!"
        "Yukari jumps. Was he waiting for her?"
        y "I’m here about what we discussed yesterday. In order to keep [anime.name] on schedule, we need the animation team to work faster."
        anim_dir "At an additional fee of {space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS], right?"
        $negotiation_buffer_high = NEGOTIATE_SUCCESS_FUNDS - 3
        y "My team and I think {space=15}{image=small_moneybag.png} [negotiation_buffer_high] should be more than enough to cover it."
        "She puts on a valiant look in the hopes that perceived confidence will convince him to accept her offer."
        "Deep in her heart, however, she can’t help but picture the worst possible outcome—the director walking away from the deal completely."
        show anim_dir smile 
        anim_dir "Aha, going to negotiate with me, are you?"
        "Her heart hammers. He sounds intrigued, but does that mean he’ll accept, or will he reject her offer anyway?"
        "It feels like an eternity as Yukari waits for his response. All she can do is silently pray for success."
        $dice_number = renpy.random.randint(0,100)
        if dice_number <= choice_raise_funds_formula():
            anim_dir "Just this one time, okay?"
            show yukari surprised
            y "Yukari blinks at him in confusion before she realizes he’s accepting her offer. No counter-offer? The negotiations went much better than she expected."
            anim_dir "I can tell you’re sincere enough to learn from your mistakes, and I can feel your burning passion to produce anime. I can’t let you down."
            show yukari happy
            y "Thank you, sir!"
            "She beams, thrilled that she negotiated a better deal with [anim_studio] so quickly."
            $negotiate_success()
        else:
            show anim_dir
            anim_dir "I admire your initiative… but I’m afraid I can’t accept your offer."
            show yukari sad
            y "What? Why?"
            anim_dir "We have multiple projects and only a small team. If we accept a lower fee to work on [anime.name], it might force us to lower the production values of the other shows."
            "Yukari’s heart sinks and she wants to argue, but considering [anim_studio]’s recent track record, he probably has good reason to be concerned."
            "She nods. She has no choice but to accept his original offer."
            "It will hurt their budget a fair bit, the outcome she’d hoped to avoid by working with [anim_studio] in the first place."
            "She needs to raise more funds for [anime.name] as soon as possible. Telling the rest of the team about this won’t be easy."
            y "I understand. We accept your original offer."
            anim_dir "All right, then we’ll speed up our work on [anime.name] for a fee of {space=15}{image=small_moneybag.png} [NEGOTIATE_DEFAULT_FUNDS]."
            $negotiate_default()
    anim_dir "Aside from price, though, there’s one other concern you should know about."
    show yukari worry
    y "Concern? What is it?"
    "She hopes she doesn’t sound as panicked as she feels."
    anim_dir "We won’t be able to get [anime.name] back on schedule on our own."
    anim_dir "Our animation team isn’t large enough to work at an accelerated rate while keeping our other projects on track as well."
    "Yukari grits her teeth. He couldn’t have told her that before their negotiations?"
    anim_dir "This means either your studio members will have to work overtime to help us or you’ll have to hire freelancers."
    anim_dir "I recommend a combination of both. In this industry, it’s easy to miss deadlines, so it’s best to have a safety net."
    show yukari
    y "Got it. I’ll see what we can do."
    "It isn’t ideal, but at least production of [anime.name] will continue and she minimized the consequences of her blunder with the storyboards."

label week_7_3:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show mayumi_f happy at right
    with dissolve
    stop music fadeout 2.0
    m "Hey Yukari, I’ve got good news for you."
    y "Oh? What is it?"
    "Good news is something they definitely need. The atmosphere in the studio still hasn’t recovered."
    m "Do you remember what we discussed last week?"
    y "I’m… not sure."
    "Everything before her discovery of the animation mix-up is a blur. Last week feels like it was years ago."
    m "We talked about making an appointment this Friday with the voice actors I hired for [anime.name] to record their lines."
    m "I managed to secure a slot for the whole afternoon. We should be able to make great progress on the voice acting for [anime.name]."
    show yukari sad_angry
    y "That's wonderful!"
    "She sighs."
    show mayumi_f worry
    m "You… don’t look happy."
    y "No, I’m glad it worked so well. You’ve done a great job with everything. Maybe you should have been the director of [anime.name] instead of me…"
    show mayumi_f sigh
    m "Yukari…"
    y "You even managed to stay positive after what happened. I can’t. I think about it over and over and wish I handled things differently."
    y " I should have looked over the storyboards again before taking them to the studio. I should have checked on their progress. I should have--"
    m "You’re a wonderful director. I wouldn’t be cut out for your role at all."
    show yukari sad
    y "Hah!"
    show mayumi_f
    m "I mean it. Everyone has their own strengths and weakness. You’re a leader. I’m not."
    show yukari surprised
    y "How have I been a good leader?"
    m "You got investors for [anime.name], you delegate tasks to everyone, and you always do your best to keep everyone on the team happy."
    m "Not to mention you’re working on the storyboards, too."
    y "The storyboards? That’s what started this mess!"
    show mayumi_f sigh
    show yukari
    m "Without you, would we even have storyboards?"
    y "Sure, Shunsuke would have handled them. I’ve needed his help often enough already."
    y "And half the time I need your help. You probably boost the team’s morale more than I do, anyway."
    show mayumi_f tsundere
    m "Yukari! Being a good leader doesn’t mean you do everything yourself."
    m "Of course you ask us for help. We’re your team members—and your friends!"
    m "And don’t forget, we wouldn’t have a team at all without you. [anime.name] was your vision, and you gathered everyone together."
    show mayumi_f sad_angry
    m "Maybe to you it looks like I’d be a good leader, but I wouldn’t have fared nearly as well in your shoes."
    y "If you say so…"
    show mayumi_f
    m "Stop stressing out about it so much. You don’t need to take all of the responsibility on your own shoulders, you know."
    m "I’m here for you if you need someone to talk to. We all are."
    show yukari laugh_eyes_closed
    "Yukari meets her earnest gaze and manages a smile."
    y "Thank you, Mayumi. Just like the old days, you’re always here to help me up when I’m down. No wonder you’re my best friend."
    show mayumi_f laugh_eyes_closed
    m "Just try to relax a little and remember you can depend on us. We're all in this together as a team."

label week_7_4:
    $nextDay()
    scene studio_main with fade
    show yukari at left with dissolve
    y "Hi everyone, sorry I can’t stay long. I'll be heading over to [anim_studio] for a while today." 
    y "Gotta make sure things are progressing smoothly so we don’t have any more major problems popping up out of nowhere. I won’t make that mistake twice!" 
    hide yukari with dissolve
    "As Yukari leaves the studio, everyone is hard at work. The room is quiet, with little more than the sound of shuffling papers. After a moment, Shunsuke breaks the silence."
    scene studio_main
    show mayumi at pos_farleft
    show shunsuke_f at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright
    with dissolve 
    ss "It sure is dead around here these days." 
    "Mayumi nods." 
    ss "I know Yukari’s the loudest one on the team, but I didn’t expect it to feel this strange when she leaves the studio." 
    s "I know what you mean." 
    yuu "Yukari’s the one who brought us together. If it wasn’t for her, we wouldn’t be working on [anime.name]. Our dreams wouldn’t be anywhere near a reality."
    ss "I hope she doesn’t still feel too guilty about what happened. She certainly is passionate." 
    yuu "And kind. I’ll never forget how we first met."
    show mayumi surprised 
    m "You mean when she went to the restaurant that night to ask you about joining the team?" 
    "For a long moment, Yuuko is silent. Then at last, she shakes her head." 
    show yuuko happy
    yuu "No. She doesn’t remember, but we met once before." 
    m "What happened?" 
    yuu "She saved my life." 
    m "Really?!"  
    show sumiko sigh
    s "She’s exaggerating." 
    show mayumi
    yuu "Maybe, but at the time it didn’t feel that way. There was a group of students infamous for being bullies. You didn’t mess with them, you just let them do what they wanted." 
    ss "I remember them." 
    yuu "I bumped into them one day. It was an accident, but, well… it’s how they were."
    yuu "They were shoving me around and cursing at me. I couldn’t get away. Then Yukari saw what was happening."
    show yuuko laugh_eyes_closed
    yuu "She marched over and yelled at them to leave me alone, punched the leader in the nose, and pulled me out of there." 
    show mayumi surprised
    m "She actually hit him?!" 
    yuu "Yep. I thought we were so dead. We ran clear across town." 
    show sumiko happy
    s "You should’ve heard her when she got home. Yukari this, Yukari that. You’d think Yukari was a superhero or something." 
    show yuuko tsundere
    yuu "Oh, stop! To me, she was. She saved me and never thought twice about it. She said she had to help someone in need, and it didn’t matter how big or scary those guys were." 
    ss "And they never bothered you again." 
    show sumiko surprised
    s "Huh? How do you know?"  
    show shunsuke_f laugh_eyes_closed
    ss "I, uh… it just sounded like a fitting end to the story, that’s all." 
    "He quickly looks away." 
    yuu "He’s right, though. They never came near us after that. I always wondered why." 
    show mayumi happy
    m "I know! I bet there was another hero, lurking in the shadows, who was impressed by Yukari’s courage and took the opportunity to scare them off for good!" 
    show sumiko happy
    s "A secret hero in the shadows? Come on, things like that don’t happen in real life."
    show mayumi sad_angry 
    m "Aw, but…" 
    show shunsuke_f
    ss "Don’t be such a downer, Sumiko. It’s possible something like that happened."
    show sumiko tsundere
    s "Strange to hear that from Mr. Logical." 
    "He shrugs and clears his throat." 
    ss "All right, enough reminiscing. We have a lot of work to do and only a limited time to do it in. Let’s show Yukari everything is going to be fine!" 
    show mayumi
    show sumiko
    show yuuko
    s "Yeah, let’s do this!" 
    "The studio is still quiet without Yukari, but the atmosphere isn’t as oppressive as it was before."
    "Yuuko works with a smile on her face, as if telling the story lifted a weight from her shoulders. Shunsuke devotes himself to the storyboards with renewed energy."
    "As for Sumiko and Mayumi, they act determined to restore optimism to the team through force of will alone if necessary."
    "When Yukari returns later that day, cheerful greetings meet her at the door. It’s almost like the incident with the key frames never happened at all." 
    "Despite her worries about the future, she can’t help but smile back. Her responsibilities no longer seem so difficult to bear." 
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_5_to_7,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_5
label week_7_5:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show mayumi_f laugh_eyes_closed at right
    with dissolve
    m "Are you ready to go to the recording studio, Yukari?" 
    y "Yeah, let’s head over there." 
    m "Wait, before we go, I forgot to tell you something." 
    show mayumi_f
    "Yukari stops dead in her tracks."
    show yukari worry
    y "What? No way! What did you forget?" 
    "Her heart pounds and her mouth goes dry. It’s going to be bad news, isn’t it? She can’t take any more bad news, not after she finally started to feel better. She braces herself for the worst." 
    m "Remember when we discussed you overseeing some of the audio work?"
    m "Well, this is the only time I’ll be able to attend the recording sessions with you, because I need to compose the soundtrack for [anime.name]." 
    show yukari surprised
    y "You mean after this I’ll have to deal with the voice actors on my own?"
    m "You'll be fine. I’ll be here for this session, so pay close attention. And if anything goes wrong, you can always ask me for help." 
    show yukari
    y "All right." 
    "All in all, it’s not nearly as bad of news as she feared."
    play music cafe_music fadeout 2.0 fadein 2.0 
    scene recording_studio with fade
    show yukari laugh_eyes_closed at left
    show mayumi_f at right
    with dissolve
    y "Whoa, this place is beautiful!" 
    m "Yup, they recently renovated, so it looks amazing." 
    m "Wait here while I get the director of [va_studio]." 
    hide mayumi_f with dissolve
    show yukari
    "Mayumi leaves, and Yukari takes some more time to admire the beautiful studio. A few minutes later, Mayumi reappears with the director." 
    scene recording_studio with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show va_dir at right
    with dissolve
    va_dir "Hello Yukari. It’s good to meet you. Let's make the voice acting for [anime.name] a success!" 
    "Yukari shakes his hand." 
    va_dir "Today we’d like to get the voice actors accustomed to their roles and cover as much ground as we can for Episode One." 
    va_dir "The voice actors will be arriving shortly. Do you know who they are?" 
    y "Yes." 
    va_dir "Great! It’s good to see you’re on top of things. Now I'll brief both of you on what we will be doing in the studio." 
    "He explains the process of recording voices. It sounds complicated, but Yukari tries her best to listen attentively."
    "Since Mayumi won’t be with her during the other sessions, she wants to make sure she understands everything." 
    va_dir "That should be all you need to know. Can you wait for me here while I set things up?" 
    y "Sure, no problem." 
    hide va_dir with dissolve
    "The director leaves the room and talks to several other staff members before disappearing from sight." 
    "Yukari runs through everything he told them again. She isn’t sure how much of the process she’ll need to deal with, but if she’s to oversee the recording, she needs to know what’s supposed to happen."
    "Otherwise, something might go wrong. [anime.name] doesn’t need any more trouble."
    scene recording_studio
    show yukari at left
    show mayumi_f at right
    with dissolve 
    m "…Yukari?" 
    "Yukari blinks. Mayumi gives her an inquisitive look." 
    show yukari surprised
    y "Sorry, did you say something?" 
    m "I asked if it felt strange for you to spend so much time out of the studio these days." 
    show yukari
    y "Oh… yeah, I guess it does." 
    "In truth, she’s been so busy lately and so worked up over the key frames, she hasn’t had a chance to notice." 
    show mayumi_f worry
    m "You’ve been too busy to notice, haven’t you?" 
    y "Did you read my mind?" 
    show mayumi_f
    m "Haha, no. I just know what happens when you really focus on something. Everything else fades away and you give it your full attention."
    show yukari surprised 
    y "I do that often?" 
    show mayumi_f sigh
    m "You always have. Remember the play when we were kids?" 
    show yukari
    "With a laugh, Yukari nods. They were very young back then, and their class put on a school play."
    "Most of the students got roles to play, but the teachers made Yukari the play’s director." 
    show yukari sigh
    y "My parents fought with me every night to get me to do my homework. I didn’t want to do anything that could distract me from the play." 
    m "And you constantly asked the other actors if they had their lines memorized yet or if they needed help." 
    y "It felt like such a huge responsibility. I thought I was going to go crazy." 
    show mayumi_f laugh_eyes_closed
    m "Instead you almost drove us crazy instead." 
    show yukari laugh_eyes_closed
    "They laugh together, and some of Yukari’s tension drains away."
    show yukari 
    y "Am I still like that?" 
    show mayumi_f
    m "Extremely focused, trying to micromanage everything, and driving people crazy? You’ve gotten better about it." 
    show yukari happy
    y "Glad to hear it." 
    m "Of course, you still could relax a little…" 
    y "You know, I haven’t thought about that play in years. I wonder if that’s when my dream of directing an anime began, even though I didn’t watch anime yet back then." 
    m "Maybe it was. Hey, do you hear footsteps? I think someone’s coming!" 
    play sound [sfx_rs_door_open,sfx_rs_door_close]
    if anime.category == Anime.HAREM:
        #a = male,b = female, c = female
        scene recording_studio
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        show va_sakura laugh_eyes_closed at right
        with dissolve
        va_c_char "Hi!" 
        "The girl bounces over to them and shakes their hands." 
        va_c_char "I’m [va_c]! I can’t wait for [anime.name]!" 
        "Yukari glances at Mayumi, who mouths “Kiko” before turning back to the voice actor."
        show mayumi laugh_eyes_closed
        m "I’m excited, too! This is Yukari, the director of [anime.name]." 
        y "Good to meet you." 
        va_c_char "This is going to be so much fun!" 
        play sound sfx_rs_door_open 
        show va_sakura at va_pos_c
        show va_a at va_pos_a
        with dissolve
        unknown "Is this where I’m supposed to be?" 
        m "Yep, come on in!" 
        "The young man stares around the studio in awe, seemingly as amazed by it as Yukari was when she arrived. He’s so distracted, he trips and stumbles the rest of the distance to them." 
        unknown "Oops. Um, hi. I’m Bradley." 
        "He holds out his hand." 
        m "This is Yukari, the director of [anime.name]." 
        "Yukari shakes his hand, puzzled by his behavior until she remembers Mayumi said he was new to voice acting." 
        y "I’m happy to meet you. This studio is beautiful, isn’t it?" 
        va_a_char "Yeah, it really is!" 
        show va_b happy at va_pos_b with dissolve
        "A woman sweeps into the room with a calm smile." 
        va_b_char "You must be Yukari, the director. I’m [va_b]." 
        y "Yep, that’s me. Glad to meet you." 
        "The woman turns." 
        show va_b
        va_b_char "And you two must be the voice actors for… Keiji and Kiko?" 
        va_a_char "Y-yeah!" 
        va_c_char "How did you know?" 
        va_b_char "A simple deduction based on the most important roles in the script." 
        "Yukari leans close to Mayumi." 
        y "Did we hire a clone of Shunsuke?" 
        "Mayumi giggles, but elbows her." 
    elif anime.category == Anime.ACTION:
        scene recording_studio with fade
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        show va_a at pos_right
        with dissolve
        # a = guy, b = female, c = male
        va_a_char "Hello again, Mayumi."
        show mayumi laugh_eyes_closed
        m "Hi! Yukari, this is [va_a]. He’ll be doing the voice of Itaru." 
        y "It’s good to meet you. I’m the director." 
        va_a_char "Good to meet you, too. I’m looking forward to [anime.name]." 
        play sound sfx_rs_door_open 
        show va_a at va_pos_a
        show va_c at va_pos_c
        with dissolve
        unknown "Greetings." 
        "His deep voice fills the studio, and he stalks toward them with his hand outstretched." 
        unknown "I am [va_c]."
        show yukari surprised
        y "Y-Yukari, the director!" 
        "She shakes his hand and tries to avoid his gaze, which seems to stare straight into her soul. To her relief, he lets go and turns to terrify the other voice actor instead." 
        m "I did warn you that Norio’s voice actor is intense." 
        y "No kidding…" 
        show yukari
        show va_b at va_pos_b with dissolve
        va_b_char "I see I’m the last to arrive." 
        "She politely bows to everyone." 
        va_b_char "My name is [va_b]." 
        m "This is Yukari, [va_a], and [va_c]." 
        va_b_char "It is a pleasure to meet all of you." 
        va_c_char "Likewise." 
        "Their eyes meet. She meets his piercing stare with a steely gaze of her own. Neither one of them moves." 
        show yukari surprised
        y "U-uh… Mayumi? What are they doing?" 
        m "I’m not sure. But [va_b] seems like a commanding sort of person, so maybe this is a silent struggle for authority." 
        show yukari
        y "Oh great, that’s all we need." 
        show mayumi happy
        m "Time to do your thing!" 
        y "My “thing”?" 
        m "Yeah, take charge. You’re our leader, after all." 
    elif anime.category == Anime.MYSTERY:
        # a = male, b = female, c = male
        scene recording_studio with fade
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        show va_a laugh_eyes_closed at pos_right
        with dissolve
        va_a_char "Ahh! It’s happening! It’s really happening!" 
        "He runs to the center of the studio and bows to an imaginary audience before tipping his imaginary hat." 
        va_a_char "Ahem! “When you have eliminated the impossible, whatever remains, however improbable, must be the truth.” Ahh!" 
        show yukari sigh
        y "Is… he all right?"
        show mayumi laugh_eyes_closed
        m "He’s fine. Just excited. Very excited." 
        "She raises her voice." 
        m "I’d like you to meet Yukari, the director of [anime.name]!" 
        "He stops his impromptu acting and dashes over to them." 
        show va_a
        va_a_char "I’m so glad to meet you. I’m [va_a], I’ll be playing Hideaki, and don’t worry, I’ve been practicing by reading up on all the great detective stories and watching mystery films and everything! It’s going to be great!" 
        play sound sfx_rs_door_open 
        show va_b at va_pos_b with dissolve
        unknown "Anyone here?"
        show va_a happy 
        va_a_char "Megumi!" 
        show va_b laugh_eyes_closed
        unknown "Hideaki!" 
        "They run toward each other and hug as though they’re actually the characters whose voice they’ll provide." 
        show mayumi
        show yukari
        m "This is Sakura, who will voice—" 
        y "Megumi." 
        va_a_char "So did you follow my advice?" 
        va_b_char "I did better than that! After I read the first mystery novel, I recreated the crime scene in the park so I could visualize it even better." 
        va_a_char "Whoa!" 
        va_b_char "It was so authentic. The police arrived and everything!" 
        "Yukari glances at Mayumi, who shrugs." 
        m "Actors can be eccentric." 
        "Yes, but too much eccentricity could make these recording sessions a nightmare."
        show va_c at va_pos_a with dissolve
        va_c_char "Is this… oh good, I’m in the right place." 
        "As he walks toward them calmly, Yukari lets out a sigh of relief that at least one of their three voice actors isn’t crazy." 
        va_c_char "I’m [va_c]." 
        y "I’m Yukari, the director. It’s good to meet you." 
        va_c_char "It is an honor, Yukari. [anime.name] sounds like a delightful project, and I cannot wait to lend you my talents." 
        va_a_char "Ahh! It’s Shin!" 
        va_b_char "Shin!!!" 
        va_c_char "Oh, I’m sorry. Are we supposed to be in-character right now? I’m afraid I didn’t realize…" 
        "He clears his throat, and his entire demeanor changes." 
        show va_c angry
        va_c_char "You FOOLS! What is the meaning of this?!"
        show yukari surprised
        "Yukari yelps and jumps backward." 
        va_c_char "This is an outrage! I won’t stand for this sort of behavior!"
        show va_b surprised
        va_b_char "Eeek! I didn’t mean anything by iiiiit!"
        show yukari
        "Yukari stares at them and then turns her confused gaze to Mayumi in the hopes of getting an explanation. Mayumi shrugs." 
        m "At least they’re into it, right?" 
    scene recording_studio with fade
    show va_dir_f at left
    show va_a at va_pos_a
    if anime.category == Anime.HAREM or anime.category == Anime.ACTION:
        show va_b at va_pos_b
    else:
        show va_sakura at va_pos_b
    if anime.category == Anime.MYSTERY or anime.category == Anime.ACTION:
        show va_c at va_pos_c
    else:
        show va_sakura at va_pos_c
    with dissolve
    "The director’s return prevents any further conversation." 
    va_dir "All right! Now that everyone is here, let’s begin!" 
    "It’s slightly chaotic at first as they get everyone situated, but soon they’re ready to begin recording their dialogue for the first episode of [anime.name]." 
    "The recording goes smoothly, and Yukari silently applauds Mayumi’s judgment."
    "Each voice actor seems perfect for his or her role. And when all three are in a scene together, that’s when she can really feel [anime.name] becoming a reality." 
    if anime.category == Anime.HAREM:
        hide va_dir_f
        hide va_a
        show va_a_f surprised at left
        show va_b at va_pos_c
        show va_sakura happy at va_pos_b
        with dissolve
        va_a_char "H-huh?! Where’s everyone else?" 
        va_b_char "Everyone else? What do you mean? This IS everyone." 
        va_a_char "B-but… you mean… I’m the only guy in the science club?!"
        show va_sakura laugh_eyes_closed
        va_c_char "What’s wrong with that? Ehehehe…"
        show va_a_f
        va_a_char "I’m just surprised, that’s—huh? What’s that smell?" 
        show va_sakura
        va_c_char "Must be my experiment." 
        show va_b shocked
        va_b_char "Experiment? Kiko, you didn’t leave it unattended, did you?" 
        va_dir "Cut!" 
        show va_a_f
        show va_b
        show va_sakura
        m "All right, now there’s a brief break for the explosion, and then the scene resumes…" 
        "Yukari watches with interest as they return to the script."
        show va_a_f shocked 
        va_a_char "W-what was that?!" 
        va_b_char "Kiko!" 
        show va_sakura laugh_eyes_closed
        va_c_char "My hypothesis was correct! Ahahaha!" 
    elif anime.category == Anime.ACTION:
        hide va_dir_f
        hide va_a
        show va_a_f shocked at left
        show va_b at va_pos_c
        show va_c at va_pos_b
        with dissolve
        va_a_char "This… this is crazy! What’s going on?" 
        show va_b sad
        va_b_char "Is something wrong, Itaru?"
        show va_a_f surprised
        va_a_char "Agh! Don’t sneak up on me like that!"
        va_b_char "I didn’t mean to startle you." 
        show va_b
        show va_a_f sad
        va_a_char "And no, nothing’s wrong. I just… listen, I’m afraid I have to cancel our plans." 
        show va_b shocked
        va_b_char "What? Why?"
        va_c_char "It is my fault. I must apologize."
        va_a_char "Agh!"
        show va_c laugh_eyes_closed
        va_c_char "Itaru and I have pressing business to discuss. Would you be so kind as to leave us alone?"
        show va_b 
        va_b_char "Oh, of course. I didn’t mean to disturb you." 
        va_a_char "Wait—" 
        show va_c angry
        va_c_char "Now, now… do you really want to involve her in this? It’s time we had a chat… just the two of us." 
    elif anime.category == Anime.MYSTERY:
        # a = male, b = female, c = male
        hide va_dir_f
        hide va_c
        show va_c_f shocked at left
        show va_b at va_pos_b
        show va_a at va_pos_c
        with dissolve
        va_c_char "Deplorable! I never dreamed I’d be treated this way…" 
        va_a_char "Hmm…" 
        va_b_char "What do you think happened here?" 
        show va_a laugh_eyes_closed
        va_a_char "Elementary, my dear Megumi!" 
        va_dir "Cut!" 
        show va_c_f
        show va_b
        "The voice actors stop, and Yukari watches with interest as the director shakes his head and holds up the script." 
        va_dir "That last line wasn’t in the script." 
        show va_a
        va_a_char "I thought I’d improvise! See, I’ve been reading mysteries, and—" 
        "The director looks at Yukari and Mayumi with a questioning glance." 
        m "Sorry, [va_a]. Could you stick with the script?" 
        va_a_char "Aw, okay…" 
        va_dir "Let’s try this scene again, from Megumi’s line." 
        va_b_char "What do you think happened here?" 
        va_a_char "I can’t be sure yet, but… hmm…" 
        va_c_char "What is it? What did you find?" 
        show va_a happy
        va_a_char "A clue." 

    "The session continues in a similar fashion. Sometimes they need to record a section again, but overall it goes smoothly."
    "Yukari pays close attention to everything Mayumi says and does."
    "The voice actors seem to get along well with each other, which helps. By the time they finish their scenes, Yukari feels more relaxed about the prospect of working with them and giving them instructions." 
    scene recording_studio with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show va_dir at pos_right
    with dissolve 
    va_dir "Well, that’s it for today. The next recording session will be next Thursday, if that fits all of your schedules." 
    y "That sounds fine to me!"
    "The voice actors nod in agreement." 
    va_dir "Mayumi?"
    m "Oh, I won’t be able to make it from now on, but Yukari can handle everything." 
    va_dir "In that case, I look forward to working with you on Thursday, Yukari." 
    "Yukari smiles nervously." 
    m "Let’s go. If you have any questions, just ask me." 
    y "Okay." 
    scene restaurant with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music restaurant_music fadein 2.0 fadeout 2.0
    "Yukari is exhausted by the time she joins the others at the restaurant that evening. The day itself wasn’t too tiring, but the entire week left her drained." 
    show yukari sigh
    y "What a week…" 
    yuu "Tired? Me too."
    s "How did the recording go?"
    show mayumi laugh_eyes_closed
    m "It went great!" 
    ss "The voice actors fit their roles well?" 
    if anime.category == Anime.HAREM:
        m "Yeah, and they seem like a fun group!" 
        show yukari happy
        y "You’d like Natsume’s voice actor. She’s like a female Shunsuke clone."
        ss "Excuse me?" 
        y "She’s logical and analytical." 
        ss "I’ll take it as a compliment, then." 
    elif anime.category == Anime.ACTION:
        m "Definitely, especially the guy we have playing Norio. He’s perfect!" 
        show yukari surprised
        y "Perfect? He’s terrifying!" 
        ss "That sounds perfect for Norio." 
    elif anime.category == Anime.MYSTERY:
        m "Oh yes. Maybe too well." 
        show shunsuke surprised
        ss "How can they fit their roles too well?" 
        show yukari happy
        y "Our detective wants to be a combination of every famous detective ever and his assistant staged a phony crime in the park to get into the mood." 
        y "As for Shin’s voice actor, he is a mild-mannered man until he gets in-character and starts shouting."
        ss "…Oh my." 
        show sumiko laugh_eyes_closed
        s "Sounds like things are going well!" 
        m "Yes, they are." 
    show yukari
    show sumiko
    show mayumi
    "From there, the conversation diminishes. Yukari yawns and focuses on her food. She doesn’t have the energy to socialize." 
    "Everyone else seems to feel the same way. They eat quietly." 
    "The silence is oddly relaxing, and Yukari takes the time to think through what happened with the storyboards."
    "It was a major setback, but now she’s confident they can overcome it, one way or another."
    "When she started working on [anime.name], she knew it would be tough, but she thought they could avoid any major issues with enough planning." 
    "But planning can’t cover everything. Mistakes happen, and they have to deal with them." 
    "As the evening comes to a close, Shunsuke stands up and lifts his glass." 
    show shunsuke happy
    ss "I propose a toast to [anime.name]."
    yuu "Now? Even after the trouble we had this week?" 
    ss "Yes. We’re back on track, and it will only get better from here."
    show yukari worry
    y "I don’t know… I think Murphy has it in for us."
    show sumiko surprised
    s "Who’s Murphy?" 
    ss "Murphy’s Law?" 
    y "Yep. “Anything that can go wrong, will go wrong.”" 
    m "Hmph. Well I favor Yhprum’s Law: “Everything that can work, will work.”" 
    show yuuko sigh
    yuu "Overconfidence is just as dangerous as pessimism."
    show yukari happy
    y "How’s this, then? Anything that can go wrong, will go wrong, but we’ll overcome it all." 
    show sumiko tsundere
    s "What’s that, Yukari’s Law?" 
    y "Maybe." 
    show shunsuke laugh_eyes_closed
    ss "I like it. To [anime.name] and Yukari’s Law!"
    show yuuko happy
    show sumiko happy
    everyone "To [anime.name] and Yukari’s Law!" 


label week_7_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "Over the weekend, Yukari writes up a report to send to their investors about the current status of [anime.name]."
    "When it comes to the animation incident, she tries to find a balance between glossing over the details and making it sound like a disaster."
    "It’s a fine line to walk, but at last she’s satisfied that her report is honest but still optimistic." 
    "Fortunately, they’ve made other progress she can include, as well. She adds a detailed account of their work with the voice actors and sends the report Sunday afternoon."
    scene studio 
    $nextWeek()
    $mayumi_tasks[0] = mayumi_second_task
    $yukari_tasks[0] = yukari_third_task
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)

label week_8_1:
    scene studio_main with fade
    show yukari at left
    show sumiko surprised at pos_right
    show yuuko at pos_outerright behind sumiko
    with dissolve
    play music studio_music fadeout 2.0 fadein 2.0
    s "Whoa, there you are! I thought you overslept." 
    y "Nope. I went to [anim_studio] this morning to check on their progress and photocopy the key frames. I thought it was better to do it early so I can work on [anime.name] this afternoon." 
    y "If I remember right, both you and Yuuko wanted to check the key frames." 
    show yuuko laugh_eyes_closed
    yuu "Yeah, I'm really excited!" 
    show sumiko laugh_eyes_closed
    s "Me too!" 
    y "Give me a moment." 
    "Yukari puts down her bag and reaches inside for the files containing the key frames, neatly sorted into many different categories." 
    y "Here’s the first key frame." 
    show yuuko worry
    show sumiko
    "As they look through the key frames, Yuuko rubs her head, clearly concerned."
    y "Is something wrong?" 
    if anime.category == Anime.HAREM:
        yuu "Oh… it might just be me…"
        show yukari sigh
        y "Come on, I’m having you two check the animations for a reason. If there’s a potential problem, you should let us know." 
        yuu "But I’m not sure what it is. Something about these key frames just seems…" 
        s "Sloppy." 
        yuu "Huh?" 
        s "I noticed it too. It’s mostly fine for the character interactions, but the animations for the science experiments look rushed." 
        yuu "Do you think it matters? It’s a character-driven story, after all."
        show sumiko sad_angry 
        s "If both of us noticed just from the frames, the audience will notice, too." 
        y "And the investor told me science stories are popular right now.We can’t let the science aspect appear sloppy." 
    elif anime.category == Anime.ACTION:
        yuu "It’s just… this first chase sequence. It should be a really exciting moment in [anime.name], right, one that sets the stage for the rest? But the timing isn’t right." 
        "Yukari thinks back to her work on the storyboards and nods." 
        y "I had some trouble with the directions for this part." 
        s "The backgrounds shift a lot during the chase, so getting the timing right is tricky." 
        yuu "And that’s not the only problem. " 
        "She taps one of the files." 
        yuu "Notice anything in the background in this key frame?" 
        s "You mean the crowd Itaru runs through?" 
        yuu "Their faces barely have any detail. I know it’s less expensive to handle it this way…" 
        show yukari sad
        y "…but it might make people think [anime.name] is poor quality. You’re right, we shouldn’t leave it like that." 
    elif anime.category == Anime.MYSTERY: 
        yuu "Look at the frames when Hideaki investigates the crime scene." 
        y "It looks fine to me." 
        s "Me too." 
        yuu "Oh…" 
        "For a moment, Yukari doesn’t think she’s going to say anything more, but then she abruptly shakes her head." 
        show yuuko sad_angry
        yuu "No, we can’t leave it like this. Don’t look at the crime scene itself, look at Hideaki. His model here isn’t consistent with his usual design." 
        show yukari surprised
        y "Oh! Now I see it!" 
        s "What can we do about it? Let the animation director know there’s a problem?" 
        show yuuko
        show yukari
        yuu "Actually, he said it’s fine for us to begin work on the key frames ourselves. I think we should be able to fix this up." 
        y "I’ll get my copy of the storyboards. Let’s do this!" 
        "With Yukari’s guidance, Yuuko and Sumiko start their work with enthusiasm, but it soon becomes clear it isn’t a simple task to complete in a few hours."
        "Although the problems seemed minor at first, the crude animations show up throughout the key frames." 
        "By the time they usually finish up for the day, the task is far from complete."
    show sumiko
    show yukari
    show yuuko
    s "Well… I guess we’ll work more on this tomorrow?" 
    yuu "Do we have that much time to spare, Yukari?" 
    show yukari sad
    "Yukari thinks it through and winces." 
    y "Well… no. If we have to fix up the key frames like this, I’m not sure we can keep [anime.name] on schedule." 
    if anim_studio == anim_studio_cheap:
        y "The director also said his animation team is too small to complete the remaining work." 
        show sumiko surprised
        s "Huh?!" 
        y "He said either you two will have to take on a lot of the work, or we’ll need to handle freelancers to help out." 
    show sumiko worry
    s "Then what are we going to do?" 
    yuu "Let’s work on the key frames tonight."
    show yukari surprised 
    y "Tonight?" 
    yuu "We don’t want to miss our deadline. If that means we have to work overtime, then we should." 
    show yukari
    show sumiko
    "Her confident tone impresses Yukari. She didn’t expect Yuuko to take charge." 
    s "If we’re staying here, I’ll go out and get us some dinner." 
    y "Good idea. It could be a long night." 
    yuu "You don’t have to stay, Yukari. It’s really just the two of us who need to work overtime." 
    y "Nah, it’s fine. I’m the director. It’s my responsibility to be here!"
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    with dissolve
    m "What are you three talking about?" 
    yuu "We’re staying at the studio to work overtime tonight." 
    show mayumi laugh_eyes_closed
    m "Oh? Count me in!" 
    y "You too?" 
    m "I have a lot of work to do on the OST." 
    s "All right, I’ll get dinner for four. What about Shunsuke? Is he staying?"
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    with dissolve
    ss "Staying where?" 
    y "We’re going to work overtime tonight."
    show shunsuke sad
    ss "Oh… Actually, I can’t. I found a great opportunity to give [anime.name] a little publicity."
    ss " There’s a small anime convention taking place from now until Thursday. Nothing big, but it will help get our name out there." 
    s "Why do you sound disappointed?" 
    ss "It makes me feel guilty if everyone’s working tonight except me."
    show yukari sigh
    y "Don’t feel guilty. After all, you’re still putting in extra time for [anime.name], even if it’s not at the studio!" 
    show shunsuke laugh_eyes_closed
    show yukari
    ss "Haha, good point. See you tomorrow. Good luck!" 
    scene studio_main_night with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    m "*yawns*" 
    "Mayumi yawns several more times, until Yukari looks over at her. Meanwhile, Sumiko and Yuuko continue working on the key frames and don’t seem to notice Mayumi at all." 
    show yukari laugh_eyes_closed
    y "Feeling sleepy already? Why don't you take a break?" 
    show mayumi_f happy
    m "Okay. Want to hear some of the music I made for [anime.name]?" 
    y "Finally. I was wondering when you’d let me hear them." 
    m "I’ve composed a few pieces so far with advice from Shunsuke. Here are the ones that are ready." 
    if anime.category == Anime.HAREM: 
        play music "music/anime/Harem/Harem Shenanigans Sample.ogg" fadein 1.0 noloop
        m "This is Natsume’s theme."
        pause 5.0
        y "I like it. It fits the character well." 
        m "Thanks! And now, let’s listen to Kiko’s theme."
        play music "music/anime/Harem/Calm Happy Music Sample.ogg" fadein 1.0 noloop
        pause 5.0
        y "Very good." 
        m "There will be variations on their themes for other scenes, but those are the basic versions." 
        y "Awesome!" 
    elif anime.category == Anime.ACTION:
        m "Let’s start with something ominous." 
        play music "music/anime/Action/Sinister and Mysterious but not that Sinister sample.ogg" fadein 1.0 noloop
        pause 5.0
        y "Definitely ominous. When will that play?" 
        m "It’s sort of the leitmotif for the conspiracy overall." 
        y "I think it fits them well."
        play music "music/anime/Action/Very Sinister sample.ogg" fadein 1.0 noloop
        m "Then there’s Norio’s theme."
        pause 5.0
        y "The whole soundtrack is ominous, isn’t it?" 
        y "I love it, though. This will be a great soundtrack!" 
    elif anime.category == Anime.MYSTERY: 
        m "Here we go."
        play music "music/anime/Mystery/Uneasiness or Investiogation Sample.ogg" fadein 1.0 noloop
        pause 5.0
        show yukari surprised
        y "Creepy!" 
        m "We’re going to use that one during Hideaki’s flashbacks. Here’s the music for when he’s investigating the current crime scene." 
        show yukari laugh_eyes_closed
        play music "music/anime/Mystery/Investigation Sample.ogg" fadein 1.0 noloop
        pause 5.0
        y "Not bad, not bad at all."
        m "[anime.name] has a difficult tone to capture, but I think I can do it." 
        y "From what I’ve heard so far, you definitely can." 
        m "Thanks!" 
    show mayumi_f worry
    show yukari
    "She suddenly lowers her voice."
    m "Oops, maybe we shouldn’t play music while Sumiko and Yuuko are trying to work." 
    "Yukari glances over, but the two artists are still hard at work. Neither of them gives any indication they heard the music. She nudges Mayumi and points at them." 
    y "I don’t think we disturbed them." 
    show mayumi_f
    m "Wow…"
    y "I’m not surprised. They're so focused, they didn’t even hear you yawning."
    show mayumi_f sigh
    m "Haha, come on, was my yawning that loud?"
    show yukari sigh
    y "Loud enough to distract me!"
    show yukari
    show mayumi_f
    "They watch the sisters a moment longer, and Yukari sighs. She appreciates their dedication to [anime.name], but she can’t help but feel guilty."
    "If her mistake hadn’t set them behind schedule, they wouldn’t need to work so late." 
    m "We’ll need to wrap things up soon, or we’ll miss the last train." 
    y "Should I let them know?" 
    m "Let’s let them work a little longer." 
    y "All right. I have a few remaining tasks to clear up before we head home." 
    "It’s the first long day, but Yukari suspects it won’t be the last if they’re to keep [anime.name] on track."
    "She only hopes they can maintain this pace and get everything done this week. If they have to work overtime too many nights, it could burn them out." 

label week_8_2:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    play music happy_music fadeout 2.0 fadein 2.0
    "The next morning, everyone gets to work right away. The future of [anime.name] hangs in the balance, and they can’t afford to waste any time." 
    ss "Yukari, I was looking at the storyboards for the second episode, and I’m confused about its direction." 
    y "What do you mean?" 
    "He walks to her desk, storyboards in hand, and sets them down." 
    ss "I don't get the flow of events in this section. How are they linked to each other?" 
    if anime.category == Anime.HAREM:
        y "Oh, this part is a montage, not a single scene. That’s why it doesn’t seem like they’re linked together at all." 
        ss "I suppose that also explains the lack of dialogue." 
        y "Exactly. With two episodes, we don’t have a lot of room for a plot arc, but a montage of school events should help." 
        ss "True, but it feels abrupt." 
        y "Hmm, let’s try to smooth it out a little." 
    elif anime.category == Anime.ACTION:
        show yukari worry 
        y "Uh…" 
        ss "Yes?"
        y "This is a fight scene, but I’m not sure why there are so many cuts."
        show shunsuke sigh
        ss "Didn’t you make it?" 
        y "Yes, but now that I look at it again, I think the early part of the fight should be handled in a single cut."
        y "Give me the storyboards. I’ll take care of it." 
    elif anime.category == Anime.MYSTERY: 
        y "This is when Hideaki finally ties the old crime to the new one. The scene is jumping back and forth between the two crime scenes to show the connections."
        show shunsuke sigh 
        ss "It’s too confusing like this. The audience won’t follow the connections." 
        y "Hmm, maybe we need to reposition some of the cels…" 
        ss "Narration might also help."
    show shunsuke
    show yukari
    "Yukari and Shunsuke spend the rest of the day fixing up the storyboards."
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    ss "Well, I’m off to the convention again. It went really well yesterday. I think I won us some fans. You can still buy tickets, if anyone wants to come."  
    m "I’d like to finish this composition."
    show yukari laugh_eyes_closed
    y "I’m staying, too. See you tomorrow, Shunsuke!" 
    scene studio_main_night with fade
    show yukari at left
    with dissolve
    "While the others work on their tasks, Yukari goes through the schedule for [anime.name]. At last, she lets out a dismayed sigh and rubs her head."
    "Even with their overtime work factored in, it doesn’t look like they’ll get everything done in time." 
    if anim_studio == anim_studio_expensive:
        "The animation studio has increased its pace, but they still need to do an extensive amount of work. They might need to call in outside help." 
        "Yukari sends a quick email to [anim_studio_dir], asking for advice."
        "To her relief, he responds within minutes and says they can delegate smaller tasks to freelance animators if that’s their preference." 
    elif anim_studio == anim_studio_cheap:
        "The director was right. If the sisters do all this work alone, they’ll burn out. They need to delegate some of the work to freelance animators."
    show mayumi_f at right with dissolve
    y "Mayumi, do you have a minute?" 
    "She keeps her voice low, although the two artists are once again so intent on their work, they might not hear if she shouted."
    m "What’s up?" 
    y "I’ve gone over the schedule, and I think we need to hire freelance animators to finish on time."
    y "I might be able to find some through my network, but do you have any other ideas?" 
    m "A lot of freelancers check online job boards. I can post there, if you like." 
    y "That sounds great." 
    "The two of them search for freelance animators until it’s once again time to catch the train and go home." 
    $rd_e_holder.emptyList(rd_e_holder.wk_5_to_7)
    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_6
label week_8_3:
    $nextDay()
    scene studio with fade
    show yukari sigh at pos_left
    show sumiko at pos_right
    show yuuko sigh at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "*yawn*"
    yuu "*yawn*"
    show shunsuke sad_angry
    ss "You guys are making me feel guilty."
    show mayumi laugh_eyes_closed
    show yukari
    show yuuko
    m "It’s okay. Working in the studio at night is actually a lot of fun!"
    show shunsuke sigh
    ss "Now I feel left out. However, the convention reminded me that we should talk about marketing." 
    show shunsuke
    #If (guerilla marketing) back in Week 2 and has a good marketing stat
    if guerilla_marketing and anime.marketing >= WEEK_8_GOOD_MARKETING_VALUE:
        ss "Our pre-release marketing efforts are going well. We already have several followers on social media."
        ss "Better yet, I saw people discussing [anime.name] on an anime forum."
        show mayumi surprised
        m "Wow, really?" 
        show yukari happy
        y "Awesome!"
        ss "But guerilla marketing alone won’t be enough." 
    elif investor_marketing and anime.marketing >= WEEK_8_GOOD_MARKETING_VALUE:
        #If the player chose to start  marketing due to Investor Advice in Week 6 and has a good marketing stat, 
        ss "Now, I’ve started several online ad campaigns."
        ss "It will be difficult to judge their effectiveness so early, but I’ve tracked their stats and they seem to have good visibility."
        show sumiko laugh_eyes_closed 
        s "For what it’s worth, some of my friends told me they’re excited for [anime.name]."
        show yukari happy 
        y "That’s good!" 
        ss "However, we still can do more." 
    elif (investor_marketing or guerilla_marketing) and anime.marketing <= WEEK_8_GOOD_MARKETING_VALUE:
        show shunsuke sigh
        ss "Honestly, our promotion efforts are not going well." 
        y "Oh…" 
        ss "We really need to step up our game if we want to get [anime.name] the attention it deserves." 
    elif not investor_marketing and not guerilla_marketing:
        "If the player declined marketing both times," 
        show shunsuke worry
        ss "We should start promoting [anime.name] now, since there's only a little time left before it will be on the air." 
        ss "Producing a great anime series is only half the battle. The other half relies on marketing."
        show sumiko surprised 
        s "What do you mean? If [anime.name] is awesome, shouldn’t the fans come naturally?"
        ss "And how will they know [anime.name] is awesome if they don't even know it exists?" 
        y "Shunsuke's right. We need to put some thought into marketing." 
    "Yukari thinks about different advertising techniques. What would help them the most?" 
    y "Ads on TV and the Internet are quite effective. They got me to try different kinds of anime I wouldn’t have watched otherwise!"
    show mayumi happy 
    m "Don't forget about posters and banners, too! I see lots of them in Akihabara. Why don’t we try renting some advertisement space there?" 
    show shunsuke sigh
    ss "Are you joking? We don't have that kind of budget!" 
    if not guerilla_marketing:
        ss "Right now, we should try some guerilla marketing."
        show sumiko surprised
        s "Guerilla marketing? But we're not in a war." 
        "For a long moment, Shunsuke just stares at her. Then he shakes his head." 
        ss "Didn’t I explain this once already?"
        show sumiko
        ss "Guerilla marketing is when you use unconventional methods to market something to achieve the highest possible gains with the lowest possible costs." 
        ss "To put it in simple terms, we’ll use creative methods to get as many fans as we can for [anime.name]." 
        m "Like going viral on social networks, right?"
        show shunsuke happy
        ss "Exactly!" 
        s "But how?" 
        y "We can’t expect to go viral right away, but we should probably set up social media accounts for [anime.name]." 
        m "Sounds good to me, but who should handle it?" 
        s "Shunsuke, definitely. He’s the closest thing we have to a marketing expert." 
        ss "Thanks, I think. I’ll create the accounts today." 
        "It’s the most sensible choice, not only because of Shunsuke’s experience, but also because he has the fewest remaining tasks of anyone on the team." 
        ss "However, [anime.name] should have its own website." 
    else:
        ss "What we really need is to give [anime.name] its own website."
    show yukari worry
    show shunsuke
    y "Will that be difficult?" 
    ss "Not necessarily. We’ll need to pay for our domain name and hosting, but I dabbled in web development a few years ago, so I might be able to set it up." 
    show yukari laugh_eyes_closed
    y "Wow, you’re really resourceful!" 
    "She looks around at the others and realizes Yuuko has been even quieter than usual during the conversation, still focused on her work." 
    show yukari
    y "Yuuko? What do you think about Shunsuke’s idea?"
    yuu "Hmm? Oh, whatever everyone else thinks is fine with me…"
    show sumiko sigh
    s "You weren’t listening at all, were you?"
    show yuuko sad
    yuu "Sorry. I have so much work to do, I didn’t want to take a break. I’m going to work on [anime.name] as much as possible today." 
    y "All right, just don’t burn yourself out. Rest if you need to." 
    show yuuko
    yuu "I will." 
    scene studio
    show yukari at left
    with dissolve
    "What should Yukari focus on today?"
    if anim_studio == anim_studio_cheap:
        menu:
            "Visit [anim_studio]":
                $week_8_cheap_studio_visited = True
                $choice_8_1_1_cheap()
                "Yukari decides to pay a visit to [anim_studio]. With the studio’s reputation in mind, she has a bad feeling things might not be going exactly as planned." 
                scene animation_studio with fade
                show yukari at left with dissolve
                "The empty lobby is a familiar sight at this point." 
                y "Hello? [anim_studio_dir], are you here?" 
                show anim_dir at right with dissolve
                anim_dir "Yukari? What brings you here today?" 
                y "I came to check on the new background art for episode one of [anime.name]." 
                anim_dir "Background art? Sure, please hold on while I get the files from our staff." 
                play sound [sfx_anim_d_open,sfx_anim_d_close]
                hide anim_dir with dissolve
                "Yukari sits down and waits for him to return. A minute passes… then another."
                "After a few minutes, she gets a little impatient. What could be taking him so long?" 
                "By the time ten minutes have passed and the director still hasn’t returned, she decides to take matters into her own hands."
                "As she approaches the door, muffled voices come from the other side of the wall. Although she can’t make out the words, it sounds like it might be an argument." 
                show yukari worry
                "She hesitates. Eavesdropping isn’t polite."
                show yukari
                "On the other hand, it could be about [anime.name]. Yukari leans closer and presses her ear against the door, but she still can’t hear the conversation." 
                "The sudden sound of approaching footsteps makes her hurry back to her seat."
                show anim_dir at right with dissolve
                anim_dir "Sorry for the delay. Here's the new background art we’ve been working on this week." 
                "His tense posture sends off more warning bells in Yukari’s mind. Nevertheless, she accepts the art from him and looks through it."
                "Soon, the reason for his anxiety becomes clear." 
                show yukari worry
                y "Why is the quality of the art so inconsistent?"
                show anim_dir frustrated
                anim_dir "One of the team people working on it is new. I should have delegated a senior staff member to oversee his work, but I thought he would be fine."
                anim_dir "I’m sorry, it was my mistake."
                show anim_dir smile 
                anim_dir "We’ll try to fix the problem as fast as we can!"
                show yukari sigh
                "Yukari now has a pretty good idea of how the quality of Kogu Studio’s last anime declined. They appear to be repeating the same disaster. Didn’t they learn?" 
                "She sighs, but as much as she’d like to blame [anim_studio_dir], she knows she’s responsible."
                "After all, she chose [anim_studio] to cut costs, well aware of the risks." 
                y "(thinking to self) At least I spotted the problem before it got out of hand."  
            "Storyboards":
                $choice_8_1_2_cheap()
                "The storyboards for the second episode could still use some work."
                "Yukari goes through them to fix the remaining problems they discussed the other day and add more directions to make sure the flow is as clear as possible."
                "From [anim_studio]’s reputation, they need as much guidance as they can get." 
            "Marketing": 
                $choice_8_1_3_cheap()
                "Shunsuke’s words about marketing leave Yukari inspired to help." 
                "While full-scale ads in Akihabara like Mayumi mentioned are out of the question, maybe they could run some smaller advertisements, especially since they cut costs by working with [anim_studio]."
                "Yukari does some research and takes notes on ideas that might be within their budget."
    elif anim_studio == anim_studio_expensive:
        menu:
            "Marketing":
                $choice_8_1_1_expensive()
                "Shunsuke’s words about marketing leave Yukari inspired to help."
                "While full-scale ads in Akihabara like Mayumi mentioned are out of the question, maybe they could run some smaller advertisements, despite the expense of working with [anim_studio]."
                "Yukari does some research and takes notes on ideas that might be within their budget."
            "Storyboards":
                $choice_8_1_2_expensive()
                "The storyboards for the second episode could still use some work."
                "Yukari goes through them to fix the remaining problems they discussed the other day and add more directions to make sure the flow is as clear as possible."
                "After all, [anim_studio_dir] likes to see them do a solid, professional job."
            "Raise funds":
                $choice_8_1_3_expensive()
                "Funds are an ever-present source of concern, especially due to [anim_studio]’s costs."
                "Yukari searches online and finds a new initiative aimed at helping new artists begin their careers."
                "It isn’t clear if the organization includes anime studios in that category, but Yukari fills out the application to find out."

    scene studio_main with fade
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke_f at left
    with dissolve
    "In the afternoon, Yukari returns to the hunt for freelance animators. So far, she’s turned up nothing."
    "The lack of progress is decidedly frustrating."
    ss "Are you staying late again?"
    show sumiko laugh_eyes_closed
    s "Not today." 
    "Yuuko looks up." 
    show yuuko surprised
    yuu "We aren’t?"
    show sumiko sigh
    s "You’ve done nothing but work all day long. You’re going to get sick if you keep this up, or have a nervous breakdown or something!" 
    show yuuko worry
    yuu "But…"
    ss "Sumiko’s right. Think of it this way, Yuuko. If you get more rest, you’ll feel refreshed and be able to work as long as you need tomorrow night!" 
    show yuuko
    yuu "All right." 
    "For the first time all week, everyone leaves the studio at the usual time." 

label week_8_4:
    $nextDay()
    scene studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    play music restaurant_music fadeout 2.0 fadein 2.0
    "Yukari paces back and forth in the studio. It’s almost time for the second recording session with the voice actors." 
    y "So, Mayumi, you’re sure you don’t want to come?"
    show mayumi_f sigh
    m "Sorry, but I really need to compose the music for [anime.name]." 
    y "Okay…" 
    "She looks around the studio."
    show mayumi_f at pos_outerright
    show shunsuke at pos_middleright_half
    with dissolve
    y "Hey, Shunsuke—" 
    show shunsuke sad_angry
    ss "Even if I wasn’t busy with marketing and PR today, how could I help? I know next to nothing about recording."
    show yukari sad 
    y "Good point, I guess…" 
    m "Before you go, Yukari, I almost forgot to tell you something." 
    "Her heart sinks." 
    show yukari surprised
    y "What is it?" 
    m "I hired voice actors for the remaining characters. They’ll join you in the studio later today." 
    y "What?!" 
    show mayumi_f laugh_eyes_closed
    m "Don’t worry. They don’t have as many lines as the others, so they don’t need to be there for as many sessions." 
    y "But I’ve never met them! Are you sure you don’t want to be there for this?"
    show mayumi_f sigh 
    m "Stop panicking. You’ll be fine. What’s the worst that could happen?"
    show yukari
    "Yukari doesn’t even want to think about that. She forces a smile and nervously leaves the studio."
    scene recording_studio with fade
    show yukari at left
    show va_dir at right
    with dissolve
    "When Yukari walks through the door, the main three voice actors are already assembled." 
    y "Sorry I’m late." 
    va_dir "Don’t worry. You’re not late, they’re early." 
    if anime.category == Anime.HAREM:
        scene recording_studio
        show yukari at left
        show va_a happy at va_pos_a
        show va_b at va_pos_b
        show va_sakura at va_pos_c
        with dissolve
        va_a_char "We thought we’d get in a little extra practice." 
        va_c_char "Are these the lines we’ll be recording today?" 
        "She holds out her script for Yukari to see. Yukari swallows nervously."
        show yukari worry
        "If that’s what they want to record, maybe she should let them… no, Mayumi made it clear that they should focus first on the scenes where only their three characters appear."
        show yukari 
        y "A-actually, no." 
        "She turns to a different part of the script." 
        y "These lines." 
        show va_sakura sad
        va_c_char "Oh…" 
        show va_b angry
        va_b_char "I told you so..." 
        show va_a
        va_a_char "At least we got to practice our characters’ voices more, even if they were the wrong lines for today’s session." 
    elif anime.category == Anime.ACTION:
        scene recording_studio
        show yukari at left
        show va_a at va_pos_a
        show va_b at va_pos_b
        show va_c sad at va_pos_c
        with dissolve
        va_c_char "You appear distressed." 
        "Yukari takes a deep breath and tells herself he isn’t glaring at her, it’s just how [va_c] is." 
        y "N-no, I’m a little nervous without Mayumi here, that’s all." 
        va_b_char "You’ll be fine." 
        "The sharp look she throws in [va_b]’s direction, however, is definitely a glare."
        show va_c surprised 
        va_c_char "What did I do?" 
        show va_b angry
        va_b_char "Tried to scare Yukari."
        va_c_char "Nonsense! Look at her, she’s fine. Aren’t you?" 
        show yukari surprised
        "Yukari jumps."
        show yukari sigh
        y "Yes, I’m fine. Fine! Perfectly fine."
        show va_a laugh_eyes_closed 
        va_a_char "Don’t worry, [va_c] doesn’t bite." 
    elif anime.category == Anime.MYSTERY:
        scene recording_studio
        show yukari at left
        show va_a laugh_eyes_closed at va_pos_c
        show va_b at va_pos_a
        show va_c at va_pos_b
        with dissolve
        va_a_char "The early detective catches the clue!" 
        show va_b laugh_eyes_closed
        va_b_char "Ooh, I like that one! I’ll have to start using it." 
        "Yukari can’t help but wonder how often the opportunity to use such a phrase comes up in her life." 
        show va_a
        va_a_char "Are you ready, Megumi?!"
        show va_b happy
        va_b_char  "I’m ready, Hideaki!" 
        "While they have an excited, in-character conversation, [va_c] walks up to Yukari." 
        hide va_a
        hide va_b
        show va_c at right
        with dissolve
        va_c_char "Are you okay? You look a little pale." 
        y "I’ll be all right." 
        "She takes a deep breath to steady herself and hopes that wasn’t a lie."
        hide va_c
    hide yukari
    show va_dir_f at left
    with dissolve
    va_dir "All right, let’s get started." 
    "Once Yukari double-checks that everyone knows which lines they’re going to record, she starts the recording session." 
    "As they read their lines, she follows along with the script." 
    if anime.category == Anime.HAREM:
        scene recording_studio
        show va_a_f angry at left
        show va_b at va_pos_b
        show va_sakura at va_pos_c
        with dissolve
        va_a_char "You can’t do things like that!" 
        va_c_char "According to my latest, hypothesis, I can." 
        show va_a_f
        va_a_char "No, I mean it just isn’t done."
        show va_b surprised
        va_b_char "Is something wrong?"
        show va_sakura sad
        va_c_char "Yes—Keiji is trying to halt the advance of science!"
        show va_b
        show va_a_f angry
        va_a_char "Yes—Kiko is conducting an unauthorized experiment in the basement!" 
        y "Hey, um, can we stop for a minute? Cut?"
        va_dir "Cut!" 
        show va_sakura
        show va_a_f
        show va_b
        "Everyone looks toward Yukari expectantly." 
        y "Sorry. It’s just that those two lines are supposed to be in unison. Could we… try it again?" 
        va_dir "Of course." 
    elif anime.category == Anime.ACTION:
        scene recording_studio
        show va_a_f at left
        show va_b at va_pos_c
        show va_c at va_pos_b
        with dissolve
        va_b_char "Itaru?" 
        show va_a_f angry
        va_a_char "G-go away, Chie! I’m busy!" 
        show va_b sad
        va_b_char "Don’t worry, this won’t take long. I just wanted to tell you that—agh!" 
        va_c_char "You might as well join us, Miss Chie." 
        show va_b surprised
        va_b_char "Y-you’re the man from the other day." 
        va_c_char "Correct. My name is Norio. Please, sit down." 
        show va_b
        va_b_char "O-okay…" 
        show va_a_f
        va_a_char "I told you to go away. Why didn’t you listen?" 
        "Yukari opens her mouth, but she finds she’s too nervous to interrupt them. At last, she raises her hand. Everyone stops and looks at her." 
        y "Sorry. I just wanted to say something to [va_a]." 
        va_a_char "What is it?" 
        y "W-well, when Itaru yells at Chie, he’s supposed to sound annoyed, but also upset and worried. After all, her life is in danger."
        y "You sounded more like she was bothering him." 
        va_a_char "Oh, okay. Let me try that line again." 
    elif anime.category == Anime.MYSTERY: 
        scene recording_studio
        show va_c_f angry at left
        show va_b at va_pos_b
        show va_a at va_pos_c
        with dissolve
        va_c_char "I demand to know why you called me here!" 
        show va_a angry
        va_a_char "Very well then, my friend, I’ll tell you. I called you here because every piece of evidence at this crime scene points to one culprit… you, Shin!" 
        va_c_char "How dare you?! You aren’t even a proper detective!" 
        show va_b angry
        va_b_char "Hey, that’s not a nice thing to say!" 
        show va_c_f
        va_c_char "Nice? After he accused me of murder?" 
        show va_b
        va_b_char "Like it or not, he’s a detective." 
        va_c_char "Hah! He’s a fraud, a phony! An arrogant rookie who thought he could do nothing wrong. How’d that go for you, rookie? Ready to make another false accusation?" 
        va_a_char "I’ve gone over this evidence a thousand times. There is no doubt in my mind—you are the murderer!" 
        y "Cut?" 
        "When no one hears her, she raises her voice." 
        y "Cut!" 
        show va_a
        show va_b
        show va_c_f
        va_dir "Is something wrong?" 
        y "Not wrong, exactly, but… [va_a], I know you’re very enthusiastic, but you sound too confident."
        y "Shin’s jab is going to make Hideaki worried, even if he says he has no doubts." 
        va_b "I agree! You should sound a little more shaken when you reply." 
    "It takes a few attempts, but at last they record the lines the way they’re supposed to sound in the episode."
    "They work a little longer, and then they take a break."
    scene recording_studio
    show yukari at left
    show va_dir at right
    with dissolve
    va_dir "Once the other voice actors get here, we’ll continue." 
    "Yukari paces back and forth, not quite as nervous as before. That didn’t go too bad."
    "When she raised her objection, they listened to what she had to say. As long as she doesn’t overlook anything obvious, maybe she can handle this without Mayumi after all." 
    if anime.category == anime.HAREM:
        hide va_dir
        show va_a at right
        with dissolve
        va_a_char "So is this your first anime?" 
        y "Yes. I just graduated from high school, actually."
        show va_a laugh_eyes_closed 
        va_a_char "Wow, cool! I wondered, since you look even younger than me and I’m new at this." 
        y "Directing an anime has been a dream of mine for years." 
        va_a_char "That’s how I felt about voice acting."
        show yukari happy
        y "Really? How did you get interested in it?" 
        show va_a
        va_a_char "As a kid, I used to watch a lot of anime and wonder about the actors. Then my mother won a contest to appear on a radio show, and she took me with her."
        va_a_char "The voice actor of one of my favorite characters was on the show too, so I got to meet him. Ever since then, I wanted to do it too." 
        y "And now you are!" 
        va_a_char "Yeah! Sometimes I worry I’ll wake up and find out it’s all been a dream." 
        show yukari
        y "I know that feeling." 
        show va_a
        va_a_char "Don’t worry. Unless you’re a part of my dream, I promise you’re awake." 
        y "What if you’re part of my dream?" 
        va_a_char "Then we’re both in trouble." 
    elif anime.category == anime.ACTION:
        hide va_dir
        show va_c at right
        with dissolve
        va_c_char "Excuse me." 
        show yukari surprised
        y "Y-yes?"
        show va_c sad
        va_c_char "I really don’t mean to make you nervous." 
        show yukari
        y "O-oh, that’s quite all right! What can I help you with?" 
        va_c_char "I wanted to apologize if I startled you earlier."
        show yukari sigh
        y "So you… scared me in order to say you’re sorry for scaring me?" 
        va_c_char "Indeed. Perhaps it was a mistake." 
        show yukari
        y "No, it’s okay, really. I appreciate the thought." 
        va_c_char "I’m used to unintentionally scaring people, although at times I try to tone it down." 
        y "At times? Does that mean sometimes you play it up instead?" 
        va_c_char "It can be useful. If you ever need seats at a crowded theater, for example, come to me. I can get empty seats around me for rows and rows, even if the rest of the place is jammed." 
        "In spite of her nervousness, Yukari laughs. Maybe he’s not such a bad guy after all." 
        y "I’ll keep that in mind." 
    elif anime.category == anime.MYSTERY:
        hide va_dir
        show va_b at right
        with dissolve
        va_b_char "You look like you’re deep in thought." 
        y "Just making sure I didn’t miss any major mistakes during the recording." 
        show va_b sad
        va_b_char "Don’t you have faith in us?"
        show yukari sigh
        y "No, it’s nothing about you! I’m just really new at this, and I worry about messing up."
        show va_b 
        va_b_char "Why don’t you try practicing?" 
        y "How…?" 
        show yukari
        "She can’t help but remember [va_b] saying she prepared for her part by recreating a fictional crime scene so well, the police came." 
        va_b_char "Imagine the worst that could happen and address it out loud. You could even ask your friends to pretend to be us and make mistakes so you can practice correcting them." 
        show yukari happy
        y "Hey… that’s not a bad idea. Thanks!" 
        va_b_char "Any time. You might not believe this, but I get really nervous, too." 
        y "You do? But you seem so relaxed." 
        va_b_char "That’s because I practice handling situations that make me nervous. Since I’m prepared for them, it doesn’t bother me as much." 
        y "I’ll give it a try sometime." 

    "Their conversation is cut off by the arrival of the other voice actors, who will play the remaining members of the cast and the side characters. Everyone seems excited to be a part of [anime.name]." 
    scene recording_studio
    show yukari at left
    show va_dir at right
    with dissolve
    va_dir "Now that everyone’s here, let’s get to work." 
    "Everyone returns to their positions. Despite new people being present, Yukari isn’t as tense anymore."
    "Not only is she more confident she can handle this, but the voice actors no longer seem like such an intimidating bunch. They’re regular people too, even if they’re playing characters in [anime.name]." 
    "She checks to make sure everyone knows what lines they’re reading, and then they resume recording." 
    if anime.category == anime.HAREM:
        scene recording_studio
        show va_a_f angry at left
        show va_b at right
        with dissolve
        va_a_char "We have to stop the experiment!"
        show va_b sad 
        va_b_char "Kiko won’t be happy with you. Are you sure?" 
        va_a_char "Happy or not, it has to be done."
        show va_b
        va_b_char "Fine. You sneak into the  basement while I keep watch." 
    elif anime.category == anime.ACTION:
        scene recording_studio
        show va_a_f surprised at left
        show va_b angry at right
        with dissolve
        va_a_char "Is he following us?" 
        va_b_char "I don’t know. Just keep running!" 
        show va_a_f sad
        va_a_char "We’ll never make it. They have resources like you can’t possibly imagine!" 
        va_b_char "I’m not about to give up and die. Keep running!" 
    elif anime.category == anime.MYSTERY: 
        scene recording_studio
        show va_a_f at left
        show va_b at right
        with dissolve
        va_b_char "What could it mean, Hideaki?" 
        va_a_char "It means we’ve been looking at this case wrong the entire time. There’s one important question we still haven’t asked: where did the murder take place?" 
        show va_b surprised
        va_b_char "What? But we know where it happened!" 
        va_a_char "No. We only know where the body was found—and where it APPEARS the murder happened." 
    "The recording continued through the most critical scenes, and Yukari smiled as they reached Shunsuke’s final twists." 
    "At last, they reach the end of the script."
    scene recording_studio
    show yukari at left
    show va_dir at right
    with dissolve
    va_dir "That’s it for today. Next Wednesday, we’ll record the OP and ED, but we’ve finished recording the lines for all the characters." 
    "Of course, she already knew the plot, but hearing the parts acted out makes the story feel more real."
    show yukari laugh_eyes_closed
    y "Great!" 
    va_dir "Would you like to go through the final lines to make sure there’s nothing that needs to be changed?"
    show yukari 
    y "Yes, thank you." 
    hide va_dir with dissolve
    "She sits down in the recording booth and listens to the recorded lines."
    "Happiness surges through her as she thinks about how close [anime.name] is to completion, but it gives way to slight uneasiness." 
    "The lines are good, but a few could be further improved. Although all the character voices are passable, a few still aren’t quite right."
    "Yukari listens to them one more time and tries to decide the best course of action." 
    menu: 
        "Ask for retakes":
            y "Excuse me." 
            show va_dir at right with dissolve
            va_dir "Yes?"
            show yukari worry
            y "Is it possible for us to redo some of these lines?" 
            va_dir "It will send us over the allotted time for this recording session, but we can do that if you think it’s important." 
            y "I do." 
            va_dir "All right." 
            show yukari
            "He gathers the voice actors back together, and Yukari points out the lines she wants re-recorded."
            "It takes a few tries, but finally all the lines for [anime.name] have been recorded to her satisfaction." 
            y "That should be everything." 
            "If success," 
            va_dir "Perfect. I wish you the best of luck with [anime.name]." 
            y "Is there an extra charge for going over our time?" 
            va_dir "No, don’t worry about it." 
            y "Are you sure?" 
            va_dir "I can tell you’re passionate about this project, and I want to see your team succeed. Consider it my contribution to the future of [anime.name]."
            show yukari happy 
            y "Wow, thanks!" 
            "If failure," 
            va_dir "Now, since you went over your time, there will be an additional fee."
            show yukari sad
            y "Oh. I understand." 
            "Even though she understands, the thought of their tiny budget shrinking even more makes her anxious. The new lines better be worth it. She can only pray she made the right decision." 
        "It's good enough":    
            show va_dir at right with dissolve
            y "Everything sounds fine." 
            va_dir "Excellent! Then I wish you the best of luck with [anime.name]." 
            "As Yukari leaves the studio, she hopes she did the right thing."
            "The voices in [anime.name] won’t all be perfect, but they’ll be good enough. It’s a fine job for a small team, and most people watching probably won’t be bothered by those few lines anyway." 
           
    scene studio_main with fade
    show yukari happy at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music casual_music fadeout 2.0 fadein 2.0
    y "I’m back!" 
    show mayumi laugh_eyes_closed
    m "How did everything go?" 
    y "Pretty good."
    "She quickly explains what happened at the recording studio."
    y "And how are things here?" 
    m "Good, and Sumiko came up with a great idea!" 
    y "What’s that?" 
    s "See, we really need to work overtime again to finish up these key frames."
    s "But why do it the way we have been, with a few hours here and there? Why don’t we have a sleepover?" 
    show yukari surprised
    y "You mean spend the whole night at the studio?!" 
    yuu "It will give us the time we need to finish our work." 
    show sumiko laugh_eyes_closed
    s "Plus it will be FUN. Sleepovers are supposed to be fun." 
    show mayumi happy
    m "What do you say, Yukari? Let’s do it!" 
    show yukari laugh_eyes_closed
    y "Well, if it’s for the sake of [anime.name], I suppose I can’t argue." 
    "Plus the thought of having a sleepover at the studio does sound fun." 
    show shunsuke sigh
    ss "Sure, have a sleepover when I can’t come." 
    s "Oh for—just skip the convention today! You went three out of the four nights, isn’t that enough?" 
    ss "There’s an important anime panel discussion today, and I want to be there." 
    m "Aw, well we’ll try not to have too much fun without you." 
    show sumiko tsundere
    s "Besides, you’ve been going to a convention while we’re all working overtime. You really don’t have room to complain!" 
    ss "Fair point." 
    y "Let’s go home and get whatever we need for the night and then meet back here." 
    scene studio_main_night with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    with dissolve
    s "I’ll get the popcorn going!" 
    "When Yukari told them to get whatever they needed, she was thinking pajamas, sleeping backs, and other necessities."
    "But while she, Mayumi, and Yuuko brought such things, Sumiko’s supplies for the night also included popcorn, soda, and a stack of movies."
    yuu "I’m not sure I can draw while eating popcorn…" 
    show sumiko tsundere
    s "Then eat it during your breaks!"
    show mayumi happy 
    m "I’ll take some! I can eat and compose music at the same time." 
    show sumiko
    s "That’s the spirit! What about you, Yukari?" 
    y "Oh, sure, I’ll have some popcorn." 
    "Her main goal for the night is to seek out freelance animators."
    "Regardless of what Sumiko thinks, this sleepover won’t be enough to put them completely back on schedule. Those freelancers will be vital." 
    "Still, it’s hard to feel too stressed with the sound of a popcorn maker in the background." 
    show sumiko laugh_eyes_closed
    s "Here’s yours, Yukari!" 
    y "Thanks." 
    s "Are you sure you don’t want any, Yuuko? I’ll set it here on the desk in case you change your mind."
    "While Yukari eats her popcorn, she resumes her search for freelancers. It’s easy to find potential candidates, but difficult to find ones willing to work on such short notice."
    "Most want to be contacted a few weeks ahead of time, rather than a few days. Those who are willing to do rush jobs charge higher fees for it."
    show yukari sigh 
    "With a sigh, she turns her attention to the revised key frames Sumiko and Yuuko already finished, to look them over one more time." 
    "As time goes on, the mood in the studio lightens."
    "Mayumi plays short pieces of music from [anime.name] as she works on composing more, and Sumiko starts one of the movies she brought on her computer with the volume turned down low."
    "They’re still working, but with the whole night ahead of them, they don’t have to work nonstop." 
    "Except Yuuko."
    scene studio_main_night
    show yukari at left
    show yuuko at right
    with dissolve
    y "Yuuko? You really should take a break sometime." 
    yuu "I know… I just want to make sure I get all of my work done." 
    show yukari sigh
    y "And if you’re overworked, you won’t do a good job. Come on, we have plenty of time." 
    yuu "If you say so." 
    show yukari
    "She sets aside her work and reaches for the popcorn her sister left her." 
    show yuuko tsundere
    yuu "But if this break costs us valuable time, I’ll blame it on you." 
    show yukari laugh_eyes_closed
    y "It’s a deal." 
    show yuuko
    scene studio_main_night
    show mayumi surprised at left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    with dissolve
    m "Sumiko! What kind of movie IS this?!" 
    show sumiko laugh_eyes_closed
    s "It’s a terrible movie. We’re going to watch it and think about how much better [anime.name] will be."
    show mayumi sad_angry 
    m "You must be joking. Come on, put something good in!" 
    s "No." 
    "She stands protectively in front of the computer with her arms outstretched to block Mayumi as she tries to get close enough to eject the disc."
    show yuuko sigh
    "Yuuko watches them struggle in front of the awful movie for a moment and then shakes her head."
    scene studio_main_night
    show yukari at left
    show yuuko at right
    with dissolve
    yuu "Do you ever look at our team and think “How in the world are these people ever going to make an anime?" 
    show yukari happy
    y "I don’t know, it seems to be working for us so far!" 
    show yuuko laugh_eyes_closed
    yuu "Haha, fair point." 
    "Mayumi and Sumiko eventually reach a compromise about what movie to watch."
    "Once it gets over, they return to work and continue in such a fashion until late at night, when they finally call it a day and go to sleep." 

label week_8_5:
    $nextDay()
    scene studio with fade
    show shunsuke_f at left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko   
    with dissolve
    ss "Good morning, everyone. How did last night’s activities go?" 
    show sumiko happy
    s "Perfect!" 
    yuu "We got a lot done. How was the convention?" 
    show shunsuke_f happy
    ss "It went well. A few people came up to me after the panel to talk about [anime.name]." 
    s "Really? Tell us everything!" 
    "As they exchange details about their latest progress, Yukari walks to Mayumi’s desk."
    scene studio_main with fade
    show yukari worry at left
    show mayumi_f at right
    with dissolve 
    y "Hey, have you found any freelance animators yet? I’m hitting a wall wherever I search." 
    show mayumi_f sad
    m "Same here." 
    y "I found a few candidates willing to start immediately, but they charge a high fee." 
    m "Why don’t we ask Sumiko or Yuuko? They might know artists who can help!" 
    "Yukari didn’t want to inconvenience the sisters by giving them even more work, after everything they’ve done already, but on the other hand hiring freelance animators will help reduce their workload, too." 
    show yukari sigh
    y "Guess we have no choice." 
    s "Did someone call for me? I heard my name."
    show sumiko at pos_middleright_half
    show mayumi_f
    with dissolve
    y "We need your help with something." 
    show sumiko surprised
    s "What is it?" 
    "Yukari hesitates."
    show sumiko tsundere
    s "Hello?" 
    y "Okay, we’re having trouble hiring freelance animators." 
    show sumiko
    "Yuuko looks up from her desk." 
    yuu "Freelance animators? I thought we were almost back on track."
    show yukari sigh
    y "That’s not exactly true. We’re getting back on schedule, but we can’t work fast enough to finish producing [anime.name] ourselves by our deadline, no matter what we do." 
    if anim_studio == anim_studio_cheap:
        y "As for [anim_studio], they don’t have enough animators to handle their end of the work, either, so we really need some freelancers." 
    elif anim_studio == anim_studio_expensive:
        y "I already spoke to the director of Asahi Studio about it."
    show sumiko worry 
    s "So what’s the problem?" 
    show yukari sad_angry
    y "Including this week, we only have 5 weeks left. That means we need to hire freelance animators on short notice, and most aren’t willing to do it." 
    show sumiko laugh_eyes_closed
    s "Don't worry! You came to the right person." 
    s "Have I told you about the art circle Yuuko and I belonged to in school? My friends have some experience with animation. I’m sure they’d do a great job!" 
    s "Should I get in touch with them?" 
    show yukari surprised
    y "Yes, please do."
    show mayumi_f happy
    show yukari
    m "Wow, that went better than I expected, but I’m not complaining!" 
    s "I’ll call them now." 
    scene studio_main
    show yukari at left
    with dissolve
    "She heads outside the studio to make the phone call. Mayumi and Yuuko return to their work, and Yukari paces while she waits to see how things turn out."
    show sumiko at right with dissolve
    "Sumiko returns within a few minutes."
    show yukari worry
    y "Well?" 
    show sumiko happy
    s "Good news! They’re available to start working anytime. See, you can count on me, hehe." 
    show yukari laugh_eyes_closed
    y "Wonderful, thank you!" 
    "[anime.name] might still be behind schedule, but they’re slowly handling every obstacle. The gloomy mood in the studio has almost vanished entirely." 
    "Yukari finishes up some of her work and jots down notes on what she needs to tell Sumiko’s friends, when her phone buzzes."
    "She checks it. It’s a text message from the director of [anim_studio] telling her their work is complete. Yukari crosses her fingers and heads over to the animation studio." 
    scene animation_studio with fade
    show yukari at left
    with dissolve
    if anim_studio == anim_studio_cheap and not week_8_cheap_studio_visited:
        "When she arrives, the director is waiting for her." 
        show anim_dir at right with dissolve
        anim_dir "I’m glad you could make it. Are you ready to take a look?" 
        y "Yes, and I wanted to let you know we’ve found some freelance animators to help." 
        anim_dir "Oh, thank goodness." 
        "Something in his tone sets off warning bells in Yukari’s mind, and when she takes a look at the art he shows her, she knows why he’s so happy to have more animators on the job."
        "The new art for the animations is wildly inconsistent." 
        show yukari sad_angry
        y "What happened?!" 
        show anim_dir frustrated
        anim_dir "Ah… sorry about that… you see, I put a new team member to work on it… I know I should have had someone more experienced oversee his work, but I thought he’d be fine." 
        "Yukari grits her teeth. This is probably why Kogu Studio’s last anime had such a decline in quality. She should have known better than to work with them, but no, she wanted to cut costs…"
        show yukari worry 
        y "We can’t leave it like this. What are we going to do?" 
        anim_dir "I’m afraid we don’t have enough time to change it now, unless you can change your schedule." 
        y "We can’t do that." 
        anim_dir "Then there’s nothing we can do."
        show yukari sad
        "Yukari stares at him. She feels like the floor is about to drop out from beneath her. She can’t deal with this alone. Maybe someone else has an idea." 
        y "Can I send pictures for my team to look at?" 
        anim_dir "Of course." 
        "She quickly emails everyone the latest art, along with a few sentences explaining her concerns about the quality and their problem with the schedule." 
        "Yuuko replies first saying that she can work all night again if it will help." 
        "Sumiko says it looks fine to her and they can’t afford to be crazy perfectionists." 
        "Mayumi tells her to relax and stop worrying so much, since the quality isn’t bad enough to ruin [anime.name]." 
        "Finally, Shunsuke replies."
        y "Who writes emails like this?!" 
        "His email is several paragraphs long and explains in detail how projects rarely go exactly the way they’re planned, and that they’re lucky [anime.name] has gone this well since it’s their first attempt to make an anime."
        "She skims his email to get the main points, and finally sighs." 
        "She looks at the director." 
        y "All right. We’ll continue as planned." 
        anim_dir "Okay. And I really am sorry about this." 
        y "It’s fine." 
        "It isn’t what she wants, but since the team is on board with it and their deadline can’t be changes, she’ll accept the art in its current state. At least [anime.name] still has a chance." 
    elif anim_studio == anim_studio_cheap and week_8_cheap_studio_visited:
        "To Yukari’s pleasant surprise, the work provided by [anim_studio] is satisfactory, with no issues or mistakes." 
        "It’s hard to believe [anime.name] has come so far in only two months. She has faith all their efforts will pay off soon, once [anime.name] is on the air." 
    scene street with fade
    show yukari at left with dissolve
    "Once she leaves the studio, she gets in touch with Sumiko’s friends. Like Sumiko promised, they’re ready to work on [anime.name] right away." 
    "It’s been a bumpy road, but at last everything is coming together."

    $random_game_event = rd_e_holder.random([rd_e_holder.all,rd_e_holder.wk_4_to_12,rd_e_holder.wk_5_to_10,rd_e_holder.wk_6_to_8])
    call expression random_game_event from _call_expression_7

    scene restaurant with fade   
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke laugh_eyes_closed at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    play music restaurant_music fadein 2.0 fadeout 2.0
    "Yukari is the last to arrive at the restaurant, but everyone greets her with happy greetings. It’s a welcome change from the previous Friday, when everyone was so quiet." 
    if not week_8_cheap_studio_visited:
        m "So did you get everything worked out at [anim_studio]?"
        show yukari sigh 
        y "Yeah. I wish we didn’t have to go with lower quality, but…" 
        m "It’ll be fine." 
    elif anim_studio == anim_studio_expensive or week_8_cheap_studio_visited:
        m "How did things go at [anim_studio]?" 
        show yukari laugh_eyes_closed
        y "Everything is on track." 
    show yukari happy
    y "I also got in touch with our new animators, and that went smoothly." 
    show sumiko tsundere
    s "See? You should have come to me from the start." 
    show mayumi laugh_eyes_closed
    m "Last week, everything seemed so hopeless, but now things are so much better!" 
    show sumiko
    ss "What about you, Mayumi? How is the soundtrack coming along?" 
    m "Pretty good, thanks. I’m starting to get the hang of this."
    show yuuko happy
    yuu "Do we get to hear them?" 
    m "Definitely. Actually, I was hoping I could get some feedback on the music next week." 
    s "Sweet." 
    y "And what have you been working on, Shunsuke? Everything going well?" 
    show sumiko tsundere
    s "It better be, since he’s the only one who didn’t work overtime." 
    show shunsuke sad_angry
    ss "Hey, I tried to stay, and you said I couldn’t!" 
    s "Details, details." 
    show sumiko
    show shunsuke
    ss "Anyway, I actually have some unexpected news."
    show yukari worry 
    y "Good news, I hope?" 
    show shunsuke laugh_eyes_closed
    ss "Very. A group of fans on social media are so pleased by what we’ve shown of [anime.name] so far, they sent us donations. This money should help take care of our recent expenses." 
    show yukari
    m "Wow, cool! I never thought you’d be this helpful." 
    show shunsuke tsundere
    ss "Excuse me?" 
    show sumiko laugh_eyes_closed
    s "Nice one, Mayumi." 
    show mayumi
    m "No, no, I didn’t mean it in a bad way! I just meant, you only joined us as a writer, so I figured you’d handle the writing and nothing else."
    "But you’ve actually helped in all sorts of ways. Now you’re even getting us donations!"
    show shunsuke 
    y "Maybe he should have been in charge of raising funds all this time." 
    "Shunsuke laughs and holds up his hands."
    ss "It’s nothing special. I just spend a lot of time on the Internet, so I know what fans want to see. I give them what they want, that’s all." 
    "Yukari stands up, and everyone looks at her." 
    show yukari laugh_eyes_closed
    y "Remember last week, when we toasted [anime.name]? This week, I think we ought to toast Shunsuke giving fans what they want." 
    ss "Oh no, you don’t have to—" 
    show sumiko happy
    s "Yeah!" 
    "She jumps to her feet as well." 
    s "To Shunsuke!" 
    everyone "To Shunsuke!" 

label week_8_6:
    $nextDay()
    scene home with fade
    show yukari at left with dissolve
    "Another weekend has arrived. What should Yukari do?"
    menu:
        "Review [anime.name]":
            $choicewe_8_1_1()
            "Yukari goes over everything they’ve completed for [anime.name] so far, from the animations to the voice acting."
            "She catches a few minor mistakes and a makes a note to fix them later, but overall everything looks good."
        "Hang out with the team":
            $choicewe_8_1_2()
            "Yukari calls up the team and invites them over for a picnic."
            "It’s like a more casual version of their restaurant meetings. They chat a little bit about [anime.name] and their upcoming plans, but for the most part they just hang out and have a good time."
        "Relax":
            $choicewe_8_1_3()
            "Yukari stays at home over the weekend to relax by reading some entertaining books and watching her favorite anime on TV."
            "It’s partly a personal celebration in honor of how far [anime.name] has come along."
    scene studio 
    $nextWeek()
    $shunsuke_tasks[0] = shunsuke_second_task
    $mayumi_tasks[0] = mayumi_fourth_task
    play music dashboard_music fadein 1.0 fadeout 1.0
    $renpy.retain_after_load()
    $UpdateProgressReport()
    $renpy.transition(dissolve)
    $in_gameplay_menu = True
    call screen start_game
    $in_gameplay_menu = False
    stop music fadeout 1.0
    $fastForwardDays(2)
    jump week_9_1

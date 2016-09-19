label week_5_1:
    scene studio with fade
    show yukari at pos_left
    show sumiko happy at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
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
    #adjust to night version
    scene home with fade
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
        "[anim_studio_expensive]":
            "Yukari decides to get in touch with [anim_studio_expensive]."
            "Working with a studio renowned for its production quality will help save them a lot more money in the long run."
            "They will have proper procedures and guidelines during the production process which will definitely be a great help to the inexperienced team."
            "Best of all, it will ensure [anime.name] has top-notch animation."
            $anim_studio = anim_studio_expensive
        "[anim_studio_cheap]":
            "Yukari decides to get in touch with [anim_studio_cheap]."
            "Despite the studio’s recent slump, her research suggests it’s only due to poor management. If she manages the team effectively, she’ll be able to turn things around for everyone."
            "The main selling point, of course, is the competitive price." 
            "[anim_studio_cheap]’s quality can be hit-and-miss, so Yukari will need to pay extra attention to them if she wants things to go smoothly."
            $anim_studio = anim_studio_cheap
label week_5_2:
    scene studio with fade 
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    ss "So which animation studio did you pick?"
    y "[anim_studio]. I'll be heading over there later with Mayumi for a consultation."
    #mayumi surprised
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
    #yukari surprised
    y "Agh! W-when did you get here? I thought I told you to wait!"
    m "You were acting weird, so I followed you."
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
    y "Very funny. Let’s go."
    scene animation_studio with fade
    if anim_studio == anim_studio_expensive:
        show yukari at left
        show mayumi_f at right
        with dissolve
        #surprised yukari
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
        #door sound
        scene animation_studio
        show yukari at pos_left
        show mayumi at pos_farleft behind yukari
        with dissolve
        staff "Hello! What brings you to [anim_studio_expensive] today?"
        #hardcoded spice and wolf inside
        staff "Oh! I see you’ve taken a liking to those Nendoroids. They’re from Spice and Wolf, which is our most popular anime series so far."
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
        #door sound
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
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
    "The next day, Yukari takes a look at the storyboards. They seem fine to her."
    y "Shunsuke, do you have a minute?"
    ss "Sure, what is it?"
    y "The director from [anim_studio] said I need to make the storyboards clearer. What do you think is wrong with them? "
    #cg storyboard
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

label week_5_4:
    $anim_studio = anim_studio_expensive
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
    if anim_studio == anim_studio_cheap:
        scene animation_studio with fade
        show yukari at left with dissolve
        "The reception desk is empty again when Yukari arrives, but before she can worry too much or consider calling out to see if anyone is around, the door opens and the director steps out."
        show anim_dir smile at right with dissolve
        anim_dir "Hello, Yukari! So, have you guys decided on who to work with to produce animation work for your team?"
        "It’s an unexpected question since Yukari never reached out to any other studios besides [anim_studio_cheap]. Then again, he’d have no way of knowing that."
        y "Yes, we’d like to work with [anim_studio_cheap]."
        anim_dir "Great! Just give me a moment while I have my assistant print out the contract for our work."
        #door sound
        hide anim_dir with dissolve
        "He disappears behind the door again. Yukari can hear faint voices, but they aren’t clear enough for her to make out the words."
        show yukari worry
        "A little nervous now that their partnership is about to become official, she paces back and forth in front of the reception desk."
        "Is [anim_studio_cheap] the right choice? Will she be able to make things work out?"
        y "(thinking to self): If something goes wrong, what am I supposed to do?"
        #door sound
        show anim_dir at right with dissolve 
        anim_dir "Sorry to keep you waiting. Here is the contract."
        "He hands the contract over to Yukari. She stares at it, overwhelmed."
        "She doesn’t know much about the legal side of things, but if she doesn’t look over the contract carefully, she could miss something that comes back to haunt them in the future."
        anim_dir "Just let me know when you’re ready."
        #door sound
        hide anim_dir with dissolve
        show yukari
        "As the director leaves, Yukari reads through the contract. After she goes through it once, she decides to call Mayumi. Her friend knows more about legal matters than she does."
        play sound "music/sfx/dialing_numbers.ogg"
        "Yukari gets out her phone and dials Mayumi’s number."
        m "Hello?"
        y "I’m at [anim_studio_cheap] now. Mind if I go over the contract with you?"
        m "Go ahead."
        "She reads the contact out loud, with particular attention to the sections she’s most unsure about. Mayumi explains them to her and points out one or two they might want to have changed."
        #surprised yukari
        y "Changed? Can you do that?"
        m "Of course. You’re negotiating!"
        "She carefully goes over what Yukari should say to the director."
        y "Thanks, Mayumi. You’re a life saver."
        m "Don’t mention it. Good luck!"
        "Yukari hangs up and approaches the door behind the reception desk. A little uncertain, she knocks."
        #door sound
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
        #door sound
        "Yukari clasps her hands in front of her and admires the Nendoroids Mayumi liked so much to calm her nerves. She only has to wait a minute."
        #door sound
        show anim_dir smile at right with dissolve
        anim_dir "Hello, Yukari! Well then, has your team decided upon a studio to work with for [anime.name]’s animation?"
        "It’s an unexpected question since Yukari never reached out to any other studios besides [anim_studio_expensive]. Then again, he’d have no way of knowing that."
        y "Yes, we’ve decided to work with [anim_studio_expensive]."
        anim_dir "I’m happy to hear that. If you’ll wait here a minute, I’ll get the contract for our work."
        hide anim_dir with dissolve
        # door sound
        "For the brief moment the door is open, Yukari hears faint voices, but once the door closes behind him, it’s as silent as when she and Mayumi first visited."
        "She can’t help but question her decision to work with [anim_studio_expensive]. High quality comes with a high price."
        "She definitely needs to make sure there aren’t extra revisions for the animation work, or they’ll be out on the streets in no time. Even the initial work will push the budget."
        #door sound
        show anim_dir smile at right with dissolve
        anim_dir "Sorry to keep you waiting. Here is the contract for our partnership."
        anim_dir "I recommend you take a good look at it, since you’re new to the anime business. You don’t want to miss critical details in the contract."
        "He hands over the contract to Yukari. She stares at it, overwhelmed. It’s a huge contract and it looks complicated. The director is right, she can’t afford to overlook important details."
        anim_dir "Read it over carefully and let my receptionist know when you’re ready."
        y "Thank you."
        #door sound
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
        #door sound
        staff "Sir, Yukari is ready."
        show anim_dir happy at right with dissolve
        anim_dir "Wonderful! Is everything in order, then?"
        show yukari happy
        y "Yes. I’m quite happy with the contract."
        "She signs it and returns it to the director."
        show yukari
        y "Thank you. I'll be back tomorrow with the revised storyboards and all the documents you'll need to start working on [anime.name]."
        anim_dir "That sounds fine. I’ll see you tomorrow, then."




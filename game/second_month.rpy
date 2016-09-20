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

label week_5_5:
    scene studio_main with fade
    show yukari at left
    show sumiko at Position(xalign=0.87,yalign=1.0)
    show yuuko at pos_outerright behind sumiko
    with dissolve
    $anim_studio = anim_studio_cheap
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
    #sound effect
    #CG here
    "Yukari bumps into Sumiko and the folder falls from her hands. The papers fall out all across the floor."
    y "Nooo! It took me so long to arrange them properly. Now I have to organize them again, and I was just about to head to [anim_studio]…"
    s "I’m sorry!"
    "No, I’m not blaming you. You were standing still, after all. It’s my fault for not paying attention to where I was walking."
    s "You’re so clumsy sometimes… Come on, I’ll help you."
    yuu "Me too."
    "The three of them work together to pick up the scattered pieces of paper and file them again."
    #end cg
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
    #surprised yukari
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
        #door sound
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
    #surprised yukari
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
    #surprised sumiko
    s "Huh?! Since when?"
    yuu "Sumiko and her friends were working on a manga, but some of the most interesting moments were off-panel. That frustrated me, so I drew those scenes myself."
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
    scene home with fade
    show yukari at left with dissolve
    "What shall Yukari do this weekend?"
    menu:
        "Spend the weekend with your friends":
            "Yukari calls up some of her friends from high school."
            "For part of the weekend, they go to the park to enjoy the nice weather, and then they spend the rest of it catching up with one another."
        "Raise Funds":
            "On her way home from the studio on Friday, Yukari noticed a local store that needed temporary help over the weekend due to a promotional event."
            "She took the opportunity to sign up."
            "Now that the weekend has arrived, she spends it working in the store to raise additional funds for [anime.name]."
        "Attend a workshop on life skills":
            "The workshop largely goes over stuff Yukari has heard time and time again, but on the other hand, it gives her a few new ideas for managing the team’s time and resources and for being an effective leader."
        "Relax":
            "She stays at home all weekend, reading books and watching anime. It’s a nice, stress-free way to recharge for the next week."

label week_6_1:
    scene studio with fade
    show yukari at pos_left
    show sumiko at pos_middleright
    show yuuko at pos_right behind sumiko
    show shunsuke at pos_outerright
    show mayumi at pos_farleft behind yukari
    with dissolve
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
        m "It’s casting Shin I’m most concerned about. Since he’s the antagonist, we need a voice actor capable of sounding sinister, without being obvious from the start."
        s "Why not have him sound completely sweet and innocent?"
        m "Because if he still sounds that way when the truth comes out, either the audience won’t believe his confession or he’ll come across as more psychopathic than Shunsuke intended."
    elif anime.category == Anime.ACTION:
        m "As the protagonist, Itaru needs a strong voice actor because of the stressful situations he’s put into."
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
        y "Hello, I’m here to see [Director Name 1]."
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
        #door sound
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
            "Yukari takes into account what Shunsuke said earlier and joins him to look over his changes and polish the storyboards further."
        "The Plot for [anime.name]":
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
        "Talent Agency":
            y "The talent agency is the best way for us to ensure we get quality voice acting."
            y "Yes, it costs more, but it will also free up our time to work on other things."
            $va_choice = "Talent Agency"
            #va choice is for branching text
        "Agent":
            y "Working through agents is the ideal middle ground."
            y "We won’t have to search for the voice actors ourselves, but we won’t have to deal with a talent agency’s high prices either."
            $va_choice = "Agent"
        "Freelancers":
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

label week_6_3:
    scene studio_main with fade
    show yukari at left
    show shunsuke at right
    with dissolve
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
        m "I spent all day talking to agents. We’ve already got a few promising voice actor candidates lined up."
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
    scene studio_main with fade
    show yukari surprised at left 
    show sumiko at right
    with dissolve
    $anim_studio = anim_studio_expensive
    #phone ringing sound
    y "Who could that be?"
    y "It’s our investor! What should I do?"
    show sumiko sigh
    s "Answer it, of course!"
    "Yukari stares at the phone, frozen with dread. Why would the investor call?"
    s "Ignoring our investor is probably a terrible idea. My guess is that he wants to check up on our progress on [anime.name]. Just talk to the man!"
    show yukari
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
    # if week 2 gureilla marketing
    # y "We’ve also done a little pre-release marketing through social networks."
    # investor "That only goes so far. A larger push will help [anime.name] receive the attention it needs."
    # if no guerilla marketing
    #y "We haven’t done any marketing yet,though."
    investor "Remember, a small studio like yours won’t have the name recognition to attract fans to [anime.name] from the start."
    investor "With a proper marketing campaign, you can catch people’s attention."
    "Yukari nods. They’ll need to work hard to win an audience for [anime.name]."
    "On the other hand, not only will they have to dip into their funds, but they’ll also need to put in the time and effort to promote it."
    investor "It’s just my advice. What do you think?"
    menu:
        "Listen to your investor's advice and start marketing":
            $investor_marketing = True
            y "You’re right. We need to start marketing, and this is the best time to do it. We’ll get started immediately."
            show investor happy
            investor "I’m glad to hear it. Contact me if you need any help."
        "Reject the offer and say you're busy with your current workload":
            $investor_marketing = False
            y "I’m afraid our current workload is too much for us to add a new task now."
            y "Until [anime.name] is complete, we’ll need to make do with minor marketing efforts."
            investor "Well, that’s your decision."
    investor "I look forward to hearing more about your progress in the future. However, I need to leave now. Good luck, Yukari."
    "She shakes his hand."
    y "Thank you."

label week_6_5:
    scene studio_main with fade
    show yukari at left
    with dissolve
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
    #to do category stuff
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
            "As she told Shunsuke, it’s critical to finish the storyboards."
            "Yukari spends the rest of the day working on the storyboard for the second episode."
        "Animation":
            "While she doesn’t have direct involvement with the animation process, Yukari looks over everything [anim_studio] has done so far to make sure it’s on track with her vision for [anime.name]."
        "Backgrounds":
            "Yukari joins Sumiko to look over the final backgrounds they’ll use for [anime.name]."
        "Relax":
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
    scene home with fade
    show yukari at left with dissolve
    "It's the weekend! What will you do?"
    menu:
        "Visit [anim_studio]":
            scene street with fade
            show yukari surprised at left with dissolve
            y "Huh? The door’s locked…"
            "She frowns at the closed studio and then notices a sign on the door that lists its hours."
            y "It’s closed on the weekends? Aw man…"
        "Raise Funds":
            "After browsing online for fundraising ideas, Yukari creates a page where fans interested in [anime.name] will be able to make small donations."
            "It might not produce too many results, but a passive way to increase their funds is exactly what they need."
        "Read Books":
            "Yukari reads a variety of books, some about the anime production process and others just for fun."
            "By the time the weekend ends, she feels inspired and ready to proceed."
        "Relax":
            "Yukari sleeps in on the weekend, watches some anime, and de-stresses to prepare for the week ahead."


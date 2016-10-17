init python:
    global anime
    global yukari_stats
    global mayumi_stats
    global shunsuke_stats
    global sumiko_stats
    global yuuko_stats

    #minus funds
    JOB_OFFER_FUNDS = 3
    REQUEST_SALARY_FUNDS = 10
    SUSPICIOUS_BUSINESSMAN_FUNDS = 5
    WRONG_FOOD_FUNDS = 5

##1.joboffering
    def rechoice_1_1(character): 
        #1) Continue working as normal and assume [Character Name] will get over it (- a lot of happiness)
        character.happiness -= 1.5
    def rechoice_1_2():
        #2) Offer [Character Name] money from funds to persuade [him/her] to stay ( -funds )
        anime.funds -= JOB_OFFER_FUNDS

##2. Request for Raise in Salary/Allowance or Money  #Condition : Happens when (A lot of funds)
    def rechoice_2_1(character): 
        #1) Tell [Character Name] to approach <abc bank>. They are known to offer reasonable loans. ( [Character Name] +stress – happiness)
        character.happiness -= 0.5
        character.stress += 0.5

    def rechoice_2_2(): 
        #2) Give [Character Name] money from the project funds 
        anime.funds -= REQUEST_SALARY_FUNDS

#3. Conflict during Team Meetings (This can be a weekly/monthly compulsory event)
    def rechoice_3_1(character): 
        #1) Agree with [Character 1] (+ Character 1 happiness )
        character.happiness += 0.5

    def rechoice_3_2(): 
        #2) Agree with [Mayumi] (+ mayumi happiness
        mayumi_stats.happiness += 0.5

    def rechoice_3_3(character): 
        #3) Try to distract them by changing the topic (% chance, if success nothing happen, if failure both–happiness)
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            #success
            return True
        else:
            #failure
            mayumi.stats.happiness -= 0.5  
            character.happiness -= 1 
            return False
        
#4. Interview Request for Aspiring Anime Producers
    def rechoice_4_1(): 
        #1) Attend the interview (+marketing if success, if fail yukari – happiness, + stress) #Condition: Marketing stats high (Week 4 onwards)
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            #success
            anime.marketing += 1.5
            return True
        else:
            #failure
            yukari_stats.happiness -= 0.5 
            yukari_stats.stress += 0.5 
            return False
        
    def rechoice_4_2(): 
        pass
        #2) Do not attend the interview
        
    def rechoice_4_3(character): 
        #3) Send [Character Name] to be interviewed instead. (low % chance to +marketing if sucesss, if fail, [Character Name] - happiness, + stress]
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            #success
            anime.marketing += 1
        else:
            #failure
            character.happiness -= 0.5
            character.stress += 0.5  
           


#5. Receiving Anonymous Troll E-Mails            # nochoice
        #if Yukari happiness > 50% nothing happen
    def rechoice_5_1_success():
        # if Yukari happiness < 50% ( -happiness, + stress for everyone)
        yukari_stats.happiness    -= 0.5
        mayumi_stats.happiness    -= 0.5
        shunsuke_stats.happiness  -= 0.5
        sumiko_stats.happiness    -= 0.5
        yuuko_stats.happiness -= 0.5
    def rechoice_5_1_failure():
        yukari_stats.stress   += 0.5
        mayumi_stats.stress   += 0.5
        shunsuke_stats.stress += 0.5
        sumiko_stats.stress   += 0.5
        yuuko_stats.stress    += 0.5

#6. A Suspicious Businessman Calls
    def rechoice_6_1(): 
        #1) Accept the advertising deal (- funds + happiness – stress for everyone) #Condition: At least <some marketing value> like 3?
        anime.funds -= SUSPICIOUS_BUSINESSMAN_FUNDS

        yukari_stats.happiness  += 0.5
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.happiness    += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.happiness   += 0.5

        yukari_stats.stress -= 0.5
        mayumi_stats.stress -= 0.5
        shunsuke_stats.stress -= 0.5
        sumiko_stats.stress -= 0.5
        yuuko_stats.stress  -= 0.5

    def rechoice_6_2():
        pass
        #2) Refuse the advertising deal

#7. Anime Convention During A Weekend
    def rechoice_7_1(character): 
        #1) Tell [Character Name] he/she won't be going 
        #(Characters who attend the convention will get a small boost in happiness or proficiency, while the one who is left out – happiness)(+ marketing for anime )
        anime.marketing += 0.5
        character.happiness  -= 1
        character_list = [yukari_stats,mayumi_stats,shunsuke_stats,yuuko_stats,sumiko_stats]
        #test this now (boost happiness and proficiency for other characters)
        for char in character_list:
            if char.name != character.name:
                char.happiness   += 0.5 
                char.proficiency += 0.5

    def rechoice_7_2(): 
        #2) Stay behind and let the four team members go
        anime.marketing += 0.5

        yukari_stats.happiness  -= 1
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.proficiency  += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.proficiency += 0.5
#8. All-You-Can-Eat Ice-Cream
    def rechoice_8_1(): #1) Continue to work without suggesting a break at the café #Condition: When Happiness low
        pass

    def rechoice_8_2():  
        #(2) Announce the café break (+happiness – stress for everyone)
        yukari_stats.happiness  += 0.5
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.Happiness += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.happiness   += 0.5

        yukari_stats.stress -= 0.5
        mayumi_stats.stress -= 0.5
        shunsuke_stats.stress -= 0.5
        sumiko_stats.stress -= 0.5
        yuuko_stats.stress  -= 0.5
#9. Street Musician Donation
    def rechoice_9_1(): 
        #(1) Continue walking home without donating( - mayumi happiness )
        mayumi_stats.happiness -= 0.5

    def rechoice_9_2(): 
        #(2) Take out your walletto donate ( + mayumi happiness)
        mayumi_stats.happiness += 0.5

#10. Flowers for Charity (got nothing)

#11. Shiny Object On The Ground
    def rechoice_11_1(): 
        #1) Cross the road without paying heed to the object
        pass
    def rechoice_11_2(): 
        #(2) Attempt to pick up the object (Yukari + happiness, - stress)
        yukari_stats.happiness += 0.5
        yukari_stats.stress -= 0.5

#12. Homeroom Teacher Surprise Visit
        #Random % chance for teacher to like their anime depending on Yukari stats (High management, low stress high happiness = higher chance)

        def rechoice_12_1_success():
            #If the teacher likes the anime, (+ happiness for everyone)
            yukari_stats.happiness     += 0.5
            mayumi_stats.happiness += 0.5
            shunsuke_stats.happiness   += 0.5
            sumiko_stats.happiness += 0.5
            yuuko_stats.happiness  += 0.5
        def rechoice_12_1_failure():
            pass
            #If the teacher doesn’t like it,

#13. Where's my umbrella?
    def rechoice_13_1(): 
        #(1) Dash home as fast as possible to try and avoid the storm ( - happiness, + stress for yukari)
        yukari_stats.happiness -= 0.5
        yukari_stats.stress += 0.5

    def rechoice_13_2(): 
        #(2) Wait under a small shelter until the storm subsides (+ yukari happiness)
        yukari_stats.happiness += 0.5

#14. Classmates Wish to Drop By  
    def rechoice_14_1(): 
        #(1) Invite the clique of girls to the studio to catch up( - happiness + stress for everyone )
        yukari_stats.happiness  -= 0.5
        mayumi_stats.happiness  -= 0.5
        shunsuke_stats.happiness    -= 0.5
        sumiko_stats.happiness  -= 0.5
        yuuko_stats.happiness   -= 0.5

        yukari_stats.stress += 0.5
        mayumi_stats.stress += 0.5
        shunsuke_stats.stress += 0.5
        sumiko_stats.stress += 0.5
        yuuko_stats.stress  += 0.5
    def rechoice_14_2(): 
        pass
        #(2) Turn them down, saying the team is too busy with production
            
#15. Won a prize on the radio! # subchoice in choiuce
        #(1) Ask how [he/she] won the prize 
        ##(a) Celebrate with Character Name and suggest sharing with the studio funds  
        ##(b) Tell off Character Name for listening to the radio during work 
    def rechoice_15_1():
        #25%
        anime.funds += 5
        yukari_stats.happiness += 0.5
        mayumi_stats.happiness += 0.5
        shunsuke_stats.happiness += 0.5
        sumiko_stats.happiness += 0.5
        yuuko_stats.happiness  += 0.5
    def rechoice_15_2(character):
        ##(B) 50% (+ minor funds)( - [character name] happiness ) (everyone else + happiness).
        character_list = [yukari_stats,mayumi_stats,shunsuke_stats,yuuko_stats,sumiko_stats]
        anime.funds += 8
        character.happiness  -= 0.5
        for char in character_list:
            if char.name != character.name:
                char.happiness += 0.5  
    def rechoice_15_3(character):
        ##(C) 75% (+ normal funds) ( - [character name] happiness ) (everyone else + happiness)
        character_list = [yukari_stats,mayumi_stats,shunsuke_stats,yuuko_stats,sumiko_stats]
        anime.funds += 10
        character.happiness  -= 1.0
        for char in character_list:
            if char.name != character.name:
                char.happiness += 0.5  
    def rechoice_15_4(character):
        ##(D) 100%(abit more than normal funds)  ( - [character name] a lot happiness ) (everyone else + happiness)
        character_list = [yukari_stats,mayumi_stats,shunsuke_stats,yuuko_stats,sumiko_stats]
        anime.funds += 15
        character.happiness  -= 1.5
        for char in character_list:
            if char.name != character.name:
                char.happiness += 0.5  

#16. Wrong Food Delivery Address
    def rechoice_16_1(): 
        #(1) Pay for the delivery and make the team happy (+ happiness for everyone, -funds )
        anime.funds -= WRONG_FOOD_FUNDS

        yukari_stats.happiness += 0.5
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.happiness += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.happiness   += 0.5

    def rechoice_16_2(): 
        #(2) Clarify to the delivery person that he’s at the wrong address
        pass

#17. Coffee or Tea?     
    def rechoice_17_1(): 
        #(1) Pick the coffee (+happiness – stress for Yukari & Mayumi)
        yukari_stats.happiness += 0.5
        mayumi_stats.happiness += 0.5

        yukari_stats.stress -= 0.5
        mayumi_stats.stress -= 0.5

    def rehoice_17_2(): 
        #(2) Pick the matcha (+happiness –stress for Shunsuke and Sumiko)
        shunsuke_stats.happiness += 0.5
        sumiko_stats.happiness += 0.5

        shunsuke_stats.stress -= 0.5
        sumiko_stats.stress -= 0.5

#18. Street Artist Sketch
    def rechoice_18_1(): 
        #(1) Small tip $ (Yukari + minor happiness, - minor stress )
        yukari_stats.happiness += 0.5 
        yukari_stats.stress -= 0.5

    def rechoice_18_2(): 
        #(2) Moderate tip $$ (Yukari + happiness, - stress )
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    def rechoice_18_3(): 
        #(3) Generous tip $$$ (Yukari + more happiness, - more stress )
        yukari_stats.happiness += 1.5
        yukari_stats.stress -= 1.5

#19. Overdue library book!  
    def rechoice_19_1():
        pass
         #(1) Return the book to the library on the way to work

    def rechoice_19_2(): 
        #(2) Choose to remain quiet since the librarian never said anything  (- happiness, + stress for yukari)
        yukari_stats.happiness -= 0.5
        yukari_stats.stress += 0.5

#20. Newbie Voice Actor Looking for Work
    def rechoice_20_1(): 
        #(1) Truthfully inform Miki that she needs more practice before she goes pro ( + yukari management )
        yukari_stats.management += 0.5

    def rechoice_20_2(): 
        #(2) Lie to Miki that her voice acting is great, in order to make use of her studio ( + stress, - happiness for yukari )
        yukari_stats.happiness -= 0.5
        yukari_stats.stress += 0.5

#21. Suspicious Backpack (nothing)

#22. New Menu - Food Tasting Session
    def rechoice_22_1(): #(1) Tell the team that there are already plans to attend the workshop (+ proficiency for everyone, - happiness for everyone)
        yukari_stats.happiness  -= 0.5
        mayumi_stats.happiness  -= 0.5
        shunsuke_stats.happiness    -= 0.5
        sumiko_stats.happiness  -= 0.5
        yuuko_stats.happiness   -= 0.5

        yukari_stats.proficiency += 0.5
        mayumi_stats.proficiency    += 0.5
        shunsuke_stats.proficiency += 0.5
        sumiko_stats.proficiency    += 0.5
        yuuko_stats.proficiency += 0.5

    def rechoice_22_2(): 
        # need buff
        #(2) Scrap the workshop plan and join the food tasting session with everyone (+ happiness, - stress for everyone)
        yukari_stats.happiness  += 0.5
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.happiness += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.happiness   += 0.5

        yukari_stats.stress -= 0.5
        mayumi_stats.stress -= 0.5
        shunsuke_stats.stress -= 0.5
        sumiko_stats.stress -= 0.5
        yuuko_stats.stress  -= 0.5

#23. Bumped into popular Seiyū Mamoru-san!
    def rechoice_23_1(): 
        #(1) Ask for an autograph and to take a picture first (mayumi +stress, - happiness)
        mayumi_stats.stress += 0.5
        mayumi_stats.happiness -= 0.5

    def rechoice_23_2(): 
        #(2) Return his sunglasses and ask if he's fine first (mayumi – stress, + happiness )
        mayumi_stats.stress -= 0.5
        mayumi_stats.happiness += 0.5

#24. Unbelievably Hot Summer
    def rechoice_24_1(): 
        #1) Call for an electrician to take a look (sumiko + abit happiness, - abit stress)
        sumiko_stats.happiness += 0.5
        sumiko_stats.stress -= 0.5

    def rechoice_24_2(): 
        #2) Tell Sumiko the AC isn’t broken (everyone –happiness + stress )
        yukari_stats.happiness  -= 0.5
        mayumi_stats.happiness  -= 0.5
        shunsuke_stats.happiness -= 0.5
        sumiko_stats.happiness  -= 0.5
        yuuko_stats.happiness   -= 0.5

        yukari_stats.stress += 0.5
        mayumi_stats.stress += 0.5
        shunsuke_stats.stress += 0.5
        sumiko_stats.stress += 0.5
        yuuko_stats.stress  += 0.5

#25. Arts Festival Performance
    def rechoice_25_1(): 
        ##(1) Yuuko (+ character more happiness, - more stress )
        yuuko_stats.happiness += 1
        yuuko_stats.stress -= 1

    def rechoice_25_2(): 
        #(2) Yukari (+ character happiness, - stress )
        yukari_stats.happiness += 0.5
        yukari_stats.stress -= 0.5

    def rechoice_25_3(): 
        #(3) Sumiko (+ character happiness, - stress )
        sumiko_stats.happiness += 0.5
        sumiko_stats.stress -= 0.5

    def rechoice_25_4(): 
        #(4) Shunsuke (+ character happiness, - stress )
        shunsuke_stats.happiness += 0.5
        shunsuke_stats.stress -= 0.5
#26. Animation Studio Ex-Employee (nothing happen)

#27. Shunsuke shows a surprise video montage
    def rechoice_27_1(): 
        #(1) Hang out with the team at the restaurant this weekend. (everyone + happiness, - stress)
        yukari_stats.happiness  += 0.5
        mayumi_stats.happiness  += 0.5
        shunsuke_stats.happiness += 0.5
        sumiko_stats.happiness  += 0.5
        yuuko_stats.happiness   += 0.5

        yukari_stats.stress -= 0.5
        mayumi_stats.stress -= 0.5
        shunsuke_stats.stress -= 0.5
        sumiko_stats.stress -= 0.5
        yuuko_stats.stress  -= 0.5
    def rechoice_27_2(): 
        #(2) Skip the restaurant to work on getting more funds instead. (+ funds, - shunsuke happiness)
        anime.funds += 10
        shunsuke_stats.happiness -= 1

#28. Child's Birthday Celebration   
    def rechoice_28_1(): 
        #(1) Yuuko gives the girl her newly-bought teddy bear keychain (+ yuuko happiness, - stress)
        yuuko_stats.happiness += 0.5
        yuuko_stats.stress -= 0.5
    def rechoice_28_2(): 
        #(2) Sumiko gives the girl a set of animal stickers she got at a bazaar (+ sumiko happiness, - stress)
        sumiko_stats.happiness += 0.5
        sumiko_stats.stress -= 0.5

#29. Decorate Restaurant (Not Y&S Restaurant) for Funds #Conditions: Happens when funds are low
    def rechoice_29_1(): 
        #(1) Take up the décor job at the restaurant (team's proficiency will drop, + stress and + some funds)
        anime.funds += 30

        # need - more 
        yukari_stats.proficiency -= 0.5
        mayumi_stats.proficiency -= 0.5
        shunsuke_stats.proficiency -= 0.5
        sumiko_stats.proficiency    -= 0.5
        yuuko_stats.proficiency -= 0.5

        yukari_stats.stress += 0.5
        mayumi_stats.stress += 0.5
        shunsuke_stats.stress += 0.5
        sumiko_stats.stress += 0.5
        yuuko_stats.stress  += 0.5
    def rechoice_29_2(): 
        pass
        #(2) Pass on the opportunity

#30. Funding Crisis  #Conditions: Funds are low
    def rechoice_30_1(): 
        #(1) Everyone should chip in so we have more money to fall back on (+ some funds, everyone except yukari – happiness, + stress )
        anime.funds += 25

        #need - more happiness & stress
        mayumi_stats.happiness -= 1
        shunsuke_stats.happiness -= 1
        sumiko_stats.happiness -= 1
        yuuko_stats.happiness -= 1

        mayumi_stats.stress += 1
        shunsuke_stats.stress += 1
        sumiko_stats.stress += 1
        yuuko_stats.stress  += 1

    def rechoice_30_2(): 
        #(2) Continue business-as-usual for the time being and be spontaneous ( - very little happiness, + very little stress for everyone)
        yukari_stats.happiness  -= 0.5
        mayumi_stats.happiness  -= 0.5
        shunsuke_stats.happiness -= 0.5
        sumiko_stats.happiness  -= 0.5
        yuuko_stats.happiness   -= 0.5

        yukari_stats.stress += 0.5
        mayumi_stats.stress += 0.5
        shunsuke_stats.stress += 0.5
        sumiko_stats.stress += 0.5
        yuuko_stats.stress  += 0.5

#31. Dance Challenge
    def rechoice_31_1(): 
        #(1) Register for the competition  (Yukari – happiness, + stress )
        yukari_stats.happiness -= 0.5
        yukari_stats.stress += 0.5
    def rechoice_31_2():
         #(2) Cheer on the competitors(Yukari + happiness, - stress)
        yukari_stats.happiness += 0.5
        yukari_stats.stress -= 0.5

#32. Free Breakfast Samples!
    def rechoice_32_1(): 
        #(1) Head into the cafe(+ happiness for sumiko, yuuko)
        sumiko_stats.happiness += 0.5
        yuuko_stats.happiness += 0.5
    def rechoice_32_2(): 
        #(2) Continue to work and be on time ( - happiness for sumiko, yuuko )
        sumiko_stats.happiness -= 0.5
        yuuko_stats.happiness -= 0.5

#33. Accessories at 50% Off!
    def rechoice_33_1():
        #(1) Go in and browse(Mayumi + happiness, - stress while everyone - happiness )
        mayumi_stats.happiness += 0.5
        mayumi_stats.stress -= 0.5

        yukari_stats.happiness  -= 0.5
        shunsuke_stats.happiness -= 0.5
        sumiko_stats.happiness  -= 0.5
        yuuko_stats.happiness   -= 0.5

    def rechoice_33_2():
        #(2) Return to the office
        pass

#34. Ideal Office Fragrance
    def rechoice_34_1(): 
        #(1) Tropical Grapefruit air freshener(Yukari + happiness, - stress )
        yukari_stats.happiness += 0.5
        yukari_stats.stress -= 0.5
    def rechoice_34_2(): 
        #(2) Ocean Breeze air freshener (Shunsuke,Mayumi + happiness, - stress)
        shunsuke_stats.happiness += 0.5
        shunsuke_stats.stress -= 0.5

        mayumi_stats.happiness += 0.5
        mayumi_stats.stress -= 0.5
    def rechoice_34_3(): 
        #(3) Classic Rosemary air freshener(Sumiko, Yuuko + happiness, - stress)
        sumiko_stats.happiness += 0.5
        sumiko_stats.stress -= 0.5

        yuuko_stats.happiness += 0.5
        yuuko_stats.stress -= 0.5

#35. How to Catch a Thief?
    def rechoice_35_1(): 
        #(1) Chase the thief (Shunsuke + happiness, - stress )
        shunsuke_stats.happiness += 0.5
        shunsuke_stats.stress -= 0.5
    def rechoice_35_2():
         #(2) Ask the lady to call the police( Shunsuke – happiness, + stress )
        shunsuke_stats.happiness -= 0.5
        shunsuke_stats.stress += 0.5
#36. Playful Child
    def rechoice_36_1(): 
        #(1) Get the child to leave(Yukari – happiness )
        yukari_stats.happiness -= 0.5
    def rechoice_36_2(): 
        #(2) Entertain the child(Yukari, Mayumi + happiness)
        yukari_stats.happiness += 0.5 
        mayumi_stats.happiness += 0.5
#37. Theme Song 
    def rechoice_37_1(): 
        pass
        #1) Pretend to not be involved

    def rechoice_37_2(): 
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            #success
            anime.marketing += 1
        else:
            #failure
            mayumi_stats.happiness -= 0.5 




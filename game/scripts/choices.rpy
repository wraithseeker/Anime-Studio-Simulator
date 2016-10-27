init python:
    global anime
    global yukari_stats
    global mayumi_stats
    global shunsuke_stats
    global sumiko_stats
    global yuuko_stats

    WEEK_8_GOOD_MARKETING_VALUE = 2.5
    #minus funds below
    EXPENSIVE_STUDIO_FUNDS_VALUE = 20
    CHEAP_STUDIO_FUNDS_VALUE = 10

    TALENT_AGENCY_FUNDS_VALUE = 20 
    AGENT_FUNDS_VALUE = 10
    FREELANCER_FUNDS_VALUE = 5

    INVESTOR_FUNDS_MARKETING_6_3_1 = 10
    ANIM_STUDIO_VALUE_10_2 = 10

    PROFESSIONAL_WEBSITE_VALUE = 20
    SHUNSUKE_WEBSITE_VALUE = 10


    NEGOTIATE_DEFAULT_FUNDS = 15
    NEGOTIATE_SUCCESS_FUNDS = 10


    def choice_raise_funds_formula():
        #Formula to calculate % chance to raise funds
        CHOICE_BASE_RAISE_FUNDS_PERCENT = 40
        CHOICE_RAISE_FUNDS_FORMULA = CHOICE_BASE_RAISE_FUNDS_PERCENT + (yukari_stats.management * 5) + (yukari_stats.proficiency * 2)
        return CHOICE_RAISE_FUNDS_FORMULA

    def choice_1_1_1():
        anime.character_design += 0.5
        anime.background += 0.5
    def choice_1_1_2():
        anime.plot += 0.5

    def choice_1_2_1():
        yukari_stats.management += 1
    def choice_1_2_2():
        yukari_stats.proficiency += 0.5
    def choice_1_2_3():
        anime.character_design += 0.5

    def choicewe_1_1_1():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
    def choicewe_1_1_2():
        yukari_stats.stress += 1.25
        anime.storyboard += 0.5
        yukari_stats.happiness -= 1.5

    def choice_2_1_1():
        shunsuke_stats.happiness -= 1.5
        yuuko_stats.happiness += 1
    def choice_2_1_2():
        shunsuke_stats.happiness += 1
        yuuko_stats.happiness -= 1.5

    def choice_2_2_1():
        anime.marketing += 0.5
    def choice_2_2_2():
        pass

    def choicewe_2_1_1():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
        mayumi_stats.happiness += 1
        mayumi_stats.stress -= 1
    def choicewe_2_1_2():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
        shunsuke_stats.happiness += 1
        shunsuke_stats.stress -= 1
    def choicewe_2_1_3():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
        yuuko_stats.happiness += 1
        yuuko_stats.stress -= 1
        sumiko_stats.happiness += 1
        sumiko_stats.stress -= 1

    def choice_3_1_1():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            yukari_stats.management += 1
            return True
        else:
            return False
    def choice_3_1_2():
        pass

    def choice_3_2_1():
        yukari_stats.happiness -= 1.5
        yukari_stats.stress += 2.5
        sumiko_stats.happiness -= 1.25
        sumiko_stats.stress += 1.5
    def choice_3_2_2():
        pass

    def choice_3_3_1():
        pass
    def choice_3_3_2():
        yukari_stats.stress += 2.5
        yukari_stats.happiness -= 2.25
        yukari_stats.proficiency += 1

    def choice_3_4_1():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
    def choice_3_4_2():
        yukari_stats.stress += 2.5

    def choicewe_3_1_1():
        yukari_stats.stress += 2
        anime.storyboard += 0.5
    def choicewe_3_1_2():
        # this choice adjusts management value
        management_value = 4
        if yukari_stats.management >= management_value:
            #stat check success
            yukari_stats.management += 1
            return True
        else:
            #failure   
            yukari_stats.management -= 0.5
            yukari_stats.stress += 2
            return False
    def choicewe_3_1_3():
        yukari_stats.stress -= 1

    def choice_4_1_1():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            yukari_stats.happiness -= 1.5
            yukari_stats.stress += 1.5
            return True
        else:
            return False
    def choice_4_1_2():
        anime.storyboard += 0.5
    def choice_4_1_3():
        yukari_stats.happiness += 1
        sumiko_stats.happiness += 1
        mayumi_stats.happiness += 1
        shunsuke_stats.happiness += 1
        yuuko_stats.stress -= 1
        yukari_stats.stress -= 1
        sumiko_stats.stress -= 1
        mayumi_stats.stress -= 1
        shunsuke_stats.stress -= 1
        yuuko_stats.stress -= 1

    def choicewe_4_1_1():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            return True
        else:
            return False
    def choicewe_4_1_2():
        yukari_stats.management += 1
    def choicewe_4_1_3():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
    def choicewe_4_1_4():
        anime.quality_check += 0.5

    def choice_5_1_1():
        yuuko_stats.proficiency += 1
        sumiko_stats.proficiency += 1
        anime.funds -= 20
        anime.quality_check += 0.5
    def choice_5_1_2():
        anime.funds -= 10

    def choicewe_5_1_1():
        yukari_stats.happiness += 1
    def choicewe_5_1_2():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            return True
        else:
            return False
    def choicewe_5_1_3():
        yukari_stats.proficiency += 1
        yukari_stats.management += 1
    def choicewe_5_1_4():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    def choice_6_1_1():
        anime.storyboard += 0.5
    def choice_6_1_2():
        anime.plot += 0.5
    def choice_6_1_3():
        anime.character_development += 0.5

    def choice_6_2_1():
        #talent agency
        anime.quality_check += 5
        anime.marketing += 1.5
        anime.funds -= TALENT_AGENCY_FUNDS_VALUE
    def choice_6_2_2():
        #agent
        anime.quality_check += 2.5
        anime.marketing += 1
        anime.funds -= AGENT_FUNDS_VALUE
    def choice_6_2_3():
        #freelancers
        anime.funds -= FREELANCER_FUNDS_VALUE

    def choice_6_3_1():
        anime.marketing += 1
        anime.funds -= INVESTOR_FUNDS_MARKETING_6_3_1
    def choice_6_3_2():
        pass

    def choice_6_4_1():
        anime.storyboard += 0.5
    def choice_6_4_2():
        anime.animation += 0.5
    def choice_6_4_3():
        anime.background += 0.5
    def choice_6_4_4():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    def choicewe_6_1_1():
        pass
    def choicewe_6_1_2():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            yukari_stats.happiness -= 1.5
            yukari_stats.stress += 1.5
            return True
        else:
            return False
    def choicewe_6_1_3():
        yukari_stats.proficiency += 1
        yukari_stats.management += 1
    def choicewe_6_1_4():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1


    # wrong choices during phone call
    def choice_7_1_1():
        mayumi_stats.stress += 1.5
        mayumi_stats.happiness -= 1.5
    def choice_7_1_2():
        yuuko_stats.stress += 1.5
        yuuko_stats.happiness -= 1.5
    def choice_7_1_3():
        sumiko_stats.stress += 1.5
        sumiko_stats.happiness -= 1.5

    def choice_7_2_1():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            yukari_stats.happiness -= 1.5
            yukari_stats.stress += 1.5
            return True
        else:
            return False
    def choice_7_2_2():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1
    def choice_7_2_3():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            yukari_stats.happiness += 1
            sumiko_stats.happiness += 1
            mayumi_stats.happiness += 1
            shunsuke_stats.happiness += 1
            yuuko_stats.stress -= 1
            yukari_stats.stress -= 1
            sumiko_stats.stress -= 1
            mayumi_stats.stress -= 1
            shunsuke_stats.stress -= 1
            yuuko_stats.stress -= 1
            return True
        else:
            return False

    def choice_8_1_1_cheap():
        pass
    def choice_8_1_2_cheap():
        # the animation number - here should be big, like what I put because it is major event in game 
        anime.animation -= 1
        anime.marketing += 0.5
    def choice_8_1_3_cheap():
        anime.storyboard += 0.5
        anime.animation -= 1

    def choice_8_1_1_expensive():
        anime.marketing += 0.5
    def choice_8_1_2_expensive():
        anime.storyboard += 0.5
    def choice_8_1_3_expensive():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.funds += 15
            yukari_stats.happiness -= 1.5
            yukari_stats.stress += 1.5
            return True
        else:
            return False

    def choicewe_8_1_1():
        anime.quality_check += 0.5
    def choicewe_8_1_2():
        yukari_stats.happiness += 1
        sumiko_stats.happiness += 1
        mayumi_stats.happiness += 1
        shunsuke_stats.happiness += 1
        yuuko_stats.stress -= 1
        yukari_stats.stress -= 1
        sumiko_stats.stress -= 1
        mayumi_stats.stress -= 1
        shunsuke_stats.stress -= 1
        yuuko_stats.stress -= 1
    def choicewe_8_1_3():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    #OST order, 3 choices, 2 wrong 1 correct for diff genres
    def choice_9_1_correct():
        anime.quality_check += 0.5
    def choice_9_1_wrong():
        anime.quality_check -= 0.5

    ### Website Choice
    ###MISSING - FUNDS FOR WEBSITE, IMPORTANT, READ IT NOW #######
    def choice_9_2_1():
        #Professional Website ($$$)
        anime.funds -= PROFESSIONAL_WEBSITE_VALUE
        anime.quality_check += 5
        anime.marketing += 2
    def choice_9_2_2():
        #Website made by Shunsuke ($$)
        anime.funds -= SHUNSUKE_WEBSITE_VALUE
        anime.quality_check += 3
        anime.marketing += 1
    def choice_9_2_3():
        pass

    def choicewe_9_1_1():
        yukari_stats.happiness += 1
        sumiko_stats.happiness += 1
        mayumi_stats.happiness += 1
        shunsuke_stats.happiness += 1
        yuuko_stats.stress -= 1
        yukari_stats.stress -= 1
        sumiko_stats.stress -= 1
        mayumi_stats.stress -= 1
        shunsuke_stats.stress -= 1
        yuuko_stats.stress -= 1
    def choicewe_9_1_2():
        yukari_stats.proficiency += 1
        yukari_stats.management += 1
    def choicewe_9_1_3():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    def choice_10_1_1():
        pass
    def choice_10_1_2():
        anime.funds -= ANIM_STUDIO_VALUE_10_2
        anime.quality_check += 0.5
        anime.marketing += 0.5

    def choice_10_2_1():
        anime.ost += 0.5
    def choice_10_2_2():
        anime.marketing += 0.5
    def choice_10_2_3():
        pass
    def choice_10_2_4():
        yukari_stats.happiness += 1
        yukari_stats.stress -= 1

    def choicewe_10_1_1():
        number = renpy.random.randint(0,100)
        if number <= choice_raise_funds_formula():
            anime.marketing += 1
            return True
        else:
            return False
    def choicewe_10_1_2():
        pass

    def choice_12_1_1():
        anime.quality_check += 0.5
    def choice_12_1_2():
        anime.voice_acting += 0.5
        anime.ost += 0.5
        anime.op_ed += 0.5
    def choice_12_1_3():
        anime.marketing += 0.5

    # happens in Week 7, Monday
    def negotiate_default():
        anime.funds -= NEGOTIATE_DEFAULT_FUNDS

    def negotiate_success():
        anime.funds -= NEGOTIATE_SUCCESS_FUNDS


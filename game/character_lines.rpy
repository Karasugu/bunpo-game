define xx = Character("XX")
define mc = Character("MC")


transform character_xx:
    xalign 1.15
    yalign 1.0
    yoffset 900
    xysize (config.screen_width // 1, int(config.screen_height * 1.7))
    fit "contain"

transform character_mc:
    yalign 1.0
    xalign 0.25
    xysize (config.screen_width // 2, int(config.screen_height * 7/ 8))
    fit "contain"

label choose_dia:
    show mc default at character_mc
    mc "質問！"
    show xx default at character_xx
    xx "なに。"
    mc "先せんせいはこう言いましたよね。"
    mc "[sentences[sentence_index]]と。" 
    mc "それはおかしいではないでしょうか。"
    show xx shock at character_xx
    xx "な、な、なにがおかしいて。俺様が言いったことに間違えがあるはずがない！"
    
    if sentence_index == correct:
        jump choose_right
    else:
        $ livesLeft = livesLeft - 1
        jump choose_wrong


label choose_wrong:
    show mc default at character_mc
    show xx shock at character_xx
    
    
    mc "おかしいなとこは..."
    show mc emotionless at character_mc
    mc "おかしいなとこは..."
    show mc question at character_mc
    mc "え？ どこがおかしいだっけ。"
    
    if livesLeft >= 1:
        show xx smirk at character_xx
        xx "だから言っただろう。"
        xx "俺様が間違うわけがない。"
        xx "またこんなことを言って俺様の授業を邪魔したら追い出すぞ！！！"

        show mc blush at character_mc
        mc "すみません..."
        jump expression current_stage
    else:
        xx "もういいから！うっぜいよ、アンタ！"
        mc "申し訳ございませんでした。"
        hide mc
        hide xx
        jump home

label choose_right:
    show mc default at character_mc
    show xx shock at character_xx

    python:
        explanation_lines = [s + "。" for s in explanation.split("。") if s.strip()]

        for line in explanation_lines:
            renpy.say(mc, line)
    
    show xx embarrass at character_xx
    xx "ぐぬぬ…！"

    hide mc
    hide xx

    if stageName == "stage1_4":
        $ stage1_4cleared = True
    if stageName == "stage2_4":
        $ stage2_4cleared = True
    if stageName == "stage3_4":
        $ stage3_4cleared = True
    if stageName == "stage4_4":
        $ stage4_4cleared = True
    if stageName == "stage5_4":
        $ stage5_4cleared = True
    if stageName == "stage6_4":
        $ stage6_4cleared = True
    if stageName == "stage7_4":
        $ stage7_4cleared = True
    if stageName == "stage8_4":
        $ stage8_4cleared = True
    if stageName == "stage9_4":
        $ stage9_4cleared = True
    if stageName == "stage1_5":
        $ stage1_5cleared = True
    if stageName == "stage2_5":
        $ stage2_5cleared = True
    if stageName == "stage3_5":
        $ stage3_5cleared = True
    if stageName == "stage4_5":
        $ stage4_5cleared = True
    if stageName == "stage5_5":
        $ stage5_5cleared = True
    if stageName == "stage6_5":
        $ stage6_5cleared = True
    if stageName == "stage7_5":
        $ stage7_5cleared = True
    if stageName == "stage8_5":
        $ stage8_5cleared = True

    jump home

label next_wrap_dia:
    show mc smile at character_mc
    mc "これで全部見たな。"
    mc "落ち着いて考えてみて、この五つの中に必ず間違いがある。"
    mc "それを見つけだし、指摘するんだ。"
    hide mc
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

label start1:
    show xx default at character_xx
    xx "ようこそ諸君、俺様の教室へ！"
    show xx smirk at character_xx
    xx "まあ俺様がしらない者はいないと思うが、一応自己紹介をしてあげろうか！"
    xx "俺様こそ偉大なるｘｘ、以後ｘｘ先生と呼ぶといい。"
    hide xx
    
    show mc default at character_mc
    mc "これが噂になっているｘｘか。"
    mc "小学生にしか見えないじゃないか。一体どうして日本語の教師になりたいと思ったやら。"
    mc "まあ大人だろうが小学生だろうが関係ない、僕のやるべきことは変わらない。"
    mc "ｘｘは必ず間違いをする。"
    mc "僕はその間違えを見つけ出し、指摘するだけ。"
    mc "先輩達の仇、僕が取る！"
    hide mc
    $ stageName = "stage1_4"

    call stage1_4


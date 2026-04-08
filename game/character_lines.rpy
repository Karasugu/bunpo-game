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
    mc "さっき、先生はこう言いましたよね。"
    mc "[sentences[sentence_index]]と。" 
    mc "それはおかしいではないでしょうか。"
    show xx shock at character_xx
    xx "な、な、なにがおかしいて。俺様が言ったことに間違いがあるはずがない！"
    
    if sentence_index == correct:
        jump choose_right
    else:
        $ livesLeft = livesLeft - 1
        jump choose_wrong


label choose_wrong:
    show mc default at character_mc
    show xx shock at character_xx
    
    
    mc "おかしいとこは..."
    show mc emotionless at character_mc
    mc "おかしいとこは..."
    show mc question at character_mc
    mc "え？ どこがおかしいんだっけ。"
    
    if livesLeft >= 1:
        show xx smirk at character_xx
        xx "だから言っただろう。俺様が間違えるわけがない。"
        xx "またこんなことを言って俺様の授業を邪魔したら追い出すぞ！！！"

        show mc blush at character_mc
        mc "すみません..."
        hide mc 
        hide xx
        jump expression current_stage
    else:
        show xx default at character_xx
        xx "もういいから！うっぜいよ、アンタ！"
        show mc cry at character_mc
        mc "申し訳ございませんでした。"
        hide mc
        hide xx
        $ returnFromStage = True
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
    if stageName == "stage1_6":
        $ stage1_5cleared = True
    if stageName == "stage2_6":
        $ stage2_5cleared = True
    if stageName == "stage3_6":
        $ stage3_5cleared = True
    if stageName == "stage4_6":
        $ stage4_5cleared = True
    if stageName == "stage5_6":
        $ stage5_5cleared = True
    if stageName == "stage6_6":
        $ stage6_5cleared = True
    if stageName == "stage7_6":
        $ stage7_5cleared = True
    if stageName == "stage8_6":
        $ stage8_5cleared = True
    if stageName == "stage9_6":
        $ stage8_5cleared = True
    $ returnFromStage = True

    jump home

label next_wrap_dia:
    show mc smile at character_mc
    mc "これで全部見たな。"
    mc "落ち着いて考えてみて。この五つの中に必ず間違いがある。"
    mc "それを見つけだし、指摘するんだ。"
    hide mc
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

label start1:
    show xx default at character_xx
    xx "ようこそ諸君、俺様の教室へ！"
    show xx smirk at character_xx
    xx "まあ俺様を知らない者はいないと思うが、一応自己紹介をしてあげようか！"
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

label END:
    show xx default at character_xx
    show mc default at character_mc
    mc "おめでとうございます！"
    xx "おめでとう..."
    mc "ここでこのゲームは終わりますが、物語は終わりませんですよね。"
    mc "xxのことなんですが、ぶっちゃけ言いますと、悪意がなかったらしいですよ。"
    mc "要するに、噂をそのまま信じちゃいけないってことですよね。"
    mc "xxは確かにお金持ちのボンボンですけど (ಠ_ಠ)、別に自由で幸せな暮らしをしていたわけではなかったんです。"
    mc "生まれたときから英才教育を受けさせられていて、自分の選択や自分の時間はほとんどなかったんです。"
    mc "xx企業のCEOの一人息子という立場が、彼に与えたのは孤独と、意地とも言えるプライドでした。"
    mc "そんな日常で、彼は素晴らしきアニメと出会ったんです。"
    mc "それから彼は自分のわずかな自由時間で色々な作品と出会い、日本語に興味を持つようになりました。"
    mc "「同じ趣味の人に出会うかも」「友達になれるかも」、そんなことを考えて彼は日本語クラスに憧れていた。"
    mc "アニメを通して独学で日本語を勉強し、12歳の誕生日で勇気を振り絞って父親にお願いをした。"
    mc "彼は分かっている、一般的な生徒として日本語教室に参加するのは、xx企業のCEOの一人息子という立場では絶対に許されないと。"
    mc "だから彼は父親にこう言った。"
    xx "「俺様は世界一の日本語教師になる！」"
    mc "...まあ、それも全部昔の話ですけどね。"
    mc "今ではxxも普通の生徒になって、みんなに謝った後、仲良くやっています。"
    mc "「どうやって？」って僕に聞いても困りますね。"
    mc "でもヒントとして僕の名前のMとCの意味を考えてみて。"
    mc "言えることは、MainなCharacterとして都合よく有名な“mc企業”の長男であっても、そして都合よくxx企業より強い後ろ盾があってもおかしくない、ってことくらいですかね (笑)"
    mc "まあ... 普通そうでもないと、xx企業のCEOの一人息子をこうも恥をかかせるわけがないよね..."
    hide xx 
    hide mc
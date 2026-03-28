define xx = Character("XX")
define mc = Character("MC")
image xx = "xx default.jpg"
image mc = "mc default.jpg"

transform character_xx:
    xalign 0.25
    yalign 1.0

transform character_mc:
    xalign 0.75
    yalign 1.0

label choose_dia:
    show mc at character_mc
    mc "質問！"
    show xx at character_xx
    xx "なに？！"
    mc "先せんせいはこう言いましたよね"
    mc "[sentences[sentence_index]]と" 
    mc "それはおかしいではないでしょうか"
    xx "な、な、なにがおかしいて。俺様が言いったことに間違えがあるはずがない！"
    
    if sentence_index == correct:
        jump choose_right
    else:
        jump choose_wrong


label choose_wrong:
    show mc at character_mc
    show xx at character_xx

    mc "おかしいなとこは..."
    mc "おかしいなとこは..."
    mc "え？ どこがおかしいだっけ。"
    
    xx "貴様アアア！！！"
    xx "またこんなことを言って俺様の授業を邪魔したら追い出すぞ！！！"

    mc "すみません..."

    jump expression current_stage

label choose_right:
    show mc at character_mc
    show xx at character_xx

    python:
        explanation_lines = [s + "。" for s in explanation.split("。") if s.strip()]

        for line in explanation_lines:
            renpy.say(mc, line)

    xx "ぐぬぬ…！"

    hide mc
    hide xx

    jump home


label start1:
    show xx at character_xx
    xx "ようこそ諸君、俺様の教室へ！"
    xx "まあ俺様がしらない者はいないと思うが、一応自己紹介をしてあげろうか！"
    xx "俺様こそ偉大なるｘｘ、以後ｘｘ先生と呼ぶといい。"
    hide xx
    
    show mc at character_mc
    mc "これが噂になっているｘｘか。"
    mc "小学生にしか見えないじゃないか。一体どうして日本語の教師になりたいと思ったやら。"
    mc "まあ大人だろうが小学生だろうが関係ない、僕のやるべきことは変わらない。"
    mc "ｘｘは必ず間違いをする。"
    mc "僕はその間違えを見つけ出し、指摘するだけ。"
    mc "先輩達の仇、僕が取る！"
    hide mc

    call stage1_5


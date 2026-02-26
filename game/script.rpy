screen skip_btn(skip_label):
    textbutton "SKIP":
        align (0.9, 0.1)
        action [Hide("storyscroll"), Hide("skip_btn"), Jump("home")]


transform scroll_up:
    yoffset 1200
    linear 200 yoffset -8000


screen storyscroll():


    frame:
        background None 
        xfill True
        yfill True

        vbox:
            at scroll_up
            xalign 0.5
            spacing 50

            text """
                これは、とある大学の、

                とある日本語321の教室で起きたーー

                悲劇の物語である。





                XXは、世界規模の企業を率いるCEOの一人息子である。

                彼は赤ん坊の頃から、

                まるで皇帝のような生活を送り、

                欲しいものはすべて手に入れ、

                苦労というものを一切知らずに育ってきた。





                ……が！

                ある日突然、彼はこう宣言した。

                「俺様は日本語教師になる！」





                その後の出来事は、想像に難くない。

                家族の権力を使い、

                元の日本語321の教師の姿を消し、

                気がつけば、XXがその教壇に立っていたのである。





                しかし

                彼の日本語は中途半端そのものだった。

                文法は怪しく、使い方も不自然。



                それにもかかわらず、

                彼は自分の間違いには気づかず、

                生徒の些細なミスだけは決して見逃さない。



                間違いを指摘しては笑い、

                恥をかかせ、

                教室は次第に恐怖の場と化していった。




                日本語を聞くだけで吐き気を覚えるようになった学生も、

                一人や二人ではない。





                ……だが、物語はここで終わらない、終わってたまるか！！



                今学期の学生たちは違った。

                恐れを知らぬ者たちーー

                文法を知り尽くした者たちである。





                彼らは立ち上がる。


                教師の発言を一文一文読み取り、


                その中に紛れ込んだ不自然な文法の使い方を見つけ出す。


                正しく見える文の中にある、


                ただ一つの違和感ーー 





                これは、


                学生たちが自分の文法知識を武器に、


                愛する日本語、しあわせであった時間、


                みんなの日本語教室を取り戻す物語である。





                """:
                size 40
                bold True
                xalign 0.5
                color "#ffffff"


screen home_screen():
    modal True
    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 30
            xalign 0.5

            text "ステージ選択":
                size 70
                color "#fff"
                xalign 0.5

            textbutton "ステージ 1" action Jump("stage1") xalign 0.5
            textbutton "ステージ 2" action Jump("stage2") xalign 0.5
            textbutton "ステージ 3" action Jump("stage3") xalign 0.5
            # Add more stages as needed


screen stage_screen(sentences, correct, current_stage):
    modal True
    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 50
            text sentences[sentence_index]:
                size 60
                xalign 0.5
                color "#fff"

            hbox:
                spacing 20
                xalign 0.5
                textbutton "Previous" action SetVariable("sentence_index", 
                                                            (sentence_index - 1) % len(sentences))
                textbutton "Next" action SetVariable("sentence_index", 
                                                        (sentence_index + 1) % len(sentences))
                textbutton "Choose" action If(sentence_index == correct, 
                                                true=Jump("home_success"), 
                                                false=Jump(current_stage))


screen success_notification():
    frame:
        xalign 0.5
        yalign 0.3
        xpadding 50
        ypadding 20
        text "正解！おめでとう！" color "#fff" size 40


label home:
    call screen home_screen


label home_success:
    show screen success_notification
    $ renpy.pause(1.5)
    hide screen success_notification
    jump home

# Stage 1
label stage1:
    $ sentences = ["私は学生です。", "私は学生だ。", "私学生です。", "私は学生でした。", "私は学生じゃない。"]
    $ correct = 2  # index of the incorrect sentence (the one to choose)
    $ current_stage = "stage1"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 2
label stage2:
    $ sentences = ["昨日、映画を見た。", "昨日、映画を見ました。", "昨日、映画を見るた。", "昨日、映画を見ている。", "昨日、映画を見たい。"]
    $ correct = 2
    $ current_stage = "stage2"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 3
label stage3:
    $ sentences = ["これは本です。", "これは本だ。", "これ本です。", "これは本でした。", "これは本じゃない。"]
    $ correct = 2
    $ current_stage = "stage3"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


label start:
    scene bg classroom2
    
    show screen storyscroll
    show screen skip_btn("home")

    $ renpy.pause(180, hard=True)

    hide screen storyscroll
    hide screen skip_btn

    jump home   
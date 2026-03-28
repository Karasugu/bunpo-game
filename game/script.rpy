init python:
    renpy.tag_quoting_dict["kw"] = ("{color=#f9a825}", "{/color}")

screen skip_btn(skip_label):
    textbutton "SKIP":
        align (0.9, 0.1)
        action [Hide("storyscroll"), Hide("skip_btn"), Jump("home")]


transform scroll_up:
    yoffset 1000
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

            textbutton "ステージ 1":
                xalign 0.5
                action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
            textbutton "ステージ 2":
                xalign 0.5
                action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
            textbutton "ステージ 3":
                xalign 0.5
                action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
            textbutton "ステージ 4":
                xalign 0.5
                action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
            textbutton "ステージ 5":
                xalign 0.5
                action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
            textbutton "ステージ 6":
                xalign 0.5
                action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
            textbutton "ステージ 7":
                xalign 0.5
                action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
            textbutton "ステージ 8":
                xalign 0.5
                action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

label initStage:
    $ livesLeft = 3
    jump expression stageName

screen stage_screen(sentences, correct, current_stage):
    modal True
    add "bg dark":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

    frame:
        background None
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 50
            text sentences[sentence_index]:
                size 100
                xalign 0.5
                color "#fff"

            hbox:
                spacing 20
                xalign 0.5
                textbutton "Previous" action SetVariable("sentence_index", 
                                                            (sentence_index - 1) % len(sentences))
                textbutton "Next" action SetVariable("sentence_index", 
                                                        (sentence_index + 1) % len(sentences))
                textbutton "Choose" action [Hide("stage_screen"), Jump("choose_dia")]


# screen success_notification(explanation):
#     frame:
#         xalign 0.5
#         yalign 0.3
#         xpadding 50
#         ypadding 20

#         vbox:
#             spacing 20
#             xalign 0.5
#             text "正解！おめでとう！" color "#fff" size 40
#             textbutton "解説" xalign 0.5 action [Hide("success_notification"), Jump(explanation)]

            
# screen failure_notification(current_stage):
#     frame:
#         xalign 0.5
#         yalign 0.3
#         xpadding 50
#         ypadding 20
#         vbox:
#             spacing 20
#             xalign 0.5
#             textbutton "もう一度" xalign 0.5 action [Hide("failure_notification"), Jump(current_stage)]

label home:
    call screen home_screen

label start:
    scene bg blured
    
    show screen storyscroll
    show screen skip_btn("home")

    $ renpy.pause(180, hard=True)

    hide screen storyscroll
    hide screen skip_btn

    jump home   
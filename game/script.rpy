transform bg_full:
    xalign 0.5
    yalign 0.5
    xsize 1920
    ysize 1080

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

                「俺様は世界一の日本語教師になる！」




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


screen home_screen:
    modal True
    frame:
        background None
        xalign 0.5
        yalign 0.25

        text "文法教室３２１":
            size 100
            bold True
            color "#f5f3f3"
            xalign 0.5
            yalign 0.5


transform buttonScrollLeft:
    xoffset 0
    linear 0.25 xoffset -260

transform buttonScrollRight:
    xoffset 0
    linear 0.25 xoffset 260

#initial titleMenuButtons screen
screen titleMenuButtons:
    $ currentMenuButtonScreen = "titleMenuButtons"
    $ lastMenuButtonPosition = "stage1"
    if stage1_4cleared == True:
        textbutton "→":
            text_size 45
            xalign 0.65
            yalign 0.65
            action [SetVariable("lastMenuButtonPosition", "stage2"), Show("titleMenuButtonsLeft1"), Hide("titleMenuButtons")]
    textbutton "ステージ 1":
        text_size 35
        xalign 0.5
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.75
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.90
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_5cleared == True:
        textbutton "ステージ 18":
            text_size 35
            xalign 3.05
            yalign 0.5
            action [SetVariable("stageName", "stage1_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_6cleared == True:
        textbutton "ステージ 19":
            text_size 35
            xalign 3.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_6cleared == True:
        textbutton "ステージ 20":
            text_size 35
            xalign 3.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_6cleared == True:
        textbutton "ステージ 21":
            text_size 35
            xalign 3.50
            yalign 0.5
            action [SetVariable("stageName", "stage4_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_6cleared == True:
        textbutton "ステージ 22":
            text_size 35
            xalign 3.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_6cleared == True:
        textbutton "ステージ 23":
            text_size 35
            xalign 3.80
            yalign 0.5
            action [SetVariable("stageName", "stage6_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_6cleared == True:
        textbutton "ステージ 24":
            text_size 35
            xalign 3.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_6cleared == True:
        textbutton "ステージ 25":
            text_size 35
            xalign 4.10
            yalign 0.5
            action [SetVariable("stageName", "stage8_6"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_6cleared == True:
        textbutton "ステージ 26":
            text_size 35
            xalign 4.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_6"), Hide(currentMenuButtonScreen), Jump("initStage")]


label initStage:
    $ livesLeft = 3
    hide screen home_screen
    jump expression stageName

screen stage_screen(sentences, correct, current_stage):
    modal True
    add "bg blured":
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 700
        background "#0201018d"
        xpadding 40
        ypadding 40

        text sentences[sentence_index]:
            size 100
            xalign 0.5
            yalign 0.5
            color "#fff"
            text_align 0.5

    if livesLeft == 3:
        add "heartFull.png" as heart1:
            xalign 0.05
            yalign 0.05
        add "heartFull.png" as heart2:
            xalign 0.10
            yalign 0.05
        add "heartFull.png" as heart3:
            xalign 0.15
            yalign 0.05
    elif livesLeft == 2:
        add "heartFull.png" as heart1:
            xalign 0.05
            yalign 0.05
        add "heartFull.png" as heart2:
            xalign 0.10
            yalign 0.05
        add "heartEmpty.png" as heart3:
            xalign 0.15
            yalign 0.05
    elif livesLeft == 1:
        add "heartFull.png" as heart1:
            xalign 0.05
            yalign 0.05
        add "heartEmpty.png" as heart2:
            xalign 0.10
            yalign 0.05
        add "heartEmpty.png" as heart3:
            xalign 0.15
            yalign 0.05


    textbutton "Choose":
        xalign 0.95
        yalign 0.05
        text_size 35
        action [SetVariable("current_stage", current_stage), Hide("stage_screen"), Jump("choose_dia")]

    hbox:
        spacing 20
        xalign 0.5
        yalign 0.95
        textbutton "Previous":
            text_size 35
            action SetVariable("sentence_index",
                                (sentence_index - 1) % len(sentences))
        textbutton "Next":
            text_size 35
            action If(
                sentence_index == 4,
                [Hide("stage_screen"), Jump("next_wrap_dia")],
                SetVariable("sentence_index", (sentence_index + 1) % len(sentences))
            )


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
#    if returnFromStage != True:
#        $ stage1Buttonxalign = 0.5
#        $ stage2Buttonxalign = 0.65
#        $ stage3Buttonxalign = 0.8
#        $ stage4Buttonxalign = 0.95
#        $ stage5Buttonxalign = 1.1
#        $ stage6Buttonxalign = 1.25
#        $ stage7Buttonxalign = 1.40
#        $ stage8Buttonxalign = 1.55
#        $ stage9Buttonxalign = 1.70
#        $ stage10Buttonxalign = 1.85
#        $ stage11Buttonxalign = 2.0
#        $ stage12Buttonxalign = 2.15
#        $ stage13Buttonxalign = 2.30
#        $ stage14Buttonxalign = 2.45
#        $ stage15Buttonxalign = 2.60
#        $ stage16Buttonxalign = 2.75
#        $ stage17Buttonxalign = 2.90
#        $ stage18Buttonxalign = 3.05
#        $ stage19Buttonxalign = 3.20
#        $ stage20Buttonxalign = 3.35
#        $ stage21Buttonxalign = 3.50
#        $ stage22Buttonxalign = 3.65
#        $ stage23Buttonxalign = 3.80
#        $ stage24Buttonxalign = 3.95
#        $ stage25Buttonxalign = 4.10
#        $ stage26Buttonxalign = 4.25
    show screen home_screen
    if lastMenuButtonPosition == "stage1":
        call screen titleMenuButtons
    if lastMenuButtonPosition == "stage2":
        call screen titleMenuButtons1
    if lastMenuButtonPosition == "stage3":
        call screen titleMenuButtons2
    if lastMenuButtonPosition == "stage4":
        call screen titleMenuButtons3
    if lastMenuButtonPosition == "stage5":
        call screen titleMenuButtons4
    if lastMenuButtonPosition == "stage6":
        call screen titleMenuButtons5
    if lastMenuButtonPosition == "stage7":
        call screen titleMenuButtons6
    if lastMenuButtonPosition == "stage8":
        call screen titleMenuButtons7
    if lastMenuButtonPosition == "stage9":
        call screen titleMenuButtons8
    if lastMenuButtonPosition == "stage10":
        call screen titleMenuButtons9
    if lastMenuButtonPosition == "stage11":
        call screen titleMenuButtons10
    if lastMenuButtonPosition == "stage12":
        call screen titleMenuButtons11
    if lastMenuButtonPosition == "stage13":
        call screen titleMenuButtons12
    if lastMenuButtonPosition == "stage14":
        call screen titleMenuButtons13
    if lastMenuButtonPosition == "stage15":
        call screen titleMenuButtons14
    if lastMenuButtonPosition == "stage16":
        call screen titleMenuButtons15
    if lastMenuButtonPosition == "stage17":
        call screen titleMenuButtons16
    if lastMenuButtonPosition == "stage18":
        call screen titleMenuButtons17
    if lastMenuButtonPosition == "stage19":
        call screen titleMenuButtons18
    if lastMenuButtonPosition == "stage20":
        call screen titleMenuButtons19
    if lastMenuButtonPosition == "stage21":
        call screen titleMenuButtons20
    if lastMenuButtonPosition == "stage22":
        call screen titleMenuButtons21
    if lastMenuButtonPosition == "stage23":
        call screen titleMenuButtons22
    if lastMenuButtonPosition == "stage24":
        call screen titleMenuButtons23
    if lastMenuButtonPosition == "stage25":
        call screen titleMenuButtons24
    if lastMenuButtonPosition == "stage26":
        call screen titleMenuButtons25
    else:
        call screen titleMenuButtons
#    call screen home_screen

label start:
    $ lastMenuButtonPosition = False
    $ returnFromStage = False
    $ stage1_4cleared = False
    $ stage2_4cleared = False
    $ stage3_4cleared = False
    $ stage4_4cleared = False
    $ stage5_4cleared = False
    $ stage6_4cleared = False
    $ stage7_4cleared = False
    $ stage8_4cleared = False
    $ stage9_4cleared = False
    $ stage1_5cleared = False
    $ stage2_5cleared = False
    $ stage3_5cleared = False
    $ stage4_5cleared = False
    $ stage5_5cleared = False
    $ stage6_5cleared = False
    $ stage7_5cleared = False
    $ stage8_5cleared = False
    $ stage1_6cleared = False
    $ stage2_6cleared = False
    $ stage3_6cleared = False
    $ stage4_6cleared = False
    $ stage5_6cleared = False
    $ stage6_6cleared = False
    $ stage7_6cleared = False
    $ stage8_6cleared = False
    $ stage9_6cleared = False
    scene bg blured
    show bg blured at bg_full

    show screen storyscroll
    show screen skip_btn("home")

    $ renpy.pause(170, hard=True)

    hide screen storyscroll
    hide screen skip_btn

    jump home

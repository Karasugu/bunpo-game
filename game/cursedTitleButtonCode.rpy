#No one should EVER replicate this code or take it as reference, it is the bodge of bodges.
#need stage counter
#store xaligns
#store last menu position

#scroll to left
screen titleMenuButtonsLeft1:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft1"
    if stage2_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage3"), Show("titleMenuButtonsLeft2"), Hide("titleMenuButtonsLeft1")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtonsLeft1")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign 0.5
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.75
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.90
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft2:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft2"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage4"), Show("titleMenuButtonsLeft3"), Hide("titleMenuButtonsLeft2")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage2"), Show("titleMenuButtonsRight1"), Hide("titleMenuButtonsLeft2")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign 0.35
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.75
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft3:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft3"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage5"), Show("titleMenuButtonsLeft4"), Hide("titleMenuButtonsLeft3")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage3"), Show("titleMenuButtonsRight2"), Hide("titleMenuButtonsLeft3")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign 0.20
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft4:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft4"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage6"), Show("titleMenuButtonsLeft5"), Hide("titleMenuButtonsLeft4")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage4"), Show("titleMenuButtonsRight3"), Hide("titleMenuButtonsLeft4")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign 0.05
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft5:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft5"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage7"), Show("titleMenuButtonsLeft6"), Hide("titleMenuButtonsLeft5")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage5"), Show("titleMenuButtonsRight4"), Hide("titleMenuButtonsLeft5")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.10
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft6:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft6"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage8"), Show("titleMenuButtonsLeft7"), Hide("titleMenuButtonsLeft6")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage6"), Show("titleMenuButtonsRight5"), Hide("titleMenuButtonsLeft6")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.25
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft7:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft7"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage9"), Show("titleMenuButtonsLeft8"), Hide("titleMenuButtonsLeft7")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage7"), Show("titleMenuButtonsRight6"), Hide("titleMenuButtonsLeft7")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.40
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft8:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft8"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage10"), Show("titleMenuButtonsLeft9"), Hide("titleMenuButtonsLeft8")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage8"), Show("titleMenuButtonsRight7"), Hide("titleMenuButtonsLeft8")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.55
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft9:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft9"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage11"), Show("titleMenuButtonsLeft10"), Hide("titleMenuButtonsLeft9")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage9"), Show("titleMenuButtonsRight8"), Hide("titleMenuButtonsLeft9")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.70
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft10:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft10"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage12"), Show("titleMenuButtonsLeft11"), Hide("titleMenuButtonsLeft10")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage10"), Show("titleMenuButtonsRight9"), Hide("titleMenuButtonsLeft10")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -0.85
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft11:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft11"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage13"), Show("titleMenuButtonsLeft12"), Hide("titleMenuButtonsLeft11")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage11"), Show("titleMenuButtonsRight10"), Hide("titleMenuButtonsLeft11")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.0
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft12:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft12"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage14"), Show("titleMenuButtonsLeft13"), Hide("titleMenuButtonsLeft12")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage12"), Show("titleMenuButtonsRight11"), Hide("titleMenuButtonsLeft12")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.15
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft13:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft13"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage15"), Show("titleMenuButtonsLeft14"), Hide("titleMenuButtonsLeft13")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage13"), Show("titleMenuButtonsRight12"), Hide("titleMenuButtonsLeft13")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.30
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft14:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft14"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage16"), Show("titleMenuButtonsLeft15"), Hide("titleMenuButtonsLeft14")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage14"), Show("titleMenuButtonsRight13"), Hide("titleMenuButtonsLeft14")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.45
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft15:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft15"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage17"), Show("titleMenuButtonsLeft16"), Hide("titleMenuButtonsLeft15")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage15"), Show("titleMenuButtonsRight14"), Hide("titleMenuButtonsLeft15")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.60
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsLeft16:
    $ currentMenuButtonScreen = "titleMenuButtonsLeft16"
#    if stage3_4cleared == True:
#        textbutton "Left":
#            text_size 35
#            xalign 0.25
#            yalign 0.9
#            action [SetVariable("lastMenuButtonPosition", "stage17"), Show("titleMenuButtonsLeft16"), Hide("titleMenuButtonsLeft15")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage16"), Show("titleMenuButtonsRight15"), Hide("titleMenuButtonsLeft16")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign -1.75
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign -1.60
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]



#centre buttons

screen titleMenuButtons1:
    $ currentMenuButtonScreen = "titleMenuButtons1"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage3"), Show("titleMenuButtons2"), Hide("titleMenuButtons1")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign 0.35
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.75
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons2:
    $ currentMenuButtonScreen = "titleMenuButtons2"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage4"), Show("titleMenuButtons3"), Hide("titleMenuButtons2")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign 0.20
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons3:
    $ currentMenuButtonScreen = "titleMenuButtons3"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage5"), Show("titleMenuButtons4"), Hide("titleMenuButtons3")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign 0.05
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons4:
    $ currentMenuButtonScreen = "titleMenuButtons4"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage6"), Show("titleMenuButtons5"), Hide("titleMenuButtons4")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.10
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons5:
    $ currentMenuButtonScreen = "titleMenuButtons5"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage7"), Show("titleMenuButtons6"), Hide("titleMenuButtons5")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.25
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons6:
    $ currentMenuButtonScreen = "titleMenuButtons6"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage8"), Show("titleMenuButtons7"), Hide("titleMenuButtons6")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.40
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons7:
    $ currentMenuButtonScreen = "titleMenuButtons7"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage9"), Show("titleMenuButtons8"), Hide("titleMenuButtons7")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.55
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons8:
    $ currentMenuButtonScreen = "titleMenuButtons8"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage10"), Show("titleMenuButtons9"), Hide("titleMenuButtons8")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.70
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons9:
    $ currentMenuButtonScreen = "titleMenuButtons9"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage11"), Show("titleMenuButtons10"), Hide("titleMenuButtons9")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -0.85
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons10:
    $ currentMenuButtonScreen = "titleMenuButtons10"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage12"), Show("titleMenuButtons11"), Hide("titleMenuButtons10")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.0
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons11:
    $ currentMenuButtonScreen = "titleMenuButtons11"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage13"), Show("titleMenuButtons12"), Hide("titleMenuButtons11")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.15
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons12:
    $ currentMenuButtonScreen = "titleMenuButtons12"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage14"), Show("titleMenuButtons13"), Hide("titleMenuButtons12")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.30
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons13:
    $ currentMenuButtonScreen = "titleMenuButtons13"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage15"), Show("titleMenuButtons14"), Hide("titleMenuButtons13")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.45
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons14:
    $ currentMenuButtonScreen = "titleMenuButtons14"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage16"), Show("titleMenuButtons15"), Hide("titleMenuButtons14")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.60
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 0.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons15:
    $ currentMenuButtonScreen = "titleMenuButtons15"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage17"), Show("titleMenuButtons16"), Hide("titleMenuButtons15")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.75
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.60
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtons16:
    $ currentMenuButtonScreen = "titleMenuButtons16"
#    if stage3_4cleared == True:
#        textbutton "Left":
#            text_size 35
#            xalign 0.25
#            yalign 0.9
#            action [SetVariable("lastMenuButtonPosition", "stage17"), Show("titleMenuButtons16"), Hide("titleMenuButtons15")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtons1")]
    textbutton "ステージ 1":
        text_size 35
        xalign -1.75
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2":
            text_size 35
            xalign -1.75
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3":
            text_size 35
            xalign -1.60
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4":
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5":
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6":
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7":
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8":
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9":
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10":
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11":
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12":
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13":
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14":
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15":
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16":
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17":
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]


#scroll to right
screen titleMenuButtonsRight:
    $ currentMenuButtonScreen = "titleMenuButtonsRight"
    if stage1_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage2"), Show("titleMenuButtonsLeft1"), Hide("titleMenuButtonsRight")]
#    textbutton "Right":
#        text_size 35
#        xalign 0.75
#        yalign 0.9
#        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtonsRight1")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign 0.35
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.75
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight1:
    $ currentMenuButtonScreen = "titleMenuButtonsRight1"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage3"), Show("titleMenuButtonsLeft2"), Hide("titleMenuButtonsRight1")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage1"), Show("titleMenuButtonsRight"), Hide("titleMenuButtonsRight1")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign 0.20
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.60
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight2:
    $ currentMenuButtonScreen = "titleMenuButtonsRight2"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage4"), Show("titleMenuButtonsLeft3"), Hide("titleMenuButtonsRight2")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage2"), Show("titleMenuButtonsRight1"), Hide("titleMenuButtonsRight2")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign 0.05
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.45
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight3:
    $ currentMenuButtonScreen = "titleMenuButtonsRight3"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage5"), Show("titleMenuButtonsLeft4"), Hide("titleMenuButtonsRight3")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage3"), Show("titleMenuButtonsRight2"), Hide("titleMenuButtonsRight3")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.10
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.30
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight4:
    $ currentMenuButtonScreen = "titleMenuButtonsRight4"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage6"), Show("titleMenuButtonsLeft5"), Hide("titleMenuButtonsRight4")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage4"), Show("titleMenuButtonsRight3"), Hide("titleMenuButtonsRight4")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.25
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.5
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.15
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight5:
    $ currentMenuButtonScreen = "titleMenuButtonsRight5"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage7"), Show("titleMenuButtonsLeft8"), Hide("titleMenuButtonsRight5")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage5"), Show("titleMenuButtonsRight4"), Hide("titleMenuButtonsRight5")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.40
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 2.0
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight6:
    $ currentMenuButtonScreen = "titleMenuButtonsRight6"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage8"), Show("titleMenuButtonsLeft7"), Hide("titleMenuButtonsRight6")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage6"), Show("titleMenuButtonsRight5"), Hide("titleMenuButtonsRight6")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.55
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.85
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight7:
    $ currentMenuButtonScreen = "titleMenuButtonsRight7"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage9"), Show("titleMenuButtonsLeft8"), Hide("titleMenuButtonsRight7")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage7"), Show("titleMenuButtonsRight6"), Hide("titleMenuButtonsRight7")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.70
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.8
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight8:
    $ currentMenuButtonScreen = "titleMenuButtonsRight8"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage10"), Show("titleMenuButtonsLeft9"), Hide("titleMenuButtonsRight8")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage8"), Show("titleMenuButtonsRight7"), Hide("titleMenuButtonsRight8")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -0.85
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight9:
    $ currentMenuButtonScreen = "titleMenuButtonsRight9"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage11"), Show("titleMenuButtonsLeft10"), Hide("titleMenuButtonsRight9")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage9"), Show("titleMenuButtonsRight8"), Hide("titleMenuButtonsRight9")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.0
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight10:
    $ currentMenuButtonScreen = "titleMenuButtonsRight10"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage12"), Show("titleMenuButtonsLeft11"), Hide("titleMenuButtonsRight10")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage10"), Show("titleMenuButtonsRight9"), Hide("titleMenuButtonsRight10")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.15
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight11:
    $ currentMenuButtonScreen = "titleMenuButtonsRight11"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage13"), Show("titleMenuButtonsLeft12"), Hide("titleMenuButtonsRight11")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage11"), Show("titleMenuButtonsRight10"), Hide("titleMenuButtonsRight11")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.30
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 1.1
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight12:
    $ currentMenuButtonScreen = "titleMenuButtonsRight12"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage14"), Show("titleMenuButtonsLeft13"), Hide("titleMenuButtonsRight12")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage12"), Show("titleMenuButtonsRight11"), Hide("titleMenuButtonsRight12")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.45
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign -0.1
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 0.95
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight13:
    $ currentMenuButtonScreen = "titleMenuButtonsRight13"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage15"), Show("titleMenuButtonsRight14"), Hide("titleMenuButtonsRight13")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage13"), Show("titleMenuButtonsRight12"), Hide("titleMenuButtonsRight13")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.60
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight14:
    $ currentMenuButtonScreen = "titleMenuButtonsRight14"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage16"), Show("titleMenuButtonsLeft15"), Hide("titleMenuButtonsRight14")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage14"), Show("titleMenuButtonsRight13"), Hide("titleMenuButtonsRight14")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.75
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.60
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

screen titleMenuButtonsRight15:
    $ currentMenuButtonScreen = "titleMenuButtonsRight15"
    if stage3_4cleared == True:
        textbutton "Left":
            text_size 35
            xalign 0.25
            yalign 0.9
            action [SetVariable("lastMenuButtonPosition", "stage17"), Show("titleMenuButtonsLeft16"), Hide("titleMenuButtonsRight15")]
    textbutton "Right":
        text_size 35
        xalign 0.75
        yalign 0.9
        action [SetVariable("lastMenuButtonPosition", "stage15"), Show("titleMenuButtonsRight14"), Hide("titleMenuButtonsRight15")]
    textbutton "ステージ 1" at buttonScrollRight:
        text_size 35
        xalign -1.60
        yalign 0.5
        action [SetVariable("stageName", "start1"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollRight:
            text_size 35
            xalign -1.45
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollRight:
            text_size 35
            xalign -1.30
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollRight:
            text_size 35
            xalign -1.15
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollRight:
            text_size 35
            xalign -1.0
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollRight:
            text_size 35
            xalign -0.85
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollRight:
            text_size 35
            xalign -0.70
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollRight:
            text_size 35
            xalign -0.55
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollRight:
            text_size 35
            xalign -0.40
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollRight:
            text_size 35
            xalign -0.25
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollRight:
            text_size 35
            xalign -0.10
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollRight:
            text_size 35
            xalign 0.05
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollRight:
            text_size 35
            xalign 0.20
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollRight:
            text_size 35
            xalign 0.35
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollRight:
            text_size 35
            xalign 0.50
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollRight:
            text_size 35
            xalign 0.65
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Hide(currentMenuButtonScreen), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollRight:
            text_size 35
            xalign 0.80
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Hide(currentMenuButtonScreen), Jump("initStage")]

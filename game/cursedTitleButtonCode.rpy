#No one should EVER replicate this code or take it as reference, it is the bodge of bodges.
#need stage counter
#store xaligns
#store last menu position

#scroll to left
screen titleMenuButtonsLeft1:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft2"), Hide("titleMenuButtonsLeft1")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft2:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft3"), Hide("titleMenuButtonsLeft2")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft3:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft4"), Hide("titleMenuButtonsLeft3")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft4:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft5"), Hide("titleMenuButtonsLeft4")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft5:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft6"), Hide("titleMenuButtonsLeft5")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft6:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft7"), Hide("titleMenuButtonsLeft6")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft7:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft8"), Hide("titleMenuButtonsLeft7")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft8:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft9"), Hide("titleMenuButtonsLeft8")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft9:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft10"), Hide("titleMenuButtonsLeft9")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft10:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft11"), Hide("titleMenuButtonsLeft10")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft11:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft12"), Hide("titleMenuButtonsLeft11")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft12:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft13"), Hide("titleMenuButtonsLeft12")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft13:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft14"), Hide("titleMenuButtonsLeft13")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft14:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft15"), Hide("titleMenuButtonsLeft14")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft15:
    textbutton "Left":
        text_size 35
        xalign 0.25
        yalign 0.9
        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft16"), Hide("titleMenuButtonsLeft15")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]

screen titleMenuButtonsLeft16:
#    textbutton "Left":
#        text_size 35
#        xalign 0.25
#        yalign 0.9
#        action [SetVariable("stage1Buttonxalign", stage1Buttonxalign - 0.15), SetVariable("stage2Buttonxalign", stage2Buttonxalign - 0.15), SetVariable("stage3Buttonxalign", stage3Buttonxalign - 0.15), SetVariable("stage4Buttonxalign", stage4Buttonxalign - 0.15), SetVariable("stage5Buttonxalign", stage5Buttonxalign - 0.15), SetVariable("stage6Buttonxalign", stage6Buttonxalign - 0.15), SetVariable("stage7Buttonxalign", stage7Buttonxalign - 0.15), SetVariable("stage8Buttonxalign", stage8Buttonxalign - 0.15), SetVariable("stage9Buttonxalign", stage9Buttonxalign - 0.15), SetVariable("stage10Buttonxalign", stage10Buttonxalign - 0.15), SetVariable("stage11Buttonxalign", stage11Buttonxalign - 0.15), SetVariable("stage12Buttonxalign", stage12Buttonxalign - 0.15), SetVariable("stage13Buttonxalign", stage13Buttonxalign - 0.15), SetVariable("stage14Buttonxalign", stage14Buttonxalign - 0.15), SetVariable("stage15Buttonxalign", stage15Buttonxalign - 0.15), SetVariable("stage16Buttonxalign", stage16Buttonxalign - 0.15), SetVariable("stage17Buttonxalign", stage17Buttonxalign - 0.15), Show("titleMenuButtonsLeft17"), Hide("titleMenuButtonsLeft16")]
    textbutton "ステージ 1" at buttonScrollLeft:
        text_size 35
        xalign stage1Buttonxalign
        yalign 0.5
        action [SetVariable("stageName", "start1"), Jump("initStage")]
    if stage1_4cleared == True:
        textbutton "ステージ 2" at buttonScrollLeft:
            text_size 35
            xalign stage2Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_4"), Jump("initStage")]
    if stage2_4cleared == True:
        textbutton "ステージ 3" at buttonScrollLeft:
            text_size 35
            xalign stage3Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_4"), Jump("initStage")]
    if stage3_4cleared == True:
        textbutton "ステージ 4" at buttonScrollLeft:
            text_size 35
            xalign stage4Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_4"), Jump("initStage")]
    if stage4_4cleared == True:
        textbutton "ステージ 5" at buttonScrollLeft:
            text_size 35
            xalign stage5Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_4"), Jump("initStage")]
    if stage5_4cleared == True:
        textbutton "ステージ 6" at buttonScrollLeft:
            text_size 35
            xalign stage6Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_4"), Jump("initStage")]
    if stage6_4cleared == True:
        textbutton "ステージ 7" at buttonScrollLeft:
            text_size 35
            xalign stage7Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_4"), Jump("initStage")]
    if stage7_4cleared == True:
        textbutton "ステージ 8" at buttonScrollLeft:
            text_size 35
            xalign stage8Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_4"), Jump("initStage")]
    if stage8_4cleared == True:
        textbutton "ステージ 9" at buttonScrollLeft:
            text_size 35
            xalign stage9Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage9_4"), Jump("initStage")]
    if stage9_4cleared == True:
        textbutton "ステージ 10" at buttonScrollLeft:
            text_size 35
            xalign stage10Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage1_5"), Jump("initStage")]
    if stage1_5cleared == True:
        textbutton "ステージ 11" at buttonScrollLeft:
            text_size 35
            xalign stage11Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage2_5"), Jump("initStage")]
    if stage2_5cleared == True:
        textbutton "ステージ 12" at buttonScrollLeft:
            text_size 35
            xalign stage12Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage3_5"), Jump("initStage")]
    if stage3_5cleared == True:
        textbutton "ステージ 13" at buttonScrollLeft:
            text_size 35
            xalign stage13Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage4_5"), Jump("initStage")]
    if stage4_5cleared == True:
        textbutton "ステージ 14" at buttonScrollLeft:
            text_size 35
            xalign stage14Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage5_5"), Jump("initStage")]
    if stage5_5cleared == True:
        textbutton "ステージ 15" at buttonScrollLeft:
            text_size 35
            xalign stage15Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage6_5"), Jump("initStage")]
    if stage6_5cleared == True:
        textbutton "ステージ 16" at buttonScrollLeft:
            text_size 35
            xalign stage16Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage7_5"), Jump("initStage")]
    if stage7_5cleared == True:
        textbutton "ステージ 17" at buttonScrollLeft:
            text_size 35
            xalign stage17Buttonxalign
            yalign 0.5
            action [SetVariable("stageName", "stage8_5"), Jump("initStage")]





#scroll to right

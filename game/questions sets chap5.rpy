# Stage 1 ～ても
label stage1:
    call dialogue1
    
    $ sentences = ["私は学生です。", "私は学生だ。", "私学生です。", "私は学生でした。", "私は学生じゃない。"]
    $ correct = 2  # index of the incorrect sentence (the one to choose)
    $ current_stage = "stage1"
    $ explanation =  "stage1_explanation"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 2 ～たび
label stage2:
    $ sentences = [
    "この映画を見るたびに、泣いてしまいます。", 
    "ご飯を食べるたびに、テレビを見ます。", 
    "スーパーに行くたびに、いらないものを買いすぎてしまいます", 
    "富士山を見るたびに、その美しさを感じます。", 
    "このレストランに行くたびに、つい同じものを注文してしまいます。"]
    $ correct = 1
    $ current_stage = "stage2"
    $ explanation =  "stage2_explanation"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 3 ～はずだ
label stage3:
    $ sentences = [
    "私は日本に留学したことがあるので、日本語が話せるはずです。", 
    "まだ早いので、あの店はまだ開いているはずです。", 
    "ケーキを持って行ったら絵理さんは喜ぶはずです。", 
    "友達と山に登るはずでしたが、雨で行けなくなりました。", 
    "研さんはもうすぐ着くはずだそうです。"]
    $ correct = 0
    $ current_stage = "stage3"
    $ explanation =  "stage3_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 4 ～ておく/～ないでおく
label stage4:
    $ sentences = [
    "これから忙しくなりそうなので、来週の宿題をしておきます。", 
    "友達が遊びにくるので、お菓子を買っておきました。", 
    "遅刻したくないので、10分早く家を出ておきます。", 
    "メアリーさんも来るかもしれないので、5人のテーブルを予約しておきました。", 
    "遅くなったので、友達が帰っておきました。"]
    $ correct = 4
    $ current_stage = "stage4"
    $ explanation =  "stage4_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 5  （もし）～ても
label stage5:
    $ sentences = [
    "例えテストで悪い点を取っても、落ち込みません。", 
    "もし雨が降っても、家でゲームをします。", 
    "おいしくても、そうでなくても、必ず大将に「いや、うまいよ！大将！」と言います。", 
    "今日勉強しなくても、まだ時間があります。", 
    "教室が遠すぎて、走っても間に合いません。"]
    $ correct = 1
    $ current_stage = "stage5"
    $ explanation =  "stage5_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 6  ～ように
label stage6:
    $ sentences = [
    "目が悪くならないように、夜にゲームをしないことにしています。", 
    "朝起きられるように、アラームを五つ設定しました。", 
    "先生の声が聞けるように、前の方に座ります。", 
    "肉がこげないように、火をよく調整しましょう。", 
    "かぜを引かないように、暖かいジャケットを着ます。"]
    $ correct = 2
    $ current_stage = "stage6"
    $ explanation =  "stage6_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 7  Nにする
label stage7:
    $ sentences = [
    "今日の晩ご飯はおすしにします。", 
    "パソコンを買うなら、ウインドウズにした方がいいですよ。", 
    "今の仕事をやめることにしました。", 
    "ゲームをするなら家事が終わってからにしてください。", 
    "週末、友達と出かけることにする予定です。"]
    $ correct = 4
    $ current_stage = "stage7"
    $ explanation =  "stage7_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 8  ～だけあって
label stage8:
    $ sentences = [
    "本田さんは野球部だけあって、足が速いです。", 
    "あのレストランはいつも込んでいるだけあって、待ち時間が長い。", 
    "サラは性格が明るいだけあって、友達が多い。", 
    "富士山はきれいなだけあって、観光客がとても多いです。", 
    "バンクーバーは公園が多いだけあって、空気がきれいです。"]
    $ correct = 1
    $ current_stage = "stage8"
    $ explanation =  "stage8_explanation" 
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Explanation to why sentence is incorrect
# Provide a short explanation to the correct bunpo usage as well
label stage1_explanation:
    "「私学生です。」は間違いです。「は」という助詞が必要です。"
    jump home

label stage2_explanation:
    "「見るた」は間違いです。動詞の過去形は「見た」です。"
    jump home

label stage3_explanation:
    "「これ本です。」は間違いです。「は」という助詞が必要です。"
    jump home



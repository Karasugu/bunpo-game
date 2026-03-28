# Stage 1 ～ても
label stage1_5:

    $ sentences = [
    "この料理、誰が食べても美味しいと思うはずです。",
    "この料理、どんな人でも作れます。",
    "この料理、どう見ても美味しいです。",
    "この料理、何を入れても美味しいです。",
    "この料理、どこの国に行ってもあります。"]
    $ correct = 2
    $ current_stage = "stage1_5"
    $ explanation = "「どう見ても」という表現はおかしいです。〜ても文型では、前半の条件が後半の結果に{color=#ff0000}関係{/color}している必要があります。料理の見た目と味は直接関係がないので、この文は不自然です。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 2 ～たび
label stage2_5:
    $ sentences = [
    "この映画を見るたびに、泣いてしまいます。",
    "ご飯を食べるたびに、テレビを見ます。",
    "スーパーに行くたびに、いらないものを買いすぎてしまいます。",
    "富士山を見るたびに、その美しさを感じます。",
    "このレストランに行くたびに、つい同じものを注文してしまいます。"]
    $ correct = 1
    $ current_stage = "stage2_5"
    $ explanation = "〜たびに文型では、後半は{color=#ff0000}自然{/color}と起こる結果や感情である必要があります。テレビを見るのは意識的な行動なので、この文は不自然です。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 3 ～はずだ
label stage3_5:
    $ sentences = [
    "私は日本に留学したことがあるので、日本語が話せるはずです。",
    "まだ早いので、あの店はまだ開いているはずです。",
    "ケーキを持って行ったら絵理さんは喜ぶはずです。",
    "友達と山に登るはずでしたが、雨で行けなくなりました。",
    "研さんはもうすぐ着くはずだそうです。"]
    $ correct = 0
    $ current_stage = "stage3_5"
    $ explanation = "「日本語が話せるはずです」という表現はおかしいです。はずですは、他のことについて{color=#ff0000}推測 (すいそく){/color}をするときに使います。しかし、自分自身のことは100％わかるはずなので、自分のことに「はずです」を使うのは不自然です。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 4 ～ておく/～ないでおく
label stage4_5:
    $ sentences = [
    "これから忙しくなりそうなので、来週の宿題をしておきます。",
    "友達が遊びにくるので、お菓子を買っておきました。",
    "遅刻したくないので、10分早く家を出ておきます。",
    "メアリーさんも来るかもしれないので、5人のテーブルを予約しておきました。",
    "遅くなったので、友達が帰っておきました。"]
    $ correct = 4
    $ current_stage = "stage4_5"
    $ explanation = "「友達が帰っておきました」という表現はおかしいです。〜ておくは、何かに{color=#ff0000}備えて事前{/color}に行動することを表します。しかし「遅くなったので」は結果を表すので、準備の意味と合いません。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 5 （もし）～ても
label stage5_5:
    $ sentences = [
    "例えテストで悪い点を取っても、落ち込みません。",
    "もし雨が降っても、家でゲームをします。",
    "おいしくても、そうでなくても、必ず大将に「いや、うまいよ！大将！」と言います。",
    "今日勉強しなくても、まだ時間があります。",
    "教室が遠すぎて、走っても間に合いません。"]
    $ correct = 1
    $ current_stage = "stage5_5"
    $ explanation = "（もし）〜ても文型では、後半は前半の条件から{color=#ff0000}予想外（よそうがい）{/color}のことを表す必要があります。雨の日に家でゲームをするのは普通のことなので、この文はおかしいです。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 6 ～ように
label stage6_5:
    $ sentences = [
    "目が悪くならないように、夜にゲームをしないことにしています。",
    "朝起きられるように、アラームを五つ設定しました。",
    "先生の声が聞けるように、前の方に座ります。",
    "肉がこげないように、火をよく調整しましょう。",
    "かぜを引かないように、暖かいジャケットを着ます。"]
    $ correct = 2
    $ current_stage = "stage6_5"
    $ explanation = "「先生の声が聞けるように」という表現はおかしいです。〜ように文型では、前半には話し手の意志で{color=#ff0000}コントロールできない{/color}動詞を使う必要があります。「聞ける」は意志でコントロールできる動詞なので、「聞こえる」を使うべきです。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 7 Nにする
label stage7_5:
    $ sentences = [
    "今日の晩ご飯はおすしにします。",
    "パソコンを買うなら、ウインドウズにした方がいいですよ。",
    "今の仕事をやめることにしました。",
    "ゲームをするなら家事が終わってからにしてください。",
    "週末、友達と出かけることにする予定です。"]
    $ correct = 4
    $ current_stage = "stage7_5"
    $ explanation = "「ことにする予定です」という表現はおかしいです。ことにするはすでに{color=#ff0000}決めた{/color}ことを表し、予定ですはこれからの計画を表します。二つを一緒に使うと意味が重なってしまうので、不自然です。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 8 ～だけあって
label stage8_5:
    $ sentences = [
    "本田さんは野球部だけあって、足が速いです。",
    "あのレストランはいつも込んでいるだけあって、待ち時間が長い。",
    "サラは性格が明るいだけあって、友達が多い。",
    "富士山はきれいなだけあって、観光客がとても多いです。",
    "バンクーバーは公園が多いだけあって、空気がきれいです。"]
    $ correct = 1
    $ current_stage = "stage8_5"
    $ explanation = "「いつも込んでいるだけあって」という表現はおかしいです。〜だけあって文型では、前半には{color=#ff0000}ポジティブ{/color}な評価や特徴が来る必要があります。「いつも込んでいる」は良いことではないので、この文は不自然です。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)



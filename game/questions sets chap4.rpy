# Stage 1 ～以来
label stage1_4:

    $ sentences = [
    "来年高校を卒業して以来、日本に行くつもります。",
    "日本に来て以来、日本語の勉強を毎日続けています。",
    "高校を卒業して以来、彼とは会っていません。",
    "子どもが生まれて以来、生活が大きく変わりました。",
    "2019年以来、この会社で働いています。"]
    $ correct = 0
    $ current_stage = "stage1_4"
    $ explanation = "「来年高校を卒業して以来」という表現はおかしいです。〜以来の文型では、{color=#ff0000}すでに起きたこと{/color}である必要があります。「来年卒業する」はまだ起きていない未来のこと、そうだろうｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 2 ～ような気がする
label stage2_4:
    $ sentences = [
    "今日は昨日より寒いような気がします。",
    "彼は少し怒っているような気がする。",
    "この問題は前にも見たような気がします。",
    "今日は雨なような気がする。",
    "最近、物価が上がっているような気がする。"]
    $ correct = 3
    $ current_stage = "stage2_4"
    $ explanation = "「雨なような気がする」という表現はおかしいですよ。名詞に〜ような気がするをつける場合、{color=#ff0000}助詞を「の」にする{/color}必要があります。「雨なような」ではなく「雨のような」が正しいですよ、ｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 3 ～はずだ
label stage3_4:
    $ sentences = [
    "せっかく日本に来たのに、ずっと雨です。",
    "せっかく作った料理だから、全部食べてください。",
    "せっかくで毎日日本語を勉強している。",
    "せっかくのチャンスを逃してしまった。",
    "せっかく来てくれたんだから、ゆっくりしていってください。"]
    $ correct = 2
    $ current_stage = "stage3_4"
    $ explanation = "「せっかくで」という表現はおかしいです。せっかくの後に文が続く場合、{color=#ff0000}助詞をつけてはいけません{/color}。「せっかく＋文」の形が正しいので、「せっかくで」ではなく「せっかく毎日〜」にするべきです、そうだろうｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 4 ～さえ
label stage4_4:
    $ sentences = [
    "彼は自分の名前さえ書けません。",
    "私は外国語の勉強が好きなのに、タイ語さえ勉強したことがありません。",
    "遅お金さえあれば、世界旅行ができます。",
    "忙しくて、昼ご飯を食べる時間さえありません。",
    "時間さえあれば、その本を読みたいです。"]
    $ correct = 1
    $ current_stage = "stage4_4"
    $ explanation = "「タイ語さえ」という表現はおかしいです。〜さえの文型では、{color=#ff0000}一番低い基準（きじゅん）{/color}である必要があります。外国語学習においてタイ語は最も簡単なものとは言えないので、この文は不自然ですよ、ｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 5 ～たばかり
label stage5_4:
    $ sentences = [
    "今、昼ご飯を食べたばかりです。",
    "日本に来たばかりなので、日本語がまだ上手ではありません。",
    "私は三年前にこのサークルに入ったばかりです。",
    "彼は大学を卒業したばかりです。",
    "このスマホは昨日買ったばかりです。"]
    $ correct = 2
    $ current_stage = "stage5_4"
    $ explanation = "「三年前に入ったばかりです」という表現はおかしいです。〜たばかりの文型では、{color=#ff0000}つい最近起きたこと{/color}を表す必要があります。吸血鬼にとって三年前は最近だろうが、僕たち人間にとって三年前はとても最近だとは言えないじゃないですか。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 6 ～ないで済む/ずに済む
label stage6_4:
    $ sentences = [
    "日本に行かないで済みたいです。",
    "今日は先生が来なかったので、宿題を出さないで済みました。",
    "電車が動いたので、歩かずに済みました。",
    "タクシーを呼んだので、雨の中を歩かないで済みました。",
    "彼が手伝ってくれたので、一人でやらずに済みました。"]
    $ correct = 0
    $ current_stage = "stage6_4"
    $ explanation = "「行かないで済みたいです」という表現はおかしいです。〜ないで済むの文型は、{color=#ff0000}結果{/color}として何かを{color=#ff0000}しなくてもよくなったこと{/color}を表します。「〜たい」をつけて願望を表すことはできないので、この文は不自然です、ｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 7 ～ほど～ない
label stage7_4:
    $ sentences = [
    "この町は東京ほどにぎやかではありません。",
    "この問題は思ったほど難しくないです。",
    "今年の冬は去年ほど寒くありません。",
    "日本はカナダほど大きくない。",
    "彼は兄ほど背が高くない。"]
    $ correct = 3
    $ current_stage = "stage7_4"
    $ explanation = "「日本はカナダほど大きくない」という表現はおかしいです。〜ほど〜ないの文型では、比べる二つのものが{color=#ff0000}同じくらい{/color}のレベルである必要があります。カナダと日本の大きさは明らかに差がありすぎるので、この文は不自然です、そうだろうｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 8 ～わけだ
label stage8_4:
    $ sentences = [
    "天気予報が言っていたから、明日雨が降るわけだ。",
    "彼は10年間日本に住んでいたから、日本語が上手なわけだ。",
    "昨日は夜遅くまで勉強したから、今日は眠いわけだ。",
    "このレストランは有名なシェフが作っているから、どうりで美味しいわけだ。",
    "今日は祝日だから、銀行が閉まっているわけだ。"]
    $ correct = 0
    $ current_stage = "stage8_4"
    $ explanation = "「明日雨が降るわけだ」という表現はおかしいです。～わけだの文型では、{color=#ff0000}不思議に思っていたことの理由がわかった時{/color}に使います。天気予報は理由を発見する状況ではなく、ただの予測なので、この文は不自然ですよ、ｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 9 ～ば～のに
label stage9_4:
    $ sentences = [
    "もっと早く来ればよかったのに。",
    "分からなければ、先生に聞けばよかったのに。",
    "時間があれば、一緒に行ったのに。",
    "電車に乗れば間に合ったのに。",
    "明日寝坊しなければ行くのに。"]
    $ correct = 4
    $ current_stage = "stage9_4"
    $ explanation = "「明日寝坊しなければ行くのに」という表現はおかしいです。〜ば〜のにの文型では、{color=#ff0000}自分でコントロールできない{/color}ことである必要があります。明日寝坊するかどうかは別にコントロールできないわけじゃないですから、この文は不自然です、そうだろうｘｘ先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)
# Stage 1 ～（という）わけではない
label stage1_6:

    $ sentences = [
    "よく家でゲームをしますが、外で遊びたいわけではないです。",
    "カナダに住んでいるからといって、フランス語が話せるわけではない。",
    "ChatGPTに単語の意味を教えてもらっただけです。作文を書かせたわけではありません。",
    "東京ディズニーランドだからといって、東京にあるわけではない。",
    "行きたくないわけじゃないけど、本当に忙しくて..."]
    $ correct = 0
    $ current_stage = "stage1_6"
    $ explanation = "「遊びたいわけではない」はおかしいです。「わけではない」は{color=#ff0000}普通そう思われそうなことを否定{/color}する表現です。「よく家でゲームをする」なら「外で遊びたくない」が自然な流れなので、「遊びたくないわけではない」であるべきです、先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 2 Nからみると/すると/いうと
label stage2_6:
    $ sentences = [
    "ネイティブの人からすると、ジョージの発音はまだまだです。",
    "けいたさんは性格からすると、モテるはずです。",
    "けいたさんは顔からみると、モテるはずです。",
    "昔、ネットで何かを調べるのに図書館までいかなければならなかった。今からみると、とても不便そうだ。",
    "パソコンを買うなら、バッテリーからいうとマックがいいです。"]
    $ correct = 2
    $ current_stage = "stage2_6"
    $ explanation = "「顔からみると」はおかしいです。「からみると」はNが{color=#ff0000}人やグループ{/color}のときに、その人の意見を伝う表現です。「顔」は人じゃないので、「顔からすると」のほうが正しいですよ、先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 3 ～（の）ではない（だろう）か
label stage3_6:
    $ sentences = [
    "先生、スライドのここに間違いがあるのではないかと思いますが...",
    "この本は難しいけど、小学生には読めないとは限らないんじゃないでしょうか。",
    "たけしはいつも宿題をしないんだけど、できないわけじゃないんじゃない？",
    "たけしはいつも宿題をしないんだけど、できないんじゃない？",
    "日本の過剰包装は絶対に環境に良くないのではないでしょうか。"]
    $ correct = 4
    $ current_stage = "stage3_6"
    $ explanation = "「絶対に〜ではないでしょうか」はおかしいです。「絶対に」は強いなのに「ではないでしょうか」は{color=#ff0000}柔らかい{/color}言い方なので、二つのトーンが合っていません。どちらかに統一しましょう、先生～。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 4 ～がる
label stage4_6:
    $ sentences = [
    "友達は新しいふでばこをほしがっていたので、誕生日に買ってあげました。",
    "今年の誕生日、何か欲しがっているものある？",
    "言語を学ぶには、恥ずかしがらずに話すことが大事です。",
    "悲しい時は強がらないで泣いてもいいですよ。",
    "おばけなんていないので、怖がる必要はありません。"]
    $ correct = 1
    $ current_stage = "stage4_6"
    $ explanation = "「〜がる」は{color=#ff0000}他の人の気持ちを外から見る{/color}時に使う表現です。直接その人に聞く時は「欲しいものある？」で大丈夫ですよ～、先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 5 ～ようとする/しない
label stage5_6:
    $ sentences = [
    "音楽を聞こうとしたら、イヤホンが壊れていることに気がついた。",
    "メガネをかけようとしたら目がねぇ。",
    "うちの子供が中々勉強しようとしなくて、困っているんです。",
    "私はタバコを吸おうとしない人と一緒に住みたいです。",
    "病気のふりをしようとしてもダメです。学校に行きなさい。"]
    $ correct = 3
    $ current_stage = "stage5_6"
    $ explanation = "「タバコを吸おうとしない」はおかしいです。「〜ようとしない」は{color=#ff0000}本来やるべきことをやらない{/color}ときに使います。タバコを吸うことは別にやるべきことじゃないですよね、先生～。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 6 ～まま
label stage6_6:
    $ sentences = [
    "靴を履いたまま入らないでください。",
    "まどを開けたまま出かけてしまった。",
    "まどが開いたまま出かけてしまった。",
    "帰ったら、まどが開いたままでした。",
    "帰ったら、まどが開けられたままでした。"]
    $ correct = 2
    $ current_stage = "stage6_6"
    $ explanation = "前半の主語は「まど」なのに後半の主語は「私」になっていて、{color=#ff0000}主語がバラバラ{/color}ですよ、先生～。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 7 ～ように言う
label stage7_6:
    $ sentences = [
    "友達に宿題を手伝ってくれるように頼みました。",
    "サラさんに早く家を出るように言ったので、今日は遅刻しないはずです。",
    "先生にしずかにするように言われました。",
    "先生に作文を直すようにお願いしました。",
    "遊んでいる子供に車に気をつけるように注意しました。"]
    $ correct = 3
    $ current_stage = "stage7_6"
    $ explanation = "「直すようにお願いした」はおかしいです。先生にお願いするときは「〜ように」だけだと少し失礼です。{color=#ff0000}「直してくださるようにお願いした」{/color}と敬意を込めた形にしましょう、先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)


# Stage 8 ～ほど
label stage8_6:
    $ sentences = [
    "このレストランの料理は一生忘れられないほどおいしいです。",
    "富士登山で二度と歩きたくないほど疲れました。",
    "このレストランの料理は一生忘れられないほどまずいです。",
    "この映画のエンディングは泣くほど悲しいらしいです。",
    "運動しすぎて、足が取れるほどだ。"]
    $ correct = 3
    $ current_stage = "stage8_6"
    $ explanation = "「泣くほど悲しい」はおかしいです。「〜ほど」は{color=#ff0000}大げさ{/color}にする表現です。悲しくて泣くのは普通のことですよ、先生。"
    $ sentence_index = 0
    call screen stage_screen(sentences, correct, current_stage)

# Stage 9 わざわざ
label stage9_6:
    $ sentences = [
    "わざわざお越しいただきありがとうございます。",
    "わざわざクッキーを作ったのに、家に忘れてきちゃった。",
    "わざわざクッキーを作ったのに、誰も食べてくれないの？",
    "わざわざクッキーを作ってくれたのに、食べられなくてごめん。",
    "わざわざ持ってきたので、ぜひ召し上がってください。"]
    $ correct = 4
    $ current_stage = "stage9_6"
    $ explanation = "「わざわざ～、ぜひ～」はおかしいです。「わざわざ」は{color=#ff0000}頑張りをアピールする{/color}ときに使うので、「わざわざ」の偉そうな感じと「ぜひ」のおすすめの感じを一緒に使いませんよ、先生。"
    call screen stage_screen(sentences, correct, current_stage)
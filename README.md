# Generating Facial Image
Flaskを用いてWeb上で顔画像の生成をするプログラム．
# ソースコードの説明
* main.py: 画像の生成，Web上での動作等が記述してある．
* network.py: GeneratorとDiscriminatorのネットワークが記述してある．
* functions.py: GeneratorとDiscriminatorで必要な関数が記述してある．
* template/index.html: Webのレイアウト等の記述がしてある．

# 処理
* 実行コマンド
```
python3 main.py
```

# 必要なライブラリ
* numpy
* flask
* chainer (over v3)
* PIL


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
Attributeを選択して，Generateボタンを押すと顔画像を生成する．
生成された顔画像はstaticディレクトリの中のimageディレクトリに保存される．
選択したAttributeは画像の下に表示され，どの顔属性を生成しているか一目で見てわかるように設計した．

![github mp4](https://user-images.githubusercontent.com/27120804/43381012-24733114-940e-11e8-9d43-e4c77a2aafe8.gif)

# 必要なライブラリ
* numpy
* flask
* chainer (over v3)
* PIL

## 学習済みモデル置き場
下記のリンクからDownloadしてソースコードと同じディレクトリに置いてください．
https://drive.google.com/open?id=1F17Jc7jyLayVIr_mh9GNrWCULH09bPUk

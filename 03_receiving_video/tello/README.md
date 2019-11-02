# 準備

## 1. ffmpeg をダウンロードしてインストール

* ffmpeg: [https://www.ffmpeg.org/](https://www.ffmpeg.org/) 

### MAC に ffmpeg をインストールする。

下記 URL から MAC用の ffmpeg をダウンロードする。
* [https://evermeet.cx/ffmpeg/ffmpeg-95589-gd3dee676b8.zip](https://evermeet.cx/ffmpeg/ffmpeg-95589-gd3dee676b8.zip)

ダウンロードした zip ファイルを下記コマンドで解凍し、実行ファイルを /usr/local/bin へコピーする。

```bash
unzip ffmpeg-95589-gd3dee676b8.zip
chmod +x ffmpeg
sudo cp ffmpeg /usr/local/bin/ffmpeg 
```

## 2. Github から リポジトリをクローン

```bash
git clone git@github.com:mpsamurai/tech-room-tello-edu-samples.git
cd tech-room-tello-edu-samples/03_receiving_video/tello
```

## 3. Pipenv を使って必要なライブラリをインストール

下記コマンドで numpy と opencv がインストールされます。

```bash
pipenv install
```

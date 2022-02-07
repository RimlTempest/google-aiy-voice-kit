# Google AIY Voice KIT

Google AIY Voice Kitとは自作でAIスピーカーを作ってみよう！というGoogle社が販売している製品です。  
プログラミング初学者の勉強用になればと思い簡単に扱えそうなコード基板を製作しました。  
※ Google AiY Voice Kitの環境構築は完了しているのが前提です。

## 環境

開発: VSCode
言語: Python3.9

## 構成

- google-aiy-voice-kit
当アプリケーションのディレクトリです。
    - .vscode  
        VSCodeの設定ファイルが入っています。
    - google-aiy-voice-kit  
        基本的にコーディングするディレクトリはこちらです。
        - libs  
            [libsについて](./google-aiy-voice-kit/libs/README.md)
            - base  
                [baseについて](./google-aiy-voice-kit/libs/base/README.md)
    - config  
        [configについて](./config/README.md)
    - logs
        [logsについて](./logs/README.md)
    - tests
        [testsについて](./tests/README.md)
    - libs
        [libsについて](./libs/README.md)
    - docs
        [docsについて](./docs/README.md)

## 内部構造

Google AIY Voice KitはGCPの`SpeechToText`を使う前提の製品ですが、こちらを使ってしまうと数アクションを行うだけでお金がかかってしまいます。  
そのため今回は音声認識ライブラリの`SpeechRecognition`を利用して`SpeechToText`のような動作を実現しております。　　
そして他にもGoogle AIY Voice Kitの読み上げ機能が日本語対応していないという問題もあります。  
こちらに関しては`Open JTalk`というテキスト音声合成システムを利用して、日本語対応しております。  

## 実行方法

導入  
```bash
$ git clone https://github.com/RimlTempest/google-aiy-voice-kit.git
```

移動
```bash
$ cd google-aiy-voice-kit
```

必要ライブラリを導入
```bash
$ pip3 install -r requirements.txt
```

実行
```bash
$ python3 -m google-aiy-voice-kit
```
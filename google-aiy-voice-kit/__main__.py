#! /usr/bin/env python3
# coding: utf-8

import threading

from aiy.board import Board, Led

import speech_recognition as sr

import libs.command as Command
import libs.logging as Logging


def main():
    with Board() as board:
        log = Logging.Logging()

        r = sr.Recognizer()
        mic = sr.Microphone()
        cmd = Command.Command(board)

        while True:
            print("何か話してください")
            board.led.state = Led.ON

            # ボタンが押されるまで待つ
            board.button.wait_for_press()
            board.led.state = Led.OFF

            done = threading.Event()
            board.button.when_pressed = done.set

            with mic as source:
                # ノイズ対策
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            print("テキスト変換中...")

            try:
                reco = r.recognize_google(audio, language="ja-JP")
                talk_text = reco

                print(f"認識結果: {talk_text}")

                """
                コマンドはここに追加する
                """

                if talk_text == "テスト":
                    cmd.test_message()
                elif talk_text == "終了":
                    cmd.message("終了します。")
                    break
                elif talk_text == "音量上げて":
                    cmd.volume(10, True)
                elif talk_text == "音量下げて":
                    cmd.volume(10, False)
                elif talk_text == "現在の音量":
                    cmd.now_volume()
                elif talk_text == "ミュート":
                    cmd.mute()
                else:
                    cmd.message(talk_text)

                """
                コマンドはここまで
                """

                # ログファイルに書き込み
                log.write(talk_text)

            except sr.UnknownValueError:
                print("音声認識に失敗しました")
            except sr.RequestError as e:
                print("音声認識サービスに接続できませんでした。 {0}".format(e))


if __name__ == "__main__":
    main()

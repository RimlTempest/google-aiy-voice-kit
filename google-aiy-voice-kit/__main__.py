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
            print("ボタンを押してください。")

            # ボタンが押されるまで待つ
            board.button.wait_for_press()

            done = threading.Event()
            board.button.when_pressed = done.set
            board.led.state = Led.ON
            cmd.message("なんでしょうか？")

            with mic as source:
                # ノイズ対策
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            print("テキスト変換中...")
            board.led.state = Led.OFF

            try:
                say = cmd._command_setting(r.recognize_google(audio, language="ja-JP"))
                print(f"認識結果: {say}")

                """
                コマンドはここに追加する
                """

                if say == "テスト":
                    cmd.test_message()
                elif say == "終了":
                    cmd.message("終了します。")
                    break
                elif say == "音量上げて":
                    cmd.volume(10, True)
                elif say == "音量下げて":
                    cmd.volume(10, False)
                elif say == "現在の音量":
                    cmd.now_volume()
                elif say == "ミュート":
                    cmd.mute()
                elif say == "電気つけて" or say == "電気付けて":
                    cmd.switch_bot(True)
                elif say == "電気けして" or say == "電気消して":
                    cmd.switch_bot(False)
                else:
                    cmd.message(say)

                """
                コマンドはここまで
                """

                # ログファイルに書き込み
                log.write(say)

            except sr.UnknownValueError:
                print("音声認識に失敗しました")
            except sr.RequestError as e:
                print("音声認識サービスに接続できませんでした。 {0}".format(e))


if __name__ == "__main__":
    main()

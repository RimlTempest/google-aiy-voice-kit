import subprocess
from aiy.board import Board, Led
import aiy.jtalk as talk


class Command:
    """
    コマンドの処理を行うクラス
    """

    def __init__(self, board: Board):
        self.board = board

    def _talk(self, message: str):
        """
        テキストを音声に変換する
        """
        text = message.encode("utf-8")
        talk.jtalk(text)
        print(text)

    def test_message(self):
        """
        テストメッセージを音声に変換して表示する
        """
        self.board.led.state = Led.ON
        self._talk("テストします")
        self.board.led.state = Led.OFF

    def message(self, message):
        """
        テキストを音声に変換して表示する
        """
        self.board.led.state = Led.ON
        self._talk(message)
        self.board.led.state = Led.OFF

    def volume(self, volume, command=True):
        """
        音量を操作する
        command=True: 音量を上げる
        command=False: 音量を下げる
        volume: 音量の値{0~100}
        """
        if command:
            set_volume = str(volume) + "%+"
        else:
            set_volume = str(volume) + "%-"

        self.board.led.state = Led.ON
        subprocess.run(["amixer", "sset", "Master", set_volume])
        self._talk("音量を10上げました")
        self.board.led.state = Led.OFF

    def now_volume(self):
        """
        現在の音量を取得して表示する
        """
        self.board.led.state = Led.ON
        res = subprocess.run(["amixer", "sget", "Master", "|", "egrep", "'\[.*%\]"])
        self._talk(f"現在の音量は{str(res)}%です")
        self.board.led.state = Led.OFF

    def mute(self):
        """
        ミュートを操作する
        """
        self.board.led.state = Led.ON
        self._talk("ミュートまたはミュート解除しました")
        subprocess.run(["amixer", "sset", "Master", "on"])
        self.board.led.state = Led.OFF

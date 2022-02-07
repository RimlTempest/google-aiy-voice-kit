from aiy.board import Led
import aiy.jtalk as talk


class BaseCommand:
    """
    基幹のコマンドの処理を行うクラス
    """

    def __init__(self, board):
        self._board = board

    def _led_on(self):
        """
        LEDを点灯する
        """
        self._board.led.state = Led.ON

    def _led_off(self):
        """
        LEDを消灯する
        """
        self._board.led.state = Led.OFF

    def _command_setting(self, reco):
        """
        コマンドを受け取り適切な形に整形する
        """
        talk_text = reco.split(" ")
        say = talk_text[0]
        return say

    def _talk(self, message: str):
        """
        テキストを音声に変換する
        """
        text = message.encode("utf-8")
        talk.jtalk(text)

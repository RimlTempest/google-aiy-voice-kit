import subprocess
import requests, json
import base.base_command as BaseCommand


class Command(BaseCommand.BaseCommand):
    """
    コマンドの処理を行うクラス
    """

    def __init__(self, board):
        super(Command, self).__init__(board)

    def test_message(self):
        """
        テストメッセージを音声に変換して表示する
        """
        self._led_on()
        self._talk("テストします")
        self._led_off()

    def message(self, message):
        """
        テキストを音声に変換して表示する
        """
        self._led_on()
        self._talk(message)
        self._led_off()

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

        self._led_on()
        subprocess.run(["amixer", "sset", "Master", set_volume])
        self._talk("音量を10上げました")
        self._led_off()

    def now_volume(self):
        """
        現在の音量を取得して表示する
        """
        self._led_on()
        res = subprocess.run(["amixer", "sget", "Master", "|", "egrep", "'\[.*%\]"])
        self._talk(f"現在の音量は{str(res)}%です")
        self._led_off()

    def mute(self):
        """
        ミュートを操作する
        """
        self._led_on()
        self._talk("ミュートまたはミュート解除しました")
        subprocess.run(["amixer", "sset", "Master", "on"])
        self._led_off()

    def switch_bot(self, command=True):
        """
        ボットをONにする
        """
        # パラメーター（要書き換え）
        DEVICEID = "SwitchBotのデバイスID"
        ACCESS_TOKEN = "開発者トークン"
        API_BASE_URL = "https://api.switch-bot.com"

        self._led_on()
        if command:
            set_switch = "turnOn"
            status = "オン"
        else:
            set_switch = "turnOff"
            status = "オフ"

        headers = {
            "Content-Type": "application/json; charset: utf8",
            "Authorization": ACCESS_TOKEN,
        }
        url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
        body = {"command": set_switch, "parameter": "default", "commandType": "command"}
        data = json.dumps(body)
        res = requests.post(url, data=data, headers=headers)
        print(res)
        self._talk(f"ボットを{status}にしました")
        self._led_off()

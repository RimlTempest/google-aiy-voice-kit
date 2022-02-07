from datetime import datetime


class Logging:
    """
    ログ生成を行うクラス
    """

    def __init__(self):
        # 文字起こしファイルのファイル名を日付のtxtファイルとする
        self.filename: str = datetime.now().strftime("%Y%m%d_%H:%M:%S")
        self.txt_path: str = f"./logs/{self.filename}.txt"

        # ログファイル作成
        with open(self.txt_path, "w+") as f:
            f.write(self.filename + "\n")

    def write(self, message):
        """
        ログを書き込む
        """
        # ログファイルに書き込み
        with open(self.txt_path, "a") as f:
            f.write(f"\n認識文字列: {message}")

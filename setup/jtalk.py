# coding: utf-8

import subprocess


def jtalk(t):
    """
    音声合成のための設定ファイル
    こちらをAIY-projects-python/src/aiy/にjtalk.pyとしてコピーしてください
    """
    open_jtalk = ["open_jtalk"]
    mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
    htsvoice = ["-m", "/usr/share/hts-voice/mei/mei_normal.htsvoice"]
    speed = ["-r", "1.0"]
    outwav = ["-ow", "open_jtalk.wav"]
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ["aplay", "-q", "open_jtalk.wav"]
    wr = subprocess.Popen(aplay)

import socket
import glob
array = glob.glob('*.sb2')
# python ヒアドキュメントってあるのか

with open("test.txt","w") as f:
    for elm in array:
        f.write ('<br><a href="./' + elm + '"> ' + elm + '</a>' + "¥n")
# 改行の書き方がわからない
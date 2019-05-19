import os
import sys
import time
from time import sleep
y = "\x1b[93m"
g = "\x1b[92m"
d = "\x1b[0m"
h = "\x1b[8m"
def tulis(s):
    for c in s + ' ':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1)

os.system("clear")
tulis(g+"[•] Ini adalah tool untuk menampilkan shortcut pada termux.")
sleep(1)
print("\n\n")

sleep(1)
input(d+'[•] Press enter to continue. \r')
sleep(2)
tulis(y+"\n[•] Sedang membuat file directory ")
load("....")
try:
      os.mkdir("/data/data/com.termux/files/home/.termux")
except:
      pass
tulis(g+"[!] Sukses membuat direktori. \n")
tulis(y+"\n[•] Sedang membuat properties ")
load("...")
shortcut = "extra-keys = [['ESC','ALT','<','>','[',']','HOME','UP','PGUP'],['TAB','(',')','{','}','|','LEFT','+','RIGHT'],['CTRL','~','`','_','-','/','END','DOWN','PGDN']]"
prop = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
prop.write(shortcut)
prop.close()
sleep(1)
tulis(g+"\n[!] Sukses membuat properties. \n")
sleep(1)
tulis(y+"\n[!] Memuat ulang ")
load("...")
os.system("termux-reload-settings")
tulis(g+"\n[!] Sukses !!\n  Terimakasih sudah memakai script ini :) \n")
os.system('rm -rf  /key/termuxkey.py')

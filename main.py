import subprocess
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.utils import *


if sys.version_info[0] != 3:
    raise(RuntimeError("This program is not supported for Python2.x versions\nPlease visit here to install Python3.x:\nhttps://www.python.org/downloads/"))

def main():
    msg = MessageManager(file_path= os.path.abspath("properties.json"))
    backup = BackupManager(backup_directory = str(msg.get("settings","backup-place")))


    print(msg.get("outputs","backup?"))
    if input().lower() == "y":
        print(msg.get("outputs","start-backup"))
        if backup.do():
            print(msg.get("outputs","bu-success"))


    print(msg.get("outputs","boot"))


    if not (subprocess.call(msg.get("settings","jvm-args",(msg.get("settings","jar-file")))) == 0):
        print(msg.get("outputs","exited-error"))

    time.sleep(1)

    print(msg.get("outputs","backup?"))
    if input().lower() == "y":
        print(msg.get("outputs","start-backup"))
        if backup.do():
            print(msg.get("outputs","bu-success"))



if __name__ == "__main__":
    main()
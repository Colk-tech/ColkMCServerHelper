import json
import time
import random
import shutil
import os.path


from lib.codeutil import Singleton


class MessageManager(Singleton):
    def __init__(self, file_path="properties.json"):
        """
        JSONを読み込んでインスタンスを作る。
        :param file_path: メッセージ情報が格納されたJSON。通常指定する必要はない。
        """
        try:
            with open(file_path, mode="r") as f:
                self.json_msg = json.loads(f.read())
        except:
            print("File doesn't exist or it is incorrect!")

    def get(self, scope, name, *kargs):
        """
        JSONからメッセージを読み込んで整形する。
        :param scope: JSONファイルの第一階層。
        :param name: JSONファイルの第二階層。
        :param kargs: 整形に使用するデータ。
        """
        msg = self.json_msg[scope][name]

        if isinstance(msg, str):
            return msg.format(*kargs)
        elif isinstance(msg, list):
            idx = random.randint(0, len(msg) - 1)
            return msg[idx].format(*kargs)
        else:
            raise RuntimeError("Illegal JSON message type!")


class BackupManager(Singleton):
    def __init__(self, backup_directory = r""):
        if not os.path.exists(backup_directory):
            try:
                os.makedirs(backup_directory)
            except:
                raise OSError("Failed to create backup directory!")
                return False
        self.backup_full_path = os.path.abspath(backup_directory)

    def do(self):
        try:
            shutil.copytree(os.path.dirname(os.path.abspath(__file__)), self.backup_full_path+"/"+str(time.time())+"/")
        except:
            raise OSError("Failed to create backup!\nPlease try to backup yourself.")
            return False
        return True
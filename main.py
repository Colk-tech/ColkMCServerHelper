# coding: utf-8

# === initialize === #
import os
import sys
import time
import shutil
ut = time.time()
def flag_initialize():
    global while_flag
    global error_flag
    while_flag = True
    error_flag = False
flag_initialize()
Current_Directory: str = os.getcwd()
# === end initialize === #

# === ask user if want to backup === #
while bool(while_flag):
    print("サーバー起動前にバックアップしますか？(Y/N)")
    if bool(error_flag) == False:
        backupYN1 = input()
        if backupYN1 == "Y" or backupYN1 == "y":
            print("バックアップを開始します...")
            backup_flag = True
            while_flag = False
        elif backupYN1 == "n" or backupYN1 == "N":
            print("バックアップしないでサーバーを起動します...")
            backup_flag = False
            while_flag = False
        else:
            print("Y/N以外が入力されました。")
            print()
# === end "ask user if want to backup" === #

flag_initialize()

# === backup data === #
if bool(backup_flag) == True:
    backup_error_flag = False
    try:
        shutil.copytree(os.getcwd(), "../Backup" + "/" + str(ut) + "/")
    except:
        backup_error_flag = True
    if bool(backup_error_flag) == False:
        print("バックアップが完了しました。")
        print("サーバーを起動します...")
    elif bool(backup_error_flag) == True:
        while bool(while_flag):
            print("バックアップに失敗しました。")
            print("サーバーを起動しますか？")
            if bool(error_flag) == False:
                backupYN1 = input()
                if backupYN1 == "Y" or backupYN1 == "y":
                    print("サーバーを起動します。")
                    backup_flag = True
                    while_flag = False
                elif backupYN1 == "n" or backupYN1 == "N":
                    print("終了します...")
                    backup_flag = False
                    while_flag = False
                    exit()
                else:
                    print("Y/N以外が入力されました。")
                    print()
# === end "backup data" === #

flag_initialize()

# === BOOT SERVER === #
os.system("cd"+" "+'"'+Current_Directory+'"')
os.system("java -Xms4096M -Xmx4096M -jar" + " server.jar " + "-o true")
# === end "BOOT SERVER" === #

# === ask user if want to backup === #
while bool(while_flag):
    print("サーバーをバックアップしますか？(Y/N)")
    if bool(error_flag) == False:
        backupYN1 = input()
        if backupYN1 == "Y" or backupYN1 == "y":
            print("バックアップを開始します...")
            backup_flag = True
            while_flag = False
        elif backupYN1 == "n" or backupYN1 == "N":
            print("バックアップしないで終了します...")
            backup_flag = False
            while_flag = False
        else:
            print("Y/N以外が入力されました。")
            print()
# === end "ask user if want to backup" === #

backup_error_flag = False

if bool(backup_flag) == True:
    try:
        shutil.copytree(os.getcwd(), "../Backup" + "/" + str(ut) + "/")
    except:
        backup_error_flag = True
    if bool(backup_error_flag) == False:
        print("バックアップが完了しました。")
    elif bool(backup_error_flag) == True:
        print("バックアップに失敗しました。")
        print("終了後、手動でバックアップすることをおすすめします。")

print("ServerHelperを終了します...")
print("続行するには任意の文字列を入力してください...")
STOPPer = input()
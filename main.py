# coding: utf-8

# === initialize === #
import os
import sys
import time
import shutil
ut = time.time()
while_flag = True
error_flag = False
def flag_initialize():
    global while_flag
    global error_flag
    while_flag = True
    error_flag = False
flag_initialize()
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
        shutil.copytree(os.getcwd(),"../Backup"+"/"+str(ut)+"/")
    except:
        backup_erroe_flag = True
    if bool(backup_error_flag) == False:
        print("バックアップが完了しました。")
        print("サーバーを起動します...")
    else:
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
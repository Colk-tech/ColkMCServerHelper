# coding: utf-8
# === start initialize ===
import os
import time
ut = time.time()
boolsec = True
boolsec2 = True
error_flag = False
# === end initialize ===


while bool(boolsec):
    print("サーバー起動前にバックアップしますか？(Y/N)")
    if bool(error_flag) == False:
        backupYN1 = input()
        if backupYN1 == "Y" or backupYN1 == "y":
            print("バックアップを開始します...")
            backup_flag = True
            boolsec = False
        elif backupYN1 == "n" or backupYN1 == "N":
            print("バックアップしないでサーバーを起動します...")
            backup_flag = False
            boolsec = False
        else:
            print("Y/N以外が入力されました。")
            print()

error_flag = False

if bool(backup_flag) == True:
    backup_error_flag = False
    import shutil
    try:
        shutil.copytree(os.getcwd(),"../Backup"+"/"+str(ut)+"/")
    except:
        backup_erroe_flag = True
    if bool(backup_error_flag) == False:
        print("バックアップが完了しました。")
        print("サーバーを起動します...")
    else:
        while bool(boolsec2):
            print("バックアップに失敗しました。")
            print("サーバーを起動しますか？")
            if bool(error_flag) == False:
                backupYN1 = input()
                if backupYN1 == "Y" or backupYN1 == "y":
                    print("バックアップを開始します...")
                    backup_flag = True
                    boolsec = False
                elif backupYN1 == "n" or backupYN1 == "N":
                    print("バックアップしないでサーバーを起動します...")
                    backup_flag = False
                    boolsec = False
                else:
                    print("Y/N以外が入力されました。")
                    print()
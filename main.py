# coding: utf-8

# === initialize === #
import os
import inputimeout
import sys
import ConfigParser
# refer https://uxmilk.jp/20599 #
import time
import shutil
ut = time.time() #Get unix time to create ID of a backup
def flag_initialize():
    """
    Initialize all the values of the flags.

    Parameters
    ----------
    while_is : bool45
    The flag for while sentences
    (Every while sentences uses same flag).
    error_is : bool
    The flag for errors
    (Every error checker uses same flag. Therefore, this flag can't be used to find where a error occurs.)
    """
    global while_is
    global error_is
    global shutdown_is
    global backup_error_is
    global shutdown_error_is
    shutdown_is = False
    backup_error_is = False
    while_is = True
    error_is = False
    shutdown_error_is = False
flag_initialize()
Current_Directory: str = os.getcwd()
# === end initialize === #

# === ask user if want to backup === #
while bool(while_is):
    print("サーバー起動前にバックアップしますか？(Y/N)")
    if bool(error_is) == False:
        usr_input_backup = input()
        if usr_input_backup == "Y" or usr_input_backup == "y":
            print("バックアップを開始します...")
            backup_is = True
            while_is = False
        elif usr_input_backup == "n" or usr_input_backup == "N":
            print("バックアップしないでサーバーを起動します...")
            backup_is = False
            while_is = False
        else:
            print("Y/N以外が入力されました。")
            print()
# === end "ask user if want to backup" === #

flag_initialize()

# === backup data === #
if bool(backup_is) == True:
    backup_error_is = False
    try:
        shutil.copytree(os.getcwd(), "../Backup" + "/" + str(ut) + "/")
    except:
        backup_error_is = True
    if bool(backup_error_is) == False:
        print("バックアップが完了しました。")
        print("サーバーを起動します...")
    elif bool(backup_error_is) == True:
        while bool(while_is):
            print("バックアップに失敗しました。")
            print("サーバーを起動しますか？")
            if bool(error_is) == False:
                usr_input_backup = input()
                if usr_input_backup == "Y" or usr_input_backup == "y":
                    print("サーバーを起動します。")
                    backup_is = True
                    while_is = False
                elif usr_input_backup == "n" or usr_input_backup == "N":
                    print("終了します...")
                    backup_is = False
                    while_is = False
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
while bool(while_is):
    print("サーバーをバックアップしますか？(Y/N)")
    if bool(error_is) == False:
        try:
            usr_input_backup = inputimeout(prompt='>>', timeout=60)
            if usr_input_backup == "Y" or usr_input_backup == "y":
                print("バックアップを開始します...")
                backup_is = True
                while_is = False
            elif usr_input_backup == "n" or usr_input_backup == "N":
                print("バックアップしないで終了します...")
                backup_is = False
                while_is = False
            else:
                print("Y/N以外が入力されました。")
                print()
        except:
            print("入力がタイムアウトしました。")
            print("強制的にバックアップします。")
            backup_is = True
            while_is = False
# === end "ask user if want to backup" === #

backup_error_is = False

if bool(backup_is) == True:
    try:
        shutil.copytree(os.getcwd(), "../Backup" + "/" + str(ut) + "/")
    except:
        backup_error_is = True
    if bool(backup_error_is) == False:
        print("バックアップが完了しました。")
    elif bool(backup_error_is) == True:
        print("バックアップに失敗しました。")
        print("終了後、手動でバックアップすることをおすすめします。")

print("続けて、コンピューターをシャットダウンしますか?")
try:
    usr_input_shutdown = inputimeout(prompt='', timeout=60)
    if usr_input_shutdown == "Y" or usr_input_shutdown == "y":
        print("シャットダウンします...")
        shutdown_is = True
        while_is = False
    elif usr_input_shutdown == "n" or usr_input_shutdown == "N":
        print("シャットダウンせずに終了します...")
        shutdown_is = False
        while_is = False
    else:
        print("シャットダウンせずに終了します...")
        shutdown_is = False
        while_is = False
except:
    print("入力がタイムアウトしました。")
    print("強制的にシャットダウンします。")
    shutdown_is = True

if bool(shutdown_is) == True:
    try:
        import subprocess
        subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
    except:
        shutdown_error_is = True
    if bool(shutdown_error_is) == False:
        print("シャットダウンします...")
        exit(0)
    elif bool(shutdown_error_is) == True:
        print("シャットダウンに失敗しました。")
        print("遠隔からのシャットダウンを試みてください。")

print("ServerHelperを終了します...")
print("続行するには任意の文字列を入力してください...")
input()
# coding: utf-8

import os
import shutil
import time
import sys
import time
import configparser

userInputed = False

backupPlace = "../Backup" + "/" + str(time.time()) + "/"
serverName = "Mohist-0c5f67e-server.jar"
Xms = "4096M"
Xmx = "4096M"

def backupper(backupPlace):
    try:
        shutil.copytree(os.getcwd(), backupPlace)
        return True
    except:
        return False

def flagInitialize():
    global userInputed
    userInputed = False

flagInitialize()

while not userInputed:
    print("Do you want to backup before boot the server? (Y/N)")
    usrInput = str.upper(input())
    if usrInput == "Y":
        if backupper(backupPlace):
            print("Backuped!")
            userInputed = True
        else:
            print("Failed to backup!")
            print("Try to backup yourself...")
            userInputed = True
    elif usrInput == "N":
        print("We are not going to backup server!")
        userInputed = True
    else:
        print("You entered something else!")
        userInputed = False

flagInitialize()

print("Booting server...")
os.system("cd" + " " + '"'+os.getcwd()+'"')
os.system("java" + " " + "-Xms" + Xms + " " + "-Xmx" + Xmx + " " + "-jar" + " " + serverName + " " + "-o true")
#os.system("python" + " " + "another.py")

while not userInputed:
    print("Do you want to backup the server? (Y/N)")
    usrInput = str.upper(input())
    if usrInput == "Y":
        if backupper(backupPlace):
            print("Backuped!")
            userInputed = True
        else:
            print("Failed to backup!")
            print("Try to backup yourself...")
            userInputed = True
    elif usrInput == "N":
        print("We are not going to backup server!")
        userInputed = True
    else:
        print("You entered something else!")
        userInputed = False

print("Shut downing this server helper...")
usrInput = input()
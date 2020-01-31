# coding: utf-8

import os
import shutil
import time
import sys
import time
import configparser

CD = os.getcwd()

config = configparser.ConfigParser()
configName = "setting-cmcsh.ini"
section1 = 'server'
section2 = 'jvm'
section3 = 'backup'

if not os.path.isfile(CD + "/" + configName):
    #section1-server
    config.add_section(section1)
    config.set(section1, 'server-jar', 'server.jar')
    #section2-jvm
    config.add_section(section2)
    config.set(section2, 'xms', '1024M')
    config.set(section2, 'xmx', '2048M')
    #section3-backup
    config.add_section(section3)
    config.set(section3, 'place', '../backups')

    with open('setting.ini', 'w') as file:
        config.write(file)

MSserver = config.get(section1, 'server-jar')
MSxms = config.get(section2, 'xms')
MSxmx = config.get(section2, 'xmx')
BUplace = config.get(section3, 'place')

userInputed = False

backupPlace = BUplace + str(time.time()) + "/"

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
        print("You entered something wrong!")
        userInputed = False

flagInitialize()

print("Booting server...")
os.system("cd" + " " + '"'+os.getcwd()+'"')
os.system("java" + " " + "-Xms" + MSxms + " " + "-Xmx" + MSxmx + " " + "-jar" + " " + MSserver + " " + "-o true")
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
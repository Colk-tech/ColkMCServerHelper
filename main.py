# coding: utf-8

import os
import shutil
import time
import sys
import time
import configparser
from typing import Any

currentDirectory = os.getcwd()

config = configparser.ConfigParser()
configName = "setting-cmcsh.ini"
section1 = 'server'
section2 = 'jvm'
section3 = 'backup'

if not os.path.isfile(currentDirectory + "/" + configName):
    print("We couldn't find setting file.")
    print("Create the setting file.")
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

    with open(configName, 'w') as file:
        config.write(file)

config.read(configName)
MSserver = config.get(section1, 'server-jar')
MSxms = config.get(section2, 'xms')
MSxmx = config.get(section2, 'xmx')
BUplace = config.get(section3, 'place')
backupPlace = BUplace + str(time.time()) + "/"

def backupCore(backupPlace):
    if bool(inputter("Do you want to backup this server? (Y/N)")):
        if backupper(backupPlace):
            print("Backup success!")
        else:
            print("Backup failed...")
            print("Try to backup manually.")
    else:
        print("We are not going to backup.")

def backupper(backupPlace):
    try:
        shutil.copytree(os.getcwd(), backupPlace)
        return True
    except:
        return False

def inputter(message,errorMessage = "You entered something wrong! Please answer in Y/N."):
    isuserinput = False
    while not isuserinput:
        print(str(message))
        userinput = str.upper(input())
        if userinput == "Y":
            isuserinput = True
            return True
        elif userinput == "N":
            isuserinput = True
            return False
        else:
            print(str(errorMessage))
            isuserinput = False

#ここからが実際に動くところ

backupCore(backupPlace)

os.system("cd" + " " + '"' + os.getcwd() + '"')
print(MSserver+MSxms+MSxmx+BUplace)
os.system("java" + " " + "-Xms" + MSxms + " " + "-Xmx" + MSxmx + " " + "-jar" + " " + MSserver + " " + "-o true")

backupCore(backupPlace)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CarLand Final Project"""

import sys
import os
import getpass
import picklecache
import passmanager
import inventorymanager


passcache = picklecache.PickleCache('datastore.pkl', True)

def adminFuntionality():
    cont = 'Y'
    while cont == 'Y':
        print "\n\n1) Add SalesMen" 
        print "2) Add Inventory"
        print "3) Delete Inventory"
        print "4) Display avaiable Inventory"
        print "5) Display sold Inventory"
        print "6) Update password"
        print "7) Create Report"
        print "8) Logout\n\n"
    
        inp = int(raw_input("What action you will perform(1-7)?"))
        if inp == 1:
            addSalesMen()
        elif inp == 2:
            addInventory() 
        elif inp == 3:
            deleteInventory()
        elif inp == 4:
            displayAvInventory()
        elif inp == 5:
            displaySlInventory()  
        elif inp == 6:
            updatePasswordAdmin()
        elif inp == 7:
            createReport()
        elif inp == 8:
            os._exit(1)
        else:
            print "Invalid input"
        cont = raw_input("Do you want to continue (Y/N)?:")

def createReport():
    x = inventorymanager.inventorymanager()
    x.createReport()

def deleteInventory():
    x = inventorymanager.inventorymanager()
    x.deleteInventory()

def updatePasswordAdmin():
    updatePassword('admin')

def displaySlInventory():
    x = inventorymanager.inventorymanager()
    x.showSoldInventory()

def displayAvInventory():
    x = inventorymanager.inventorymanager()
    x.showAvaibleInventory()

def updatePassword(user):
    pswd = getpass.getpass('New Password:')
    newpass = passmanager.getEncPassword(user,pswd)
    passcache[user]=newpass

def addSalesMen():
    user = raw_input("User Name : ")
    password = getpass.getpass('Password:')
    passData = passmanager.getEncPassword(user,password)
    passcache[user]=passData
    
def addInventory():
    x = inventorymanager.inventorymanager() 
    x.addInventory()

def validDatePassword(user,password):
    savesalt = passcache[user][1]
    savepass = passcache[user][1]
    return passmanager.validPassword(user, password, passcache)

def salesMenFunctionality():
    cont = 'Y'
    while cont == 'Y':
        print "\n1) Sell Car"
        print "2) Cancel Car sold"
        print "3) Display avaiable Inventory"
        print "4) Display sold Inventory"
        print "5) Logout"
        try:
            inp = int(raw_input("Please choose option (1-5)?"))
        except:
            inp = 0
        if inp == 1:
            sellCar()
        elif inp == 2:
            revertSell()
        elif inp == 3:
            displayAvInventory()
        elif inp == 4:
            displaySlInventory()
        elif inp == 5:
            os._exit(1)
        else:
            print "Invalid input"
        cont = raw_input("Do you want to continue (Y/N)?:")

def sellCar():
    x = inventorymanager.inventorymanager()
    x.sellInventory()

def revertSell():
    x = inventorymanager.inventorymanager()
    x.revertSell()

if __name__ == "__main__":
    inp = raw_input("Are you Admin/SalesPerson(A/S)?")

    if inp == 'A':
        pswd = getpass.getpass('Password:')
        auth = validDatePassword('admin', pswd)
        if auth:
            print "\nWelecome {0}\n".format('Admin Brian')
            adminFuntionality()
        else:
            print "Invalid Admin Password"
    elif inp == 'S':
        user = raw_input("User:")
        pswd = getpass.getpass('Password:')
        auth = validDatePassword(user, pswd)
        if auth:
            print "Welecome {0}".format(user)
            salesMenFunctionality()
        else:
            print "Invalid user and password combination"
    else:
        print "{0} is invalid".format(inp)

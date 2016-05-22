#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CarLand Final Project"""

import csv
import car
import picklecache


class inventorymanager():
    def __init__(self):
        self.invcache = picklecache.PickleCache('invstore.pkl', True)

    def createReport(self):
        b = open('Report.csv', 'w')
        data = []
        data.append(['serielno', 'fuel', 'modelyear', 'color', 'manufacture',
                     'model','status'])
        inv = self.invcache.getData()
        for key, value in inv.iteritems():
            if value[1] =='a':
                status = 'available'
            else:
                status = 'sold'
            mycar = value[0]
            data.append([mycar.serielno, mycar.fuel, mycar.modelyear,
                         mycar.color, mycar.manufacture, mycar.model,
                         mycar.old_new,status])
            a = csv.writer(b)
            a.writerows(data)
            b.close()
            print 'Please check Report.csv for report'
        
    def sellInventory(self):
        s = raw_input("Enter Serial no of car you want to sell\
        (example  - MERC1234-2014):")
        inv = self.invcache.getData()
        if inv.has_key(s):
            self.invcache[s][1] = 's'
            print "Invetory {0}  sold successfully".format(s)
            self.invcache.flush()
        else:
            print "Invetory {0}  doest not exist".format(s)

    def revertSell(self):
        s = raw_input("Enter Seriel no of car you want to revert the sell\
        (example  - MERC1234-2014):")
        inv = self.invcache.getData()
        if inv.has_key(s):
            self.invcache[s][1] = 'a'
            print "Invetory {0}  sell reverted successfully".format(s)
            self.invcache.flush()
        else:
            print "Invetory {0}  doest not exist".format(s)
          
    def deleteInventory(self):
        s = raw_input("Enter Seriel no(example  - MERC1234-2014):")
        inv = self.invcache.getData()
        if inv.has_key(s):
            del self.invcache[s]
            print("Invetory {0}  deleted successfully".format(s)) 
        else:
            print "Invetory {0}  doest not exist".format(s) 
    
    def addInventory(self):
        s = raw_input("Enter Seriel no(example  - MERC1234-2014):")
        f = raw_input("Enter Fuel type (example - DIESEL/PETROL):")
        y = raw_input("Enter model year (example - 2014):")
        c = raw_input("Enter Color (example - RED ):")
        m = raw_input("Enter manufaturer (example - ge):")
        md = raw_input("Enter model (example - sparks):") 
        olnw = raw_input("Enter f its old or new (example - new/old):") 
        mycar = car.car(s, f, y, c, m, md, olnw)
        rec = [mycar, 'a']
        self.invcache[s]=rec
        print "Car with seriel no {0} sucessfully added to invertory".format(s)

    def showAvaibleInventory(self):
        data = self.getAvaibleInventory()
        if len(data):
            print '{:20s} {:10s} {:10s} {:10s} {:20} {:20} \
            {:10}'.format('serielno', 'fuel', 'modelyear', 'color', \
                           'manufacture', 'model', 'type')  
        else:
            print "There is no inventory avaible"
        for i in data:
            print i

    def showSoldInventory(self):
        data = self.getSoldInventory()
        if len(data):
            print('{:20s} {:10s} {:10s} {:10s} {:20} {:20} \
            {:10}'.format('serielno', 'fuel', 'modelyear', 'color',\
                           'manufacture', 'model', 'type'))  
        else:
            print "There is no sold inventory"
        for i in data:
            print i
 
    def getAvaibleInventory(self): 
        inv = self.invcache.getData()
        lst = []
        for key, value in inv.iteritems():
            if value[1] == 'a':
                mycar = value[0]
                lst.append('{:20s} {:10s} {:10s} {:10s} {:20} {:20} \
                {:10}'.format(mycar.serielno, mycar.fuel, mycar.modelyear, \
                              mycar.color, mycar.manufacture, mycar.model,\
                              mycar.old_new))
                #print('{:20s} {:10s} {:5s} {:10s} {:20} {:20} '.format
                #(mycar.serielno, mycar.fuel, mycar.modelyear, mycar.color,
                #mycar.manufacture, mycar.model))
        return lst

    def getSoldInventory(self):
        nv = self.invcache.getData()
        lst = []
        for key, value in inv.iteritems():
            if value[1] == 's':
                mycar = value[0]
                lst.append('{:20s} {:10s} {:10s} {:10s} {:20} {:20} \
                {:10}'.format(mycar.serielno, mycar.fuel, mycar.modelyear,\
                              mycar.color, mycar.manufacture, mycar.model,\
                              mycar.old_new))
                #print('{:20s} {:10s} {:5s} {:10s} {:20} {:20} '.format
                #(mycar.serielno, mycar.fuel, mycar.modelyear, mycar.color,
                #mycar.manufacture, mycar.model))
        return lst

import subprocess
import time
import pickle
def install():
    print("installing the required modules this may take time", end="")
    v = ["colorama", "pandas", "mysql", "datetime", "matplotlib"]
    for m in v:
        print(".", end="")
        subprocess.run(["pip", "install", m], capture_output=True, text=True)
    print("\n COMPLETED")

    time.sleep(1)


install()

import pandas as pd
import mysql.connector
import os
import numpy as np
import datetime
import matplotlib.pyplot as plt
import mysql.connector as sql
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)





def effect():
    print()
    for x in range(0, 22):
        time.sleep(1)
        print("\n")


def acknowledgements():
    close()
    print('''
    I would like to express my special thanks of gratitude to my teacher Mr. Rakesh soni as well as our principal
    Dr. Lalita Singh who gave me the golden opportunity to do this wonderful project which also helped me in doing a lot
    of research, and I came to know about so many new things. I am really thankful to them
    ''')


def introduction():
    x = '''
    Namaste! My name is Advait Dhakad and I am a student of class XII-D. This is a project on MySQL connectivity
    with Python and Matplotlib.
    The topic I have taken up is Stock Management. I have prepared a stock management programme for a psuedo 
    company Crazy Mobile. It will allow the user to manage purchase, sale and stock of the company along with profits 
    and analysis, supplier info. and customer info. '''
    x.center(20)
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+x)


def close():
    clear = lambda: os.system("cls")
    clear()                     # to clear cmd



pss = input("Enter your SQL password: ")
mycon = sql.connect(host='localhost', user='root', passwd=pss)  # connecting to sql
cursor = mycon.cursor()
qry = "create database IF NOT EXISTS project_try;"                         # giving creation query
cursor.execute(qry)
qry = "use project_try"                                                    # using the database
cursor.execute(qry)


def creating_db():
    # creating tables
    qry1 = '''CREATE TABLE if not exists Realme_Purchase(
               ProdNo int(3) primary key,
               SupplierName varchar(30),
               QTY   int,
               Purchase_time  date,
               AMT int
               );
               '''
    qry2 = '''CREATE TABLE if not exists Realme_Sales(
           SalesNo int(3),
           BuyerName varchar(30),
           QTY   int,
           Sales_time date,
           AMT  int,
           FOREIGN KEY (SalesNo) references Realme_Purchase(ProdNo));'''

    qry3 = '''CREATE TABLE if not exists Apple_Purchase(
                   ProdNo int(3) primary key,
                   SupplierName varchar(30),
                   QTY   int,
                   Purchase_time  date,
                   AMT int
                   );
                   '''
    qry4 = '''CREATE TABLE if not exists Apple_Sales(
               SalesNo int(3),
               BuyerName varchar(30),
               QTY   int,
               Sales_time date,
               AMT  int,
               FOREIGN KEY (SalesNo) references Apple_Purchase(ProdNo));'''

    qry5 = '''CREATE TABLE if not exists OnePlus_Purchase(
                   ProdNo int(3) primary key,
                   SupplierName varchar(30),
                   QTY   int,
                   Purchase_time  date,
                   AMT int
                   );
                   '''
    qry6 = '''CREATE TABLE if not exists OnePlus_Sales(
               SalesNo int(3),
               BuyerName varchar(30),
               QTY   int,
               Sales_time date,
               AMT  int,
               FOREIGN KEY (SalesNo) references OnePlus_Purchase(ProdNo));'''

    qry7 = '''CREATE TABLE if not exists Vivo_Purchase(
                   ProdNo int(3) primary key,
                   SupplierName varchar(30),
                   QTY   int,
                   Purchase_time  date,
                   AMT int
                   );
                   '''
    qry8 = '''CREATE TABLE if not exists Vivo_Sales(
               SalesNo int(3),
               BuyerName varchar(30),
               QTY   int,
               Sales_time date,
               AMT  int,
               FOREIGN KEY (SalesNo) references Vivo_Purchase(ProdNo));'''

    qry9 = '''CREATE TABLE if not exists Customer(
               TradeNo int(3),
               BuyerName varchar(30),
               number  bigint,
               City varchar(20),
               Company  varchar(10)       
               );'''

    qry10 = '''CREATE TABLE if not exists Supplier(
               TradeNo int(3),
               SupplierName varchar(30),
               number  bigint,
               City varchar(20),
               Company  varchar(10)
               );'''
    cursor.execute(qry1)                      # executing the Query
    cursor.execute(qry2)
    cursor.execute(qry3)
    cursor.execute(qry4)
    cursor.execute(qry5)
    cursor.execute(qry6)
    cursor.execute(qry7)
    cursor.execute(qry8)
    cursor.execute(qry9)
    cursor.execute(qry10)


def purchases():                        # purchases section
    while True:
        v = pickle.load(open("v.bat", "rb"))
        print('''
                |======================|
                | 1 - to see tables    |
                | 2 - to add           |
                | 3 - to go to home    |
                |======================|''')
        i = input("Enter your choice: ")
        if i == "1":
            print("\n\tTO DISPLAY ALL PURCHASES\n")
            sqld = "SELECT * from %s_purchase;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            print()
            print()
        elif i == "2":
            Pno = str(input("\t\t\t Enter purchase Number :"))
            Se = str(input("\t\t\tEnter supplier Name :"))
            QTY = str(input("\t\t\t Enter purchase Quantity :"))
            AMT = str(input("\t\t\t Enter purchase Amount :"))
            No = str(input("\t\t\t Enter Phone Number of Supplier :"))
            city = str(input("\t\t\t Enter City of Supplier :"))
            date = str(datetime.date.today())
            try:
                sqld = "INSERT INTO %s_Purchase values ({},'{}',{},'{}',{})".format(Pno, Se, QTY, date, AMT) % (v,)
                cursor.execute(sqld)
                mycon.commit()
                sqld1 = "INSERT INTO SUPPLIER VALUE ({}, '{}', {}, '{}', '{}')".format(Pno, Se, No, city, v)
                cursor.execute(sqld1)
                mycon.commit()
            except mysql.connector.errors.IntegrityError:
                print("Purchase already exist")
                purchases()
            except mysql.connector.errors.ProgrammingError:
                print("You have Entered wrong values")
                purchases()
        elif i == "3":
            main()
            os.remove("v.bat")
            break
        else:
            print("you have entered wrong choice")


def purchases_return():                # purchases return section
    global cnt, tcno, tadd, tcname, ttime
    while True:
        v = pickle.load(open("v.bat", "rb"))
        print('''
                |======================|
                | 1 - to remove        |
                | 2 - to edit          |
                | 3 - to go to home    |
                |======================|''')
        i = input("Enter your choice: ")
        if i == "1":
            sqld = "SELECT * from %s_purchase;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            print("\n\tTO DELETE A Purchase\n")
            code = int(input("\t\t\tEnter Purchase NO :"))
            search = "SELECT count(*) from %s_purchase WHERE ProdNo ={};".format(code) % (v,)
            cursor.execute(search)
            for x in cursor:
                cnt = x[0]
            if cnt == 0:
                print("\t\t\tPurchase with PurchaseNO ID", code, "not found.")
            else:
                sqlq = "DELETE FROM %s_purchase where ProdNo = {};".format(code) % (v,)
                cursor.execute(sqlq)
                print("\t\t\tPurchase was deleted.")
            mycon.commit()

        elif i == "2":
            print("\n\tTO EDIT CUSTOMER INFORMATION\n")
            print("\tYou can edit supplier name, QTY, AMT. \n")
            sqld = "SELECT * from %s_purchase;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            code = int(input("\t\t\tEnter customer id :"))
            search = "select count(*) from %s_purchase WHERE ProdNo={};".format(code) % (v,)
            cursor.execute(search)
            for x in cursor:
                cnt = x[0]
            if cnt == 0:
                print("Purchases with PurchaseNo", code, "not found.")
            else:
                search = "select * from %s_Purchase WHERE ProdNo={};".format(code) % (v,)
                cursor.execute(search)
                for x in cursor:
                    tcname = x[1]
                    tadd = x[2]
                    ttime = x[3]
                    tcno = x[4]
                ncname = input("Enter new supplier name for < " + tcname + " > : ")
                qty = int(input("Enter new Quantity instead of < " + str(tadd) + " > : "))
                print("The Purchase took place on ", ttime, "No need to change")
                amt = int(input("Enter new Amt instead of < " + str(tcno) + " > : "))
                sqlq = '''update %s_Purchase
                           SET SupplierName='{}',QTY='{}',AMt={}
                           WHERE ProdNo={};'''.format(ncname.strip(), qty, amt, code) % (v,)
                cursor.execute(sqlq)
                mycon.commit()
                print("\n Purchases info updated successfully.")

        elif i == "3":
            print("\n")
            main()
            os.remove("v.bat")
            break
        else:
            print("You have entered wrong value")


def sales():
    while True:
        v = pickle.load(open("v.bat", "rb"))
        print('''
                |======================|
                | 1 - to see tables    |
                | 2 - to add           |
                | 3 - to go to home    |
                |======================|''')
        i = input("Enter your choice: ")
        if i == "1":
            print("\n\tTO DISPLAY ALL sales\n")
            sqld = "SELECT * from %s_sales;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            print()
            print()
        elif i == "2":
            s = "select prodno,SUM(QTY) from %s_purchase;" % (v,)
            rf = pd.read_sql(s, mycon)
            print(rf)
            Pno = str(input("\t\t\t Enter Sales Number(Should be same to purchase number) :"))
            Se = str(input("\t\t\tEnter Buyer's Name :"))
            QTY = str(input("\t\t\t Enter sales Quantity(should be less than qty in purchase) :"))
            AMT = str(input("\t\t\t Enter Sales Amount :"))
            No = str(input("\t\t\t Enter Phone Number of Customer :"))
            city = str(input("\t\t\t Enter City of Customer :"))
            date = str(datetime.date.today())
            try:
                sqld = "INSERT INTO %s_sales values ({},'{}',{},'{}',{})".format(Pno, Se, QTY, date, AMT) % (v,)
                cursor.execute(sqld)
                mycon.commit()
                sqld1 = "INSERT INTO Customer VALUE ({}, '{}', {}, '{}', '{}')".format(Pno, Se, No, city, v)
                cursor.execute(sqld1)
                mycon.commit()
            except mysql.connector.errors.ProgrammingError:
                print("You have entered Wrong values ")
                sales()
            except mysql.connector.errors.IntegrityError:
                print("You have entred wrong sales number")
        elif i == "3":
            main()
            os.remove("v.bat")
            break
        else:
            print("you have entered wrong choice")


def sales_return():
    global cnt, tcno, tadd, tcname, ttime
    while True:
        v = pickle.load(open("v.bat", "rb"))
        print('''
                        |======================|
                        | 1 - to remove        |
                        | 2 - to edit          |
                        | 3 - to go to home    |
                        |======================|''')
        i = input("Enter your choice: ")
        if i == "1":
            sqld = "SELECT * from %s_sales;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            print("\n\tTO DELETE A Sales\n")
            code = int(input("\t\t\tEnter sales NO :"))
            search = "SELECT count(*) from %s_sales WHERE salesNo ={};".format(code) % (v,)
            cursor.execute(search)
            for x in cursor:
                cnt = x[0]
            if cnt == 0:
                print("\t\t\tsales with salesNO", code, "not found.")
            else:
                sqlq = "DELETE FROM %s_sales where salesNo = {};".format(code) % (v,)
                cursor.execute(sqlq)
                print("\t\t\tsales was deleted.")
            mycon.commit()

        elif i == "2":
            print("\n\tTO EDIT SALES INFORMATION\n")
            print("\tYou can edit Buyer name, QTY, AMT. \n")
            sqld = "SELECT * from %s_sales;" % (v,)
            df = pd.read_sql(sqld, mycon)
            print(df)
            code = int(input("\t\t\tEnter sales id :"))
            search = "select count(*) from %s_sales WHERE SalesNo={};".format(code) % (v,)
            cursor.execute(search)
            for x in cursor:
                cnt = x[0]
            if cnt == 0:
                print("sales with salesNo", code, "not found.")
            else:
                search = "select * from %s_sales WHERE SalesNo={};".format(code) % (v,)
                cursor.execute(search)
                for x in cursor:
                    tcname = x[1]
                    tadd = x[2]
                    ttime = x[3]
                    tcno = x[4]
                ncname = input("Enter new Buyer name for < " + tcname + " > : ")
                qty = int(input("Enter new Quantity instead of < " + str(tadd) + " > : "))
                print("The sales took place on ", ttime, "No need to change")
                amt = int(input("Enter new Amt instead of < " + str(tcno) + " > : "))
                sqlq = '''update %s_sales
                               SET BuyerName='{}',QTY='{}',AMt={}
                               WHERE salesNo={};'''.format(ncname.strip(), qty, amt, code) % (v,)
                cursor.execute(sqlq)
                mycon.commit()
                print("\n sales info updated successfully.")

        elif i == "3":
            print("\n")
            main()
            os.remove("v.bat")
            break
        else:
            print("You have entered wrong value")


def analysis():
    a_purchase = pd.read_sql("select * from apple_purchase;", mycon)
    o_purchase = pd.read_sql("select * from oneplus_purchase;", mycon)
    r_purchase = pd.read_sql("select * from realme_purchase;", mycon)
    v_purchase = pd.read_sql("select * from vivo_purchase;", mycon)
    a_sales = pd.read_sql("select * from apple_sales", mycon)
    o_sales = pd.read_sql("select * from oneplus_sales;", mycon)
    r_sales = pd.read_sql("select * from realme_sales;", mycon)
    v_sales = pd.read_sql("select * from vivo_sales;", mycon)
    pa = a_purchase["QTY"]
    po = o_purchase["QTY"]
    pr = r_purchase["QTY"]
    pv = v_purchase["QTY"]
    sa = a_sales["QTY"]
    so = o_sales["QTY"]
    sr = r_sales["QTY"]
    sv = v_sales["QTY"]
    pp = pa.sum(axis=0, skipna=True) - sa.sum(axis=0, skipna=True)
    op = po.sum(axis=0, skipna=True) - so.sum(axis=0, skipna=True)
    rp = pr.sum(axis=0, skipna=True) - sr.sum(axis=0, skipna=True)
    vp = pv.sum(axis=0, skipna=True) - sv.sum(axis=0, skipna=True)
    pa = a_purchase["AMT"]
    po = o_purchase["AMT"]
    pr = r_purchase["AMT"]
    pv = v_purchase["AMT"]
    sa = a_sales["AMT"]
    so = o_sales["AMT"]
    sr = r_sales["AMT"]
    sv = v_sales["AMT"]
    ps = sa.sum(axis=0, skipna=True) - pa.sum(axis=0, skipna=True)
    ns = so.sum(axis=0, skipna=True) - po.sum(axis=0, skipna=True)
    rs = sr.sum(axis=0, skipna=True) - pr.sum(axis=0, skipna=True)
    vs = sv.sum(axis=0, skipna=True) - pv.sum(axis=0, skipna=True)
    while True:
        print('''
                |=======================|
                | 1 - FOR STOCKS        |
                | 2 - FOR PROFITS       |
                | 3 - FOR COMPARISON    |
                | 4 - TO GO BACK        |
                |=======================|''')
        choice = input("Enter Your Choice: ")
        if choice == "4":
            main()
        elif choice == "2":
            print("Profits of apple: ", ps)
            print("Profits of oneplus: ", ns)
            print("Profits of realme: ", rs)
            print("Profits of vivo: ", vs)
            print("Total PROFITS: ", (ps + ns + rs + vs))
            la = ["Apple", "Oneplus", "Realme", "Vivo"]
            plt.title("Profit share of each company")
            plt.xlabel("Company")
            plt.ylabel("Profit (in INR)")
            v = [ps, ns, rs, vs]
            i = [1, 2, 3, 4]
            plt.plot(la, v, marker="o")
            plt.show()
        elif choice == "1":
            print("STOCKS of apple: ", pp)
            print("STOCKS of oneplus: ", op)
            print("STOCKS of realme: ", rp)
            print("STOCKS of vivo: ", vp)
            print("total STOCKS:", (pp+op+rp+vp))
            la = ["Apple", "Oneplus", "Realme", "Vivo"]
            plt.title("STOCKS share of each company")
            plt.ylabel("Number of Stock")
            plt.xlabel("Companies")
            v = [pp, op, rp, vp]
            plt.plot(la, v, marker="o")
            plt.show()
        elif choice == "3":
            while True:
                print('''
                    |=================|
                    | 1 - FOR PROFITS |
                    | 2 - FOR STOCKS  |
                    | 3 - TO GO BACK  |
                    |=================|
                    ''')
                c = input("Enter the choice for Comparison: ")
                if c == "1":
                    plt.figure(figsize=(7, 6))
                    plt.xlabel("MONTHS")
                    plt.ylabel("AMT")
                    r = np.arange(4)
                    plt.title("Profits Comparison")
                    print("""
                    |==========================|
                    |    COMPANIES AVAILABLE   |
                    | 1 - FOR REALME           |
                    | 2 - FOR APPLE            |
                    | 3 - FOR ONEPLUS          |
                    | 4 - FOR VIVO             |
                    |==========================|""")
                    a = input("Enter you want to compare: ")
                    b = input("Enter you want to compare with: ")
                    if a == "1":
                        dt = [rs / 4, rs / 3, rs / 2, rs]
                        plt.bar(r + 0.0, dt, width=0.25, label="Realme")
                        if b == "2":
                            dt1 = [ps/4, ps/3, ps/2, ps]
                            plt.bar(r+0.25, dt1, width=0.25, label="Apple")
                        elif b == "3":
                            dt1 = [ns / 4, ns / 3, ns / 2, ns]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "4":
                            dt1 = [vs / 4, vs / 3, vs / 2, vs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "2":
                        dt = [ps / 4, ps / 3, ps / 2, ps]
                        plt.bar(r + 0.0, dt, width=0.25, label="Apple")
                        if b == "1":
                            dt1 = [rs / 4, rs / 3, rs / 2, rs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        elif b == "3":
                            dt1 = [ns / 4, ns / 3, ns / 2, ns]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "4":
                            dt1 = [vs / 4, vs / 3, vs / 2, vs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "3":
                        dt = [ns / 4, ns / 3, ns / 2, ns]
                        plt.bar(r + 0.0, dt, width=0.25, label="OnePlus")
                        if b == "2":
                            dt1 = [ps / 4, ps / 3, ps / 2, ps]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Apple")
                        elif b == "1":
                            dt1 = [rs / 4, rs / 3, rs / 2, rs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        elif b == "4":
                            dt1 = [vs / 4, vs / 3, vs / 2, vs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "4":
                        dt = [vs / 4, vs / 3, vs / 2, vs]
                        plt.bar(r + 0.0, dt, width=0.25, label="Vivo")
                        if b == "2":
                            dt1 = [ps / 4, ps / 3, ps / 2, ps]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Apple")
                        elif b == "3":
                            dt1 = [ns / 4, ns / 3, ns / 2, ns]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "1":
                            dt1 = [rs / 4, rs / 3, rs / 2, rs]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    else:
                        print("Enter correct value")
                    plt.xticks(r, ["Q1", "Q2", "Q3", "Q4"])
                    plt.legend(loc="best")
                    plt.show()
                    dt1 = []
                    dt = []
                elif c == "2":
                    plt.figure(figsize=(7, 6))
                    plt.xlabel("MONTHS")
                    plt.ylabel("QTY")
                    r = np.arange(4)
                    plt.title("Profits Comparison")
                    print("""
                    |==========================|
                    |    COMPANIES AVAILABLE   |
                    | 1 - FOR REALME           |
                    | 2 - FOR APPLE            |
                    | 3 - FOR ONEPLUS          |
                    | 4 - FOR VIVO             |
                    |==========================|""")
                    a = input("Enter you want to compare: ")
                    b = input("Enter you want to compare with: ")
                    if a == "1":
                        dt = [rp / 4, rp / 3, rp / 2, rp]
                        plt.bar(r + 0.0, dt, width=0.25, label="Realme")
                        if b == "2":
                            dt1 = [pp/4, pp/3, pp/2, pp]
                            plt.bar(r+0.25, dt1, width=0.25, label="Apple")
                        elif b == "3":
                            dt1 = [op / 4, op / 3, op / 2, op]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "4":
                            dt1 = [vp / 4, vp / 3, vp / 2, vp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "2":
                        dt = [pp / 4, pp / 3, pp / 2, pp]
                        plt.bar(r + 0.0, dt, width=0.25, label="Apple")
                        if b == "1":
                            dt1 = [rp / 4, rp / 3, rp / 2, rp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        elif b == "3":
                            dt1 = [op / 4, op / 3, op / 2, op]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "4":
                            dt1 = [vp / 4, vp / 3, vp / 2, vp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "3":
                        dt = [op / 4, op / 3, op / 2, op]
                        plt.bar(r + 0.0, dt, width=0.25, label="OnePlus")
                        if b == "2":
                            dt1 = [pp / 4, pp / 3, pp / 2, pp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Apple")
                        elif b == "1":
                            dt1 = [rp / 4, rp / 3, rp / 2, rp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        elif b == "4":
                            dt1 = [vp / 4, vp / 3, vp / 2, vp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Vivo")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    elif a == "4":
                        dt = [vp / 4, vp / 3, vp / 2, vp]
                        plt.bar(r + 0.0, dt, width=0.25, label="Vivo")
                        if b == "2":
                            dt1 = [pp / 4, pp / 3, pp / 2, pp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Apple")
                        elif b == "3":
                            dt1 = [op / 4, op / 3, op / 2, op]
                            plt.bar(r + 0.25, dt1, width=0.25, label="OnePlus")
                        elif b == "1":
                            dt1 = [rp / 4, rp / 3, rp / 2, rp]
                            plt.bar(r + 0.25, dt1, width=0.25, label="Realme")
                        else:
                            print("Enter correct value for B \nPrinted output as seen viable")
                    else:
                        print("Enter correct value")
                    plt.xticks(r, ["Q1", "Q2", "Q3", "Q4"])
                    plt.legend(loc="best")
                    plt.show()
                    dt1 = []
                    dt = []
                elif c == "3":
                    analysis()
                else:
                    print("Enter Correct Value")


def supp_info():
    while True:
        print("""
        |=================================|
        |1 - TO SEE SUPPLIER INFORMATION  |
        |2 - TO EDIT SUPPLIER INFORMATION |
        |3 - TO GO BACK                   |
        |=================================|""")
        choice = input("Enter your Choice: ")
        if choice == "1":
            print("\n\tTO DISPLAY SUPPLIER\n")
            sqld = "SELECT * from Supplier;"
            df = pd.read_sql(sqld, mycon)
            print(df)
            print()
            print()
        elif choice == "3":
            main()
        elif choice == "2":
                print("\n\tTO EDIT SUPPLIER INFORMATION\n")
                print("\tYou can edit  phone number, city. \n")
                sqld = "SELECT * from supplier;"
                df = pd.read_sql(sqld, mycon)
                print(df)
                code = int(input("\t\t\tEnter TradeNo id :"))
                search = "select count(*) from Supplier WHERE TradeNo={};".format(code)
                cursor.execute(search)
                for x in cursor:
                    cnt = x[0]

                if cnt == 0:

                    print("Supplier with TradeNo", code, "not found.")
                else:
                    search = "select * from Supplier WHERE TradeNo={};".format(code)
                    cursor.execute(search)
                    for x in cursor:
                        tcity = x[3]
                        tadd = x[2]
                    pho = int(input("Enter new Number instead of < " + str(tadd) + " > : "))
                    city = input("Enter new New city name for < " + tcity + " > : ")
                    sqlq = '''update supplier
                                   SET number='{}',city='{}'
                                   WHERE TradeNo={};'''.format(pho, city.strip(), code)
                    cursor.execute(sqlq)
                    mycon.commit()
                    print("\n Supplier info updated successfully.")

        else:
            print("Enter correct value")


def search_all():
    while True:
        print("\tTO SEARCH IN ALL TABLES")
        print('''
                 |=============================|
                 | 1 - search by ProdNo/SalesNo|
                 | 2 - search by name          |
                 | 3 - To GO BACK              |
                 |=============================|
    ''')
        choice = input("Enter Your Choice: ")
        if choice == "1":
            code = input("\t\t\tEnter ProdNo :")
            p = ["apple_purchase", "oneplus_purchase", "realme_purchase", "Vivo_purchase"]
            s = ["apple_sales", "oneplus_sales", "realme_sales", "Vivo_sales"]
            e = ["customer", "supplier"]
            for v in p:
                try:
                    search = "SELECT * FROM %s where prodno = %s;" % (v, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
            for xy in e:
                try:
                    search = "SELECT * FROM %s where TradeNo = %s;" % (xy, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
            for v in s:
                try:
                    search = "SELECT * FROM %s where salesno = %s;" % (v, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
        elif choice == "2":
            code = str(input("\t\t\tEnter Name or initials :"))
            p = ["apple_purchase", "oneplus_purchase", "realme_purchase", "Vivo_purchase"]
            s = ["apple_sales", "oneplus_sales", "realme_sales", "Vivo_sales"]
            e = ["customer", "supplier"]
            for v in p:
                try:
                    search = "SELECT * FROM %s where SupplierName like '%s%%';" % (v, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
            for xy in e:
                try:
                    search = "SELECT * FROM %s where TradeNo like '%s%%';" % (xy, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
            for v in s:
                try:
                    search = "SELECT * FROM %s where BuyerName like '%s%%';" % (v, code,)
                    mdf = pd.read_sql(search, mycon)
                    a = mdf.empty
                    if a == False:
                        print("\n", mdf, "\n")
                except mysql.connector.Error as err:
                    print(err)
        elif choice == "3":
            main()
            os.remove("v.bat")
            break
        else:
            print("you have entered wrong choice")


def cust_info():
    while True:
        print("""
        |=================================|
        |1 - TO SEE CUSTOMER INFORMATION  |
        |2 - TO EDIT CUSTOMER INFORMATION |
        |3 - TO GO BACK                   |
        |=================================|""")
        choice = input("Enter your Choice: ")
        if choice == "1":
            print("\n\tTO DISPLAY CUSTOMER\n")
            sqld = "SELECT * from customer;"
            df = pd.read_sql(sqld, mycon)
            print(df)
            print()
            print()
        elif choice == "3":
            main()
        elif choice == "2":
                print("\n\tTO EDIT CUSTOMER INFORMATION\n")
                print("\tYou can edit  phone number, city. \n")
                sqld = "SELECT * from Customer;"
                df = pd.read_sql(sqld, mycon)
                print(df)
                code = int(input("\t\t\tEnter TradeNo id :"))
                search = "select count(*) from Customer WHERE TradeNo={};".format(code)
                cursor.execute(search)
                for x in cursor:
                    cnt = x[0]

                if cnt == 0:

                    print("Supplier with TradeNo", code, "not found.")
                else:
                    search = "select * from Customer WHERE TradeNo={};".format(code)
                    cursor.execute(search)
                    for x in cursor:
                        tcity = x[3]
                        tadd = x[2]
                    pho = int(input("Enter new Number instead of < " + str(tadd) + " > : "))
                    city = input("Enter new New city name for < " + tcity + " > : ")
                    sqlq = '''update Customer
                                   SET number='{}',city='{}'
                                   WHERE TradeNo={};'''.format(pho, city.strip(), code)
                    cursor.execute(sqlq)
                    mycon.commit()
                    print("\n Customer info updated successfully.")

        else:
            print("Enter correct value")


def main():
    close()
    print(Fore.MAGENTA+Style.BRIGHT+
        '''
__          ________ _      _____ ____  __  __ ______   _______ ____  
\ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \ 
 \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | |
  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | |
   \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| |
    \/  \/   |______|______\_____\____/|_|  |_|______|    |_|  \____/ 
                                                                      
                                                                      
  _____ _____             ________     __
 / ____|  __ \     /\    |___  /\ \   / /
| |    | |__) |   /  \      / /  \ \_/ / 
| |    |  _  /   / /\ \    / /    \   /  
| |____| | \ \  / ____ \  / /__    | |   
 \_____|_|  \_\/_/    \_\/_____|   |_|   
                                         
                                         
 __  __  ____  ____ _____ _      ______ 
|  \/  |/ __ \|  _ \_   _| |    |  ____|
| \  / | |  | | |_) || | | |    | |__   
| |\/| | |  | |  _ < | | | |    |  __|  
| |  | | |__| | |_) || |_| |____| |____ 
|_|  |_|\____/|____/_____|______|______|
''')
    while True:
        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
            |==========================|
            | 1 - FOR REALME           |
            | 2 - FOR APPLE            |
            | 3 - FOR ONEPLUS          |
            | 4 - FOR VIVO             |
            | 5 - FOR GLOBAL SEARCH    |
            | 6 - FOR ANALYSIS         |
            | 7 - FOR SUPPLIER INFO    |
            | 8 - FOR CUSTOMER INFO    |
            | 9 - TO EXIT              |
            |==========================|''')
        choice = input("Enter your choice: ")
        if choice == "1":
            print(Fore.YELLOW+'''                                       ,--,                              
                                        ,---.'|             ____             
    ,-.----.       ,---,.   ,---,       |   | :           ,'  , `.    ,---,. 
    \    /  \    ,'  .' |  '  .' \      :   : |        ,-+-,.' _ |  ,'  .' | 
    ;   :    \ ,---.'   | /  ;    '.    |   ' :     ,-+-. ;   , ||,---.'   | 
    |   | .\ : |   |   .':  :       \   ;   ; '    ,--.'|'   |  ;||   |   .' 
    .   : |: | :   :  |-,:  |   /\   \  '   | |__ |   |  ,', |  '::   :  |-, 
    |   |  \ : :   |  ;/||  :  ' ;.   : |   | :.'||   | /  | |  ||:   |  ;/| 
    |   : .  / |   :   .'|  |  ;/  \   \'   :    ;'   | :  | :  |,|   :   .' 
    ;   | |  \ |   |  |-,'  :  | \  \ ,'|   |  ./ ;   . |  ; |--' |   |  |-, 
    |   | ;\  \'   :  ;/||  |  '  '--'  ;   : ;   |   : |  | ,    '   :  ;/| 
    :   ' | \.'|   |    \|  :  :        |   ,/    |   : '  |/     |   |    \ 
    :   : :-'  |   :   .'|  | ,'        '---'     ;   | |`-'      |   :   .' 
    |   |.'    |   | ,'  `--''                    |   ;/          |   | ,'   
    `---'      `----'                             '---'           `----'     

    ''')
            v = "Realme"
            pickle.dump(v, open("v.bat", "wb"))
            break
        elif choice == "2":
            print(Fore.RED+'''
                                        ,--,              
               ,-.----.   ,-.----.   ,---.'|              
   ,---,       \    /  \  \    /  \  |   | :       ,---,. 
  '  .' \      |   :    \ |   :    \ :   : |     ,'  .' | 
 /  ;    '.    |   |  .\ :|   |  .\ :|   ' :   ,---.'   | 
:  :       \   .   :  |: |.   :  |: |;   ; '   |   |   .' 
:  |   /\   \  |   |   \ :|   |   \ :'   | |__ :   :  |-, 
|  :  ' ;.   : |   : .   /|   : .   /|   | :.'|:   |  ;/| 
|  |  ;/  \   \;   | |`-' ;   | |`-' '   :    ;|   :   .' 
'  :  | \  \ ,'|   | ;    |   | ;    |   |  ./ |   |  |-, 
|  |  '  '--'  :   ' |    :   ' |    ;   : ;   '   :  ;/| 
|  :  :        :   : :    :   : :    |   ,/    |   |    \ 
|  | ,'        |   | :    |   | :    '---'     |   :   .' 
`--''          `---'.|    `---'.|              |   | ,'   
                 `---`      `---`              `----'   ''')
            v = "Apple"
            pickle.dump(v, open("v.bat", "wb"))
            break
        elif choice == "3":
            print(Fore.CYAN+"""                                      
        ,----..            ,--.           
       /   /   \         ,--.'|    ,---,. 
      /   .     :    ,--,:  : |  ,'  .' | 
     .   /   ;.  \,`--.'`|  ' :,---.'   | 
    .   ;   /  ` ;|   :  :  | ||   |   .' 
    ;   |  ; \ ; |:   |   \ | ::   :  |-, 
    |   :  | ; | '|   : '  '; |:   |  ;/| 
    .   |  ' ' ' :'   ' ;.    ;|   :   .' 
    '   ;  \; /  ||   | | \   ||   |  |-, 
     \   \  ',  / '   : |  ; .''   :  ;/| 
      ;   :    /  |   | '`--'  |   |    \ 
       \   \ .'   '   : |      |   :   .' 
        `---`     ;   |.'      |   | ,'   
                  '---'        `----'     

                  ,--,                             
    ,-.----.   ,---.'|                             
    \    /  \  |   | :                  .--.--.    
    |   :    \ :   : |            ,--, /  /    '.  
    |   |  .\ :|   ' :          ,'_ /||  :  /`. /  
    .   :  |: |;   ; '     .--. |  | :;  |  |--`   
    |   |   \ :'   | |__ ,'_ /| :  . ||  :  ;_     
    |   : .   /|   | :.'||  ' | |  . . \  \    `.  
    ;   | |`-' '   :    ;|  | ' |  | |  `----.   \ 
    |   | ;    |   |  ./ :  | | :  ' ;  __ \  \  | 
    :   ' |    ;   : ;   |  ; ' |  | ' /  /`--'  / 
    :   : :    |   ,/    :  | : ;  ; |'--'.     /  
    |   | :    '---'     '  :  `--'   \ `--'---'   
    `---'.|              :  ,      .-./            
      `---`               `--`----' """)
            v = "Oneplus"
            pickle.dump(v, open("v.bat", "wb"))
            break
        elif choice == "4":
            print(Fore.BLUE+'''
                                               
                                    ,----..    
               ,---,               /   /   \   
       ,---.,`--.' |       ,---.  /   .     :  
      /__./||   :  :      /__./| .   /   ;.  \ 
 ,---.;  ; |:   |  ' ,---.;  ; |.   ;   /  ` ; 
/___/ \  | ||   :  |/___/ \  | |;   |  ; \ ; | 
\   ;  \ ' |'   '  ;\   ;  \ ' ||   :  | ; | ' 
 \   \  \: ||   |  | \   \  \: |.   |  ' ' ' : 
  ;   \  ' .'   :  ;  ;   \  ' .'   ;  \; /  | 
   \   \   '|   |  '   \   \   ' \   \  ',  /  
    \   `  ;'   :  |    \   `  ;  ;   :    /   
     :   \ |;   |.'      :   \ |   \   \ .'    
      '---" '---'         '---"     `---` ''')
            v = "Vivo"
            pickle.dump(v, open("v.bat", "wb"))
            break
        elif choice == "5":
            print("You have selected global search")
            search_all()
            break
        elif choice == "6":
            print("you have selected analysis")
            analysis()
            break
        elif choice == "7":
            print("You have selected Supplier Information")
            supp_info()
        elif choice == "8":
            print("YOU have selected  Customer Information")
            cust_info()
        elif choice == "9":
            print("you have selected to exit")
            acknowledgements()

            print(Fore.LIGHTMAGENTA_EX+'''
 _______ _    _          _   _ _  __ __     ______  _    _ 
|__   __| |  | |   /\   | \ | | |/ / \ \   / / __ \| |  | |
   | |  | |__| |  /  \  |  \| | ' /   \ \_/ / |  | | |  | |
   | |  |  __  | / /\ \ | . ` |  <     \   /| |  | | |  | |
   | |  | |  | |/ ____ \| |\  | . \     | | | |__| | |__| |
   |_|  |_|  |_/_/    \_\_| \_|_|\_\    |_|  \____/ \____/ 
                                                           
                                                           
''')

            effect()
            os.system("taskkill -im cmd.exe")
        else:
            print("you have entered wrong value")
    while True:
        print('''
                |========================|
                | 1 - FOR PURCHASES      |
                | 2 - FOR PURCHASE RETURN|
                | 3 - FOR SALES          |
                | 4 - FOR SALES RETURN   |
                |========================|''')
        choice = input("ENTER YOUR CHOICE: ")
        if choice == "1":
            print("you have selected purchases")
            purchases()
            break
        elif choice == "2":
            print("you have selected purchase return")
            purchases_return()
            break
        elif choice == "3":
            print("you have selected sales")
            sales()
            break
        elif choice == "4":
            print("you have selected sales return")
            sales_return()
            break
        else:
            print("you have entered wrong choice please enter again")


close()
introduction()
effect()
creating_db()
main()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pymysql
import pandas as a
conn=pymysql.connect(host='localhost',port=int(3306),user='root',passwd='root',db='Online_Shop')
def initDB():
    mycursor = conn.cursor()
def displayOrderMenu():
    print('------- MENU -------')
    print('  1. Register yourself with us')
    print('  2. Show Products')
    print('  3. Show Orders')
    print('  4. Show Payment History')
    print('  5. Add/Veiw Sellers')
    print('  9. Go back to previous menu')
    print('--------------------')
    
def displayAnalysisMenu():
    print('------- Analysis-------')
    print('  1. Customers Per Year')
    print('  2. Delivery Time')
    print('  3. Review Scores')
    print('  4. Popular Payment Methods')
    print('  5. Payment Installments')
    print('  6. Revenue')
    print('  9. Go back to previous menu')
    print('--------------------')

def displayMainMenu():
    print('------- MENU -------')
    print('  1. Shop with us')
    print('  2. See our Stats')
    print('  9. Exit')
    print('--------------------')

def analysisRun():
    displayAnalysisMenu()
    n = int(input("Enter option : "))
    if n == 1:
        os.system('cls')  # For Windows
        customers_per_year()
    elif n == 2:
        os.system('cls')
        average_delivery_time()
    elif n == 3:
        os.system('cls')
        average_review_score()
    elif n == 4:
        os.system('cls')
        popular_payment_method()
    elif n == 5:
        os.system('cls')
        payment_installments()
    elif n == 6:
        os.system('cls')
        average_revenue()
    elif n == 9:
        os.system('cls')
        run()
    else:
        os.system('cls')
        analysisRun()

def exit():
    n = int(input(" Press 9 to go back to previous menu : "))

    if n == 9:
        os.system('cls')  # For Windows
        orderRun()
    else:
        print(" Invalid Option")
        exit()
def goBack():
    n = int(input(" Press 9 to go back to previous menu : "))

    if n == 9:
        os.system('cls')  # For Windows
        analysisRun()
    else:
        print(" Invalid Option")
        exit()

        
def Register():
    
    print('------ User Registration ------\n')
    uniqueID =  input('Enter user name : ')
    city =  input('Enter your city : ')
    state = input('Enter your state : ')
    postal = input('Enter your zip-code : ')
    mycursor = conn.cursor()
    sql = 'INSERT INTO customers (`customer_id`,`customer_unique_id`,`customer_zip_code`,`customer_city`,`customer_state`) VALUES (%s,%s,%s,%s,%s)'
    val = (uniqueID,uniqueID,postal,city,state)
    mycursor.execute(sql,val)
    conn.commit()

    print('------ SUCCESS ------\n')
    exit()

        
def showProducts():
    
    mycursor = conn.cursor()
    print('------ Now choose from thousands of brands ------\n')
    print('------ 1. Shop by category ------\n')
    print('------ 2. Shop by price ------\n')
    n = int(input(" Enter your choice: "))
    if n == 1:
        os.system('cls')  # For Windows
        mycursor.execute("SELECT DISTINCT product_category_name from products")
        product_list = mycursor.fetchall()
        i = 0
        if len(product_list) == 0:
            print(" No product categories exist")
        else:
            for category in product_list:
                i += 1
                print(i,": ", category[0])
            print('------ Enter the category name from above------\n')
            s=input()
            sql="SELECT DISTINCT product_id from products where product_category_name= '" +s+"'"
            mycursor.execute(sql)
            products = mycursor.fetchall()
            if len(products) == 0:
                print("No products of this category exist")
            else:
                print('------ The available products are ------\n')
                i = 0
                for p in products:
                    i += 1
                    print(i,": ", p[0])

        
    elif n == 2:
        os.system('cls')
        print('------ Enter the maximum price range------\n')
        max_range=input()
        print('------ Enter the minimum price range------\n')
        min_range=input()
        sql="SELECT  products.product_id from products inner join order_items on products.product_id=order_items.product_id where price <='" +max_range+"' and price >='"+min_range+"'"
        mycursor.execute(sql)
        inrange = mycursor.fetchall()
        if len(inrange) == 0:
            print("No products of this category exist")
        else:
            i = 0
            for p in inrange:
                i += 1
                print(i,": ", p[0])
                print("\n")
    print('------ SUCCESS ------\n')
    exit()

def showOrders():
    
    mycursor = conn.cursor()
    print('------ Now choose from thousands of brands ------\n')
    print('------ 1. Search your order status ------\n')
    print('------ 2. Show previous orders ------\n')
    n = int(input(" Enter your choice: "))
    c_id=input("Please enter your customer_id : ")
    print("\n")
    if n == 1:
        os.system('cls')  # For Windows
        sql="SELECT order_status,order_id,order_delivered_customer_date from orders inner join customers on orders.customer_id= customers.customer_id where orders.customer_id = '"+c_id+"'"
        mycursor.execute(sql)
        o_list = mycursor.fetchall()
        i = 0
        for o in o_list:
            i += 1
            print("Your order status for order_id: ",o[1], "is", o[0],"on",o[2])
            s=o[1]
            print("\n")
            sql1="SELECT review_comment_message from reviews where order_id= '" +s+"'"
            mycursor.execute(sql1)
            reviewss = mycursor.fetchall()
            if len(reviewss) == 0:
                print("No review for this product exist")
            else:
                i = 0
                for r in reviewss:
                    i += 1
                    print("Your entered review for this product is -: ", r[0])
                    n = int(input(" Press 8 to update review or 9 to exit: "))
                    if n == 8:
                        up = input(" Enter your review: ")
                        sql1="Update reviews set review_comment_message =' " +up+ "' where order_id='" +s+"'"
                        mycursor.execute(sql1) 
                        conn.commit()
                    elif n==9:
                        orderRun()
                        return

                    

        
    elif n == 2:
        os.system('cls')
        print('------ Enter the order month------\n')
        range=input()
        sql="SELECT order_id from orders where Month(order_purchase_timestamp) ='" +range+"' and customer_id='"+c_id+"'"
        mycursor.execute(sql)
        inrange = mycursor.fetchall()
        if len(inrange) == 0:
            print("No orders were made in this month")
        else:
            i = 0
            for p in inrange:
                i += 1
                print("Order_id for orders in this month are: ", p[0])
    print('------ SUCCESS ------\n')
    exit()
        

def paymentHistory():
    
    mycursor = conn.cursor()
    o_id=input("Please enter your order_id")
    print('------ Search by ------\n')
    print('------ 1. by order_id ------\n')
    print('------ 2. by payment_type ------\n')
    n = int(input(" Enter your choice: "))
    if n == 1:
        os.system('cls')  # For Windows
        sql="SELECT payment_value,payment_type from order_payments where order_id ='"+o_id+"'"
        mycursor.execute(sql)
        o_list = mycursor.fetchall()
        i = 0
        for o in o_list:
            i += 1
            print("Amount: ", o[0])
            print("mode: ", o[1])

        
    elif n == 2:
        os.system('cls')
        print('------ Enter the payment method------\n')
        range=input()
        sql="SELECT payment_value from order_payments where payment_type='" +range+"' and order_id='"+o_id+"'"
        mycursor.execute(sql)
        inrange = mycursor.fetchall()
        if len(inrange) == 0:
            print("No orders were made using this payment method")
        else:
            i = 0
            for p in inrange:
                i += 1
                print("Payment value for order: "+o_id+ " is ",p[0])
    print('------ SUCCESS ------\n')
    exit()

def addSeller():
    #print('------ Now choose from thousands of brands ------\n')
    mycursor = conn.cursor()
    print('------ 1. Register as seller ------\n')
    print('------ 2. View sellers at your location ------\n')
    n = int(input(" Enter your choice: "))
    if n == 1:
        print('------ Seller Registration ------\n')
        uniqueID =  input('Enter user name : ')
        city =  input('Enter your city : ')
        state = input('Enter your state : ')
        postal = input('Enter your zip-code : ')
        sql = 'INSERT INTO seller (`seller_id`,`seller_zip_code`,`seller_city`,`seller_state`) VALUES (%s,%s,%s,%s)'
        val = (uniqueID,postal,city,state)
        mycursor.execute(sql,val)
        conn.commit()
    elif n == 2:
        s = input(" Enter your state: ")
        sql="SELECT seller_id from sellers where seller_state = '" +s+"'"
        mycursor.execute(sql)
        inrange = mycursor.fetchall()
        if len(inrange) == 0:
            print("Sorry ! No sellers available at this location")
        else:
            i = 0
            for p in inrange:
                i += 1
                print("Seller_id:- ", p[0])

    print('------ SUCCESS ------\n')
    exit()
    

def customers_per_year(): #p1
    mycursor = conn.cursor()
    print('------ As per are latest dataset the customers per year stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT YEAR(order_purchase_timestamp) AS Year ,COUNT(DISTINCT customer_unique_id) FROM customers JOIN orders ON customers.customer_id = orders.customer_id GROUP BY year;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        print("Year: ", r[0])
        print("Number of customers: ", r[1])
        print("\n")
        #print()
    goBack()

def average_delivery_time(): #p2

    mycursor = conn.cursor()
    print('------ As per are latest dataset the average delivery time stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT ROUND(SUM(IF(TIMESTAMPDIFF(day,order_purchase_timestamp,order_delivered_customer_date) <= 3,1,0))/COUNT(order_id)*100,2),ROUND(SUM(IF(TIMESTAMPDIFF(day,order_purchase_timestamp,order_delivered_customer_date) BETWEEN 4 AND 5,1,0))/COUNT(order_id)*100,2),ROUND(SUM(IF(TIMESTAMPDIFF(day,order_purchase_timestamp,order_delivered_customer_date) BETWEEN 6 AND 14,1,0))/COUNT(order_id)*100,2) ,ROUND(SUM(IF(TIMESTAMPDIFF(day,order_purchase_timestamp,order_delivered_customer_date) > 14,1,0))/COUNT(order_id)*100,2) FROM orders WHERE order_status = 'delivered' AND order_delivered_customer_date != '0000-00-00 00:00:00' AND TIMESTAMPDIFF(day,order_purchase_timestamp,order_delivered_customer_date) >= 0;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        print("In 3 days: ", r[0])
        print("In a week: ", r[1])
        print("In Two weeks: ", r[2])
        print("In three weeks: ", r[3])
        print("\n")
        #print()
    goBack()

def average_review_score(): #p3

    mycursor = conn.cursor()
    print('------ As per are latest dataset the average delivery time stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT SUM(IF(review_score = 1,1,0)), SUM(IF(review_score = 2,1,0)), SUM(IF(review_score = 3,1,0)), SUM(IF(review_score = 4,1,0)),SUM(IF(review_score = 5,1,0)) FROM (SELECT order_status, review_score FROM orders JOIN reviews ON orders.order_id = reviews.order_id) a"    
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        print("1 star: ", r[0])
        print("2 star: ", r[1])
        print("3 star: ", r[2])
        print("4 star: ", r[3])
        print("5 star: ", r[4])
        print("\n")
        #print()
    goBack()

def popular_payment_method(): #p4

    mycursor = conn.cursor()
    print('------ As per are latest dataset the popular payment method stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT payment_type,COUNT(order_id) AS num_payments FROM order_payments GROUP BY payment_type ORDER BY num_payments DESC;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        if r[0]!='1' and r[0]!='NA':
            print(r[0]," : ", r[1])
    goBack()
        
def payment_installments(): #p4

    mycursor = conn.cursor()
    print('------ As per are latest dataset the average number of installment stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT MIN(payment_installments),AVG(payment_installments),MAX(payment_installments) FROM order_payments;"    
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        print("Minimum Number of installments: ", r[0])
        print("Average Number of installments: ", r[1])
        print("Maximum Number of installments: ", r[2])
        print("\n")
    goBack()

def average_revenue(): #p5

    mycursor = conn.cursor()
    print('------ As per are latest dataset the average revenue stats are ------\n')
    os.system('cls')  # For Windows
    sql="SELECT YEAR(order_purchase_timestamp) AS year, SUM(revenue) FROM (SELECT order_id, ROUND(SUM(price) + SUM(freight_value),2) AS revenue FROM order_items GROUP BY order_id) a JOIN orders ON a.order_id = orders.order_id WHERE order_status = 'delivered' GROUP BY year ORDER BY year;"    
    mycursor.execute(sql)
    result = mycursor.fetchall()
    i = 0
    for r in result:
        i += 1
        print(r[0]," : ", r[1])   
    goBack()

def run():
    displayMainMenu()
    n = int(input("Enter option : "))
    if n == 1:
        os.system('cls')  # For Windows
        orderRun()
    elif n == 2:
        os.system('cls')
        analysisRun()
    elif n == 9:
        os.system('cls')
        print('----- Thank You -----')
    else:
        os.system('cls')
        run()
def orderRun():
    displayOrderMenu()
    n = int(input("Enter option : "))
    if n == 1:
        os.system('cls')  # For Windows
        Register()
    elif n == 2:
        os.system('cls')
        showProducts()
    elif n == 3:
        os.system('cls')
        showOrders()
    elif n == 4:
        os.system('cls')
        paymentHistory()
    elif n == 5:
        os.system('cls')
        addSeller()
    elif n == 9:
        os.system('cls')
        run()
    else:
        os.system('cls')
        orderRun()
        

    
    
if __name__ == '__main__':
    #initDB()
    run()
    #analysisRun()


# In[ ]:





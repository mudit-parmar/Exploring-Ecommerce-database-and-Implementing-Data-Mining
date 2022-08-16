-- Creating the database and tables for the ECE656 Ecommerce Project

CREATE DATABASE E_Commerce;

use E_Commerce;

DROP TABLE IF EXISTS order_payments;

CREATE TABLE order_payments (
     order_id varchar(50),
     payment_sequential int,
     payment_type varchar (50),
     payment_installments int,
     payment_value float check(payment_value >= 0)
	 );

DROP TABLE IF EXISTS order_items;

CREATE TABLE order_items (
     order_id varchar(50) NOT NULL,
     order_item_id varchar (50),
     product_id varchar (50),
     seller_id varchar (50),
     price float check(price >= 0),
     freight_value float check(freight_value >= 0)) ;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
     customer_id varchar (50) NOT NULL PRIMARY KEY,
     customer_unique_id varchar(50),
     customer_zip_code int,
     customer_city varchar (50),
     customer_state varchar (50)
     );

DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews
     (review_id varchar (50) NOT NULL,
     order_id varchar (50) NOT NULL,
     review_score int,
     review_comment_title varchar (50),
     review_comment_message varchar (500),
     review_creation_date timestamp,
     review_answer_timestamp timestamp,
	 PRIMARY KEY (review_id, order_id),
	 CONSTRAINT CHK_reviewScore CHECK (review_score>0 AND review_score<=5));

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
     order_id VARCHAR(100) PRIMARY KEY,
     customer_id VARCHAR(100),
     order_status VARCHAR(50),
     order_purchase_timestamp TIMESTAMP,
     order_approved_at TIMESTAMP,
     order_delivered_carrier_date TIMESTAMP,
     order_delivered_customer_date TIMESTAMP,
     order_estimated_delivery_date TIMESTAMP,
	 CONSTRAINT chk_orderStatus CHECK (order_status IN ('delivered', 'shipped', 'processing'))
     );

DROP TABLE IF EXISTS products;

CREATE TABLE products (
     product_id varchar(50) NOT NULL PRIMARY KEY,
     product_category_name VARCHAR(70),
     product_name_length int ,
     product_description_length int,
     product_photos_qty int,
     product_weight_g int ,
     product_length_cm int ,
     product_height_cm int ,
     product_width_cm int);

DROP TABLE IF EXISTS sellers;

CREATE TABLE sellers
     (seller_id varchar(50) NOT NULL PRIMARY KEY,
     seller_zip_code_prefix int,
     seller_city varchar (100) ,
     seller_state varchar(2) CHECK (LENGTH(seller_state) <=2)
     );

DROP TABLE IF EXISTS combined;

CREATE TABLE combined (
     product_id varchar (50),
     seller_id varchar (50),
     order_id varchar(50), customer_id varchar (50),     order_status VARCHAR(50),
     order_purchase_timestamp TIMESTAMP,
     order_approved_at TIMESTAMP,
     order_delivered_carrier_date TIMESTAMP,
     order_delivered_customer_date TIMESTAMP,
     order_estimated_delivery_date TIMESTAMP, customer_unique_id varchar(50),
     customer_zip_code int,
     customer_city varchar (50),
     customer_state varchar (50), review_id varchar (50),
     review_score int,
     review_comment_title varchar (50),
     review_comment_message varchar (500),
     review_creation_date timestamp,
     review_answer_timestamp timestamp,  payment_sequential int,
     payment_type varchar (50),
     payment_installments int,
     payment_value float, order_item_id varchar (50), price float,
     freight_value float, seller_zip_code_prefix int,
     seller_city varchar (100) ,
     seller_state varchar(15), product_category_name VARCHAR(70),
     product_name_length int,
     product_description_length int,
     product_photos_qty int,
     product_weight_g int,
     product_length_cm int ,
     product_height_cm int ,
     product_width_cm int);

DROP TABLE IF EXISTS product_category;

CREATE TABLE product_category (
product_category_name VARCHAR(70) NOT NULL  PRIMARY KEY
);

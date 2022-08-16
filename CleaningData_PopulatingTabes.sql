use E_Commerce;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Orders_merged.csv' 
INTO TABLE combined 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
(product_id, seller_id, order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at,order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date, customer_unique_id, @customer_zip_code, customer_city, customer_state, review_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp, payment_sequential, payment_type, payment_installments, payment_value, order_item_id, price, freight_value, @seller_zip_code_prefix, seller_city, seller_state, @product_category_name, @product_name_length, @product_description_length, @product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
SET
product_name_length = NULLIF(@product_name_length,'NA'),
product_description_length = NULLIF(@product_description_length,'NA'),
product_photos_qty = NULLIF(@product_photos_qty,'NA'),
customer_zip_code = NULLIF(@customer_zip_code,'0'),
seller_zip_code_prefix = NULLIF(@seller_zip_code_prefix,'0'),
product_category_name = NULLIF(@product_category_name,'');


INSERT INTO customers SELECT DISTINCT customer_id, customer_unique_id, customer_zip_code, customer_city, customer_state FROM combined;

-- Data Cleaning
DELETE FROM combined where product_id = "23384f296aa1bf6461d22912093a9847" and product_category_name ="63";
-- Data Cleaning
DELETE FROM combined where product_category_name = "pcs";
-- Data Cleaning
DELETE FROM combined where seller_id = "891071be6ba827b591264c90c2ae8a63" and seller_state= "cama_mesa_banho";

DELETE FROM combined where order_id = "order_id";


INSERT INTO product_category SELECT DISTINCT product_category_name from combined where product_category_name IS NOT NULL;

INSERT INTO products SELECT DISTINCT product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g , product_length_cm , product_height_cm , product_width_cm FROM combined;

INSERT INTO orders SELECT DISTINCT order_id , customer_id ,  order_status , order_purchase_timestamp, order_approved_at, order_delivered_carrier_date,  order_delivered_customer_date, order_estimated_delivery_date FROM combined;

INSERT INTO sellers SELECT DISTINCT seller_id, seller_zip_code_prefix, seller_city ,seller_state FROM combined;



INSERT INTO order_payments  SELECT DISTINCT order_id, payment_sequential , payment_type, payment_installments, payment_value  FROM combined;

INSERT INTO order_items SELECT  DISTINCT order_id, order_item_id , product_id , seller_id, price, freight_value FROM combined;

INSERT INTO  reviews SELECT DISTINCT review_id, order_id,review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp FROM combined;


DROP TABLE IF EXISTS combined;

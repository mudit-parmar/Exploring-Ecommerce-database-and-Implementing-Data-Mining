-- Adding foreign keys constraints on the E commerce database tables

use E_Commerce;

-- Adding foreign keys constraints on the pyament tabe such that the order_id references to the order_id in the order table.
ALTER TABLE order_payments 
ADD CONSTRAINT FK_OrderpaymentsOrders
FOREIGN KEY (order_id) REFERENCES orders(order_id);


-- Adding the required foreign keys constraints on the order_items table
ALTER TABLE order_items 
ADD CONSTRAINT FK_OrderitemsOrders
FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE order_items
ADD CONSTRAINT FK_OrderitemsProducts
FOREIGN KEY (product_id) REFERENCES products(product_id);

ALTER TABLE order_items 
ADD CONSTRAINT FK_OrderitemsSellers
FOREIGN KEY (seller_id) REFERENCES sellers(seller_id);


-- Adding the required foreign keys constraints on the reviews table
ALTER TABLE reviews 
ADD CONSTRAINT FK_ReviewsOrders
FOREIGN KEY (order_id) REFERENCES orders(order_id);


-- Adding the required foreign keys constraints on the reviews table
ALTER TABLE orders 
ADD CONSTRAINT FK_OrdersCustomers
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);


-- Adding the required foreign keys constraints on the reviews table
ALTER TABLE products 
ADD CONSTRAINT FK_ProductsProductcategory
FOREIGN KEY (product_category_name) REFERENCES product_category(product_category_name);





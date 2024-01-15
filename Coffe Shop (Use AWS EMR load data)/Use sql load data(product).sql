use STUDENT_TCHE368;

CREATE TABLE product (
product_id INT, 
product_group VARCHAR(255), 
product_category VARCHAR(255), 
product_type VARCHAR(255), 
product VARCHAR(255), 
product_description VARCHAR(255), 
unit_of_measure VARCHAR(255), 
current_wholesale_price FLOAT, 
current_retail_price VARCHAR(255), 
tax_exempt_yn VARCHAR(255), 
promo_yn VARCHAR(255), 
new_product_yn VARCHAR(255)
);

DELETE FROM product;
-- load the product csv file to data_base 
LOAD DATA LOCAL INFILE "C:/Program Files/MySQL/MySQL Workbench 8.0/manage_bigdata/HW3/product.csv"
INTO TABLE product
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

SELECT * FROM product;

-- insert 5 null rows to product tbale 
insert into product values 
(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

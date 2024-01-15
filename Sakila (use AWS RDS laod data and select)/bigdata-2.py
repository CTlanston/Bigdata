import mysql.connector
import csv

# Establish MySQL connection
mydb = mysql.connector.connect(
    host="bigdata-hw-db.c3f4g2yxdyve.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Ct123456",
    database="sakila_database",
    allow_local_infile=True
)


# Initialize cursor
mycursor = mydb.cursor()
select_query  ="""
-- Write a query to find the top five film genres in gross revenue in descending order
SELECT
    category,  -- Select the category (film genre)
    SUM(amount) AS amount  -- Sum the revenue for each category
FROM
(
    -- Subquery A: Gets the inventory_id and associated category for each film
    SELECT
        c.inventory_id AS inventory_id,  -- Inventory ID
        d.name AS category  -- Category (film genre)
    FROM
        film a  -- Film table
    LEFT JOIN
        film_category b  -- Film-Category mapping table
    ON a.film_id = b.film_id
    INNER JOIN
        inventory c  -- Inventory table
    ON a.film_id = c.film_id
    INNER JOIN
        category d  -- Category table
    ON b.category_id = d.category_id
) A
INNER JOIN
(
    -- Subquery B: Sums the revenue for each inventory_id (film copy)
    SELECT
        a.inventory_id AS inventory_id,  -- Inventory ID
        SUM(amount) AS amount  -- Revenue
    FROM
        rental a  -- Rental table
    INNER JOIN
        payment b  -- Payment table
    ON a.rental_id = b.rental_id
    GROUP BY
        a.inventory_id  -- Group by inventory_id
) B
ON A.inventory_id = B.inventory_id  -- Join A and B on inventory_id
GROUP BY category  -- Group by category to sum revenue per genre
ORDER BY SUM(amount) DESC  -- Sort by revenue in descending order
LIMIT 5;  -- Limit to top 5 genres
"""

mycursor.execute(load_data_query, multi = True)

results = mycursor.fetchall()

# Print the results
for row in results:
    print(row)
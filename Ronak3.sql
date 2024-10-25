UPDATE products
SET price = price * 1.10;

SELECT name, price AS new_price
FROM products;
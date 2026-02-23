-- Total revenue
SELECT SUM(sales) AS total_revenue FROM sales;

-- Monthly sales
SELECT
MONTH(orderDate) AS month,
SUM(sales) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Top customers
SELECT
customerName,
SUM(sales) AS total_spent
FROM sales
GROUP BY customerName
ORDER BY total_spent DESC
LIMIT 10;

-- Sales by product
SELECT
productLine,
SUM(sales) AS revenue
FROM sales
GROUP BY productLine
ORDER BY revenue DESC;

-- Sales by country
SELECT
country,
SUM(sales) AS revenue
FROM sales
GROUP BY country
ORDER BY revenue DESC;
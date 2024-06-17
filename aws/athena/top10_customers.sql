CREATE VIEW top10_customers AS
SELECT 
"product id",
"product name",
SUM(quantity) as total_products_purchased
FROM "demo"."ordersoutput"
GROUP BY "product id", "product name"
ORDER BY total_products_purchased DESC 
LIMIT 10;
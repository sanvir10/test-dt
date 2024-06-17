CREATE VIEW top10_seller_products AS
SELECT
"product id",
"product name",
SUM(quantity) as total_sells
FROM "demo"."ordersoutput"
GROUP BY "product id", "product name"
ORDER BY total_sells DESC 
LIMIT 10;
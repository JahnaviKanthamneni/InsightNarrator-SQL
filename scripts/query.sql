SELECT region, SUM(revenue) AS total_revenue
FROM sales_data
WHERE quarter = 'Q2'
GROUP BY region;

Query 1

SELECT fund_name, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY fund_name
ORDER BY avg_nav DESC;

Query 2

SELECT fund_name, COUNT(*) AS total_records
FROM fact_nav
GROUP BY fund_name;

Query 3

SELECT *
FROM fact_nav
WHERE nav = (SELECT MAX(nav) FROM fact_nav);


Query 4

SELECT *
FROM fact_nav
WHERE nav = (SELECT MIN(nav) FROM fact_nav);


Query 5

SELECT fund_name,
       MAX(nav) - MIN(nav) AS nav_range
FROM fact_nav
GROUP BY fund_name;


Query 6

SELECT fund_name, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY fund_name;

Query 7

SELECT fund_name,
       MAX(nav) - MIN(nav) AS volatility_proxy
FROM fact_nav
GROUP BY fund_name
ORDER BY volatility_proxy DESC;


Query 8

SELECT date, COUNT(*) 
FROM fact_nav
GROUP BY date;


Query 9

SELECT *
FROM fact_nav f1
WHERE date = (
    SELECT MAX(date)
    FROM fact_nav f2
    WHERE f1.fund_name = f2.fund_name
);

Query 10

SELECT DISTINCT fund_name
FROM fact_nav
WHERE nav > 5000;




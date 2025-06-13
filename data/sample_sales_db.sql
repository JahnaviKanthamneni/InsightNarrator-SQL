DROP TABLE IF EXISTS sales_data;

CREATE TABLE sales_data (
    id INTEGER PRIMARY KEY,
    region TEXT,
    product TEXT,
    quarter TEXT,
    revenue INTEGER,
    units_sold INTEGER
);

INSERT INTO sales_data (region, product, quarter, revenue, units_sold) VALUES
('North', 'Widget A', 'Q1', 12000, 100),
('North', 'Widget A', 'Q2', 14000, 120),
('South', 'Widget A', 'Q1', 10000, 90),
('South', 'Widget A', 'Q2', 9500, 80),
('East', 'Widget B', 'Q1', 8000, 60),
('East', 'Widget B', 'Q2', 9000, 70),
('West', 'Widget B', 'Q1', 7000, 50),
('West', 'Widget B', 'Q2', 8500, 65);

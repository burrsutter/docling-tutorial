## The following is the raw sales output

|   OrderID | OrderDate   | Customer       | Region   | Product   |   Quantity |   UnitPrice |   TotalSales |
|-----------|-------------|----------------|----------|-----------|------------|-------------|--------------|
|      1001 | 2025-01-05  | Acme Corp      | North    | Widget A  |         10 |        9.99 |        99.9  |
|      1002 | 2025-01-06  | Global Inc     | South    | Widget B  |          5 |       19.99 |        99.95 |
|      1003 | 2025-01-07  | Tech Solutions | East     | Gadget X  |          7 |       14.5  |       101.5  |
|      1004 | 2025-01-08  | Innovate LLC   | West     | Widget A  |         12 |        9.99 |       119.88 |
|      1005 | 2025-01-09  | Acme Corp      | North    | Gadget Y  |          3 |       29.99 |        89.97 |
|      1006 | 2025-01-10  | Global Inc     | South    | Widget B  |          8 |       19.99 |       159.92 |
|      1007 | 2025-01-11  | Tech Solutions | East     | Widget A  |         15 |        9.99 |       149.85 |
|      1008 | 2025-01-12  | Innovate LLC   | West     | Gadget X  |          4 |       14.5  |        58    |
|      1009 | 2025-01-13  | Acme Corp      | North    | Widget B  |          6 |       19.99 |       119.94 |
|      1010 | 2025-01-14  | Global Inc     | South    | Gadget Y  |          2 |       29.99 |        59.98 |

## By Customer

|   OrderID | OrderDate   | Customer   | Region   | Product   |   Quantity |   UnitPrice |   TotalSales |
|-----------|-------------|------------|----------|-----------|------------|-------------|--------------|
|      1005 | 2025-01-09  | Acme Corp  | North    | Gadget Y  |          3 |       29.99 |        89.97 |
|      1001 | 2025-01-05  | Acme Corp  | North    | Widget A  |         10 |        9.99 |        99.9  |
|      1009 | 2025-01-13  | Acme Corp  | North    | Widget B  |          6 |       19.99 |       119.94 |
|      1010 | 2025-01-14  | Global Inc | South    | Gadget Y  |          2 |       29.99 |        59.98 |
|      1002 | 2025-01-06  | Global Inc | South    | Widget B  |          5 |       19.99 |        99.95 |

|   1006 | 2025-01-10   | Global Inc     | South   | Widget B   |   8 |   19.99 |   159.92 |
|--------|--------------|----------------|---------|------------|-----|---------|----------|
|   1008 | 2025-01-12   | Innovate LLC   | West    | Gadget X   |   4 |   14.5  |    58    |
|   1004 | 2025-01-08   | Innovate LLC   | West    | Widget A   |  12 |    9.99 |   119.88 |
|   1003 | 2025-01-07   | Tech Solutions | East    | Gadget X   |   7 |   14.5  |   101.5  |
|   1007 | 2025-01-11   | Tech Solutions | East    | Widget A   |  15 |    9.99 |   149.85 |
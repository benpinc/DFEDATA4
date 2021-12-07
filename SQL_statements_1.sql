USE WideWorldImporters;

/* A general list of queries to show existing knowledge */

/*Distinct list of values*/

SELECT DISTINCT customername
FROM sales.Customers;

/*Conditions*/
SELECT *
FROM Sales.Orders as SO
WHERE PickedByPersonID IS NULL

/*Inner Join, aggregations, aliasing and grouping*/
SELECT SC.CustomerID AS CustomerID, SC.CustomerName AS CustomerName, sum(IL.UnitPrice) AS TotalUnitPrice,  avg(IL.UnitPrice) AS AvgUnitPrice, min(IL.UnitPrice) AS MinUnitPrice, max(IL.UnitPrice) AS MaxUnitPrice
FROM sales.InvoiceLines as IL
JOIN sales.CustomerTransactions as CT
ON CT.InvoiceID = IL.InvoiceID
JOIN sales.Customers AS SC
ON SC.CustomerID = CT.CustomerID
GROUP BY SC.CustomerID, SC.CustomerName;

/* WHERE and HAVING conditions */
SELECT SalespersonPersonID as ID, count(SO.OrderID) AS nOrders
FROM Sales.Orders as SO
WHERE SO.SalespersonPersonID >5
GROUP BY SalespersonPersonID
HAVING count(SO.OrderID) >7250;
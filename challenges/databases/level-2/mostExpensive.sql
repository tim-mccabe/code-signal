CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT MIN(name) AS name
    FROM Products
    WHERE (price * quantity) = (SELECT MAX(price * quantity)
                                FROM Products);
END
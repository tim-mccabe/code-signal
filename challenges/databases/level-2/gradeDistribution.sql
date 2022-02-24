CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        Name
        ,ID
    FROM
        Grades
    WHERE
        Final > (Midterm1 + Midterm2)/2
    ORDER BY LEFT(name,3), ID;
END
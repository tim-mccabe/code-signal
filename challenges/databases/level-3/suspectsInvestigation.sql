CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT id
            , name
            , surname
    FROM Suspect
    WHERE height <= 170 
        AND LOWER(name) LIKE 'b%'
        AND LOWER(surname) LIKE 'gre_n'
    ORDER BY id;
END

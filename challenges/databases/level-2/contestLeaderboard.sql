CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT name
    FROM leaderboard
    ORDER BY score DESC
    LIMIT 3,5;
END
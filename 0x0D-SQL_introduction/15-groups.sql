-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT score.score, COUNT(*) AS number from second_table as score GROUP BY score.score ORDER BY `score` DESC;
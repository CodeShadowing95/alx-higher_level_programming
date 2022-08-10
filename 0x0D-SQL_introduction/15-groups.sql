-- Script that lists the number of records with the same score in a table
SELECT DISTINCT(score), COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;

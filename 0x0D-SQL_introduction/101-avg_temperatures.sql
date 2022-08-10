-- Import a table dump in a database and write a script that displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

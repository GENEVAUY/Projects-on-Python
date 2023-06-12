USE Sakila;
#Determine the shortest and longest movie durations 
#and name the values as max_duration and min_duration.
SELECT 
MAX(length) AS max_duration, 
MIN(length) AS min_duration 
FROM film;

#Express the average movie duration...
SELECT 
ROUND (AVG(length)) 
FROM film;

##in hours and minutes.
SELECT 
CONCAT
(FLOOR(AVG(length) / 60),' hours ',
FLOOR((AVG(length) % 60)),' minutes') 
FROM film;

#Calculate the number of days that the company has been operating
SELECT
 DATEDIFF(MAX(rental_date), 
 MIN(rental_date)) 
 FROM rental;

#Retrieve rental information and add two additional columns to show the month and weekday of the rental. Return 20 rows of results.
SELECT *,
 MONTH(rental_date) AS month, 
 DAYNAME(rental_date) AS weekdays 
 FROM rental
 LIMIT 20;

#Retrieve rental information and add an additional column called DAY_TYPE with values 'weekend' or 'workday', depending on the day of the week. 
SELECT *,
CASE WHEN 
DAYOFWEEK(rental_date) 
IN (1, 7)
 THEN 'weekend' 
 ELSE 'workday' 
 END AS DAY_TYPE ,
 DAYNAME(rental_date)
 FROM rental;

#Retrieve the film titles and their rental duration. If any rental duration value is NULL, replace it with the string 'Not Available'
SELECT title,
coalesce(rental_duration , "Not Available"),
 AS rental_duration 
 FROM film 
 ORDER BY title;

#retrieve the concatenated first and last names of our customers, along with the first 3 characters of their email address
SELECT 
CONCAT(first_name, ' ', last_name) AS full_name,
LEFT(email, 3) AS email_prefix
FROM customer
ORDER BY last_name 
ASC;

##CHALLENGE 2
#The total number of films that have been released.
SELECT COUNT(*) 
FROM film;

#The number of films for each rating.
SELECT rating,
COUNT(*) 
FROM film 
GROUP BY rating;

#The number of films for each rating, and sort the results in descending order of the number of films. 
SELECT rating, COUNT(*)
FROM film
GROUP BY rating
ORDER BY COUNT(*) 
DESC;


# determine the number of rentals processed by each employee
SELECT staff_id, COUNT(*)
FROM rental
GROUP BY staff_id;

#The mean film duration for each rating, and sort the results in descending order of the mean duration. 
SELECT rating, ROUND(AVG(length), 2)
FROM film
GROUP BY rating
ORDER BY ROUND(AVG(length), 2) DESC;

# Identify which ratings have a mean duration of over two hours
SELECT rating, ROUND(AVG(length), 2)
FROM film
GROUP BY rating
HAVING AVG(length) > 120;

#Determine which last names are not repeated in the table actor.
SELECT last_name
FROM actor
GROUP BY last_name
HAVING COUNT(*) = 1;

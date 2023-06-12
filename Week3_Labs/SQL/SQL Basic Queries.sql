USE sakila;

#Exercise 1: Show all tables

SHOW TABLES;

#Retrieve all the data from the tables actor, film,customer
SELECT * FROM actor;
SELECT * FROM film;
SELECT * FROM customer;
#another way
SELECT * FROM actor, film, customer;

#Titles of all films from the film table
SELECT title FROM film;

#List of languages used in films, with the column aliased as language from the language table
SELECT name AS language FROM language;

#List of first names of all employees from the staff table
SELECT first_name FROM STAFF;

#Retrieve unique release years.
SELECT DISTINCT release_year FROM Film;

##Counting records for database insights:
#Determine the number of stores that the company has.
SELECT COUNT(*) FROM store;

#Determine the number of employees that the company has.
SELECT COUNT(*) AS employee_count FROM staff;

#Determine how many films are available for rent and how many have been rented.
SELECT COUNT(*) AS inventory_id FROM rental;	
SELECT COUNT(*) AS rental_id FROM rental;
SELECT COUNT(DISTINCT (inventory_id)) AS available FROM rental;

#Determine the number of distinct last names of the actors in the database.
SELECT DISTINCT last_name FROM actor;

#Retrieve the 10 longest films.
SELECT * FROM film ORDER BY length DESC LIMIT 10;

#Use filtering techniques in order to:
#Retrieve all actors with the first name "SCARLETT".
SELECT * FROM actor WHERE first_name ="SCARLETT";

#Retrieve all movies that have ARMAGEDDON in their title and have a duration longer than 100 minutes.
SELECT * FROM film WHERE title LIKE '%ARMAGEDDON%' AND length > 100;

#Determine the number of films that include Behind the Scenes content
SELECT COUNT(*) special_features FROM film;

SELECT COUNT(*) special_features FROM film WHERE special_features LIKE "%Behind The Scenes%"

![image](https://user-images.githubusercontent.com/122611622/221138850-a2d336fc-5305-4b4a-973c-08735bc5b844.png)
## 1-task

![image](https://user-images.githubusercontent.com/122611622/221139534-db08ae10-71dd-4dd5-b3cc-dc70cf95e95b.png)
## 2-task

![image](https://user-images.githubusercontent.com/122611622/221139645-ea01bfa6-587a-4255-8dd2-d02b7f6b9d12.png)
## 3-task

![image](https://user-images.githubusercontent.com/122611622/221139796-494321ed-46c4-4464-8962-2c45f7d2b3b4.png)
## 4-task
SELECT *
FROM categories
WHERE category_name = 'Confections'

![image](https://user-images.githubusercontent.com/122611622/221139981-8abc5e08-7a69-4347-b71f-d812f55a3913.png)
## 5-task 
SELECT *
FROM categories
WHERE category_name = 'Seafood' or category_name = 'Produce'

![image](https://user-images.githubusercontent.com/122611622/221140208-00a2e1ab-ca84-4724-97ed-0fa74a2d29c2.png)
## 6-task 
SELECT *
FROM categories
WHERE category_id between 6 and 8

![image](https://user-images.githubusercontent.com/122611622/221140428-9d0b2434-6834-4fa0-82df-8db2245a8806.png)
## 7-task 
SELECT *
FROM categories
order by description

![image](https://user-images.githubusercontent.com/122611622/221141849-14df9b63-224e-4eee-8be3-ef89b93a3726.png)
## 10-task 
SELECT contact_name,contact_title
FROM customers
where contact_title='Owner'

![image](https://user-images.githubusercontent.com/122611622/221142685-6a3a9edd-cf0f-4d17-90fb-5b14389d1703.png)
## 11-task 
SELECT contact_name,city
FROM customers
where city='London'

![image](https://user-images.githubusercontent.com/122611622/221143225-8ff74b36-8e26-4131-a223-9115d11623fe.png)
## 12-task
SELECT contact_name,region
FROM customers
where region is null

![image](https://user-images.githubusercontent.com/122611622/221143641-a2fe9783-9e3a-41de-8247-72bb8e8cb821.png)
## 13-task
SELECT contact_name,region
FROM customers
where region is not null

![image](https://user-images.githubusercontent.com/122611622/221144135-a246d815-6682-409d-b064-f4f3e43ad864.png)
## 14-task
SELECT contact_name,country
FROM customers
where country = 'Germany'

![image](https://user-images.githubusercontent.com/122611622/221144546-4280aba8-e45a-48c0-8431-fbf11474efba.png)
## 15-task
SELECT count(*)
FROM customers
where country = 'Germany'

![image](https://user-images.githubusercontent.com/122611622/221140952-2b103828-23af-43e8-a06c-078f7dbd65ae.png)
## 16-task
SELECT contact_name, fax
FROM customers
where fax is not null
order by customers.contact_name

![image](https://user-images.githubusercontent.com/122611622/221145655-4cb132b2-83d3-4268-b668-6323c23177b8.png)
## 19-task
SELECT first_name, title_of_courtesy
FROM employees
where title_of_courtesy = 'Mr.'
order by first_name

![image](https://user-images.githubusercontent.com/122611622/221146403-b5bf7f81-41dc-467f-af1d-fe6bee5718fe.png)
## 20-task
SELECT first_name, title
FROM employees
where title = 'Sales RepresentativeS'
order by first_name

![image](https://user-images.githubusercontent.com/122611622/221148672-ad3eb06e-03b5-4918-8c54-5144c413313a.png)
## 21-task
SELECT first_name, hire_date
FROM employees
where hire_date between '1994-01-01' and '1994-12-31'
order by first_name

![image](https://user-images.githubusercontent.com/122611622/221149245-7527f045-992e-4f7c-899e-0422f3979d96.png)
## 22-task
SELECT first_name, last_name, title, city, home_phone
FROM employees
where region is not null
order by first_name

![image](https://user-images.githubusercontent.com/122611622/221149903-db9bde6d-0ca5-499d-90a9-33bb0fa29f55.png)
## 23-task
SELECT *
FROM orders
where customer_id = 'VINET'

![image](https://user-images.githubusercontent.com/122611622/221150264-2d21a1d4-5b49-47f8-b042-8589e1b2093b.png)
## 24-task
SELECT *
FROM orders
where order_date between '1996-01-01' and '1996-12-31'

![image](https://user-images.githubusercontent.com/122611622/221150697-74eaabec-1555-4cc5-86c3-d8b1b6d41465.png)
## 25-task
SELECT order_id, customer_id, ship_region
FROM orders
where ship_region is not null

![image](https://user-images.githubusercontent.com/122611622/221151103-0b0b56cb-0b5d-418e-99b6-a1723ca97464.png)
## 26-task
SELECT *
FROM orders
where order_id between 10300 and 10400

![image](https://user-images.githubusercontent.com/122611622/221151778-90a69c99-0fbd-49cf-8e73-a18e4e80281e.png)
## 27-task
SELECT sum(unit_price)
FROM order_details

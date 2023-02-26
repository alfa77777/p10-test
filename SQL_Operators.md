## 1-task
![image](https://user-images.githubusercontent.com/122611622/221418862-f41ea81c-0a38-4aad-8e6a-6ef48ddc2894.png)

```sql
SELECT * FROM customer 
WHERE grade > 100
```
## 3-task
![image](https://user-images.githubusercontent.com/122611622/221418954-4bab5feb-d325-44d9-888c-a02a04c8bc5b.png)

```sql
SELECT * FROM customer 
WHERE city = 'New York' OR grade>100
```
## 5-task
![image](https://user-images.githubusercontent.com/122611622/221419076-300d60b9-21bd-40ac-ad4a-1584c5edeac5.png)

```sql
SELECT * FROM customer 
WHERE NOT (city = 'New York' OR grade>100)
```
## 7-task
![image](https://user-images.githubusercontent.com/122611622/221419264-8d35bc20-2804-4236-b936-0d8ec39f65d1.png)

```sql
SELECT salesman_id,name,city,commission 
FROM salesman 
WHERE (commission > 0.10 AND commission< 0.12)
```
## 9-task
![image](https://user-images.githubusercontent.com/122611622/221419403-24d907f8-18a2-4185-bd92-0a6effb5bc48.png)

```sql
SELECT * FROM  orders 
WHERE NOT(
(ord_date ='2012-08-17' OR customer_id>3005) AND 
purch_amt<1000
)
```
## 11-task
![image](https://user-images.githubusercontent.com/122611622/221419585-c271b538-3aca-4e61-a0ca-65b4c3ee5ed4.png)

```sql
SELECT *  FROM emp_details  
WHERE emp_lname ='Dosni' OR emp_lname= 'Mardy'
```

## 1-task
![image](https://user-images.githubusercontent.com/122611622/221421514-df545e09-bae9-42b1-9370-82d6af858859.png)

```sql
SELECT SUM (purch_amt) FROM orders
```
## 4-task
![image](https://user-images.githubusercontent.com/122611622/221421558-5325fdad-8904-41a5-b6c5-276f0402f0a2.png)

```sql
SELECT COUNT(*) FROM customer
```
## 7-task
![image](https://user-images.githubusercontent.com/122611622/221421590-e516725e-db11-4b78-895f-2892e944b6e4.png)

```sql
SELECT MIN(purch_amt) FROM orders
```
## 10-task
![image](https://user-images.githubusercontent.com/122611622/221421659-5ccbc189-c361-4aef-ba35-d426c8378de5.png)

```sql
SELECT customer_id,ord_date,MAX(purch_amt) 
FROM orders GROUP BY customer_id,ord_date
```
## 13-task
![image](https://user-images.githubusercontent.com/122611622/221421713-74147407-d1c3-429e-8d8d-995afe828178.png)

```sql
SELECT customer_id,ord_date,MAX(purch_amt) 
FROM orders 
GROUP BY customer_id,ord_date 
HAVING MAX(purch_amt) 
BETWEEN 2000 AND 6000
```
## 16-task
![image](https://user-images.githubusercontent.com/122611622/221421796-6b1b5330-70bb-443b-afaf-31af3731a3f0.png)

```sql
SELECT customer_id,MAX(purch_amt) 
FROM orders WHERE customer_id 
BETWEEN 3002 and 3007 
GROUP BY customer_id HAVING MAX(purch_amt)>1000
```
## 19-task
![image](https://user-images.githubusercontent.com/122611622/221421877-b75fb48c-27d3-41af-9e64-59ea16b4e7b4.png)

```sql
SELECT COUNT(*) FROM salesman 
WHERE city IS NOT NULL
```
## 20-task
![image](https://user-images.githubusercontent.com/122611622/221525419-4bb88cc5-30d0-4a0c-9ba3-ae155c32dc48.png)

```sql
SELECT ord_date,salesman_id,COUNT(*) FROM orders GROUP BY ord_date,salesman_id
```
## 21-task
![image](https://user-images.githubusercontent.com/122611622/221523318-65552a6b-b5cc-4c86-bc5d-034c525e2235.png)

```sql
SELECT AVG(pro_price) AS "Average Price" 
FROM item_mast
```
## 22-task
![image](https://user-images.githubusercontent.com/122611622/221422116-a367d6b2-d392-42b6-ac1c-75ca7d25e272.png)

```sql
SELECT COUNT(*) AS "Number of Products" 
FROM item_mast WHERE pro_price >= 350
```
## 23-task
![image](https://user-images.githubusercontent.com/122611622/221522822-da4e8e3b-68ba-47cf-a067-7b7f770a1065.png)

```sql
SELECT AVG(pro_price) AS "Average Price", pro_com AS "Company ID" FROM item_mast GROUP BY pro_com
```
## 24-task
![image](https://user-images.githubusercontent.com/122611622/221498996-6e9cf9dd-ad97-469a-9651-0150f57d1590.png)

```sql
SELECT SUM(dpt_allotment) 
FROM emp_department
```
## 25-task
![image](https://user-images.githubusercontent.com/122611622/221497973-3263a488-61a1-4ebb-ae62-894e48b46b89.png)

```sql
SELECT emp_dept, COUNT(*) 
FROM emp_details GROUP BY emp_dep
```

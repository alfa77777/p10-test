## 1-task
![image](https://user-images.githubusercontent.com/122611622/221416341-d4089a89-01ea-48c6-851b-1dbbe8c0318a.png)

```sql
SELECT * FROM salesman
```

## 2-task
![image](https://user-images.githubusercontent.com/122611622/221416494-14f9eabf-651f-4adb-a1df-d03b8dc4e7f3.png)

```sql
SELECT 'This is SQL Exercise, Practice and Solution'
```

## 3-task
![image](https://user-images.githubusercontent.com/122611622/221416907-4076be86-9007-4793-a6f1-00df105f4240.png)

```sql
SELECT 5, 10, 15
```

## 4-task
![image](https://user-images.githubusercontent.com/122611622/221417020-0bc1d92a-8c76-4559-be2a-ab0e7e5baf7e.png)

```sql
SELECT 10 + 15
```

## 5-task
![image](https://user-images.githubusercontent.com/122611622/221417152-dfb38683-2479-49f9-bb46-9822a54fff14.png)

```sql
SELECT 10 + 15 - 5 * 2
```

## 6-task
![image](https://user-images.githubusercontent.com/122611622/221417231-5f09208a-4a15-46b0-8d2c-498e8b783332.png)

```sql
SELECT name, commission FROM salesman
```

## 7-task
![image](https://user-images.githubusercontent.com/122611622/221417349-161ab5f1-b8e7-402b-89ad-fb2931f3b7ba.png)

```sql
SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders
```

## 8-task
![image](https://user-images.githubusercontent.com/122611622/221417470-e3b8d499-72da-480b-bd91-94ad5e3010f2.png)

```sql
SELECT DISTINCT salesman_id FROM orders
```

## 9-task
![image](https://user-images.githubusercontent.com/122611622/221417659-a41db0c5-4282-4d31-9499-6a11f827b186.png)

```sql
SELECT name,city FROM salesman 
WHERE city='Paris'
```

## 10-task
![image](https://user-images.githubusercontent.com/122611622/221417714-fce5e92d-81f9-461b-a736-c6a07db1257c.png)

```sql
SELECT *FROM customer 
WHERE grade=200
```

## 15-task
![image](https://user-images.githubusercontent.com/122611622/221417927-cfb316a1-a118-4ae3-a6c2-a19ab776e62d.png)

```sql
SELECT winner FROM nobel_win 
WHERE year>=1950 AND subject='Physics'
```
## 20-task
![image](https://user-images.githubusercontent.com/122611622/221418005-fecd3933-91cb-4f4f-b03c-9937e06cdbc2.png)

```sql
SELECT * FROM nobel_win 
WHERE year=1970 AND 
subject NOT IN('Physiology','Economics')
```
## 25-task
![image](https://user-images.githubusercontent.com/122611622/221418127-f080cc3c-52c4-42e7-b3cf-d32c590504f9.png)

```sql
SELECT * FROM item_mast 
WHERE pro_price 
BETWEEN 200 AND 600
```
## 30-task
![image](https://user-images.githubusercontent.com/122611622/221418289-a4df0045-8d27-4e83-aa23-6cdf12d234d5.png)

```sql
SELECT pro_name, pro_price 
FROM item_mast 
WHERE pro_price = (
SELECT MIN(pro_price) 
FROM item_mast
)
```

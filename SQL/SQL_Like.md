## 1-task
![image](https://user-images.githubusercontent.com/122611622/221420462-37180ba5-ac05-4cfb-9eef-96e127b01cc7.png)

```sql
SELECT * FROM salesman 
WHERE city = 'Paris' OR city = 'Rome'
```
## 3-task
![image](https://user-images.githubusercontent.com/122611622/221420543-c9a79819-1494-40a6-85b7-2cebb8670db8.png)

```sql
SELECT * FROM salesman 
WHERE NOT city IN('Paris','Rome')
```

## 5-task
![image](https://user-images.githubusercontent.com/122611622/221420595-18a047ea-247f-466c-8309-8e6bc7cea96f.png)

```sql
SELECT * FROM salesman 
WHERE commission BETWEEN 0.12 AND 0.14
```

## 7-task
![image](https://user-images.githubusercontent.com/122611622/221420673-d6cca1a4-ee73-45ca-9c65-9cbafb58a481.png)

```sql
SELECT * FROM salesman 
WHERE name BETWEEN 'A' and 'L
```

## 10-task
![image](https://user-images.githubusercontent.com/122611622/221420846-485130f4-5ba1-48e5-aafe-8235f4a2d7ab.png)

```sql
SELECT * FROM customer 
WHERE cust_name LIKE '%n'
```

## 15-task
![image](https://user-images.githubusercontent.com/122611622/221420930-6bb89547-8786-4bc9-b08a-1370d23088e4.png)

```sql
SELECT * FROM testtable 
WHERE col1 NOT LIKE '%//%' ESCAPE '/'
```

## 20-task
![image](https://user-images.githubusercontent.com/122611622/221421049-9bb8eb3f-92a2-4df8-9199-7a6192004bd2.png)

```sql
SELECT * FROM customer 
WHERE grade IS NULL
```

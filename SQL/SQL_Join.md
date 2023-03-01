## 1-task
![image](https://user-images.githubusercontent.com/122611622/222098631-ef401711-ee20-4ab9-b9d5-5f87b2ff9a3d.png)

```sql
SELECT E.first_name , E.last_name, 
    E.department_id , D.department_name 
FROM employees E 
JOIN departments D
ON E.department_id = D.department_id
```

## 2-task
![image](https://user-images.githubusercontent.com/122611622/222098387-4080b779-e808-485d-ad77-a445b3058f01.png)

```sql
SELECT E.first_name, E.last_name, 
    D.department_name, L.city, L.state_province 
FROM employees E 
JOIN departments D 
ON E.department_id = D.department_id 
JOIN locations L 
ON D.location_id = L.location_id
```
## 5-task
![image](https://user-images.githubusercontent.com/122611622/222099531-70c03bf4-33ff-4e5f-99c6-6b30b8fd6931.png)

```sql
SELECT E.first_name,E.last_name, 
    D.department_name, L.city, L.state_province 
FROM employees E 
JOIN departments D  
ON E.department_id = D.department_id 
JOIN locations L 
ON D.location_id = L.location_id 
WHERE E.first_name LIKE  '%z%'
```
## 8-task
![image](https://user-images.githubusercontent.com/122611622/222100350-ef5a8994-15a9-42a6-af5f-2db911e9b93e.png)

```sql
SELECT E.first_name AS "Employee Name", 
    M.first_name AS "Manager" 
FROM employees E 
JOIN employees M 
ON E.manager_id = M.employee_id
```
## 11-task
![image](https://user-images.githubusercontent.com/122611622/222101509-98cc01ae-3c5c-4429-ab6c-a6fd9c0d30ac.png)

```sql
SELECT E.first_name AS "Employee Name", M.first_name AS "Manager" 
FROM employees E 
LEFT JOIN employees M 
ON E.manager_id = M.employee_id
```
## 14-task
![image](https://user-images.githubusercontent.com/122611622/222102134-8d74460d-5781-47d4-95c2-fb3800164900.png)

```sql
SELECT job_title, first_name || ' ' || last_name AS Employee_name, 
    max_salary-salary AS salary_difference 
FROM employees NATURAL JOIN jobs
```
## 17-task
![image](https://user-images.githubusercontent.com/122611622/222102888-74012fc4-ed45-499e-880f-98ff5bcb9260.png)

```sql
SELECT country_name,city, department_name 
FROM countries 
JOIN locations USING (country_id) 
JOIN departments USING (location_id)
```
## 20-task
![image](https://user-images.githubusercontent.com/122611622/222103503-efd0dd81-6320-4be5-a343-9e30fad6fc94.png)

```sql
SELECT a.* 
FROM  job_history a 
JOIN employees m 
ON (a.employee_id = m.employee_id) 
WHERE salary >= 12000
```
## 23-task
![image](https://user-images.githubusercontent.com/122611622/222104150-f0f8e4ce-3cde-4a0d-a2cd-90eaa97d6520.png)

```sql
SELECT employee_id, job_title, 
    end_date-start_date DAYS 
FROM job_history 
NATURAL JOIN jobs 
WHERE department_id=80
```
## 27-task
![image](https://user-images.githubusercontent.com/122611622/222104737-e0367839-b90a-4867-afef-614c2f34147f.png)

```sql
SELECT first_name || ' ' || last_name AS Employee_name, 
    employee_id, country_name 
FROM employees 
JOIN departments 
USING(department_id) 
    JOIN locations 
    USING( location_id) 
        JOIN countries 
        USING ( country_id)
```

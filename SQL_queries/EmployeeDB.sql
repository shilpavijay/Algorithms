/*
SCHEMA:

CREATE TABLE employees (
    emp_no      INT             NOT NULL,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,    
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
);

CREATE TABLE departments (
    dept_no     CHAR(4)         NOT NULL,
    dept_name   VARCHAR(40)     NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE  KEY (dept_name)
);

CREATE TABLE dept_manager (
   emp_no       INT             NOT NULL,
   dept_no      CHAR(4)         NOT NULL,
   from_date    DATE            NOT NULL,
   to_date      DATE            NOT NULL,
   FOREIGN KEY (emp_no)  REFERENCES employees (emp_no)    ON DELETE CASCADE,
   FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
   PRIMARY KEY (emp_no,dept_no)
); 

CREATE TABLE dept_emp (
    emp_no      INT             NOT NULL,
    dept_no     CHAR(4)         NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no)  REFERENCES employees   (emp_no)  ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,dept_no)
);

CREATE TABLE titles (
    emp_no      INT             NOT NULL,
    title       VARCHAR(50)     NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,title, from_date)
) 
; 

CREATE TABLE salaries (
    emp_no      INT             NOT NULL,
    salary      INT             NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, from_date)
) 
; 
*/

--Q1: GET THE THIRD HIGHEST SALARY:

select * from (
select emp_no,salary,dense_rank() 
over(order by salary desc)r from employees.salaries) A
where r=2;


--Q2: GET THIRD HIGHEST SALARY WITHOUT RANK FUNCTION:
select emp_no,salary from employees.salaries e1 
where 3 = (
    select count(distinct salary) from employees.salaries e2 
    where e2.salary > e1.salary
    )

--or--

select * from (
select emp_no,salary,
(select count(*) from employees.salaries e2 
where e2.salary > e1.salary)rnum
from employees.salaries e1
order by rnum
)
where rnum=3;


--Q3: GET RANK WITHOUT RANK FUNCTION:
select emp_no,salary,
(select count(*) from employees.salaries e2 
where e2.salary > e1.salary)rnum
from employees.salaries e1
order by rnum;

--Explanation: The inner subquery takes each record from outer query(in the order it is passed) and 
--computes the number of salaries greater than the given salary (in the outer query). This is nothing but
--the rank of the current row. Same happens for all the records and we get a rank column

--Q4: GET TOP 3 SALARIES OF EMPLOYEES PER DEPARTMENT
select dept_no,emp_no,salary,r from (
select dept_no,e1.emp_no as emp_no,salary,dense_rank()
over(partition by dept_no order by salary)r
from employees.salaries e1 JOIN employees.dept_emp d1 ON e1.emp_no) A
where r <=3 


--Q5: SELECT/DELETE DUPLICATE RECORDS
select emp_no from employees
group by emp_no
having count(*) > 1


delete from employees
 where id not in (
    select max(id)
      from employees
     group by emp_no)
     
--OR
DELETE t1 FROM test t1, test t2 
WHERE t1.id > t2.id AND t1.email = t2.email

--Q5: GET THE AGE AND TENURE OF EMPLOYEES 







-- Binning Queries for Age, Year, Salary

get top performers in each age group
get top performers in each age group for every year
get salary ranges for each department
get salary hikes historically for each department (rolling diff)

-- get salary range across departments and titles
select dept_name, title, CONCAT(min(salary), ' - ',max(salary)) as salary_range from curr_emp_data ced group by 1, 2

-- get salary range across departments
select dept_name, CONCAT(min(salary), ' - ',max(salary)) as salary_range from curr_emp_data ced group by 1

-- get salary range across titles
select title, CONCAT(min(salary), ' - ',max(salary)) as salary_range from curr_emp_data ced group by 1
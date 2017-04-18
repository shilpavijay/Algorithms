mysql> select * from emp;
+---------+------+------+--------+---------+
| name    | age  | dept | gender | sal     |
+---------+------+------+--------+---------+
| abc     |   20 |    1 | F      |   10000 |
| shilpa  |   12 |    2 | F      | 2000000 |
| lulu    |   22 |    2 | F      | 2000000 |
| Micheal |   42 |    2 | M      |   50000 |
| Bento   |   42 |    1 | M      | 1000000 |
| Gregory |   29 |    1 | M      |   50000 |
|         |   21 |    1 | F      |    NULL |
| NULL    |   21 |    1 | F      |    NULL |
+---------+------+------+--------+---------+

mysql> select * from dept;
+------+-----------+
| dno  | dname     |
+------+-----------+
|    1 | wholesale |
|    2 | retail    |
+------+-----------+

Q1: Fetch alternate records from emp (even and odd)

Odd:
mysql> select * from 
    -> (select (@id :=@id+1) rowid,t.* 
    -> from emp t, (select @id :=0) id) t 
    -> where rowid % 2 =1;

Even:
mysql> select * from 
    -> (select (@id :=@id+1) rowid,t.* 
    -> from emp t, (select @id :=0) id) t 
    -> where rowid % 2 !=1;

Q2: List dept no., Dept name for all the departments in which there are no employees in the department.        

mysql> select dno,dname
    -> from dept
    -> where dno NOT IN (select distinct dept from emp);

Q3: Get nth max salaries

mysql> select * from emp e1 
	-> where &n=(select count(*) from emp e2 where e1.sal <=e2.sal);


Q4: Count the total sal deptno wise where 2 or more employees exist.

mysql> select dept,sum(sal),count(*)
    -> from emp
    -> group by dept
    -> having count(*) >=2;

Q5: Write a SQL Query find number of employees according to gender whose sal is greater than 50000

mysql> select gender,count(*)
    -> from emp
    -> where sal > 50000
    -> group by  gender;




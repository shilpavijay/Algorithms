mysql> select * from post;       
+------------+--------+-------+  
| dt         | postno | likes |  
+------------+--------+-------+  
| 2017-01-01 |      1 |    12 |  
| 2017-01-01 |      2 |     0 |  
| 2017-01-01 |      3 |    10 |  
| 2017-01-02 |      1 |     0 |  
| 2017-01-02 |      2 |    10 |  
| 2017-01-02 |      3 |    20 |  
+------------+--------+-------+  


QUERY 1:
--------
The result must have three cols:  
date, no. of posts having 'likes' greater than zero, total number of likes on the given day.

mysql> select dt,count(*) postsGreaterThan0, sum(likes) sumlikes
    -> from post
    -> where likes > 0
    -> group by dt;


QUERY 2:
--------
Date should be 1st Jan and no. of likes should be greater than 15
and Date should be 2nd Jan and no. of likes should be greater than 15

mysql> select * from post
    -> where (dt = '2017-01-01' and likes > 10)
    -> UNION
    -> (select * from post
    -> where (dt = '2017-01-02' and likes > 10));
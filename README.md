# Log Analysis


This project to retrieve some statistics from database 

<br>
it's  the  third project in Fullstack web developer Nanodegree
<br>
##steps to work in this project 
* intall virtualbox
* configure it with vagrant
*Download database
*run the command
```
psql -d news -f newsdata.sql
```
## Views 
### 1- To calaulate error logins
```
create view error as select count(*) as errors,date(TIME) as date from log
where status='404 NOT FOUND' group by date order by errors DESC
```
### 2- To claculate all logins for every day
```
 create view total as select count(*) as total,date(TIME) as date from l
og group by date order by total desc
```

# Log Analysis


This project to retrieve some statistics from database 

<br>
it's  the  third project in Fullstack web developer Nanodegree
<br>
<h2> steps to work in this project </h2> 
<ul>
<li> intall virtualbox </li>
<li> configure it with vagrant</li>
<li>Download database</li>
<li>run the command
</ul>
```
   psql -d news -f newsdata.sql
```
<h2> Views </h2>
<h3> 1- To calaulate error logins </h3>
```
create view error as select count(*) as errors,date(TIME) as date from log
where status='404 NOT FOUND' group by date order by errors DESC
```
<h3> 2- To claculate all logins for every day </h3>
```
 create view total as select count(*) as total,date(TIME) as date from l
og group by date order by total desc
```

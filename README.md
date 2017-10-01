# Log Analysis


This project to retrieve some statistics from database 

<br>
it's  the  third project in Fullstack web developer Nanodegree
<br>
<h2> steps to work in this project </h2> 
<ul>
<li> intall virtualbox </li>
<li> configure it with vagrant</li>
<li>Download database from <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"> here</a></li>
<li>run the command
</ul>
<pre>
<code>
   psql -d news -f newsdata.sql
</code>
</pre>
and to run this code run the command
<pre>
<code>
   python ammarr.py
</code>
</pre>
<h2> Views </h2>
<h3> 1- To calaulate error logins </h3>
<pre><code>
create view error as select count(*) as errors,date(TIME) as date from 
log where status='404 NOT FOUND' group by date order by errors DESC
</code></pre>

<h3> 2- To claculate all logins for every day </h3>
<pre><code>
 create view total as select count(*) as total,date(TIME) as date from lo
g group by date order by total desc
</code></pre>


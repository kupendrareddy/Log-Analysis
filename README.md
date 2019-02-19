#LOG ANALYSIS
This Project is the part of the Udacity's Full Stack Web Developer Nanodegree

##PROJECT OVERVIEW
This is the solution for the Log Analysis project in Udacity's Full Stack Web Developer Nanodegree course.In this project we have to
execute three queries on large database.The queries as follows
 * Most popular three articles of all time.
 * Most popular article authors of all time.
 * Days on which more than 1% of requests lead to error.

## Helpful Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)

 
## Requirements

[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/) - An open source version control system
The code is error free and conforms PEP8 style recommendations.



## system setup and how to access this project
1. If you dont have the latest version of python download it from the link given above.
2. download and install vagrant and virtual box.
3. Download the **newsdata.sql** (extract from **LogAnalysis.zip** ) and **log.py** files and move them to your **vagrant** directory within your VM.

## RUN THESE COMMANDS FROM THE TERMINAL IN THE FOLDER WHERE YOUR VAGRANT IS INSTALLED

1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant/LogAnalysis``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python log.py``` to run the reporting tool.

## CREATE VIEW
* For third query views are:
*<h4>log_star</h4>
```sql
CREATE VIEW log_star AS
SELECT count(*) as stat, 
status, cast(time as date) as day
FROM log WHERE status like '%404%'
GROUP BY status, day
ORDER BY stat desc limit 3;
```
<h4>total_viewers</h4>
```sql
CREATE VIEW total_viewers AS
SELECT count(*) as viewers,
cast(time as date) as err_time
FROM log
GROUP BY err_time;
```
<h4>err_count</h4>
```sql
CREATE VIEW err_count AS
SELECT * from log_star join total_viewers
ON log_star.day = total_viewers.err_time;
```
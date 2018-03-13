# Log--Analysis

## Project Overview
   >In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### Pre-Requisites:
 - [Python](https://www.python.org)
 - [Vagrant](https://www.vagrantup.com)
 - [Virtual Machine](https://www.virtualbox.org)

 ### Setup Project:
  - Install Vagrant and VirtualBox
  - Download or clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
  - Download the provided data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  - Downlaod or Clone this repository.
  - Unzip this file after downloading it. The file inside is called newsdata.sql.
  - Copy the newsdata.sql file and content of this current repository.

### Launching the Virtual Machine:
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
```$ vagrant up```
1. Then Log into this using command:
```$ vagrant ssh```
1. Change directory to /vagrant and look around with ls.

### Setting up the database and Creating Views:
- Load the data in local database using the command:
```psql -d news -f newsdata.sql```

### The data provided includes three tables:
- Authors table
 The authors table includes information about the authors of articles.
- Articles table
 The articles table includes the articles themselves.
- Log table
 The log table includes one entry for each time a user has accessed the site.

Use ```psql -d news``` to connect to database.

### Create view error_view using:
 ```
 CREATE OR REPLACE
    VIEW error_view 
      AS 
      SELECT date(time) 
        AS Date,round(sum(case status when '200 OK' THEN 0 else 1 end)*100.0/count(status),1) 
        AS Error_Percentage 
      FROM log GROUP BY 
        Date 
      ORDER BY 
        Error_Percentage 
      DESC;
 ```

Collumn name        |  type
------------------- | -------------
Date                |varchar2
Error_Percentage    |float

### Running the queries:
From the vagrant directory inside the _virtual machine_,run _logs.py_ using:

``` $ python3 logs.py ```


# FSND Project Logs Analysis

The tool runs three reports to provide answers to the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project Overview

First you must have the PostgreSQL news database craeted and also, you must have imported the newsdata.sql file.
You can do that using the command below
```sql
- psql -d news -f newsdata.sql
```
The last method in the code creates a view the view is created using the following code
```sql
- create or replace view log_status as select Date,Total,Error,\
        (Error::float*100)/Total::float as Percent from\
        (select time::timestamp::date as Date, count(status) as Total,\
        sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
        from log group by time::timestamp::date) as result\
        where (Error::float*100)/Total::float > 1.0 order by Percent desc;
```
Then run the command below to run the log reporter:
```bash
python log_reporter.py
```


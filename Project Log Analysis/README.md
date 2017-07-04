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
Then run the command below to run the log reporter:
```bash
python log_reporter.py
```


#! /usr/bin/env python

from db import db_session_context

# Name of database stored in a constant for easy referencing
DB_NAME = 'news'


def show_popular_articles():
    # Find the three most popular articles of all time

    print "\n\n-- Three most popular articles of all time --"

    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT articles.title, count(log.status) as count
            FROM articles, log
            WHERE log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
            GROUP BY articles.title
            ORDER BY count desc
            LIMIT 3;
        """)
        results = cursor.fetchall()

    # for each article/view count tuple, print article -- view count
    for article in results:
        print "%s -- %s views" % (article[0], article[1])


def show_popular_authors():
    # Find the three most popular authors of all time

    print "\n\n-- Most popular authors of all time --"

    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT authors.name, count(log.status) as count
            FROM authors, articles, log
            WHERE articles.author = authors.id
              and log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
            GROUP BY authors.name
            ORDER BY count desc;
        """)
        results = cursor.fetchall()

    # For each author/view count, print author -- view count
    for author in results:
        print "%s -- %s views" % (author[0], author[1])


def error_log_status():
    # Print days on which more than 1% of requests lead to errors
    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        # Query the view log status to get what we need
        query = "select * from log_status"
        cursor.execute(query)
        result = cursor.fetchall()
        print "\n\n-- Days with more than 1% of errors: --"
        for i in range(0, len(result), 1):
            print str(result[i][0]) + " - " +str(round(result[i][3], 2)) +"% errors"


# Execute all methods
if __name__ == "__main__":
    show_popular_articles()
    show_popular_authors()
    error_log_status()

#!/usr/bin/env python
import psycopg2


# database variable globally declared
DBNAME = "news"

# Variable holding questions
query_title1 = ("1.What are the most popular three articles of all time?")
query_title2 = ("2.Who are the most popular article authors of all time?")
query_title3 = ("3.On which days did more than 1% of requests lead to errors?")

# First query
query1 = """SELECT articles.title AS Articles,COUNT(*)
            as Views FROM articles,log WHERE log.path
            LIKE concat('%',articles.slug,'%') AND
            log.status LIKE '%200 OK%' GROUP BY
            articles.title,path ORDER BY Views DESC
            LIMIT 3"""
# Second query
query2 = """SELECT authors.name AS Author,COUNT(*) AS Views
            FROM log,authors,articles WHERE path LIKE
            concat('%',articles.slug,'%') AND authors.id=articles.author
            AND log.status LIKE '%200 OK%' GROUP BY authors.name ORDER BY
            Views DESC """
# Third query
query3 = """SELECT * FROM error_view WHERE Error_Percentage > 1 """


def answer_query(query):
	"""Connects to database ,intialize a cursor
	executes query and returns all rows fetched
	"""
	# connecting to database
    db = psycopg2.connect(database=DBNAME)
    # Initiating cursor
    c = db.cursor()
    # Query execution
    c.execute(query)
    # fetching contents of table
    results = c.fetchall()
    # Closing database
    db.close()
    return results


# Function to print third query
def printerrorquery(results):
    """prints Question ,takes results, and displays results"""
    print(query_title3)
    # Loop to fetch and print values of result
    for i in results:
        Article = i[0]
        Views = i[1]
        print("\t %s -- %.1f" % (Article, Views) + " % errors")


# Function to print first and second query
def printmequery(results, title):
    """Prints result of query and title of question"""
    print(title)
    for i in results:
        Article = i[0]
        Views = i[1]
        print('\t %s -- %d' % (Article, Views) + " views")

result1 = answer_query(query1)
printmequery(result1, query_title1)
print('\n')
result2 = answer_query(query2)
printmequery(result2, query_title2)
print('\n')
results3 = answer_query(query3)
printerrorquery(results3)

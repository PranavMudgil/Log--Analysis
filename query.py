import psycopg2,bleach


#database variable globally declared
DBNAME = "news"

#Variable holding questions
query_title1 = ("1. What are the most popular three articles of all time?")
query_title2 = ("2. Who are the most popular article authors of all time?")
query_title3 = ("3. On which days did more than 1% of requests lead to errors?")

#First query
query1 = """select articles.title as Articles,count(*)
             as Views from articles,log where log.path
             like concat('%',articles.slug,'%') and 
             log.status like '%200 OK%' group by
             articles.title,path order by Views desc
             limit 3"""
#Second query
query2 = """select authors.name as Author,count(*) as Views
         from articles,log,authors where articles.author=authors.id
         and log.path like concat('%',articles.slug,'%') and 
         log.status like '%200%' group by authors.name,log.path order
         by log.path desc limit 3"""
#Third query
query3 = "select * from error_view where Error_Percentage > 1 "
def answer_query(query):
    #connecting to database
    db = psycopg2.connect(database=DBNAME)
    #Initiating cursor
    c = db.cursor()
    #Query execution
    c.execute(query)
    #fetching contents of table
    results = c.fetchall()
    #Closing database
    db.close()
    return results

#Function to print third query
def printerrorquery(results):
    print(query_title3)
    #Loop to fetch and print values of result
    for i in results:
        Article = i[0]
        Views = i[1]
        print("\t %s -- %.1f" %(Article,Views)+" % errors")

#Function to print first and second query        
def printmequery(results,title):
    print(title)
    for i in results:
        Article = i[0]
        Views = i[1]
        print('\t %s -- %d' %(Article,Views)+" views")
        
result1 = answer_query(query1)
printmequery(result1,query_title1)
print('\n')
result2 = answer_query(query2)
printmequery(result2,query_title2)
print('\n')
results3 = answer_query(query3)
printerrorquery(results3)

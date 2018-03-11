import psycopg2,bleach


DBNAME = "news"

query_title1 = ("1. What are the most popular three articles of all time?")
query_title2 = ("2. Who are the most popular article authors of all time?")
query_title3 = ("3. On which days did more than 1% of requests lead to errors?")
query1 = """select articles.title as Articles,count(*)
             as Views from articles,log where log.path
             like concat('%',articles.slug,'%') and 
             log.status like '%200 OK%' group by
             articles.title,path order by Views desc
             limit 3"""

query2 = """select authors.name as Author,count(*) as Views
         from articles,log,authors where articles.author=authors.id
         and log.path like concat('%',articles.slug,'%') and 
         log.status like '%200%' group by authors.name,log.path order
         by log.path desc limit 3"""

query3 = "select * from error_view where Error_Percentage > 1 "
def answer_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def printerrorquery(results):
    print(query_title3)
    for i in results:
        Article = i[0]
        Views = i[1]
        print("\t %s -- %.1f" %(Article,Views)+" % errors")
        
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

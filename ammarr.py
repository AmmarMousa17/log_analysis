import psycopg2

DBNAME = "news"


# Function execute query and return results from database news


def query_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# query to answer first question
query1 = (
    "select  count(*) as count ,articles.title "
    "from articles inner join log on log.path "
    "like concat('/article/', articles.slug) group by "
    "articles.title, log.path order by count desc limit 3")

# query to answer second question
query2 = (
    "select count(*) as count ,authors.name from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('/article/', articles.slug)"
    " group by authors.name order by count desc")

# query to answer third question
query3 = (
    "select total.date ,(100.0*error.errors)/total.total "
    " from error join total "
    "on total.date=error.date "
    "where (100.0*error.errors)/total.total>1.0")

# store query results and question and title in Dictionary
query_1 = {
    'question': " The 3 most popular articles of all time are:\n",
    'results': query_results(query1)}

query_2 = {
    'question': " The most popular article authors of all time are:\n",
    'results': query_results(query2)}

query_3 = {
    'question': " Days with more than 1% of request that lead to an error:\n",
    'results': query_results(query3)}


# print first and second queries


def print_views(query_result):
    print (query_result['question'])
    for result in query_result['results']:
        print(str(result[0]) + ' .... ' + str(result[1]) + ' views \n')


# print the last query


def print_errors(query_result):
    print (query_result['question'])
    for result in query_result['results']:
        print(str(result[0]) + ' .... ' + str(result[1]) + ' % errors')


# last output
print_views(query_1)
print_views(query_2)
print_errors(query_3)

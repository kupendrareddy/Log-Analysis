# !/usr/bin/env python3

import psycopg2 as pscg

DB = "news"


first_1 = ("SELECT title, count(*) as views FROM articles \n"
           "  JOIN log\n"
           "    ON articles.slug = substring(log.path, 10)\n"
           "    GROUP BY title ORDER BY views DESC LIMIT 3;")


second_2 = ("SELECT authors.name, count(*) as views\n"
            "    FROM articles \n"
            "    JOIN authors\n"
            "      ON articles.author = authors.id \n"
            "      JOIN log \n"
            "      ON articles.slug = substring(log.path, 10)\n"
            "      WHERE log.status LIKE '200 OK'\n"
            "      GROUP BY authors.name ORDER BY views DESC;")


third_3 = ("SELECT round((stat*100.0)/viewers, 3) as\n"
           "        result, to_char(err_time, 'Mon DD, YYYY')\n"
           "        FROM err_count ORDER BY result desc limit 1;")

# Connect to the database and feed query to extract results


def get_queryResults(sql_query):
    db = pscg.connect(database=DB)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results


answ1 = get_queryResults(first_1)
answ2 = get_queryResults(second_2)
answ3 = get_queryResults(third_3)


# Create a function to print query results


def print_answ(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")


print("What are the most popular articles of all time?")
print_answ(answ1)
print("Who are the most popular article authors of all time?")
print_answ(answ2)
print("On which days more than 1% of the requests led to error?")
print("\t" + answ3[0][1] + " - " + str(answ3[0][0]) + "%")

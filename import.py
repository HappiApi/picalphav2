import os
import psycopg2
import urlparse
import csv

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://vdbennzvevmumz:4IyA_mZ8eHxsKN1go1yrpUa_FI@ec2-54-204-20-209.compute-1.amazonaws.com:5432/d9js65ocv8ilj7")

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor = conn.cursor()

def pluck(props, row):
    return [ row[prop] for prop in props ]

with open('data/ks4/2014_KS4.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    filtered = filter(lambda x: int(x["RECTYPE"]) < 3, reader)
    values = map(lambda x: pluck(['URN', 'SCHNAME', 'NFTYPE', 'ADMPOL'], x), filtered)
    values = values[1756:]
    for value in values:
        print(value[0], value[1])
        cursor.execute(
            """INSERT INTO schools (pic_code, name, type, admission)
            VALUES (%s, %s, %s, %s);""",
            value)
    # cursor.executemany(
    #     """INSERT INTO schools (pic_code, name, type, admission)
    #     VALUES (%s, %s, %s, %s);""",
    #     values);
    conn.commit()
    cursor.close()
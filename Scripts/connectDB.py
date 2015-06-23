import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://jbtupggsocbcax:g3ak8Wslf8dNWtIfqYVVPOieEt@ec2-54-195-252-202.eu-west-1.compute.amazonaws.com:5432/d19mqfm9qh2juj")

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor = conn.cursor()
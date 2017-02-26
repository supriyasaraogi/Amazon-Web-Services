import boto
import uuid
#import boto.s3.connection
#import mysql.connector
import csv
import time
import urllib
import pymysql
import random
import sys
from itertools import *
import credentials
import boto.ec2
import memcache
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
application = Flask(__name__)

@application.route('/search', methods=['GET'])
def memcache():
		result={}
		global count
		#memcache.flush_all()
		#client = Client(('asgn3cluster.enu0sa.0001.usw2.cache.amazonaws.com', 11211))
		mc = memcache.Client(['supriyacluster.es0cdo.0001.usw2.cache.amazonaws.com:11211'])
		print mc
		print "enter the table name:",
		filename = raw_input()
		cur = conn.cursor()
		count_query='SELECT COUNT(*) FROM {}'.format(filename)
		cur.execute(count_query)
		count_res=cur.fetchall()
		for row in count_res:
			count=row[0]
		before-time = time.time()
		print("enter the number of times")
		times=int(raw_input())
		for i in range(0,times):
			rand_number = random.randrange(0, count)
			query = 'SELECT * FROM {} where CountryorTerretory {}'.format(filename,rand_number)
			print rand_number
			key = str(rand_number)
			if mc.get(key) is not None:
				result[str(key)]= mc.get(key)
				print ("Taking from memcache")
			else:
				cur.execute(query)
				res= cur.fetchall()
				print res
				for row in res:
					key=row[0]
				print(key)
				print("from rds")
				mc.add(str(key),res)
				result[str(key)]=res
		print result
		after-time = time.time()
		duration=after-time-before-time

		print "Time taken to execute select query with memcache 10 " + " times = " + str(duration) + " seconds"
		return float(duration)
		return render_template('upload.html', z=duration)
		print "successful"
		random()
def random():
    print("enter the number of times")
    times = int(raw_input())
    beforeTime = time.time()
    print "enter the table name:",
    filename = raw_input()
    with conn.cursor() as cur :
	#alter_query= 'alter table {} add column tableid int auto_increment primary key first'.format(filename)
	#cur.execute(alter_query)
        for i in range(1, times):
            rand_number = random.randrange(0, 10)
            query = 'SELECT * FROM {} where CountryorTerritory {}'.format(filename, rand_number)
            cur.execute(query)
            print(cur.fetchall())
    afterTime = time.time()
    timeDifference = afterTime - beforeTime
    print "Time difference: "
    print timeDifference
    return float(timeDifference)


conn = pymysql.connect(credentials.rds_host, user=credentials.username, passwd=credentials.password,
                      db=credentials.dbname)
ran_time=random_gen()
mem_time=memcache_query()
total=ran_time-mem_time

if __name__ == "__main__":
    application.run()	
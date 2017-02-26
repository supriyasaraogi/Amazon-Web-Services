import boto
import uuid
import boto.s3.connection
from random import Random as _Random
import mysql.connector
import credentials
import csv
import time
import urllib
import os
import pymysql
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
application = Flask(__name__)

config = {
'user': credentials.username,
'password': credentials.password,
'host':credentials.rds_host,
'database': credentials.dbname,
'raise_on_warnings': True
}
conn = mysql.connector.connect(**config)
cur=conn.cursor()

s3 = boto.connect_s3(credentials.AWS_ACCESS_KEY_ID, credentials.AWS_SECRET_ACCESS_KEY, is_secure=False)
bucket=s3.lookup('akiajakmp7pc25yg4bfqsupriyasaraogi')
key=bucket.lookup('UNPrecip.csv')
def upload_to_db():

		print("enter the bucket name:"),
		bucket_name = raw_input()
		bucket = s3.get_bucket(bucket_name)

		all_users = 'http://acs.amazonaws.com/groups/global/AllUsers'

		for key in bucket:
			print str(key).split(",")
			readable = False
			acl = key.get_acl()
			for grant in acl.acl.grants:
				if grant.permission == 'READ':
					if grant.uri == all_users:
						readable = True
			if not readable:
				key.make_public()

		opens = urllib.URLopener()
		print("enter the filename:"),
		file_name = raw_input()
		link = "wget https://s3.amazonaws.com/" + bucket_name + "/" + file_name
		os.system(link)
		name_list = file_name.split('.')
		filename = name_list[0]
		#create_stmt="create table SupriyaDatabase.newfile (C1 integer primary key, C2 varchar(50), C3 varchar(50), C4(varcharr(50))'
		#query ="create table SupriyaDatabase.{}(CountryorTerritory varchar(50), StationName varchar(50), WMOStationNumber varchar(50), Unit varchar(50), Jan varchar(50), Feb varchar(50), Mar varchar(50), Apr varchar(50), May varchar(50), Jun varchar(50), Jul varchar(50), Aug varchar(50), Sep varchar(50), Oct varchar(50), Nov varchar(50), December varchar(50) )".format(filename)
		#cur.execute(query)
		uploadCSV = """LOAD DATA LOCAL INFILE 'UNPrecip.csv' INTO TABLE SupriyaDatabase.UNPrecip FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES """
		cur.execute(uploadCSV)
		conn.commit()

upload_to_db()
if __name__ == "__main__":
    application.run()	
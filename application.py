import boto
import boto.s3
import sys
from boto.s3.key import Key
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

HOST= str(os.getenv('VCAP_APP_HOST', 'localhost'))
PORT=int(os.getenv('VCAP_APP_PORT', '5000'))

AWS_ACCESS_KEY_ID= 'AKIAJAKMP7PC25YG4BFQ'
AWS_SECRET_ACCESS_KEY='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'

bucket_name = AWS_ACCESS_KEY_ID.lower() + 'supriyasaraogi'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
	AWS_SECRET_ACCESS_KEY)



bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

@app.route('/')
def Welcome():
    return render_template('example.html')
print "working.."

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()
       # conn = S3Connection(settings.ACCESS_KEY, settings.SECRET_KEY)
       #bucket = conn.get_bucket(settings.BUCKET_NAME)
    
@app.route('/upload', methods=['POST'])
def upload():
    testfile = request.files['file']
    print 'Uploading %s to Amazon S3 bucket %s' % \
		(testfile, bucket_name)
    k = Key(bucket)
    k.key = 'new 2'
        # k.set_contents_from_file(data_file)
    k.set_contents_from_filename(testfile.filename,
    cb=percent_cb, num_cb=10)
    print "working..1"
        # return jsonify(name=file_name)
        #return jsonify(name=file_name)
    return render_template('upload.html')
print "success"


    

#port = os.getenv('PORT', '8000')
if __name__ == "__main__":
    app.run()

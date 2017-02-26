# Amazon-Web-Services
Database and Cache:
1. Get access to AWS (Amazon Cloud).
2. Find a large dataset (50K tuples or larger)

http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php (test, small)
https://www.data.gov/ (many here, for example vehicle recalls)

3. Copy that file to AWS, and time (instrument) how much time it takes.
4. Put the data into a Relational DB. (time)
5. the code to do one thousand, 5 thousand and 20 thousand random
(small) queries. (time)
6. Repeated using queries of only 200 to 800 tuples.
7. Repeated previous two steps using “Elastic” Cache (Memcache, etc.)
8.
Web Services :
Using AWS repeated creating and queries of data created a Web interface allowing users
(of that web interface) to dynamically create queries.
(Show times on web page)

# DealerSpider
Spider that crawls the dealer information from http://www.statecollege.com/auto/dealers

# Library
Library needed:
	
* Redis	
* Python 2.7.x
* redis-py
* hiredis
* scrapy 1.x

# Run
To run the DealerSpider, first you need to install scrapy

```
$ sudo pip install scrapy
```

Then the Redis database

```
$ brew install redis
```

Then install the redis-py

```
$ sudo pip install redis
```

Then hiredis

```
$ pip install hiredis
```

Then start redis server

```
$ redis-server
```

Finally run the following command in the root dirctory of DealerSpider project

```
$ scrapy crawl dealerspider
```
Then all cars' data from http://www.statecollege.com/auto/dealers/ would be stored into your local redis database.


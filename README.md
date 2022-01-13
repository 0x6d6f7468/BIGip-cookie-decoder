# F5 Big-IP cookie decoder

Now upgraded to support Python 3. Requires Python 3.6+

This Python script takes an F5 BIG-IP persistence cookie and decodes the IP address and TCP port values. This allows you to determine the internal IP address(es) of a load balanced webserver. Typically, Big-IP cookies are composed by a prefix of "BIGipServer", the pool name and contain an encoded string (internal IP address and port of the load-balanced web server).

This is an example of a Big-IP Cookie from the internet:

```
BIGipServer<pool_name>=1677787402.36895.0000
```

Sample usage:

```
$ python3 BIGIP_decode_cookie.py BIGipServer<pool_name>=1677787402.36895.0000

[*] Cookie to decode: BIGipServer<pool_name>=1677787402.36895.0000

[*] Pool name: <pool_name>
[*] Decoded IP and Port: 10.1.1.100:8080

```

Thanks to https://penturalabs.wordpress.com/2011/03/29/how-to-decode-big-ip-f5-persistence-cookie-values/ 

import httplib, urlparse, sys
from pymd5 import md5, padding
#url = sys.argv[1]

# Your code to modify url goes here

url = 'https://eecs388.org/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp'
parsedURL = urlparse.urlparse(url)
token = urlparse.parse_qs(parsedURL.query)['token'][0]

print token


#url = 'https://eecs388.org/project1/api?token=acc711db59ca4e60872e9afd9466cdc7&user=admin&command1=ListFiles&command2=NoOp'
#parsedUrl = urlparse.urlparse(url)

#conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
#conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
#print conn.getresponse().read()
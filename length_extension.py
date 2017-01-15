import httplib, urlparse, sys
from pymd5 import md5, padding
import urllib
#url = sys.argv[1]

# Your code to modify url goes here

url = 'https://eecs388.org/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp'
parsedURL = urlparse.urlparse(url)


dict =  urlparse.parse_qs(parsedURL.query)

#print parsedURL.scheme
token = urlparse.parse_qs(parsedURL.query)['token'][0]
end_url = "&user="+dict['user'][0]+"&command1="+dict['command1'][0]+"&command2="+dict['command2'][0]
begin_url = parsedURL.scheme+"://"+ parsedURL.netloc + parsedURL.path+"?token="

length_of_m = (len(end_url) + 7)

bits = (length_of_m + len(padding(length_of_m*8)))*8

h = md5(state = token.decode("hex"), count = bits)
x = "&command3=UnlockAllSafes"
h.update(x)

url = begin_url+h.hexdigest()+end_url+urllib.quote(padding(length_of_m*8))+x

#url = 'https://eecs388.org/project1/api?token=acc711db59ca4e60872e9afd9466cdc7&user=admin&command1=ListFiles&command2=NoOp'
parsedUrl = urlparse.urlparse(url)

conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()





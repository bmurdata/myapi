import urllib.request as req,  json 

def testLink(baseURL:str()):
    with req.urlopen(baseURL) as url:
        data=json.loads(url.read().decode())
    print(len(data))
    print(data)

# Test functions present in azurefunctions, with code option
print("Testing Jobs search by Code")

myurl="http://localhost:7071/api/byjobcode?code=454668"
testLink(myurl)

print("Testing Metadata search by Code")

myurl="http://localhost:7071/api/jobMeta?code=466305"
testLink(myurl)

print("Testing full content search by Code")

myurl="http://localhost:7071/api/jobPost?code=466305"
testLink(myurl)
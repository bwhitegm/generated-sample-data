import os
import json
import urllib3

http = urllib3.PoolManager()

###url - base url to fhir endpoint
###json - json body, unencoded
def make_fhir_request(url, jdata):
    encoded = json.dumps(jdata).encode('utf-8')
    r = http.request(
        "POST",
        url,
        headers={
            'Content-Type':'application/fhir+json'
        },
        body=encoded
    )
    print(r.status)

print("server url (default http://localhost:4004/fhir):")
server = input()
if server == "":
    server = "http://localhost:4004/fhir"
os.chdir("..")
wd = os.getcwd()
datad = os.path.join(wd, "R4/SYNTHEA")
files = os.listdir(datad)
for file in files:
    print(file)
    filepath = os.path.join(datad, file)
    with open(filepath, 'r', encoding="utf-8") as f:
        jdata = json.load(f)
        make_fhir_request(server, jdata)






import requests
import os
from pprint import pprint
import lxml.etree as etree
import re


pkt="66649bbf6490008a9615c48486dd600aafc604c4063b260088010422020061fd779b2a8f8ce52607f8b040030c160000000000000080de0201bbf9372e88938c5b768010005a120700000101080aacec9f5e658bd18114dfce7a8d3ecdb0230501"
#url= f"https://hpd.gasmi.net/api.php?force=ipv6&format=text&data={pkt}"


#pkt="pkt.txt"
type="ipv6"
#pkt=input("Enter packet:")
#type=input("Enter Packet Type... ipv4/ipv6:")

if re.match(r'.*\.txt$',pkt,re.IGNORECASE):
    try:
        FD=open(pkt)
        pkt=FD.readlines()
        pkt=(''.join(pkt))
        #print(pkt)
    except:
        print("File Open error")


#print(pkt)
try:
    url = f"https://hpd.gasmi.net/api.php?&force={type}&data={pkt}"
    #print(url)
    cmd = f"curl https://hpd.gasmi.net/api.php?force={type}&data={pkt}"

    #data=os.system(cmd)
    data=requests.get(url)

except:
    print("An Exception Occurred")


#x = etree.parse(data.content)
etree.tostring(data.content, encoding='unicode', pretty_print=True)
#print (etree.tostring(data.content, pretty_print=True))
#pprint(data.content)
#pprint(x)
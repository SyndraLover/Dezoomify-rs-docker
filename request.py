import requests
import sys

link=str(sys.argv[2])
url=str(sys.argv[1])
requests.post(url=url, json={"link":link})
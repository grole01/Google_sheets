import requests

proxy="64.235.204.107:8080"

r =requests.get("https://httpbin.org/ip", proxies={"http":proxy,"https":proxy}, timeout=5)

#print(r.json())
print(r.status_code)
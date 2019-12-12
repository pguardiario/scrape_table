from selenium import webdriver
import json, os, sys

if os.popen('pwd').read().strip() == '/home/runner':
  os.system("chmod +x /home/runner/phantomjs")
  driver = webdriver.PhantomJS(executable_path='/home/runner/phantomjs')
else:
  driver = webdriver.Chrome()

driver.get("https://www.coinbase.com/price")

# inject jquery + tabletojson
from requests import get
for js in ["http://code.jquery.com/jquery-1.11.3.min.js", "https://cdn.jsdelivr.net/npm/table-to-json@0.13.0/lib/jquery.tabletojson.min.js"]:
  body = get(js).content.decode('utf8')
  driver.execute_script(body)

# get that data out painlessly
data = driver.execute_script("return $('table').tableToJSON()")
driver.close()

print(json.dumps(data, indent=2))
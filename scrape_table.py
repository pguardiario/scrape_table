from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.coinbase.com/price")

# inject jquery + tabletojson
from requests import get
for js in ["http://code.jquery.com/jquery-1.11.3.min.js", "https://cdn.jsdelivr.net/npm/table-to-json@0.13.0/lib/jquery.tabletojson.min.js"]:
  body = get(js).content.decode('utf8')
  driver.execute_script(body)

# get that data out painlessly
data = driver.execute_script("return $('table').tableToJSON()")

print('x')
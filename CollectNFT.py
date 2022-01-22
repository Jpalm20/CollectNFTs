import requests
import json
import shutil

url = "https://api.opensea.io/api/v1/assets?owner={WALLET ADDRESS}&order_direction=desc&offset=0&limit=20"

response = requests.request("GET", url)

formatted = response.text
temp = json.loads(formatted)

ids = []
for item in temp['assets']:
    ids.append(item['image_url'])

index = 1
for id in ids:
	res = requests.get(id, stream=True)
	if res.status_code == 200:
		with open('id#'+str(index)+'.jpg', 'wb') as f:
			shutil.copyfileobj(res.raw, f)
		print('Image sucessfully Downloaded')
		index+=1
	else:
		print('Image Couldn\'t be retrieved')

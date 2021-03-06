#------------------------------------------------------------------------------
# Update product in a catalog.  
# PUT  /v1/catalog/{catalog_name}/products/{id}
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header
# Replace 'your_api_key' with your API key.
headers = {'X-Api-Key': props['X-Api-Key']}

# Catalog name.
catalog_name = 'sample_catalog'

# Product id.
id = 'ABOFA15AWWWSW1149401'

# API end point,
api_endpoint = '/v1/catalog/%s/products/%s'%(catalog_name,id)

url = urljoin(api_gateway_url,api_endpoint)

data = {}
data['out_of_stock'] = 'yes'

params = {}
# Optional parameters.
params['download_images'] = 'true'
params['ignore_detail_images'] = 'true'

response = requests.put(url,
                        headers=headers,
                        json=data,
                        params=params)

print response.status_code
pprint(response.json())


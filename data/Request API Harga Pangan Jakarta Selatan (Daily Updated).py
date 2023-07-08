#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests


# # 8 Juli 2023

# In[2]:


url_jaksel = "https://infopangan.jakarta.go.id/publik/market/id/34"


# In[3]:


header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


# In[49]:


jaksel_tebet = "https://infopangan.jakarta.go.id/api/price/lists?mid=34"


# In[50]:


# API Request
r = requests.get(jaksel_tebet, headers = header).json()


# In[51]:


print(r)


# In[52]:


# scraping
name_product_list = []
price_list = []
prev_price_list = []
change_price_list = []
satuan_list = []

product_data = r['data']['prices']

for item in product_data:
    name_product_list.append(item['name'])
    price_list.append(item['price'])
    prev_price_list.append(item['price_compare'])
    change_price_list.append(item['changed'])
    satuan_list.append(item['unit'])


# In[53]:


import csv

# combine
rows = zip(name_product_list, price_list, prev_price_list, change_price_list, satuan_list)

csv_file = 'jaksel_pasar_tebet.csv'

# write to csv
with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    
    # write the header row
    writer.writerow(['nama_produk', 'harga_produk', 'harga_sebelumnya', 'perubahan_harga', 'satuan'])
    
    # write rows
    writer.writerows(rows)
    
print("Data has been saved to", csv_file)


# In[54]:


jaksel_pasming = "https://infopangan.jakarta.go.id/api/price/lists?mid=9"


# In[56]:


# API Request
r = requests.get(jaksel_pasming, headers = header).json()


# In[57]:


# scraping
name_product_list = []
price_list = []
prev_price_list = []
change_price_list = []
satuan_list = []

product_data = r['data']['prices']

for item in product_data:
    name_product_list.append(item['name'])
    price_list.append(item['price'])
    prev_price_list.append(item['price_compare'])
    change_price_list.append(item['changed'])
    satuan_list.append(item['unit'])


# In[58]:


import csv

# combine
rows = zip(name_product_list, price_list, prev_price_list, change_price_list, satuan_list)

csv_file = 'jaksel_pasar_minggu.csv'

# write to csv
with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    
    # write the header row
    writer.writerow(['nama_produk', 'harga_produk', 'harga_sebelumnya', 'perubahan_harga', 'satuan'])
    
    # write rows
    writer.writerows(rows)
    
print("Data has been saved to", csv_file)


# In[59]:


jaksel_kebayoran_lama = "https://infopangan.jakarta.go.id/api/price/lists?mid=28"


# In[60]:


# API Request
r = requests.get(jaksel_kebayoran_lama, headers = header).json()


# In[61]:


# scraping
name_product_list = []
price_list = []
prev_price_list = []
change_price_list = []
satuan_list = []

product_data = r['data']['prices']

for item in product_data:
    name_product_list.append(item['name'])
    price_list.append(item['price'])
    prev_price_list.append(item['price_compare'])
    change_price_list.append(item['changed'])
    satuan_list.append(item['unit'])


# In[62]:


import csv

# combine
rows = zip(name_product_list, price_list, prev_price_list, change_price_list, satuan_list)

csv_file = 'jaksel_kebayoran_lama.csv'

# write to csv
with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    
    # write the header row
    writer.writerow(['nama_produk', 'harga_produk', 'harga_sebelumnya', 'perubahan_harga', 'satuan'])
    
    # write rows
    writer.writerows(rows)
    
print("Data has been saved to", csv_file)


# In[72]:


jaksel_cipete = "https://infopangan.jakarta.go.id/api/price/lists?mid=29"


# In[73]:


# API Request
r = requests.get(jaksel_cipete, headers = header).json()


# In[74]:


# scraping
name_product_list = []
price_list = []
prev_price_list = []
change_price_list = []
satuan_list = []

product_data = r['data']['prices']

for item in product_data:
    name_product_list.append(item['name'])
    price_list.append(item['price'])
    prev_price_list.append(item['price_compare'])
    change_price_list.append(item['changed'])
    satuan_list.append(item['unit'])


# In[75]:


import csv

# combine
rows = zip(name_product_list, price_list, prev_price_list, change_price_list, satuan_list)

csv_file = 'jaksel_cipete.csv'

# write to csv
with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    
    # write the header row
    writer.writerow(['nama_produk', 'harga_produk', 'harga_sebelumnya', 'perubahan_harga', 'satuan'])
    
    # write rows
    writer.writerows(rows)
    
print("Data has been saved to", csv_file)


# In[76]:


jaksel_la = "https://infopangan.jakarta.go.id/api/price/lists?mid=32"


# In[77]:


# API Request
r = requests.get(jaksel_la, headers = header).json()


# In[78]:


# scraping
name_product_list = []
price_list = []
prev_price_list = []
change_price_list = []
satuan_list = []

product_data = r['data']['prices']

for item in product_data:
    name_product_list.append(item['name'])
    price_list.append(item['price'])
    prev_price_list.append(item['price_compare'])
    change_price_list.append(item['changed'])
    satuan_list.append(item['unit'])


# In[79]:


import csv

# combine
rows = zip(name_product_list, price_list, prev_price_list, change_price_list, satuan_list)

csv_file = 'jaksel_la.csv'

# write to csv
with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    
    # write the header row
    writer.writerow(['nama_produk', 'harga_produk', 'harga_sebelumnya', 'perubahan_harga', 'satuan'])
    
    # write rows
    writer.writerows(rows)
    
print("Data has been saved to", csv_file)


# In[ ]:





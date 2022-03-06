#!/usr/bin/env python
# coding: utf-8

# In[28]:


get_ipython().system('pip install selenium')


# In[29]:


url= 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&p%5B%5D=facets.brand%255B%255D%3DAPPLE&otracker=clp_metro_expandable_6_26.metroExpandable.METRO_EXPANDABLE_Apple_laptops-store_SKIHMOPFPDC3_wp9&fm=neo%2Fmerchandising&iid=M_b4d0e2ef-aaac-4e7e-9272-9b8be53c2dc5_26.SKIHMOPFPDC3&ppt=clp&ppn=laptops-store&ssid=j5fwd6niaz0hnchs1645514684273'


# In[30]:


import os


# In[31]:


os.chdir('E:/Scripting')


# In[32]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[33]:


browser = webdriver.Firefox()
browser.get(url)


# In[34]:


html = browser.page_source
html


# In[35]:


soup = BeautifulSoup(html,'html.parser')
soup


# In[36]:


soup.select('div._4rR01T')


# In[37]:


soup.select('div._4rR01T')[0].text


# In[38]:


product_name=[i.text for i in soup.select('div._4rR01T')]
product_name


# In[54]:


len(product_name)


# In[39]:


soup.select('div._30jeq3._1_WHN1')[0].text


# In[40]:


product_cost=[i.text for i in soup.select('div._30jeq3._1_WHN1')]
product_cost


# In[56]:


len(product_cost)


# In[41]:


soup.select('div._3LWZlK')


# In[42]:


product_rating=[i.text for i in soup.select('div._3LWZlK')]
product_rating


# In[57]:


len(product_rating)


# In[43]:


soup.select('span._2_R_DZ')[0].text


# In[44]:


total_ratings_total_reviews=[i.text for i in soup.select('span._2_R_DZ')]
total_ratings_total_reviews


# In[58]:


len(total_ratings_total_reviews)


# In[63]:


soup.select('ul._1xgFaf')[1].text


# In[72]:


device_specs= [i.text for i in soup.select('ul._1xgFaf')]
device_specs


# In[73]:


len(device_specs)


# In[76]:


import pandas as pd
def macbook(soup):
    device_specs= [i.text for i in soup.select('ul._1xgFaf')]
    total_ratings_total_reviews=[i.text for i in soup.select('span._2_R_DZ')]
    product_rating=[i.text for i in soup.select('div._3LWZlK')]
    product_cost=[i.text.strip() for i in soup.select('div._30jeq3._1_WHN1')]
    product_name=[i.text.strip() for i in soup.select('div._4rR01T')]
    return pd.DataFrame({"Product Name":product_name,"Price":product_cost,"Rating out of 5":product_rating,"Total Ratings and Reviews":total_ratings_total_reviews,"Specifications":device_specs})


# In[77]:


df = macbook(soup)
df


# In[81]:


df.describe()


# In[83]:


df.shape


# In[84]:


df.to_csv("MacBook products.csv")


# In[85]:


df.to_csv()


# In[ ]:





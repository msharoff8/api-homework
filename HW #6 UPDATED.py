
# coding: utf-8

# 3 Takeaways:
# 
# 1. Temperature almost always falls with increasing latitude. While these temperatures were taken in a small sample of cities on one particular day, the trend is striking, and conforms to common knowledge. 
# 
# 2. In the 500 cities sampled, humidity rises at higher latitudes. However, this may reflect seasonality or time of day.
# 
# 3. There is no strong relationship between latitude and wind speed or cloudiness.

# In[5]:


lon=[]
lat=[]
Temperature=[]
Humidity=[]
Cloudiness=[]
WindSpeed=[]
City=[]

for x in range(10000): 
    lon.append(random.randint(-180, 180))
    lat.append(random.randint(-90, 90))

city_weather=pd.DataFrame({'lon':lon,
                          'lat': lat})

city_weather['temp']=''
city_weather['hum']=''
city_weather['cloud']=''
city_weather['wind']=''
city_weather['city']=''

counter=0

city_weather.head()


# In[6]:


while counter<500:
    for index, row in city_weather.iterrows():
        url = "http://api.openweathermap.org/data/2.5/weather?"

        lon = str(row['lon'])
        lat = str(row['lat'])

        query_url=url+'appid='+api_key+'&lat='+lat+'&lon='+lon
        
        response=requests.get(query_url)
        
        response=response.json()
        
         
        if response['name']!='':
    
            city_weather.set_value(index, "city",
                                response["name"])
            city_weather.set_value(index, "temp",
                                response["main"]["temp"])
            city_weather.set_value(index, "hum",
                                response["main"]["humidity"])
            city_weather.set_value(index, "cloud",
                                response["clouds"]["all"])
            city_weather.set_value(index, "wind",
                                response["wind"]["speed"])
        
            counter=counter+1
        
            print(response['id'])
            print(response['name'])


# In[16]:


city_weather.head(500)


# In[27]:


plot_df=city_weather.loc[city_weather['city']!='',:]
plot_df.head(500)


# In[44]:


latitude=plot_df['lat']
longitude=plot_df['lon']
temperature=(9/5)*(plot_df['temp']-273)+32
humidity=plot_df['hum']
cloudiness=plot_df['cloud']
windiness=plot_df['wind']*2.24


# In[47]:


plt.scatter(latitude, temperature, marker="o", facecolors="red", edgecolors="black",
            s=latitude, alpha=0.75)

plt.title('Temperature by Latitude, 4/1/2018')
plt.xlabel('Latitude')
plt.ylabel('Temperature (F)')
plt.savefig('Graph#1')


# In[50]:


plt.scatter(latitude, humidity, marker="o", facecolors="red", edgecolors="black",
            s=latitude, alpha=0.75)

plt.title('Humdity by Latitude, 4/1/2018')
plt.xlabel('Latitude')
plt.ylabel('Humidity (%)')
plt.savefig('Graph#2')


# In[51]:


plt.scatter(cloudiness, humidity, marker="o", facecolors="red", edgecolors="black",
            s=latitude, alpha=0.75)

plt.title('Cloudiness by Latitude, 4/1/2018')
plt.xlabel('Latitude')
plt.ylabel('Cloudiness (%)')
plt.savefig('Graph#3')


# In[52]:


plt.scatter(latitude, windiness, marker="o", facecolors="red", edgecolors="black",
            s=latitude, alpha=0.75)

plt.title('Wind Speed by Latitude, 4/1/2018')
plt.xlabel('Latitude')
plt.ylabel('Wind Speed (mph)')
plt.savefig('Graph#4')


# In[55]:


plot_df.to_csv('Weather Data.csv')


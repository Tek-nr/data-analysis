#!/usr/bin/env python
# coding: utf-8

# #  Veri Bilimi İçin İstatistik

# ### Örnek Teorisi

# In[1]:


import numpy as np


# In[2]:


populasyon = np.random.randint(0,80,10000)


# In[4]:


populasyon[0:10]


# In[9]:


#örneklem çekimi
np.random.seed(115) #fonksiyonu tekrar çalıştırdığımızda 
                #aynı örneklemleri çekmemizi sağlar
orneklem = np.random.choice(a=populasyon, size =100) #Populasyonun üzerinden 
                                            #rastgele x (100) tane örnek çek 
orneklem[0:10]


# In[10]:


orneklem.mean()


# In[11]:


populasyon.mean()


# In[12]:


#örneklem dağılımı


# In[13]:


np.random.seed(10)
orneklem1 = np.random.choice(a = populasyon, size=100)
orneklem2 = np.random.choice(a = populasyon, size=100)
orneklem3 = np.random.choice(a = populasyon, size=100)
orneklem4 = np.random.choice(a = populasyon, size=100)
orneklem5 = np.random.choice(a = populasyon, size=100)
orneklem6 = np.random.choice(a = populasyon, size=100)
orneklem7 = np.random.choice(a = populasyon, size=100)
orneklem8 = np.random.choice(a = populasyon, size=100)
orneklem9 = np.random.choice(a = populasyon, size=100)
orneklem10 = np.random.choice(a = populasyon, size=100)


# In[14]:


(orneklem1.mean() + orneklem2.mean() + orneklem3.mean() +orneklem4.mean()
+orneklem5.mean()+orneklem6.mean() + orneklem7.mean() + orneklem8.mean() +
 orneklem9.mean() + orneklem10.mean())/10


# ### Betimsel İstatistikler

# In[15]:


import seaborn as sns
tips= sns.load_dataset("tips")
df = tips.copy()
df.head()


# In[16]:


df.describe().T


# In[18]:


get_ipython().system('pip install researchpy')


# In[19]:


import researchpy as rp


# In[20]:


rp.summary_cont(df[["total_bill","tip","size"]])


# In[22]:


rp.summary_cat(df[["sex","smoker","day"]])


# In[23]:


df[["tip","total_bill"]].cov()


# In[24]:


df[["tip","total_bill"]].corr()


# ### İş Uygulaması: Fiyat Stratejisi Karar Destek

# In[36]:


import numpy as np
fiyatlar = np.random.randint(10,110,1000)
fiyatlar.mean()


# In[37]:


import statsmodels.stats.api as sms


# In[38]:


sms.DescrStatsW(fiyatlar).tconfint_mean()


# ## Olasılık Dağılımları

# ### Bernoulli Dağılımı

# In[39]:


from scipy.stats import bernoulli


# In[40]:


p= 0.6


# In[43]:


rv = bernoulli(p)
rv.pmf(k=1) #probability mass functions
#şu an k'nin true olması olayı ile ilgileniyoruz


# In[45]:


rv.pmf(k=0) #şu an ise k'nin false olması olayı ile ilgileniyoruz


# ## Büyük Sayılar Yasası

# In[48]:


import numpy as np
rng = np.random.RandomState(123)
for i in np.arange(1,21):
    deney_sayisi=2**i
    yazi_turalar= rng.randint(0,2, size=deney_sayisi)
    yazi_olasiliklari = np.mean(yazi_turalar)
    print("Atis sayisi: ", deney_sayisi,"---- Yazi Olasiligi: %.2f" % (yazi_olasiliklari*100))


# ## Binom Dağılımı

# In[49]:


from scipy.stats import binom


# In[52]:


p=0.01
n=100
rv = binom(n,p)
print(rv.pmf(1))
print(rv.pmf(5))
print(rv.pmf(10))


# ## Poison Dağılımı

# In[1]:


from scipy.stats import poisson


# In[2]:


lambda_=0.1


# In[4]:


rv = poisson(mu=lambda_)
print(rv.pmf(k=0))


# In[5]:


print(rv.pmf(k=3))


# In[6]:


print(rv.pmf(k=5))


# ## Normal Dağılım

# In[7]:


from scipy.stats import norm


# In[8]:


#90'dan fazla olması
1-norm.cdf(90,80,5) #cdf= cumulative density function
#norm.cdf(hesaplanmak istenen değer, ortalama, standart sapma)


# In[9]:


#70'den fazla olması
1-norm.cdf(70,80,5)


# In[11]:


#73'den fazla olması
norm.cdf(73,80,5)


# In[12]:


#85 ile 90 arasında olması
norm.cdf(90,80,5) - norm.cdf(85,80,5)


# In[ ]:





# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as mat
import seaborn as sea
import streamlit as lit

"""Pada Colab akan digunakan 4 libraries, yaitu:
* Numpy sebagai Data Assessing dan Cleaning
* Pandas sebagai Data Accessing dan Gathering
* Matplotlib.pyplot dan Seaborn untuk visualisasi data

Selanjutnya pada Python akan ada 1 tambahan Library yaitu Streamlit untuk pembuatan Dashboard.

## Data Wrangling

### Gathering Data

Dibawah adalah langkah langkah meng-import data dari github ke Google Colab dan nantinya Python
"""

#Meng-Upload data yang sudah didapatkan, yaitu data penggunaan sepeda perjam dari tanggal 1 Januari 2011 sampai 31 Desember 2012
bikehour = pd.read_csv("https://raw.githubusercontent.com/Denino04/Bangkit_Hub/main/hour.csv")

#Menunjukkan 5 line teratas dari data yang dimiliki
print(bikehour.head())

"""### Assessing Data"""

#Mengecek apakah ada data kosong / data hilang pada dataset
print(bikehour.isnull().sum())

#Mengecek apakah ada data yang terduplikasi pada dateset
print(bikehour.duplicated().sum())

"""mengecek apakah ada outliers pada data data yang ada dalam dataset"""

temp25, temp75 = np.percentile(bikehour.temp, 25), np.percentile(bikehour.temp, 75)
tempiqr = temp75 - temp25
tempcut_off = tempiqr * 1.5
minimum, maximum = temp25 - tempcut_off, temp75 + tempcut_off

temp_outliers = [x for x in bikehour.temp if x < minimum or x > maximum]
if(temp_outliers == []):
  print("No Outliers")
else:
  print(temp_outliers)

atemp25, atemp75 = np.percentile(bikehour.atemp, 25), np.percentile(bikehour.atemp, 75)
atempiqr = atemp75 - atemp25
atempcut_off = atempiqr * 1.5
minimum, maximum = atemp25 - atempcut_off, atemp75 + atempcut_off

atemp_outliers = [x for x in bikehour.atemp if x < minimum or x > maximum]
if(atemp_outliers == []):
  print("No Outliers")
else:
  print(atemp_outliers)

"""### Dari yang bisa disimpulkan diatas, data yang dimiliki telah bersih dengan tidak adanya data yang hilang, terduplikasi, ataupun Outlier data.

# Cleaning Data

## Karena pada sesi Assessing Data tidak ditemukan Missing value, Duplicated value, ataupun Outliers, maka tidak diperlukan adanya Cleaning data lebih lanjut.
"""

bikehour2 = bikehour.drop(['dteday'], axis=1)

"""## Exploratory Data Analysis (EDA)

### Explore ...

DIbawah adalah deskripsi numerik lengkap tentang semua variabel pada data kecuali Dteday yang adalah time-series
"""

print(bikehour.describe())

"""Dibawah melihat korelasi jumlah total sepeda dengan variabel lainnya"""

print(bikehour2.corr()['cnt'])

"""### Selanjutnya adalah korelasi spesifik tiap tiap variabel dengan jumlah total sepeda.

Korelasi pertama adalah temperature dan A-temp, dimana keduanya memiliki korelasi yang relatif sejajar dengan jumlah total sepeda
"""

#korelasi temp, atemp, dan cnt
biketemp = bikehour[['temp', 'atemp', 'cnt']]
print(biketemp.corr()["cnt"])

"""Korelasi kedua adalah dengan situasi udara, dimana keduanya sedikit berkebalikan dengan nilai korelasi negatif"""

#korelasi weathersit dan cnt
bikeweather = bikehour[['weathersit', 'cnt']]
print(bikeweather.corr()['cnt'])

"""Sama seperti Temperature, korelasi dengan Jam pada hari relatif sejajar"""

#korelasi hr dan cnt
biketime = bikehour[['hr', 'cnt']]
print(biketime.corr()['cnt'])

"""Disini bisa dilihat bahwa korelasi jumlah total sepeda relatif terbalik dengan humiditas udara, namun hampir tidak ada korelasi dengan kekuatan angin, atau memiliki korelasi yang ekstrim pada 2 ujung."""

#korelasi hum, windspeed, dan cnt
bikewind = bikehour[['hum', 'windspeed', 'cnt']]
print(bikewind.corr()["cnt"])

"""## Visualization & Explanatory Analysis

### Visualisasi plot untuk variabel variabel yang akan digunakan, yaitu:
*   hr
*   temp
*   atemp
*   weathersit
*   hum
*   windspeed
*   cnt
"""

#Visualisasi temperatur dan A-temperatur terhadap waktu pada 2 tahun
fig = mat.figure(figsize=(12,5))
ax = fig.add_subplot(1,1,1)

ax.plot(bikehour['dteday'], bikehour['temp'], color='blue')
ax.plot(bikehour['dteday'], bikehour['atemp'], color='green')
ax.set_xlabel('dates',size=15)
ax.set_ylabel('Temperatures',size=15)
mat.show()

"""Bisa dilihat dari grafik diatas, temperatur dan A-Temperatur naik dan turun tergantung dengan tanggal pada tahun, dimana Januari tahun 2011, Desember 2011, Januari 2012, dan Desember 2012 menjadi titik rendah temperatur.

Disini, temperatur berskala dari 0 (0 C) sampai 1.0 (41 C) dan A-Temperatur 0 (0 C) sampai 1.0 (50 C)
"""

#Visualisasi situasi cuaca (Weathersit) terhadap waktu pada 2 tahun
fig = mat.figure(figsize=(12,5))
ax = fig.add_subplot(1,1,1)

ax.plot(bikehour['dteday'], bikehour['weathersit'], color='green')
ax.set_xlabel('dates',size=15)
ax.set_ylabel('weather Situations',size=15)
mat.show()

"""Bisa dilihat pada grafik, dominasi situasi cuaca berada pada nomor 2 yaitu berawan. Diikuti dengan situasi 3 yaitu gerimis dan/atau salju ringan. Setelah itu adalah nomor 1, yaitu cerah, dan diakhiri dengan nomor 4 yaitu hujan deras dan badai salju."""

#Visualisasi temperatur dan A-temperatur terhadap waktu pada 2 tahun
fig = mat.figure(figsize=(12,5))
ax = fig.add_subplot(1,1,1)

ax.plot(bikehour['dteday'], bikehour['hum'], color='blue')
ax.plot(bikehour['dteday'], bikehour['windspeed'], color='green')
ax.set_xlabel('dates',size=15)
ax.set_ylabel('Air Quality',size=15)
mat.show()

"""Diatas adalah grafik kualitas air yang mencangkup humiditas dan kencang angin dimana humiditas relatif sedang sampai tinggi sepanjang 2 tahun, dan kecepatan angin relatif sedang ke rendang sepanjang 2 tahun."""

#Visualisasi temperatur dan A-temperatur terhadap waktu pada 2 tahun
fig = mat.figure(figsize=(12,5))
ax = fig.add_subplot(1,1,1)

ax.plot(bikehour['dteday'], bikehour['cnt'], color='green')
ax.set_xlabel('dates',size=15)
ax.set_ylabel('Bike Counts',size=15)
mat.show()
"""Grafik diatas menunjukkan bahwa penggunaan sepeda meningkat ditengah tahun dan menurun di awal dan akhir tahun, dan juga adanya peningkatan penggunaan sepeda pada tahun 2012 dibanding tahun 2011.

### Pertanyaan 1: Apakah Temperatur (temp) dan "Feels Like" Temperatur (atemp) berpengaruh pada jumlah total penggunaan sepeda (cnt)?
"""

#Korelasi Temp dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['temp'])
mat.xlabel('Bike Counts',size=15)
mat.ylabel('Temperature',size=15)
mat.show()

#Korelasi A-Temp dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['atemp'], color='red')
mat.xlabel('Bike Counts',size=15)
mat.ylabel('A-Temperature',size=15)
mat.show()

"""Diatas adalah grafik scatterplot yang menunjukkan bahwa penggunaan sepeda memuncak dimana suhu sekitar dan suhu udara relatif tinggi walaupun tidak sangat tinggi. 0.7 untuk temperatur dan 0.6 untuk A-Temperatur.

### Pertanyaan 2: Apakah waktu jam dalam sebuah hari (hr) berpengaruh pada jumlah total penggunaan sepeda (cnt)?
"""

#Korelasi Weathersit dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['weathersit'], color='red')
mat.xlabel('Bike Counts',size=15)
mat.ylabel('Weather',size=15)
mat.show()

"""Pada grafik korelasi diatas dapat dilihat dengan jelas bahwa penggunaan sepeda relatif setara pada cuaca terang, berawan, dan gerimis kecil dengan sedikit perbedaan. Dan juga bisa dilihat bahwa hampir tidak ada penggunaan sepeda pada cuaca hujan deras dan/atau badai salju.

### Pertanyaan 3: Apakah waktu jam dalam sebuah hari (hr) berpengaruh pada jumlah total penggunaan sepeda (cnt)?
"""

#Korelasi hr dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['hr'], color='green')
mat.xlabel('Bike Counts',size=15)
mat.ylabel('Hour of the Day',size=15)
mat.show()

"""Diatas adalah korelasi jam pada sebuah hari dengan penggunaan sepeda, dimana penggunaan memuncak pada sekitar dan 9 dan sekitar jam 18 - 19.

###Pertanyaan 4: Apakah kelembapan (hum) dan kecepatan angin (windspeed) berpengaruh pada jumlah total penggunaan sepeda (cnt)?
"""

#Korelasi hum dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['hum'], color='Pink')
mat.xlabel('Bike Counts',size=15)
mat.ylabel('Humidity',size=15)
mat.show()
#Korelasi windspeed dan cnt
mat.figure(figsize=(12, 5))
sea.regplot(x=bikehour['cnt'], y=bikehour['windspeed'], color='cyan')
mat.xlabel('Bike Counts',size=15)
mat.ylabel('Wind Speed',size=15)
mat.show()

"""Bisa dilihat dari grafik diatas bahwa penggunaan sepeda memuncak saat humiditas udara relatif sedang kebawah. Sama dengan humiditas, penggunaan sepeda naik saat kecepatan udara menurun.

## Conclusion

- Conclusion 1: Bisa disimpulkan bahwa orang orang akan menggunakan sepeda mereka ataupun rental pada saat temperatur yang ada pada lingkungan sekitar relatif hangat, mungkin karena suhu hangat mendorong keinginan berolahraga.

- Conclution 2: Bisa disimpulkan bahwa penduduk akan menggunakan sepeda saat suhu nyaman dan tenang, dari cuaca terang, berawan, dan juga gerimis kecil. Walaupun ada beberapa yang nekat menggunakan sepeda pada hujan deras ataupun badai salju.

- Conclusion 3: Waktu yang cocok untuk bersepeda terlihat adalah pagi sekitar jam 9, mungkin dengan banyaknya yang berangkat kerja. Penggunaan sepeda juga naik pada jamm 18 dan 19, menandakan bahwa awal malam hari mungkinlah waktu yang tepat untuk bersepeda tenang.

- Conclusion 4: Dari kedua grafik bisa disimpulkan bahwa orang orang suka bersepeda saat kualitas udara tenang, dengan humiditas rendah agar tidak terlalu berkeringat dan juga kekuatan angin yang lemah.
"""
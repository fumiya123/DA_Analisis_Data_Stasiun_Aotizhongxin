import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
from datetime import datetime
from datetime import timedelta

all_df = pd.read_csv('https://raw.githubusercontent.com/fumiya123/DA_Analisis_Data_Stasiun_Aotizhongxin/main/dashboard/main_data.csv')
day_df = pd.read_csv('https://raw.githubusercontent.com/fumiya123/DA_Analisis_Data_Stasiun_Aotizhongxin/main/dashboard/data_day.csv')
st.header('Dashboard Index Kualitas Udara Stasiun Aotizhongxin')

#st.write(all_df)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://i.imgur.com/wkufRHT.png")

    # Mengambil start_date & end_date dari date_input
    tgl_input = st.date_input(
        label='Tanggal',
        value="today")

    tgl_before = tgl_input + timedelta(days=-7)
    tgl_now = pd.to_datetime(tgl_input)
    tgl_se = tgl_now + timedelta(hours=23)
    tgl_after = tgl_input + timedelta(days=7)

# filter data before 7 hari
before_df = day_df[(day_df["Datetime"] >= str(tgl_before)) &
                (day_df["Datetime"] < str(tgl_input))]

# filter data hari ini
today_df = all_df[(all_df["Datetime"] >= str(tgl_now)) &
                (all_df["Datetime"] <= str(tgl_se))]

# filter data after 7 hari
after_df = day_df[(day_df["Datetime"] > str(tgl_input)) &
                (day_df["Datetime"] <= str(tgl_after))]

# Corelasi metrik kadar PM2.5, PM10, SO2, NO2, CO dan O3
correlation_matrix = today_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr().round(2)

# untuk mengatur ukuran
fig, ax = plt.subplots(figsize=(6, 6))

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True, cmap untuk mengatur warna dari biru=dingin dan merah=panas,
# linewidths untuk memberikan spasi antar baris dan kolom
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk PM2.5, PM10, SO2, NO2, CO dan O3", size=13)
st.pyplot(fig)

# plot regresi 1
col1, col2 = st.columns(2)
fig, ax = plt.subplots(figsize=(16, 8))
with col1:
  option1 = st.selectbox("Option X", ("PM2.5", "PM10", "SO2", "NO2", "CO", "O3"), placeholder="Choose an option", key="option1")
with col2:
  option2 = st.selectbox("Option Y", ("PM2.5", "PM10", "SO2", "NO2", "CO", "O3"), placeholder="Choose an option", key="option2")
sns.regplot(x=option1, y=option2, data=today_df)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.set_xlabel(option1, fontsize=20)
ax.set_ylabel(option2, fontsize=20)
st.pyplot(fig)

# Corelasi metrik Temperatur dan Suhu Titik Embun
correlation_matrix = today_df[['TEMP', 'DEWP']].corr().round(2)

# untuk mengatur ukuran
fig, ax = plt.subplots(figsize=(5, 5))

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True, cmap untuk mengatur warna dari biru=dingin dan merah=panas,
# linewidths untuk memberikan spasi antar baris dan kolom
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Temperatur dan Suhu Titik Embun", size=10)
st.pyplot(fig)

# Today Plot
st.subheader("Indeks Kualitas Udara Hari ini")

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
  today_df['hour'], today_df['Skor'], color='red'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.set_ylabel('Skor', fontsize=20)
ax.set_xlabel('Jam', fontsize=20)
st.pyplot(fig)

# Before Plot
st.subheader("Indeks Kualitas Udara 7 Hari yang lalu")

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
  before_df['Datetime'], before_df['Skor'], color='red'
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.set_xticks(np.arange(len(before_df['Datetime'])), rotation=45, labels=before_df['Datetime'])
ax.set_ylabel('Skor', fontsize=20)
ax.set_xlabel('Tanggal', fontsize=20)
st.pyplot(fig)

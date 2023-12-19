# Dashboard AQI Stasiun Aotizhongxin

## Run in Local
### Setup environment
```
conda create --name da-analisis-data-stasiun-aotizhongxin python=3.9
conda activate da-analisis-data-stasiun-aotizhongxin
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel protobuf
```

### Run steamlit app
```
streamlit run app.py
```

## Run in Colab
1. Buka file Analisis Data Udara Stasiun Aotizhongxin.ipynb di google colab
2. Scrol ke bawah file .ipynb ke cell kode `!streamlit run app.py & npx localtunnel --port 8501`
3. Jika output dari program sudah keluar akan muncul link di sebelah your url is klik link tersebut
   ![image](https://github.com/fumiya123/DA_Analisis_Data_Stasiun_Aotizhongxin/assets/98727343/d028f2f0-ccd7-4658-9ae7-907a2f5b3dfd)
4. Anda akan diarahkan ke tab baru

   ![image](https://github.com/fumiya123/DA_Analisis_Data_Stasiun_Aotizhongxin/assets/98727343/370103b9-7b62-42f0-8a13-7c31ed26353a)
5. setelah itu inputkan IP External URL

   ![image](https://github.com/fumiya123/DA_Analisis_Data_Stasiun_Aotizhongxin/assets/98727343/778e1a09-07ff-470f-b7da-9ab22260d1d4)
6. Dan terakhir Klik Tombol Click to Submit, Dashboard sudah bisa dijalankan
 

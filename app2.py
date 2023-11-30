import pickle
import streamlit as st
import pandas as pd

st.title("Prediksi Kematian Pasien Penderita Penyakit Gagal Jantung")
st.image("prediksi_jantung.jpg", width=400)

# Membagi visualisasi menjadi 3 kolom di bagian utama
col1, col2, col3 = st.columns(3)

# Membuat sidebar untuk input fitur
with st.sidebar:
    st.title("Input Fitur")
    # Memberikan kunci unik untuk setiap st.number_input
    age = st.number_input('Usia', key='age')
    sex = st.selectbox('Jenis Kelamin (0=Female, 1=Male)', (0, 1), key='sex')
    smoking = st.selectbox('Merokok? (0=No, 1=Yes)', (0, 1), key='smoking')
    anaemia = st.selectbox('Anemia? (0=No, 1=Yes)', (0, 1), key='anaemia')
    diabetes = st.selectbox('Diabetes? (0=No, 1=Yes)', (0, 1), key='diabetes')
    high_blood_pressure = st.selectbox('Tekanan Darah Tinggi? (0=No, 1=Yes)', (0, 1), key='high_blood_pressure')
    creatinine_phosphokinase = st.number_input('CPK enzyme level (mcg/L)', key='creatinine_phosphokinase')
    serum_creatinine = st.number_input('Kadar serum creatinine (mg/dL)', key='serum_creatinine')
    platelets = st.number_input('Platelets (kiloplatelets/mL)', key='platelets')
    ejection_fraction = st.number_input('Persentase fraksi ejeksi jantung', key='ejection_fraction')
    day = st.number_input('Berapa hari follow up?', key='day')
    serum_sodium = st.number_input('Kadar natrium (mEq/L)', key='serum_sodium')

    input_df = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'smoking': [smoking],
        'anaemia': [anaemia],
        'diabetes': [diabetes],
        'high_blood_pressure': [high_blood_pressure],
        'creatinine_phosphokinase': [creatinine_phosphokinase],
        'serum_creatinine': [serum_creatinine],
        'platelets': [platelets],
        'ejection_fraction': [ejection_fraction],
        'day': [day],
        'serum_sodium': [serum_sodium],
    })

# Load dataset dan model
heart_dataset = pd.read_csv('heart_failure_clinical_records_dataset.csv')
heart_dataset = heart_dataset.drop(columns=['DEATH_EVENT'])

# Gabungkan input pengguna dengan dataset
df = pd.concat([input_df, heart_dataset], axis=0)



# Ambil hanya baris pertama pada user input data                                   
df = df[:1]                                   
                                   
st.write(input_df)

model = pickle.load(open('prediksi_jantung.pkl', 'rb'))
predict = ''                             
if st.button("Prediksi Kematian Pasien"):
    predict = model.predict(df)
    if predict.size > 0:
        death_predict = 'Pasien sudah meninggal sebelum waktu follow-up' if predict[0] == 1 else 'Pasien masih bertahan pada waktu follow-up'
        st.success(death_predict)
    else:
        st.warning("Model prediction tidak tersedia.")

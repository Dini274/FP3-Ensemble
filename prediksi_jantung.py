import pickle
import streamlit as st

# Load the pre-trained model
model = pickle.load(open('prediksi_jantung.pkl', 'rb'))

# Set the title and add an image
st.title("Prediksi Kematian Gagal Jantung")
st.image("prediksi_jantung.jpg", width=400)

# Create input widgets in a single column
st.sidebar.title("Input Data Pasien")
age  = st.sidebar.number_input('Berapa usia anda?')
anaemia = st.sidebar.number_input('Apakah menderita anaemia? (0=Tidak, 1=Ya)', (0,1))
creatinine_phosphokinase = st.sidebar.number_input('kadar enzim CPK dalam darah')
diabetes = st.sidebar.number_input('Apakah memiliki riwayat diabetes? (0=Tidak, 1=Ya)',(0,1))
ejection_fraction = st.sidebar.number_input('Persentase fraksi ejeksi jantung')
high_blood_pressure = st.sidebar.number_input('Apakah memiliki tekanan darah tinggi? (0=Tidak, 1=Ya)', min_value=0)
platelets = st.sidebar.number_input('platelets dalam darah (kiloplatelets/mL)')
serum_creatinine = st.sidebar.number_input('kadar kreatinin dalam darah (mg/dL)')
serum_sodium = st.sidebar.number_input('kadar natrium dalam serum darah (mEq/L)')
sex = st.sidebar.number_input('Gender (0=Perempuan, 1=Laki-laki)', (0,1))
smoking = st.sidebar.number_input('Apakah anda merokok? (0=Tidak, 1=Ya)',(0,1))
day = st.sidebar.number_input('Berapa hari follow up?')

# Add a button to trigger the prediction
if st.sidebar.button("Prediksi Kematian"):
    # Perform prediction using the model
    predict = model.predict([[age,anaemia,creatinine_phosphokinase,diabetes,high_blood_pressure,platelets,serum_sodium,sex,smoking,day,ejection_fraction,serum_creatinine]])

    # Display the prediction result in the main column
    st.title("Hasil Prediksi")
    st.write("Prediksi Kematian Gagal Jantung:", predict[0])

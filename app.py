import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Model ve scaler yükle
model = joblib.load('best_model_svm.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🩺 Diyabet Tahmin Uygulaması")
st.markdown("Aşağıdaki bilgileri girerek diyabet riskini tahmin edebilirsiniz.")

# Girişler
age = st.slider("Yaş", 18, 90, 30)
bmi = st.slider("Vücut Kitle İndeksi (BMI)", 10.0, 50.0, 22.0)
smoking = st.selectbox("Sigara Kullanıyor musunuz?", [0, 1])
alcohol = st.selectbox("Alkol Kullanıyor musunuz?", [0, 1])
phys = st.selectbox("Fiziksel Aktivite Yapıyor musunuz?", [0, 1])

# Eğitimde kullanılan tüm sütun isimleri
columns = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
           'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
           'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
           'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']

# Boş bir satırlık DataFrame oluştur
input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

# Kullanıcının girdiği verileri ilgili sütunlara yerleştir
input_data['Age'] = age
input_data['BMI'] = bmi
input_data['Smoker'] = smoking
input_data['PhysActivity'] = phys
input_data['HvyAlcoholConsump'] = alcohol

# Tahmin butonu
if st.button("Tahmin Et"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("🔴 Yüksek diyabet riski tespit edildi!")
    else:
        st.success("🟢 Diyabet riski düşük görünüyor.")

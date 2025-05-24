import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Model ve scaler yükle
model = joblib.load('best_model_svm.pkl')
scaler = joblib.load('scaler.pkl')

st.image("https://tektiklabilgielinde.saglik.gov.tr/depo/sagligimyeni/hastaliklar/diyabet/tip1/resim_5.jpg", width=40)
st.title("🩺 Diyabet Tahmin Uygulaması")
st.markdown("Aşağıdaki bilgileri girerek diyabet riskinizi öğrenebilirsiniz.")

# Kullanıcıdan verileri al
age = st.slider("Yaş", 18, 90, 30)
weight = st.number_input("Kilonuz (kg)", 30.0, 200.0, 70.0)
height_cm = st.number_input("Boyunuz (cm)", 100.0, 220.0, 170.0)
smoking = st.selectbox("Sigara Kullanıyor musunuz?", [0, 1])
alcohol = st.selectbox("Alkol Kullanıyor musunuz?", [0, 1])
phys = st.selectbox("Fiziksel Aktivite Yapıyor musunuz?", [0, 1])

# BMI Hesapla
height_m = height_cm / 100
bmi = round(weight / (height_m ** 2), 2)
st.markdown(f"💡 Hesaplanan Vücut Kitle İndeksiniz (BMI): **{bmi}**")

# Eğitimde kullanılan tüm sütunlar
columns = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
           'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
           'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
           'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']

# Boş DataFrame
input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

# Girdileri yerleştir
input_data['Age'] = age
input_data['BMI'] = bmi
input_data['Smoker'] = smoking
input_data['PhysActivity'] = phys
input_data['HvyAlcoholConsump'] = alcohol

# Tahmin
if st.button("Tahmin Et"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("🔴 Yüksek diyabet riski tespit edildi!")
    else:
        st.success("🟢 Diyabet riski düşük görünüyor.")

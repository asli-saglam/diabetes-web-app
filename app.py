import streamlit as st
import pandas as pd
import joblib

# Model ve scaler yükle
model = joblib.load('best_model_svm.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🩺 Diyabet Tahmin Uygulaması")

st.markdown("Aşağıdaki bilgileri girerek diyabet riskini tahmin edebilirsiniz.")

# Basit özellikler (örnek olarak)
age = st.slider("Yaş", 18, 90, 30)
bmi = st.slider("Vücut Kitle İndeksi (BMI)", 10.0, 50.0, 22.0)
smoking = st.selectbox("Sigara Kullanıyor musunuz?", [0, 1])
alcohol = st.selectbox("Alkol Kullanıyor musunuz?", [0, 1])
phys = st.selectbox("Fiziksel Aktivite Yapıyor musunuz?", [0, 1])

# Veri çerçevesi oluştur
input_data = pd.DataFrame([[age, bmi, smoking, alcohol, phys]],
                          columns=['Age', 'BMI', 'Smoker', 'AlcoholDrinker', 'PhysActivity'])

scaled_input = scaler.transform(input_data)
prediction = model.predict(scaled_input)

if st.button("Tahmin Et"):
    if prediction[0] == 1:
        st.error("🔴 Yüksek diyabet riski tespit edildi!")
    else:
        st.success("🟢 Diyabet riski düşük görünüyor.")

import streamlit as st
import joblib
import sklearn

st.set_page_config(page_title='Laptop | AI', page_icon='favicon.png')

model = joblib.load('models/model.pkl')

companies = ['Dell', 'Lenovo', 'Asus', 'HP', 'Apple', 'Toshiba', 'Acer', 'Other', 'MSI']
typename = ['Notebook',
 'Gaming',
 '2 in 1 Convertible',
 'Ultrabook',
 'Workstation',
 'Netbook']
cpu = ['Intel Core i5', 'Intel Core i7', 'Other', 'AMD']
ram = [2, 4, 6, 8, 12, 16, 24, 32, 64]
gpu = ['Intel', 'Nvidia', 'AMD']
yn = ['yes', 'no']
md = ['HDD', 'SSD', 'Other']
storage = [ 500,  256, 1000,  180,  512,  128,   32, 2000,   16,   64,  240]
os= ['Windows', 'No OS', 'Other', 'Mac OS']

st.title("Laptop Price Predictor")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)

with col1:
    company = st.selectbox("Select The Laptop Company", companies)

with col2:
    typename = st.selectbox("Select The Laptop Type", typename)

with col3:
    Inches = st.number_input("Enter The Laptop Screen Size (Inches)")

with col4:
    cpu_value = st.selectbox("Select The CPU", cpu)

with col5:
    ram_value = st.selectbox("Select The RAM (GB)", ram)

with col6:
    gpu_value = st.selectbox("Select The GPU", gpu)

with col7:
    weight = st.number_input("Enter The Laptop Weight (KG)")

with col8:
    ts = st.selectbox("Touch Screen", yn)

with col9:
    hds = st.selectbox("HD Screen", yn)

with col10:
    mdv =  st.selectbox("Select The Memory Drive", md)

with col11:
    storage_value =  st.selectbox("Select The Storage (GB)", storage)

with col12:
    ops = st.selectbox("Select The OS", os)

if st.button("Predict"):
    data = [[company, typename, Inches, cpu_value, ram_value, gpu_value, weight, ts, hds, mdv, storage_value, ops]]
    prediction = model.predict(data)
    st.header(f"₹ {round(prediction[0], 2)}")




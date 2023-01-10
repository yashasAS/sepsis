import pandas as pd
import streamlit as st
import pickle
data = pickle.load(open('data.pkl','rb'))
st.title('Sepsis classification')
col1, col2 = st.columns([1, 3])

with col1:
    st.image("sepsis.jpg",
                caption="I'll help you identify sepsis",
                 width=300)
with col2:
    HR = st.sidebar.number_input('Insert the HR value',value = data['HR'].mean())
    O2Sat = st.sidebar.number_input('Insert the O2Sat value',value = data['O2Sat'].mean())
    Temp = st.sidebar.number_input('Insert the temp value',value = data['Temp'].mean())
    SBP = st.sidebar.number_input('Insert the SBP value',value = data['SBP'].mean())
    MAP = st.sidebar.number_input('Insert the MAP value',value = data['MAP'].mean())
    DBP = st.sidebar.number_input('Insert the DBP value',value = data['DBP'].mean())
    Resp = st.sidebar.number_input('Insert the Resp value',value = data['Resp'].mean())
    EtCO2 = st.sidebar.number_input('Insert the EtCO2 value',value = data['EtCO2'].mean())
    BaseExcess = st.sidebar.number_input('Insert the BaseExcess value',value = data['BaseExcess'].mean())
    HCO3 = st.sidebar.number_input('Insert the HCO3 value',value = data['HCO3'].mean())
    FiO2 = st.sidebar.number_input('Insert the FiO2 value',value = data['FiO2'].mean())
    pH = st.sidebar.number_input('Insert the pH value',value = data['pH'].mean())
    PaCO2 = st.sidebar.number_input('Insert the PaCO2 value',value = data['PaCO2'].mean())
    SaO2 = st.sidebar.number_input('Insert the SaO2 value',value = data['SaO2'].mean())
    AST = st.sidebar.number_input('Insert the AST value',value = data['AST'].mean())
    BUN = st.sidebar.number_input('Insert the BUN value',value = data['BUN'].mean())
    Alkalinephos = st.sidebar.number_input('Insert the Alkalinephos value',value = data['Alkalinephos'].mean())
    Calcium = st.sidebar.number_input('Insert the Calcium value',value = data['Calcium'].mean())
    Chloride = st.sidebar.number_input('Insert the Chloride value',value = data['Chloride'].mean())
    Creatinine = st.sidebar.number_input('Insert the Creatinine value',value = data['Creatinine'].mean())
    Bilirubin_direct = st.sidebar.number_input('Insert the Bilirubin_direct value',value = data['Bilirubin_direct'].mean())
    Glucose = st.sidebar.number_input('Insert the Glucose value',value = data['Glucose'].mean())
    Lactate = st.sidebar.number_input('Insert the Lactate value',value = data['Lactate'].mean())
    Magnesium = st.sidebar.number_input('Insert the Magnesium value',value = data['Magnesium'].mean())
    Phosphate = st.sidebar.number_input('Insert the Phosphate value',value = data['Phosphate'].mean())
    Potassium = st.sidebar.number_input('Insert the Potassium value',value = data['Potassium'].mean())
    Bilirubin_total = st.sidebar.number_input('Insert the Bilirubin_total value',value = data['Bilirubin_total'].mean())
    TroponinI = st.sidebar.number_input('Insert the TroponinI value',value = data['TroponinI'].mean())
    Hct = st.sidebar.number_input('Insert the Hct value',value = data['Hct'].mean())
    Hgb = st.sidebar.number_input('Insert the Hgb value',value = data['Hgb'].mean())
    PTT = st.sidebar.number_input('Insert the PTT value',value = data['PTT'].mean())
    WBC = st.sidebar.number_input('Insert the WBC value',value = data['WBC'].mean())
    Fibrinogen = st.sidebar.number_input('Insert the Fibrinogen value',value = data['Fibrinogen'].mean())
    Platelets = st.sidebar.number_input('Insert the Platelets value',value = data['Platelets'].mean())
    Age = st.sidebar.number_input('Age',value = data['Age'].mean())
    Gender = st.sidebar.selectbox('Insert the Gender', ('0', '1'))
    Unit1 =  data['Unit1'].mean()
    Unit2 = data['Unit2'].mean()
    HospAdmTime = data['HospAdmTime'].mean()
    ICULOS = st.sidebar.number_input('Insert the ICULOS value',value = data['ICULOS'].mean())
    time = data['time'].mean()




features = pd.DataFrame({
"HR" : [HR],
"O2Sat" : [O2Sat],
"Temp": [Temp],
"SBP":[SBP],
"MAP": [MAP],
"DBP": [DBP],
"Resp": [Resp],
"EtCO2": [EtCO2],
"BaseExcess": [BaseExcess],
"HCO3": [HCO3],
"FiO2": [FiO2],
"pH": [pH],
"PaCO2": [PaCO2],
"SaO2": [SaO2],
"AST": [AST],
"BUN": [BUN],
"Alkalinephos": [Alkalinephos],
"Calcium": [Calcium],
"Chloride": [Chloride],
"Creatinine": [Creatinine],
"Bilirubin_direct": [Bilirubin_direct],
"Glucose": [Glucose],
"Lactate": [Lactate],
"Magnesium": [Magnesium],
"Phosphate": [Phosphate],
"Potassium": [Potassium],
"Bilirubin_total": [Bilirubin_total],
"TroponinI":[TroponinI],
"Hct": [Hct],
"Hgb": [Hgb],
"PTT": [PTT],
"WBC": [WBC],
"Fibrinogen": [Fibrinogen],
"Platelets": [Platelets],
"Age": [Age],
"Gender": [Gender],
"Unit1": [Unit1],
"Unit2": [Unit2],
"HospAdmTime": [HospAdmTime],
"ICULOS": [ICULOS],
"time": [time]

})
st.dataframe(features)
model = pickle.load(open('model.pkl','rb'))
y_pred = st.button('Get report')
y_pred = model.predict(features)
#st.write(y_pred)
if (y_pred)==0:
    st.title('Sepsis not identified')
else:
    st.title('Sepsis identified')

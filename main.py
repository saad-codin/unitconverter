import streamlit as st 

conversions = { 
    "Metre" : 1 , 
    "Kilometre" : 0.001, 
    "Centimetre" : 100, 
     "Mile" : 0.000621371,
     "Millimetre": 1000,
     "Yard" : 1.09361, 
     "Foot" : 3.28084, 
     "Inch" : 39.3701
}

st.title ("🔢 Unit Converter") 

st.subheader ("Length Conversion ") 

value = st.number_input ("Enter value", min_value = 0.0 , value = 1.0)

input_unit = st.selectbox ("From", list(conversions.keys())) 

output_unit = st.selectbox ("To", list(conversions.keys())) 

if st.button("Convert"): 
    result = value * (conversions[output_unit] / conversions[input_unit]) 
    st.success(f"{value} {input_unit} = {result:.4f} {output_unit}")


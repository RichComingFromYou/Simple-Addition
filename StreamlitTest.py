import streamlit as st
import pandas as pd
import numpy as np

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """
# st.subheader("1-Magic:")
# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

st.subheader ("Input Number Plus 10")
num = st.number_input ("Input Number: ")
num += 10
st.write ("Result")
st.write (num)

st.subheader("Input Text")
Text = st.text_input ("Input Text :")
st.write ("Result :",Text)

st.video(youtu.be/BBJa32lCaaY, format='video/mp4', start_time=0)
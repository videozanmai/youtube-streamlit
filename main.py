import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit超入門を更新')
st.write('プログレスバーの表示')
'start!!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0)
    

left_colmn,right_colmn = st.columns(2)
leftButton = left_colmn.button('左ボタン：右に文字を表示する')
if leftButton:
    right_colmn.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')

# option = st.sidebar.selectbox(
#     'あなたが好きな数字をいれてください。',
#     list(range(1,11))
# )
# st.sidebar.write('あなたが好きな数字は、',option,'ですね。')

# t = st.text_input('あなたの趣味を教えて下さい。')
# 'へ～',t,'なんですね。'

# condition = st.slider('あなたの調子は。',0,100,50)
# 'あなたの調子は',condition

if st.checkbox('Show Image'):
    img = Image.open('image.jpg')
    st.image(img, caption='写真', use_column_width=True)


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)


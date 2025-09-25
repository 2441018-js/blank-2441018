
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 실제 폰트 경로 및 이름으로 수정
font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fonst/NanumGothic-Regular.ttf'))
if os.path.exists(font_path):
    fontprop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = fontprop.get_name()
    plt.rcParams['axes.unicode_minus'] = False
else:
    st.warning(f'폰트 파일을 찾을 수 없습니다: {font_path}')

# Streamlit 스타일(한글 폰트 적용)
st.markdown('<style>div[data-testid="stMarkdownContainer"]{ font-family: NanumGothic, sans-serif; }</style>', unsafe_allow_html=True)

st.title('간단한 데이터 시각화')

# 예시 데이터 생성
data = {
	'월': ['1월', '2월', '3월', '4월', '5월'],
	'매출': np.random.randint(100, 500, 5),
	'고객수': np.random.randint(10, 100, 5)
}
df = pd.DataFrame(data)

st.subheader('데이터 미리보기')
st.dataframe(df)

st.subheader('매출 추이 (Line Chart)')
st.line_chart(df.set_index('월')['매출'])

st.subheader('고객수 (Bar Chart)')
st.bar_chart(df.set_index('월')['고객수'])

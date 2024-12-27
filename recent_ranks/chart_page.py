import streamlit as st
import pandas as pd
import numpy as np
main_hitter = pd.DataFrame({
    '이름':['강백호','로하스','문상철'],
    '월':['3월','4월','5월','6월','7월','8월','9월'],
    '강백호 안타':[]
})
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["강백호", "로하스", "문상철"])

st.line_chart(chart_data)




st.title('로하스 타격 지표')

data = pd.DataFrame({
    '월': ['3월','4월','5월','6월','7월','8월','9월'],
    '타석 수': [50, 90, 88, 97, 105,95, 76],
    '타율': [0.4, 0.3, 0.31, 0.33, 0.54, 0.41,0.35],
    '홈런':[3, 4, 8, 5, 6, 2, 6]
})

st.dataframe(data, use_container_width=True)

st.bar_chart(data.set_index('월')['홈런'])
st.line_chart(data.set_index('월')['타율'])
fig = data.plot.pie(
    y='홈런',
    labels=data['월'],
    autopct= '%1.1f%%',
    figsize=(8,8),
    legend = False,
    title = '로하스 타격지표표'
).get_figure()
st.pyplot(fig)

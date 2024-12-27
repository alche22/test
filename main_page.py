import streamlit as st

st.title('야구 개막 언제해')
st.header('KBO 개막')
st.subheader('2025년 3월 22일!')

st.text('우리팀의 개막전 상대는?')

options = ['기아타이거즈', '삼성라이온즈', '엘지트윈스','두산베어스','케이티위즈','SSG랜더스','롯데자이언츠','한화이글스', '엔씨다이노스', '키움히어로즈']
selected = st.selectbox('우리팀', options)

if selected == '기아타이거즈':
    st.write('엔씨다이노스')

if selected == '삼성라이온즈':
    st.write('키움히어로즈')

if selected == '엘지트윈스':
    st.write('롯데자이언츠')

if selected == '케이티위즈':
    st.write('한화이글스')

if selected == 'SSG랜더스':
    st.write('두산베어스')

if selected == '두산베어스':
    st.write('SSG랜더스')

if selected == '한화이글스':
    st.write('케이티위즈')

if selected == '롯데자이언츠':
    st.write('엘지트윈스')

if selected == '키움히어로즈':
    st.write('삼성라이온즈')

if selected == '엔씨다이노스':
    st.write('기아타이거즈')


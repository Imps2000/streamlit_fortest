import streamlit as st


# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")

st.button("Reset", type="primary")
if st.button("안녕! 여기를 눌러봐"):
    st.write("왜 눌러")
else:
    st.write("절대 누르지마")

if st.button("누르면", type="tertiary"):
    st.write("큰일난다")
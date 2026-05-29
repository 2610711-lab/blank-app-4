import streamlit as st

# 앱 제목 설정
st.title("🔢 신나는 구구단 앱")
st.subheader("파이썬으로 만든 구구단 출력 프로그램입니다.")

# 사이드바에서 모드 선택하기
mode = st.sidebar.selectbox("출력 모드 선택", ["특정 단만 보기", "2단부터 9단까지 전부 보기"])

if mode == "특정 단만 보기":
    # 사용자가 원하는 단을 슬라이더로 선택 (2단 ~ 9단)
    dan = st.slider("확인할 단을 선택하세요", min_value=2, max_value=9, value=2)
    
    st.write(### f"### 🎯 구구단 {dan}단")
    
    # 선택한 단 출력
    for j in range(1, 10):
        st.text(f"{dan} × {j} = {dan * j}")

elif mode == "2단부터 9단까지 전부 보기":
    st.write("### 📚 구구단 2단 ~ 9단")
    
    # 스트림릿에서 레이아웃을 깔끔하게 나누기 위해 컬럼 생성
    # 2단부터 9단까지 총 8개의 칸을 만듭니다.
    cols = st.columns(4)  # 한 줄에 4개씩 배치
    
    for i in range(2, 10):
        # i가 2~5일 때는 첫 번째 줄, 6~9일 때는 두 번째 줄에 배치되도록 인덱스 계산
        col_idx = (i - 2) % 4
        
        with cols[col_idx]:
            st.markdown(f"**[{i}단]**")
            for j in range(1, 10):
                st.text(f"{i} × {j} = {i * j}")
            st.write("") # 단 사이에 약간의 공백 추가

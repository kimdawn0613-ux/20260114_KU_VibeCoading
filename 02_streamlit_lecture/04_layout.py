"""
4단계: 레이아웃과 컨테이너
학습 목표: 페이지 구조를 체계적으로 구성하기
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="레이아웃 배우기",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

st.title("🎨 레이아웃 구성하기")

# ============================================
# 1. 사이드바
# ============================================
st.sidebar.title("⚙️ 설정 패널")
st.sidebar.write("사이드바는 설정이나 필터를 배치하기 좋습니다.")

sidebar_option = st.sidebar.selectbox(
    "옵션 선택:",
    ["옵션 1", "옵션 2", "옵션 3"]
)

sidebar_slider = st.sidebar.slider(
    "값 조정:",
    0, 100, 50
)

st.sidebar.divider()
st.sidebar.info(f"""
**현재 설정**
- 선택: {sidebar_option}
- 값: {sidebar_slider}
""")

# ============================================
# 2. 컬럼 레이아웃
# ============================================
st.header("1. 컬럼 레이아웃")

st.subheader("2개 컬럼 (1:1 비율)")
col1, col2 = st.columns(2)

with col1:
    st.write("**왼쪽 컬럼**")
    st.button("버튼 1", use_container_width=True, key="left_btn1")
    st.button("버튼 1", use_container_width=True, key="left_btn2")

with col2:
    st.write("**오른쪽 컬럼**")
    st.button("버튼 2", use_container_width=True, key="right_btn1")
    st.button("버튼 2", use_container_width=True, key="right_btn2")


# 구분선
st.divider()

st.subheader("3개 컬럼 (1:2:1 비율)")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.metric("사용자", "1,234", "+12%")

with col2:
    st.write("중앙 컬럼은 넓게!")
    st.progress(0.7)

with col3:
    st.metric("매출", "₩5M", "+8%")

# ============================================
# 3. 탭
# ============================================
st.divider()
st.header("2. 탭 레이아웃")

tab1, tab2, tab3  = st.tabs(["⚙️ 설정", "ℹ️ 정보", "new!"])

with tab1:
    st.subheader("설정 탭")
    
    theme = st.selectbox("테마:", ["라이트", "다크"])
    language = st.selectbox("언어:", ["한국어", "English"])
    
    if st.button("설정 저장"):
        st.success("설정이 저장되었습니다!")

with tab2:
    st.subheader("정보 탭")
    st.info("""
    **버전**: 1.0.0  
    **개발자**: Streamlit Team  
    **라이선스**: MIT
    """)


# ============================================
# 4. 확장 가능한 섹션 (Expander)
# ============================================
st.divider()
st.header("3. 확장 섹션 (Expander)")

with st.expander("📖 더 자세히 보기"):
    st.write("""
    여기는 기본적으로 숨겨져 있는 내용입니다.
    클릭하면 펼쳐집니다!
    """)
    st.code("""
    def hello():
        return "Hello, World!"
    """, language="python")

with st.expander("📊 통계 데이터", expanded=True):
    st.write("expanded=True로 설정하면 기본으로 펼쳐져 있습니다.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("방문자", "1,234")
    col2.metric("페이지뷰", "5,678")
    col3.metric("전환율", "3.2%")

# ============================================
# 5. Empty (동적 업데이트)
# ============================================
st.divider()
st.header("5. Empty (동적 업데이트)")

import time

placeholder = st.empty()

if st.button("카운트다운 시작"):
    for i in range(5, 0, -1):
        placeholder.write(f"⏰ {i}초 남았습니다...")
        time.sleep(1) # 1초 기다리기
    placeholder.success("✅ 완료!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제 1: 제품 상세 페이지 만들기

다음 레이아웃으로 제품 상세 페이지를 만드세요:

**구조:**
1. 사이드바: 카테고리 선택, 가격 범위 필터
2. 메인 영역:
   - 2개 컬럼 (1:1): 왼쪽에 이미지, 오른쪽에 상품 정보
   - 탭: 상세설명, 리뷰, 배송정보
   - Expander: FAQ
""")

# 실습

import streamlit as st

st.subheader("제품 상세 페이지")

col1, col2 = st.columns(2)

with col1:
    # 실제 이미지 위치에 맞게 경로 수정
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ96jQ9W4bT93OXaPYPMiX3hSW3ioFRp-2mCA&s", use_container_width=True)

with col2:
    st.subheader("무선 헤드폰 Pro")
    st.write("**₩299,000**")
    st.write("⭐⭐⭐⭐⭐ (4.8) - 리뷰 324개")

    # 여기에는 자유롭게 리뷰 내용 작성
    st.markdown("---")
    st.write("고급 노이즈 캔슬링 기능이 탑재된 프리미엄 무선 헤드폰")


# 예시 답안
with st.expander("💡 과제 1 예시 답안"):
    st.subheader("제품 상세 페이지")
    
    # 2컬럼 레이아웃
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ96jQ9W4bT93OXaPYPMiX3hSW3ioFRp-2mCA&s", use_container_width=True)
    
    with col2:
        st.write("### 🎧 무선 헤드폰 Pro")
        st.write("**₩299,000**")
        st.write("⭐⭐⭐⭐⭐ (4.8) - 리뷰 324개")
        st.write("---")
        st.write("고급 노이즈 캔슬링 기능이 탑재된 프리미엄 무선 헤드폰")
        
        quantity = st.number_input("수량:", min_value=1, value=1)
        col_a, col_b = st.columns(2)
        col_a.button("🛒 장바구니", use_container_width=True)
        col_b.button("💳 바로 구매", type="primary", use_container_width=True)
    
    # 탭
    tab1, tab2, tab3 = st.tabs(["📋 상세설명", "⭐ 리뷰", "🚚 배송정보"])
    
    with tab1:
        st.write("**주요 특징**")
        st.write("- 최대 30시간 재생")
        st.write("- 고급 노이즈 캔슬링")
        st.write("- 블루투스 5.0")
    
    with tab2:
        st.write("평균 평점: ⭐ 4.8/5.0")
        st.write("---")
        st.write("**김철수**: ⭐⭐⭐⭐⭐")
        st.write("정말 좋아요!")
    
    with tab3:
        st.info("무료 배송 (2-3일 소요)")
    
    # FAQ
    with st.expander("❓ 자주 묻는 질문"):
        st.write("**Q: 배송은 얼마나 걸리나요?**")
        st.write("A: 보통 2-3일 소요됩니다.")

with st.expander("💡 과제 2 예시 답안"):
    st.subheader("데이터 분석 대시보드")
    
    # 상단 메트릭
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("총 방문자", "12,345", "+8%")
    m2.metric("페이지뷰", "45,678", "+12%")
    m3.metric("전환율", "3.2%", "-0.3%")
    m4.metric("평균 체류", "5:23", "+15s")
    
    # 중단
    left, right = st.columns([2, 1])
    
    with left:
        st.write("**방문자 추이**")
        data = pd.DataFrame(
            np.random.randint(100, 200, 30),
            columns=['방문자']
        )
        st.line_chart(data)
    
    with right:
        st.write("**필터**")
        period = st.selectbox("기간:", ["오늘", "7일", "30일", "90일"])
        source = st.multiselect("소스:", ["검색", "SNS", "직접", "광고"])
        st.button("적용", type="primary", use_container_width=True)
    
    # 하단 탭
    t1, t2, t3 = st.tabs(["📊 데이터", "📈 통계", "⚙️ 설정"])
    
    with t1:
        sample_df = pd.DataFrame({
            '날짜': pd.date_range('2026-01-01', periods=5),
            '방문자': [120, 145, 132, 156, 143]
        })
        st.dataframe(sample_df, use_container_width=True)
    
    with t2:
        st.write("평균 방문자:", data['방문자'].mean())
        st.write("최대값:", data['방문자'].max())
        st.write("최소값:", data['방문자'].min())
    
    with t3:
        st.write("대시보드 설정")
        st.checkbox("자동 새로고침")
        st.selectbox("새로고침 간격:", ["1분", "5분", "10분"])


# 지피티 캡쳐

import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    "<h2 style='margin-bottom: 20px;'>제품 상세 페이지</h2>",
    unsafe_allow_html=True,
)

with st.container():
    col1, col2 = st.columns([3, 4])

    # 왼쪽: 이미지
    with col1:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ96jQ9W4bT93OXaPYPMiX3hSW3ioFRp-2mCA&s",
            use_container_width=True,
        )

    # 오른쪽: 정보
    with col2:
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
                <span style="font-size:22px;">🎧</span>
                <span style="font-size:24px; font-weight:700;">무선 헤드폰 <span style="font-weight:400;">Pro</span></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='color:#555;'>₩299,000</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="margin:4px 0 12px 0;">
                <span style="color:#f1c40f; font-size:18px;">★★★★★</span>
                <span style="font-size:13px; color:#555; margin-left:6px;">
                    (4.8) - 리뷰 324개
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("고급 노이즈 캔슬링 기능이 탑재된 프리미엄 무선 헤드폰")

        # 수량
        st.markdown("**수량:**")
        q_col1, q_col2, q_col3 = st.columns([1, 2, 1])
        with q_col1:
            minus = st.button("−", key="qty_minus")
        with q_col2:
            quantity = st.number_input(
                "",
                min_value=1,
                max_value=99,
                value=1,
                step=1,
                label_visibility="collapsed",
                key="qty_input",
            )
        with q_col3:
            plus = st.button("+", key="qty_plus")

        # 장바구니 / 바로구매 버튼
        b1, b2 = st.columns([1, 1])
        with b1:
            cart = st.button("🛒 장바구니", use_container_width=True, key="btn_cart")
        with b2:
            buy = st.button("📘 바로 구매", use_container_width=True, key="btn_buy")

        if cart:
            st.success(f"{quantity}개를 장바구니에 담았습니다.")
        if buy:
            st.success(f"{quantity}개를 바로 구매합니다.")

st.markdown("<hr>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📕 상세설명", "⭐ 리뷰", "🚚 배송정보"])

with tab1:
    st.subheader("주요 특징")
    st.markdown(
        """
        - 최대 30시간 재생  
        - 고급 노이즈 캔슬링  
        - 블루투스 5.0
        """
    )

with tab2:
    st.markdown("**평균 평점:** ⭐ 4.8/5.0")
    st.markdown("---")
    st.markdown("**김철수**: ⭐⭐⭐⭐⭐")
    st.write("정말 좋아요!")

with tab3:
    st.info("무료 배송 (2–3일 소요)")

with st.expander("❓ 자주 묻는 질문"):
    st.write("교환/반품, A/S 관련 자주 묻는 질문을 여기에 넣을 수 있습니다.")

# 실행 파일
# 실행 명령어 : streamlit run app.py

"""Streamlit 앱의 진입점.

이 파일은 화면을 직접 구현하지 않고, 페이지를 등록하고 실행하는 역할만 담당한다.
"""

import streamlit as st

from ui.api_page import render_api_page
from ui.db_page import render_db_page


# 앱 전체에 공통으로 적용할 브라우저 제목과 화면 폭을 설정한다.
st.set_page_config(
    page_title="네이버 뉴스 검색/저장/조회 예시",
    layout="wide",
)

# API 조회/저장 페이지를 등록한다.
api_page = st.Page(
    render_api_page,
    title="API 조회",
    default=True,
)

# DB에 저장된 뉴스 조회 페이지를 등록한다.
db_page = st.Page(
    render_db_page,
    title="DB 저장 뉴스 조회",
)

# 사이드바에는 페이지 이동 링크만 표시한다.
navigation = st.navigation([api_page, db_page], position="sidebar")
navigation.run()
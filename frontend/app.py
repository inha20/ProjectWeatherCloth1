import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Backend API Configuration
API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="미세미세 - 스마트 옷차림 추천", layout="wide")

st.title("🧥 미세미세 (Smart Clothing Recommender)")
st.markdown("---")

# Sidebar: User Profile
with st.sidebar:
    st.header("👤 사용자 프로필")
    user_id = st.text_input("사용자 ID", value="default_user")
    
    if st.button("신규 가입"):
        name = st.text_input("이름")
        region = st.selectbox("지역", ["서울", "부산", "인천", "대구", "대전", "광주", "울산", "제주"])
        if name:
            resp = requests.post(f"{API_BASE_URL}/users/", json={"user_id": user_id, "name": name, "region": region})
            if resp.status_code == 200:
                st.success("회원가입 완료!")
            else:
                st.error("이미 존재하는 ID이거나 오류가 발생했습니다.")

# Main Area: Dashboard
try:
    # 1. Fetch User Data
    user_resp = requests.get(f"{API_BASE_URL}/users/{user_id}")
    if user_resp.status_code == 200:
        user_data = user_resp.json()
        st.info(f"선택된 지역: **{user_data['region']}** | 민감도: 추위 {user_data['cold_sensitivity']} / 더위 {user_data['heat_sensitivity']}")
        
        # 2. Fetch Recommendation
        if st.button("🔄 실시간 추천 받기"):
            rec_resp = requests.get(f"{API_BASE_URL}/recommend/{user_id}")
            if rec_resp.status_code == 200:
                data = rec_resp.json()
                
                # Layout: Weather & Recommendation
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.subheader("☀️ 현재 날씨")
                    w = data["weather"]
                    st.metric("현재 온도", f"{w['temperature']}°C")
                    st.metric("체감 온도", f"{w['feels_like']}°C")
                    st.write(f"💧 습도: {w['humidity']}%")
                    st.write(f"💨 풍속: {w['wind_speed']}m/s")
                    
                    st.subheader("🌫️ 미세먼지")
                    d = data["dust"]
                    color = "green" if d["status"] == "좋음" else "orange" if d["status"] == "보통" else "red"
                    st.markdown(f"상태: <span style='color:{color}; font-weight:bold;'>{d['status']}</span>", unsafe_allow_html=True)
                    st.write(f"PM2.5: {d['pm25']}µg/m³")
                
                with col2:
                    st.subheader("👔 추천 옷차림")
                    r = data["recommendation"]
                    
                    # Recommendation Cards
                    st.success(f"**필요 보온 지수 (CLO):** {r['warmth_score']}")
                    
                    st.markdown("#### [코디 조합]")
                    if r["outer"]:
                        st.info(f"🧥 **겉옷**: {r['outer']}")
                    st.warning(f"👕 **상의**: {r['top']}")
                    st.warning(f"👖 **하의**: {r['bottom']}")
                    st.info(f"👟 **신발**: {r['shoes']}")
                    
                    if r["accessories"]:
                        st.markdown(f"👓 **액세서리**: {', '.join(r['accessories'])}")
                    
                    if r["tips"]:
                        st.markdown("---")
                        st.markdown("#### 💡 오늘을 위한 팁")
                        for tip in r["tips"]:
                            st.write(f"- {tip}")
                            
            else:
                st.error("추천 데이터를 가져오지 못했습니다.")
    else:
        st.warning("사용자 ID를 확인하거나 먼저 회원가입을 진행해 주세요.")

except Exception as e:
    st.error(f"백엔드 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요. ({e})")

st.markdown("---")
st.caption("Designed with ❤️ for professional portfolio.")

# 🧥 미세미세 (Smart Clothing Recommender) v2.0

> 날씨, 미세먼지, 개인 건강 상태를 종합 분석하여 최적의 옷차림을 제안하는 **전문가급 AI 의류 추천 시스템**입니다.

![App Preview](https://via.placeholder.com/1200x600/0d1117/e6edf3?text=Weather+Cloth+v2.0+Dashboard+Preview)

## 🌟 주요 특징 (Core Features)

- **전문적인 Client-Server 아키텍처**: FastAPI 백엔드와 Streamlit 프론트엔드를 분리하여 실제 서비스 환경을 구현했습니다.
- **점수 기반 추천 엔진 (Score-based Engine)**: 단순 `if-else`를 넘어, 의류별 보온 지수(CLO)와 기상 변수(온도, 습도, 풍속 등)를 조합한 정밀 알고리즘을 사용합니다.
- **개인화 보정 시스템**: 사용자의 추위/더위 민감도 및 과거 피드백을 학습하여 추천 결과를 개인화합니다.
- **실무급 데이터 관리**: SQLAlchemy ORM을 사용하여 PostgreSQL/SQLite를 모두 지원하는 견고한 데이터 레이어를 구축했습니다.

## 🏗️ 시스템 아키텍처 (Architecture)

```mermaid
graph TD
    A[Streamlit Frontend] -->|REST API| B[FastAPI Backend]
    B --> C[Weather Service]
    B --> D[Recommendation Service]
    B --> E[User Service]
    C -->|Fetch| F[Public Data API]
    E -->|ORM| G[Database (SQLAlchemy)]
    D -->|Logic| H[Score-based Algorithm]
```

## 🚀 시작하기 (Getting Started)

### 방법 1: 원클릭 설치 및 실행 (Windows)
1. `install.bat` 실행 (가상환경 및 패키지 설치)
2. `run.bat` 실행 (Backend & Frontend 자동 시작)

### 방법 2: 수동 실행
1. `pip install -r requirements.txt`
2. `uvicorn backend.app:app --port 8000` (백엔드 실행)
3. `streamlit run frontend/app.py` (프론트엔드 실행)

## 📂 파일 구조 (Directory Structure)

- `backend/`: FastAPI 기반의 서버 사이드 로직
  - `services/`: 날씨 수집 및 추천 엔진 핵심 알고리즘
- `frontend/`: Streamlit 기반의 인터랙티브 웹 대시보드
- `install.bat` / `run.bat`: 자동화 스크립트
- `MANUAL.md`: 상세 기능 가이드
- `INTERVIEW.md`: 기술 면접 대비 질문 및 답변

---
Designed with professional standards for portfolio excellence.

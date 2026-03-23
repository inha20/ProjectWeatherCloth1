@echo off
chcp 65001 >nul
echo ====================================
echo   ProjectWeatherCloth1 실행 중
echo ====================================
echo.

call venv\Scripts\activate

echo [1/2] 백엔드 서버(FastAPI) 시작 중...
start /b uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload

echo [2/2] 프론트엔드 대시보드(Streamlit) 시작 중...
timeout /t 3 >nul
streamlit run frontend/app.py --server.port 8501

pause

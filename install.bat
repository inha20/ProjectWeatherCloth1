@echo off
chcp 65001 >nul
echo ====================================
echo   ProjectWeatherCloth1 설치 가이드
echo ====================================
echo.
echo 1. 가상환경 생성 중...
python -m venv venv
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않거나 경로 설정이 잘못되었습니다.
    pause
    exit /b
)

echo 2. 필수 패키지 설치 중...
call venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy pydantic-settings streamlit requests psycopg2-binary
if errorlevel 1 (
    echo [오류] 패키지 설치 과정에서 실패했습니다.
    pause
    exit /b
)

echo.
echo 설치 완료! run.bat을 실행하여 프로그램을 시작하세요.
pause

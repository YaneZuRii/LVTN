@echo off
chcp 65001 >nul
title Up LVTN len GitHub
cd /d "%~dp0"

echo ============================================
echo  Thu muc chua FILE: %CD%
echo  GitHub: https://github.com/YaneZuRii/LVTN
echo ============================================
echo.
echo Neu loi 403: mo file docs\HUONG_DAN_UP_LEN_GIT.md
echo (xoa credential cu + tao token moi)
echo.
pause

git status
echo.
echo Dang push len GitHub (origin main)...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo THANH CONG! Xem: https://github.com/YaneZuRii/LVTN
) else (
    echo.
    echo THAT BAI. Lam theo HUONG_DAN_UP_LEN_GIT.md
    start "" "%~dp0docs\HUONG_DAN_UP_LEN_GIT.md"
)
echo.
pause
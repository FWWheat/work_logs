@echo off
chcp 65001 >nul
title 白色物体轨迹跟踪程序

echo ========================================
echo   白色物体实时轨迹跟踪程序
echo ========================================
echo.
echo 请选择运行模式：
echo   1. 使用ALVIUM相机（推荐）
echo   2. 使用电脑摄像头
echo   3. 测试模式（模拟动画）
echo   4. 退出
echo.

set /p choice=请输入选项 (1-4): 

if "%choice%"=="1" (
    echo.
    echo 正在启动ALVIUM相机模式...
    echo.
    python realtime_trajectory_demo.py
) else if "%choice%"=="2" (
    echo.
    echo 正在启动摄像头模式...
    echo.
    python realtime_trajectory_demo.py --webcam
) else if "%choice%"=="3" (
    echo.
    echo 正在启动测试模式...
    echo.
    python trajectory_tracker.py
) else if "%choice%"=="4" (
    echo.
    echo 再见！
    timeout /t 2 >nul
    exit
) else (
    echo.
    echo 无效的选项！
    timeout /t 2 >nul
    goto :eof
)

echo.
echo ========================================
echo 程序已结束
echo ========================================
pause


@echo off
echo ============================================
echo 关闭可能占用相机的Vimba程序
echo ============================================
echo.

echo 正在查找并关闭Vimba相关进程...
echo.

taskkill /F /IM "VimbaViewer.exe" 2>nul
if %errorlevel% == 0 (
    echo [√] 已关闭 Vimba Viewer
) else (
    echo [ ] Vimba Viewer 未运行
)

taskkill /F /IM "VimbaXViewer.exe" 2>nul
if %errorlevel% == 0 (
    echo [√] 已关闭 Vimba X Viewer
) else (
    echo [ ] Vimba X Viewer 未运行
)

taskkill /F /IM "VmbPy*.exe" 2>nul

echo.
echo ============================================
echo 完成！现在可以运行程序了
echo ============================================
echo.
pause


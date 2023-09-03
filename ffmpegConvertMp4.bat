@echo off
 
::在下方设置需要处理的视频格式
set Ext=*.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov

md output

for %%a in (%Ext%) do (
	if /i %%~xa==.mp4 (
		ffmpeg -i "%%a"  "output\%%~na.mp4"
	) else (
		ffmpeg -i "%%a" -c copy "output\%%~na.mp4"
		del %%a
	)
)

::pause

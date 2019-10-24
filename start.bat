@echo off

set /p pushKey=サーバー起動前にバックアップしますか(y/n)？  : %pushKey%
if "%pushKey%"=="y" (
	echo バックアップを開始します...
	echo.
	xcopy /s /q %CD% C:\MNMCBUs\Rikaisha_kettle_backup1\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%\
	echo.
	echo 処理が完了しました。サーバーを起動します...
) else if "%pushKey%"=="n" ( 
	echo バックアップしないで起動します...
) else if "%pushKey%"=="Y" ( 
	echo 大文字が入力されました。バックアップしないで起動します...
)else (
	echo y以外が入力されました。バックアップしないで起動します...
)
echo.

java -Xms4096M -Xmx4096M -jar Mohist-36b8702-server.jar -o true

set /p pushKey=バックアップしますか(y/n)？  : %pushKey%
if "%pushKey%"=="y" (
	echo バックアップを開始します...
	echo.
	xcopy /s /q %CD% C:\COLKMCBUs\Rikaisha_kettle_backup\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%\
	echo.
	echo 処理が完了しました。
) else if "%pushKey%"=="n" ( 
	echo サーバを終了しました。
) else if "%pushKey%"=="Y" ( 
	echo 大文字が入力されました。サーバーを終了しました。
)else (
	echo y以外が入力されました。サーバーを終了しました。
)
echo.

pause
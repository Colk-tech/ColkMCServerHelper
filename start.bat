@echo off

set /p pushKey=�T�[�o�[�N���O�Ƀo�b�N�A�b�v���܂���(y/n)�H  : %pushKey%
if "%pushKey%"=="y" (
	echo �o�b�N�A�b�v���J�n���܂�...
	echo.
	xcopy /s /q %CD% C:\MNMCBUs\Rikaisha_kettle_backup1\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%\
	echo.
	echo �������������܂����B�T�[�o�[���N�����܂�...
) else if "%pushKey%"=="n" ( 
	echo �o�b�N�A�b�v���Ȃ��ŋN�����܂�...
) else if "%pushKey%"=="Y" ( 
	echo �啶�������͂���܂����B�o�b�N�A�b�v���Ȃ��ŋN�����܂�...
)else (
	echo y�ȊO�����͂���܂����B�o�b�N�A�b�v���Ȃ��ŋN�����܂�...
)
echo.

java -Xms4096M -Xmx4096M -jar Mohist-36b8702-server.jar -o true

set /p pushKey=�o�b�N�A�b�v���܂���(y/n)�H  : %pushKey%
if "%pushKey%"=="y" (
	echo �o�b�N�A�b�v���J�n���܂�...
	echo.
	xcopy /s /q %CD% C:\COLKMCBUs\Rikaisha_kettle_backup\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%\
	echo.
	echo �������������܂����B
) else if "%pushKey%"=="n" ( 
	echo �T�[�o���I�����܂����B
) else if "%pushKey%"=="Y" ( 
	echo �啶�������͂���܂����B�T�[�o�[���I�����܂����B
)else (
	echo y�ȊO�����͂���܂����B�T�[�o�[���I�����܂����B
)
echo.

pause
; milktea0614@naver.com
;
; =========== GUI ===========
Gui, Add, Button, x10 y20 w150 h20 gCancel, 모든 예약 종료 취소			;모든 예약 종료 취소 버튼
Gui, Add, Button, x10 y70 w100 h20 gStopOne, 1시간 뒤 종료			; 1시간 뒤 종료 버튼
Gui, Add, Button, x150 y70 w100 h20 gStopTwo, 2시간 뒤 종료		; 2시간 뒤 종료 버튼
Gui, Add, Button, x200 y110 w50 h20 gStop, 종료

Gui, Add, Edit, x10 y110 w50 h20 vThour +Number,0
Gui, Add, Edit, x100 y110 w50 h20 vTminute +Number,0

Gui, Add, Text, x65 y115 w25 h20, 시간
Gui, Add, Text, x155 y115 w40 h20, 분 뒤에

Gui, Add, Text, x10 y60 w260 h1 0x4			; 수평 라인 1
Gui, Add, Text, x10 y100 w260 h1 0x4			; 수평 라인 2

Gui, Show, w280 h150,Window10 예약종료
;===========================

GoSub,Main

Main:
	; 내용 구현
	return

Stop:
	GuiControlGet, Tminute
	GuiControlGet, Thour
	if (Tminute="")||(Thour=""){
		MsgBox, 입력된 값이 잘 못 되었습니다.
	} else {
		ctime :=Thour*3600+Tminute*60
		RunWait, %ComSpec% /c "shutdown -a", ,hide
		RunWait, %ComSpec% /c "shutdown -s -t %ctime%", ,hide
	}
	return
	
StopOne:
	RunWait, %ComSpec% /c "shutdown -a", ,hide
	RunWait, %ComSpec% /c "shutdown -s -t 3600", ,hide
	return
	
StopTwo:
	RunWait, %ComSpec% /c "shutdown -a", ,hide
	RunWait, %ComSpec% /c "shutdown -s -t 7200", ,hide
	return
	
Cancel:
	RunWait, %ComSpec% /c "shutdown -a", ,hide
	return

GuiClose:
	exitapp
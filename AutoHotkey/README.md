# AutoHotkey
AutiHotkey를 사용하면서 알게 된 사실이나 기록할만한 사실, 구현한 스크립트 등을 업로드 합니다.

하기는 제가 기억할 만하다고 생각되는 정보를 조금씩 추가하여 업로드 합니다.

***


### 1. AutoHotkey Draw Line
	global SS_BLACKRECT   := 0x4       ; Window Frame (COLOR_WINDOWFRAME)과 같은 색을 단색으로 채움
    global SS_GRAYRECT    := 0x5       ; Desktop (COLOR_BACKGROUND)과 같은 색을 단색으로 채움
    global SS_WHITERECT   := 0x6       ; Window (COLOR_WINDOW)과 같은 색을 단색으로 채움
    global SS_BLACKFRAME  := 0x7       ; Window Frame (COLOR_WINDOWFRAME)과 같은 색을 단색으로 채움
    global SS_GRAYFRAME   := 0x8       ; Desktop, the screen background (COLOR_BACKGROUND)과 같은 단색으로 채움

###### AutoHotkey 사용 예시
	Gui, Add, Text, x10  y30    w50   h1    0x4       ; 수평 라인
    Gui, Add, Text, x10  y40    w1    h50   0x4       ; 수직 라인

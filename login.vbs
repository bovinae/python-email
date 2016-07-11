set sh=WScript.CreateObject("WScript.Shell")
sh.SendKeys "ssh linwei@essh.sandai.net{ENTER}"
WScript.Sleep 1500
sh.SendKeys "FwMPLc1k{ENTER}"

Dim objfs
Dim s
Set objfs=CreateObject("scripting.filesystemobject")
'objf.SkipLine()
'objf.Skip(4)
Dim cnt
cnt=0
do
	WScript.Sleep 500
	Set objf=objfs.OpenTextFile("C:\Users\lin\tmp.txt",1,False)
	s=objf.Read(8)
	objf.close
	If Int(s)>0 Then
		sh.SendKeys Int(s)
		sh.SendKeys "{ENTER}"
		exit do
	End If
	cnt=cnt+1
	If cnt>50 Then
		exit do
	End If
loop

'WScript.Sleep 500
'sh.SendKeys "exit{ENTER}"
'WScript.Sleep 500
'sh.SendKeys "{ENTER}"
'WScript.Sleep 500
'sh.SendKeys "quit{ENTER}"

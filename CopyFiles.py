from pywinauto.application import Application
#import time


password=input("Password: ")
app = Application ().start (cmd_line=u'putty -ssh automation@10.58.220.139')
putty = app.PuTTY
putty.wait ('ready')
#time.sleep (1)
putty.type_keys (password)
putty.type_keys ("{ENTER}")
#time.sleep (1)
putty.type_keys ("ls")
putty.type_keys ("{ENTER}")
putty.type_keys("cp log1/1.pdf targetdir/",with_spaces=True)
putty.type_keys("{ENTER}")
putty.type_keys("cp log2/2.pdf targetdir/",with_spaces=True)
putty.type_keys("{ENTER}")
putty.type_keys("cp log3/3.pdf targetdir/",with_spaces=True)
putty.type_keys("{ENTER}")
putty.type_keys("cp log4/4.pdf targetdir/",with_spaces=True)
putty.type_keys("{ENTER}")
putty.type_keys("cd targetdir",with_spaces=True)
putty.type_keys("{ENTER}")
putty.type_keys("ls")
putty.type_keys("{ENTER}")
#time.sleep (5)
putty.type_keys("exit")
putty.type_keys("{ENTER}")

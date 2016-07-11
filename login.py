# -*- coding: utf-8 -*- 

import imaplib
import email
import os
import threading
import time
import datetime
import math
import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(r'C:\Users\lin\tmp.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

file_init = open(r"C:\Users\lin\tmp.txt", "w")
file_init.write("00000000")
file_init.close()
	
def start_xshell():
	os.system('start Xshell.exe')
	os.system('C:\Users\lin\login.vbs')
	
def get_passcode():
	cnt = 1
	while True:
		time.sleep(1)
		conn = imaplib.IMAP4("imap.xunlei.com", 143)
		conn.login("linwei@xunlei.com", "Yt3w1D6bwH0Q")
		conn.select("INBOX")
		type, data = conn.search(None, '(SUBJECT "Essh")')
		msgList = data[0].split()
		type,data=conn.fetch(msgList[len(msgList)-1],'(RFC822)')
		msg=email.message_from_string(data[0][1])	
		logger.info("%s" % (msg))	
		content=msg.get_payload(decode=True)
		user, passcode = content.split("passcode: ")
		d=datetime.datetime.strptime(msg["Date"], "%a, %d %b %Y %H:%M +0800")
		logger.info("%s" % (d))
		s=int(time.mktime(d.timetuple()))
		now = int(math.floor(time.time()))		
		logger.info("%d" % (s))
		logger.info("%d" % (now))
		conn.logout()
		if(now - s < 90 or cnt >= 20):
			try:
			   	file_out = open(r"C:\Users\lin\tmp.txt", "w")
				file_out.write(passcode)
				file_out.close()
			except IOError, e:
			   logger.info("%s" % (e))	
			break
		if(cnt < 20):
			cnt += 1

#if __name__ == '__main__':
threads = []
t1 = threading.Thread(target=start_xshell)
threads.append(t1)
t2 = threading.Thread(target=get_passcode)
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()

for t in threads:
	t.join()	

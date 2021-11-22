"""
SMTP Tester / Mail Sender Using Python Library smtplib
------------------------------------------------------------------------
By: Mohammed Shahid
------------------------------------------------------------------------
Repo : https://github.com/pkshahid/smtp_tester/


Usage: python test_smtp.py
            OR
       python3 test_smtp.py

At verbose == False and debuglevel == 0, smtptest will either succeed silently or print an error. 
Setting verbose or a debuglevel to 1 will generate intermediate output.

See also http://docs.python.org/library/smtplib.html
"""



import smtplib
from time import strftime
import sys



#-----------------------------------------------------------------------
#                       CONFIGURATION INPUTS 
#-----------------------------------------------------------------------
USE_SSL        = False                                  # True to use with SSL
USE_TLS        = True                                   # True to user with TLS
SMTP_USER      = '<smtp_username>'                   	# SMTP USERNAME
SMTP_PASS      = '<smtp_password>'                  	# SMTP PASSWORD 
FROM_ADDRESS   = 'frommail@example.com'           	# Email address which use as From address
TO_ADDRESS     = 'tomail@example.com'               	# Email Address or array of emails which mail to be send
SERVER_ADDRESS = '<smtp_host>'                  	# SMTP Host        
PORT 	       = 587                                    # SMTP Port  (Eg :- 587,25,465)
DEBUG	       = 1                                      # 1/0 to set/unset Debug mode
VERBOSE        = True                                   # True/False to enable/disable Verbose

TIMESTAMP      = strftime("%Y-%m-%d %H:%M:%S")          # Current Time (Optional)

#-----------------------------------------------------------------------




#<<<<<<<<<<<<<<<<<<<<< MESSAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

MESSAGE = "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s" % (FROM_ADDRESS, TO_ADDRESS, TIMESTAMP,TIMESTAMP)

#<<<<<<<<<<<<<<<<<<<<< MESSAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




#-----------------------------------------------------------------------
#                       OPERATION
#-----------------------------------------------------------------------
server = None
if USE_SSL:
	server = smtplib.SMTP_SSL()
else:
	server = smtplib.SMTP()

server.set_debuglevel(DEBUG)
server.connect(SERVER_ADDRESS, PORT)
server.ehlo()
if USE_SSL: server.starttls()
server.ehlo()
if SMTP_USER != "": server.login(SMTP_USER, SMTP_PASS)
server.sendmail(FROM_ADDRESS, TO_ADDRESS, MESSAGE)
server.quit()

#-----------------------------------------------------------------------

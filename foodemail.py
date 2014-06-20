import smtplib
from datetime import datetime
import get
groceries = ["Hey! \n\nThe grocery list for this week is as follows: \n\n"]
food = {'protein': [['hummus', 1.5, 780],['honey roasted turkey', 0.75, 270],['tofu', 0.4, 500], ['soup', 1.5, 250]], 'drinks': [['diet ginger ale(packs of 12)', 0.5], ['water bottles', 3], ['unsweetened almond/soy milk', 0.75]], 'fruit/veg': [['oranges/clementines', .2, 60],['bananas(bunch)', .2, 80],['green apples', 3, 80], ['salad', 1/3, 40], ['frozen corn', 0.5, 100],['green peppers', 2, 15]]}

def noticeEMail(starttime, usr, psw, fromaddr, toaddr, message):
 # Calculate run time
 runtime=datetime.now() - starttime
    
 # Initialize SMTP server
 server=smtplib.SMTP('smtp.gmail.com:587')
 server.starttls()
 server.login(usr,psw)
    
 # Send email
 senddate=datetime.strftime(datetime.now(), '%Y-%m-%d')
 subject="Grocery List for this week"
 m="Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (senddate, fromaddr, toaddr, subject)
 msg=message
    
 server.sendmail(fromaddr, toaddr, m+msg)
 server.quit()


if __name__ == '__main__':
 # Start time of script
 starttime=datetime.now()
 
 # Fill these in with the appropriate info...
 usr='YOUREMAIL'
 psw=get.getPass('YOURPASSWORD')
 fromaddr='YOUREMAIL@SERVER.COM'
 toaddr= ['RECIPIENT@SERVER.COM', 'RECIPIENT2@SERVER.COM'] #As many recipients as you like

 #creates appropriate grocery info    
 index = ['protein', 'drinks', 'fruit/veg']
 print "Days? "
 days = int(raw_input())
 for x in range(0, len(food)):
  for y in range(0, len(food[index[x]])-1):
   if int(days*food[index[x]][y][1]) > 0:
    string = '\t' + food[index[x]][y][0] + ' x%d \n' % int(days*food[index[x]][y][1])
    groceries.append(string)
   else: pass
 print ' '.join(str(k) for k in groceries)
 print "Enter 0 if satisfactory, enter 1 to add to the list: "
 user = int(raw_input())
 if user == 0: pass
 elif user == 1:
  print "What would you like to add?"
  addition = raw_input()
  y = [x.strip() for x in addition.split(',')]
  for x in xrange(0, len(y)):
   groceries.append("\t%s \n" % y[x]) 
 groceries.append("\nCheers! \n\t \tRin")
 msg = ' '.join(str(k) for k in groceries)
 # Send notification email
     noticeEMail(starttime, usr, psw, fromaddr, toaddr, msg)

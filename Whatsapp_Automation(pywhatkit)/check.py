# importing the module
import pywhatkit
from datetime import date, datetime
 
# using Exception Handling to avoid
# unprecedented errors
try:

  now = datetime.now()

   
  # sending message to receiver
  pywhatkit.sendwhatmsg("+919931496730",
                        "Hello from r",
                        int(now.strftime("%H")), int(now.strftime("%S"))+2)
                        
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")
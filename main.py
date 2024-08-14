import pywhatkit as w
from number import phone_number

# phone_number = '+911234567890'
msg = 'hello'
hour = 10
minutes = 27

w.sendwhatmsg(phone_number, msg, hour, minutes)

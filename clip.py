import pyperclip
import time

last_value = pyperclip.paste()
tmp_value = ""
while True:
    time.sleep(1)
    tmp_value = pyperclip.paste()
    
    if tmp_value != last_value and tmp_value!= "":
            #recent_value = tmp_value 
            out = tmp_value.replace("\r\n"," ")
            pyperclip.copy(out)
            print("\n value was changed into: %s" %str(out))
            last_value = tmp_value
            time.sleep(1)
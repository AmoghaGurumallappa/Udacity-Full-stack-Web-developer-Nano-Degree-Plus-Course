import time;
import webbrowser;


i=3;
j=0;

print("This program started"+time.ctime())
while(j<i):
    time.sleep(10)
    webbrowser.open("http://amoghagurumallappa.wixsite.com/mysite")
    j=j+1;


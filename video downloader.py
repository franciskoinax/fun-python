from pytube import YouTube
import sys
print(sys.argv)# sys provides some variables used or maintained by the Python interpreter
# argv stands for "argument vector" and is a list in Python that holds the command-line arguments passed to the script
$ pythonargvtest.py
['argvtest.py']
? pythonargvtest.py 1  z
if len(sys.argv) < 2:
    print("no arguments given")
    quit()
else:
    arg1 = sys.argv[1]
link = argv[1] #is going to give the first command line argument
yt = YouTube(link)
print("title: ",yt.title)
print("View: ", yt.views)

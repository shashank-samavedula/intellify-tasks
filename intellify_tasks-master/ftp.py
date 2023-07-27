import ftplib
 
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")
 
data = []
 
ftp.dir(data.append)
 
ftp.quit()
 
for line in data:
    print("-", line)
    

import ftplib
 
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")
 
data = []
 
ftp.cwd('/pub/')          
ftp.dir(data.append)
 
ftp.quit()
 
for line in data:
    print("-", line)


import ftplib
 
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")
 
 
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")
 
ftp.cwd('/pub/')          
getFile(ftp,'README.nluug')

try:
    fp = open('README.nluug')
    for line in fp:
        print(line)
except:
    print("Error")
ftp.quit()
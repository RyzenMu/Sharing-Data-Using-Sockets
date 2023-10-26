import urllib.request

fileContent = urllib.request.urlopen('http://marvin.cs.uidaho.edu/Teaching/CS515/pythonTutorial.pdf')
fp = open('pythonGuidoVanRossum1.pdf', 'wb')
fp.writelines(fileContent.decode())
fp.close()

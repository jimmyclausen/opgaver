'''
Created on 27/11/2012

@author: jimju
'''
myfile = open("ferieplan2013 14.txt", encoding="utf-8")

for thisline in myfile.readlines():
    print(thisline)
    
    Description = myfile.readline()
    print( Description )
    
    dateline = myfile.readline()
    print(dateline)
    
    dateparts = dateline.split( "-" )
    print( dateparts )
    
    startdate = dateparts[0]
    startdate = startdate.strip().strip(")(") # strip (")(") betyder den skal fjerne " fra linien
    print ( startdate )
    
    
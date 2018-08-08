import visa
import pylab as pl
import numpy as np

rm=visa.ResourceManager() 
myinst=rm.open_resource("USB0::0x0699::0x0408::C012443::INSTR") 
myinst.timeout=2000 
myinst.write('*CLS') 
myinst.write('*IDN?') 

myinst.write(':DATa:SOUrce CH1') 
myinst.write(':DATa:STARt 1') 
myinst.write(':DATa:STOP 8000 ') 
myinst.write(':DATa:ENCdg ASCIi') 
myinst.write(':DATa:WIDth 1') 
myinst.write(':HEADer 1') 
myinst.write('WFMOutpre?') 
complete=myinst.read() 
myinst.write(':HEADer 0') 
myinst.write(':CURVe?') 

filename=(r'''C:\Users\UCaN_Lab02\Desktop\test1.csv''') 
my_file= open(filename,'w') 
my_file.truncate() 
my_file.write(myinst.read()) 
my_file=open(filename,'r') 
#contents=my_file.read() 
my_file.close() 
#print (contents) 
myinst.close()

print('Close Instrument Connection') 
print('Complete')

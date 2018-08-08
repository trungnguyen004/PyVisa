import time
import visa
import pylab as pl
import numpy as np

visa_address = 'USB0::0x0699::0x0408::C012443::INSTR'

rm = visa.ResourceManager()
inst = rm.open_resource(visa_address)
inst.timeout = 2000 # 2 seconds
inst.write('*CLS') # Clear ESR

print(inst.query("*IDN?"))

# while loop should be here

for i in range(10):
    input("""
    ACTION:
    Connect probe to oscilloscope Channel 1 and the probe compensation signal.
    Press Enter to continue...
    """)

    inst.write('data:source CH1') # Channel 1
    inst.write('data:start 1') # First sample
    record = int(inst.query('wfmoutpre:nr_pt?'))
    inst.write('data:stop {}'.format(record)) # Last sample 
    inst.write('data:encdg ASCIi') 
    inst.write('data:width 1')  
    inst.write('wfmoutpre?') 
    complete=inst.read() 
    inst.write('header 0') 
    inst.write('curve?')

    filename=(r'''C:\Users\UCaN_Lab02\Desktop\Data_collect %d.csv''' %(i)) 
    my_file= open(filename,'w') 
    my_file.truncate() 
    my_file.write(inst.read())   
    my_file.close()  
    
inst.close()
print('Close Instrument Connection')
print('Complete')

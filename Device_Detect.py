import visa
import sys


rm = visa.ResourceManager()
print (rm.list_resources())
inst = rm.open_resource('USB0::0x0699::0x0408::C012443::INSTR')
print(inst)
print(inst.query("*IDN?"))
print(inst.write("*IDN?"))
print(inst.write("*CLS"))
values = inst.query_binary_values('CURV?', datatype='d', is_big_endian=True)
#print(values)
print(inst.session)
print(inst.timeout)


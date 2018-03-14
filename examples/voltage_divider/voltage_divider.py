from pycircuit.build import Builder
from pycircuit.circuit import *
from pycircuit.library import *

Component('Connector', 'A connector', Pin('vin'), Pin('vout'), Pin('gnd'))
Device('Connector', 'Connector', 'Pins_3x1',
       Map('A1', 'vin'),
       Map('A2', 'vout'),
       Map('A3', 'gnd')
       )


@circuit('Voltage Divider', 'gnd', None, 'vin', 'vout')
def voltage_divider(self, gnd, vin, vout):
    Inst('R', '10k 0805')['~', '~'] = vin, vout
    Inst('R', '10k 0805')['~', '~'] = vout, gnd


@circuit('Voltage Divider Top')
def top(self):
    vin, vout, gnd = nets('vin vout gnd')
    SubInst(voltage_divider())['vin', 'vout', 'gnd'] = vin, vout, gnd
    Inst('Connector', 'Pins_3x1')['vin', 'vout', 'gnd'] = vin, vout, gnd


if __name__ == '__main__':
    Builder(top()).compile()

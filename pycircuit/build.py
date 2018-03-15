import os
from pycircuit.compiler import Compiler


def netlistsvg(filein, fileout):
    skin = '~/repos/netlistsvg/lib/analog.svg'
    os.system('netlistsvg --skin %s %s -o %s' % (skin, filein, fileout))


def string_to_filename(string):
    return string.lower().replace(' ', '_')


class Builder(object):
    def __init__(self, circuit):
        self.base_file_name = string_to_filename(circuit.name)
        self.builddir = 'build'
        self.files = {
            'net_in': self.base_file_name + '.net',
            'net_out': self.base_file_name + '.out.net',
            'net_yosys': self.base_file_name + '.json',
            'net_svg': self.base_file_name + '.net.svg'
        }
        for tag, filename in self.files.items():
            self.files[tag] = os.path.join(self.builddir, filename)

        self.circuit = circuit

    def compile(self):
        if not os.path.exists(self.builddir):
            os.makedirs(self.builddir)
        
        self.circuit.to_file(self.files['net_in'])
        
        circuit = Compiler.compile(self.files['net_in'], self.files['net_out'])
        circuit.to_yosys_file(self.files['net_yosys'])
        
        netlistsvg(self.files['net_yosys'], self.files['net_svg'])
        return circuit

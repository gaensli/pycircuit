import numpy as np
import scipy.signal as sig
from pycircuit.build import Builder
from pycircuit.testbench import testbench

from sallen_key import lp_sallen_key, top


def lp_optimize():
    tb = Builder(testbench(lp_sallen_key())).compile()

if __name__ == '__main__':
    lp_optimize()

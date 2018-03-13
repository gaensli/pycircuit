from pycircuit.build import Builder
from pycircuit.library.design_rules import oshpark_4layer
from pycircuit.library.outlines import sick_of_beige
from placer import Placer
from pykicad.pcb import Zone
from mcu import mcu


def place(filein, fileout):
    placer = Placer()
    placer.place(filein, fileout)


def post_process(pcb, kpcb):
    xmin, ymin, xmax, ymax = pcb.outline.polygon.bounds
    coords = [(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin)]

    zone = Zone(net_name='GND', layer='F.Cu',
                polygon=coords, clearance=0.3)
    
    kpcb.zones.append(zone)
    return kpcb


if __name__ == '__main__':
    Builder(mcu(), outline=sick_of_beige('DP8080'), pcb_attributes=oshpark_4layer(),
            place=place, post_process=post_process).build()

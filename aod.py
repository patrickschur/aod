import argparse
import struct


SET_MEMORY_CLOCK = 0x20001
SET_TCL = 0x20002
SET_TRCDRD = 0x20003
SET_TRCDWR = 0x20004
SET_TRAS = 0x20005
SET_TRP = 0x20006
SET_PROCODT = 0x20007
SET_TRCPAGE = 0x20008
SET_TRC = 0x20009
SET_TRFC = 0x2000A
SET_TRFC2 = 0x2000B
SET_TRFC4 = 0x2000C
SET_TFAW = 0x2000D
SET_TRRDS = 0x2000E
SET_TRRDL = 0x2000F
SET_TWR = 0x20010
SET_TWTRS = 0x20011
SET_TWTRL = 0x20012
SET_TCKE = 0x20013
SET_TCWL = 0x20014
SET_TRTP = 0x20015
SET_TRDRDSC = 0x20016
SET_TRDRDSCL = 0x20017
SET_TRDRDSD = 0x20018
SET_TRDRDDD = 0x20019
SET_TWRWRSC = 0x2001A
SET_TWRWRSCL = 0x2001B
SET_TWRWRSD = 0x2001C
SET_TWRWRDD = 0x2001D
SET_TRDWR = 0x2001E
SET_TWRRD = 0x2001F


class AOD:
    def __init__(self):
        self.COMMANDS = {
            'mclk': self.set_mclk,
            'tcl': self.set_tcl,
            'trcdrd': self.set_trcdrd,
            'trcdwr': self.set_trcdwr,
            'tras': self.set_tras,
            'trp': self.set_trp,
            'procodt': self.set_procodt,
            'trcpage': self.set_trcpage,
            'trc': self.set_trc,
            'trfc': self.set_trfc,
            'trfc2': self.set_trfc2,
            'trfc4': self.set_trfc4,
            'tfaw': self.set_tfaw,
            'trrds': self.set_trrds,
            'trrdl': self.set_trrdl,
            'twr': self.set_twr,
            'twtrs': self.set_twtrs,
            'twtrl': self.set_twtrl,
            'tcke': self.set_tcke,
            'tcwl': self.set_tcwl,
            'trtp': self.set_trtp,
            'trdrdsc': self.set_trdrdsc,
            'trdrdscl': self.set_trdrdscl,
            'trdrdsd': self.set_trdrdsd,
            'trdrddd': self.set_trdrddd,
            'twrwrsc': self.set_twrwrsc,
            'twrwrscl': self.set_twrwrscl,
            'twrwrsd': self.set_twrwrsd,
            'twrwrdd': self.set_twrwrdd,
            'trdwr': self.set_trdwr,
            'twrrd': self.set_twrrd,
        }

    def __enter__(self):
        self.aod = open('/proc/acpi/call', 'w+')
        return self

    def __exit__(self, *_):
        self.aod.close()

    def dispatch(self, k, v):
        if k in self.COMMANDS:
            # noinspection PyArgumentList
            self.COMMANDS[k](v)

    @staticmethod
    def create_buffer(command, value):
        buffer = struct.pack('IH', command, value)
        return 'b' + ''.join([f'{i:02X}' for i in buffer])

    def wmaa(self, command, value):
        buffer = AOD.create_buffer(command, value)
        self.aod.write(f'\\AOD_.WMAA 0 5 {buffer}')
        self.aod.seek(0)

    def set_mclk(self, memory_clock):
        self.wmaa(SET_MEMORY_CLOCK, memory_clock)

    def set_tcl(self, tcl):
        self.wmaa(SET_TCL, tcl)

    def set_trcdrd(self, trcdrd):
        self.wmaa(SET_TRCDRD, trcdrd)

    def set_trcdwr(self, trcdwr):
        self.wmaa(SET_TRCDWR, trcdwr)

    def set_tras(self, tras):
        self.wmaa(SET_TRAS, tras)

    def set_trp(self, trp):
        self.wmaa(SET_TRP, trp)

    def set_procodt(self, procodt):
        self.wmaa(SET_PROCODT, procodt)

    def set_trcpage(self, trcpage):
        self.wmaa(SET_TRCPAGE, trcpage)

    def set_trc(self, trc):
        self.wmaa(SET_TRC, trc)

    def set_trfc(self, trfc):
        self.wmaa(SET_TRFC, trfc)

    def set_trfc2(self, trfc2):
        self.wmaa(SET_TRFC2, trfc2)

    def set_trfc4(self, trfc4):
        self.wmaa(SET_TRFC4, trfc4)

    def set_tfaw(self, tfaw):
        self.wmaa(SET_TFAW, tfaw)

    def set_trrds(self, trrds):
        self.wmaa(SET_TRRDS, trrds)

    def set_trrdl(self, trrdl):
        self.wmaa(SET_TRRDL, trrdl)

    def set_twr(self, twr):
        self.wmaa(SET_TWR, twr)

    def set_twtrs(self, twtrs):
        self.wmaa(SET_TWTRS, twtrs)

    def set_twtrl(self, twtrl):
        self.wmaa(SET_TWTRL, twtrl)

    def set_tcke(self, tcke):
        self.wmaa(SET_TCKE, tcke)

    def set_tcwl(self, tcwl):
        self.wmaa(SET_TCWL, tcwl)

    def set_trtp(self, trtp):
        self.wmaa(SET_TRTP, trtp)

    def set_trdrdsc(self, trdrdsc):
        self.wmaa(SET_TRDRDSC, trdrdsc)

    def set_trdrdscl(self, trdrdscl):
        self.wmaa(SET_TRDRDSCL, trdrdscl)

    def set_trdrdsd(self, trdrdsd):
        self.wmaa(SET_TRDRDSD, trdrdsd)

    def set_trdrddd(self, trdrddd):
        self.wmaa(SET_TRDRDDD, trdrddd)

    def set_twrwrsc(self, twrwrsc):
        self.wmaa(SET_TWRWRSC, twrwrsc)

    def set_twrwrscl(self, twrwrscl):
        self.wmaa(SET_TWRWRSCL, twrwrscl)

    def set_twrwrsd(self, twrwrsd):
        self.wmaa(SET_TWRWRSD, twrwrsd)

    def set_twrwrdd(self, twrwrdd):
        self.wmaa(SET_TWRWRDD, twrwrdd)

    def set_trdwr(self, trdwr):
        self.wmaa(SET_TRDWR, trdwr)

    def set_twrrd(self, twrrd):
        self.wmaa(SET_TWRRD, twrrd)


def main():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('--mclk', type=int, help='Set memory clock')
    parser.add_argument('--tcl', type=int, help='Set tCL')
    parser.add_argument('--trcdrd', type=int, help='Set tRCDRD')
    parser.add_argument('--trcdwr', type=int, help='Set tRCDWR')
    parser.add_argument('--tras', type=int, help='Set tRAS')
    parser.add_argument('--trp', type=int, help='Set tRP')
    parser.add_argument('--procodt', type=int, help='Set ProcODT')
    parser.add_argument('--trcpage', type=int, help='Set tRCPAGE')
    parser.add_argument('--trc', type=int, help='Set tRC')
    parser.add_argument('--trfc', type=int, help='Set tRFC')
    parser.add_argument('--trfc2', type=int, help='Set tRFC2')
    parser.add_argument('--trfc4', type=int, help='Set tRFC4')
    parser.add_argument('--tfaw', type=int, help='Set tFAW')
    parser.add_argument('--trrds', type=int, help='Set tRRDS')
    parser.add_argument('--trrdl', type=int, help='Set tRRDL')
    parser.add_argument('--twr', type=int, help='Set tWR')
    parser.add_argument('--twtrs', type=int, help='Set tWTRS')
    parser.add_argument('--twtrl', type=int, help='Set tWTRL')
    parser.add_argument('--tcke', type=int, help='Set tCKE')
    parser.add_argument('--tcwl', type=int, help='Set tCWL')
    parser.add_argument('--trtp', type=int, help='Set tRTP')
    parser.add_argument('--trdrdsc', type=int, help='Set tRDRDSC')
    parser.add_argument('--trdrdscl', type=int, help='Set tRDRDSCL')
    parser.add_argument('--trdrdsd', type=int, help='Set tRDRDSD')
    parser.add_argument('--trdrddd', type=int, help='Set tRDRDDD')
    parser.add_argument('--twrwrsc', type=int, help='Set tWRWRSC')
    parser.add_argument('--twrwrscl', type=int, help='Set tWRWRSCL')
    parser.add_argument('--twrwrsd', type=int, help='Set tWRWRSD')
    parser.add_argument('--twrwrdd', type=int, help='Set tWRWRDD')
    parser.add_argument('--trdwr', type=int, help='Set tRDWR')
    parser.add_argument('--twrrd', type=int, help='Set tWRRD')

    args = parser.parse_args()

    with AOD() as aod:
        for k, v in vars(args).items():
            aod.dispatch(k, v)


if __name__ == '__main__':
    main()

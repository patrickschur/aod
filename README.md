# aod

> **Caution**: Use at your own risk! I'm not responsible for any damage! You could brick your device!

Change memory timings via WMI interface on Linux.

## Requirements

To be able to call ACPI methods, you need to install the kernel module [acpi_call](https://github.com/nix-community/acpi_call).

```shell
sudo apt install acpi-call-dkms
sudo modprobe acpi_call
```

## Usage

```shell
sudo python3 aod.py --help
```

## Options

```txt
--mclk MCLK          Set memory clock
--tcl TCL            Set tCL
--trcdrd TRCDRD      Set tRCDRD
--trcdwr TRCDWR      Set tRCDWR
--tras TRAS          Set tRAS
--trp TRP            Set tRP
--procodt PROCODT    Set ProcODT
--trcpage TRCPAGE    Set tRCPAGE
--trc TRC            Set tRC
--trfc TRFC          Set tRFC
--trfc2 TRFC2        Set tRFC2
--trfc4 TRFC4        Set tRFC4
--tfaw TFAW          Set tFAW
--trrds TRRDS        Set tRRDS
--trrdl TRRDL        Set tRRDL
--twr TWR            Set tWR
--twtrs TWTRS        Set tWTRS
--twtrl TWTRL        Set tWTRL
--tcke TCKE          Set tCKE
--tcwl TCWL          Set tCWL
--trtp TRTP          Set tRTP
--trdrdsc TRDRDSC    Set tRDRDSC
--trdrdscl TRDRDSCL  Set tRDRDSCL
--trdrdsd TRDRDSD    Set tRDRDSD
--trdrddd TRDRDDD    Set tRDRDDD
--twrwrsc TWRWRSC    Set tWRWRSC
--twrwrscl TWRWRSCL  Set tWRWRSCL
--twrwrsd TWRWRSD    Set tWRWRSD
--twrwrdd TWRWRDD    Set tWRWRDD
--trdwr TRDWR        Set tRDWR
--twrrd TWRRD        Set tWRRD
```

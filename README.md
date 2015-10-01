# seabios
Open-source legacy BIOS implementation


--------[Request]--------------------------------------------------------------------------------------------
            

New Bios implementation preparation.




      UNLOCK INTEL ME @
     {0x00000000-0x00000fff}
     {0x00005000-0x005fffff}
     
Reprogram EEPROM CHIP-- flash Programer "Opaque flash chip" {12288 kb}"





    PCI Devices:
      Bus 0, Device 25, Function 0                      Intel 82579LM Gigabit Network Connection
      Bus 0, Device 31, Function 2                      Intel 82801HB(M) ICH8(M) - SATA RAID Controller
      Bus 3, Device 0, Function 0                       Intel Centrino Ultimate-N 6300 AGN 3x3 HMC WiFi Adapter (Dell)
      Bus 0, Device 1, Function 0                       Intel Ivy Bridge - PCI Express Controller
      Bus 0, Device 0, Function 0                       Intel Ivy Bridge-MB - Host Bridge/DRAM Controller
      Bus 0, Device 2, Function 0                       Intel Ivy Bridge-MB - Integrated Graphics Controller (MB GT2)
      Bus 0, Device 27, Function 0                      Intel Panther Point PCH - High Definition Audio Controller [C-1]
      Bus 0, Device 22, Function 0                      Intel Panther Point PCH - Host Embedded Controller Interface 1 (HECI1) [C-1]
      Bus 0, Device 28, Function 0                      Intel Panther Point PCH - PCI Express Port 1
      Bus 0, Device 28, Function 1                      Intel Panther Point PCH - PCI Express Port 2
      Bus 0, Device 28, Function 2                      Intel Panther Point PCH - PCI Express Port 3
      Bus 0, Device 28, Function 3                      Intel Panther Point PCH - PCI Express Port 4
      Bus 0, Device 28, Function 7                      Intel Panther Point PCH - PCI Express Port 8
      Bus 0, Device 31, Function 3                      Intel Panther Point PCH - SMBus Controller [C-1]
      Bus 0, Device 31, Function 6                      Intel Panther Point PCH - Thermal Management Controller [C-1]
      Bus 0, Device 29, Function 0                      Intel Panther Point PCH - USB 2.0 EHCI Controller #1 [C-1]
      Bus 0, Device 26, Function 0                      Intel Panther Point PCH - USB 2.0 EHCI Controller #2 [C-1]
      Bus 0, Device 20, Function 0                      Intel Panther Point PCH - USB 3.0 xHCI Controller [C-1]
      Bus 0, Device 31, Function 0                      Intel QM77 Chipset - LPC Interface Controller [C-1]
      Bus 1, Device 0, Function 0                       nVIDIA Quadro K2000M (Dell) Video Adapter
      Bus 12, Device 0, Function 0                      O2Micro OHCI Compliant IEEE1394 Host Controller
      Bus 12, Device 0, Function 1                      O2Micro OZ600R/OZ900R Integrated MMC/SD Controller

    PnP Devices:
      PNP0C08                                           ACPI Driver/BIOS
      FIXEDBUTTON                                       ACPI Fixed Feature Button
      PNP0C14                                           ACPI Management Interface
      THERMALZONE                                       ACPI Thermal Zone
      PNP0A08                                           ACPI Three-wire Device Bus
      PNP0C0A                                           Control Method Battery
      PNP0C0A                                           Control Method Battery
      DLL053E                                           Dell Touchpad
      PNP0200                                           DMA Controller
      PNP0401                                           ECP Parallel Port
      PNP0C09                                           Embedded Controller Device
      PNP0103                                           High Precision Event Timer
      INT0800                                           Intel Flash EEPROM
      INT3F0D                                           Intel Watchdog Timer
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      GENUINEINTEL_-_INTEL64_FAMILY_6_MODEL_58_-_______INTEL(R)_CORE(TM)_I7-3840QM_CPU_@_2.80GHZIntel(R) Core(TM) i7-3840QM CPU @ 2.80GHz
      PNP0C0D                                           Lid
      ACPI0003                                          Microsoft AC Adapter
      ISATAP                                            Microsoft ISATAP Adapter #2
      ISATAP                                            Microsoft ISATAP Adapter #3
      ISATAP                                            Microsoft ISATAP Adapter #4
      ISATAP                                            Microsoft ISATAP Adapter #5
      ISATAP                                            Microsoft ISATAP Adapter
      TEREDO                                            Microsoft Teredo Tunneling Adapter
      PNP0C04                                           Numeric Data Processor
      PNP0C0C                                           Power Button
      PNP0000                                           Programmable Interrupt Controller
      PNP0B00                                           Real-Time Clock
      PNP0C0E                                           Sleep Button
      DLLK053E                                          Standard PS/2 Keyboard
      SMO8810                                           STMicroelectronics 3-Axis Digital Accelerometer
      PNP0C01                                           System Board Extension
      PNP0C01                                           System Board Extension
      PNP0100                                           System Timer
      PNP0C02                                           Thermal Monitoring ACPI Device
      PNP0C02                                           Thermal Monitoring ACPI Device
      PNP0C02                                           Thermal Monitoring ACPI Device

    LPT PnP Devices:
      MICROSOFTRAWPORT                                  Printer Port Logical Interface

    USB Devices:
      413C 8197                                         Dell Wireless 380 Bluetooth 4.0 Module
      8087 0024                                         Generic USB Hub
      8087 0024                                         Generic USB Hub
      0C45 643F                                         Integrated Webcam
      046D C52B                                         USB Composite Device
      0C45 643F                                         USB Composite Device
      046D C52B                                         USB Input Device (Logitech Download Assistant)
      046D C52B                                         USB Input Device
      046D C52B                                         USB Input Device

    Ports:
      LPT1                                              ECP Printer Port (LPT1)


--------[ Debug - PCI ]-------------------------------------------------------------------------------------------------

    B00 D00 F00:  Intel Ivy Bridge-MB - Host Bridge/DRAM Controller
                  
      Offset 000:  86 80 54 01  06 00 90 20  09 00 00 06  00 00 00 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  E0 00 00 00  00 00 00 00  00 00 00 00 
      Offset 040:  01 90 D1 FE  00 00 00 00  01 00 D1 FE  00 00 00 00 
      Offset 050:  09 02 00 00  19 00 00 00  07 00 90 CF  01 00 00 CD 
      Offset 060:  05 00 00 F8  00 00 00 00  01 80 D1 FE  00 00 00 00 
      Offset 070:  00 00 00 FE  03 00 00 00  00 0C 00 FE  7F 00 00 00 
      Offset 080:  10 11 11 11  01 00 11 00  1A 00 00 00  00 00 00 00 
      Offset 090:  01 00 00 FE  03 00 00 00  01 00 50 2E  04 00 00 00 
      Offset 0A0:  01 00 00 00  04 00 00 00  01 00 60 2E  04 00 00 00 
      Offset 0B0:  01 00 A0 CD  01 00 80 CD  01 00 00 CD  01 00 A0 CF 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  09 00 0C 01  9B 21 00 E2  D0 00 E0 76  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  C8 0F 09 00  00 00 00 00 

    B00 D01 F00:  Intel Ivy Bridge - PCI Express Controller
                  
      Offset 000:  86 80 51 01  07 00 10 00  09 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 01 01 00  E0 E0 00 00 
      Offset 020:  00 F5 00 F6  01 E0 F1 F1  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  88 00 00 00  00 00 00 00  10 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 0A 
      Offset 080:  01 90 03 C8  08 00 00 00  0D 80 00 00  28 10 3E 05 
      Offset 090:  05 A0 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  10 00 42 01  01 80 00 00  20 00 00 00  03 AD 61 02 
      Offset 0B0:  43 00 01 D9  80 25 0C 00  00 00 40 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  0E 00 00 00 
      Offset 0D0:  43 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 01 00  00 00 00 00  01 00 10 00 

    B00 D02 F00:  Intel Ivy Bridge-MB - Integrated Graphics Controller (MB GT2)
                  
      Offset 000:  86 80 66 01  07 04 90 00  09 00 00 03  00 00 00 00 
      Offset 010:  04 00 40 F6  00 00 00 00  0C 00 00 D0  00 00 00 00 
      Offset 020:  01 F0 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  90 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  09 00 0C 01  9B 21 00 E2  D0 00 E0 76  00 00 00 00 
      Offset 050:  09 02 00 00  19 00 00 00  00 00 00 00  01 00 A0 CD 
      Offset 060:  00 00 02 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  05 D0 01 00  0C F0 EF FE  A0 49 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  13 00 06 03  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  01 A4 22 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  01 00 00 00  00 80 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  00 00 09 00  18 70 7D CA 

    B00 D14 F00:  Intel Panther Point PCH - USB 3.0 xHCI Controller [C-1]
                  
      Offset 000:  86 80 31 1E  06 04 90 02  04 30 03 0C  00 00 00 00 
      Offset 010:  04 00 E2 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  70 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  FD 0F 0E 80  39 C2 03 80  00 00 00 00  00 00 00 00 
      Offset 050:  17 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  30 20 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  01 80 C2 C1  08 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 00 B7 00  0C F0 EF FE  00 00 00 00  A8 49 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  8F 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  03 0C 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  0B 00 00 00  0F 00 00 00  0B 00 00 00  0F 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D16 F00:  Intel Panther Point PCH - Host Embedded Controller Interface 1 (HECI1) [C-1]
                  
      Offset 000:  86 80 3A 1E  06 04 10 00  04 00 80 07  00 00 80 00 
      Offset 010:  04 C0 E3 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  50 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  45 02 00 1E  20 00 01 80  06 01 00 69  E0 3F 00 10 
      Offset 050:  01 8C 03 C8  08 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 00 00  00 00 00 00  00 00 00 00  05 00 81 00 
      Offset 090:  0C F0 EF FE  00 00 00 00  90 49 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  02 00 00 C0 
      Offset 0C0:  EE 25 DB 61  73 FA 58 37  E9 3E 3F 7D  B9 36 FB 51 
      Offset 0D0:  81 87 BB B1  C5 09 4E C1  E7 88 18 B0  3F 4F 92 27 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    B00 D19 F00:  Intel 82579LM Gigabit Network Connection
                  
      Offset 000:  86 80 02 15  06 04 10 00  04 00 00 02  00 00 00 00 
      Offset 010:  00 00 E0 F7  00 90 E3 F7  01 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  C8 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  01 D0 22 C8  00 21 00 07 
      Offset 0D0:  05 E0 81 00  00 00 E0 FE  00 00 00 00  80 40 00 00 
      Offset 0E0:  13 00 06 03  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    B00 D1A F00:  Intel Panther Point PCH - USB 2.0 EHCI Controller #2 [C-1]
                  
      Offset 000:  86 80 2D 1E  06 00 90 02  04 20 03 0C  00 00 00 00 
      Offset 010:  00 80 E3 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  50 00 00 00  00 00 00 00  10 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  01 58 C2 C9  00 00 00 00  0A 98 A0 20  00 00 00 00 
      Offset 060:  20 20 FF 07  00 00 00 00  01 00 00 01  00 20 00 00 
      Offset 070:  00 00 DF 3F  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 80 00  11 88 0C 93  30 0D 00 24  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  13 00 06 03  00 01 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 AA FF 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  04 30 67 CB 
      Offset 0F0:  00 00 00 00  88 85 80 00  87 0F 05 08  08 17 5B 20 

    B00 D1B F00:  Intel Panther Point PCH - High Definition Audio Controller [C-1]
                  
      Offset 000:  86 80 20 1E  06 00 10 00  04 00 03 04  10 00 00 00 
      Offset 010:  04 00 E3 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  50 00 00 00  00 00 00 00  16 01 00 00 
      Offset 040:  01 00 00 05  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  01 60 42 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  05 70 80 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  10 00 91 00  00 00 00 10  00 08 10 00  00 00 00 00 
      Offset 080:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 04 02 01  00 24 00 40  00 0C A3 82  10 00 33 02 
      Offset 0D0:  00 0C A3 02  10 00 33 02  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1C F00:  Intel Panther Point PCH - PCI Express Port 1
                  
      Offset 000:  86 80 10 1E  04 00 10 00  C4 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 02 02 00  F0 00 00 20 
      Offset 020:  F0 FF 00 00  F1 FF 01 00  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  40 00 00 00  00 00 00 00  10 01 00 00 
      Offset 040:  10 80 42 01  00 80 00 00  00 00 10 00  12 4C 12 01 
      Offset 050:  03 00 01 10  00 B2 04 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  16 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  02 00 01 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 90 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  0D A0 00 00  28 10 3E 05  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 00 02 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 01  02 0B 00 00  00 80 11 81  00 00 00 00 
      Offset 0E0:  00 3F 00 00  00 00 00 00  03 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1C F01:  Intel Panther Point PCH - PCI Express Port 2
                  
      Offset 000:  86 80 12 1E  06 00 10 00  C4 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 03 03 00  F0 00 00 00 
      Offset 020:  D0 F7 D0 F7  F1 FF 01 00  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  40 00 00 00  00 00 00 00  11 02 00 00 
      Offset 040:  10 80 42 01  00 80 00 00  00 00 10 00  12 3C 12 02 
      Offset 050:  42 00 11 70  00 B2 0C 00  00 00 40 00  00 00 00 00 
      Offset 060:  00 00 00 00  16 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  02 00 01 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 90 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  0D A0 00 00  28 10 3E 05  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 00 02 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 01  02 0B 00 00  00 80 11 81  00 00 00 00 
      Offset 0E0:  00 03 00 00  00 00 00 00  01 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1C F02:  Intel Panther Point PCH - PCI Express Port 3
                  
      Offset 000:  86 80 14 1E  07 00 10 00  C4 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 04 07 00  D0 D0 00 20 
      Offset 020:  20 F7 B0 F7  B1 F2 41 F3  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  40 00 00 00  00 00 00 00  12 03 00 00 
      Offset 040:  10 80 42 01  00 80 00 00  00 00 10 00  12 4C 12 03 
      Offset 050:  03 00 01 10  60 B2 14 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  16 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  02 00 01 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 90 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  0D A0 00 00  28 10 3E 05  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 00 02 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 01  00 0B 00 00  02 80 11 C1  00 00 00 00 
      Offset 0E0:  00 03 00 00  00 00 00 00  03 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1C F03:  Intel Panther Point PCH - PCI Express Port 4
                  
      Offset 000:  86 80 16 1E  07 00 10 00  C4 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 08 0B 00  C0 C0 00 20 
      Offset 020:  80 F6 10 F7  11 F2 A1 F2  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  40 00 00 00  00 00 00 00  13 04 00 00 
      Offset 040:  10 80 42 01  00 80 00 00  00 00 10 00  12 4C 12 04 
      Offset 050:  00 00 01 10  60 B2 1C 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  16 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  02 00 01 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 90 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  0D A0 00 00  28 10 3E 05  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 00 02 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 01  00 0B 00 00  02 80 11 C1  00 00 00 00 
      Offset 0E0:  00 03 00 00  00 00 00 00  01 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1C F07:  Intel Panther Point PCH - PCI Express Port 8
                  
      Offset 000:  86 80 1E 1E  06 00 10 00  C4 00 04 06  10 00 81 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 0C 0C 00  F0 00 00 20 
      Offset 020:  C0 F7 C0 F7  F1 FF 01 00  00 00 00 00  00 00 00 00 
      Offset 030:  00 00 00 00  40 00 00 00  00 00 00 00  13 04 00 00 
      Offset 040:  10 80 42 01  00 80 00 00  00 00 10 00  12 4C 12 08 
      Offset 050:  03 00 11 30  00 B2 3C 00  00 00 40 00  00 00 00 00 
      Offset 060:  00 00 00 00  16 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  02 00 01 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 90 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  0D A0 00 00  28 10 3E 05  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 00 02 C8  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 01  02 0B 00 00  00 80 11 81  00 00 00 00 
      Offset 0E0:  00 03 00 00  00 00 00 00  01 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1D F00:  Intel Panther Point PCH - USB 2.0 EHCI Controller #1 [C-1]
                  
      Offset 000:  86 80 26 1E  06 00 90 02  04 20 03 0C  00 00 00 00 
      Offset 010:  00 70 E3 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  50 00 00 00  00 00 00 00  15 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  01 58 C2 C9  00 00 00 00  0A 98 A0 20  00 00 00 00 
      Offset 060:  20 20 FF 07  00 00 00 00  01 00 00 01  00 20 00 00 
      Offset 070:  00 00 DF 3F  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 80 00  11 88 0C 93  30 0D 00 24  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  13 00 06 03  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 AA FF 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  84 20 8B C7 
      Offset 0F0:  00 00 00 00  88 85 80 00  87 0F 05 08  08 17 5B 20 

    B00 D1F F00:  Intel QM77 Chipset - LPC Interface Controller [C-1]
                  
      Offset 000:  86 80 55 1E  07 00 10 02  04 00 01 06  00 00 80 00 
      Offset 010:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  E0 00 00 00  00 00 00 00  00 00 00 00 
      Offset 040:  01 04 00 00  80 00 00 00  01 05 00 00  10 00 00 00 
      Offset 050:  F8 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  8B 8A 8A 85  D0 00 00 00  83 85 8B 80  F8 F0 00 00 
      Offset 070:  78 F0 78 F0  78 F0 78 F0  78 F0 78 F0  78 F0 78 F0 
      Offset 080:  00 00 0F 1C  81 06 7C 00  21 09 5C 00  E1 07 3C 00 
      Offset 090:  00 00 00 00  00 0F 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  14 0E A0 00  49 18 06 00  00 47 00 00  00 00 01 82 
      Offset 0B0:  00 00 00 00  00 00 00 00  02 00 00 10  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  33 22 11 00  67 45 00 00  CF FF 00 00  0A 00 00 00 
      Offset 0E0:  09 00 0C 10  00 00 00 00  B3 02 E4 06  00 00 00 00 
      Offset 0F0:  01 C0 D1 FE  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1F F02:  Intel 82801HB(M) ICH8(M) - SATA RAID Controller
                  
      Offset 000:  86 80 2A 28  07 00 B0 02  04 00 04 01  00 00 00 00 
      Offset 010:  D1 F0 00 00  C1 F0 00 00  B1 F0 00 00  A1 F0 00 00 
      Offset 020:  61 F0 00 00  00 60 E3 F7  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  80 00 00 00  00 00 00 00  13 02 00 00 
      Offset 040:  00 80 00 80  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  01 A8 03 40  08 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 70 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  A0 06 39 89  83 01 00 06  08 42 5C 01  00 00 00 00 
      Offset 0A0:  E0 00 00 00  39 00 00 00  12 B0 10 00  48 00 00 00 
      Offset 0B0:  13 00 06 03  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1F F03:  Intel Panther Point PCH - SMBus Controller [C-1]
                  
      Offset 000:  86 80 22 1E  03 00 80 02  04 00 05 0C  00 00 00 00 
      Offset 010:  04 50 E3 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  41 F0 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  00 00 00 00  00 00 00 00  0A 03 00 00 
      Offset 040:  01 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  03 04 04 00  00 00 08 08  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  04 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B00 D1F F06:  Intel Panther Point PCH - Thermal Management Controller [C-1]
                  
      Offset 000:  86 80 24 1E  00 00 10 00  04 00 80 11  00 00 00 00 
      Offset 010:  04 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  50 00 00 00  00 00 00 00  0A 03 00 00 
      Offset 040:  05 00 A0 CF  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  01 00 23 00  08 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  05 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  87 0F 05 08  00 00 00 00 

    B01 D00 F00:  nVIDIA Quadro K2000M (Dell) Video Adapter
                  
      Offset 000:  DE 10 FB 0F  06 00 10 00  A1 00 00 03  10 00 00 00 
      Offset 010:  00 00 00 F5  0C 00 00 E0  00 00 00 00  0C 00 00 F0 
      Offset 020:  00 00 00 00  81 EF 00 00  00 00 00 00  28 10 3E 15 
      Offset 030:  00 00 00 00  60 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  28 10 3E 15  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  01 00 00 00  01 00 00 00  CE D6 23 00  00 00 00 00 
      Offset 060:  01 68 03 00  08 00 00 00  05 78 81 00  0C F0 EF FE 
      Offset 070:  00 00 00 00  70 49 00 00  10 B4 02 00  E1 8D 2C 01 
      Offset 080:  30 29 00 00  02 BD 47 00  43 01 01 11  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  13 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  02 00 21 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  09 00 14 01  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0F0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    B03 D00 F00:  Intel Centrino Ultimate-N 6300 AGN 3x3 HMC WiFi Adapter (Dell)
                  
      Offset 000:  86 80 2B 42  06 04 10 00  35 00 80 02  10 00 00 00 
      Offset 010:  04 00 D0 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  86 80 21 11 
      Offset 030:  00 00 00 00  C8 00 00 00  00 00 00 00  00 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 070:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 080:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 090:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  01 D0 23 C8  00 00 00 0D 
      Offset 0D0:  05 E0 81 00  0C F0 EF FE  00 00 00 00  B0 49 00 00 
      Offset 0E0:  10 00 01 00  C0 8E 00 10  00 08 19 00  11 9C 06 00 
      Offset 0F0:  42 00 11 10  00 00 00 00  00 00 00 00  00 00 00 00 

    B0C D00 F00:  O2Micro OHCI Compliant IEEE1394 Host Controller
                  
      Offset 000:  17 12 F7 13  06 00 10 00  05 10 00 0C  10 00 80 00 
      Offset 010:  00 30 C0 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  A0 00 00 00  00 00 00 00  13 01 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 80 80 01  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  68 98 00 00  28 00 FF 38  F0 68 7E 77  18 27 18 27 
      Offset 070:  18 1D 80 00  28 78 18 2F  00 00 00 00  00 00 00 00 
      Offset 080:  10 00 01 00  80 8D 90 05  00 08 09 00  11 8C 07 00 
      Offset 090:  03 01 11 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 80 03 FE  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  10 55 1E 00  00 00 00 00 
      Offset 0D0:  00 00 00 80  08 C3 16 02  04 00 00 00  94 21 2F 04 
      Offset 0E0:  7A CB 05 00  64 00 00 48  00 02 10 1F  C4 67 00 0D 
      Offset 0F0:  40 A8 12 E0  F9 7B 80 84  07 7F 00 40  48 C0 06 81 

    B0C D00 F01:  O2Micro OZ600R/OZ900R Integrated MMC/SD Controller
                  
      Offset 000:  17 12 21 83  06 00 10 00  05 01 05 08  10 00 80 00 
      Offset 010:  00 20 C0 F7  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 020:  00 00 00 00  00 00 00 00  00 00 00 00  28 10 3E 05 
      Offset 030:  00 00 00 00  A0 00 00 00  00 00 00 00  10 02 00 00 
      Offset 040:  00 00 00 00  00 00 00 00  00 80 80 01  00 00 00 00 
      Offset 050:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 060:  68 98 00 00  28 00 FF 38  F0 68 7E 77  18 27 18 27 
      Offset 070:  18 1D 80 00  28 78 18 2F  00 00 00 00  00 00 00 00 
      Offset 080:  10 00 01 00  80 8D 90 05  00 28 09 00  11 8C 07 00 
      Offset 090:  03 01 11 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0A0:  01 80 03 FE  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 0C0:  00 00 00 00  00 00 00 00  10 55 1E 00  00 00 00 00 
      Offset 0D0:  00 00 00 80  08 C3 16 02  04 00 00 00  94 21 2F 04 
      Offset 0E0:  7A CB 05 00  64 00 00 48  00 02 10 1F  C4 67 00 0D 
      Offset 0F0:  40 A8 12 E0  F9 7B 80 84  07 7F 00 40  48 C0 06 81 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4000:  BB 8B 1C 00  65 64 18 8C  20 22 04 0A  B4 58 00 00 
      Offset 4010:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 10 00 
      Offset 4020:  05 00 10 00  2A 2A 2A 2A  33 33 0E 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4280:  00 00 00 00  00 00 04 00  00 00 00 00  44 00 00 00 
      Offset 4290:  80 40 00 00  FF 98 00 00  60 18 80 6C  D8 04 00 00 
      Offset 42A0:  0F 10 00 00  00 82 F8 41  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4400:  BB 8B 1C 00  65 64 18 8C  20 22 04 0A  B4 58 00 00 
      Offset 4410:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 10 00 
      Offset 4420:  05 00 10 00  2A 2A 2A 2A  33 33 0E 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4680:  00 00 00 00  00 00 04 00  00 00 00 00  44 00 00 00 
      Offset 4690:  80 40 00 00  FF 98 00 00  60 18 80 6C  D8 04 00 00 
      Offset 46A0:  0F 10 00 00  00 82 F8 41  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4800:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 4810:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 4A80:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 4A90:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 5000:  24 00 00 00  10 10 66 00  10 10 66 00  00 00 60 00 
      Offset 5010:  00 00 00 00  00 00 40 20  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 5880:  E7 71 91 CA  00 00 00 00  D0 DA E4 00  00 00 00 00 
      Offset 5890:  51 1A 1C 00  0B BC 1D 00  00 00 00 00  00 00 00 00 
      Offset 58A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 58B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 58C0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 58D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 58E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 58F0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 5900:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 5910:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 5920:  00 00 00 00  18 00 00 00  B4 EB 96 06  3B CD 09 00 
      Offset 5930:  68 01 20 01  00 00 00 00  03 10 0A 00  0D 72 BC 09 
      Offset 5940:  71 8E A6 00  14 D1 00 00  00 07 00 00  00 00 00 00 
      Offset 5950:  00 00 00 00  00 00 10 00  00 1C 01 F0  00 0C 08 00 
      Offset 5960:  5D 28 4D 01  E8 C1 79 51  28 B4 79 51  BC BD B5 A5 
      Offset 5970:  74 74 7A 03  74 74 7A 03  52 00 00 00  52 00 00 00 
      Offset 5980:  52 00 00 00  C7 31 4E 2D  00 00 00 00  00 00 00 00 
      Offset 5990:  FF 00 00 00  FF 00 00 00  1A 0D 07 00  00 12 69 00 
      Offset 59A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 59B0:  80 03 00 80  94 14 14 18  70 01 00 80  94 14 14 18 
      Offset 59C0:  00 00 17 88  00 00 00 00  00 00 00 00  00 00 00 00 

    PCI-8086-0154:  Intel SNB/IVB/HSW/CRW/BDW/SKL MCHBAR @ FED10000h
                  
      Offset 5E00:  06 00 00 00  06 00 00 00  00 00 00 00  00 00 00 00 
      Offset 5E10:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 

    PCI-8086-1E24:  Intel 5/6/7/8/9/10-series PCH TBARB @ CFA00000h
                  
      Offset 00:  00 BA 01 DF  2B 3A 00 00  FD 04 5D 00  00 00 C0 00 
      Offset 10:  00 00 40 1A  87 DE 8C 80  00 00 00 00  00 00 00 00 
      Offset 20:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 30:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 80 
      Offset 40:  00 02 00 FF  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 50:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 60:  00 00 00 00  00 00 00 00  00 00 00 00  20 1B 16 05 
      Offset 70:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset 80:  00 00 00 04  61 61 00 FF  00 00 00 00  00 00 00 00 
      Offset 90:  C8 8F 10 15  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset A0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset B0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset C0:  00 00 00 00  00 00 00 FF  00 00 00 00  00 00 00 00 
      Offset D0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset E0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 
      Offset F0:  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00 


--------[ Debug - Video BIOS ]------------------------------------------------------------------------------------------

    C000:0000  U.x...000000000000.$..#.@...00IBM VGA Compatible BIOS. .n.~.....
    C000:0040  PCIR............................&.V.f.v.....n...................
    C000:0080  ..........7............................................DH.....DH
    C000:00C0  .....DH....0DH.....DI.....DI.....DJ.....DJ....0DJ.....DI....0DI.
    C000:0100  ....DJ.....DK.....DK.....DK....0.L......L......L....0.L......M..
    C000:0140  ....M.....0.D..2.h..4....8....:....<....A.D..C.h..E....I....K...
    C000:0180  .M....P D..R h..T ...X ...Z ...\ ...`.T..a.T..b T..c.n..d.n..e n
    C000:01C0  ..f....g....h ...i....j....k ...l....m....n ...o....p....q ...}.
    C000:0200  ...~.... ........ .-..`............ .1..l...........rQ.. n(U...
    C000:0240  !....... ....`"........... ....@.......... .1X. (.........V. .1X
    C000:0280  . .P........d..@A.&0..6.......... A. 0.`........0*..Q.*@0p......
    C000:02C0  ...4..Q.*@..........H?@0b.2@@.........h[..r.<P..................
    C000:0300  ..E............................................E................
    C000:0340  ...................For Evaluation Use Only....(........c-'(.+...
    C000:0380  ..............................................(........c-'(.+...
    C000:03C0  ..............................................P........c_OP.U...


--------[ Debug - Unknown ]---------------------------------------------------------------------------------------------

    FW PHY          Unknown (00000CC2-00401105)


------------------------------------------------------------------------------------------------------------------------

The names of actual companies and products mentioned herein may be the trademarks of their respective owners.

# CW-Mapfile-to-CSV
*By ReaZ0n23*  

## What's this?
CodeWarriorで生成されたMapFileをcsv形式に変換するスクリプトです。  
Wii向けのゲームソフトのMapFileで動作確認しています。

## Usage
スクリプトファイル本体と同じディレクトリに.mapファイルを配置することで動作します。出力ファイルも同様に、同じディレクトリに生成します。

## Example
以下は使用例です。  
*sample.map*
```
.init section layout
  Starting        Virtual  File
  address  Size   address  offset
  ---------------------------------
  00000000 000380 80004000 000001e0  1 .init 	Runtime.PPCEABI.H.a __mem.o
  00000000 00029c 80004000 000001e0  4 memcpy 	Runtime.PPCEABI.H.a __mem.o
  0000029c 0000b4 8000429c 0000047c  4 __fill_mem 	Runtime.PPCEABI.H.a __mem.o
  00000350 000030 80004350 00000530  4 memset 	Runtime.PPCEABI.H.a __mem.o
  00000380 001f34 80004380 00000560  1 .init 	TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o
  00000380 000000 80004380 00000560    gTRKInterruptVectorTable (entry of .init) 	TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o
  000022b4 000000 800062b4 00002494    gTRKInterruptVectorTableEnd (entry of .init) 	TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o
  000022b4 00000c 800062c0 000024a0 16 *fill*
  000022c0 00035c 800062c0 000024a0  1 .init 	os.a __start.o
  000022c0 000028 800062c0 000024a0 16 __check_pad3 	os.a __start.o
  000022f0 00000c 800062f0 000024d0 16 __set_debug_bba 	os.a __start.o
  00002300 000008 80006300 000024e0 16 __get_debug_bba 	os.a __start.o
  00002310 000168 80006310 000024f0 16 __start 	os.a __start.o
  00002480 000044 80006480 00002660 16 __my_flush_cache 	os.a __start.o
  000024d0 000090 800064d0 000026b0 16 __init_registers 	os.a __start.o
  00002560 0000bc 80006560 00002740 16 __init_data 	os.a __start.o
  0000261c 000004 80006620 00002800 16 *fill*
  00002620 000064 80006620 00002800  1 .init 	os.a __ppc_eabi_init.o
  00002620 000024 80006620 00002800 16 __init_hardware 	os.a __ppc_eabi_init.o
  00002650 000034 80006650 00002830 16 __flush_cache 	os.a __ppc_eabi_init.o
  00002684 0000a4 80006684 00002864  1 .init 	Linker Generated Symbol File 
  00002684 000084 80006684 00002864  4 _rom_copy_info 	Linker Generated Symbol File 
  00002708 000020 80006708 000028e8  4 _bss_init_info 	Linker Generated Symbol File 
```
sample.map.csv
```
Section,Address,VirtualAddress,Symbol,ObjectFile,Size(Bytes)
.init,0x00000000,0x80004000,.init,Runtime.PPCEABI.H.a __mem.o,896
.init,0x00000000,0x80004000,memcpy,Runtime.PPCEABI.H.a __mem.o,668
.init,0x0000029c,0x8000429c,__fill_mem,Runtime.PPCEABI.H.a __mem.o,180
.init,0x00000350,0x80004350,memset,Runtime.PPCEABI.H.a __mem.o,48
.init,0x00000380,0x80004380,.init,TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o,7988
.init,0x00000380,0x80004380,gTRKInterruptVectorTable (entry of .init),TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o,0
.init,0x000022b4,0x800062b4,gTRKInterruptVectorTableEnd (entry of .init),TRK_Hollywood_Revolution.a D:\Data\wiiProj\metrotrk\metrotrk\__exception.o,0
.init,0x000022c0,0x800062c0,.init,os.a __start.o,860
.init,0x000022c0,0x800062c0,__check_pad3,os.a __start.o,40
.init,0x000022f0,0x800062f0,__set_debug_bba,os.a __start.o,12
.init,0x00002300,0x80006300,__get_debug_bba,os.a __start.o,8
.init,0x00002310,0x80006310,__start,os.a __start.o,360
.init,0x00002480,0x80006480,__my_flush_cache,os.a __start.o,68
.init,0x000024d0,0x800064d0,__init_registers,os.a __start.o,144
.init,0x00002560,0x80006560,__init_data,os.a __start.o,188
.init,0x00002620,0x80006620,.init,os.a __ppc_eabi_init.o,100
.init,0x00002620,0x80006620,__init_hardware,os.a __ppc_eabi_init.o,36
.init,0x00002650,0x80006650,__flush_cache,os.a __ppc_eabi_init.o,52
.init,0x00002684,0x80006684,.init,Linker Generated Symbol File,164
.init,0x00002684,0x80006684,_rom_copy_info,Linker Generated Symbol File,132
.init,0x00002708,0x80006708,_bss_init_info,Linker Generated Symbol File,32
```

## Change Log
**v1.0**
 - First Release

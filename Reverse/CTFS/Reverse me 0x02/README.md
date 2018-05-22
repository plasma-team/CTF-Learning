## Reverse me 0x02 (Reverse)
Look at the dissas

### Reference
- https://www.perspectiverisk.com/intro-to-basic-disassembly-reverse-engineering/
- https://www.tutorialspoint.com/assembly_programming/index.htm
- https://github.com/longld/peda

### Proof of Concept
Disini saya menggunakan GDB-PEDA, untuk installasinya bisa langsung ke https://github.com/longld/peda

- Step by Step
	- Dari clue diatas `look at the dissas` langsung saja gass :horse_racing:
	- Langkah pertama harus dilakukan iyalah mengecek keseluruhan fungsi dari program
	```
	gdb-peda$ info functions 
	All defined functions:
	Non-debugging symbols:
	0x08048320  _init
	0x08048360  puts@plt
	0x08048370  __gmon_start__@plt
	0x08048380  __libc_start_main@plt
	0x08048390  fprintf@plt
	0x080483a0  _start
	0x080483d0  __do_global_dtors_aux
	0x08048430  frame_dummy
	0x08048454  notmain
	0x080484d0  main
	0x08048510  __libc_csu_init
	0x08048580  __libc_csu_fini
	0x08048582  __i686.get_pc_thunk.bx
	0x08048590  __do_global_ctors_aux
	0x080485bc  _fini
	```
	- Kita disassembly fungsi ```main``` terlebih dahulu
	```
	gdb-peda$ pdisass main
	Dump of assembler code for function main:
	   0x080484d0 <+0>:	push   ebp
	   0x080484d1 <+1>:	mov    ebp,esp
	   0x080484d3 <+3>:	and    esp,0xfffffff0
	   0x080484d6 <+6>:	sub    esp,0x10
	   0x080484d9 <+9>:	cmp    DWORD PTR [ebp+0x8],0x1
	   0x080484dd <+13>:	jle    0x80484f1 <main+33>
	   0x080484df <+15>:	mov    eax,DWORD PTR [ebp+0xc]
	   0x080484e2 <+18>:	add    eax,0x4
	   0x080484e5 <+21>:	mov    eax,DWORD PTR [eax]
	   0x080484e7 <+23>:	mov    DWORD PTR [esp],eax
	   0x080484ea <+26>:	call   0x8048454 <notmain>
	   0x080484ef <+31>:	jmp    0x80484fe <main+46>
	   0x080484f1 <+33>:	nop
	   0x080484f2 <+34>:	mov    DWORD PTR [esp],0x80485e0
	   0x080484f9 <+41>:	call   0x8048360 <puts@plt>
	   0x080484fe <+46>:	mov    eax,0x0
	   0x08048503 <+51>:	leave  
	   0x08048504 <+52>:	ret    
	End of assembler dump.
	```
	- Dari address ```0x080484ea``` terdapat perintah call fungsi ```notmain```
	- Lanjut kita kepoin fungsi ```notmain```
	```
	gdb-peda$ pdisass notmain
	Dump of assembler code for function notmain:
	   0x08048454 <+0>:	push   ebp
	   0x08048455 <+1>:	mov    ebp,esp
	   0x08048457 <+3>:	push   edi
	   0x08048458 <+4>:	push   ebx
	   0x08048459 <+5>:	sub    esp,0x30
	   0x0804845c <+8>:	mov    DWORD PTR [ebp-0xc],0x0
	   0x08048463 <+15>:	jmp    0x8048482 <notmain+46>
	   0x08048465 <+17>:	mov    eax,DWORD PTR [ebp-0xc]
	   0x08048468 <+20>:	add    eax,0x804a018
	   0x0804846d <+25>:	movzx  eax,BYTE PTR [eax]
	   0x08048470 <+28>:	xor    eax,0x33
	   0x08048473 <+31>:	mov    edx,DWORD PTR [ebp-0xc]
	   0x08048476 <+34>:	add    edx,0x804a018
	   0x0804847c <+40>:	mov    BYTE PTR [edx],al
	   0x0804847e <+42>:	add    DWORD PTR [ebp-0xc],0x1
	   0x08048482 <+46>:	cmp    DWORD PTR [ebp-0xc],0x10
	   0x08048486 <+50>:	jle    0x8048465 <notmain+17>
	   0x08048488 <+52>:	mov    ebx,0x804a018
	   0x0804848d <+57>:	mov    eax,DWORD PTR [ebp+0x8]
	   0x08048490 <+60>:	mov    DWORD PTR [ebp-0x1c],0xffffffff
	   0x08048497 <+67>:	mov    edx,eax
	   0x08048499 <+69>:	mov    eax,0x0
	   0x0804849e <+74>:	mov    ecx,DWORD PTR [ebp-0x1c]
	   0x080484a1 <+77>:	mov    edi,edx
	   0x080484a3 <+79>:	repnz scas al,BYTE PTR es:[edi]
	   0x080484a5 <+81>:	mov    eax,ecx
	   0x080484a7 <+83>:	not    eax
	   0x080484a9 <+85>:	sub    eax,0x1
	   0x080484ac <+88>:	cmp    eax,0x35
	   0x080484af <+91>:	jne    0x80484b8 <notmain+100>
	   0x080484b1 <+93>:	mov    eax,ds:0x804a060
	   0x080484b6 <+98>:	jmp    0x80484bd <notmain+105>
	   0x080484b8 <+100>:	mov    eax,ds:0x804a040
	   0x080484bd <+105>:	mov    DWORD PTR [esp+0x4],ebx
	   0x080484c1 <+109>:	mov    DWORD PTR [esp],eax
	   0x080484c4 <+112>:	call   0x8048390 <fprintf@plt>
	   0x080484c9 <+117>:	add    esp,0x30
	   0x080484cc <+120>:	pop    ebx
	   0x080484cd <+121>:	pop    edi
	   0x080484ce <+122>:	pop    ebp
	   0x080484cf <+123>:	ret    
	End of assembler dump.
	```
	- Pada address ```0x080484ac``` terdapat cmp yang membandingkan antara ```eax,0x35```
	- Lanjut kita taruh breakpoint di address tersebut ```0x080484ac```
	```
	gdb-peda$ b *0x080484ac
	Breakpoint 1 at 0x80484ac
	```
	- Setelah di jalankan program hanya mengeluarkan output ```Temukan Flag!!``` setelah ditelusuri menggunakan IDA, ternyata dari fungsi ```main``` meminta ```argv``` tambahan agar fungsi ```notmain``` dapat terpanggil.
	```
	int __cdecl main(int argc, const char **argv, const char **envp)
	{
	  if ( argc <= 1 )
	    puts("Temukan Flag!!");
	  else
	    notmain(argv[1]);
	  return 0;
	}
	```
	
- Capture the flag :triangular_flag_on_post:
```
gdb-peda$ run
gdb-peda$ x/s 0x804a018
0x804a018 <szflag.1854>:	**censored**
```
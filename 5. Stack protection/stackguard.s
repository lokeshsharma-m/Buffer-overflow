	.file	"stackguard.c"
	.comm	secret,4,4
	.section	.rodata
.LC0:
	.string	"copied successfully"
.LC1:
	.string	"stack overflow is detected"
	.text
	.globl	fun
	.type	fun, @function
fun:
.LFB2:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$24, %esp
	  //secret value is stored in between the buffer and ebp
	movl	secret, %eax
	movl	%eax, -12(%ebp)
	subl	$8, %esp
	pushl	8(%ebp)
	leal	-24(%ebp), %eax
	pushl	%eax
	call	strcpy
	addl	$16, %esp
	 //secret value is checked with stack guard
	movl	secret, %eax
	cmpl	%eax, -12(%ebp)
	jne	.L2
	subl	$12, %esp
	pushl	$.LC0
	call	puts
	addl	$16, %esp
	jmp	.L3
.L2:
	subl	$12, %esp
	pushl	$.LC1
	call	puts
	addl	$16, %esp
	subl	$12, %esp
	pushl	$1
	call	exit
.L3:
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE2:
	.size	fun, .-fun
	.section	.rodata
.LC2:
	.string	"enter the input:"
	.text
	.globl	main
	.type	main, @function
main:
.LFB3:
	.cfi_startproc
	leal	4(%esp), %ecx
	.cfi_def_cfa 1, 0
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	movl	%esp, %ebp
	pushl	%ecx
	.cfi_escape 0xf,0x3,0x75,0x7c,0x6
	subl	$68, %esp
	call	rand
	movl	%eax, secret
	subl	$12, %esp
	pushl	$.LC2
	call	puts
	addl	$16, %esp
	subl	$12, %esp
	leal	-68(%ebp), %eax
	pushl	%eax
	call	gets
	addl	$16, %esp
	subl	$12, %esp
	leal	-68(%ebp), %eax
	pushl	%eax
	call	fun
	addl	$16, %esp
	movl	$0, %eax
	movl	-4(%ebp), %ecx
	.cfi_def_cfa 1, 0
	leave
	.cfi_restore 5
	leal	-4(%ecx), %esp
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE3:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
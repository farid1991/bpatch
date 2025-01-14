;arm
include "x.inc"

        code16

        adr r0,.1
        bx r0
.1:

        code32
; test_clean_d_cache(); */
; .2: on page 2-24 */
.2:
        MRC p15, 0, r15, c7, c10, 3 ; test and clean
        BNE .2

; drain_write_buffer(); */
        MOV R0,0
        MCR p15, 0, R0, c7, c10, 4

; invalidate_i_cache(); */
        MOV R0,0
        MCR p15, 0, R0, c7, c5, 0

        adr r0,.3+1
        bx r0

        code16
.3:
        mov r0,r5
        add r0,0x10
        mov r1,r6
        add r1,0x10
        blx r1
        nop

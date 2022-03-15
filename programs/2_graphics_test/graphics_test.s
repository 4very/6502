LCD = $6000

SPAGEADDR = %10110000 ; LCD 010
SUCOLADDR = %00010000 ; LCD 010
SLCOLADDR = %00000000 ; LCD 010
WRITE = %110




    .org $8000







;----------------------------------------------------------------------
;
; 0x0001: start page
; 0x0002: start column (upper)
; 0x0003: start column (lower)

; 0x0004: start addr
; 0x0005: end addr


lcd_write:
    lda #$00
    sta $0003

    ldx #$00
new_col:
    jsr setcoladdr
    ldy #$00

new_row:
    jsr setpageaddr
    jsr setpxl

    inc $0003
    iny

    cpy #$4
    bne new_row

	inx
    cpx #32
    bne new_col

    
exit:
    lda #$FF
    sta $0000

setcoladdr: 
    ; transfer x to coladdr of lcd
    pha
    stx $0001

    lda $0001
    and #%11110000
    ror
    ror
    ror
    ror
    ORA #%00010000
    sta $6002

    lda $0001
    and #%00001111
    ora #%00000000
	beq TEMP_FOR_EMULATOR
    sta $6002

    pla
    rts

TEMP_FOR_EMULATOR:
	lda #%10101110
	sta $6002

	pla
	rts

setpageaddr:
    ; transfer y to pageaddr of lcd
    pha
    sty $0001

    lda $0001
    and #%00001111
    ora #%10110000
    sta $6002

    pla
    rts


setpxl:
    pha

    stx $0004
    stx $0002

    asl $0004
    asl $0004

    lda $0004
    sty $0003
    ora $0003

    sta $0004
    ldx $0004

    lda $9000,x
    sta $6006

    ldx $0002
    pla
    rts



    .org $9000
	.byte %11000000
	.byte %00011111
	.byte %00000000
	.byte %00000000
	.byte %00110000
	.byte %11100000
	.byte %00000001
	.byte %00000000
	.byte %00001000
	.byte %00000000
	.byte %00000110
	.byte %00000000
	.byte %00000100
	.byte %00000000
	.byte %00011000
	.byte %00000000
	.byte %00000010
	.byte %00000000
	.byte %00100000
	.byte %00000000
	.byte %00000010
	.byte %00000100
	.byte %01000000
	.byte %00000000
	.byte %00000001
	.byte %00000111
	.byte %10000000
	.byte %00000000
	.byte %11100001
	.byte %00000001
	.byte %00000000
	.byte %00000011
	.byte %00111001
	.byte %00000001
	.byte %00000000
	.byte %00000010
	.byte %11100001
	.byte %00000001
	.byte %00000000
	.byte %00000100
	.byte %10000010
	.byte %00000111
	.byte %00000000
	.byte %00001000
	.byte %00000100
	.byte %00000100
	.byte %00000000
	.byte %00010000
	.byte %00000100
	.byte %01000000
	.byte %00000000
	.byte %00100000
	.byte %00011000
	.byte %11110000
	.byte %00000001
	.byte %01000000
	.byte %00100000
	.byte %01000000
	.byte %00000000
	.byte %01000000
	.byte %11000000
	.byte %01000001
	.byte %00000000
	.byte %10000000
	.byte %11000000
	.byte %00000000
	.byte %00000000
	.byte %10000000
	.byte %00100000
	.byte %00000000
	.byte %00000000
	.byte %01000000
	.byte %00011000
	.byte %00000000
	.byte %00000000
	.byte %01000000
	.byte %00000100
	.byte %00000000
	.byte %00000000
	.byte %00100000
	.byte %00000100
	.byte %00000000
	.byte %00000000
	.byte %00010000
	.byte %10000010
	.byte %01111111
	.byte %00000000
	.byte %00001000
	.byte %00000001
	.byte %01000010
	.byte %00000000
	.byte %00001000
	.byte %00000001
	.byte %01000010
	.byte %00000000
	.byte %00000100
	.byte %00000001
	.byte %01111110
	.byte %00000000
	.byte %00000011
	.byte %00000001
	.byte %00000000
	.byte %10000000
	.byte %00000000
	.byte %00000001
	.byte %00000000
	.byte %01000000
	.byte %00000000
	.byte %00000010
	.byte %00000000
	.byte %00110000
	.byte %00000000
	.byte %00000100
	.byte %00000000
	.byte %00001000
	.byte %00000000
	.byte %00001000
	.byte %00000000
	.byte %00000110
	.byte %00000000
	.byte %00110000
	.byte %11100000
	.byte %00000001
	.byte %00000000
	.byte %11000000
	.byte %00011111
	.byte %00000000
	.byte %00000000



    .org $fffc
    .word $8000
    .word $0000

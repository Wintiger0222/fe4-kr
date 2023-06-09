hirom

; !Original_menu_font_table = $879471 
; !Original_menu_font_table2 = $9471
; !Original_menu_font_table_index = $879471
; !Original_menu_font_table_index2 = $9471
!text_table_position =  $879D77
!text_table_position2 =  $9D77

org $C00A2B;size:F50h
incbin "menu_font/newfont.bin.fe4"
org $C0197B;size:63Fh
incbin "menu_font/statusfont.bin.fe4"

org $C03C10
;we will write them at armips
menu_font_table_index:
dw $0000
dw $0000
dw $0000
dw $0000;84
dw $0000;85
dw $0000;86
dw $0000;87
dw $0000;88
dw $0000
dw $0000;8A
dw $0000;8B
dw $0000
dw $0000
dw $0000;8E
dw $0000
dw $0000;90
dw $0000
dw $0000
dw $0000
dw $0000;94
dw $0000

org $C03C60
menu_font_table:
;set blank for armips


;normal text print routine
org $879354
  PHB 
  PHP 
  PHK 
  PLB 
  LDA $00
  PHA 
  LDA $02
  PHA 
  LDA $04
  PHA 
  PHX 
  PHY 
  LDY $0531
  SEP #$20
  LDA $0533
  PHA 
  REP #$20
  PLB 
  LDA $0006,Y
  STA $33
  LDA $0007,Y
  STA $34
  STZ $00
  TXA 
  SEP #$20
  STA $00
  XBA 
  STA $004202;WRMPYA
  LDA $0000,Y
  STA $004203;WRMPYB
  NOP 
  NOP 
  NOP 
  REP #$20
  LDA $004216;RDMPYL
  CLC 
  ADC $00
  ASL 
  PHA 
  LDA $0000,Y
  AND #$00FF
  ASL 
  STA $04
  PLY 
  LDX $24
  SEP #$20
  LDA $26
  PHA 
  REP #$20
  PLB 
unknown_8793AE:
  LDA $0000,X
  BEQ unknown_8793C3
  AND #$00FF
  CMP #$0084
  ; BCS unknown_87941D; we don't use second type table
  BRA unknown_8793D1
unknown_8793BD:
  INX 
  INX 
  INY 
  INY 
  BRA unknown_8793AE
unknown_8793C3:
  PLY 
  PLX 
  PLA 
  STA $04
  PLA 
  STA $02
  PLA 
  STA $00
  PLP 
  PLB 
  RTL 
org $8793D1
unknown_8793D1:;normal text
  PHX 
  SEC 
  SBC #$0081
  ASL 
  TAX 
  LDA menu_font_table_index,X
  STA $00
  PLX 
  PHX 
  PHY 
  LDA $0001,X
  AND #$00FF
  SEC 
  ; SBC #$0040
  PHA 
  AND #$0007
  STA $02
  PLA 
  AND #$FFF8
  ASL 
  CLC 
  ADC $02
  ASL 
  CLC 
  ADC $00
  TAX 
  LDA $00053A
  CLC 
  ADC menu_font_table,X
  STA [$33],Y
  TYA 
  CLC 
  ADC $04
  TAY 
  LDA $00053A
  CLC 
  ADC menu_font_table+$10,X
  STA [$33],Y
  PLY 
  PLX 
  BRA unknown_8793BD
  
org $87941D
unknown_87941D: ;routine for second type table, we not use
  PHX 
  LDA $0000,X
  LDX #$0000
_loop:
  CMP !text_table_position,X
  BEQ _found
  INX 
  INX 
  INX 
  INX 
  INX 
  INX 
  CPX #$005A
  BCC _loop
  BRA _none
_found:
  PHY 
  LDA $00053A
  CLC 
  ADC !text_table_position+$2,X
  STA [$33],Y
  TYA 
  CLC 
  ADC $04
  TAY 
  LDA $00053A
  CLC 
  ADC !text_table_position+$4,X
  STA [$33],Y
  PLY 
  PLX 
  JMP unknown_8793BD
_none:
  PHY 
  LDA $00053C
  STA [$33],Y
  TYA 
  CLC 
  ADC $04
  TAY 
  LDA $00053C
  STA [$33],Y
  PLY 
  PLX 
  JMP unknown_8793BD
  
  
;battle text print routine  
org $879DD1
  PHB 
  PHP 
  PHK 
  PLB 
  PHX 
  PHA 
  ; AND #$00FF
  ; CMP #$0084
  PLA 
  ; BCS unknown_879E19
  PHA 
  AND #$00FF
  SEC 
  SBC #$0081
  ASL 
  TAX 
  LDA menu_font_table_index,X
  STA $14
  PLA 
  XBA 
  AND #$00FF
  SEC 
  ; SBC #$0040
  PHA 
  AND #$0007
  STA $16
  PLA 
  AND #$FFF8
  ASL 
  CLC 
  ADC $16
  ASL 
  CLC 
  ADC $14
  TAX 
  LDA menu_font_table,X
  STA $14
  LDA menu_font_table+$10,X
  STA $16
  PLX 
  PLP 
  PLB 
  RTL 
org $879E19
unknown_879E19:  ;routine for second type table, we not use
  LDX #$0000
unknown_879E1C: 
  CMP !text_table_position2,X
  BEQ unknown_879E2E
  INX 
  INX 
  INX 
  INX 
  INX 
  INX 
  CPX #$005A
  BCC unknown_879E1C
  BRA unknown_879E3C
unknown_879E2E:
  LDA !text_table_position2+2,X
  STA $14
  LDA !text_table_position2+4,X
  STA $16
unknown_879E38:
  PLX 
  PLP 
  PLB 
  RTL 
unknown_879E3C: 
  STZ $14
  STZ $16
  BRA unknown_879E38
  
  
;option menu font hack
;because of scanline, we use another font for menu
org $829500
option_menu_font:
  incbin "menu_font/optionfont_hack.2bpp"
option_menu_font_end:

org $80E6D3 
  JSL option_menu_hack
  
;original menu font table position
;we will use this area
org $879471 
option_menu_hack:
  JSL $878979
  PHA
  PHX
  PHY
  SEP #$20
  LDA.B #option_menu_font
  STA $4312    ;data adress low
  LDA.B #option_menu_font>>8
  STA $4313    ;data adress high
  LDA.B #option_menu_font>>16
  STA $4314    ;data adress bank
  LDA.B #(option_menu_font_end-option_menu_font)
  STA $4315    ;size
  LDA.B #(option_menu_font_end-option_menu_font)>>8
  STA $4316    ;size
  LDA #$00
  STA $2116    ;VRAM L
  LDA #$00
  STA $2117    ;VRAM H
  LDA #$01
  STA $4310
  LDA #$18
  STA $4311
  LDA #$02
  STA $420B
  REP #$20
  PLY
  PLX
  PLA
  RTL 

;status screen position hack
;;top screen
org $899C0A ;Char Status Chr Attack
db $15
org $899C1B ;Char Status Chr Accuracy
db $15
org $899C2C ;Char Status Chr Range
db $15
org $899C3D ;Char Status Chr Evade
db $15

;first screen
org $899CB9 ;Char Status Stat Power 
db $07
org $899CCA ;Char Status Stat Magic
db $06
org $899CDB ;Char Status Stat Skill
db $06
org $899CEC ;Char Status Stat Speed
db $05
org $899CFD ;Char Status Stat Luck
db $03
org $899D0E ;Char Status Stat Defence
db $05
org $899D1F ;Char Status Stat Magic Defence
db $03


;second screen left
org $899DDB ;Char Status Info Leader
db $03
org $899DF2 ;Char Status Info Army
db $04
org $899E05 ;Char Status Info Lover
db $04
org $899E16 ;Char Status Info Talk
db $04
org $899E27 ;Char Status Info Move
db $04
org $899E38 ;Char Status Info Gold
db $03
org $899E49 ;Char Status Info Arena Level
db $02
org $899E5A ;Char Status Info Status
db $04

;second screen right
org $899E6B ;Char Status Rank Sword
db $12
org $899E7C ;Char Status Rank Lance
db $12
org $899E8D ;Char Status Rank Axe
db $12
org $899E9E ;Char Status Rank Bow
db $12
org $899EAF ;Char Status Rank Staff
db $12
org $899EC0 ;Char Status Rank Fire
db $1A
org $899ED1 ;Char Status Rank Thunder
db $1A
org $899EE2 ;Char Status Rank Wind
db $1A
org $899EF3 ;Char Status Rank Light
db $1A
org $899F04 ;Char Status Rank Dark
db $1A


org $899AA1 ;value Status Rank Fire
db $16
org $899AB6 ;value Status Rank Thunder
db $16
org $899ACB ;value Status Rank Wind
db $16
org $899AE0 ;value Status Rank Light
db $16
org $899AF5 ;value Status Rank Dark
db $16

;sprite oam
org $898ADC ;sprite Status Rank Fire
db $3F
org $898AE1 ;sprite Status Rank Thunder
db $3F
org $898AE6 ;sprite Status Rank Wind
db $3F
org $898AEB ;sprite Status Rank Light
db $3F
org $898AF0 ;sprite Status Rank Dark
db $3F
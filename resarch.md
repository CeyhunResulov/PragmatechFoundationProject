## 
display:flex                    ----   alt-alta olan elementleri bir setirde yerlesdirir ve bu emir hemin elementlerin atasina verilmelidir)
1.flex-direction:column         ----   qutulari sutun uzre yerlesdirir 
                 column-reverse ----   qutulari sutun uzre asagdan yuxariya dogru yerlesdirir
                 row            ----   qutulari setir uzre yerlesdirir
                 row-reverse    ----   qutulari setir uzre sagdan sola dogru yerlesdirir

2.flex-wrap:wrap                ----   qutular bir setre sigmadigda olcusu kicilir ve wrap qutulari novbeti setre kecirerek olcusunu saxlayir
            nowrap              ----   wrap-i legv edir
            wrap-reverse        ----   qutulari sonuncu setirden baslayaraq evvele dogru yerlesdirir

3.flex-flow:column wrap        ------  flex-direction ve flex-wrap birlesdirir

4.justify-content:flex-start   ------  elementleri setrin evvelinde yerlesdirir
                  flex-end     ------  elementeleri setrin sonunda yerlesdirir    
                  center       ------  elementleri setrin ortasinda yerlesdirir
                  space-between------  elementler arasinda eyni olcude bosluq yaradir
                  space-around ------  hem elementler hemde setrin evvelinden ve sonundan eyni olcude bosluq yaradir

5.align-content:-------justfy-contentle eyni emirleri sutun uzre yerine yetirir

6.align-itms:flex-start        ------  ?????????
             flex-end          
             center
             stretch
             besline





display:grid               ------  hem setir hem de sutun uzre qutulari yerlesdirir
1.grid-template-row: 1fr 1fr 1fr        ------  setirleri yaradir
2.grid-template-column: auto auto auto     ------  sutunlari yaradir
3.grid-gap: 10px 20px        ------  setir ve sutun qutulari arasinda bosluq yaradir 1 ci setirler arasi bosluq,ikinci sutunlar arasi bosluq
4.grid-column-start:  1       ------>  bu iki emir sutunun hansi hisseni tutmasini mueyyen edir
5.grid-column-end:3           ------^
6.grid-row-start:
7.grid-row-end:
6.grid-area: x / y / s / d    ------ bu emir grid-column ve grid-row kodlarini ozunde birlesdirir
                                     grid-row-start(x),grid-column-start(y),grid-row-end(s),grid-column-end.




display:grid ve display:flex ferqleri:
displey:grid eyni vaxta hem setir hemde sutun uzre istifade oluna bilir.esasen boyuk hisselerin hazirlanmasinda istifade olunur.
displey:flex ya setir yadaki sutun uzre qutulari yerlesdire bilir.kicik elementleri flex ile yerlesdirmek daha rahat olar mence.mes ul>li>a kimi hisseler ucun flex daha yaxsidir
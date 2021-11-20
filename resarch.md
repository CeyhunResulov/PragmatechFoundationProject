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
grid-template-row: 1fr 1fr 1fr        ------  setirleri yaradir
grid-template-column: auto auto auto     ------  sutunlari yaradir
grid-gap: 10px 20px        ------  setir ve sutun qutulari arasinda bosluq yaradir 1 ci setirler arasi bosluq,ikinci sutunlar arasi bosluq
grid-column-start:  1       ------  bu iki emir sutunun hansi hisseni tutmasini mueyyen edir
grid-column-end:3
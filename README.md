# Pokémon Card Launcher

work in progress!

inspired by the famous money gun, a pokemon card launcher, self explanatory--it launches pokemon cards! also has a screen that can display whatever you want :P

# Wiring

<img width="1500" height="1300" alt="wiring" src="https://github.com/user-attachments/assets/8ad14a5d-b392-44dc-859d-7c5864d8de25" />

# BOM

| Item              | Price (USD)  | Quantity | Total (USD)  | Purchase Link                     |
|-------------------|--------------|----------|--------------|-----------------------------------|
| Raspberry Pi Pico | $4.83        | 1        | $4.83        |[AliExpress](https://www.aliexpress.com/item/1005008714908011.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%209.66%21USD%204.83%21%21USD%204.83%21%21%21%402103205117538590533514861e2028%2112000046359830441%21ct%21CA%21-1%21%211%210)|
| L298N Motor Driver| $1.92        | 1        | $1.92        |[AliExpress](https://www.aliexpress.com/item/32392774289.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.92%21USD%201.92%21%21USD%201.92%21%21%21%402103205117538590533514861e2028%2157692613834%21ct%21CA%21-1%21%211%210)|
| Breadboard        | $1.95        | 1        | $1.95        |[AliExpress](https://www.aliexpress.com/item/1005004532352681.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.95%21USD%201.95%21%21USD%201.95%21%21%21%402103205117538590533514861e2028%2112000029625253661%21ct%21CA%21-1%21%211%210)|
| DC Motor          | $3.99        | 1        | $3.99        |[AliExpress](https://www.aliexpress.com/item/1005009088012332.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%203.99%21USD%203.99%21%21USD%203.99%21%21%21%402103205117538590533514861e2028%2112000047864628861%21ct%21CA%21-1%21%211%210)|
| Rubber Wheel      | $2.83        | 1        | $2.83        |[AliExpress](https://www.aliexpress.com/item/4001224816603.html?spm=a2g0o.cart.0.0.11d138daAiug11&mp=1&pdp_npi=5%40dis%21USD%21USD%202.83%21USD%202.83%21%21USD%202.83%21%21%21%40210337c117538600189653250e5237%2110000015356947869%21ct%21CA%21-1%21%211%210)|
| Tactile Button    | $1.88        | 1        | $1.88        |[AliExpress](https://www.aliexpress.com/item/4000678658427.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.88%21USD%201.88%21%21USD%201.88%21%21%21%402103205117538590533514861e2028%2110000005854848642%21ct%21CA%21-1%21%211%210)|
| Jumper Wires (Kit)| $7.75        | 1        | $7.75        |[AliExpress](https://www.aliexpress.com/item/1005003219096948.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%207.75%21USD%203.20%21%21USD%203.20%21%21%21%402103205117538590533514861e2028%2112000024783046672%21ct%21CA%21-1%21%211%210)|
| 9V Battery Holder | $1.32        | 1        | $1.32        |[AliExpress](https://www.aliexpress.com/item/1005005554453537.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.32%21USD%201.32%21%21USD%201.32%21%21%21%402103205117538590533514861e2028%2112000035453673630%21ct%21CA%21-1%21%211%210)|
| OLED Screen       | $4.62        | 1        | $4.62        |[AliExpress](https://www.aliexpress.com/item/4000049991220.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%204.62%21USD%204.62%21%21USD%204.62%21%21%21%402103205117538590533514861e2028%2112000038048905094%21ct%21CA%21-1%21%211%210)|
| On/Off Switch     | $1.54        | 1        | $1.54        |[AliExpress](https://www.aliexpress.com/item/32873386670.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.54%21USD%201.54%21%21USD%201.54%21%21%21%402103205117538590533514861e2028%2165526366999%21ct%21CA%21-1%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D)|
| AA Battery Holder | $4.52        | 1        | $4.52        |[AliExpress](https://www.aliexpress.com/item/1005006283625827.html?spm=a2g0o.cart.0.0.7ff538dauBhahg&mp=1&pdp_npi=5%40dis%21USD%21USD%2010.27%21USD%204.52%21%21USD%204.52%21%21%21%40210313e917538592948841044e6017%2112000036604532383%21ct%21CA%21-1%21%211%210)|
| 4x AA Batteries   | $7.26        | 1        | $7.26        |[Amazon](https://www.amazon.ca/dp/B00000JHQ6/?coliid=I3MD84OOKTOVUK&colid=JDF2MW8L7EB4&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)|
| 2x 9V Batteries   | $8.70        | 1        | $8.70        |[Amazon](https://www.amazon.ca/dp/B00003IE4E/?coliid=I3T4SJ4LC8GOCX&colid=JDF2MW8L7EB4&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)|

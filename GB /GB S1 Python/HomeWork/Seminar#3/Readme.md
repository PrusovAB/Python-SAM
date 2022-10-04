# Урок 3. Данные, функции и модули в Python



     
     
     
     
     
                                 ,▄▄▄▓▓████████▓▓▄▄,
                             ,▄████████████████████████▄
                            █████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████▄
                           ███▒╬╬╬███▒╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣███
                           ███╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬███─
                           ███╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬███─
                       ,   ███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬███▄▄▄▄▄╓
                  ▄▓███████████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬████████████▄
                ▓████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██▒░░░░░│╙▀███▄
              ╓███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██▒░░░░░░░░│╙███
             ]███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██▒░░░░░░░░░░╟██▌
             ███▒╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██░░░░░░░░░░░░███
             ███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██▌░░░░░░░░░░░░╟██⌐
            ▐███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓▓█████▀░░░░░░░░░░░░░╟██Γ
            ▐███╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀╙└░░░░░░░░░░░░░░░╟██Γ
             ███╬╬╬╬╬╬╬╬╬╬╬╬╬██▀└'│││││░││░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟██Γ
             ███╬╬╬╬╬╬╬╬╬╬╬╬██▀││││││░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███
             ╟███╬╬╬╬╬╬╬╬╬╬╬██│││││░││░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐██▌
              ███▓╬╬╬╬╬╬╬╬╬╬██│││░││░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄███
               ▀███▓╬╬╬╬╬╬╬╬██│░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░,▄███▀
                └▀████████████│░░░░░░░░░░░░█████████████████████████▀
                   └▀▀▀▀▀▀▀███░░░░░░░░░░░░░└└└└└└│││││││╫██▀▀▀▀▀╙└
                           ███░░░░░░░░░░░░░░░░░░░Q▄▄░░░░╫██─
                           ███░░░░░░░░░░░░░░░░░░▓████░░░╫██─
                           ███▄░░░░░░░░░░░░░░░░░╙███▀░░░███─
                            ████▄░░░░░░░░░░░░░░░░░░░░░▄███▀
                             ╙▀█████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓█████▀─
                                └╙▀▀███████████████▀▀╙─
     
     
     
     
[size=9px][font=monospace][color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080]                             [/color][color=#707070],[/color][color=#5d5d5d]▄[/color][color=#4c4c4c]▄[/color][color=#404040]▄[/color][color=#353535]▓[/color][color=#2d2d2d]▓[/color][color=#272727]█[/color][color=#232323]█[/color][color=#1e1e1e]█[/color][color=#1e1e1e]███[/color][color=#242424]█[/color][color=#292929]█[/color][color=#2f2f2f]▓[/color][color=#383838]▓[/color][color=#444444]▄[/color][color=#525252]▄[/color][color=#646464],[/color]
[color=#808080]                         [/color][color=#717171],[/color][color=#424242]▄[/color][color=#1d1d1d]█[/color][color=#020202]█[/color][color=#000000]███[/color][color=#04111b]█[/color][color=#061a28]█[/color][color=#072233]█[/color][color=#08273c]█[/color][color=#092a41]██[/color][color=#0a2d45]█████[/color][color=#071e2e]█[/color][color=#051722]█[/color][color=#030d13]█[/color][color=#010203]█[/color][color=#000000]██[/color][color=#090909]█[/color][color=#292929]█[/color][color=#525252]▄[/color]
[color=#808080]                        [/color][color=#2a2a2a]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#04141f]█[/color][color=#0b3856]█[/color][color=#11517e]╬[/color][color=#146297]╬[/color][color=#146499]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#145784]╬[/color][color=#104366]╬[/color][color=#0b293d]█[/color][color=#03070b]█[/color][color=#000000]██[/color][color=#3e3e3e]▄[/color]
[color=#808080]                       [/color][color=#141414]█[/color][color=#000000]█[/color][color=#010102]█[/color][color=#0f4b74]▒[/color][color=#14659c]╬[/color][color=#14649a]╬╬[/color][color=#0d3e60]█[/color][color=#0a324d]██[/color][color=#135e8f]▒[/color][color=#146397]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#0e3652]╣[/color][color=#010001]█[/color][color=#000000]█[/color][color=#1c1c1c]█[/color]
[color=#808080]                       [/color][color=#000000]█[/color][color=#000000]█[/color][color=#041119]█[/color][color=#14649a]╬[/color][color=#146499]╬╬[/color][color=#04101a]█[/color][color=#000000]█[/color][color=#000000]██[/color][color=#03070c]█[/color][color=#146195]╬[/color][color=#146195]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155989]╬[/color][color=#092336]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#676767]─[/color]
[color=#808080]                       [/color][color=#000000]█[/color][color=#000000]█[/color][color=#040f18]█[/color][color=#146499]╬[/color][color=#146499]╬╬[/color][color=#11537f]╬[/color][color=#08273c]█[/color][color=#061a28]██[/color][color=#104d75]╬[/color][color=#146195]╬[/color][color=#146093]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155988]╬╬[/color][color=#09283d]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#646464]─[/color]
[color=#808080]                   [/color][color=#717171],   [/color][color=#000000]█[/color][color=#000000]█[/color][color=#030e16]█[/color][color=#146498]╬[/color][color=#146397]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155c8b]╬[/color][color=#155b8a]╬╬╬╬╬╬╬╬╬[/color][color=#09273c]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#444444]▄[/color][color=#575757]▄[/color][color=#575757]▄▄▄[/color][color=#606060]╓[/color]
[color=#808080]              [/color][color=#4f4f4f]▄[/color][color=#2b2b2b]▓[/color][color=#0d0d0d]█[/color][color=#000000]█[/color][color=#000000]████████[/color][color=#041521]█[/color][color=#041520]████████████[/color][color=#145581]╬[/color][color=#155c8b]╬[/color][color=#155b8a]╬╬╬╬╬╬╬╬╬╬╬[/color][color=#0a273b]█[/color][color=#000000]█[/color][color=#020101]█████████[/color][color=#212121]█[/color][color=#4e4e4e]▄[/color]
[color=#808080]            [/color][color=#313131]▓[/color][color=#010101]█[/color][color=#000000]█[/color][color=#030b10]█[/color][color=#0a2c44]█[/color][color=#0e4469]╬[/color][color=#11537e]╬[/color][color=#135d8d]╬[/color][color=#135d8f]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#09273b]█[/color][color=#000001]█[/color][color=#b19122]▒[/color][color=#d6b029]░[/color][color=#d6b029]░░░░│[/color][color=#a88920]╙[/color][color=#665314]▀[/color][color=#0f0c04]█[/color][color=#000000]██[/color][color=#4b4b4b]▄[/color]
[color=#808080]          [/color][color=#616161]╓[/color][color=#060606]█[/color][color=#000000]██[/color][color=#0f476e]╬[/color][color=#14649b]╬[/color][color=#146499]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#145d8e]╬[/color][color=#155c8c]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#09263a]█[/color][color=#000001]█[/color][color=#b09122]▒[/color][color=#d6af29]░[/color][color=#d6af29]░░░░░░░│[/color][color=#635014]╙[/color][color=#000000]█[/color][color=#000000]█[/color][color=#2a2a2a]█[/color]
[color=#808080]         [/color][color=#6d6d6d]][/color][color=#020202]█[/color][color=#000000]█[/color][color=#040e15]█[/color][color=#146093]╬[/color][color=#146499]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155986]╬[/color][color=#155985]╬╬╬╬╬╬╬╬[/color][color=#092538]█[/color][color=#000001]█[/color][color=#b19022]▒[/color][color=#d7af28]░[/color][color=#d7af28]░░░░░░░░░[/color][color=#745c16]╟[/color][color=#000000]█[/color][color=#000000]█[/color][color=#3d3d3d]▌[/color]
[color=#808080]         [/color][color=#181818]█[/color][color=#000000]█[/color][color=#010001]█[/color][color=#125887]▒[/color][color=#146499]╬[/color][color=#146499]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155c8c]╬[/color][color=#155b8a]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#14557f]╬[/color][color=#040d14]█[/color][color=#000000]█[/color][color=#c49f24]░[/color][color=#d8ae28]░[/color][color=#d8ae27]░░░░░░░░░░[/color][color=#1c1706]█[/color][color=#000000]█[/color][color=#010101]█[/color]
[color=#808080]         ██[/color][color=#051520]█[/color][color=#136499]╬[/color][color=#136498]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155c8b]╬[/color][color=#155b8a]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#15547f]╬[/color][color=#134b71]╬[/color][color=#061623]█[/color][color=#000001]█[/color][color=#4e3f0f]▌[/color][color=#d8af27]░[/color][color=#d8ae27]░░░░░░░░░░░[/color][color=#715815]╟[/color][color=#000000]█[/color][color=#000000]█[/color][color=#565656]⌐[/color]
[color=#808080]        [/color][color=#5d5d5d]▐[/color][color=#000000]█[/color][color=#000000]█[/color][color=#082b41]█[/color][color=#146397]╬[/color][color=#146296]╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#155b8a]╬[/color][color=#145986]╬[/color][color=#13537e]╬[/color][color=#124f78]╬╬╬╬╬╬[/color][color=#124d75]╬╬╬╬╬╬╬╬▓[/color][color=#104163]▓[/color][color=#0e3855]█[/color][color=#0a283c]█[/color][color=#05111a]█[/color][color=#000001]█[/color][color=#141004]█[/color][color=#7f6617]▀[/color][color=#d7ae27]░[/color][color=#d8ad27]░░░░░░░░░░░░[/color][color=#7a5f16]╟[/color][color=#000000]█[/color][color=#000000]█[/color][color=#535353]Γ[/color]
[color=#808080]        [/color][color=#5b5b5b]▐[/color][color=#000000]█[/color][color=#000000]█[/color][color=#0a2d46]█[/color][color=#146195]╬[/color][color=#146195]╬╬╬╬╬╬╬╬╬╬╬╬╬[/color][color=#0e3b5a]▓[/color][color=#071a27]█[/color][color=#020406]█[/color][color=#030201]█[/color][color=#231e08]█[/color][color=#41370e]▀[/color][color=#514411]▀[/color][color=#564812]▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀[/color][color=#6d5814]▀[/color][color=#886e19]╙[/color][color=#b89421]└[/color][color=#d8ae27]░[/color][color=#d8ad27]░░░░░░░░░░░░░░[/color][color=#7a5f15]╟[/color][color=#000000]█[/color][color=#000000]█[/color][color=#535353]Γ[/color]
[color=#808080]         [/color][color=#000000]█[/color][color=#000000]█[/color][color=#072031]█[/color][color=#146195]╬[/color][color=#146093]╬╬╬╬╬╬╬╬╬╬╬[/color][color=#145480]╬[/color][color=#040e15]█[/color][color=#010001]█[/color][color=#43390f]▀[/color][color=#a18923]└[/color][color=#d1b22c]'[/color][color=#d3b32c]│││││░││░░░░░░░░░░[/color][color=#d8ae27]░[/color][color=#d8ae27]░░░░░░░░░░░░░░░░░[/color][color=#7a5e15]╟[/color][color=#000000]█[/color][color=#000000]█[/color][color=#535353]Γ[/color]
[color=#808080]         [/color][color=#050505]█[/color][color=#000000]██[/color][color=#145f91]╬[/color][color=#146092]╬╬╬╬╬╬╬╬╬╬╬[/color][color=#06141e]█[/color][color=#000001]█[/color][color=#88731e]▀[/color][color=#d3b32c]│[/color][color=#d3b32c]│││││░░│░░░░░░░░░░░[/color][color=#d8ae27]░[/color][color=#d8ad27]░░░░░░░░░░░░░░░░░░[/color][color=#3d2e0b]█[/color][color=#000000]█[/color][color=#000000]█[/color]
[color=#808080]         [/color][color=#3e3e3e]╟[/color][color=#000000]█[/color][color=#000001]█[/color][color=#0c3754]█[/color][color=#146091]╬[/color][color=#145e8f]╬╬╬╬╬╬╬╬╬╬[/color][color=#010102]█[/color][color=#100e04]█[/color][color=#d3b32c]│[/color][color=#d3b22c]││││░││░░░░░░░░░░░░[/color][color=#d8ad27]░[/color][color=#d8ad27]░░░░░░░░░░░░░░░░░░[/color][color=#a57f19]▐[/color][color=#010000]█[/color][color=#000000]█[/color][color=#222222]▌[/color]
[color=#808080]          [/color][color=#1a1a1a]█[/color][color=#000000]█[/color][color=#000101]█[/color][color=#0e3f61]▓[/color][color=#145e8f]╬[/color][color=#145d8d]╬╬╬╬╬╬╬╬╬[/color][color=#010102]█[/color][color=#1b1706]█[/color][color=#d3b22c]│[/color][color=#d4b12c]││░││░░░░░░░░░░░░░░[/color][color=#d9ae26]░[/color][color=#daae25]░░░░░░░░░░░░░░░░░[/color][color=#947117]▄[/color][color=#040302]█[/color][color=#000000]█[/color][color=#131313]█[/color]
[color=#808080]           [/color][color=#2b2b2b]▀[/color][color=#000000]█[/color][color=#000000]█[/color][color=#071d2d]█[/color][color=#124b71]▓[/color][color=#155b8a]╬[/color][color=#155a8a]╬╬╬╬╬╬╬[/color][color=#010102]█[/color][color=#1b1705]█[/color][color=#d4b12b]│[/color][color=#d4b12b]░│░░░░░░░░░░░░░░░░[/color][color=#daae25]░░░░[/color][color=#daad25]░░░░░░░░░░░░[/color][color=#d1a020],[/color][color=#906e16]▄[/color][color=#2d2208]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#323232]▀[/color]
[color=#808080]            [/color][color=#636363]└[/color][color=#242424]▀[/color][color=#010101]█[/color][color=#000000]█[/color][color=#02070a]█[/color][color=#071a28]█[/color][color=#0a263a]█[/color][color=#0a293f]█████[/color][color=#010001]█[/color][color=#1b1706]█[/color][color=#d5b12a]│[/color][color=#d5b12a]░░░░░░░░░░░░[/color][color=#3f330d]█[/color][color=#3a2f0b]███████████████████[/color][color=#302407]█[/color][color=#110c03]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#0c0c0c]█[/color][color=#383838]▀[/color]
[color=#808080]               [/color][color=#5b5b5b]└[/color][color=#3e3e3e]▀[/color][color=#2b2b2b]▀[/color][color=#212121]▀[/color][color=#1d1d1d]▀[/color][color=#1d1d1d]▀▀▀[/color][color=#000000]█[/color][color=#000000]█[/color][color=#1b1706]█[/color][color=#d5b02a]░[/color][color=#d6b029]░░░░░░░░░░░░[/color][color=#bc9621]└[/color][color=#bb9620]└└└└└│││││││[/color][color=#58440e]╫[/color][color=#000000]█[/color][color=#000000]█[/color][color=#2b2b2b]▀[/color][color=#373737]▀[/color][color=#373737]▀▀[/color][color=#3c3c3c]▀[/color][color=#474747]╙[/color][color=#5b5b5b]└[/color]
[color=#808080]                       [/color][color=#010101]█[/color][color=#000000]█[/color][color=#1c1705]█[/color][color=#d6b029]░[/color][color=#d6b029]░░░░░░░░░░░░░░░░░░[/color][color=#c49a20]Q[/color][color=#9d7b1a]▄[/color][color=#ae881d]▄[/color][color=#daa923]░[/color][color=#dcab23]░░░[/color][color=#684f10]╫[/color][color=#000000]█[/color][color=#000000]█[/color][color=#646464]─[/color]
[color=#808080]                       [/color][color=#010101]█[/color][color=#000000]█[/color][color=#1c1706]█[/color][color=#d6af29]░[/color][color=#d6af29]░░░░░░░░░░░░░░░░░[/color][color=#675012]▓[/color][color=#000000]█[/color][color=#000000]██[/color][color=#130e04]█[/color][color=#d9a822]░[/color][color=#ddaa22]░░[/color][color=#685010]╫[/color][color=#000000]█[/color][color=#000000]█[/color][color=#636363]─[/color]
[color=#808080]                       [/color][color=#161616]█[/color][color=#000000]█[/color][color=#010101]█[/color][color=#ab8b21]▄[/color][color=#d7af28]░[/color][color=#d8af27]░░░░░░░░░░░░░░░░[/color][color=#ab851c]╙[/color][color=#302508]█[/color][color=#0c0902]█[/color][color=#191305]█[/color][color=#674f11]▀[/color][color=#ddaa22]░[/color][color=#ddaa22]░░[/color][color=#49370c]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#666666]─[/color]
[color=#808080]                        [/color][color=#1b1b1b]█[/color][color=#000000]█[/color][color=#010101]█[/color][color=#51410f]█[/color][color=#aa891f]▄[/color][color=#d7ad27]░[/color][color=#d8ad27]░░░░░░░░░░░░░░░░░░░[/color][color=#dca921]░[/color][color=#a67f1a]▄[/color][color=#3d2e0a]█[/color][color=#000000]█[/color][color=#000000]█[/color][color=#363636]▀[/color]
[color=#808080]                         [/color][color=#5c5c5c]╙[/color][color=#252525]▀[/color][color=#020202]█[/color][color=#000000]██[/color][color=#312709]█[/color][color=#574510]█[/color][color=#795f15]▄[/color][color=#8d7018]▄[/color][color=#a3811c]▄[/color][color=#b38d1e]▄[/color][color=#bc941f]▄[/color][color=#c29820]▄▄▄▄▄▄[/color][color=#b38a1c]▄[/color][color=#a17c19]▄[/color][color=#8e6d16]▄[/color][color=#785c13]▓[/color][color=#56420e]█[/color][color=#2f2407]█[/color][color=#040301]█[/color][color=#000000]██[/color][color=#2b2b2b]▀[/color][color=#686868]─[/color]
[color=#808080]                            [/color][color=#646464]└[/color][color=#474747]╙[/color][color=#303030]▀[/color][color=#1d1d1d]▀[/color][color=#0e0e0e]█[/color][color=#030303]█[/color][color=#000000]████████████[/color][color=#0f0f0f]█[/color][color=#1e1e1e]▀[/color][color=#323232]▀[/color][color=#494949]╙[/color][color=#666666]─[/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080] [/color]

[/font][/size]

<!DOCTYPE html><head><meta charset="utf-8"></head><body style="font: 9px monospace; line-height:9px; background-color:white;"><span></span><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#707070">,</span><span style="color:#5d5d5d">▄</span><span style="color:#4c4c4c">▄</span><span style="color:#404040">▄</span><span style="color:#353535">▓</span><span style="color:#2d2d2d">▓</span><span style="color:#272727">█</span><span style="color:#232323">█</span><span style="color:#1e1e1e">█</span><span style="color:#1e1e1e">███</span><span style="color:#242424">█</span><span style="color:#292929">█</span><span style="color:#2f2f2f">▓</span><span style="color:#383838">▓</span><span style="color:#444444">▄</span><span style="color:#525252">▄</span><span style="color:#646464">,</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#717171">,</span><span style="color:#424242">▄</span><span style="color:#1d1d1d">█</span><span style="color:#020202">█</span><span style="color:#000000">███</span><span style="color:#04111b">█</span><span style="color:#061a28">█</span><span style="color:#072233">█</span><span style="color:#08273c">█</span><span style="color:#092a41">██</span><span style="color:#0a2d45">█████</span><span style="color:#071e2e">█</span><span style="color:#051722">█</span><span style="color:#030d13">█</span><span style="color:#010203">█</span><span style="color:#000000">██</span><span style="color:#090909">█</span><span style="color:#292929">█</span><span style="color:#525252">▄</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#2a2a2a">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#04141f">█</span><span style="color:#0b3856">█</span><span style="color:#11517e">╬</span><span style="color:#146297">╬</span><span style="color:#146499">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#145784">╬</span><span style="color:#104366">╬</span><span style="color:#0b293d">█</span><span style="color:#03070b">█</span><span style="color:#000000">██</span><span style="color:#3e3e3e">▄</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#141414">█</span><span style="color:#000000">█</span><span style="color:#010102">█</span><span style="color:#0f4b74">▒</span><span style="color:#14659c">╬</span><span style="color:#14649a">╬╬</span><span style="color:#0d3e60">█</span><span style="color:#0a324d">██</span><span style="color:#135e8f">▒</span><span style="color:#146397">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#0e3652">╣</span><span style="color:#010001">█</span><span style="color:#000000">█</span><span style="color:#1c1c1c">█</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#041119">█</span><span style="color:#14649a">╬</span><span style="color:#146499">╬╬</span><span style="color:#04101a">█</span><span style="color:#000000">█</span><span style="color:#000000">██</span><span style="color:#03070c">█</span><span style="color:#146195">╬</span><span style="color:#146195">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155989">╬</span><span style="color:#092336">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#676767">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#040f18">█</span><span style="color:#146499">╬</span><span style="color:#146499">╬╬</span><span style="color:#11537f">╬</span><span style="color:#08273c">█</span><span style="color:#061a28">██</span><span style="color:#104d75">╬</span><span style="color:#146195">╬</span><span style="color:#146093">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155988">╬╬</span><span style="color:#09283d">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#646464">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#717171">,&nbsp;&nbsp;&nbsp;</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#030e16">█</span><span style="color:#146498">╬</span><span style="color:#146397">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155c8b">╬</span><span style="color:#155b8a">╬╬╬╬╬╬╬╬╬</span><span style="color:#09273c">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#444444">▄</span><span style="color:#575757">▄</span><span style="color:#575757">▄▄▄</span><span style="color:#606060">╓</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#4f4f4f">▄</span><span style="color:#2b2b2b">▓</span><span style="color:#0d0d0d">█</span><span style="color:#000000">█</span><span style="color:#000000">████████</span><span style="color:#041521">█</span><span style="color:#041520">████████████</span><span style="color:#145581">╬</span><span style="color:#155c8b">╬</span><span style="color:#155b8a">╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#0a273b">█</span><span style="color:#000000">█</span><span style="color:#020101">█████████</span><span style="color:#212121">█</span><span style="color:#4e4e4e">▄</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#313131">▓</span><span style="color:#010101">█</span><span style="color:#000000">█</span><span style="color:#030b10">█</span><span style="color:#0a2c44">█</span><span style="color:#0e4469">╬</span><span style="color:#11537e">╬</span><span style="color:#135d8d">╬</span><span style="color:#135d8f">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#09273b">█</span><span style="color:#000001">█</span><span style="color:#b19122">▒</span><span style="color:#d6b029">░</span><span style="color:#d6b029">░░░░│</span><span style="color:#a88920">╙</span><span style="color:#665314">▀</span><span style="color:#0f0c04">█</span><span style="color:#000000">██</span><span style="color:#4b4b4b">▄</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#616161">╓</span><span style="color:#060606">█</span><span style="color:#000000">██</span><span style="color:#0f476e">╬</span><span style="color:#14649b">╬</span><span style="color:#146499">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#145d8e">╬</span><span style="color:#155c8c">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#09263a">█</span><span style="color:#000001">█</span><span style="color:#b09122">▒</span><span style="color:#d6af29">░</span><span style="color:#d6af29">░░░░░░░│</span><span style="color:#635014">╙</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#2a2a2a">█</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#6d6d6d">]</span><span style="color:#020202">█</span><span style="color:#000000">█</span><span style="color:#040e15">█</span><span style="color:#146093">╬</span><span style="color:#146499">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155986">╬</span><span style="color:#155985">╬╬╬╬╬╬╬╬</span><span style="color:#092538">█</span><span style="color:#000001">█</span><span style="color:#b19022">▒</span><span style="color:#d7af28">░</span><span style="color:#d7af28">░░░░░░░░░</span><span style="color:#745c16">╟</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#3d3d3d">▌</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#181818">█</span><span style="color:#000000">█</span><span style="color:#010001">█</span><span style="color:#125887">▒</span><span style="color:#146499">╬</span><span style="color:#146499">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155c8c">╬</span><span style="color:#155b8a">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#14557f">╬</span><span style="color:#040d14">█</span><span style="color:#000000">█</span><span style="color:#c49f24">░</span><span style="color:#d8ae28">░</span><span style="color:#d8ae27">░░░░░░░░░░</span><span style="color:#1c1706">█</span><span style="color:#000000">█</span><span style="color:#010101">█</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;██</span><span style="color:#051520">█</span><span style="color:#136499">╬</span><span style="color:#136498">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155c8b">╬</span><span style="color:#155b8a">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#15547f">╬</span><span style="color:#134b71">╬</span><span style="color:#061623">█</span><span style="color:#000001">█</span><span style="color:#4e3f0f">▌</span><span style="color:#d8af27">░</span><span style="color:#d8ae27">░░░░░░░░░░░</span><span style="color:#715815">╟</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#565656">⌐</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#5d5d5d">▐</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#082b41">█</span><span style="color:#146397">╬</span><span style="color:#146296">╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#155b8a">╬</span><span style="color:#145986">╬</span><span style="color:#13537e">╬</span><span style="color:#124f78">╬╬╬╬╬╬</span><span style="color:#124d75">╬╬╬╬╬╬╬╬▓</span><span style="color:#104163">▓</span><span style="color:#0e3855">█</span><span style="color:#0a283c">█</span><span style="color:#05111a">█</span><span style="color:#000001">█</span><span style="color:#141004">█</span><span style="color:#7f6617">▀</span><span style="color:#d7ae27">░</span><span style="color:#d8ad27">░░░░░░░░░░░░</span><span style="color:#7a5f16">╟</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#535353">Γ</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#5b5b5b">▐</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#0a2d46">█</span><span style="color:#146195">╬</span><span style="color:#146195">╬╬╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#0e3b5a">▓</span><span style="color:#071a27">█</span><span style="color:#020406">█</span><span style="color:#030201">█</span><span style="color:#231e08">█</span><span style="color:#41370e">▀</span><span style="color:#514411">▀</span><span style="color:#564812">▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀</span><span style="color:#6d5814">▀</span><span style="color:#886e19">╙</span><span style="color:#b89421">└</span><span style="color:#d8ae27">░</span><span style="color:#d8ad27">░░░░░░░░░░░░░░</span><span style="color:#7a5f15">╟</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#535353">Γ</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#072031">█</span><span style="color:#146195">╬</span><span style="color:#146093">╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#145480">╬</span><span style="color:#040e15">█</span><span style="color:#010001">█</span><span style="color:#43390f">▀</span><span style="color:#a18923">└</span><span style="color:#d1b22c">'</span><span style="color:#d3b32c">│││││░││░░░░░░░░░░</span><span style="color:#d8ae27">░</span><span style="color:#d8ae27">░░░░░░░░░░░░░░░░░</span><span style="color:#7a5e15">╟</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#535353">Γ</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#050505">█</span><span style="color:#000000">██</span><span style="color:#145f91">╬</span><span style="color:#146092">╬╬╬╬╬╬╬╬╬╬╬</span><span style="color:#06141e">█</span><span style="color:#000001">█</span><span style="color:#88731e">▀</span><span style="color:#d3b32c">│</span><span style="color:#d3b32c">│││││░░│░░░░░░░░░░░</span><span style="color:#d8ae27">░</span><span style="color:#d8ad27">░░░░░░░░░░░░░░░░░░</span><span style="color:#3d2e0b">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#3e3e3e">╟</span><span style="color:#000000">█</span><span style="color:#000001">█</span><span style="color:#0c3754">█</span><span style="color:#146091">╬</span><span style="color:#145e8f">╬╬╬╬╬╬╬╬╬╬</span><span style="color:#010102">█</span><span style="color:#100e04">█</span><span style="color:#d3b32c">│</span><span style="color:#d3b22c">││││░││░░░░░░░░░░░░</span><span style="color:#d8ad27">░</span><span style="color:#d8ad27">░░░░░░░░░░░░░░░░░░</span><span style="color:#a57f19">▐</span><span style="color:#010000">█</span><span style="color:#000000">█</span><span style="color:#222222">▌</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#1a1a1a">█</span><span style="color:#000000">█</span><span style="color:#000101">█</span><span style="color:#0e3f61">▓</span><span style="color:#145e8f">╬</span><span style="color:#145d8d">╬╬╬╬╬╬╬╬╬</span><span style="color:#010102">█</span><span style="color:#1b1706">█</span><span style="color:#d3b22c">│</span><span style="color:#d4b12c">││░││░░░░░░░░░░░░░░</span><span style="color:#d9ae26">░</span><span style="color:#daae25">░░░░░░░░░░░░░░░░░</span><span style="color:#947117">▄</span><span style="color:#040302">█</span><span style="color:#000000">█</span><span style="color:#131313">█</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#2b2b2b">▀</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#071d2d">█</span><span style="color:#124b71">▓</span><span style="color:#155b8a">╬</span><span style="color:#155a8a">╬╬╬╬╬╬╬</span><span style="color:#010102">█</span><span style="color:#1b1705">█</span><span style="color:#d4b12b">│</span><span style="color:#d4b12b">░│░░░░░░░░░░░░░░░░</span><span style="color:#daae25">░░░░</span><span style="color:#daad25">░░░░░░░░░░░░</span><span style="color:#d1a020">,</span><span style="color:#906e16">▄</span><span style="color:#2d2208">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#323232">▀</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#636363">└</span><span style="color:#242424">▀</span><span style="color:#010101">█</span><span style="color:#000000">█</span><span style="color:#02070a">█</span><span style="color:#071a28">█</span><span style="color:#0a263a">█</span><span style="color:#0a293f">█████</span><span style="color:#010001">█</span><span style="color:#1b1706">█</span><span style="color:#d5b12a">│</span><span style="color:#d5b12a">░░░░░░░░░░░░</span><span style="color:#3f330d">█</span><span style="color:#3a2f0b">███████████████████</span><span style="color:#302407">█</span><span style="color:#110c03">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#0c0c0c">█</span><span style="color:#383838">▀</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#5b5b5b">└</span><span style="color:#3e3e3e">▀</span><span style="color:#2b2b2b">▀</span><span style="color:#212121">▀</span><span style="color:#1d1d1d">▀</span><span style="color:#1d1d1d">▀▀▀</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#1b1706">█</span><span style="color:#d5b02a">░</span><span style="color:#d6b029">░░░░░░░░░░░░</span><span style="color:#bc9621">└</span><span style="color:#bb9620">└└└└└│││││││</span><span style="color:#58440e">╫</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#2b2b2b">▀</span><span style="color:#373737">▀</span><span style="color:#373737">▀▀</span><span style="color:#3c3c3c">▀</span><span style="color:#474747">╙</span><span style="color:#5b5b5b">└</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#010101">█</span><span style="color:#000000">█</span><span style="color:#1c1705">█</span><span style="color:#d6b029">░</span><span style="color:#d6b029">░░░░░░░░░░░░░░░░░░</span><span style="color:#c49a20">Q</span><span style="color:#9d7b1a">▄</span><span style="color:#ae881d">▄</span><span style="color:#daa923">░</span><span style="color:#dcab23">░░░</span><span style="color:#684f10">╫</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#646464">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#010101">█</span><span style="color:#000000">█</span><span style="color:#1c1706">█</span><span style="color:#d6af29">░</span><span style="color:#d6af29">░░░░░░░░░░░░░░░░░</span><span style="color:#675012">▓</span><span style="color:#000000">█</span><span style="color:#000000">██</span><span style="color:#130e04">█</span><span style="color:#d9a822">░</span><span style="color:#ddaa22">░░</span><span style="color:#685010">╫</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#636363">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#161616">█</span><span style="color:#000000">█</span><span style="color:#010101">█</span><span style="color:#ab8b21">▄</span><span style="color:#d7af28">░</span><span style="color:#d8af27">░░░░░░░░░░░░░░░░</span><span style="color:#ab851c">╙</span><span style="color:#302508">█</span><span style="color:#0c0902">█</span><span style="color:#191305">█</span><span style="color:#674f11">▀</span><span style="color:#ddaa22">░</span><span style="color:#ddaa22">░░</span><span style="color:#49370c">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#666666">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#1b1b1b">█</span><span style="color:#000000">█</span><span style="color:#010101">█</span><span style="color:#51410f">█</span><span style="color:#aa891f">▄</span><span style="color:#d7ad27">░</span><span style="color:#d8ad27">░░░░░░░░░░░░░░░░░░░</span><span style="color:#dca921">░</span><span style="color:#a67f1a">▄</span><span style="color:#3d2e0a">█</span><span style="color:#000000">█</span><span style="color:#000000">█</span><span style="color:#363636">▀</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#5c5c5c">╙</span><span style="color:#252525">▀</span><span style="color:#020202">█</span><span style="color:#000000">██</span><span style="color:#312709">█</span><span style="color:#574510">█</span><span style="color:#795f15">▄</span><span style="color:#8d7018">▄</span><span style="color:#a3811c">▄</span><span style="color:#b38d1e">▄</span><span style="color:#bc941f">▄</span><span style="color:#c29820">▄▄▄▄▄▄</span><span style="color:#b38a1c">▄</span><span style="color:#a17c19">▄</span><span style="color:#8e6d16">▄</span><span style="color:#785c13">▓</span><span style="color:#56420e">█</span><span style="color:#2f2407">█</span><span style="color:#040301">█</span><span style="color:#000000">██</span><span style="color:#2b2b2b">▀</span><span style="color:#686868">─</span><br><span style="color:#808080">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color:#646464">└</span><span style="color:#474747">╙</span><span style="color:#303030">▀</span><span style="color:#1d1d1d">▀</span><span style="color:#0e0e0e">█</span><span style="color:#030303">█</span><span style="color:#000000">████████████</span><span style="color:#0f0f0f">█</span><span style="color:#1e1e1e">▀</span><span style="color:#323232">▀</span><span style="color:#494949">╙</span><span style="color:#666666">─</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><span style="color:#808080">&nbsp;</span><br><br></body></html>

1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)
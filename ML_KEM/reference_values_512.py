from ML_KEM.reference_values import RefValues, RefValuesKeygen, RefValuesEncrypt
from ML_KEM.MLKEM_parameters import MLKEM_512, MLKEM_PARAMETER

RefValuesKeygen512 = RefValuesKeygen(MLKEM_PARAMETER.ML_KEM_512)
RefValuesKeygen512.AC = [[[[None] * 256] for i in range(0, MLKEM_512.k)] for j in range(0, MLKEM_512.k)]
RefValuesKeygen512.AC[0][0] = [0x04B4,0x026E,0x033C,0x00FF,0x090E,0x01F9,0x05CB,0x093B,0x0590,0x0670,0x063B,0x0759,0x0A9F,0x08CF,0x01CA,0x01DE,
0x015F,0x03B4,0x0B64,0x0BF8,0x0533,0x0259,0x0964,0x0026,0x0AC8,0x0291,0x026E,0x0816,0x0985,0x0271,0x0350,0x057B,
0x0985,0x0802,0x0B25,0x0420,0x0013,0x04B4,0x00D2,0x053E,0x0CF0,0x0B44,0x07FA,0x02E5,0x076E,0x0871,0x041F,0x063A,
0x08A2,0x0666,0x03F7,0x093B,0x0A5B,0x0210,0x0A4C,0x01C0,0x08E4,0x0875,0x0842,0x0421,0x0424,0x04DE,0x028C,0x01F8,
0x05D0,0x02D5,0x0C0E,0x0AE4,0x0801,0x025B,0x0246,0x085F,0x09DF,0x04BA,0x0181,0x05F9,0x02C5,0x09EE,0x04DC,0x0007,
0x0C3F,0x00C9,0x0C39,0x09E5,0x08E9,0x056F,0x0807,0x0A6B,0x09E1,0x07D5,0x0546,0x0AC8,0x07F3,0x0862,0x0C4F,0x0B3D,
0x09CF,0x00F1,0x0CB2,0x0C8C,0x0334,0x0B32,0x0AE1,0x0B8E,0x0386,0x0B25,0x02C2,0x0225,0x076D,0x0AEB,0x06F2,0x088E,
0x09AE,0x0508,0x007D,0x099B,0x02F0,0x078A,0x0AED,0x0839,0x0A89,0x03CA,0x0C5B,0x0CB6,0x0801,0x027C,0x0849,0x0537,
0x044A,0x0B54,0x05CA,0x0338,0x0840,0x0726,0x0C5F,0x0AA8,0x04B5,0x0CBD,0x0938,0x01C9,0x012D,0x0B4A,0x0AAF,0x0B2E,
0x096D,0x03BF,0x0B6E,0x0701,0x05CB,0x0A36,0x02D7,0x0C4E,0x0655,0x0AF5,0x0AFA,0x0CDD,0x0AE1,0x02B7,0x0213,0x0531,
0x064F,0x00BD,0x0672,0x0796,0x0483,0x08E6,0x055A,0x0C8E,0x0574,0x03A6,0x02A9,0x03C5,0x03B7,0x0940,0x0B4C,0x0B16,
0x06C3,0x0C7C,0x0729,0x0BAB,0x0BB3,0x0329,0x0776,0x06F0,0x06AF,0x0AAA,0x0945,0x0230,0x045D,0x0647,0x02DC,0x0968,
0x061A,0x08AA,0x0213,0x0688,0x081D,0x01AE,0x0A48,0x0064,0x06AD,0x0BA2,0x02EA,0x05FF,0x001D,0x0953,0x0AF3,0x08EA,
0x03B4,0x000A,0x033D,0x073F,0x0855,0x0937,0x0A16,0x080C,0x0509,0x08C6,0x0C76,0x0BAD,0x05F9,0x0CDB,0x0BC4,0x0342,
0x0960,0x079C,0x0802,0x079A,0x0BF0,0x07B1,0x02C3,0x0B8C,0x07FF,0x0AAF,0x0B89,0x051C,0x095F,0x088C,0x0C79,0x0123,
0x007B,0x0439,0x02D5,0x0707,0x0415,0x04A0,0x09D7,0x0B5B,0x0A23,0x0CC3,0x01AA,0x0903,0x09D5,0x0599,0x0CB5,0x07BF,
]
RefValuesKeygen512.AC[0][1] = [0x0CF6,0x0C3C,0x0129,0x0CEB,0x0BFC,0x07D8,0x0A69,0x0305,0x0890,0x0ACE,0x0708,0x05F2,0x0C01,0x09E6,0x096F,0x0B7B,
0x0830,0x0CC0,0x07B7,0x012C,0x0697,0x075B,0x044E,0x00CC,0x0B4C,0x0AC7,0x07EC,0x0230,0x043D,0x0A08,0x03F6,0x0985,
0x0018,0x042B,0x0ADF,0x0933,0x0A90,0x0570,0x09B2,0x060D,0x0192,0x08AF,0x0B96,0x0BD2,0x01AB,0x0060,0x0AD8,0x0190,
0x03B7,0x0BDF,0x021D,0x08C8,0x0436,0x076E,0x060C,0x091C,0x082F,0x0341,0x058A,0x0B1C,0x01B7,0x0B35,0x078D,0x0C00,
0x0322,0x0ACB,0x00B4,0x02D0,0x0BDC,0x069E,0x0B27,0x050F,0x0869,0x0BB5,0x06E3,0x0B1D,0x0917,0x08C0,0x02CD,0x0B9E,
0x02CC,0x0247,0x0131,0x0BBF,0x0340,0x0B16,0x055F,0x090D,0x03B0,0x0749,0x0715,0x0171,0x08F8,0x0CFD,0x0BE2,0x0712,
0x0C6F,0x050E,0x0206,0x077B,0x02C5,0x0411,0x03F3,0x0AC7,0x0677,0x0B47,0x058E,0x0313,0x00E1,0x05C2,0x0A1E,0x0248,
0x0535,0x04FE,0x0B71,0x0ACA,0x06F9,0x0662,0x04A8,0x03E7,0x0249,0x06F6,0x0920,0x024A,0x01F1,0x0AA3,0x0457,0x052A,
0x0A31,0x0931,0x0254,0x07B8,0x0427,0x03A3,0x0C3B,0x05D4,0x01FC,0x0A03,0x08F0,0x0020,0x0972,0x0BCD,0x0931,0x0610,
0x0983,0x00A8,0x02CB,0x0AFD,0x09BB,0x04A4,0x0CC8,0x0CC6,0x05FF,0x02AB,0x0765,0x07B7,0x04E0,0x0805,0x02E7,0x03E5,
0x016C,0x09FF,0x042C,0x02CF,0x0655,0x02B7,0x0823,0x0938,0x00FB,0x0A5B,0x0550,0x05EC,0x059A,0x022D,0x01E4,0x0283,
0x0886,0x0912,0x07CC,0x0361,0x02A9,0x0042,0x09CC,0x0691,0x07F5,0x0743,0x0AAC,0x057D,0x0966,0x0C3C,0x0848,0x0C4D,
0x06D5,0x00AE,0x022B,0x05BC,0x01A0,0x018C,0x072A,0x0A93,0x00E0,0x038E,0x0B9C,0x0156,0x0388,0x09CC,0x0795,0x004E,
0x0A7E,0x087E,0x0C8B,0x09A9,0x05DF,0x077C,0x0431,0x031B,0x0861,0x0C90,0x060C,0x03B1,0x035C,0x03D2,0x0C0F,0x0130,
0x032F,0x0B5F,0x094C,0x02D1,0x0880,0x0877,0x0C78,0x0C19,0x05E9,0x021A,0x01CD,0x0602,0x0CEA,0x0B0E,0x021E,0x0C7E,
0x01A0,0x09A3,0x0539,0x08AD,0x0159,0x025F,0x05D2,0x0181,0x08A7,0x095E,0x0C86,0x00FA,0x007E,0x04CB,0x0606,0x07DC,
]
RefValuesKeygen512.AC[1][0] = [0x0C62,0x0215,0x035B,0x0BFB,0x06DF,0x09FD,0x00AE,0x0291,0x0C62,0x07EA,0x07C0,0x063A,0x0098,0x0722,0x09D6,0x09F1,
0x0356,0x038C,0x010E,0x0AC4,0x00D3,0x018B,0x0388,0x035D,0x05B4,0x04DB,0x063C,0x0BEE,0x06B4,0x0332,0x0A67,0x08F4,
0x06ED,0x04E8,0x0190,0x0CE5,0x0B67,0x06FA,0x0066,0x0351,0x0023,0x087D,0x0A95,0x0902,0x0CD9,0x0C1C,0x06F3,0x0A7C,
0x0CC3,0x01A5,0x0C93,0x0930,0x08AE,0x0A0F,0x0203,0x0A85,0x070E,0x05B6,0x0997,0x0778,0x0238,0x0521,0x01D1,0x0870,
0x0B7E,0x0A92,0x0857,0x09E8,0x06EA,0x01F9,0x04E1,0x07AD,0x0100,0x006E,0x0607,0x0B7B,0x0654,0x06F5,0x0ABC,0x02D8,
0x0859,0x09E4,0x0AA2,0x079B,0x07BB,0x0923,0x0BAB,0x0AC1,0x0742,0x0C84,0x07E0,0x0B0A,0x008B,0x04E2,0x0710,0x0C0B,
0x00E2,0x0A63,0x028A,0x0188,0x0318,0x0843,0x07A6,0x0A1C,0x0200,0x0154,0x0926,0x0BEF,0x08B0,0x00A9,0x05F6,0x0B21,
0x070E,0x0224,0x0219,0x06B4,0x0291,0x0B54,0x06EE,0x08FA,0x0832,0x0165,0x051E,0x0C8E,0x086D,0x091F,0x03AB,0x0086,
0x07A9,0x0A7E,0x005F,0x092F,0x06AA,0x0995,0x0844,0x0055,0x05ED,0x002E,0x044D,0x03B5,0x0777,0x08D1,0x0456,0x0091,
0x0A70,0x004D,0x0246,0x0A9C,0x0BFF,0x074D,0x076E,0x013E,0x01DC,0x09B0,0x0803,0x036D,0x0C65,0x03BC,0x0736,0x0310,
0x07B9,0x0564,0x0602,0x0756,0x051B,0x0839,0x080B,0x04C3,0x034A,0x04A1,0x04EE,0x0357,0x04CB,0x02CA,0x0512,0x047B,
0x06BB,0x04BD,0x0AF9,0x06E3,0x0673,0x09BD,0x01A2,0x09AC,0x0170,0x0CD3,0x020E,0x0CD7,0x0512,0x02B6,0x04AC,0x041A,
0x0B5C,0x094C,0x0035,0x00D7,0x067D,0x04F1,0x01F0,0x03F5,0x0169,0x094C,0x0799,0x0171,0x0439,0x06ED,0x02A8,0x04EB,
0x09D9,0x0AA4,0x09DA,0x01F7,0x038A,0x04D3,0x070B,0x0949,0x0BAD,0x009D,0x01D3,0x0762,0x054D,0x013F,0x0A17,0x03E7,
0x045E,0x0646,0x0804,0x0C15,0x08D7,0x02FF,0x02C4,0x09DB,0x0005,0x08F6,0x0670,0x03EA,0x0513,0x0327,0x026A,0x0116,
0x020C,0x0C58,0x0CF9,0x0556,0x013D,0x08D7,0x0B4E,0x04FE,0x0A0F,0x0904,0x04CE,0x00A6,0x021F,0x0867,0x0915,0x05E3,
]
RefValuesKeygen512.AC[1][1] = [0x051F,0x03F8,0x0AFC,0x060B,0x0786,0x0845,0x0A7D,0x0AF8,0x0AE6,0x05CC,0x03FE,0x0483,0x01BF,0x0241,0x044C,0x0945,
0x054B,0x07BE,0x060E,0x0630,0x020E,0x08F0,0x075F,0x0656,0x0BEA,0x033C,0x0389,0x0AD1,0x0C98,0x0925,0x07EE,0x0529,
0x0788,0x03D8,0x0905,0x0BB5,0x0CE7,0x099E,0x0B88,0x0985,0x0768,0x07FF,0x06F2,0x07EF,0x0BD4,0x07A1,0x04A1,0x03C2,
0x0AA1,0x0327,0x0850,0x027E,0x05F5,0x05D1,0x06FE,0x0804,0x06C1,0x066C,0x09BE,0x0553,0x02F7,0x0543,0x0A4E,0x0117,
0x0AA3,0x030F,0x079B,0x0433,0x035A,0x009C,0x083B,0x0CFE,0x079D,0x060E,0x0019,0x085F,0x08EA,0x029C,0x0B6D,0x0157,
0x0B07,0x0A49,0x01A8,0x00BF,0x0B56,0x05A6,0x02F5,0x0CAE,0x04CC,0x03BF,0x03AD,0x0A6D,0x0BE0,0x0A5F,0x08B6,0x0983,
0x056D,0x05A5,0x04E4,0x0CEB,0x085F,0x0988,0x000E,0x03F2,0x0BAC,0x0963,0x0C34,0x047F,0x09DF,0x0B3A,0x0CE8,0x036B,
0x0436,0x01D6,0x016E,0x0C8E,0x0AEA,0x0649,0x0656,0x030D,0x0618,0x052C,0x0066,0x02B4,0x04A4,0x069D,0x0A88,0x0976,
0x0327,0x0457,0x0655,0x0493,0x05F1,0x0591,0x09E5,0x0823,0x0794,0x0167,0x019A,0x0A96,0x04B0,0x0C3B,0x0AAB,0x09AE,
0x05AE,0x098D,0x072A,0x0AB9,0x04E6,0x0498,0x0BF2,0x0557,0x0452,0x0B23,0x03AA,0x0A10,0x0095,0x09F9,0x0A48,0x0691,
0x0145,0x0AE0,0x02EE,0x03DC,0x025F,0x04A1,0x0BFD,0x0C03,0x0490,0x010C,0x0760,0x0A72,0x0BD9,0x040A,0x0150,0x0563,
0x054E,0x049B,0x0C00,0x0118,0x033A,0x0793,0x02A9,0x054E,0x06AB,0x055E,0x0845,0x007E,0x00D7,0x074B,0x03CD,0x03A3,
0x08B6,0x009A,0x0669,0x0383,0x018C,0x05AE,0x0816,0x0031,0x0460,0x0479,0x086F,0x0C79,0x03AA,0x0367,0x02B5,0x03BD,
0x0755,0x0329,0x0067,0x053D,0x013E,0x0063,0x0BE1,0x0A4A,0x04AA,0x03D6,0x0B55,0x0CB0,0x00A7,0x07CD,0x01B5,0x0B59,
0x0572,0x08DA,0x05B1,0x0051,0x04CB,0x0308,0x049F,0x0298,0x04C1,0x0B6F,0x0133,0x096B,0x0665,0x06D4,0x0C45,0x0BC9,
0x034B,0x0C9C,0x06D3,0x07BC,0x068E,0x0959,0x0B3C,0x01BF,0x02F4,0x0795,0x0B87,0x04E4,0x0116,0x07CA,0x038D,0x0A08,
]

RefValuesKeygen512.SC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.SC[0] = [-2,1,0,-1,0,1,2,0,3,1,0,0,0,1,1,2,
2,2,0,2,-2,-2,2,1,0,-2,-2,1,0,-1,0,0,
2,1,-3,2,-1,-1,-1,2,2,1,0,-1,-1,-2,2,0,
0,3,0,-1,-1,1,0,1,-2,1,1,2,-1,2,2,1,
2,1,1,1,2,0,0,-1,0,-1,-1,1,0,-1,-1,0,
0,1,0,0,0,0,-3,1,-1,2,-1,-2,1,0,-1,2,
1,2,-1,1,0,0,1,-2,1,0,2,1,-1,-1,0,0,
0,-1,0,-1,0,-1,0,-1,-1,-1,2,-1,1,0,-1,1,
-1,1,0,-1,-2,-2,1,0,-2,1,-1,0,0,-2,0,1,
-1,-2,-1,2,-1,-1,2,-1,-1,1,1,2,-1,-1,1,1,
-1,1,-1,0,-2,3,0,0,0,1,-3,-1,0,0,-1,-2,
0,1,1,-2,0,-1,0,-1,1,3,1,0,0,-1,0,0,
-1,0,1,-1,0,0,0,0,-2,-1,1,-1,2,0,0,2,
1,2,0,-1,0,1,0,0,0,2,0,1,0,-1,1,1,
-1,0,-1,1,1,-1,1,2,0,2,-1,2,1,1,-1,-1,
1,0,1,0,-1,-1,-1,-2,3,-1,-1,-1,1,0,-1,0,
]
RefValuesKeygen512.SC[1] = [1,1,0,0,1,1,-2,-1,1,-1,0,-1,0,-1,1,1,
0,-2,0,1,-1,1,3,-1,1,0,1,1,-1,-2,-1,-2,
-1,-1,0,0,0,0,2,0,1,1,-1,0,-2,1,-1,-1,
3,1,1,1,1,0,1,0,-1,0,-2,-2,1,-1,1,-3,
0,-1,-3,0,1,-1,0,1,1,0,3,-2,1,0,-1,0,
-1,0,1,0,-1,0,0,0,1,1,1,0,-1,1,1,-1,
-2,1,-1,2,0,0,-1,-2,1,1,1,2,-2,1,-2,-1,
1,-2,-1,1,-1,1,0,0,-2,0,1,0,2,1,-1,3,
0,-1,0,1,2,0,-1,0,-2,-1,2,1,-1,2,1,0,
-1,0,-1,0,-1,-1,0,0,0,0,-1,0,0,-1,1,1,
1,1,-1,-1,-1,-1,1,1,0,-2,0,1,0,1,1,-1,
-2,-1,1,2,1,1,-1,0,0,-1,1,0,1,-1,1,-2,
0,-1,-1,1,3,0,1,1,-3,1,-1,0,1,0,-1,0,
0,2,-1,0,-1,0,1,0,1,-1,0,0,2,-1,1,2,
-1,1,2,1,-1,0,1,0,0,0,0,-2,0,0,-1,-1,
-1,0,2,0,0,-1,2,1,1,1,0,0,-1,0,-2,1,
]

RefValuesKeygen512.EC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.EC[0] = [1,0,0,0,1,0,-1,0,-1,-1,0,2,1,0,0,-1,
0,1,-1,0,-1,-1,-1,-1,2,2,0,-2,0,1,-1,0,
1,0,2,-2,-1,-2,-1,0,-1,-2,1,1,2,-1,-2,2,
3,1,0,-1,-1,0,0,1,0,1,0,0,0,0,0,1,
1,0,2,2,2,2,2,-1,-3,1,2,1,0,-1,2,-2,
3,-3,0,-1,-1,1,-1,-1,0,0,-1,0,-2,1,-1,1,
1,-1,-1,-1,-2,1,0,2,-2,2,0,0,0,-2,-3,1,
1,0,0,0,1,0,0,1,-1,0,-1,0,-1,0,-2,0,
-1,-1,3,2,-1,1,1,0,1,0,0,1,0,-1,-2,-1,
-2,-2,1,3,-1,0,-1,2,0,0,0,-1,1,1,0,1,
-2,-1,0,0,1,-1,-2,1,1,-3,0,2,-1,-3,1,0,
1,-1,2,0,0,0,2,2,1,0,1,0,1,-1,2,1,
-1,-2,1,1,0,1,2,-1,-2,1,0,-1,0,-1,-1,1,
-1,1,-1,-2,0,-2,-1,0,-2,-2,2,-1,-2,1,0,-1,
0,2,1,-1,0,0,-1,1,0,0,0,1,-2,1,0,-1,
2,-1,1,1,-1,1,-3,-2,-1,-1,-2,0,-1,1,0,-1,
]
RefValuesKeygen512.EC[1] = [0,-2,-1,-2,1,0,-1,-3,1,1,0,1,-1,-1,1,2,
-1,-1,1,-1,1,1,0,-1,0,0,0,0,-1,1,0,-1,
0,-1,-1,0,1,1,1,0,2,0,0,0,0,0,-1,-1,
-1,0,1,3,1,0,0,-1,-2,2,1,0,1,0,-2,1,
0,1,2,-1,0,2,-1,-2,2,1,-1,2,1,-1,-2,1,
2,-1,-1,0,-1,-1,-3,0,1,-1,0,0,0,0,1,-2,
1,-2,0,0,1,0,0,2,0,-2,-1,1,0,0,-1,0,
0,1,-1,0,-1,-1,0,-1,0,1,-1,2,3,-1,0,-1,
-1,-2,-1,-1,0,0,2,1,2,1,-1,-2,0,0,0,1,
1,0,0,-1,0,0,0,1,0,0,0,1,1,2,-1,1,
1,0,0,1,0,-1,-1,1,1,2,0,0,2,0,1,0,
0,-1,0,1,-1,0,1,0,0,0,1,1,1,2,-1,-1,
-2,-1,0,2,0,-1,2,1,0,0,0,1,1,-1,-2,0,
0,0,0,-1,-2,0,2,1,0,1,-1,-1,1,2,-1,-2,
0,1,-1,0,-1,1,0,0,0,0,1,0,-1,0,2,0,
1,1,-1,0,0,2,3,-1,2,1,-1,1,-2,-1,-2,2,
]

RefValuesKeygen512.SHC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.SHC[0] = [-1539,120,-829,579,1120,-36,1617,-422,-236,700,-312,-498,1491,39,836,-264,
23,-282,-1011,-886,-482,-1475,972,1432,1267,-718,1162,1250,288,-758,-762,140,
-1094,1291,1457,-414,1291,1077,-324,149,-969,-62,-702,-844,1599,-1020,-225,91,
-1584,-901,-1081,-1188,1478,469,239,-1520,873,581,842,-1550,1363,1127,1041,-1434,
345,77,452,626,-1478,-1475,156,-1380,-801,69,-756,1646,-896,-100,1390,1074,
467,-230,-571,715,411,-1183,936,-763,-1088,454,-1652,1105,-645,-1592,1229,1267,
-1308,375,-1406,551,677,-901,-994,-1592,-1227,-717,1066,1373,908,106,-497,-747,
-240,-1416,-1023,1353,-966,1018,22,-1296,-735,314,-1160,-1186,85,-976,563,-466,
-639,225,988,-1614,139,-450,-1537,1564,-1491,942,1368,1219,1152,639,-1454,-1147,
-1635,-368,169,-187,-787,897,1371,-79,874,1267,-523,796,-927,1030,-63,-912,
-952,610,-625,967,-255,-885,-1380,1358,793,925,-1094,-859,-95,-46,607,-870,
893,-1484,-8,-1157,1433,582,-1116,875,1261,-44,892,-13,-1328,-342,745,-93,
-1377,-245,853,9,1512,-845,-1343,397,1370,881,-811,-222,-1078,-1634,649,984,
315,-1112,1365,0,-1032,-871,-458,-1599,263,-1258,1448,1168,-105,-51,-77,1522,
-1248,-637,-1606,990,-407,1480,925,-359,1621,-154,389,-1244,-1344,-129,-1219,-618,
-747,223,1010,840,1660,-36,-1486,1380,384,-1574,-252,-990,1664,1160,-272,-1537,
]
RefValuesKeygen512.SHC[1] = [1364,451,1094,-584,-971,701,391,1364,1601,-669,-693,699,325,-36,-1363,-736,
593,-630,633,-1452,1345,1574,1218,-1115,1391,390,-1174,-925,-926,284,-1419,717,
-736,862,1155,-667,-1570,-616,-1094,-1432,487,-240,933,-1260,-835,1019,-1091,1314,
1626,-1036,-349,-273,761,289,1397,344,-1600,-1089,274,-1085,-1270,481,-1465,-60,
-1175,-9,240,967,-1320,1362,1305,1481,-1473,-86,-1609,636,887,-1349,1600,190,
535,1306,336,86,-1566,-1360,1235,742,-968,-998,-1074,1103,-66,-746,825,731,
-1439,723,-319,-868,1262,959,555,985,-1074,598,1317,450,744,-1451,423,355,
-358,985,-523,1443,894,-100,602,-804,-963,105,-1394,-294,-1038,608,302,1589,
-539,563,914,-803,540,-402,-325,767,363,1142,-674,-46,-1569,1270,-109,683,
1191,-1053,-570,266,144,-544,19,-316,-986,-865,1256,-687,-1582,1658,-803,-822,
839,-1418,928,-915,1558,757,1290,-839,-704,1194,233,639,-639,-485,1216,-459,
1344,-1058,-1396,-463,1139,420,-751,-82,-880,19,-615,-750,13,641,-813,-629,
-82,-1582,-684,-544,619,731,-213,847,-773,-399,519,-772,-572,-1331,-1273,-388,
1260,-1252,1137,1123,1571,-364,1628,50,1638,1146,662,1499,1423,-949,772,-177,
-984,-1234,-889,220,-999,-93,202,-794,968,-1098,-447,707,-704,612,1304,-1302,
228,-109,-614,211,-184,-167,-506,-968,-920,119,-978,-870,-1357,-480,1609,1101,
]

RefValuesKeygen512.EHC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.EHC [0] = [586,296,-41,1585,-674,-41,-488,14,-232,-931,554,-107,-330,494,475,548,
-348,-1080,153,276,1473,1501,-1648,-1079,1109,199,-1264,1076,924,1517,-93,-671,
726,17,-506,1267,775,623,-1230,-698,1450,-1311,-1200,728,323,-1193,691,-619,
-921,-99,-1569,-1636,906,-738,-222,-666,-1457,185,-672,1260,1124,-736,209,515,
-610,-749,-1205,827,863,-531,-684,-187,-100,331,-826,-25,-1406,-508,944,530,
30,-1512,-1011,-765,-1532,934,-1210,-441,-811,-860,-1371,-1140,-1219,617,1662,1196,
783,-270,906,-145,-1416,600,-1604,-1563,1173,258,-1342,646,-86,-594,-1066,-853,
1237,415,-1071,-533,-497,292,528,-819,1337,421,-235,614,160,1310,374,1209,
-1574,847,-578,-169,506,1122,1546,1159,-328,-452,95,1166,-1339,691,969,487,
138,436,-1466,-974,394,315,-273,50,-137,83,198,1091,1455,85,1370,-1478,
774,465,-1475,325,440,-1165,1019,-1390,-1607,1598,441,-48,-644,931,304,-1442,
-1095,259,539,1328,-316,768,-958,-928,480,1180,-379,-872,-127,-263,-220,1518,
1287,41,-87,1481,1103,-318,-16,-506,1351,-1349,-579,-1352,636,-77,946,-1151,
366,1605,54,637,-1211,1321,-1495,-1176,734,-1158,-1368,-267,648,700,214,-558,
-1048,-101,494,920,-917,1260,-1586,-1251,838,-202,-1653,-525,927,-354,-326,-1469,
374,-920,-716,446,-856,-1170,-95,-1633,-986,-1460,1249,-247,-1318,1143,-911,-1563,
]
RefValuesKeygen512.EHC [1] = [-483,-977,-287,-1560,1282,-483,-495,418,611,1647,-1152,729,1455,401,1059,710,
-452,103,-1388,1320,-384,-798,-236,464,1048,-1395,-90,468,268,-1137,-24,441,
-514,699,1449,288,-815,408,367,245,1231,491,-1452,-633,586,696,-1408,-997,
389,307,348,484,-917,775,1482,-1416,750,-960,-1297,1397,761,-1249,-1196,-1134,
-973,-1557,-174,-1663,-991,1509,1503,-296,1392,724,-258,65,323,838,-381,-1105,
901,1597,-509,-842,-826,589,-796,-549,-62,642,1104,1082,302,1547,1215,811,
1112,-216,1183,-102,-1500,755,-1007,652,-1604,1469,1154,457,1426,-887,-456,-576,
-1178,80,-697,141,-708,-702,-42,1422,471,-1295,981,986,-1021,-1395,-1179,999,
-584,644,1490,-810,-126,832,367,1378,-1115,939,358,-1573,1649,-704,-261,1527,
1045,1254,1217,59,-1478,1380,-430,984,-755,-412,375,966,1320,1270,-622,5,
1583,-598,663,1066,768,-469,-1136,1222,-1480,352,-658,-764,333,855,525,1264,
-999,616,-1017,-248,-621,1550,-778,-186,-1190,489,-1646,1208,1201,-1389,-1262,729,
-765,1550,-56,590,-1197,-1156,-1454,714,270,260,240,1013,1435,934,-37,-688,
-1155,-51,1163,-1003,188,-1103,1130,-1012,1264,-94,-1597,993,717,-1390,705,-325,
648,575,-872,564,174,-771,1349,-381,-616,-207,-866,-685,951,490,-904,375,
-632,783,-1151,390,-415,-182,-1291,-1554,-528,-1562,-496,1385,-718,-310,-1408,-121,
]

RefValuesKeygen512.ASC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.ASC[0] = [1107,-1193,-563,592,906,607,-1565,-1599,-589,1102,250,738,-1378,-56,-195,1565,
-318,-1404,425,39,990,-1112,713,-873,993,1354,200,345,880,1393,-1500,443,
-663,-975,-1445,-529,-1346,759,1356,294,-1224,226,-310,-1640,-877,-546,636,-875,
-1096,-443,-1191,1422,-659,923,-1434,525,1224,955,-467,-75,134,-255,-623,26,
552,530,-1240,145,1309,-512,-904,-195,-361,-1606,-1057,-396,-612,1333,1349,-1459,
896,624,584,-147,142,756,610,-313,299,1038,1445,423,171,-1355,1148,-260,
538,360,-1300,-758,115,-705,214,132,52,207,-570,-1508,-893,781,276,1590,
-1270,323,188,-510,-1487,357,1144,-694,-1181,620,1436,-1378,-1135,785,-1308,351,
-543,-612,1162,-685,-1209,-1422,1131,313,334,578,-938,-406,286,1606,-1457,-1422,
514,476,-484,477,277,-153,-815,343,382,756,368,169,-1149,317,1679,1419,
427,-757,821,-1426,-992,1094,-1129,239,-923,-708,-1501,1033,226,1494,1287,-612,
-1195,-1134,-975,1400,-799,1161,918,-1167,-1049,-999,-371,-918,1164,-1028,-1160,-554,
1478,510,686,-1539,268,258,-1096,-132,-383,-1077,1260,1357,-173,1448,-929,1175,
-852,-171,1137,1477,-1618,1563,822,963,-367,495,52,1018,760,-1114,385,479,
-884,-230,-1260,-1389,-1343,-607,-138,-955,393,1581,-420,-868,-908,-48,1115,1316,
772,45,1236,-513,486,805,1402,-607,-767,1209,150,1253,-95,38,472,-1638,
]
RefValuesKeygen512.ASC[1] = [764,-800,1457,-901,1444,1094,-218,26,209,-166,1008,-109,515,368,-1557,-1156,
1114,-1467,302,972,1546,1431,-892,-1047,1127,1580,149,1044,-311,-310,812,1658,
-460,-1662,-1205,601,-1409,-1084,24,801,1328,-1328,-210,568,1120,875,527,-1043,
429,-532,-881,376,87,181,194,915,644,-516,738,-434,718,-1110,1123,-610,
-1660,-813,-1005,-450,1628,-913,983,1682,-1505,-1157,-510,1651,740,797,116,1084,
-1549,625,-152,-316,377,-864,1244,1233,-1015,813,-735,1652,-1343,1539,1301,1397,
1582,-812,25,-1042,1365,298,-709,1405,-1336,-336,-47,-575,620,-707,-566,-814,
-1286,-915,1061,-1196,1651,-1460,661,180,-1044,900,985,-1371,-1014,1049,-219,-686,
185,-1463,-546,611,1090,974,1351,400,1453,1048,-1080,-680,302,-116,428,1314,
277,-1236,-1005,-914,602,-1376,-1534,1178,1217,1536,107,-124,701,-1659,9,213,
-293,-563,85,1483,-240,-277,-885,-976,-720,1613,1144,-201,-1352,1059,-763,1026,
443,-969,-161,-608,-1426,1351,922,-1019,-586,819,1638,1564,646,1636,-1606,1192,
1215,-10,-55,1194,517,847,-212,60,-1621,-399,1603,-1592,-473,-1397,552,-934,
445,-220,831,10,-768,163,8,-850,-1433,336,1043,349,945,571,-834,882,
-884,1593,-956,-844,392,531,-962,-578,-457,1660,1595,-949,-1096,478,1366,-693,
-3,-1651,1333,-145,829,-1431,1299,-63,276,1135,-1109,-1265,909,1627,-594,787,
]

RefValuesKeygen512.ASEC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.ASEC[0] = [-1636,-897,-604,-1152,232,566,1276,-1585,-821,171,804,631,1621,438,280,-1216,
-666,845,578,315,-866,389,-935,1377,-1227,1553,-1064,1421,-1525,-419,-1593,-228,
63,-958,1378,738,-571,1382,126,-404,226,-1085,-1510,-912,-554,1590,1327,-1494,
1312,-542,569,-214,247,185,-1656,-141,-233,1140,-1139,1185,1258,-991,-414,541,
-58,-219,884,972,-1157,-1043,-1588,-382,-461,-1275,1446,-421,1311,825,-1036,-929,
926,-888,-427,-912,-1390,-1639,-600,-754,-512,178,74,-717,-1048,-738,-519,936,
1321,90,-394,-903,-1301,-105,-1390,-1431,1225,465,1417,-862,-979,187,-790,737,
-33,738,-883,-1043,1345,649,-1657,-1513,156,1041,1201,-764,-975,-1234,-934,1560,
1212,235,584,-854,-703,-300,-652,1472,6,126,-843,760,-1053,-1032,-488,-935,
652,912,1379,-497,671,162,-1088,393,245,839,566,1260,306,402,-280,-59,
1201,-292,-654,-1101,-552,-71,-110,-1151,799,890,-1060,985,-418,-904,1591,1275,
1039,-875,-436,-601,-1115,-1400,-40,1234,-569,181,-750,1539,1037,-1291,-1380,964,
-564,551,599,-58,1371,-60,-1112,-638,968,903,681,5,463,1371,17,24,
-486,1434,1191,-1215,500,-445,-673,-213,367,-663,-1316,751,1408,-414,599,-79,
1397,-331,-766,-469,1069,653,1605,1123,1231,1379,1256,-1393,19,-402,789,-153,
1146,-875,520,-67,-370,-365,1307,1089,1576,-251,1399,1006,-1413,1181,-439,128,
]
RefValuesKeygen512.ASEC[1] = [281,1552,1170,868,-603,611,-713,444,820,1481,-144,620,-1359,769,-498,-446,
662,-1364,-1086,-1037,1162,633,-1128,-583,-1154,185,59,1512,-43,-1447,788,-1230,
-974,-963,244,889,1105,-676,391,1046,-770,-837,-1662,-65,-1623,1571,-881,1289,
818,-225,-533,860,-830,956,-1653,-501,1394,-1476,-559,963,1479,970,-73,1585,
696,959,-1179,1216,637,596,-843,1386,-113,-433,-768,-1613,1063,1635,-265,-21,
-648,-1107,-661,-1158,-449,-275,448,684,-1077,1455,369,-595,-1041,-243,-813,-1121,
-635,-1028,1208,-1144,-135,1053,1613,-1272,389,1133,1107,-118,-1283,-1594,-1022,-1390,
865,-835,364,-1055,943,1167,619,1602,-573,-395,-1363,-385,1294,-346,-1398,313,
-399,-819,944,-199,964,-1523,-1611,-1551,338,-1342,-722,1076,-1378,-820,167,-488,
1322,18,212,-855,-876,4,1365,-1167,462,1124,482,842,-1308,-389,-613,218,
1290,-1161,748,-780,528,-746,1308,246,1129,-1364,486,-965,-1019,-1415,-238,-1039,
-556,-353,-1178,-856,1282,-428,144,-1205,1553,1308,-8,-557,-1482,247,461,-1408,
450,1540,-111,-1545,-680,-309,1663,774,-1351,-139,-1486,-579,962,-463,515,-1622,
-710,-271,-1335,-993,-580,-940,1138,1467,-169,242,-554,1342,1662,-819,-129,557,
-236,-1161,1501,-280,566,-240,387,-959,-1073,1453,729,-1634,-145,968,462,-318,
-635,-868,182,245,414,-1613,8,-1617,-252,-427,-1605,120,191,1317,1327,666,
]

RefValuesKeygen512.PKC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesKeygen512.PKC[0] = [-1636,-897,-604,-1152,232,566,1276,-1585,-821,171,804,631,1621,438,280,-1216,
-666,845,578,315,-866,389,-935,1377,-1227,1553,-1064,1421,-1525,-419,-1593,-228,
63,-958,1378,738,-571,1382,126,-404,226,-1085,-1510,-912,-554,1590,1327,-1494,
1312,-542,569,-214,247,185,-1656,-141,-233,1140,-1139,1185,1258,-991,-414,541,
-58,-219,884,972,-1157,-1043,-1588,-382,-461,-1275,1446,-421,1311,825,-1036,-929,
926,-888,-427,-912,-1390,-1639,-600,-754,-512,178,74,-717,-1048,-738,-519,936,
1321,90,-394,-903,-1301,-105,-1390,-1431,1225,465,1417,-862,-979,187,-790,737,
-33,738,-883,-1043,1345,649,-1657,-1513,156,1041,1201,-764,-975,-1234,-934,1560,
1212,235,584,-854,-703,-300,-652,1472,6,126,-843,760,-1053,-1032,-488,-935,
652,912,1379,-497,671,162,-1088,393,245,839,566,1260,306,402,-280,-59,
1201,-292,-654,-1101,-552,-71,-110,-1151,799,890,-1060,985,-418,-904,1591,1275,
1039,-875,-436,-601,-1115,-1400,-40,1234,-569,181,-750,1539,1037,-1291,-1380,964,
-564,551,599,-58,1371,-60,-1112,-638,968,903,681,5,463,1371,17,24,
-486,1434,1191,-1215,500,-445,-673,-213,367,-663,-1316,751,1408,-414,599,-79,
1397,-331,-766,-469,1069,653,1605,1123,1231,1379,1256,-1393,19,-402,789,-153,
1146,-875,520,-67,-370,-365,1307,1089,1576,-251,1399,1006,-1413,1181,-439,128,
]
RefValuesKeygen512.PKC[1] = [281,1552,1170,868,-603,611,-713,444,820,1481,-144,620,-1359,769,-498,-446,
662,-1364,-1086,-1037,1162,633,-1128,-583,-1154,185,59,1512,-43,-1447,788,-1230,
-974,-963,244,889,1105,-676,391,1046,-770,-837,-1662,-65,-1623,1571,-881,1289,
818,-225,-533,860,-830,956,-1653,-501,1394,-1476,-559,963,1479,970,-73,1585,
696,959,-1179,1216,637,596,-843,1386,-113,-433,-768,-1613,1063,1635,-265,-21,
-648,-1107,-661,-1158,-449,-275,448,684,-1077,1455,369,-595,-1041,-243,-813,-1121,
-635,-1028,1208,-1144,-135,1053,1613,-1272,389,1133,1107,-118,-1283,-1594,-1022,-1390,
865,-835,364,-1055,943,1167,619,1602,-573,-395,-1363,-385,1294,-346,-1398,313,
-399,-819,944,-199,964,-1523,-1611,-1551,338,-1342,-722,1076,-1378,-820,167,-488,
1322,18,212,-855,-876,4,1365,-1167,462,1124,482,842,-1308,-389,-613,218,
1290,-1161,748,-780,528,-746,1308,246,1129,-1364,486,-965,-1019,-1415,-238,-1039,
-556,-353,-1178,-856,1282,-428,144,-1205,1553,1308,-8,-557,-1482,247,461,-1408,
450,1540,-111,-1545,-680,-309,1663,774,-1351,-139,-1486,-579,962,-463,515,-1622,
-710,-271,-1335,-993,-580,-940,1138,1467,-169,242,-554,1342,1662,-819,-129,557,
-236,-1161,1501,-280,566,-240,387,-959,-1073,1453,729,-1634,-145,968,462,-318,
-635,-868,182,245,414,-1613,8,-1617,-252,-427,-1605,120,191,1317,1327,666,
]

RefValuesKeygen512.SKPC = int(
        'FE8607C4392460D4CD51B6B515CC2BC9FBB0D375024493BF1770BE0EB9981FEB73CC8359F334A38A'
        '244E20B1A007CA08BBB850B135B60B5543BD5B093839CC435A9B3F569020BC05D1C697C8D885C6551D'
        'EF10716953244A336F53754611747659D104C421273BE7739CD079E059040DEA6681D9C96E2543D3B1'
        'C1C6BA2C9B2186A863A0C1681C8D16457C9A6CCD344FE57717837722A5C2971F996C3648A32AD4558C'
        'A306106BA1119C770299543BA93F16107F22AA1379F88555109333F2B2821A0EDC336B8BF0B300C761'
        '2EE73A58354C80F4275367889E16B9A960C4EE19385B25CB6A334FF6CA31626940C21C97492926907A'
        '3C02CC989DE75419D339BB689AA23CCD5FB2997D5373F9CC87996524A5B836ED54CD7C43CFD1B7BAE9'
        '42CAA0C7C0559300E8459BC2D7185A1537D639C2CBF86989823D3B918A550500F9A899372B6C077181'
        'A8054998ECCCB42C5F2148A8BBE63D6A8B5C9DA3B95576C6855182C107C83E78A916FA0DF283347CD6'
        'CD33475680B16D053C92808648F10B7054351C4694AB36D92B8741554146A64CBA2B45D1CDAE17A251'
        'B2A8795275416562C2648A6F65186B489663C91176D72C21EA358364A6DF96A9BB9876E711C1A55381'
        'BEB93FBE28525A568FA40BBFF91212758515C1068C12418C0B181E4857CC6A88CFF0703CD927551995'
        '5C40B7CAB8C62777C37B40E60B17A251506105E3167BD3642E39B991CFF844BF7CA139B32D62372DC2'
        'DB99EEF43B2B923DCF682525251CE86275A731169B9B3DF63A5A7ED3C95AD29D3E99068FB7BDF30826'
        '2E5163E63A2392E39D1CF2B6BCFB2F6B61475F3ACDE0664F94BC2AA7448EC7AA109010AE1350BC2709'
        '9AE824A5D3A667DEB99C477377A0E39616562F0AA59B41AA4AE9F02782CAB1C064B340F58D8D27B373'
        '441A12FACA9139019A3AA10D1028D4C9A8AF3C6D551AAE6BB22D2CFC34FC29B707D29FC5EA7C08D8B7'
        'ECD4817134462356B95C260366A64796B25D8FC5940403C529F98288C90D1A49CACA709EC8738B423B'
        '2C414A2618B57EE440C99B3A0D49ACC5079B936979072FB999B417B249D644'
        , base=16).to_bytes(MLKEM_512.dkPKElen, 'big')

RefValuesKeygen512.PKPC = int(
        '9D0698A51A88E86023FC046DCCB90A24732755661B18118467DA3442B2139F59185A1956361861D9D85'
        '80CE7B5C8D6C13F309462252EC66A567ED0B6E2408C1B1797D76A632FB5722035AE39B2C2F7900B8946C7'
        '184C478E184AEA249263DB21C76CC274C33C7CE88ECD36B8346B80A6C5B51F9533F508969E9398561B979'
        '3A769A9FAA0012B0B4A40A3E9F8A1FA8A3A29A50577AB97EC87C993A776C9141D89359A2EB90BEB192EE0'
        '2C2E8EE98E4195288886719C1041B154A032F9825B8961BCB40E48B29A425ABD750A5C06E007B6892FE49'
        '88F19AB958C02396305B19F220AC19818F5703436C24E322119E96BCCB1D4BD734A8BD9AACB932C881FA3'
        '37DD983D5F9B9737B64F0F64994D8BAAA69878D92C4DC85A0B133A600D647F9D473CCD7A225772CC5B55C'
        'CA938A8C87338A95200CFB1551180011BAB59A72484F441B460CAC26FA1A6DDF72E8035B65722CB7565BB'
        '03CAB22DD428453646CF3456E8047913F0B61583C67A649908E2CB8F4BB91B15442866C077E53E7CD7494'
        'A0B08190161924436A63A2638CA1B34935C71CC26B217300F3BB496D27AC3488F8A942799A8AB7F980B3B'
        '805ED6AC7514338333E993F4903751D4A5876141FFC99B8306CCAA36629099503203C2ECCA35C3C93B8CC'
        '6B072D573D23A3CC7A53CB81C63B8F23B66084C7D4225B6A956900CB5014A6B273466F8CBCE79EA8A6CBA'
        '8740EBBEC0C12ACCF85A71E1AAF0E8C0D4098A86DA8FB894887ADC414D968085D14653B4C8FE776C03397'
        '961E39B6C218EAFF3486B2264C46AB7AE07B80E75BA8B971372EB9CB0A3C3C4E370B6266F52317C2F4A43'
        '9FD79CA790B12A2501D4A09A954900552587CE4146E2A134E5C7B79CAA0D0A8587EC529F1072A11C650F6'
        '9D47AE6C19306A977132C8FD50ABA67989A0255B590C08411C651F94CAD37770FCD1178C24160928C6F59'
        'CABC7F6630BA67C733E7ABC223B303B26A3B2ABFCA0792BD5A9572B45B582C0FD7EA537EE69C80DC22158'
        'C87DD95BE3612C1832194D0D85AD9F269708C3CCE31BC86DA99B6500F9E416B08006B056CB5BC8607BF50'
        '522FA529855DD1E6847BB6E28483F21626785165F707ABEFE6571F4E39FB01EA88302353'
        , base=16).to_bytes(MLKEM_512.ekPKElen, 'big')

RefValuesEncrypt512 = RefValuesEncrypt(MLKEM_PARAMETER.ML_KEM_512)
RefValuesEncrypt512.PKC = [[None] for i in range(0, MLKEM_512.k)]
RefValuesEncrypt512.PKC[0] = [1693,2432,2725,2177,232,566,1276,1744,2508,171,804,631,1621,438,280,2113,
2663,845,578,315,2463,389,2394,1377,2102,1553,2265,1421,1804,2910,1736,3101,
63,2371,1378,738,2758,1382,126,2925,226,2244,1819,2417,2775,1590,1327,1835,
1312,2787,569,3115,247,185,1673,3188,3096,1140,2190,1185,1258,2338,2915,541,
3271,3110,884,972,2172,2286,1741,2947,2868,2054,1446,2908,1311,825,2293,2400,
926,2441,2902,2417,1939,1690,2729,2575,2817,178,74,2612,2281,2591,2810,936,
1321,90,2935,2426,2028,3224,1939,1898,1225,465,1417,2467,2350,187,2539,737,
3296,738,2446,2286,1345,649,1672,1816,156,1041,1201,2565,2354,2095,2395,1560,
1212,235,584,2475,2626,3029,2677,1472,6,126,2486,760,2276,2297,2841,2394,
652,912,1379,2832,671,162,2241,393,245,839,566,1260,306,402,3049,3270,
1201,3037,2675,2228,2777,3258,3219,2178,799,890,2269,985,2911,2425,1591,1275,
1039,2454,2893,2728,2214,1929,3289,1234,2760,181,2579,1539,1037,2038,1949,964,
2765,551,599,3271,1371,3269,2217,2691,968,903,681,5,463,1371,17,24,
2843,1434,1191,2114,500,2884,2656,3116,367,2666,2013,751,1408,2915,599,3250,
1397,2998,2563,2860,1069,653,1605,1123,1231,1379,1256,1936,19,2927,789,3176,
1146,2454,520,3262,2959,2964,1307,1089,1576,3078,1399,1006,1916,1181,2890,128,
]
RefValuesEncrypt512.PKC[1] = [281,1552,1170,868,2726,611,2616,444,820,1481,3185,620,1970,769,2831,2883,
662,1965,2243,2292,1162,633,2201,2746,2175,185,59,1512,3286,1882,788,2099,
2355,2366,244,889,1105,2653,391,1046,2559,2492,1667,3264,1706,1571,2448,1289,
818,3104,2796,860,2499,956,1676,2828,1394,1853,2770,963,1479,970,3256,1585,
696,959,2150,1216,637,596,2486,1386,3216,2896,2561,1716,1063,1635,3064,3308,
2681,2222,2668,2171,2880,3054,448,684,2252,1455,369,2734,2288,3086,2516,2208,
2694,2301,1208,2185,3194,1053,1613,2057,389,1133,1107,3211,2046,1735,2307,1939,
865,2494,364,2274,943,1167,619,1602,2756,2934,1966,2944,1294,2983,1931,313,
2930,2510,944,3130,964,1806,1718,1778,338,1987,2607,1076,1951,2509,167,2841,
1322,18,212,2474,2453,4,1365,2162,462,1124,482,842,2021,2940,2716,218,
1290,2168,748,2549,528,2583,1308,246,1129,1965,486,2364,2310,1914,3091,2290,
2773,2976,2151,2473,1282,2901,144,2124,1553,1308,3321,2772,1847,247,461,1921,
450,1540,3218,1784,2649,3020,1663,774,1978,3190,1843,2750,962,2866,515,1707,
2619,3058,1994,2336,2749,2389,1138,1467,3160,242,2775,1342,1662,2510,3200,557,
3093,2168,1501,3049,566,3089,387,2370,2256,1453,729,1695,3184,968,462,3011,
2694,2461,182,245,414,1716,8,1712,3077,2902,1724,120,191,1317,1327,666,
] 

RefValues512 = RefValues(MLKEM_PARAMETER.ML_KEM_512)
RefValues512.keygen = RefValuesKeygen512
RefValues512.encrypt = RefValuesEncrypt512
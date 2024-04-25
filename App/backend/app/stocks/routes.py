from flask import Flask, request, jsonify
from .functions import main
from . import stocks

@stocks.route('/stock', methods=['GET'])
async def get_data():
    gainers = [
  {
    "symbol": "CSSE",
    "name": "Chicken Soup for the Soul Entertainment, Inc.",
    "change": 0.273,
    "price": 0.4253,
    "changesPercentage": 179.2515
  },
  {
    "symbol": "FXLV",
    "name": "F45 Training Holdings Inc.",
    "change": 0.09,
    "price": 0.15,
    "changesPercentage": 150
  },
  {
    "symbol": "AIRE",
    "name": "reAlpha Tech Corp. Common Stock",
    "change": 0.559,
    "price": 1.16,
    "changesPercentage": 93.0116
  },
  {
    "symbol": "BOF",
    "name": "BranchOut Food Inc.",
    "change": 0.94,
    "price": 2.08,
    "changesPercentage": 82.4561
  },
  {
    "symbol": "LICN",
    "name": "Lichen China Limited",
    "change": 0.439,
    "price": 0.999,
    "changesPercentage": 78.3929
  },
  {
    "symbol": "AMST",
    "name": "Amesite Inc.",
    "change": 1.36,
    "price": 3.35,
    "changesPercentage": 68.3417
  },
  {
    "symbol": "MTC",
    "name": "MMTec, Inc.",
    "change": 1.36,
    "price": 3.6,
    "changesPercentage": 60.7143
  },
  {
    "symbol": "JTAIZ",
    "name": "Jet.AI Inc.",
    "change": 0.1849,
    "price": 0.5,
    "changesPercentage": 58.6798
  },
  {
    "symbol": "WIMI",
    "name": "WiMi Hologram Cloud Inc.",
    "change": 0.4246,
    "price": 1.15,
    "changesPercentage": 58.5332
  },
  {
    "symbol": "SKIL",
    "name": "Skillsoft Corp.",
    "change": 2.89,
    "price": 8.6,
    "changesPercentage": 50.613
  },
  {
    "symbol": "POET",
    "name": "POET Technologies Inc.",
    "change": 0.7,
    "price": 2.28,
    "changesPercentage": 44.3038
  },
  {
    "symbol": "MULN",
    "name": "Mullen Automotive, Inc.",
    "change": 1.04,
    "price": 3.77,
    "changesPercentage": 38.0952
  },
  {
    "symbol": "RILY",
    "name": "B. Riley Financial, Inc.",
    "change": 8.03,
    "price": 29.75,
    "changesPercentage": 36.9705
  },
  {
    "symbol": "WHLM",
    "name": "Wilhelmina International, Inc.",
    "change": 1.65,
    "price": 6.25,
    "changesPercentage": 35.8696
  },
  {
    "symbol": "JL",
    "name": "J-Long Group Limited Ordinary Shares",
    "change": 0.2513,
    "price": 0.96,
    "changesPercentage": 35.4593
  },
  {
    "symbol": "STI",
    "name": "Solidion Technology Inc.",
    "change": 0.46,
    "price": 1.98,
    "changesPercentage": 30.2632
  },
  {
    "symbol": "TROO",
    "name": "TROOPS, Inc.",
    "change": 0.32,
    "price": 1.41,
    "changesPercentage": 29.3578
  },
  {
    "symbol": "CYCC",
    "name": "Cyclacel Pharmaceuticals, Inc.",
    "change": 0.5099,
    "price": 2.2999,
    "changesPercentage": 28.486
  },
  {
    "symbol": "XWEL",
    "name": "XWELL, Inc.",
    "change": 0.38,
    "price": 1.8,
    "changesPercentage": 26.7606
  },
  {
    "symbol": "RCAT",
    "name": "Red Cat Holdings, Inc.",
    "change": 0.32,
    "price": 1.52,
    "changesPercentage": 26.6667
  },
  {
    "symbol": "RBBN",
    "name": "Ribbon Communications Inc.",
    "change": 0.68,
    "price": 3.25,
    "changesPercentage": 26.4591
  },
  {
    "symbol": "VTAK",
    "name": "Catheter Precision, Inc.",
    "change": 0.1193,
    "price": 0.575,
    "changesPercentage": 26.1795
  },
  {
    "symbol": "TSLR",
    "name": "GraniteShares 1.75x Long TSLA Daily ETF",
    "change": 1.93,
    "price": 10.04,
    "changesPercentage": 23.7978
  },
  {
    "symbol": "TSLT",
    "name": "T-REX 2X Long Tesla Daily Target ETF",
    "change": 1.75,
    "price": 9.11,
    "changesPercentage": 23.7772
  },
  {
    "symbol": "TSLL",
    "name": "Direxion Daily TSLA Bull 1.5X Shares",
    "change": 1.27,
    "price": 6.66,
    "changesPercentage": 23.5622
  },
  {
    "symbol": "CZOO",
    "name": "Cazoo Group Ltd",
    "change": 2.08,
    "price": 11.1,
    "changesPercentage": 23.0599
  },
  {
    "symbol": "AMPE",
    "name": "Ampio Pharmaceuticals, Inc.",
    "change": 0.064,
    "price": 0.35,
    "changesPercentage": 22.3776
  },
  {
    "symbol": "TRSG",
    "name": "Tungray Technologies Inc Class A Ordinary Shares",
    "change": 1.19,
    "price": 6.9,
    "changesPercentage": 20.8406
  },
  {
    "symbol": "YYAI",
    "name": "YayYo, Inc.",
    "change": 0.1521,
    "price": 0.884,
    "changesPercentage": 20.7815
  },
  {
    "symbol": "COMS",
    "name": "COMSovereign Holding Corp.",
    "change": 0.0399,
    "price": 0.24,
    "changesPercentage": 19.94
  },
  {
    "symbol": "CDTX",
    "name": "Cidara Therapeutics, Inc.",
    "change": 2.04,
    "price": 12.29,
    "changesPercentage": 19.9024
  },
  {
    "symbol": "CALC",
    "name": "CalciMedica, Inc.",
    "change": 0.91,
    "price": 5.49,
    "changesPercentage": 19.869
  },
  {
    "symbol": "ONFO",
    "name": "Onfolio Holdings, Inc.",
    "change": 0.0957,
    "price": 0.5955,
    "changesPercentage": 19.1477
  },
  {
    "symbol": "IKT",
    "name": "Inhibikase Therapeutics, Inc.",
    "change": 0.29,
    "price": 1.87,
    "changesPercentage": 18.3544
  },
  {
    "symbol": "TELO",
    "name": "Telomir Pharmaceuticals, Inc. Common Stock",
    "change": 1.07,
    "price": 6.97,
    "changesPercentage": 18.1356
  },
  {
    "symbol": "YQ",
    "name": "17 Education & Technology Group Inc.",
    "change": 0.4,
    "price": 2.75,
    "changesPercentage": 17.0213
  },
  {
    "symbol": "SOBR",
    "name": "SOBR Safe, Inc.",
    "change": 0.0437,
    "price": 0.3021,
    "changesPercentage": 16.9118
  },
  {
    "symbol": "HWH",
    "name": "HWH International Inc.",
    "change": 0.25,
    "price": 1.76,
    "changesPercentage": 16.5563
  },
  {
    "symbol": "UXIN",
    "name": "Uxin Limited",
    "change": 0.27,
    "price": 1.93,
    "changesPercentage": 16.2651
  },
  {
    "symbol": "AGEN",
    "name": "Agenus Inc.",
    "change": 0.96,
    "price": 7.42,
    "changesPercentage": 14.8607
  },
  {
    "symbol": "TSL",
    "name": "GraniteShares ETF Trust - GraniteShares 2x Long Tesla Daily ETF",
    "change": 0.8,
    "price": 6.21,
    "changesPercentage": 14.7874
  },
  {
    "symbol": "AAGR",
    "name": "African Agriculture Holdings Inc.",
    "change": 0.0499,
    "price": 0.3999,
    "changesPercentage": 14.2571
  },
  {
    "symbol": "KARO",
    "name": "Karooooo Ltd.",
    "change": 3.85,
    "price": 31.25,
    "changesPercentage": 14.0511
  },
  {
    "symbol": "CISS",
    "name": "C3is Inc.",
    "change": 0.175,
    "price": 1.43,
    "changesPercentage": 13.9442
  },
  {
    "symbol": "EVA",
    "name": "Enviva Inc.",
    "change": 0.054,
    "price": 0.4499,
    "changesPercentage": 13.6398
  },
  {
    "symbol": "APYX",
    "name": "Apyx Medical Corporation",
    "change": 0.18,
    "price": 1.5,
    "changesPercentage": 13.6364
  },
  {
    "symbol": "ENLV",
    "name": "Enlivex Therapeutics Ltd.",
    "change": 0.18,
    "price": 1.5,
    "changesPercentage": 13.6364
  },
  {
    "symbol": "CGEM",
    "name": "Cullinan Oncology, Inc.",
    "change": 2.22,
    "price": 18.89,
    "changesPercentage": 13.3173
  },
  {
    "symbol": "AIH",
    "name": "Aesthetic Medical International Holdings Group Limited",
    "change": 0.051,
    "price": 0.458,
    "changesPercentage": 12.5307
  },
  {
    "symbol": "ILAG",
    "name": "Intelligent Living Application Group Inc.",
    "change": 0.059,
    "price": 0.54,
    "changesPercentage": 12.2661
  }
]
    losers = [
  {
    "symbol": "NCI",
    "name": "Neo-Concept International Group Holdings Limited",
    "change": -7.16,
    "price": 2.34,
    "changesPercentage": -75.3684
  },
  {
    "symbol": "ISUN",
    "name": "iSun, Inc.",
    "change": -0.0576,
    "price": 0.094,
    "changesPercentage": -37.9947
  },
  {
    "symbol": "GCTK",
    "name": "GlucoTrack, Inc.",
    "change": -0.281,
    "price": 0.479,
    "changesPercentage": -36.9737
  },
  {
    "symbol": "VAXX",
    "name": "Vaxxinity, Inc.",
    "change": -0.0674,
    "price": 0.1326,
    "changesPercentage": -33.7
  },
  {
    "symbol": "EVO",
    "name": "Evotec SE",
    "change": -2.57,
    "price": 5.23,
    "changesPercentage": -32.9487
  },
  {
    "symbol": "GNTA",
    "name": "Genenta Science S.p.A.",
    "change": -1.16,
    "price": 2.55,
    "changesPercentage": -31.2668
  },
  {
    "symbol": "NIVF",
    "name": "NewGenIvf Group Limited",
    "change": -0.68,
    "price": 1.55,
    "changesPercentage": -30.4933
  },
  {
    "symbol": "IROHR",
    "name": "Iron Horse Acquisitions Corp. Right",
    "change": -0.09,
    "price": 0.21,
    "changesPercentage": -30
  },
  {
    "symbol": "ATMCR",
    "name": "AlphaTime Acquisition Corp Right",
    "change": -0.0448,
    "price": 0.1052,
    "changesPercentage": -29.8667
  },
  {
    "symbol": "ATXI",
    "name": "Avenue Therapeutics, Inc.",
    "change": -0.0397,
    "price": 0.0943,
    "changesPercentage": -29.6269
  },
  {
    "symbol": "TSLZ",
    "name": "T-Rex 2X Inverse Tesla Daily Target ETF",
    "change": -13.49,
    "price": 42.43,
    "changesPercentage": -24.1237
  },
  {
    "symbol": "TSDD",
    "name": "GraniteShares 1.5x Short TSLA Daily ETF",
    "change": -8.53,
    "price": 26.97,
    "changesPercentage": -24.0282
  },
  {
    "symbol": "SBFM",
    "name": "Sunshine Biopharma, Inc.",
    "change": -0.28,
    "price": 0.93,
    "changesPercentage": -23.1405
  },
  {
    "symbol": "GMBL",
    "name": "Esports Entertainment Group, Inc.",
    "change": -0.1489,
    "price": 0.6411,
    "changesPercentage": -18.8481
  },
  {
    "symbol": "TCJH",
    "name": "Top KingWin Ltd",
    "change": -0.23,
    "price": 1.01,
    "changesPercentage": -18.5484
  },
  {
    "symbol": "APDN",
    "name": "Applied DNA Sciences, Inc.",
    "change": -0.0512,
    "price": 0.2388,
    "changesPercentage": -17.6552
  },
  {
    "symbol": "AGBA",
    "name": "AGBA Acquisition Limited",
    "change": -0.52,
    "price": 2.45,
    "changesPercentage": -17.5084
  },
  {
    "symbol": "FNCH",
    "name": "Finch Therapeutics Group, Inc.",
    "change": -0.48,
    "price": 2.3,
    "changesPercentage": -17.2662
  },
  {
    "symbol": "ADXN",
    "name": "Addex Therapeutics Ltd",
    "change": -3.19,
    "price": 15.55,
    "changesPercentage": -17.0224
  },
  {
    "symbol": "AWIN",
    "name": "AERWINS Technologies Inc.",
    "change": -0.55,
    "price": 2.78,
    "changesPercentage": -16.5165
  },
  {
    "symbol": "CAPT",
    "name": "Captivision Inc.",
    "change": -0.95,
    "price": 4.91,
    "changesPercentage": -16.2116
  },
  {
    "symbol": "RVYL",
    "name": "Ryvyl Inc.",
    "change": -0.26,
    "price": 1.38,
    "changesPercentage": -15.8537
  },
  {
    "symbol": "MLEC",
    "name": "Moolec Science SA",
    "change": -0.27,
    "price": 1.46,
    "changesPercentage": -15.6069
  },
  {
    "symbol": "ZAPP",
    "name": "Zapp Electric Vehicles Group Limited",
    "change": -0.71,
    "price": 3.91,
    "changesPercentage": -15.368
  },
  {
    "symbol": "LNZA",
    "name": "LanzaTech Global, Inc.",
    "change": -0.395,
    "price": 2.235,
    "changesPercentage": -15.019
  },
  {
    "symbol": "NUWE",
    "name": "Nuwellis, Inc.",
    "change": -0.0443,
    "price": 0.2521,
    "changesPercentage": -14.946
  },
  {
    "symbol": "VTNR",
    "name": "Vertex Energy, Inc.",
    "change": -0.25,
    "price": 1.43,
    "changesPercentage": -14.881
  },
  {
    "symbol": "MOBQ",
    "name": "Mobiquity Technologies, Inc.",
    "change": -0.1334,
    "price": 0.7665,
    "changesPercentage": -14.8239
  },
  {
    "symbol": "LSDI",
    "name": "Lucy Scientific Discovery Inc.",
    "change": -0.152,
    "price": 0.898,
    "changesPercentage": -14.4762
  },
  {
    "symbol": "MOGU",
    "name": "MOGU Inc.",
    "change": -0.3,
    "price": 1.78,
    "changesPercentage": -14.4231
  },
  {
    "symbol": "AIU",
    "name": "Meta Data Limited",
    "change": -0.0844,
    "price": 0.5008,
    "changesPercentage": -14.4224
  },
  {
    "symbol": "JEWL",
    "name": "Adamas One Corp.",
    "change": -0.0514,
    "price": 0.3075,
    "changesPercentage": -14.3215
  },
  {
    "symbol": "RCON",
    "name": "Recon Technology, Ltd.",
    "change": -0.0143,
    "price": 0.0869,
    "changesPercentage": -14.1304
  },
  {
    "symbol": "EDU",
    "name": "New Oriental Education & Technology Group Inc.",
    "change": -12.51,
    "price": 77.08,
    "changesPercentage": -13.9636
  },
  {
    "symbol": "NUZE",
    "name": "NuZee, Inc.",
    "change": -0.18,
    "price": 1.17,
    "changesPercentage": -13.3333
  },
  {
    "symbol": "HNRA",
    "name": "HNR Acquisition Corp",
    "change": -0.3506,
    "price": 2.2879,
    "changesPercentage": -13.2879
  },
  {
    "symbol": "BNAI",
    "name": "Brand Engagement Network, Inc.",
    "change": -0.57,
    "price": 3.73,
    "changesPercentage": -13.2558
  },
  {
    "symbol": "CETX",
    "name": "Cemtrex, Inc.",
    "change": -0.33,
    "price": 2.16,
    "changesPercentage": -13.253
  },
  {
    "symbol": "SCLX",
    "name": "Scilex Holding Company",
    "change": -0.1267,
    "price": 0.85,
    "changesPercentage": -12.9723
  },
  {
    "symbol": "KIRK",
    "name": "Kirkland's, Inc.",
    "change": -0.29,
    "price": 1.98,
    "changesPercentage": -12.7753
  },
  {
    "symbol": "KPRX",
    "name": "Kiora Pharmaceuticals, Inc.",
    "change": -0.0737,
    "price": 0.5058,
    "changesPercentage": -12.7179
  },
  {
    "symbol": "NXL",
    "name": "Nexalin Technology, Inc.",
    "change": -0.205,
    "price": 1.42,
    "changesPercentage": -12.6154
  },
  {
    "symbol": "JYD",
    "name": "Jayud Global Logistics Limited",
    "change": -0.13,
    "price": 0.91,
    "changesPercentage": -12.5
  },
  {
    "symbol": "VLCN",
    "name": "Volcon, Inc.",
    "change": -0.0367,
    "price": 0.2579,
    "changesPercentage": -12.4576
  },
  {
    "symbol": "SMXT",
    "name": "Solarmax Technology Inc. Common Stock",
    "change": -1.13,
    "price": 8.02,
    "changesPercentage": -12.3497
  },
  {
    "symbol": "NAAS",
    "name": "NaaS Technology Inc.",
    "change": -0.1202,
    "price": 0.8602,
    "changesPercentage": -12.2603
  },
  {
    "symbol": "IBRX",
    "name": "ImmunityBio, Inc.",
    "change": -0.67,
    "price": 4.82,
    "changesPercentage": -12.204
  },
  {
    "symbol": "TSLS",
    "name": "Direxion Daily TSLA Bear 1X Shares",
    "change": -3.68,
    "price": 26.91,
    "changesPercentage": -12.0301
  },
  {
    "symbol": "BJDX",
    "name": "Bluejay Diagnostics, Inc.",
    "change": -0.0751,
    "price": 0.5499,
    "changesPercentage": -12.016
  },
  {
    "symbol": "TSLQ",
    "name": "AXS TSLA Bear Daily ETF",
    "change": -5.53,
    "price": 40.53,
    "changesPercentage": -12.0061
  }
]
    actives =  [
  {
    "symbol": "CSSE",
    "name": "Chicken Soup for the Soul Entertainment, Inc.",
    "change": 0.273,
    "price": 0.4253,
    "changesPercentage": 179.2515
  },
  {
    "symbol": "TSLA",
    "name": "Tesla, Inc.",
    "change": 17.45,
    "price": 162.13,
    "changesPercentage": 12.0611
  },
  {
    "symbol": "SQQQ",
    "name": "ProShares UltraPro Short QQQ",
    "change": -0.1,
    "price": 11.81,
    "changesPercentage": -0.8396
  },
  {
    "symbol": "BOF",
    "name": "BranchOut Food Inc.",
    "change": 0.94,
    "price": 2.08,
    "changesPercentage": 82.4561
  },
  {
    "symbol": "NKLA",
    "name": "Nikola Corporation",
    "change": -0.0153,
    "price": 0.62,
    "changesPercentage": -2.4083
  },
  {
    "symbol": "SOXL",
    "name": "Direxion Daily Semiconductor Bull 3X Shares",
    "change": 1.38,
    "price": 35.49,
    "changesPercentage": 4.0457
  },
  {
    "symbol": "T",
    "name": "AT&T Inc.",
    "change": 0.31,
    "price": 16.81,
    "changesPercentage": 1.8788
  },
  {
    "symbol": "TQQQ",
    "name": "ProShares UltraPro QQQ",
    "change": 0.52,
    "price": 53.71,
    "changesPercentage": 0.9776
  },
  {
    "symbol": "AMST",
    "name": "Amesite Inc.",
    "change": 1.36,
    "price": 3.35,
    "changesPercentage": 68.3417
  },
  {
    "symbol": "F",
    "name": "Ford Motor Company",
    "change": 0.01,
    "price": 12.95,
    "changesPercentage": 0.0773
  },
  {
    "symbol": "SPY",
    "name": "SPDR S&P 500 ETF Trust",
    "change": -0.24,
    "price": 505.41,
    "changesPercentage": -0.0475
  },
  {
    "symbol": "FFIE",
    "name": "Faraday Future Intelligent Electric Inc.",
    "change": -0.0041,
    "price": 0.0499,
    "changesPercentage": -7.5926
  },
  {
    "symbol": "INTC",
    "name": "Intel Corporation",
    "change": 0.22,
    "price": 34.5,
    "changesPercentage": 0.6418
  },
  {
    "symbol": "CYN",
    "name": "Cyngn Inc.",
    "change": -0.0074,
    "price": 0.1066,
    "changesPercentage": -6.4912
  },
  {
    "symbol": "NVDA",
    "name": "NVIDIA Corporation",
    "change": -27.46,
    "price": 796.77,
    "changesPercentage": -3.3316
  },
  {
    "symbol": "RIOT",
    "name": "Riot Blockchain, Inc.",
    "change": 0.03,
    "price": 11.88,
    "changesPercentage": 0.2532
  },
  {
    "symbol": "TLT",
    "name": "iShares 20+ Year Treasury Bond ETF",
    "change": -0.63,
    "price": 88.4,
    "changesPercentage": -0.7076
  },
  {
    "symbol": "TSLL",
    "name": "Direxion Daily TSLA Bull 1.5X Shares",
    "change": 1.27,
    "price": 6.66,
    "changesPercentage": 23.5622
  },
  {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "change": 2.12,
    "price": 169.02,
    "changesPercentage": 1.2702
  },
  {
    "symbol": "QQQ",
    "name": "Invesco QQQ Trust",
    "change": 1.44,
    "price": 426.51,
    "changesPercentage": 0.3388
  },
  {
    "symbol": "SINT",
    "name": "Sintx Technologies, Inc.",
    "change": 0.0029,
    "price": 0.0387,
    "changesPercentage": 8.1006
  },
  {
    "symbol": "MARA",
    "name": "Marathon Digital Holdings, Inc.",
    "change": -0.35,
    "price": 19.09,
    "changesPercentage": -1.8004
  },
  {
    "symbol": "FXI",
    "name": "iShares China Large-Cap ETF",
    "change": 0.47,
    "price": 25.27,
    "changesPercentage": 1.8952
  },
  {
    "symbol": "SPTS",
    "name": "SPDR Portfolio Short Term Treasury ETF",
    "change": -0.02,
    "price": 28.74,
    "changesPercentage": -0.0695
  },
  {
    "symbol": "DNA",
    "name": "Ginkgo Bioworks Holdings, Inc.",
    "change": -0.0247,
    "price": 0.8458,
    "changesPercentage": -2.8374
  },
  {
    "symbol": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "change": -0.53,
    "price": 151.74,
    "changesPercentage": -0.3481
  },
  {
    "symbol": "SOUN",
    "name": "SoundHound AI, Inc.",
    "change": -0.16,
    "price": 4.01,
    "changesPercentage": -3.8369
  },
  {
    "symbol": "TPET",
    "name": "Trio Petroleum Corp.",
    "change": 0.0414,
    "price": 0.4015,
    "changesPercentage": 11.4968
  },
  {
    "symbol": "PEGY",
    "name": "Pineapple Energy Inc.",
    "change": -0.0053,
    "price": 0.0513,
    "changesPercentage": -9.364
  },
  {
    "symbol": "AAL",
    "name": "American Airlines Group Inc.",
    "change": -0.31,
    "price": 13.92,
    "changesPercentage": -2.1785
  },
  {
    "symbol": "SOFI",
    "name": "SoFi Technologies, Inc.",
    "change": 0.02,
    "price": 7.6,
    "changesPercentage": 0.2639
  },
  {
    "symbol": "TELL",
    "name": "Tellurian Inc.",
    "change": 0.0306,
    "price": 0.44,
    "changesPercentage": 7.4744
  },
  {
    "symbol": "FCEL",
    "name": "FuelCell Energy, Inc.",
    "change": -0.0557,
    "price": 0.863,
    "changesPercentage": -6.0629
  },
  {
    "symbol": "PLUG",
    "name": "Plug Power Inc.",
    "change": -0.18,
    "price": 2.41,
    "changesPercentage": -6.9498
  },
  {
    "symbol": "HYG",
    "name": "iShares iBoxx $ High Yield Corporate Bond ETF",
    "change": -0.17,
    "price": 76.54,
    "changesPercentage": -0.2216
  },
  {
    "symbol": "VALE",
    "name": "Vale S.A.",
    "change": 0.16,
    "price": 12.37,
    "changesPercentage": 1.3104
  },
  {
    "symbol": "CLSK",
    "name": "CleanSpark, Inc.",
    "change": -0.95,
    "price": 19.78,
    "changesPercentage": -4.5827
  },
  {
    "symbol": "RIVN",
    "name": "Rivian Automotive, Inc.",
    "change": -0.2,
    "price": 8.84,
    "changesPercentage": -2.2124
  },
  {
    "symbol": "PLTR",
    "name": "Palantir Technologies Inc.",
    "change": -0.05,
    "price": 21.59,
    "changesPercentage": -0.231
  },
  {
    "symbol": "JAGX",
    "name": "Jaguar Health, Inc.",
    "change": 0.0019,
    "price": 0.1699,
    "changesPercentage": 1.131
  },
  {
    "symbol": "XLF",
    "name": "Financial Select Sector SPDR Fund",
    "change": -0.01,
    "price": 41.12,
    "changesPercentage": -0.0243
  },
  {
    "symbol": "NIO",
    "name": "NIO Inc.",
    "change": 0.14,
    "price": 4.15,
    "changesPercentage": 3.4913
  },
  {
    "symbol": "AMZN",
    "name": "Amazon.com, Inc.",
    "change": -2.95,
    "price": 176.59,
    "changesPercentage": -1.6431
  },
  {
    "symbol": "IBIT",
    "name": "iShares Bitcoin Trust",
    "change": -1.49,
    "price": 36.41,
    "changesPercentage": -3.9314
  },
  {
    "symbol": "AIRE",
    "name": "reAlpha Tech Corp. Common Stock",
    "change": 0.559,
    "price": 1.16,
    "changesPercentage": 93.0116
  },
  {
    "symbol": "SPXS",
    "name": "Direxion Daily S&P 500 Bear 3X Shares",
    "change": 0,
    "price": 9.75,
    "changesPercentage": 0
  },
  {
    "symbol": "HSCS",
    "name": "Heart Test Laboratories, Inc.",
    "change": 0.009,
    "price": 0.1079,
    "changesPercentage": 9.1001
  },
  {
    "symbol": "VRT",
    "name": "Vertiv Holdings Co",
    "change": 5.4,
    "price": 84.57,
    "changesPercentage": 6.8208
  },
  {
    "symbol": "SNAP",
    "name": "Snap Inc.",
    "change": -0.31,
    "price": 11.08,
    "changesPercentage": -2.7217
  },
  {
    "symbol": "META",
    "name": "Meta Platforms, Inc.",
    "change": -2.6,
    "price": 493.5,
    "changesPercentage": -0.5241
  }
]
    return jsonify({
        'gainers': gainers,
        'losers': losers,
        'actives': actives
    })

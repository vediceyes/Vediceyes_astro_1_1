FLG_TOPOCTR = 32768
FLG_SPEED = 256
FLG_SWIEPH =2
FLG_SIDEREAL = 65536
GREG_CAL= 1
JULIAN_CAL=0


Zodiac_sign= {0:"Ari",1:"Tau", 2:"Gem", 3:"Can", 4:"Leo", 5:"Vir", 6:"Lib", 7:"Sco", 8:"Sag", 9:"Cap", 10:"Aqu", 11:"Pis"}
Planet_List = {0:"SU", 1:"MO", 2:"ME", 3:"VE", 4:"MA", 5:"JU", 6:"SA",7:"URAN", 8:"NEPT", 9:"PLUT", 10:"RA"}
House_list= [1,2,3,4,5,6,7,8,9,10,11,12]
#Planet_List_loop = [0,1,2,3,4,5,6,7,8,9,11]
Planet_List_loop = [0,1,2,3,4,5,6,10]
Planet_Loop = ["SU", "MO","ME","VE","MA","JU","SA","RA"]
Planet_Loop_ws = {"SU":"2","MO":"3","ME":"4","VE":"5","MA":"6","JU":"7","SA":"8","RA":"9"}

Planet_Element = {"SU":"Fire ",
                  "MO":"Water",
                  "ME":"Earth",
                  "VE":"Water",
                  "MA":"Fire ",
                  "JU":"Ether",
                  "SA":"Air  ",
                  "URAN":"Fire ",
                  "NEPT":"?    ",
                  "PLUT":"?    ",
                  "RA":"Air  ",
                  "KE":"Fire "}

Lagna_Element = {"Ari":"Fire ",
                 "Tau":"Earth",
                 "Gem":"Air  ",
                 "Can":"Water",
                 "Leo":"Fire ",
                 "Vir":"Earth",
                 "Lib":"Air  ",
                 "Sco":"Water",
                 "Sag":"Fire ",
                 "Cap":"Earth",
                 "Aqu":"Air  ",
                 "Pis":"Water"}

Exalt_List = {"SU":"Ari",
              "MO":"Tau",
              "ME":"Vir",
              "VE":"Pis",
              "MA":"Cap",
              "JU":"Can",
              "SA":"Lib",
              "URAN":"?  ",
              "NEPT":"?  ",
              "PLUT":"?  ",
              "RA":"Tau",
              "KE":"Sco"}

Fall_List = {"SU":"Lib",
             "MO":"Sco",
             "ME":"Pis",
             "VE":"Vir",
             "MA":"Can",
             "JU":"Cap",
             "SA":"Ari",
             "URAN":"?  ",
             "NEPT":"?  ",
             "PLUT":"?  ",
             "RA":"Sco",
             "KE":"Tau"}

Trikona_List = {"SU":"Leo",
                "MO":"Tau",
                "ME":"Vir",
                "VE":"Lib",
                "MA":"Ari",
                "JU":"Sag",
                "SA":"Aqu",
                "URAN":"?  ",
                "NEPT":"?  ",
                "PLUT":"?  ",
                "RA":"N/A",
                "KE":"N/A"}

Malefics_List = ["SU", "MA", "SA", "RA", "KE"]

Benefics_List = ["MO", "VE", "ME", "JU"]


Ruler_List    = {"Ari":"MA",
                 "Tau":"VE",
                 "Gem":"ME",
                 "Can":"MO",
                 "Leo":"SU",
                 "Vir":"ME",
                 "Lib":"VE",
                 "Sco":"MA",
                 "Sag":"JU",
                 "Cap":"SA",
                 "Aqu":"SA",
                 "Pis":"JU"}

# Moon Rules Cancer here,,, but Trikona Taurus.. Whyyy?

Planet_sex     = {"SU":"Male",
                  "MO":"Female",
                  "ME":"Neutral",
                  "VE":"Female",
                  "MA":"Male",
                  "JU":"Male",
                  "SA":"Neutral",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RA":"N/A",
                  "KE":"N/A"}

Planet_caste   = {"SU":"Ksatriya",
                  "MO":"Vaisya",
                  "ME":"Vaisya",
                  "VE":"Brahmana",
                  "MA":"Ksatriya",
                  "JU":"Brahmana",
                  "SA":"Sudras",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RA":"Ksatriya",
                  "KE":"Ksatriya"}

Planet_modes   = {"SU":"Satvic",
                  "MO":"Satvic",
                  "ME":"Rajasic",
                  "VE":"Rajasic",
                  "MA":"Tamasic",
                  "JU":"Satvic",
                  "SA":"Tamasic",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RA":"N/A",
                  "KE":"N/A"}

Planet_governance= {  "SU":"Soul of All",
                      "MO":"Mind",
                      "ME":"Speech",
                      "VE":"Semen",
                      "MA":"One's Strength",
                      "JU":"Knowledge and General Happiness",
                      "SA":"Grief",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RA":"N/A",
                      "KE":"N/A"}

Planet_color = {      "SU":"Blood red",
                      "MO":"Tawney",
                      "ME":"Green",
                      "VE":"Varigated",
                      "MA":"Blood red",
                      "JU":"Tawny",
                      "SA":"Dark",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RA":"N/A",
                      "KE":"N/A"}


Planet_ingredients = {"SU":"Bones",
                      "MO":"Blood",
                      "ME":"Skin",
                      "VE":"Semen",
                      "MA":"Marrow",
                      "JU":"Fat",
                      "SA":"Muscles",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RA":"N/A",
                      "KE":"N/A"}

Planet_direction = {      "SU":"South",
                          "MO":"North-West",
                          "ME":"North-East",
                          "VE":"South-East",
                          "MA":"South",
                          "JU":"North-East",
                          "SA":"West",
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RA":"South-west",
                          "KE":"N/A"}

Planet_houses = {         "SU":"10",
                          "MO":"4",
                          "ME":"1",
                          "VE":"4",
                          "MA":"10",
                          "JU":"1",
                          "SA":"7",
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RA":"?",
                          "KE":"N/A"}


Planet_friends = {        "SU":["MO", "MA", "JU"],
                          "MO":["SU", "ME"],
                          "ME":["SU", "VE"],
                          "VE":["ME", "SA"],
                          "MA":["SU", "MO", "JU"],
                          "JU":["SU", "MO", "MA"],
                          "SA":["ME", "VE"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RA":["JU", "VE", "SA"],
                          "KE":["MA", "VE", "SA"]}

Planet_enemies = {        "SU":["VE", "SA"],
                          "MO":"N/A",
                          "ME":["MO"],
                          "VE":["MO", "SU"],
                          "MA":["ME"],
                          "JU":["ME", "VE"],
                          "SA":["SU", "MO", "MA"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RA":["SU", "MO", "MA"],
                          "KE":["SU", "MO"]}

Planet_equals = {         "SU":["Mercury"],
                          "MO":["MA", "JU", "VE", "SA"],
                          "ME":["MA", "JU", "SA"],
                          "VE":["MA", "JU"],
                          "MA":["VE", "SA"],
                          "JU":["SA"],
                          "SA":["JU"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RA":["ME"],
                          "KE":["ME", "JU"]}

Temp_friends = { "1":["2", "3", "4", "10", "11", "12"],
                 "2":["3", "4", "5", "11", "12", "1"],
                 "3":["4", "5", "6", "12", "1",  "2"],
                 "4":["5", "6", "7", "1"  ,"2",  "3"],
                 "5":["6", "7", "8", "2", "3", "4"],
                 "6":["7", "8", "9", "3", "4",  "5"],
                 "7":["8", "9", "10", "4"  ,"5",  "6"],
                 "8":["9",  "10", "11", "5", "6", "7"],
                 "9":["10", "11", "12", "6", "7",  "8"],
                "10":["11", "12", "1", "7"  ,"8",  "9"],
                "11":["12", "1", "2", "8", "9", "10"],
                "12":["1",  "2", "3", "9", "10", "11"]}

Temp_enemies = {"1": ["1", "5", "6", "7", "8", "9"],
                "2": ["2", "6", "7", "8", "9", "10"],
                "3": ["3", "7", "8", "9", "10", "11"],
                "4": ["4", "8", "9", "10", "11", "12"],
                "5": ["5", "9", "10", "11", "12", "1"],
                "6": ["6", "10", "11", "12", "1", "2"],
                "7": ["7", "11", "12", "1", "2", "3"],
                "8": ["8", "12", "1", "2", "3", "4"],
                "9": ["9", "1",  "2", "3", "4", "5"],
                "10": ["10", "2", "3", "4", "5", "6"],
                "11": ["11", "3", "4", "5", "6", "7"],
                "12": ["12", "4", "5", "6", "7", "8"]}


signs_List_ws = {"Ari":"B16",
                 "Tau":"C16",
                 "Gem":"D16",
                 "Can":"E16",
                 "Leo":"F16",
                 "Vir":"G16",
                 "Lib":"H16",
                 "Sco":"I16",
                 "Sag":"J16",
                 "Cap":"K16",
                 "Aqu":"L16",
                 "Pis":"M16"}

House_List_ws= {"1": "B26",
                "2": "C26",
                "3": "D26",
                "4": "E26",
                "5": "F26",
                "6": "G26",
                "7": "H26",
                "8": "I26",
                "9": "J26",
                "10":"K26",
                "11":"L26",
                "12":"M26"}

Dignity_List= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N"]

SH_List= ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]











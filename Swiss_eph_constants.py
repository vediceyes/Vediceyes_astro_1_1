FLG_TOPOCTR = 32768
FLG_SPEED = 256
FLG_SWIEPH =2
FLG_SIDEREAL = 65536
GREG_CAL= 1
JULIAN_CAL=0


Zodiac_sign= {0:"Ari",1:"Tau", 2:"Gem", 3:"Can", 4:"Leo", 5:"Vir", 6:"Lib", 7:"Sco", 8:"Sag", 9:"Cap", 10:"Aqu", 11:"Pis"}
Planet_List = {0:"SUN$", 1:"MOON", 2:"MERC", 3:"VENU", 4:"MARS", 5:"JUPI", 6:"SATU",7:"URAN", 8:"NEPT", 9:"PLUT", 11:"RAHU"}
House_list= [1,2,3,4,5,6,7,8,9,10,11,12]
Planet_List_loop = [0,1,2,3,4,5,6,7,8,9,11]
Planet_Element = {"SUN$":"Fire ",
                  "MOON":"Water",
                  "MERC":"Earth",
                  "VENU":"Water",
                  "MARS":"Fire ",
                  "JUPI":"Ether",
                  "SATU":"Air  ",
                  "URAN":"Fire ",
                  "NEPT":"?    ",
                  "PLUT":"?    ",
                  "RAHU":"Air  ",
                  "KETU":"Fire "}

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

Exalt_List = {"SUN$":"Ari",
              "MOON":"Tau",
              "MERC":"Vir",
              "VENU":"Pis",
              "MARS":"Cap",
              "JUPI":"Can",
              "SATU":"Lib",
              "URAN":"?  ",
              "NEPT":"?  ",
              "PLUT":"?  ",
              "RAHU":"Tau",
              "KETU":"Sco"}

Fall_List = {"SUN$":"Lib",
             "MOON":"Sco",
             "MERC":"Pis",
             "VENU":"Vir",
             "MARS":"Can",
             "JUPI":"Cap",
             "SATU":"Ari",
             "URAN":"?  ",
             "NEPT":"?  ",
             "PLUT":"?  ",
             "RAHU":"Sco",
             "KETU":"Tau"}

Trikona_List = {"SUN$":"Leo",
                "MOON":"Tau",
                "MERC":"Vir",
                "VENU":"Lib",
                "MARS":"Ari",
                "JUPI":"Sag",
                "SATU":"Aqu",
                "URAN":"?  ",
                "NEPT":"?  ",
                "PLUT":"?  ",
                "RAHU":"N/A",
                "KETU":"N/A"}

Malefics_List = ["SUN$", "MARS", "SATU", "RAHU", "KETU"]

Benefics_List = ["MOON", "VENU", "MERC", "JUPI"]


Ruler_List    = {"Ari":"MARS",
                 "Tau":"VENU",
                 "Gem":"MERC",
                 "Can":"MOON",
                 "Leo":"SUN$",
                 "Vir":"MERC",
                 "Lib":"VENU ",
                 "Sco":"MARS",
                 "Sag":"JUPI",
                 "Cap":"SATU",
                 "Aqu":"SATU",
                 "Pis":"JUPI"}

# Moon Rules Cancer here,,, but Trikona Taurus.. Whyyy?

Planet_sex     = {"SUN$":"Male",
                  "MOON":"Female",
                  "MERC":"Neutral",
                  "VENU":"Female",
                  "MARS":"Male",
                  "JUPI":"Male",
                  "SATU":"Neutral",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RAHU":"N/A",
                  "KETU":"N/A"}

Planet_caste   = {"SUN$":"Ksatriya",
                  "MOON":"Vaisya",
                  "MERC":"Vaisya",
                  "VENU":"Brahmana",
                  "MARS":"Ksatriya",
                  "JUPI":"Brahmana",
                  "SATU":"Sudras",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RAHU":"Ksatriya",
                  "KETU":"Ksatriya"}

Planet_modes   = {"SUN$":"Satvic",
                  "MOON":"Satvic",
                  "MERC":"Rajasic",
                  "VENU":"Rajasic",
                  "MARS":"Tamasic",
                  "JUPI":"Satvic",
                  "SATU":"Tamasic",
                  "URAN":"?",
                  "NEPT":"?",
                  "PLUT":"?",
                  "RAHU":"N/A",
                  "KETU":"N/A"}

Planet_governance= {  "SUN$":"Soul of All",
                      "MOON":"Mind",
                      "MERC":"Speech",
                      "VENU":"Semen",
                      "MARS":"One's Strength",
                      "JUPI":"Knowledge and General Happiness",
                      "SATU":"Grief",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RAHU":"N/A",
                      "KETU":"N/A"}

Planet_color = {      "SUN$":"Blood red",
                      "MOON":"Tawney",
                      "MERC":"Green",
                      "VENU":"Varigated",
                      "MARS":"Blood red",
                      "JUPI":"Tawny",
                      "SATU":"Dark",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RAHU":"N/A",
                      "KETU":"N/A"}


Planet_ingredients = {"SUN$":"Bones",
                      "MOON":"Blood",
                      "MERC":"Skin",
                      "VENU":"Semen",
                      "MARS":"Marrow",
                      "JUPI":"Fat",
                      "SATU":"Muscles",
                      "URAN":"?",
                      "NEPT":"?",
                      "PLUT":"?",
                      "RAHU":"N/A",
                      "KETU":"N/A"}

Planet_direction = {      "SUN$":"South",
                          "MOON":"North-West",
                          "MERC":"North-East",
                          "VENU":"South-East",
                          "MARS":"South",
                          "JUPI":"North-East",
                          "SATU":"West",
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RAHU":"South-west",
                          "KETU":"N/A"}

Planet_houses = {         "SUN$":"10",
                          "MOON":"4",
                          "MERC":"1",
                          "VENU":"4",
                          "MARS":"10",
                          "JUPI":"1",
                          "SATU":"7",
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RAHU":"?",
                          "KETU":"N/A"}


Planet_friends = {        "SUN$":["MOON", "MARS", "JUPI"],
                          "MOON":["SUN$", "MERC"],
                          "MERC":["SUN$", "VENU"],
                          "VENU":["MERC", "SATU"],
                          "MARS":["SUN$", "MOON", "JUPI"],
                          "JUPI":["SUN$", "MOON", "MARS"],
                          "SATU":["MERC", "VENU"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RAHU":["JUPI", "VENU", "SATU"],
                          "KETU":["MARS", "VENU", "SATU"]}

Planet_enemies = {        "SUN$":["VENU", "SATU"],
                          "MOON":"N/A",
                          "MERC":["MOON"],
                          "VENU":["MOON", "SUN$"],
                          "MARS":["MERC"],
                          "JUPI":["MERC", "VENU"],
                          "SATU":["SUN$", "MOON", "MARS"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RAHU":["SUN$", "MOON", "MARS"],
                          "KETU":["SUN$", "MOON"]}

Planet_equals = {         "SUN$":["Mercury"],
                          "MOON":["MARS", "JUPI", "VENU", "SATU"],
                          "MERC":["MARS", "JUPI", "SATU"],
                          "VENU":["MARS", "JUPI"],
                          "MARS":["VENU", "SATU"],
                          "JUPI":["SATU"],
                          "SATU":["JUPI"],
                          "URAN":"?",
                          "NEPT":"?",
                          "PLUT":"?",
                          "RAHU":["MERC"],
                          "KETU":["MERC", "JUPI"]}


Temp_Friends =  ["4","10","3","11","2","12"]

Temp_Enemies = ["1","5","6","7","8","9"]





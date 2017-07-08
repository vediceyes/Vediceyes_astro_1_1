import swisseph as swe
import collections
from Swiss_eph_constants import *


swe.set_ephe_path('/usr/share/ephe') # set path to ephemeris files



class Chart(object):


    def __init__(self):
        self.data = []

    def Setup_eph(self, lat,long,side=1):

        swe.set_topo(lat,long)
        swe.set_sid_mode(side)


    def decdeg2dms(self, dd):
       is_positive = dd >= 0
       dd = abs(dd)
       minutes,seconds = divmod(dd*3600,60)
       degrees,minutes = divmod(minutes,60)
       degrees = degrees if is_positive else -degrees
       return (degrees,minutes,seconds)

    def prnt(self, var):

        return(str(var[0])+'º '+str(var[1])+"' "+str(round(var[2],2))+ '"')

    def getHouse(self, PlanetLocDict,HouseDict, planet):

        HousePosList = sorted(HouseDict.keys())

        firstkey= HousePosList[0]

        HousePosList.insert(0,firstkey)

        HousePosList.insert(13, 360)

        #print("New List", HousePosList)

        for a in range(1,14):

             if PlanetLocDict[planet]<=HousePosList[a]:
                 #print(HousePosList[a])
                 return HousePosList[a-1]
                 break

    def getASC(self, HouseDict):

        HousePosList = list(HouseDict.keys())

        print("")

        print("ASCENDANT LAGNA: ", Zodiac_sign[int(HousePosList[0]/30)], "("+Lagna_Element[Zodiac_sign[int(HousePosList[0]/30)]]+")")

        print("")

        return Zodiac_sign[int(HousePosList[0]/30)]


    def Header(self):
        print("")

        print("*******SUDHARSHANA VEDIC ASTROLOGY SOFTWARE*******")

        print("")


    def CaclHouses(self):
        house_loc = swe.houses_ex(self.Bday_accurate[1], lat, lon, str.encode('P'), FLG_SIDEREAL)

        Cusps = house_loc[0]

        Asc = house_loc[1]

        HouseDict = collections.OrderedDict()

        for j in House_list:
            HouseDict[Cusps[j - 1]] = str(j)

            # print("House "+str(j) + " in "+Zodiac_sign[int(Cusps[j-1]/30)], prnt(decdeg2dms((Cusps[j-1] % 30))))

        HousePosList = sorted(HouseDict.keys())

        return HouseDict,HousePosList

    def CalcPlanets(self,HouseDict):
        # print("HouseposList", HousePosList)

        print("")

        print("PLANET POSITIONS FOR NATAL CHART")

        print("")

        PlanetLocDict = collections.OrderedDict()
        PlanetZodiacDict = collections.OrderedDict()

        for i in Planet_List_loop:
            planet_pos = swe.calc_ut(self.Bday_accurate[1], i, FLG_SIDEREAL + FLG_SWIEPH)

            PlanetLocDict[Planet_List[i]] = planet_pos[0]
            PlanetZodiacDict[Planet_List[i]] = Zodiac_sign[int(planet_pos[0] / 30)]

            # print("Planet Dict", PlanetLocDict)

            print(Planet_List[i],"("+Planet_Element[Planet_List[i]]+")", " in House", HouseDict[self.getHouse(PlanetLocDict, HouseDict, Planet_List[i])], " in Lagna ", Zodiac_sign[int(planet_pos[0]/ 30)], "("+ Lagna_Element[Zodiac_sign[int(planet_pos[0]/ 30)]]+")")

    def GetAyanamsa(self):

        ayan = swe.get_ayanamsa_ut(self.Bday_accurate[1])

        print("Ayanamsa = ", self.prnt(self.decdeg2dms(ayan)))


    def ReadingSetup(self,Name,POB,Chart_type):
        print("Name: " + Name)
        print("Place of Birth = " + POB)
        print("Chart Type = " + Chart_type)

    def DateTime(self,year,month,date,hr,min,sec):

        return swe.utc_to_jd(year,month,date,hr,min,sec,GREG_CAL)



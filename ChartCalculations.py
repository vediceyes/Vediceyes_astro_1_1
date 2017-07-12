import swisseph as swe
import collections
from Swiss_eph_constants import *


swe.set_ephe_path('/usr/share/ephe') #set path to ephemeris files



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


    def CaclHouses(self, Bday_accurate, lon, lat):

        print(lat)
        print(lon)
        house_loc = swe.houses_ex(Bday_accurate[1], lat, lon, str.encode('P'), FLG_SIDEREAL)

        Cusps = house_loc[0]

        Asc = house_loc[1]

        HouseDict = collections.OrderedDict()

        for j in House_list:
            HouseDict[Cusps[j - 1]] = str(j)

            print("House "+str(j) + " in "+Zodiac_sign[int(Cusps[j-1]/30)], self.prnt(self.decdeg2dms((Cusps[j-1] % 30))))

        HousePosList = sorted(HouseDict.keys())

        print(HousePosList)
        print(HouseDict)


        return HouseDict,HousePosList

    def CalcPlanets(self,HouseDict,Bday_accurate,ws):
        # print("HouseposList", HousePosList)

        print("")

        print("PLANET POSITIONS FOR NATAL CHART")

        print("")

        PlanetLocDict = collections.OrderedDict()
        PlanetZodiacDict = collections.OrderedDict()

        Block1_count=2
        Block2_count=17
        Block3_count=33

        for i in Planet_List_loop:
            planet_pos = swe.calc_ut(Bday_accurate[1], i, FLG_SIDEREAL + FLG_SWIEPH)

            PlanetLocDict[Planet_List[i]] = planet_pos[0]
            PlanetZodiacDict[Planet_List[i]] = Zodiac_sign[int(planet_pos[0] / 30)]

            #print("Planet Dict", PlanetLocDict)

            ws['A'+str(Block1_count)] = Planet_List[i]# Planet Name
            ws['B' + str(Block1_count)] = Zodiac_sign[int(planet_pos[0]/ 30)] # Lagna
            ws['C' + str(Block1_count)] = Ruler_List[Zodiac_sign[int(planet_pos[0]/ 30)]]# Lagna Lord

            ws['M' + str(Block1_count)] =HouseDict[self.getHouse(PlanetLocDict, HouseDict, Planet_List[i])] # House number

            if Exalt_List[Planet_List[i]]==Zodiac_sign[int(planet_pos[0]/ 30)]:
                ws['D' + str(Block1_count)] = 'Yes'

            if Fall_List[Planet_List[i]]==Zodiac_sign[int(planet_pos[0]/ 30)]:
                ws['E' + str(Block1_count)] = 'Yes'

            if Trikona_List[Planet_List[i]]==Zodiac_sign[int(planet_pos[0]/ 30)]:
                ws['F' + str(Block1_count)] = 'Yes'

            for f in Planet_friends[Planet_List[i]]:

                if f==Ruler_List[Zodiac_sign[int(planet_pos[0]/ 30)]]:
                    ws['G' + str(Block1_count)] = 'Yes'
            for e in Planet_enemies[Planet_List[i]]:

                if e==Ruler_List[Zodiac_sign[int(planet_pos[0]/ 30)]]:
                    ws['H' + str(Block1_count)] = 'Yes'
            for n in Planet_equals[Planet_List[i]]:

                if n==Ruler_List[Zodiac_sign[int(planet_pos[0]/ 30)]]:
                    ws['I' + str(Block1_count)] = 'Yes'

        # Calculating Lagna Lord's House Positions

            print(Planet_List[i], "(" + Planet_Element[Planet_List[i]] + ")", " in House",
                  HouseDict[self.getHouse(PlanetLocDict, HouseDict, Planet_List[i])], " in Lagna ",
                  Zodiac_sign[int(planet_pos[0] / 30)], "(" + Lagna_Element[Zodiac_sign[int(planet_pos[0] / 30)]] + ")")

            Block1_count = Block1_count + 1
            Block2_count = Block2_count + 1
            Block3_count = Block3_count + 1



        Block1_count = 2
        for temp in Planet_Loop:

            print(ws["C"+str(Block1_count)].value)

            Lnumber = Planet_Loop_ws[ws["C"+str(Block1_count)].value]

            print(Lnumber)

            ws["N"+str(Block1_count)]= ws["M"+ Lnumber].value

            Block1_count= Block1_count+1

        Block1_count = 2
        # Calculating Temp Friends or Eneimies
        for tf in Planet_Loop:

            for tempf in Temp_friends[ws['M'+str(Block1_count)].value]:

                print(tempf)
                print(ws['N'+str(Block1_count)].value)
                if tempf==ws['N'+str(Block1_count)].value:

                    print("Did it")

                    ws['J' + str(Block1_count)] = 'Yes'

            Block1_count = Block1_count + 1

        Block1_count = 2

        for te in Planet_Loop:

            for tempe in Temp_enemies[ws['M' + str(Block1_count)].value]:

                if tempe == ws['N' + str(Block1_count)].value:
                    ws['K' + str(Block1_count)] = 'Yes'

            Block1_count = Block1_count + 1

        # Dignity calculation

        Block1_count = 2

        for te in Planet_Loop:

            if ws['J'+str(Block1_count)].value=='Yes':
                if ws['G' + str(Block1_count)].value == 'Yes':
                    ws['L' + str(Block1_count)]="Good Friend"

            if ws['J'+str(Block1_count)].value=='Yes':
                if ws['I' + str(Block1_count)].value == 'Yes':
                    ws['L' + str(Block1_count)]="Friend"

            if ws['J'+str(Block1_count)].value=='Yes':
                if ws['H'+str(Block1_count)].value=='Yes':
                    ws['L' + str(Block1_count)]="Neutral"

            if ws['K'+str(Block1_count)].value=='Yes':
                if ws['G'+str(Block1_count)].value=='Yes':
                    ws['L' + str(Block1_count)]="Neutral"

            if ws['K'+str(Block1_count)].value=='Yes':
                if ws['I' + str(Block1_count)].value == 'Yes':
                    ws['L' + str(Block1_count)]="Enemy"

            if ws['K'+str(Block1_count)].value=='Yes':

                if ws['H'+str(Block1_count)].value=='Yes':
                    ws['L' + str(Block1_count)]="Great Enemy"


            Block1_count = Block1_count + 1

        Block1_count = 2

        for l in Planet_List_loop:

            if ws[signs_List_ws[ws['B'+str(Block1_count)].value]].value== None:

                ws[signs_List_ws[ws['B' + str(Block1_count)].value]] =  ws['A' + str(Block1_count)].value

            else:
                ws[signs_List_ws[ws['B'+str(Block1_count)].value]]=ws[signs_List_ws[ws['B'+str(Block1_count)].value]].value+ "/" +ws['A'+str(Block1_count)].value

            Block1_count = Block1_count + 1

        Block1_count = 2

        for k in Planet_List_loop:

            if ws[House_List_ws[ws['M' + str(Block1_count)].value]].value== None:

                ws[House_List_ws[ws['M' + str(Block1_count)].value]] = ws['A' + str(Block1_count)].value
            else:

                ws[House_List_ws[ws['M' + str(Block1_count)].value]] = ws[House_List_ws[ws['M' + str(Block1_count)].value]].value+ "/" + ws['A' + str(Block1_count)].value

            Block1_count = Block1_count + 1

    def GetAyanamsa(self, Bday_accurate):

        ayan = swe.get_ayanamsa_ut(self.Bday_accurate[1])

        print("Ayanamsa = ", self.prnt(self.decdeg2dms(ayan)))


    def ReadingSetup(self,Name,POB,Chart_type):
        print("Name: " + Name)
        print("Place of Birth = " + POB)
        print("Chart Type = " + Chart_type)

    def DateTime(self,year,month,date,hr,min,sec):

        return swe.utc_to_jd(year,month,date,hr,min,sec,GREG_CAL)

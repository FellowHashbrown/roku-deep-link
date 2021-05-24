#!/usr/bin/python3
from requests import post

IP_ADDRESS="REPLACE ME"

season1 = [198443, 198453, 198457,
           198461, 198465, 198469]
season2 = [198474, 198481, 198485, 198489, 198493,
           198497, 198501, 198505, 198509, 198513,
           198517, 198521, 198525, 198529, 198533,
           198537, 198541, 198545, 198549, 198553,
           198557, 198561]
season3 = [198569, 198573, 198577, 198581, 198585,
           198589, 198593, 198597, 198601, 198609,
           198613, 198617, 198621, 198625, 198629,
           198633, 198637, 198641, 198645, 198649,
           198653, 198657, 198661]

season4 = [198669, 198673, 198677, 198681, 198685,
           198689, 198693, 198697, 198701, 198705,
           198709, 198713, 198717, 198721]
season5 = [198726, 198733, 198737, 198741, 198745,
           198749, 198753, 198757, 198761, 198765,
           198769, 198773, 198777, 198781, 198785,
           198789, 198793, 198797, 198801, 198805,
           198809, 198813, 198817, 198821, 198825,
           198829]
season6 = [198834, 198841, 198845, 198849, 198853,
           198857, 198861, 198865, 198869, 198873,
           198877, 198881, 198885, 198889, 198893,
           198897, 198901, 198905, 198909, 198913,
           198917, 198921, 198925, 198929, 198933,
           198937]

season7 = [200306, 200310, 200314, 200318, 200322,
           200326, 200330, 200334, 200338, 200342,
           200346, 200350, 200360, 200368, 200372,
           200376, 200380, 200384, 200388, 200392,
           200396, 200404, 200408, 200413, 200422,
           200428]
season8 = [230410, 230414, 230418, 230430, 230450,
           230454, 230458, 230462, 230466, 230470,
           230474, 230478, 230482, 230486, 230490,
           230494, 230498, 230502, 230506, 230510,
           334362, 334366, 334370, 334374]
season9 = [365472, 365476, 365480, 365484, 365488,
           365492, 365496, 365500, 365504, 365508,
           365512, 365516, 365524, 365520, 365528,
           365532, 365536, 365540, 365544, 365548,
           365552, 365556, 445773, 446359, 446363,
           446367, 446371]
seasons = [season1, season2, season3,
           season4, season5, season6,
           season7, season8, season9]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: the_office.py <season> <episode>")
    else:
        season = int(sys.argv[1])
        episode = int(sys.argv[2])
        if season < 1 or season > 9:
            print(f"{season} is out of range (1-9)")
        else:
            season -= 1
            if episode < 1 or episode > len(seasons[season]):
                print(f"{episode} is out of range (1-{len(seasons[season])})")
            else:
                episode -= 1
                post("http://{}:8060/launch/13842?contentId={}&mediaType={}".format(
                    IP_ADDRESS, seasons[season][episode], "episode"))

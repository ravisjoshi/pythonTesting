"""
You're now a baseball game point recorder.
Given a list of strings, each string can be one of the 4 following types:
    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.
You need to return the sum of the points you could get in all the rounds.

Input: ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Input: ["5","-2","4","C","D","9","+","+"]  /  Output: 27
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.

Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.
"""
from time import time

class Solution:

    def calPoints_BruteForce(self, ops):
        slist = []
        for op in ops:
            if op == 'C':
                slist.pop(-1)
            elif op == 'D':
                slist.append(int(slist[-1])*2)
            elif op == '+':
                slist.append(int(slist[-1])+int(slist[-2]))
            else:
                slist.append(int(op))
        return sum(slist)

    def calPoints(self, ops):
        slist = []
        lops = list(ops)
        index = 0
        while index < len(lops):
            # print('I am at:{}  i={}'.format(lops[index], index))
            if lops[index] == 'C':
                lops.pop(index-1)
                lops.pop(index-1)
                index -= 1
            elif lops[index] == 'D':
                lops.pop(index)
                lops.insert(index, int(lops[index-1])*2)
                index += 1
            elif lops[index] == '+':
                lops.pop(index)
                temp = lops[index-1] + lops[index-2]
                lops.insert(index, temp)
                index += 1
            else:
                lops[index] = int(lops[index])
                index += 1


        return sum(lops)



s = Solution()

ops = ["5","2","C","D","+"]
print(s.calPoints(ops))

ops = ["5","-2","4","C","D","9","+","+"]
print(s.calPoints(ops))

start = time()
ops = ["-1077","C","12019","-19870","+","9541","7375","+","C","29534","18056","D","20324","21554","C","19512","-22593","C","-23780","D","-21505","C","-3126","-23104","C","D","+","-24162","-351","C","D","+","23126","7477","26374","C","+","297","D","+","C","-11681","+","3047","+","C","+","25670","377","-21650","25191","+","D","-27852","C","-14140","C","-22184","-7839","-3553","15914","C","15814","20955","D","+","D","D","-15670","20092","D","D","-23704","+","18861","C","16174","+","18558","5093","9206","+","-9257","3040","11876","-18700","-20411","17802","-1083","D","22718","24580","C","-9502","C","1856","C","15935","D","D","-27153","-2103","C","-4956","+","3173","3368","+","D","-26373","C","+","C","-7103","C","D","+","C","20772","-14048","16365","D","D","-4483","1840","-8309","-6313","D","C","D","D","-28023","-29986","20284","C","+","+","-22582","D","-3252","9764","C","+","D","C","-11170","D","+","-20181","7193","+","-15672","C","-3282","C","-17314","26287","-6652","15009","C","6310","D","D","+","23780","C","-19206","D","D","7698","6163","-7002","+","+","22885","D","+","26861","+","-12447","C","-23756","C","22865","25892","-19447","C","-2519","7184","D","C","D","3279","6799","-11006","17569","C","D","18596","-2942","D","17183","4513","+","+","C","D","1064","9060","-7823","-12783","C","8402","C","-6231","C","-27214","C","25849","-5832","D","-14186","D","22307","+","D","17265","3146","+","C","D","+","+","23760","9080","20104","-3115","24248","+","6443","D","27570","D","2594","D","14586","C","D","-29314","-28354","-26849","-5578","-16469","C","D","-25156","C","+","-23198","-1580","-20313","-16505","28937","-11754","-1730","7319","D","10728","+","+","-2841","+","+","6517","+","-17397","-24120","+","+","8104","C","-4952","C","-4151","2001","D","-28761","26189","-1515","D","7616","4661","D","+","-3424","-2829","D","29528","D","10443","-6373","-3474","D","14258","+","-14994","24593","25330","-6338","15818","-28893","D","D","+","25613","20343","25250","10157","D","9981","-4684","+","24381","-14271","D","C","-13902","-26545","20014","28540","16487","D","-11052","+","-18681","-81","+","+","C","-7225","+","5996","D","C","C","C","C","C","C","-11861","C","-27347","-3731","C","14496","C","C","+","-18513","-13151","-13374","18811","-29845","-6341","-947","6951","D","-15229","1156","-1497","D","D","-20138","-24178","+","24902","5719","-10066","-26400","-7948","-4868","-726","-4877","-799","29569","-2703","-4556","25670","2671","-1587","D","24283","C","C","9668","13844","C","+","-26947","D","+","C","28224","-19801","+","-27160","14083","4859","D","D","-24815","+","C","D","-21498","9848","-19982","+","21210","-5514","-17963","23080","-16414","-18100","+","16701","+","-15027","D","3876","29463","-10535","-17746","-14678","-25839","5355","-377","-27853","-16239","D","+","10851","C","23509","-2650","+","22199","+","4947","C","15955","-14081","5252","-27264","-22891","C","-25133","C","D","13375","-7986","7745","10355","6667","C","+","C","-5034","C","D","C","+","C","14362","C","11052","12612","+","10349","D","D","10098","-19195","1718","15332","20766","19827","18489","+","-7496","4837","D","D","28814","+","4293","16510","C","-25579","-8045","-10401","C","D","-1358","D","+","-22406","16883","D","-13518","+","D","+","C","3895","-12990","-3566","-18379","C","D","18133","+","D","C","-2563","13957","6847","D","D","C","2685","28221","-22893","-485","-27214","4646","C","14175","3367","C","-10460","C","3420","+","23427","C","25895","C","D","D","+","C","D","C","4660","-8635","C","8299","18690","C","C","10136","D","3929","28048","C","24789","+","-13078","12726","-12206","C","22579","25762","+","D","6267","D","-19077","2091","C","19623","C","C","+","+","+","18665","D","D","+","-925","3644","+","21322","10880","D","+","C","11490","7601","29162","5084","22505","+","-20356","-18135","D","D","-12168","4777","26865","+","+","D","C","C","+","D","11734","D","-29443","D","+","5071","6723","18981","D","-11260","21882","-23711","9612","-9667","+","C","C","4259","C","427","+","-13414","C","2747","D","-19989","-10275","-15","-27538","-13157","+","-11445","9937","+","D","-8460","+","+","+","D","-25544","-11911","3347","9961","D","D","+","19125","D","4794","D","2207","27884","C","-22238","C","11951","19614","C","+","-17260","D","C","-27984","27645","C","+","D","1704","D","23758","23226","26406","C","D","C","17794","28184","-27354","19537","+","19522","C","-13887","C","15864","-28057","-28078","C","29633","-14428","20570","+","+","D","-18219","+","-23481","14244","14717","+","-6464","C","+","16603","12981","C","-23575","C","-25045","-19113","-15871","C","-23103","-12109","-6007","+","D","C","-894","-1736","+","8426","-16786","-3174","20039","-3619","+","9099","826","-22051","7451","21351","15255","-6203","11523","D","4754","-24534","D","D","+","24126","C","+","24200","+","-21399","23441","D","-8790","D","D","-12656","17688","24301","-143","25271","-5214","28855","25022","C","-3043","-10265","-5658","-21111","C","-11142","+","C","-16009","+","3467","3259","+","+","C","D","-18439","-15084","D","D","C","C","609","27166","D","-18119","-16022","C","-29778","-18902","-7509","17141","D","-24677","+","C","+","12188","-4860","-29551","-11457","-20204","C","+","15396","-23201","D","26288","7751","C","-2050","3053","-7607","6912","8093","8519","5172","25942","-6544","C","D","C","639","C","C","2981","+","11417","19351","+","-3997","-27241","-4477","23398","20277","16275","+","7425","D","4515","-12388","C","-15508","C","21800","C","D","-2126","C","C","14329","54","C","10183","5831","-6236","-24840","D","28037","-15149","-4274","2509","+","+","+","D","8292","-3152","-1208","D","C","14259","29830","13596","20676","-24908","28409","-2231","+","D","+","-3433","-5727","C","D","-4027","-7734","9532","21731","-2590","17317","D","C","20659","25399","+","-15613","C","+","+","C","-12114","D","-1718","C","-24507","23030","D","10089","8728","-24893","-15616","D","+","D","C","6860","+","-4039","-19735","-22196","19647","D","D","D","2210","D","-20124","20619","5158","C","25632","C","10058","-20707","-29879","+","24689","-9003","19263","+","20202","C","C","-6811","D","28209","25914","+","-28184","C","21432","2010","+","C","D","-14553","1062","D","-10642","8180","599","17269","-1904","+","D","C","D","D","+","8716","10839","D","22042","+","+","-29169","+","+"]
print(s.calPoints(ops))
end = time()
print("Elapsed time: {}".format(end-start))

start = time()
ops = ["-1077","C","12019","-19870","+","9541","7375","+","C","29534","18056","D","20324","21554","C","19512","-22593","C","-23780","D","-21505","C","-3126","-23104","C","D","+","-24162","-351","C","D","+","23126","7477","26374","C","+","297","D","+","C","-11681","+","3047","+","C","+","25670","377","-21650","25191","+","D","-27852","C","-14140","C","-22184","-7839","-3553","15914","C","15814","20955","D","+","D","D","-15670","20092","D","D","-23704","+","18861","C","16174","+","18558","5093","9206","+","-9257","3040","11876","-18700","-20411","17802","-1083","D","22718","24580","C","-9502","C","1856","C","15935","D","D","-27153","-2103","C","-4956","+","3173","3368","+","D","-26373","C","+","C","-7103","C","D","+","C","20772","-14048","16365","D","D","-4483","1840","-8309","-6313","D","C","D","D","-28023","-29986","20284","C","+","+","-22582","D","-3252","9764","C","+","D","C","-11170","D","+","-20181","7193","+","-15672","C","-3282","C","-17314","26287","-6652","15009","C","6310","D","D","+","23780","C","-19206","D","D","7698","6163","-7002","+","+","22885","D","+","26861","+","-12447","C","-23756","C","22865","25892","-19447","C","-2519","7184","D","C","D","3279","6799","-11006","17569","C","D","18596","-2942","D","17183","4513","+","+","C","D","1064","9060","-7823","-12783","C","8402","C","-6231","C","-27214","C","25849","-5832","D","-14186","D","22307","+","D","17265","3146","+","C","D","+","+","23760","9080","20104","-3115","24248","+","6443","D","27570","D","2594","D","14586","C","D","-29314","-28354","-26849","-5578","-16469","C","D","-25156","C","+","-23198","-1580","-20313","-16505","28937","-11754","-1730","7319","D","10728","+","+","-2841","+","+","6517","+","-17397","-24120","+","+","8104","C","-4952","C","-4151","2001","D","-28761","26189","-1515","D","7616","4661","D","+","-3424","-2829","D","29528","D","10443","-6373","-3474","D","14258","+","-14994","24593","25330","-6338","15818","-28893","D","D","+","25613","20343","25250","10157","D","9981","-4684","+","24381","-14271","D","C","-13902","-26545","20014","28540","16487","D","-11052","+","-18681","-81","+","+","C","-7225","+","5996","D","C","C","C","C","C","C","-11861","C","-27347","-3731","C","14496","C","C","+","-18513","-13151","-13374","18811","-29845","-6341","-947","6951","D","-15229","1156","-1497","D","D","-20138","-24178","+","24902","5719","-10066","-26400","-7948","-4868","-726","-4877","-799","29569","-2703","-4556","25670","2671","-1587","D","24283","C","C","9668","13844","C","+","-26947","D","+","C","28224","-19801","+","-27160","14083","4859","D","D","-24815","+","C","D","-21498","9848","-19982","+","21210","-5514","-17963","23080","-16414","-18100","+","16701","+","-15027","D","3876","29463","-10535","-17746","-14678","-25839","5355","-377","-27853","-16239","D","+","10851","C","23509","-2650","+","22199","+","4947","C","15955","-14081","5252","-27264","-22891","C","-25133","C","D","13375","-7986","7745","10355","6667","C","+","C","-5034","C","D","C","+","C","14362","C","11052","12612","+","10349","D","D","10098","-19195","1718","15332","20766","19827","18489","+","-7496","4837","D","D","28814","+","4293","16510","C","-25579","-8045","-10401","C","D","-1358","D","+","-22406","16883","D","-13518","+","D","+","C","3895","-12990","-3566","-18379","C","D","18133","+","D","C","-2563","13957","6847","D","D","C","2685","28221","-22893","-485","-27214","4646","C","14175","3367","C","-10460","C","3420","+","23427","C","25895","C","D","D","+","C","D","C","4660","-8635","C","8299","18690","C","C","10136","D","3929","28048","C","24789","+","-13078","12726","-12206","C","22579","25762","+","D","6267","D","-19077","2091","C","19623","C","C","+","+","+","18665","D","D","+","-925","3644","+","21322","10880","D","+","C","11490","7601","29162","5084","22505","+","-20356","-18135","D","D","-12168","4777","26865","+","+","D","C","C","+","D","11734","D","-29443","D","+","5071","6723","18981","D","-11260","21882","-23711","9612","-9667","+","C","C","4259","C","427","+","-13414","C","2747","D","-19989","-10275","-15","-27538","-13157","+","-11445","9937","+","D","-8460","+","+","+","D","-25544","-11911","3347","9961","D","D","+","19125","D","4794","D","2207","27884","C","-22238","C","11951","19614","C","+","-17260","D","C","-27984","27645","C","+","D","1704","D","23758","23226","26406","C","D","C","17794","28184","-27354","19537","+","19522","C","-13887","C","15864","-28057","-28078","C","29633","-14428","20570","+","+","D","-18219","+","-23481","14244","14717","+","-6464","C","+","16603","12981","C","-23575","C","-25045","-19113","-15871","C","-23103","-12109","-6007","+","D","C","-894","-1736","+","8426","-16786","-3174","20039","-3619","+","9099","826","-22051","7451","21351","15255","-6203","11523","D","4754","-24534","D","D","+","24126","C","+","24200","+","-21399","23441","D","-8790","D","D","-12656","17688","24301","-143","25271","-5214","28855","25022","C","-3043","-10265","-5658","-21111","C","-11142","+","C","-16009","+","3467","3259","+","+","C","D","-18439","-15084","D","D","C","C","609","27166","D","-18119","-16022","C","-29778","-18902","-7509","17141","D","-24677","+","C","+","12188","-4860","-29551","-11457","-20204","C","+","15396","-23201","D","26288","7751","C","-2050","3053","-7607","6912","8093","8519","5172","25942","-6544","C","D","C","639","C","C","2981","+","11417","19351","+","-3997","-27241","-4477","23398","20277","16275","+","7425","D","4515","-12388","C","-15508","C","21800","C","D","-2126","C","C","14329","54","C","10183","5831","-6236","-24840","D","28037","-15149","-4274","2509","+","+","+","D","8292","-3152","-1208","D","C","14259","29830","13596","20676","-24908","28409","-2231","+","D","+","-3433","-5727","C","D","-4027","-7734","9532","21731","-2590","17317","D","C","20659","25399","+","-15613","C","+","+","C","-12114","D","-1718","C","-24507","23030","D","10089","8728","-24893","-15616","D","+","D","C","6860","+","-4039","-19735","-22196","19647","D","D","D","2210","D","-20124","20619","5158","C","25632","C","10058","-20707","-29879","+","24689","-9003","19263","+","20202","C","C","-6811","D","28209","25914","+","-28184","C","21432","2010","+","C","D","-14553","1062","D","-10642","8180","599","17269","-1904","+","D","C","D","D","+","8716","10839","D","22042","+","+","-29169","+","+"]
print(s.calPoints_BruteForce(ops))
end = time()
print("Elapsed time: {}".format(end-start))


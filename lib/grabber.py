from opgg.opgg import OPGG
from opgg.summoner import Summoner


def test():    
    opgg = OPGG()
    
    summoner: Summoner
    for summoner in opgg.search(["NVeEnzo"]):
        print(summoner)
        

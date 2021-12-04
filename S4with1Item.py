# S4 Standard Settings

from datetime import datetime
import random

nowAlex = datetime.now() 
# Alex is appended to the end of variable names to avoid variable overlap

timestampAlex = datetime.timestamp(nowAlex)

random.seed(timestampAlex)

def assignPermalinkAlex(startingItemIndexAlex):
    if startingItemIndexAlex == 1: # Bait Bag Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAggAAAAAAQAA"
        startingItemAlex = "the Bait Bag"
    elif startingItemIndexAlex == 2: # Bombs Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAhAAAAAAAQAA"
        startingItemAlex = "Bombs"
    elif startingItemIndexAlex == 3: # Boomerang Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAiAAAAAAAQAA"
        startingItemAlex = "the Boomerang"
    elif startingItemIndexAlex == 4: # Deku Leaf Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAgABAAAAAQAA"
        startingItemAlex = "the Deku Leaf"
    elif startingItemIndexAlex == 5: # Hookshot Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAgAAAgAAAQAA"
        startingItemAlex = "the Hookshot"
    elif startingItemIndexAlex == 6: # Power Bracelets Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAgAAAAQAAQAA"
        startingItemAlex = "the Power Bracelets"
    elif startingItemIndexAlex == 7: # Bow Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAgAAAAAEAQAA"
        startingItemAlex = "a Bow"
    elif startingItemIndexAlex == 8: # Skull Hammer Start
        samplePermalinkWithStartingItemAlex = "MS45LjAAU2FtcGxlUGVybWFsaW5rcwAFCyIAD3DAAgAAAAgAAQAA"
        startingItemAlex = "the Skull Hammer"
    return samplePermalinkWithStartingItemAlex, startingItemAlex




startingItemIndexAlex = random.randint(1,8)
startingItemResultAlex = assignPermalinkAlex(startingItemIndexAlex)
print("Your starting item is {}.".format(startingItemResultAlex[1]))
print("Your sample permalink is {}.".format(startingItemResultAlex[0]))



 

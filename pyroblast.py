from requests import get, exceptions
from helpers import urlBuilder

SCRYFALL_API_URL = "https://api.scryfall.com/"


def getSet(setCode:str = None, scryfallID:str = None, tcgPlagerID:int= None):
    ''' 
    This function is a wrapper for the /sets endpoint in scryfall's API
    - The setCode, scryfallID, and tcgPlayerID args are all optional and all exclusive (only one may be used at a time)
    - setCode (str) : adding a value for the setCode argument will return the endpoint of /sets/:setCode endpoint of the srcyfall api.  This value should be the Set Code from a magic set
    - scryfallID (str) : adding a value for the scryfallID argument will return the endpoint of /sets/:scryfallID endpoint of the scryfall api.  This value should be the scryfall id of a magic set
    - tcgPlayerID (int) : adding a value for the tcgPlayerID argument will return the endpoint of /sets/tcgplayer/:tcgPLayerID endpoint of the scryfall api.  This value should be the tcgplayer id of a magic set
    '''
    if setCode == None and scryfallID == None and tcgPlagerID == None:
        try:
            req = get(urlBuilder(SCRYFALL_API_URL, "sets"))
            assert req.status_code == 200
            return req.json()
        except AssertionError:
            print("An error has occurred")
        except exceptions.ConnectionError:
            raise ConnectionError("ERROR: Unable to make connection to " + SCRYFALL_API_URL)
    elif not ((setCode is not None) ^ (scryfallID is not None) ^ (tcgPlagerID is not None)):
        raise SyntaxError("Please use either Set Code, Scryfall ID or TCGPlayer ID, not more than one")
    elif setCode is not None:
        try:
            req = get(urlBuilder(SCRYFALL_API_URL, "sets", setCode))
            assert req.status_code == 200 
            return req.json()
        except AssertionError:
            if req.status_code == 404:
                raise ValueError(f"The Set '{setCode}' does not exist, please try again")
        except exceptions.ConnectionError:
            raise ConnectionError("ERROR: Unable to make connection to " + SCRYFALL_API_URL)
    elif scryfallID is not None:
        try:
            req = get(urlBuilder(SCRYFALL_API_URL, "sets", scryfallID))
            assert req.status_code == 200 
            return req.json()
        except AssertionError:
            if req.status_code == 404:
                raise ValueError(f"The Set with id '{scryfallID}' does not exist, please try again")
        except exceptions.ConnectionError:
            raise ConnectionError("ERROR: Unable to make connection to " + SCRYFALL_API_URL)
    elif tcgPlagerID is not None:
        if type(tcgPlagerID) != type(1):
            raise TypeError(f"tcgPlayerID type should be 'int' not '{type(tcgPlagerID)}'")
        try:
            req = get(urlBuilder(SCRYFALL_API_URL, "sets", "tcgplayer", tcgPlagerID))
            assert req.status_code == 200 
            return req.json()
        except AssertionError:
            if req.status_code == 404:
                raise ValueError(f"The Set with tcgplayerid '{tcgPlagerID}' does not exist, please try again")
        except exceptions.ConnectionError:
            raise ConnectionError("ERROR: Unable to make connection to " + SCRYFALL_API_URL)



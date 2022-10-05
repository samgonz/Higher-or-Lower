import random
import followerData

def getFirstSelection(randomFirstSelection):
    firstSelectionName = followerData.data[randomFirstSelection-1]['name']
    firstSelectionDescription = followerData.data[randomFirstSelection-1]['description']
    firstSelectionCountry = followerData.data[randomFirstSelection-1]['country']
    print(f'\nCelebrity: {firstSelectionName}')
    print(f'Description: {firstSelectionDescription}')
    print(f'Country: {firstSelectionCountry}')
    
def getSecondSelection(randomSecondSelection):    
    secondSelectionName = followerData.data[randomSecondSelection-1]['name']
    secondSelectionDescription = followerData.data[randomSecondSelection-1]['description']
    secondSelectionCountry = followerData.data[randomSecondSelection-1]['country']
    print(f'Celebrity: {secondSelectionName}')
    print(f'Description: {secondSelectionDescription}')
    print(f'Country: {secondSelectionCountry}\n')
    
def getRandomCelebrity():
    return random.randint(0, len(followerData.data))    

def getFollowerCount(selection):
    return int(followerData.data[selection-1]['follower_count'])
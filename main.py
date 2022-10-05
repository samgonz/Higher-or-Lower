import splashScreen
import getSelectionData
import followerData

print(splashScreen.logo)
print(splashScreen.instructions)
playGame = input('Type [enter] to start game\n').lower()
winningCelebrity = 0
userGuess = 0

while playGame == 'enter':
    # Gets the random celberity from followerData.data
    randomFirstSelection = getSelectionData.getRandomCelebrity()
    randomSecondSelection = getSelectionData.getRandomCelebrity()
    
    # Gets the random celberity data and prints it out
    getSelectionData.getFirstSelection(randomFirstSelection)
    print(splashScreen.versus)
    getSelectionData.getSecondSelection(randomSecondSelection)
    
    userGuess = int(input('Who has a higher follower count, choose 1 for top and 2 for bottom\n'))
    
    # Gets the follower count of 1st and 2nd celberity. Then it subtracts them to get a negative or positive count
    followerCount = getSelectionData.getFollowerCount(randomFirstSelection) - getSelectionData.getFollowerCount(randomSecondSelection)
    
    # Checks to see which celebrity has more followers
    if followerCount > 1:
        print(followerData.data[randomFirstSelection-1]['name'],', is the winning Celebrity.')
        winningCelebrity = 1
        break
    elif followerCount == 0:
        print('Both celberities had the same follower count.')
        winningCelebrity = 0
        break
    else:
        print(followerData.data[randomSecondSelection-1]['name'],', is the winning Celebrity.')
        winningCelebrity = 2
        break
 
# Checks to see if user is a winner or loser    
if winningCelebrity == userGuess:
    print('Congratulations! You win!\n')        
elif winningCelebrity == 0:
    print('Try again,\n')
else:
    print('Unfortunately, you lost.\n')

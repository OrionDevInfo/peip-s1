import tp05_j421, tp05_bandit, tp05_roulette

def p() :
    print("Let's play!")
    g = input('Choose a game:\nA - 421\nB - Bandit manchot\nC - Roulette\n')
    if g == 'A' : tp05_j421.main421()
    elif g == 'B' : tp05_bandit.mainBandit()
    elif g == 'C' : tp05_roulette.mainRoulette()

if __name__ == '__main__' :
    p()

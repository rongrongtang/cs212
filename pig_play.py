import random

other={0:1,1:0}
def diceGen():
    while True:
        yield random.randint(1,6)
        
def toll(state,d):
    (p,me,you,pending)=state
    if d==1:
        return (other[p],you,me+1,0)
    else:
        return (p,me,you,pending+d)
    
def hold_at(x):
    def score(state):
        (p,me,you,pending)=state
        if me+pending>=x:
            return (p,me+pending,you,0)
        else:
            return (other[p],you,me+pending,0)
    return score

def strategy():
    strategies=['hold','toll']
    return random.choice(strategies)

def pig(playnames,dice=diceGen()):
    state=(0,0,0,0)    
    goal=30
    while(True):
        (p,me,you,pending)=state
        if me>=goal:
            return playnames[p]+'win'
        elif you>=goal:
            return playnames[other[p]]+'win'
        else:
            print('it is %s turn'%playnames[p])
            choice=strategy()
            print(choice)
            if choice=='hold':
                state=hold_at(goal)(state)
                (p,me,you,pending)=state
                print('%s score is %d'%(playnames[other[p]],you))
            else:
                d=next(dice)
                print('dice is',d)
                state=toll(state,d)
                (p,me,you,pending)=state
                if pending==0:
                    print('pending is 1,score is ',you)
                else:
                    print('%s pending is %d,score is %d'%(playnames[p],pending,pending+me))
                
    
def test():
    dice=iter([6,6,6,6,6,6,6,6,2])
    print(pig(['zly','running']))
test()
            
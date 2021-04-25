import copy

def empty(state,cap):
    d={}    
    for i in range(len(state)):
        if state[i]!=0:
            stateList=list(copy.copy(state))
            stateList[i]=0
            d[tuple(stateList)]=('empty ',i+1)        
    return d
    
def full(state,cap):    
    d={}
    
    for i in range(len(state)):
        stateList=list(copy.copy(state))
        stateList[i]=cap[i]
        d[tuple(stateList)]=('full ',i+1)
    return d

def pour1T2(state,cap1,cap2):
    """pour cap1 to cap2"""
    x,y=state
    X=cap1
    Y=cap2
    return (0,x+y) if x+y<Y else (x-(Y-y),Y)    


def pSuccessors(state,cap):
    d={}
    emp=empty(state,cap)
    ful=full(state,cap)
    d.update(emp.items())
    d.update(ful.items())
    newDic={}
    for i in range(len(cap)):
        for j in range(len(cap)):
            if i!=j:
                newState=list(copy.copy(state))
                pourState=(state[i],state[j])
                cap1=cap[i]
                cap2=cap[j]
                remaind1,remaind2=pour1T2(pourState,cap1,cap2)
                newState[i]=remaind1
                newState[j]=remaind2
                newState=tuple(newState)
                newDic[newState]=('pour ',i+1,j+1)
    d.update(newDic)
    return d

def search(caps,goal):
    start=tuple([0]*len(caps))
    if goal in caps:
        return caps
    frontier=[[start]]
    visit=set()
    while(frontier):
        path=frontier.pop(0)
        state=path[-1]        
        for newstate,action in pSuccessors(state,caps).items():
            if newstate not in visit:
                visit.add(newstate)
                path2=path+[newstate]
                if goal in newstate:
                    return path2
                frontier.append(path2)

def test():
    caps=(1,2,4,8)
    goal=5
    print(search(caps,goal))
    
test()



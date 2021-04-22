def bsuccessors(state):
    here,there=state
    d={}    
    if 'light' in here:
        for a in here:
            for b in here:                
                if a!='light' and b!='light':                    
                    nh=here-frozenset((a,b,'light'))
                    nt=(there|frozenset((a,b,'light')))                    
                    d[(nh,nt)]=(a,b,'->')
                    
    else:
        for a in there:
            for b in there:
                if a!='light' and b!='light':
                    nh=frozenset(here|set((a,b,'light')))
                    nt=frozenset(there-set((a,b,'light')))                    
                    d[(nh,nt)]=(a,b,'<-')
    return d

def crossBridge(state,goal):
    if state==goal or not state:
        return state
    frontier=[[state]]    
    visit=set()     
    while(frontier):
        path=frontier.pop(0)
        state=path[-1]
        if not state or state==goal:
            return path
        visit.add(state)
        for newstate,action in bsuccessors(state).items():
            if newstate not in visit:             
                totalCost=bcost(action)+path_cost(path)
                path2=path+[(action,totalCost),newstate]
                frontier=addPath(frontier,path2)               
    return None

def bcost(action):
    a,b,direction=action
    return max(a,b)
                
def path_cost(path):
    if len(path)<3:
        return 0
    action,totalcost=path[-2]
    return totalcost

def addPath(frontier,path):
    old=None
    for i,p in enumerate(frontier):        
        if p[-1]==path[-1]:
            old=i  
    if old==None:
        frontier.append(path)   
    elif old!=None and path_cost(frontier[old])>path_cost(path):       
        del frontier[old]
        frontier.append(path)  
    return frontier

def test_addPath():
    frontier=[[((1,2),(5,10,'light')),((5,'<-'),5),((1,2,5),(10,'light'))]]
    path=[((1,2,5),(10,'light'))]
    print(addPath(frontier,path))
#test_addPath()

def test():
    here=frozenset([1,2,5,10,'light'])
    there=frozenset()    
    state=(here,there)
    goal=(there,here)
    b=crossBridge(state,goal)
    print(b)
test()

def testb():
    here=set()
    there=set([1,2,5,10,'light'])
    time=0
    print(bsuccessors((here,there)))

#testb()

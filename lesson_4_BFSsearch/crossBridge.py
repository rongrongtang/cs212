def bsuccessors(state):
    here,there,time=state
    d={}
    
    if 'light' in here:
        for a in here:
            for b in here:                
                if a!='light' and b!='light':                    
                    nh=frozenset(here-set((a,b,'light')))
                    nt=frozenset(there|set((a,b,'light')))                    
                    d[(nh,nt,max(a,b)+time)]=(a,b,'->')
                    
    else:
        for a in there:
            for b in there:
                if a!='light' and b!='light':
                    nh=frozenset(here|set((a,b,'light')))
                    nt=frozenset(there-set((a,b,'light')))                    
                    d[(nh,nt,max(a,b)+time)]=(a,b,'<-')
    return d

def crossBridge(state,goal):
    if state[:2]==goal or not state:
        return state
    frontier=[[state]]
    visit=set()    
    while(frontier):
        path=frontier.pop(0)
        state=path[-1]
        if not state or state[:2]==goal:
            return path
        for newstate,action in bsuccessors(state).items():
            if newstate not in visit:
                here,there,time=newstate                
                
                visit.add(newstate)
                path2=path+[action,newstate]               
                frontier.append(path2)                
                frontier.sort(key=tcost)
    return None

def tcost(path):
    return path[-1][2]
                
def esplate_time(path):
    state=path[-1]
    return state[2]
            
            
def test():
    here=set([1,2,5,10,'light'])
    there=set()
    time=0
    state=(here,there,time)
    goal=(there,here)
    b=crossBridge(state,goal)
    print(b)
test()

def testb():
    here=set()
    there=set([1,2,5,10,'light'])
    time=0
    print(bsuccessors((here,there,time)))

#testb()

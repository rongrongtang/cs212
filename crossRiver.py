def crossRiver(monkey,person,opMon,opPerson,boat):
    if boat==1:
        return {(monkey-2,person,opMon+2,opPerson,-boat),(monkey,person-2,opMon,opPerson+2,-boat),(monkey-1,person-1,opMon+1,opPerson+1,-boat),(monkey-1,person,opMon+1,opPerson,-boat),(monkey,person-1,opMon,opPerson+1,-boat)}
    else:
        return {(monkey+2,person,opMon-2,opPerson,-boat),(monkey,person+2,opMon,opPerson-2,-boat),(monkey+1,person+1,opMon-1,opPerson-1,-boat),(monkey+1,person,opMon-1,opPerson,-boat),(monkey,person+1,opMon,opPerson-1,-boat)}

def isLegal(m,p,om,op):
    if m<0 or p<0:
        return False
    elif (m>p and p!=0) or (om>op and op!=0):
        return False    
    return True

def success(m,p,om,op,b):
    s=[]
    for num in crossRiver(m,p,om,op,b):
        m,p,om,op,b=num        
        if isLegal(m,p,om,op):
            s.append((m,p,om,op,b))
    return s

#print(success(1,3,2,0,-1))

def crossBFS(goal=(0,0,3,3,-1),state=(3,3,0,0,1)):
    if goal==state:
        return state
    seq=[[state]]
    """list is a container. the content in the
list will be increased. so it's need 2-d list"""
    visited=set()
    visited.add(state)
    while seq:
        path=seq.pop(0)
        m,n,om,op,b=path[-1]
        for nextState in success(m,n,om,op,b):
            if nextState not in visited:
                visited.add(nextState)                
                path2=path+[nextState]                
                if goal==nextState:
                    return path2
                else:
                    seq.append(path2)
    return False
 
        
def test():    
    print(crossBFS())
    

test()
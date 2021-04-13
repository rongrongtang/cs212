def success(x,y,X,Y):
    assert x<=X and y<=Y
    return {(0,y),(x,0),(X,y),(x,Y),(0,x+y) if (x+y<=Y) else (x-(Y-y),Y),(x+y,0) if (x+y<=X) else (X,y-(X-x))}

def test():
    print(success(2,4,9,4))

def pureBFS(X,Y,goal,state=(0,0)):
    if goal in state:
        return state
    seq=[[state]]
    """list is a container. the content in the
list will be increased. so it's need 2-d list"""
    visited=set()
    visited.add(state)
    while seq:
        path=seq.pop(0)
        x,y=path[-1]
        for nextState in success(x,y,X,Y):            
            if nextState not in visited:
                visited.add(nextState)                
                path2=path+[nextState]                
                if goal in nextState:
                    return path2
                else:
                    seq.append(path2)
    return False


def pureDFS(X,Y,goal,state=(0,0)):
    if goal in state:
        return state
    stack=[]
    visit=set()
    visit.add(state)
    stack.append([state])
    while(stack):
        path=stack.pop(-1)
        x,y=path[-1]
        for nextState in success(x,y,X,Y):            
            if nextState not in visit:
                visit.add(nextState)                
                path2=path+[nextState]                
                if goal in nextState:
                    return path2
                else:
                    stack.append(path2)
    return False
        
        
        
def testPur():    
    print(pureBFS(9,4,6))
    print(pureDFS(9,4,6))

testPur()
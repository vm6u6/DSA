# Directed Acyclic Graph (DAG)

def CourseSchedule ( numC, pre ):
    visited = []
    for i in range( numC ):
        visited.append(0)
    course = []
    for i in range( numC ):
        tmp = []
        for j in range( numC ):
            tmp.append(0)
        course.append(tmp)
    for u, v in pre:
        course[u][v] = 1

    for i in range( numC ):
        if dfs( course, visited, i ) == False:
            return False
    return True

def dfs ( course, visited, i ):
    L = len(course[i])
    for j in range( L ):
        if ( course[i][j] == 1 ):
            visited[i] == 1
            if visited[j] == 1:
                return False
            else:
                if dfs( course, visited, j ) == False:  
                    return False
                visited[i] = 0

numCourses = 2
prerequisites = [[1,0]]
print( CourseSchedule( numCourses, prerequisites ) )
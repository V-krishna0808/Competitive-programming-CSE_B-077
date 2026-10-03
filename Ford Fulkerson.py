from collections import deque
def bfs(graph,source,sink,parent):
    visited=[False]*len(graph)
    queue=deque([source])
    visited[source]=True
    while queue:
        u=queue.popleft()
        for ind,val in enumerate(graph[u]):
            if not visited[ind] and val>0:
                queue.append(ind)
                visited[ind]=True
                parent[ind]=u
                if ind==sink:
                    return True
    return False
def ford_fulkerson(graph,source,sink):
    parent=[-1]*len(graph)
    max_flow=0
    while bfs(graph,source,sink,parent):
        path_flow=float("Inf")
        s=sink
        while s!=source:
            path_flow=min(path_flow,graph[parent[s]][s])
            s=parent[s]
        max_flow+=path_flow
        v=sink
        while v!=source:
            u=parent[v]
            graph[u][v]-=path_flow
            graph[v][u]+=path_flow
            v=parent[v]
    return max_flow
v,e=map(int,input().split())
graph=[[0]*v for _ in range(v)]
for _ in range(e):
    u,v_node,w=map(int,input().split())
    graph[u][v_node]=w
print(ford_fulkerson(graph,0,v-1))

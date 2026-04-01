# List of servers receiving requests
#How many distinct servers
def find_distinct_servers(servers):
    map = {}
    for server in servers:
        if server in map:
            map[server] += 1

        else:
            map[server] = 1

    ans = []
    for m in map:
        ans.append(m)
    return ans

servers_1 = ['s1', 's2', 's3', 's2', 's1', 's4', 's2', 's4']
print(find_distinct_servers(servers_1))

#you're given a list if IP addresses from a logfile
# you need to find the IPs that appear more than n times

ips = [
    "192.168.1.1",
    "10.0.0.5",
    "192.168.1.1",
    "172.16.0.2",
    "192.168.1.1",
    "10.0.0.5"
]

N = 2

def find_ips_more_than_n_times(ips, N):
    ips_set = {}

    for ip in ips:
        if ip not in ips_set:
            ips_set[ip] = 1
        else:
            ips_set[ip] += 1

    ans = []
    for ip in ips_set:
        if ips_set[ip] > N:
            ans.append(ip)
            return "".join(ans)

    return -1

print(find_ips_more_than_n_times(ips, N))


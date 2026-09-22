def total_rows(rows):
    return len(rows)

def unique_ips(rows):
    return len(set(row['ip'] for row in rows))

from collections import Counter
def top_ips(rows,n=10):
    return Counter(row['ip'] for row in rows).most_common(n)

def status_count(rows):
    return Counter(row['status'] for row in rows)

def error_rate(rows):
    total,errors=0,0
   
    for row in rows:
        if row['status'] >= 500:
            errors+=1
        total+=1
    try:
        percentage=(errors/total)*100
    except ZeroDivisionError:
        return 0.00
    else:
        return percentage


def requests_per_hour(rows):
    d={}
    for row in rows:
        time=row['time'][12:14]
        d[time]=d.get(time,0)+1
    return d

def top_paths(rows,n=4):
    return Counter(row['path'] for row in rows).most_common(n)

def total_bytes(rows):
    return sum(row['size'] for row in rows)

if __name__=='__main__':
    from logparse import read_file,parse_line
    rows=[parse_line(i) for i in read_file('sample.log')]
    rows=[i for i in rows if i is not None]

    print('total request =',total_rows(rows))
    print('unique ips = ',unique_ips(rows))
    print('most ips = ',top_ips(rows))
    print('status count = ',dict(status_count(rows)))
    print('error rate = ',error_rate(rows))
    print('requests per hour = ',requests_per_hour(rows))
    print('top paths = ',top_paths(rows))
    print('total bytes = ',total_bytes(rows))
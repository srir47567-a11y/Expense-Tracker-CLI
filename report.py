from analyse import top_ips,unique_ips,total_rows,top_paths,total_bytes,error_rate,status_count
from logparse import read_file,parse_line
rows=[parse_line(i) for i in read_file('sample.log')]
rows=[i for i in rows if i is not None]

def header():
    print('=' * 30)
    print("LOG REPORT".center(30))
    print('=' * 30)

def sections(title,values):
    print()
    print(title)
    print('-'*20)

    for ips,count in values:
        print(f'{ips:<20}{count:>6}')
    

def print_numbers(title,values):
    print(f'{title:<15}:{values}')

nums=[('total request',total_rows),('unique_ips',unique_ips),('total_bytes',total_bytes),('error_rate',error_rate)]
section=[('top_ips',top_ips),('status count',status_count),('top paths',top_paths)]

if __name__=='__main__':
    header()
    
    for title,value in nums:
        print_numbers(title,value(rows))


    for title,value in section:
        sections(title,value(rows))
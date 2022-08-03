import argparse
import textwrap
import requests
import re,random,os,time
import prettytable as pt


def main(url):
    full_url = f"https://baidurank.aizhan.com:443/baidu/{url}/"
    session = requests.session()
    response = session.get(full_url)
    response_text = response.text

    with open('response_text.txt','w',encoding='u8')as f:
        f.write(response_text)
    with open('response_text.txt', 'r', encoding='u8')as rd:
        x = rd.readlines()
    for i in x:
        if '/images/br/' in i:
            text = i.strip()
            break
        elif '您的查询太频繁了' in i:
            print('您的查询太频繁了')
            return False
    pattern = re.compile(r'\d+')
    result = pattern.findall(text)
    print(f"{url}的百度权重是{result[0]}")

    Domain.append(url)
    Weight.append(result[0])

    os.remove('response_text.txt')
    time.sleep(2)

def banner():
    banner = """ 
  ______                _______ _                    _   
 |___  /               |__   __| |                  | |  
    / / ___ _ __ ___      | |  | |__  _ __ ___  __ _| |_ 
   / / / _ \ '__/ _ \     | |  | '_ \| '__/ _ \/ _` | __|
  / /_|  __/ | | (_) |    | |  | | | | | |  __/ (_| | |_ 
 /_____\___|_|  \___/     |_|  |_| |_|_|  \___|\__,_|\__|
                                                                                                                                                                                                                 
    """
    print(banner)


def result():
    table = pt.PrettyTable()
    table.add_column('编号', [i for i in range(1, len(Domain) + 1)])
    table.add_column('域名', [i for i in Domain])
    table.add_column('百度权重', [i for i in Weight])
    print(table)

if __name__ == '__main__':
    banner()
    Domain = []
    Weight = []
    parser = argparse.ArgumentParser(description='百度权重查询', formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:python DomainWeight.py -f url.txt'''))
    parser.add_argument("-f", type=argparse.FileType(mode='r',encoding='u8'), required=True,dest='file',help="Input file directory")
    args = parser.parse_args()
    with args.file as file:
        res = file.readlines()
    for url in res:
        url = url.strip()
        if main(url) == False:
            print('程序终止')
            break
    result()


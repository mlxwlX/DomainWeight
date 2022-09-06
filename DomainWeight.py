import argparse
import textwrap
import requests
import time
from bs4 import BeautifulSoup
import prettytable as pt


def main(url):
    full_url = f"https://baidurank.aizhan.com:443/baidu/{url}/"
    session = requests.session()
    response = session.get(full_url)
    response_text = response.text

    # bs4对html进行解析，寻找回复包中的关键字
    bs = BeautifulSoup(response_text, "html.parser")
    bs_list = []
    for item in bs.find_all("img"):
        bs_list.append(item.get("src"))
    for num in range(0, 15):
        logo = f"//statics.aizhan.com/images/br/{num}.png"
        if logo in bs_list:
            print(f"{url}的百度权重是{num}")
            break

    Domain.append(url)
    Weight.append(num)
    # 做延时，避免访问频繁
    time.sleep(1)


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
    parser.add_argument("-f", type=argparse.FileType(mode='r', encoding='u8'), required=False, dest='file',
                          help="Input file directory")

    parser.add_argument('-u', help='target url', dest='url',required=False)
    args = parser.parse_args()

    if args.url:
        main(args.url)
    if args.file:
        with args.file as file:
            res = file.readlines()
        for url in res:
            url = url.strip()
            main(url)
    result()

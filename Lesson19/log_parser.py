import argparse
import re
import json
from collections import defaultdict
# from collections import Counter TODO: не забыть упомянуть

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process access.log')
    # https://docs.python.org/3/library/argparse.html
    # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('-f', dest='file',  action='store', help='Path to logfile', default='access.log')
    args = parser.parse_args()

    dict_ip = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
    dict_meth = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
    total = 0

    client_errors = {}
    server_errors = {}

    with open(args.file) as file:
        for index, line in enumerate(file.readlines()):
            # 109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip is not None:
                ip = ip.group()

                total += 1
            else:
                continue

            method = re.search(r'] "(POST|GET|PUT|DELETE|HEAD)\s(.*)\sHTTP.*?"\s(\d+)', line)
            if method is not None:
                url = method.groups()[1]
                code = int(method.groups()[2])
                method = method.groups()[0]
                if 400 <= code <= 499:
                    client_errors[(url, method, code, ip)] = client_errors.get((url, method, code, ip), 0) + 1
                if 500 <= code <= 599:
                    server_errors[(url, method, code, ip)] = server_errors.get((url, method, code, ip), 0) + 1
            else:
                continue

            dict_meth[method] += 1
            dict_ip[ip][method] += 1

            # if index > 99:
            #     break

    top10 = sorted(dict_ip.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    top10_client_errors = sorted(client_errors.items(), key=lambda x: x[1], reverse=True)[:10]

    top10_server_errors = sorted(server_errors.items(), key=lambda x: x[1], reverse=True)[:10]

#    for item in dict_ip.items():
 #       print(item[1])

    # print(dict_ip)
    # print(json.dumps(dict_ip, indent=4))
    # print(json.dumps(dict_meth, indent=4))  # общее кол-во запросов
    # print(total)  # общее кол-во запросов
    # print(dict_ip)  # общее кол-во запросов
    # for item in top10:
    #    print(item[0], sum(item[1].values()))

    top10_list = []
    for item in top10:
        top10_list.append({'ip': item[0], 'requests': sum(item[1].values())})

    top10_client_errors_list = []
    for item in top10_client_errors:
        top10_client_errors_list.append({
            'url': item[0][0],
            'method': item[0][1],
            'code': item[0][2],
            'ip': item[0][3],
            'requests': item[1]})

    top10_server_errors_list = []
    for item in top10_server_errors:
        top10_server_errors_list.append({
            'url': item[0][0],
            'method': item[0][1],
            'code': item[0][2],
            'ip': item[0][3],
            'requests': item[1]})


    result = { 'total': total,
               'methods': dict_meth,
               'top10': top10_list,
               'top10_client_errors': top10_client_errors_list,
               'top10_server_errors': top10_server_errors_list,
    }

    print(json.dumps(result, indent=4))

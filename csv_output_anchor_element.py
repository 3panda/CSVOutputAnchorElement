#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests


def main(target_url):
    print(target_url)
    url = target_url
    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.RequestException as err:
        print(target_url + "の取得に失敗しました")
        print("エラーの内容は以下の通りです")
        print("---------------------")
        print(err)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        main(target_url=sys.argv[1])
    else:
        print("usage.")
        print("{filename} <target_url(ex:http://www.xxxxx)>"
              .format(filename=sys.argv[0]))

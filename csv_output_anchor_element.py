#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import csv


def main(target_url: str):
    print(target_url)
    url = target_url
    try:
        r = requests.get(url)
        with open('get.html', mode='w') as f:
            f.write(r.text)
            print(r.text)

        # CSVに書き出し
        csv_output()

    except requests.exceptions.RequestException as err:
        print(target_url + "の取得に失敗しました")
        print("エラーの内容は以下の通りです")
        print("---------------------")
        print(err)


def csv_output(output_name: str ="anchor_element.csv"):
    print(output_name + "に書き出し")

    body = [
        ['タイトル1', 'title1', 'title1.html'],
        ['タイトル2', 'title2', 'title2.html'],
        ['タイトル3', '', 'title3.html'],
        ['タイトル4', 'title4', 'title4.html'],
        ['タイトル5', '', 'title5.html'],
    ]
    with open(output_name, 'w') as f:
        # writerオブジェクト作成
        writer = csv.writer(f)
        # 内容を書き込む
        for b in body:
            writer.writerow(b)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        main(target_url=sys.argv[1])
    else:
        print("usage.")
        print("{filename} <target_url(ex:http://www.xxxxx)>"
              .format(filename=sys.argv[0]))

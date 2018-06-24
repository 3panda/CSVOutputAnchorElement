#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import bs4
import csv
from typing import List


def main(target_url: str):
    print(target_url)
    url = target_url
    a_elem_data = []
    try:
        # 指定されたhtmlを取得し一旦保存
        r = requests.get(url)
        with open('get.html', mode='w') as f:
            f.write(r.text)

        # 保存したhtmlを開く、解析
        f = open('get.html', 'r')
        soup = bs4.BeautifulSoup(f, "html.parser")
        elems = soup.select('a')
        for elem in elems:
            get_elem = []
            get_elem.append(elem.getText().replace('\n', ''))
            title = elem.get('title')
            if (title is None):
                title = ''
            get_elem.append(title.replace('\n', ''))
            get_elem.append(elem.get('href').replace('\n', ''))
            a_elem_data.append(get_elem)
        # ソートしておく
        a_elem_data.sort()
        # 重複データの削除
        formatted = deleted_to_duplicate_data(a_elem_data)

        # CSVに書き出し
        csv_output(formatted)

    except requests.exceptions.RequestException as err:
        print(target_url + "の取得に失敗しました")
        print("エラーの内容は以下の通りです")
        print("---------------------")
        print(err)


def deleted_to_duplicate_data(l: List[List[str]]) -> List[List[str]]:
    check_list = l
    del_num = []
    for i in range(len(l)):
        # 削除対象は探索しない
        if (i in del_num):
            break
        for j in range(len(check_list)):
            # 同じ値は

            if (i != j):
                duplicate_value = list(set(l[i]) & set(check_list[j]))
                duplicate_number = len(duplicate_value)
                # 重複要素　全ての場合は即削除
                # TODO: リンクテキスト, title属性, href属性のつ
                if duplicate_number == 3:
                    check_list[j] = ''
                # 重複要素 二つの場合は空が無ければ削除
                elif duplicate_number == 2:
                    if ('' not in duplicate_value):
                        check_list[j] = ''
    # 空白を削除して返す
    return filter(lambda str: str != '', check_list)


def csv_output(body: List[List[str]], output_name: str = "anchor_element.csv"):
    print(output_name + "に書き出し")
    with open(output_name, 'w', newline='') as f:
        # writerオブジェクト作成
        writer = csv.writer(
                 f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
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

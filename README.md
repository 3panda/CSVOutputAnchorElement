# CSVOutputAnchorElement
入力したURLの全てのアンカー要素の以下の値を取得しcsvに出力する

- テキスト
- title属性
- href属性


## 前提条件

### 動作環境
- Python3.6.4以上

### 使用パッケージ
- requests
- beautifulsoup4
```
pip install requests
pip install beautifulsoup4
```

## 利用方法
```
Python3 csv_output_anchor_element.py <target_url>
```

- <target_url>
アンカー要素の値を取得したいURL

## 出力結果

### 出力ファイル
```
anchor_element,csv
```

### 出力形式
```
アンカーテキスト,title属性の値,href属性の値
```

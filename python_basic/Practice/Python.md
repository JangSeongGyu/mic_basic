# Python 研修（応用編）

## 目標

- pip でパッケージ（ライブラリ）を管理できる。
- pandas を利用してデータの操作ができるようになる。
- pyodbc を利用して DB の操作ができるようになる。
- openpyxl を利用して Excel の作成、編集などができるようになる。

## pip とは？

### Python のパッケージ管理システム

Python で作られたソフトウェアは **\*パッケージ** という形で配布されますが、これらのパッケージをインストール したりアップデートしたりアンインストールしたりするためのツールが pip です。

## \*パッケージとは?

Python の機能を拡張するための追加モジュールやライブラリを指し、これらを用いることで様々な機能を手軽に利用することができます。

## pip を使うと何が便利?

他の開発者がすでに開発して公開している Python パッケージを簡単に導入できます。 自分で一からコードを書く必要がなくなり、新規開発の時間と労力を節約することができます。

## pip コマンド

- pip のバージョン確認

```
pip --version
```

- pip のアップデート

```
pip install --upgrade pip
```

- pip のインストール一覧確認

```
pip list
```

- pip のインストール

```
pip install [package_name]
```

- pip のアンインストール

```
pip uninstall [package_name]
```

# pandas とは

データ解析を容易にする機能を提供する Python のデータ解析ライブラリです。
データフレーム(DataFrame)などの独自のデータ構造が提供されており、様々な処理が可能です。
表形式のデータを SQL のように操作することが可能で、かつ高速で処理出来ます

```
pip install pandas
```

## pandas のデータ型

### Series

1 次元データ、列や行として使われる

```python
series_data = [10,15,20,25]
ser = pd.Series(series_data)
```

### DataFrame

2 次元データ、Seires で列と行が構成されているテーブル。

```python
dataframe_data = ([
    [100, "a", True],
    [200, "b", False],
    [150, "d", False],
    [550, "c", True]
])
df = pd.DataFrame(dataframe_data)
```

## 列名、行名の変更

### 行名（Index）の変更

```python
df.index=["01","02","03","04"]
```

### 列名（Column）の変更

```python
df.columns=["A","B","C"]
```

## データの範囲を指定

> ### 注意！
>
> ここからの研修は「titanic.csv」を活用して行う
>
> ```
> df = pd.read_csv("./titanic.csv")
> ```

### 列の指定

```python
df["Age"]
```

### 複数の列を指定

```python
df[["Age","Name"]]
```

### 行の指定

```python
print(df[0:10])
```

> ### 注意！
>
> [0:10]は列名の配列を Return するので問題ない。  
> [1]は列名が「１」というデータを探そうとするのでエラーが発生！
>
> ```python
> print(df[1])
> ```

### 行数の指定

上から{n}行までのデータを取る。

```python
df.head(number)
```

```python
df.head()
df.head(3)
```

下から{n}行までのデータを取る。

```python
df.tail(number)
```

```python
df.tail()
df.tail(3)
```

> ### 注意！
>
> 行数を入力しない場合、5 行までに表示されます。

### 複数の（行、列）名を指定

```python
df.loc[[行],[列]]
```

```python
print(df.loc[[2,5]]) # 行の指定
print(df.loc[:,["Age","Name"]]) # 列の指定
print(df.loc[[2,5],["Age","Name"]]) # 行、列の指定
```

### 複数の（行、列）Index を指定

```python
df.iloc[[行No],[列No]]
```

```python
print(df.iloc[1]) # 行指定
print(df.iloc[:,0:2]) #　列指定
print(df.iloc[1:3,1:3]) #　列、行指定
```

### 一つの結果のみ取得する

特定のデータのみ取得するので「loc、iloc」より早い

```python
print(df.at[0,"Age"])
print(df.iat[0,1])
```

### 比較演算子で範囲を指定

Age 列のデータが 30 以上だったら True、以外は False の配列を返す。

```python
df["Age"]>=30
```

条件に該当するデータのみ返す。

```python
df[df["Age"]]>=30
```

20,30 歳のデータを取得する。

```python
df[df["Age"].isin([20,30,40])]
```

## ソート

列を基準にソートする

```python
df.sort_values("列名")
```

```python
df.sort_values("B")
```

ascending が True = 昇順、False = 降順

```python
print(df.sort_values("B",ascending=False))
```

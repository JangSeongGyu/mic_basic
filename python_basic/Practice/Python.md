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

```
series_data = [10,15,20,25]
ser = pd.Series(series_data)
```

### DataFrame

2 次元データ、Seires で列と行が構成されているテーブル。

```python
dataframe_data = ([
    [100, "a", True],
    [150, "b", False],
    [300, "c", False],
    [550, "d", True]
])
df = pd.DataFrame(dataframe_data)
```

## 列名、行名の変更

### 行名（Index）の変更

```
df.index=["01","02","03","04"]
```

> ### 列名（Column）の変更
>
> ```
> df.columns=["A","B","C"]
> ```

## 表示する列名、行名の指定

### 列の指定

```
df["A"]
```

### 複数の列を指定

```
df[["B","C"]]
```

### 行の指定

```
print(df[0:1])
```

```

```

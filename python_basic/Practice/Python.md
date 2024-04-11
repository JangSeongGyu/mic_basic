<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap" rel="stylesheet">
<head>
<style>  
h1,h2,h3,h4,h5,h6,p {
    font-family: "Noto Sans JP", sans-serif;
}
</style>

</head>

# Python 研修（応用編）

## pip とは？

### Python のパッケージ管理システム

Python で作られたソフトウェアは **\*パッケージ** という形で配布されますが、これらのパッケージをインストール したりアップデートしたりアンインストールしたりするためのツールが pip です。

### \*パッケージとは

Python の機能を拡張するための追加モジュールやライブラリを指し、これらを用いることで様々な機能を手軽に利用することができます。

## pip を使うと何が便利？

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

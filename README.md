# dsc-TIMEdelete

[Releases](https://github.com/ryuya0124/dsc-TIMEdelete/releases)から利用環境に合うファイルをダウンロードしてください。
全OS版ともインストール不要のポータブル配布です。Windows／Ubuntu版はアーカイブを展開して実行し、アンインストール時は展開したフォルダを削除してください。macOS版は署名・公証済みDMGを開き、`dsc-TIMEdelete.command`をダブルクリックして起動します。macOS版の設定と既定出力は`~/Documents/dsc-TIMEdelete`に保存され、アンインストール時はDMGと必要に応じてこのフォルダを削除します。

| OS | 対応状況 |
| --- | --- |
| Windows 11 x64 | 対応（Windows Server 2025でビルド） |
| Ubuntu latest x64 | 対応 |
| macOS 26 Apple Silicon | 対応 |

## このツールについて
・Project DIVAで使われるdscファイルから  
　不要なタイムスタンプ行(TIME();)を削除するツールです。

・「TIME」から始まる行が2行以上連続で続いたときに
最も下のものだけを残して削除します。

## 使い方
・Script Editorでdscファイルを読み込みます。

・Script Editor上でテキストを全文コピーして、  
　PC内の適当な場所に.txt形式で保存しておきます。

・このテキストファイルの絶対パスをコピーしておきます。  

・このツールを起動し、テキストファイルへの絶対パスを入力します。  
　(初回起動時は最初に言語を設定します)

・処理が無事に終了するとこのツールがあるフォルダ内に  
　Output.txtというテキストファイルが生成されます。

・Output.txtを全文コピーして、Script Editorでペーストすることで、  
　不要なタイムスタンプを削除することができます。

コマンドラインから入力・出力ファイルと言語を指定することもできます。

```shell
dsc-TIMEdelete input.txt --output Output.txt --language ja
```

## 二次配布について
・ご自由にどうぞ。

## 制作者X(Twitter)
[@_ryuya_0124](https://twitter.com/_ryuya_0124)

## About this tool
This tool deletes unnecessary timestamp lines (TIME();) from dsc files used in Project DIVA.

When two or more lines starting with "TIME" are followed in succession,
only the bottom one is left and deleted.

## How to use  
Load a dsc file in the Script Editor.

Copy the entire text in the Script Editor and save it in .txt format  
in an appropriate location on your PC.

Copy the absolute path of the text file.

Start the tool and enter the absolute path to the text file.  
(The first time the tool is launched, the language is set first.)

When the process is successfully completed, a text file named "Output.txt"  
will be generated in current directory.

You can remove unnecessary timestamps by copying the Output.txt file  
in its entirety and pasting it in the Script Editor.

The input, output, and language can also be supplied on the command line:

```shell
dsc-TIMEdelete input.txt --output Output.txt --language en
```

## Build

Python 3.14 is used for release builds.

```shell
python -m pip install -r requirements-build.txt
python -m unittest discover -s tests -v
python -m PyInstaller --clean --noconfirm --console --onedir --add-data "lang.json:." --name dsc-TIMEdelete dsc-TIMEdelete.py
```

Pushing a version tag builds and publishes Windows, Ubuntu, and Apple Silicon macOS archives through GitHub Actions. The macOS DMG is signed with the Developer ID Application certificate managed by fastlane match, notarized by Apple, and stapled. The Windows job compiles the PyInstaller 6.22.3 bootloader locally and uses `onedir` packaging to reduce antivirus false-positive risk; it cannot guarantee that every antivirus engine will accept every build.

## Secondary distribution
Secondary distribution is permitted.

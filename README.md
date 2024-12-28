# dsc-TIMEdelete

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

## Secondary distribution
Secondary distribution is permitted.

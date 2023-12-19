import os

def main():
        # ファイルパスを入力
    while True:
        try:
            filepath = input('ファイルパスを入力してください：')
            filepath = filepath.strip('"')
            
            with open(filepath):
                break
        except FileNotFoundError:
            print('ファイルが見つかりませんでした。')
        except:
            print('ファイルパスに無効な文字が含まれています。')

    print('入力:',filepath)
    
    # ファイルを読み込む
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # 新規ファイルに操作後のテキストを書き込む
    with open('Output.txt', 'w') as f:
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('TIME'):
                if i+1 < len(lines) and lines[i+1].startswith('TIME'):
                    # 次の行がTIMEから始まる場合、次の次の行がTIMEから始まるか確認する
                    j = i+1
                    while j < len(lines) and lines[j].startswith('TIME'):
                        j += 1
                    i = j-2
                else:
                    # 次の行がTIMEから始まらない場合、そのまま書き込む
                    f.write(line)
            else:
                # TIMEから始まらない場合、そのまま書き込む
                f.write(line)
            i += 1

    print('処理が完了しました。')
    cd = os.getcwd()
    print('出力:',cd+'\Output.txt')
    
if __name__ == '__main__':
    main()
    input()

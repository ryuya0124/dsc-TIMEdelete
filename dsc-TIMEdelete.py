import os
import configparser
import json

def main():
    # 言語設定を取得
    config = configparser.ConfigParser()

    if not os.path.isfile('Settings.ini'):
        # 初回実行時に言語選択を尋ねる
        lang = input("Please select a language \n1.English(en) or 2.日本語(ja): ").lower()
        while lang not in ['1','2','en', 'ja']:
            print("\nInvalid input.")
            lang = input("1.English(en) or 2.日本語(ja): ").lower()
        if lang == "1":
            lang = "en"
        elif lang == "2":
            lang = "ja"
        
        
        # 言語設定を保存
        config['DEFAULT'] = {'language': lang}
        with open('Settings.ini', 'w') as f:
            config.write(f)
    else:
        # 言語設定を読み込む
        try:
            config.read('Settings.ini')
            lang = config.get('DEFAULT', 'language')
        except (configparser.Error, FileNotFoundError):
            print("Error: Failed to read the configuration file.")
            print("The program will now exit.")
            return


    # 言語リソースを取得
    try:
        with open('lang.json', 'r', encoding='utf-8') as f:
            lang_resources = json.load(f)[lang]
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: Failed to read the language resource file.")
        print("The program will now exit.")
        return

    # ファイルパスを入力
    while True:
        try:
            filepath = input(lang_resources['filepath'])
            filepath = filepath.strip('"')

            with open(filepath, 'r', encoding='utf-8') as f:
                break
        except FileNotFoundError:
            print(lang_resources['file_not_found'])
        except:
            print(lang_resources['invalid_characters'])

    # 入力文を出力
    print(lang_resources['input'].format(filepath))

    # ファイルを読み込む
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 新規ファイルに操作後のテキストを書き込む
    with open('Output.txt', 'w', encoding='utf-8') as f:
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

    # 処理が完了したことを出力
    print(lang_resources['completed'])

    # 出力ファイルパスを出力
    result_file_path = os.path.join(os.getcwd(), 'Output.txt')
    print(lang_resources['output'].format(result_file_path))

if __name__ == '__main__':
    main()
    input()

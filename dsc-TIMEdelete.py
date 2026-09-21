import argparse
import configparser
import json
import sys
from pathlib import Path


APP_DIR = Path(sys.executable).resolve().parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent
RESOURCE_DIR = Path(getattr(sys, '_MEIPASS', APP_DIR))
DATA_DIR = Path.home() / 'Documents' / 'dsc-TIMEdelete' if getattr(sys, 'frozen', False) and sys.platform == 'darwin' else APP_DIR


def collapse_consecutive_time_lines(lines):
    """Keep only the last line in each consecutive block beginning with TIME."""
    result = []
    pending_time_line = None

    for line in lines:
        if line.startswith('TIME'):
            pending_time_line = line
            continue

        if pending_time_line is not None:
            result.append(pending_time_line)
            pending_time_line = None
        result.append(line)

    if pending_time_line is not None:
        result.append(pending_time_line)

    return result


def select_language(settings_path, requested_language=None):
    config = configparser.ConfigParser()

    if requested_language:
        language = requested_language
    elif settings_path.is_file():
        try:
            config.read(settings_path, encoding='utf-8')
            language = config.get('DEFAULT', 'language')
        except (configparser.Error, OSError, UnicodeError, KeyError):
            print('Error: Failed to read the configuration file.')
            return None
    else:
        language = input('Please select a language \n1.English(en) or 2.日本語(ja): ').lower()
        while language not in {'1', '2', 'en', 'ja'}:
            print('\nInvalid input.')
            language = input('1.English(en) or 2.日本語(ja): ').lower()

    language = {'1': 'en', '2': 'ja'}.get(language, language)
    if language not in {'en', 'ja'}:
        print('Error: Unsupported language in the configuration file.')
        return None

    config['DEFAULT'] = {'language': language}
    try:
        with settings_path.open('w', encoding='utf-8') as settings_file:
            config.write(settings_file)
    except OSError:
        print(f'Warning: Could not save language settings to {settings_path}.')

    return language


def load_language_resources(language):
    try:
        with (RESOURCE_DIR / 'lang.json').open(encoding='utf-8') as resource_file:
            return json.load(resource_file)[language]
    except (json.JSONDecodeError, OSError, KeyError):
        print('Error: Failed to read the language resource file.')
        return None


def request_input_path(resources):
    while True:
        raw_path = input(resources['filepath']).strip().strip('"')
        input_path = Path(raw_path).expanduser()
        try:
            with input_path.open(encoding='utf-8'):
                return input_path
        except FileNotFoundError:
            print(resources['file_not_found'])
        except (OSError, UnicodeError):
            print(resources['invalid_characters'])


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description='Remove redundant consecutive TIME lines from a Project DIVA script export.'
    )
    parser.add_argument('input', nargs='?', type=Path, help='UTF-8 input text file')
    parser.add_argument('-o', '--output', type=Path, help='Output path (default: the platform data directory)')
    parser.add_argument('--language', choices=('en', 'ja'), help='Override and save the interface language')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f'Error: Failed to create the data directory: {error}')
        return 1

    language = select_language(DATA_DIR / 'Settings.ini', args.language)
    if language is None:
        return 1

    resources = load_language_resources(language)
    if resources is None:
        return 1

    input_path = args.input.expanduser() if args.input else request_input_path(resources)
    output_path = args.output.expanduser() if args.output else DATA_DIR / 'Output.txt'

    try:
        lines = input_path.read_text(encoding='utf-8').splitlines(keepends=True)
    except FileNotFoundError:
        print(resources['file_not_found'])
        return 1
    except (OSError, UnicodeError):
        print(resources['invalid_characters'])
        return 1

    print(resources['input'].format(input_path))
    try:
        output_path.write_text(''.join(collapse_consecutive_time_lines(lines)), encoding='utf-8')
    except OSError as error:
        print(f'Error: Failed to write output: {error}')
        return 1

    print(resources['completed'])
    print(resources['output'].format(output_path.resolve()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

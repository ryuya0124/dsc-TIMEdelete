import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / 'dsc-TIMEdelete.py'
SPEC = importlib.util.spec_from_file_location('dsc_timedelete', MODULE_PATH)
APP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(APP)


class CollapseTimeLinesTests(unittest.TestCase):
    def test_keeps_only_last_time_line_in_each_block(self):
        lines = [
            'TIME(100);\n',
            'TIME(200);\n',
            'BAR(1);\n',
            'TIME(300);\n',
            'TIME(400);\n',
            'TIME(500);\n',
        ]

        self.assertEqual(
            APP.collapse_consecutive_time_lines(lines),
            ['TIME(200);\n', 'BAR(1);\n', 'TIME(500);\n'],
        )

    def test_preserves_non_time_lines(self):
        lines = ['BAR(1);\n', 'TARGET(2);\n']
        self.assertEqual(APP.collapse_consecutive_time_lines(lines), lines)

    def test_preserves_single_time_line(self):
        lines = ['TIME(100);\n', 'BAR(1);\n']
        self.assertEqual(APP.collapse_consecutive_time_lines(lines), lines)


if __name__ == '__main__':
    unittest.main()

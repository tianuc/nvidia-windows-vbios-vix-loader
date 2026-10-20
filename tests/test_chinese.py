"""Chinese confirmations must remain complete before any firmware operation."""
import string
import tempfile
from pathlib import Path
import unittest

from nvidia_vbios.windows_loader.controller import STRINGS, Controller
from test_windows_loader import RTX_5070, platform, rom


class ChineseTests(unittest.TestCase):
    def test_every_string_has_matching_format_fields(self):
        def fields(text):
            return {field for _, field, _, _ in string.Formatter().parse(text) if field is not None}
        self.assertEqual(set(STRINGS['en']), set(STRINGS['zh_CN']))
        for key, text in STRINGS['en'].items():
            self.assertEqual(fields(text), fields(STRINGS['zh_CN'][key]), key)

    def test_chinese_confirmation_and_file_validation_never_write(self):
        fake, key = platform()
        c = Controller(fake, 'zh_CN')
        c.refresh()
        self.assertEqual(c.rows()[0][-1], '无覆盖')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '验证.rom'
            path.write_bytes(rom(RTX_5070))
            c.choose_file(str(path))
            question = c.confirm_load()
            for phrase in ('确认', '将此 VBIOS', '注册表', '设置', '损坏硬件'):
                if phrase == '确认':
                    self.assertIn(phrase, c.text['confirm_load_title'])
                else:
                    self.assertIn(phrase, question)
            self.assertEqual((key.calls, fake.writable_opens, fake.restarted), ([], 0, []))
            path.write_bytes(b'bad')
            c.choose_file(str(path))
            self.assertFalse(c.can_load())
            self.assertIn('文件未通过检查', c.validation_text()[1])


if __name__ == '__main__':
    unittest.main()

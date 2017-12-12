from regression_tests import *

base_settings = TestSettings(
    input='test.exe',
)

class TestNoInstructionInSelectedRange0x0To0x0(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x0-0x0'
    )

    def test_no_function_decompiled(self):
        assert self.out_c.func_count == 0

class TestNoInstructionInSelectedRange0x0To0x0DecodeOnly(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x0-0x0 --select-decode-only'
    )

    def setUp(self):
        pass

    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decomp.return_code, 0)
        assert self.decomp.log.contains(r'Error: No instructions were decoded')

class TestNoInstructionInSelectedRange0x1To0x1(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x1-0x1'
    )

    def test_no_function_decompiled(self):
        assert self.out_c.func_count == 0

class TestNoInstructionInSelectedRange0x1To0x1DecodeOnly(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x1-0x1 --select-decode-only'
    )

    def setUp(self):
        pass

    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decomp.return_code, 0)
        assert self.decomp.log.contains(r'Error: No instructions were decoded')

class TestInstructionInSelectedRange0x407741To0x4077411(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x407741-0x407741'
    )

    def test_one_function_decompiled(self):
        assert self.out_c.has_just_funcs('main')
        assert self.out_c.contains('Address range: 0x407740 - 0x40775d')
        assert self.out_c.has_string_literal('Hello world')
        main = self.out_c.funcs['main']
        assert main.calls('___main', 'puts')

class TestInstructionInSelectedRange0x407741To0x4077411DecodeOnly(Test):
    settings=CriticalTestSettings.from_settings(base_settings,
        args='--select-ranges 0x407741-0x407741 --select-decode-only'
    )

    def setUp(self):
        pass

    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decomp.return_code, 0)
        assert self.decomp.log.contains(r'Error: No instructions were decoded')

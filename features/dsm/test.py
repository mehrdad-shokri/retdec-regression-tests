from regression_tests import *

class TestElfWithoutSection(Test):
    settings=TestSettings(
        input='elf_without_sections'
    )

    def test_elf_without_sections_dsm(self):
        assert self.out_dsm.contains(r'; section: seg[0-9]{4}')

class TestFunctionThroughSections(Test):
    settings=TestSettings(
        input='ack.x86.gcc-4.7.2.O0.g.elf'
    )

    def test_one_function_is_not_through_several_sections(self):
        assert self.out_dsm.contains(r'; function: _init at 0x8048354 -- 0x8048380')
        assert self.out_dsm.contains(r'; function: function_8048390 at 0x8048390 -- 0x804839f')
        assert self.out_dsm.contains(r'; function: function_80483d0 at 0x80483d0 -- 0x80483df')
        assert self.out_dsm.contains(r'0x8048390:\s*ff 35 e0 98 04 08\s*push dword ptr \[0x80498e0\]')

        assert not self.out_dsm.contains(r'0x8048381:')
        assert not self.out_dsm.contains(r'; data inside code section at 0x8048390 -- 0x80483a0')
        assert not self.out_dsm.contains(r'0x8048390:\s*ff 35 e0 98 04 08 ff 25\s*e4 98 04 08 00 00 00 00')

    def test_functions_in_plt(self):
        assert self.out_dsm.contains(r'; function: function_8048390 at 0x8048390 -- 0x804839f')
        assert self.out_dsm.contains(r'; function: function_80483a0 at 0x80483a0 -- 0x80483af')
        assert self.out_dsm.contains(r'; function: function_80483b0 at 0x80483b0 -- 0x80483bf')
        assert self.out_dsm.contains(r'; function: function_80483c0 at 0x80483c0 -- 0x80483cf')
        assert self.out_dsm.contains(r'; function: function_80483d0 at 0x80483d0 -- 0x80483df')


class TestDsm(Test):
    settings=TestSettings(
        input='ackermann.x86.clang-3.2.O0.g.ex'
    )

    def test_defined_functions(self):
        assert self.out_dsm.contains(r'; function: ___mingw_invalidParameterHandler at 0x401000 -- 0x401001')
        assert self.out_dsm.contains(r'; function: _pre_cpp_init at 0x401010 -- 0x401052')
        assert self.out_dsm.contains(r'; function: _pre_c_init at 0x401060 -- 0x40117d')
        assert self.out_dsm.contains(r'; function: ___tmainCRTStartup at 0x401180 -- 0x4014bf')
        assert self.out_dsm.contains(r'; function: _WinMainCRTStartup at 0x4014c0 -- 0x4014d9')
        assert self.out_dsm.contains(r'; function: _mainCRTStartup at 0x4014e0 -- 0x4014f9')
        assert self.out_dsm.contains(r'; function: ___gcc_register_frame at 0x401500 -- 0x40154d')
        assert self.out_dsm.contains(r'; function: ___gcc_deregister_frame at 0x401550 -- 0x401554')
        assert self.out_dsm.contains(r'; function: _naive_ackermann at 0x401560 -- 0x4015f2') # 0x4015f0')
        assert self.out_dsm.contains(r'; function: _iterative_ackermann at 0x401600 -- 0x401661')
        assert self.out_dsm.contains(r'; function: _formula_ackermann at 0x401670 -- 0x40171f')
        assert self.out_dsm.contains(r'; function: main at 0x401720 -- 0x40184b')
        assert self.out_dsm.contains(r'; function: ___getmainargs at 0x407700 -- 0x40770.')
        assert self.out_dsm.contains(r'; function: ___set_app_type at 0x407708 -- 0x40770.')
        assert self.out_dsm.contains(r'; function: _memcpy at 0x407710 -- 0x40771.')
        assert self.out_dsm.contains(r'; function: _malloc at 0x407718 -- 0x40771.')
        assert self.out_dsm.contains(r'; function: _strlen at 0x407720 -- 0x40772.')
        assert self.out_dsm.contains(r'; function: __cexit at 0x407728 -- 0x40772.')
        assert self.out_dsm.contains(r'; function: __amsg_exit at 0x407730 -- 0x40773.')
        assert self.out_dsm.contains(r'; function: __initterm at 0x407738 -- 0x40773.')
        assert self.out_dsm.contains(r'; function: _exit at 0x407740 -- 0x40774.')
        assert self.out_dsm.contains(r'; function: _scanf at 0x407748 -- 0x40774.')
        assert self.out_dsm.contains(r'; function: _printf at 0x407750 -- 0x40775.')
        assert self.out_dsm.contains(r'; function: __lock at 0x407758 -- 0x40775.')
        assert self.out_dsm.contains(r'; function: ___dllonexit at 0x407760 -- 0x40776.')
        assert self.out_dsm.contains(r'; function: __unlock at 0x407768 -- 0x40776.')
        assert self.out_dsm.contains(r'; function: _signal at 0x407770 -- 0x40777.')
        assert self.out_dsm.contains(r'; function: ___setusermatherr at 0x407778 -- 0x40777.')
        assert self.out_dsm.contains(r'; function: _abort at 0x407780 -- 0x40778.')
        assert self.out_dsm.contains(r'; function: _strncmp at 0x407788 -- 0x40778.')
        assert self.out_dsm.contains(r'; function: _calloc at 0x407790 -- 0x40779.')
        assert self.out_dsm.contains(r'; function: _free at 0x407798 -- 0x40779.')
        assert self.out_dsm.contains(r'; function: _fputc at 0x4077a0 -- 0x4077a.')
        assert self.out_dsm.contains(r'; function: _localeconv at 0x4077a8 -- 0x4077a.')
        assert self.out_dsm.contains(r'; function: __errno at 0x4077b0 -- 0x4077b.')
        assert self.out_dsm.contains(r'; function: _getenv at 0x4077b8 -- 0x4077b.')
        assert self.out_dsm.contains(r'; function: _strerror at 0x4077c0 -- 0x4077c.')
        assert self.out_dsm.contains(r'; function: _wcslen at 0x4077c8 -- 0x4077c.')
        assert self.out_dsm.contains(r'; function: _setlocale at 0x4077d0 -- 0x4077d.')
        assert self.out_dsm.contains(r'; function: _strchr at 0x4077d8 -- 0x4077d.')
        assert self.out_dsm.contains(r'; function: _atoi at 0x4077e0 -- 0x4077e.')
        assert self.out_dsm.contains(r'; function: _register_frame_ctor at 0x407a40 -- 0x407a6.')
        assert self.out_dsm.contains(r'; function: __encode_pointer at 0x401950 -- 0x401954')

    def test_strings_in_code(self):
        assert self.out_dsm.contains(r'0x4012b7:.* ; "_set_invalid_parameter_handler"\n')
        assert self.out_dsm.contains(r'0x40150f:.* ; "libgcj-13.dll"\n')
        assert self.out_dsm.contains(r'0x401528:.* ; "_Jv_RegisterClasses"\n')
        assert self.out_dsm.contains(r'0x40174c:.* ; "%d %d"\n')
        assert self.out_dsm.contains(r'0x401799:.* ; "Naive:     %u \(%u calls\)\\n"\n')
        assert self.out_dsm.contains(r'0x4017da:.* ; "Iterative: %u \(%u calls\)\\n"\n')
        assert self.out_dsm.contains(r'0x40181b:.* ; "Formula:   %u \(%u calls\)\\n"\n')

    def test_strings_in_data(self):
        assert self.out_dsm.contains(r'0x408004:.* "%d %d"\n')
        assert self.out_dsm.contains(r'0x40800a:.* "Naive:     %u \(%u calls\)\\n"\n')
        assert self.out_dsm.contains(r'0x408024:.* "Iterative: %u \(%u calls\)\\n"\n')
        assert self.out_dsm.contains(r'0x40803e:.* "Formula:   %u \(%u calls\)\\n"\n')
        assert self.out_dsm.contains(r'0x409000:.* "_set_invalid_parameter_handler"\n')
        assert self.out_dsm.contains(r'0x409020:.*  "libgcj-13.dll"\n')
        assert self.out_dsm.contains(r'0x40902e:.* "_Jv_RegisterClasses"\n')

    def test_statically_linked_functions(self):
        assert self.out_dsm.contains(r'; statically linked function: ___dyn_tls_init@12 at 0x4018a0 -- 0x40191.')
        assert self.out_dsm.contains(r'; statically linked function: _mingw_onexit at 0x401960 -- 0x401a1.')
        assert self.out_dsm.contains(r'; statically linked function: _atexit at 0x401a20 -- 0x401a3.')
        assert self.out_dsm.contains(r'; statically linked function: __gnu_exception_handler@4 at 0x401a40 -- 0x401b9.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_raise_matherr at 0x401ba0 -- 0x401be.')
        assert self.out_dsm.contains(r'; statically linked function: __matherr at 0x401c00 -- 0x401c5.')
        assert self.out_dsm.contains(r'; statically linked function: __pei386_runtime_relocator at 0x401f10 -- 0x4021b.')
        assert self.out_dsm.contains(r'; statically linked function: __ValidateImageBase at 0x4021c0 -- 0x4021e.')
        assert self.out_dsm.contains(r'; statically linked function: __FindPESection at 0x4021f0 -- 0x40222.')
        assert self.out_dsm.contains(r'; statically linked function: __FindPESectionByName at 0x402230 -- 0x4022b.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_GetSectionForAddress at 0x4022c0 -- 0x4022f.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_GetSectionCount at 0x402300 -- 0x40232.')
        assert self.out_dsm.contains(r'; statically linked function: __FindPESectionExec at 0x402330 -- 0x40238.')
        assert self.out_dsm.contains(r'; statically linked function: __GetPEImageBase at 0x402390 -- 0x4023b.')
        assert self.out_dsm.contains(r'; statically linked function: __IsNonwritableInCurrentImage at 0x4023c0 -- 0x40240.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_enum_import_library_names at 0x402410 -- 0x40249.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_get_msvcrt_handle at 0x4024a0 -- 0x40255.')
        assert self.out_dsm.contains(r'; statically linked function: ___do_global_dtors at 0x402570 -- 0x40259.')
        assert self.out_dsm.contains(r'; statically linked function: ___do_global_ctors at 0x4025a0 -- 0x4025e.')
        assert self.out_dsm.contains(r'; statically linked function: ___main at 0x4025f0 -- 0x40260.')
        assert self.out_dsm.contains(r'; statically linked function: ___security_init_cookie at 0x402610 -- 0x4026d.')
        assert self.out_dsm.contains(r'; statically linked function: ___report_gsfailure at 0x4026e0 -- 0x40276.')
        assert self.out_dsm.contains(r'; statically linked function: ____w64_mingwthr_add_key_dtor at 0x4027e0 -- 0x40286.')
        assert self.out_dsm.contains(r'; statically linked function: ____w64_mingwthr_remove_key_dtor at 0x402870 -- 0x40290.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_TLScallback at 0x402910 -- 0x4029a.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_fprintf at 0x402a20 -- 0x402a5.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_vfprintf at 0x402a60 -- 0x402a9.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_pformat at 0x4040f0 -- 0x404a3.')
        assert self.out_dsm.contains(r'; statically linked function: ___gdtoa at 0x404a40 -- 0x406041')
        assert self.out_dsm.contains(r'; statically linked function: _wcrtomb at 0x4060f0 -- 0x40614.')
        assert self.out_dsm.contains(r'; statically linked function: _wcsrtombs at 0x406150 -- 0x40624.')
        assert self.out_dsm.contains(r'; statically linked function: _mbrtowc at 0x4063f0 -- 0x40646.')
        assert self.out_dsm.contains(r'; statically linked function: _mbsrtowcs at 0x406470 -- 0x40659.')
        assert self.out_dsm.contains(r'; statically linked function: _mbrlen at 0x4065a0 -- 0x4065f.')
        assert self.out_dsm.contains(r'; statically linked function: ___rv_alloc_D2A at 0x406600 -- 0x40663.')
        assert self.out_dsm.contains(r'; statically linked function: ___nrv_alloc_D2A at 0x406640 -- 0x40668.')
        assert self.out_dsm.contains(r'; statically linked function: ___freedtoa at 0x406690 -- 0x4066a.')
        assert self.out_dsm.contains(r'; statically linked function: ___quorem_D2A at 0x4066b0 -- 0x4068b.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_set_output_format at 0x4068c0 -- 0x40692.')
        assert self.out_dsm.contains(r'; statically linked function: ___mingw_get_output_format at 0x406930 -- 0x40698.')
        assert self.out_dsm.contains(r'; statically linked function: ___Balloc_D2A at 0x406ac0 -- 0x406b7.')
        assert self.out_dsm.contains(r'; statically linked function: ___Bfree_D2A at 0x406b80 -- 0x406bc.')
        assert self.out_dsm.contains(r'; statically linked function: ___multadd_D2A at 0x406bd0 -- 0x406cb.')
        assert self.out_dsm.contains(r'; statically linked function: ___i2b_D2A at 0x406cc0 -- 0x406ce.')
        assert self.out_dsm.contains(r'; statically linked function: ___mult_D2A at 0x406cf0 -- 0x406e4.')
        assert self.out_dsm.contains(r'; statically linked function: ___pow5mult_D2A at 0x406e50 -- 0x406f6.')
        assert self.out_dsm.contains(r'; statically linked function: ___lshift_D2A at 0x406f70 -- 0x40707.')
        assert self.out_dsm.contains(r'; statically linked function: ___cmp_D2A at 0x407080 -- 0x4070e.')
        assert self.out_dsm.contains(r'; statically linked function: ___diff_D2A at 0x4070f0 -- 0x40727.')
        assert self.out_dsm.contains(r'; statically linked function: ___b2d_D2A at 0x407280 -- 0x40737.')
        assert self.out_dsm.contains(r'; statically linked function: ___d2b_D2A at 0x407380 -- 0x40748.')
        assert self.out_dsm.contains(r'; statically linked function: ___strcp_D2A at 0x407490 -- 0x4074b0')
        assert self.out_dsm.contains(r'; statically linked function: ___rshift_D2A at 0x4074c0 -- 0x4075c.')
        assert self.out_dsm.contains(r'; statically linked function: ___trailz_D2A at 0x4075d0 -- 0x40760.')
        assert self.out_dsm.contains(r'; statically linked function: _?__umoddi3 at 0x4077f0 -- 0x40792.')
        assert self.out_dsm.contains(r'; statically linked function: _?__udivdi3 at 0x407930 -- 0x407a3.')
        assert self.out_dsm.contains(r'; statically linked function: __InterlockedCompareExchange at 0x4029e0 -- 0x4029f2')
        assert self.out_dsm.contains(r'; statically linked function: _InterlockedCompareExchange@12 at 0x402a00 -- 0x402a12')

    def test_data_inside_code(self):
        assert self.out_dsm.contains(r'; data inside code section at 0x4029f3 -- 0x4029ff')
        assert self.out_dsm.contains(r'; data inside code section at 0x402bf4 -- 0x402bff')
        assert self.out_dsm.contains(r'; data inside code section at 0x4034ea -- 0x4034ef')

    def test_sections(self):
        assert self.out_dsm.contains(r'; section: .text')
        assert self.out_dsm.contains(r'; section: .data')
        assert self.out_dsm.contains(r'; section: .rdata')
        assert self.out_dsm.contains(r'; section: .idata')
        assert self.out_dsm.contains(r'; section: .CRT')
        assert self.out_dsm.contains(r'; section: .tls')

    def test_some_random_data(self):
        assert self.out_dsm.contains(r'0x402a61:   ec 2c 8b 44 24 38 c7 44  24 08 00 00 00 00 c7 04   |.,.D$8.D$.......|')
        assert self.out_dsm.contains(r'0x406990:   56 89 c6 53 83 ec 14 8b  15 40 ad 40 00 83 fa 02   |V..S.....@.@....|')
        assert self.out_dsm.contains(r'0x407931:   ec 2c 8b 54 24 3c 89 7c  24 24 8b 4c 24 38 8b 7c   |.,.T$<.|$$.L$8.||')
        assert self.out_dsm.contains(r'0x408068:   02 00 00 00 ff ff ff ff  40 00 00 00 c3 bf ff ff   |........@.......|')
        assert self.out_dsm.contains(r'0x408098:   4e e6 40 bb b1 19 bf 44  00 00 00 00               |N.@....D....    |')
        assert self.out_dsm.contains(r'0x409362:   40 00 90 46 40 00 04 42  40 00 68 46 40 00 44 46   |@..F@..B@.hF@.DF|')
        assert self.out_dsm.contains(r'0x409642:   00 00                                              |..              |')
        assert self.out_dsm.contains(r'0x40b000:   3c b0 00 00 00 00 00 00  00 00 00 00 30 b6 00 00   |<...........0...|')
        assert self.out_dsm.contains(r'0x40b1a0:   3a b4 00 00 48 b4 00 00  58 b4 00 00 64 b4 00 00   |:...H...X...d...|')
        assert self.out_dsm.contains(r'0x40b6d0:   6d 73 76 63 72 74 2e 64  6c 6c 00 00               |msvcrt.dll..    |')
        assert self.out_dsm.contains(r'0x40c000:   00 00 00 00 10 10 40 00  00 00 00 00 00 00 00 00   |......@.........|')
        assert self.out_dsm.contains(r'0x40c030:   00 00 00 00                                        |....            |')
        assert self.out_dsm.contains(r'0x40d000:   19 d0 40 00 1c d0 40 00  38 a0 40 00 20 c0 40 00   |..@...@.8.@. .@.|')

    def test_function_addresses_in_instructions(self):
        assert self.out_dsm.contains(r'0x4015d2:.*call 0x401560 <_naive_ackermann>')
        assert self.out_dsm.contains(r'0x4012a4:.*call dword ptr \[0x40b17c\] <SetUnhandledExceptionFilter>')
        assert self.out_dsm.contains(r'0x401483:.*call dword ptr \[0x40b158\] <GetStartupInfoA>')
        assert self.out_dsm.contains(r'0x407710:.*jmp dword ptr \[0x40b1e8\] <memcpy>')
        assert self.out_dsm.contains(r'0x407740:.*jmp dword ptr \[0x40b21c\] <exit>')
        assert self.out_dsm.contains(r'0x407770:.*jmp dword ptr \[0x40b1f8\] <signal>')
        assert self.out_dsm.contains(r'0x4077a8:.*jmp dword ptr \[0x40b1e0\] <localeconv>')
        assert self.out_dsm.contains(r'0x4077e0:.*jmp dword ptr \[0x40b214\] <atoi>')

    def test_function_offsets_in_instructions(self):
        assert self.out_dsm.contains(r'0x401096:.*je 0x401100 <_pre_c_init\+0xa0>')
        assert self.out_dsm.contains(r'0x4011e8:.*jne 0x401480 <___tmainCRTStartup\+0x300>')
        assert self.out_dsm.contains(r'0x40147b:.*jmp 0x401268 <___tmainCRTStartup\+0xe8>')
        assert self.out_dsm.contains(r'0x401623:.*je 0x401657 <_iterative_ackermann\+0x57>')
        assert self.out_dsm.contains(r'0x401713:.*jmp 0x40168f <_formula_ackermann\+0x1f>')

    def test_bug_1619(self):
        assert self.out_dsm.contains(r'0x401096:.*je 0x401100')
        assert self.out_dsm.contains(r'0x4011e8:.*jne 0x401480')
        assert self.out_dsm.contains(r'0x40147b:.*jmp 0x401268')
        assert self.out_dsm.contains(r'0x401623:.*je 0x401657')
        assert self.out_dsm.contains(r'0x401713:.*jmp 0x40168f')

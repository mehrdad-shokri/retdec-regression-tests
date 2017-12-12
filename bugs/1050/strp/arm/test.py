from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='strp-strip',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( ' Copyright(c) 1996, 1998 by ' )
		assert self.out_c.has_string_literal( '%s%s%s%s' )
		assert self.out_c.has_string_literal( '0.9' )
		assert self.out_c.has_string_literal( 'Eddie Buckley <eddie@sjfn.nb.ca>\\n' )
		assert self.out_c.has_string_literal( 'Fix line breaks in FILE(s), or standard input to standard output.' )
		assert self.out_c.has_string_literal( "Try `%s -h' for more information.\\n" )
		assert self.out_c.has_string_literal( 'Usage: %s [OPTION] [FILE]...\\n' )
		assert self.out_c.has_string_literal( '\\nIf more than one command line option is present only the first one is used.' )
		assert self.out_c.has_string_literal( '\\nWith no FILE or when FILE is - read from standard input and write to standard\\n output.\\n' )
		assert self.out_c.has_string_literal( '\\n\\t-d\\tmake DOS format (CR-LF)' )
		assert self.out_c.has_string_literal( '\\t-h\\tshow this help and version number' )
		assert self.out_c.has_string_literal( '\\t-m\\tmake MAC/Amiga format (CR)' )
		assert self.out_c.has_string_literal( '\\t-u\\tmake UNIX format (LF)' )
		assert self.out_c.has_string_literal( '\\t-v\\tprint version number and exit' )
		assert self.out_c.has_string_literal( 'strp version ' )
		assert self.out_c.has_string_literal( 'usage %s %s\\n' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_8000' )  # _init
		assert self.out_c.has_func( 'function_80b0' )  # frame_dummy
		assert self.out_c.has_func( 'entry_point' )  # entry_point
		assert self.out_c.has_func( 'function_8354' )  # help
		assert self.out_c.has_func( 'function_83bc' )  # ver
		assert self.out_c.has_func( 'function_84f4' )  # usage
		assert self.out_c.has_func( 'function_8524' )  # try
		assert self.out_c.has_func( 'main' )  # main
		assert self.out_c.has_func( 'function_9430' )  # rindex
		assert self.out_c.has_func( 'function_11b98' )  # __do_global_ctors_aux

	# Functions reported in #1050 as not detected.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_80b0' )  # call___do_global_dtors_aux
		#assert self.out_c.has_func( 'function_8218' )  # to_unix
		assert self.out_c.has_func( 'function_8280' )  # to_dos
		assert self.out_c.has_func( 'function_82fc' )  # to_mac
		#assert self.out_c.has_func( 'function_83fc' )  # arg_parse
		#assert self.out_c.has_func( 'function_84c8' )  # isdir

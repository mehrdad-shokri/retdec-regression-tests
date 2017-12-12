from regression_tests import *

class bin_1(Test):

	settings = TestSettings(
		input='1-init_bin-bd92ce74.unpacked.elf',
		args='--backend-no-opts'
	)

	def test_for_some_random_imported_functions(self):
		assert self.out_c.has_comment_matching(r'.*int32_t.*\*\*.*__ctype_toupper_loc\(.*')
		assert self.out_c.has_comment_matching(r'.*int __xstat\(.*')
		assert self.out_c.has_comment_matching(r'.*int munmap\(.*')
		assert self.out_c.has_comment_matching(r'.*long.*ptrace\(.*')
		assert self.out_c.has_comment_matching(r'.*char.*\*.*strcat\(.*')
		assert self.out_c.has_comment_matching(r'.*pid_t waitpid\(.*')

class bin_2(Test):

	settings = TestSettings(
		input='2-backdoor-2acf2bc7.so.elf'
	)

	def test_for_some_random_imported_functions(self):
		assert self.out_c.has_comment_matching(r'.*int32_t.*\*\*.*__ctype_toupper_loc\(.*')
		assert self.out_c.has_comment_matching(r'.*size_t fread\(.*')
		assert self.out_c.has_comment_matching(r'.*int mkdir\(.*')
		assert self.out_c.has_comment_matching(r'.*FILE \* popen\(.*')
		assert self.out_c.has_comment_matching(r'.*long.*strtoul\(.*')
		assert self.out_c.has_comment_matching(r'.*pid_t waitpid\(.*')

class bin_3(Test):

	settings = TestSettings(
		input='3-backdoor-753dc7cd.unpacked.elf',
		args='--backend-no-opts'
	)

	def test_check_for_strings(self):
		assert self.out_c.has_string_literal( '~`!@#$%^&*()_+{}|[]\\\\;:\'\\"<>,./?' )
		assert self.out_c.has_string_literal( '/proc/sys/kernel/random/boot_id' )
		assert self.out_c.has_string_literal( 'Rule: .*' )
		assert self.out_c.has_string_literal( '%s/.config' )
		assert self.out_c.has_string_literal( '%s/%s' )
		assert self.out_c.has_string_literal( '%s/%s.%s.config' )
		assert self.out_c.has_string_literal( '%s/.kde' )
		assert self.out_c.has_string_literal( '/proc/self/cmdline' )
		assert self.out_c.has_string_literal( '%s/autostart' )
		assert self.out_c.has_string_literal( '%s/%s%s.desktop' )
		assert self.out_c.has_string_literal( '%s/Autostart' )
		assert self.out_c.has_string_literal( 'killall unix-daemon' )

	def test_for_some_random_imported_functions(self):
		assert self.out_c.has_comment_matching(r'.*int __xstat\(.*')
		assert self.out_c.has_comment_matching(r'.*int.*connect\(.*')
		assert self.out_c.has_comment_matching(r'.*void.*\*.*memcpy\(.*')
		assert self.out_c.has_comment_matching(r'.*void pthread_exit\(.*')
		assert self.out_c.has_comment_matching(r'.*sig.*signal\(.*')
		assert self.out_c.has_comment_matching(r'.*int uname\(.*')

class bin_4(Test):

	settings = TestSettings(
		input='4-form_grabber-b794ce9e.so.elf'
	)

	def test_for_some_random_imported_functions(self):
		assert self.out_c.has_comment_matching(r'.*int32_t.*\*\*.*__ctype_toupper_loc\(.*')
		assert self.out_c.has_comment_matching(r'.*void.*\*.*dlsym\(.*')
		assert self.out_c.has_comment_matching(r'.*int ftruncate\(.*')
		assert self.out_c.has_comment_matching(r'.*void.*\*.*mmap\(.*')
		assert self.out_c.has_comment_matching(r'.*int pthread_mutex_unlock\(.*')
		assert self.out_c.has_comment_matching(r'.*long.*sysconf\(.*')

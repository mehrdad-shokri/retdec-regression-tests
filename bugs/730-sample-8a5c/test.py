#
# Tests sample 8A5CCB7A5695E3B4FEBCF098DBDB496E from #730.
# Tests mainly detection of strings and functions called by syscall.
#

from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='8A5C',
		args='-k'
	)

	# These are not all strings recognized in output, just some important/random.
	#
	def test_check_for_strings(self):
		assert self.out_c.has_string_literal('telnetd')
		assert self.out_c.has_string_literal('insmod /lib/modules/`uname -r`/kernel/net/ipv4/netfilter/ip_tables.ko')
		assert self.out_c.has_string_literal('/var/run/gcc')
		assert self.out_c.has_string_literal('nodes')
		assert self.out_c.has_string_literal('rm -rf ')
		#assert self.out_c.has_string_literal('httpd')
		assert self.out_c.has_string_literal('/bin/sh')
		assert self.out_c.has_string_literal('iptables -D INPUT -p tcp --dport 23 -j DROP')
		assert self.out_c.has_string_literal('/var/run/z')
		assert self.out_c.has_string_literal('insmod /lib/modules/`uname -r`/kernel/net/ipv4/netfilter/ip_tables.ko')
		assert self.out_c.has_string_literal('echo -n > ')

	# Syscalled functions are added as linked and should be dumpped as comments in "External Functions" section.
	# Note: these are not all detected external functions.
	#
	def test_external_fncs_from_syscalls(self):
		assert self.out_c.has_comment_matching(r'.*accept\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*bind\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*connect\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*execve\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*fstat\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*listen\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*pipe\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*sendto\(.*\);') or self.out_c.has_comment_matching(r'.*ssize_t.*sendto\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int.*unlink\(.*\);')
		assert self.out_c.has_comment_matching(r'.*ssize_t.*write\(.*\);')

	# Right now, we can not check if function X calls function Y, so we just check presence of functions calling syscalls.
	# All of these are in Hex-Rays as well.
	#
	def test_has_functions_using_syscalls(self):
		assert self.out_c.has_func( 'function_aff4' ) # accept()
		assert self.out_c.has_func( 'function_a2f4' ) # bind()
		assert self.out_c.has_func( 'function_b360' ) # connect()
		assert self.out_c.has_func( 'function_876c' ) # execve(), NOT in Hex-Rays.
		assert self.out_c.has_func( 'function_a374' ) # fstat()
		assert self.out_c.has_func( 'function_a35c' ) # listen()
		assert self.out_c.has_func( 'function_9c58' ) # pipe()
		assert self.out_c.has_func( 'function_bf68' ) # sendto()
		assert self.out_c.has_func( 'function_8a28' ) # unlink()
		assert self.out_c.has_func( 'function_15ff4' ) # write()

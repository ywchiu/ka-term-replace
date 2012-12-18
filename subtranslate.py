## -*- coding: utf8 -*-
import codecs
import sys
import os


def term_translate(src_dir, trg_dir, term_base):
	for dirname, dirnames, filenames in os.walk('subtitle/'):
		for filename in filenames:
			fName =  os.path.join(dirname, filename)
	
			fp = open(fName, 'r')
			original_content = fp.read().decode('utf-8')
			fp.close()

			termbase = open(term_base, 'r')

			for rec in termbase.readlines():
				line = rec.split('\n')
				ele = line[0].split('\t')
				if len(ele[0].decode('utf-8')) > 1:
					original_content = original_content.replace(ele[1].decode('utf-8'),ele[0].decode('utf-8'))

			fp = open('%s'%(trg_dir + filename), 'w')
			fp.write(original_content.encode('utf-8'))
			fp.close()

term_translate('subtitle/', 'tc_subtitle/', 'termtab_tc.txt')

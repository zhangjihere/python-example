#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cStringIO

small_emps=[
	["Maray", "Jane"],
	["jenny", "doe"],
	["Alice","johnson"]
	]

big_emps=small_emps[::]
for i in xrange(6):
  big_emps += big_emps

print '#'*15
print 'Employee List Sizes:'
print 'tsmall_emps size=%i'%(len(small_emps))
print 'tbig_emps size=%i\n'%(len(big_emps))

def accumulate_str(employees):
  emp_table='<table>\n'
  for l_name, f_name in employees:
    emp_table+='\t<tr><td>%s, %s</td></tr>\n' % (l_name, f_name)
  emp_table+='</table>'
  return emp_table

def accumulate_list(employees):
  items=['<table>\n']
  for l_name, f_name in employees:
    items.append('\t<tr><td>%s, %s</td></tr>\n'%(l_name, f_name))
  items.append('</table>')
  emp_table= ''.join(items)
  return emp_table

def accumulate_cStringIO(employees):
  emp_table=cStringIO.StringIO()
  emp_table.write('<table>\n')
  for l_name, f_name in employees:
    emp_table.write('\t<tr><td>%s, %s</td></tr>\n'%(l_name, f_name))
  emp_table.write('</table>')
  emp_table_s=emp_table.getvalue()
  emp_table.close()
  return emp_table_s

if __name__ == '__main__':
    import timeit
    print '#'*15
    print 'Small employee_list test...'
    print 'tDefault String Accumulation'
    t = timeit.Timer("accumulate_str(small_emps)",
            "from __main__ import accumulate_str, small_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)

    print "tDefault List Accumulation"
    t = timeit.Timer("accumulate_list(small_emps)",
            "from __main__ import accumulate_list, small_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)

    print "tCStringIO Accumulation"
    t = timeit.Timer("accumulate_cStringIO(small_emps)",
            "from __main__ import accumulate_cStringIO, small_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)

    ##########################
    # BIG EMPLOYEE LIST TEST #
    ##########################
    print '#'*15
    print 'Big employee_list test...'
    print "tDefault String Accumulation"
    t = timeit.Timer("accumulate_str(big_emps)",
            "from __main__ import accumulate_str, big_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)

    print "tDefault List Accumulation"
    t = timeit.Timer("accumulate_list(big_emps)",
            "from __main__ import accumulate_list, big_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)

    print "tCStringIO Accumulation"
    t = timeit.Timer("accumulate_cStringIO(big_emps)",
            "from __main__ import accumulate_cStringIO, big_emps")
    print "tElapsed time: %0.5s\n"%t.timeit(number=50000)














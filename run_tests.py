# coding=utf-8

from builtins import chr
import collections
from functools import reduce
import importlib
import timeit

SOLUTION_NAMES = [
    'dan',
    'matt',
    'hailey_speed',
    'hailey_readability',
    'hailey_functional',
    'ben',
    'ben_itertools',
    'matt_codegolf',
    'hailey_codegolf',
    'ben_codegolf',
    'ben_codegolf_one_statement',
]

solutions = [importlib.import_module(name) for name in SOLUTION_NAMES]


def unicode_range(startOrd, endOrd):
  """Returns a string consisting of the Unicode characters with codepoint
  ranging from `startOrd` to `endOrd`."""
  return u''.join(chr(i) for i in range(startOrd, endOrd))


def truncate_at(s, max_length):
  return s if len(s) <= max_length else '{}...'.format(s[:max_length])


# Default number of trials to run when timing a test case with `timeit`.  If
# your test case is big, you'll probably want to set `TestCase.num_trials` to
# something smaller.
DEFAULT_NUM_TRIALS = int(1e4)


def make_test_case(*args, **kwargs):
  """Factory function that emulates default arguments for `namedtuple`s
  (exists natively in Python 3.7)."""
  if len(args) < 4 and 'num_trials' not in kwargs:
    kwargs = dict(kwargs, num_trials=DEFAULT_NUM_TRIALS)
  return TestCase(*args, **kwargs)


TestCase = collections.namedtuple(
    'TestCase', ['name', 'inpt', 'expected_out', 'num_trials'])


TEST_CASES = [
    make_test_case('Sorted with some chars not in p',
                   inpt=('google', 'ole'), expected_out=True),
    make_test_case('Order violation only on repeated char',
                   inpt=('google', 'gol'), expected_out=False),
    make_test_case('everything is sorted wrt empty',
                   inpt=('google', ''), expected_out=True),
    make_test_case('empty is sorted wrt anything',
                   inpt=('', 'google'), expected_out=True),
    # Thanks Hailey for making these test cases.  Unfortunately I didn't have
    # time to give them meaningful names.
    make_test_case('TODO: let\'s go shopping',
                   inpt=('hailey', 'sale'), expected_out=True),
    make_test_case('TODO: name this test #1',
                   inpt=('a', 'a'), expected_out=True),
    make_test_case('TODO: name this test #2',
                   inpt=('a', 'b'), expected_out=True),
    make_test_case('TODO: name this test #3',
                   inpt=('ab', 'ab'), expected_out=True),
    make_test_case('TODO: name this test #4',
                   inpt=('ab', 'ba'), expected_out=False),
    make_test_case('TODO: name this test #5',
                   inpt=('ab', 'abc'), expected_out=True),
    make_test_case('TODO: name this test #6',
                   inpt=('ab', 'cab'), expected_out=True),
    make_test_case('TODO: name this test #7',
                   inpt=('ab', 'cba'), expected_out=False),
    make_test_case('TODO: name this test #8',
                   inpt=('abc', 'ab'), expected_out=True),
    make_test_case('TODO: name this test #9',
                   inpt=('abc', 'ba'), expected_out=False),
    make_test_case('TODO: name this test #10',
                   inpt=('cab', 'ab'), expected_out=True),
    make_test_case('TODO: name this test #11',
                   inpt=('cab', 'ba'), expected_out=False),
    make_test_case('TODO: name this test #12',
                   inpt=('abc', 'ab'), expected_out=True),
    make_test_case('TODO: name this test #13',
                   inpt=('hinson', 'hailey'), expected_out=True),
    make_test_case('TODO: name this test #14',
                   inpt=('matt', 'york'), expected_out=True),
    make_test_case('TODO: name this test #15',
                   inpt=('ben zinberg', 'ben'), expected_out=False),
    make_test_case('TODO: name this test #16',
                   inpt=('This is a sentence.', 'ha'), expected_out=True),
    make_test_case('TODO: name this test #18',
                   inpt=('This is a sentence.', '1234'), expected_out=True),
    make_test_case('TODO: name this test #19',
                   inpt=('This is a sentence.', 'sé'), expected_out=True),
    make_test_case('TODO: name this test #20',
                   inpt=('This is a sentence.', 'se'), expected_out=True),
    make_test_case('TODO: name this test #21',
                   inpt=('This is a sentence.', 'te'), expected_out=False),
    make_test_case('TODO: name this test #22',
                   inpt=('allécher quelqu\'un', 'seq'), expected_out=False),
    make_test_case('TODO: name this test #23',
                   inpt=('allécher quelqu\'un', 'sé'), expected_out=True),
    make_test_case('TODO: name this test #24',
                   inpt=('abcde', 'bc]d'), expected_out=True),
    make_test_case('TODO: name this test #25',
                   inpt=('abcd(e', 'bc(d'), expected_out=False),
    make_test_case('TODO: name this test #26',
                   inpt=('abcd\\e', 'bc\\de'), expected_out=False),
] + reduce(lambda x, y: x+y, ([
    make_test_case('Time trial, sorted, |s| = |p| = {}'.format(big),
                   inpt=(unicode_range(0, big),
                         unicode_range(0, big)),
                   expected_out=True,
                   num_trials=1),
    make_test_case(('Time trial, order violation in the middle,'
                    ' |s| = |p| = {}').format(big),
                   inpt=(u'\u0000'.join([unicode_range(0, big // 2),
                                         unicode_range(big // 2, big)]),
                         unicode_range(0, big)),
                   expected_out=False,
                   num_trials=1),
] for big in (
    10,
    100,
    int(1e3),
    int(1e4),
    int(1e5),
    int(1e6),
)))


def run_tests(module, time_trial=True, verbose=False):
  print('====== Testing {} ======'.format(module.__name__))
  failures = []
  if time_trial:
    times = []
  for (i, test_case) in enumerate(TEST_CASES):
    actual_out = module.is_sorted_wrt(*test_case.inpt)
    if time_trial:
      time_secs = timeit.timeit(
          '{module}.is_sorted_wrt(*TEST_CASES[{i}].inpt)'.format(
              module=module.__name__, i=i),
          setup='from __main__ import TEST_CASES; import {}'.format(
              ', '.join(module.__name__ for module in solutions)),
          number=test_case.num_trials)
      times.append(time_secs)
      time_info = '{:.05f}sec '.format(time_secs)
    else:
      time_info = ''

    passed = (actual_out == test_case.expected_out)
    if not passed:
      print(('{time_info}[FAILED] {t.name}\n  s={t.inpt[0]}\n  p={t.inpt[1]}'
             '\n  expected={t.expected_out}\n  actual={actual}').format(
          t=test_case,
          time_info=time_info,
          s=truncate_at(test_case.inpt[0], 20),
          p=truncate_at(test_case.inpt[1], 20),
          actual=actual_out))
      failures.append(i)
    elif verbose:
      print('{time_info}[PASSED] {t.name}'.format(t=test_case,
                                                  time_info=time_info))

  if len(failures) == 0:
    print('All tests passed!')
  else:
    print('{} tests failed.'.format(len(failures)))
  if time_trial:
    print('Total time: {:.05f} sec'.format(sum(times)))


if __name__ == '__main__':
  for module in solutions:
    run_tests(module, time_trial=True, verbose=True)

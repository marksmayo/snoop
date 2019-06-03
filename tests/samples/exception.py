import snoop


def foo():
    raise TypeError('''
    very
    bad''')


def bar():
    try:
        str(foo())
    except Exception:
        str(1)
        raise


@snoop(depth=3)
def main():
    try:
        bar()
    except:
        pass


if __name__ == '__main__':
    main()


expected_output = r"""
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 19
12:34:56.78   19 | def main():
12:34:56.78   20 |     try:
12:34:56.78   21 |         bar()
    12:34:56.78 >>> Call to bar in File "/path/to_file.py", line 10
    12:34:56.78   10 | def bar():
    12:34:56.78   11 |     try:
    12:34:56.78   12 |         str(foo())
        12:34:56.78 >>> Call to foo in File "/path/to_file.py", line 4
        12:34:56.78    4 | def foo():
        12:34:56.78    5 |     raise TypeError('''
        12:34:56.78    7 |     bad''')
        12:34:56.78 !!! TypeError: 
        12:34:56.78 !!!     very
        12:34:56.78 !!!     bad
        12:34:56.78 !!! Call ended by exception
    12:34:56.78   12 |         str(foo())
    12:34:56.78 !!! TypeError: 
    12:34:56.78 !!!     very
    12:34:56.78 !!!     bad
    12:34:56.78 !!! When evaluating: foo()
    12:34:56.78   13 |     except Exception:
    12:34:56.78   14 |         str(1)
    12:34:56.78   15 |         raise
    12:34:56.78 !!! Call ended by exception
12:34:56.78   21 |         bar()
12:34:56.78 !!! TypeError: 
12:34:56.78 !!!     very
12:34:56.78 !!!     bad
12:34:56.78   22 |     except:
12:34:56.78   23 |         pass
12:34:56.78 <<< Return value from main: None
"""

import lab5q6
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('5\nKualaLumpur\nMalaysia\n[3.0, -2, \'C\']\n0.5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab5q6.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'[5.0, \'KualaLumpur\', \'Malaysia\', [3.0, -2, \'C\'], 0.5]') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab5q6.py") as tf:
    head = [next(tf) for _ in range(24)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab5q6.py") as tf:
    head = [next(tf) for _ in range(24)]
    s = tf.read()
    assert(s.find("my_list") != -1 )

def test_case4(monkeypatch, capsys):
    number_inputs = StringIO('5\nKualaLumpur\nMalaysia\n[3.0, -2, \'C\']\n0.5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab5q6.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'[5.0, \'KualaLumpur\', \'Malaysia\', [3.0, -2, \'C\']]') != -1
    assert captured_stdout.strip().find(f'[5.0, \'KualaLumpur\', [3.0, -2, \'C\']]') != -1
    assert captured_stdout.strip().find(f'[\'KualaLumpur\', [3.0, -2, \'C\']]') != -1




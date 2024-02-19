import lab6q4
from io import StringIO
from sys import stderr

def generate_value(a=0, b=0):
  if a == 1 and b == 100:
    return 5
  else:
    return 6

def test_matching(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("10\n5\n6\n7\n8\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab6q4.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'1') != -1

def test_matching2(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("10\n10\n6\n7\n8\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab6q4.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'2') != -1



def test_case2(monkeypatch, capsys):
  with open(f"lab6q4.py") as tf:
    head = [next(tf) for _ in range(13)]
    s = tf.read()
    assert(s.find("for") != -1 )


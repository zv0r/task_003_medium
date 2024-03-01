from subprocess import run, PIPE
import os
import shutil
import pytest
import filecmp

B_FILE_PATH = './bin/simple_db'
DB_FILE_NAME = './database.txt'

def test_bin_folder_contains_simple_db():
    assert os.path.isfile(B_FILE_PATH)

def test_simple_db_not_correct_input_1():
    result = run([B_FILE_PATH], input='WRONG', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_2():
    result = run([B_FILE_PATH], input='exit', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_3():
    result = run([B_FILE_PATH], input='show', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_4():
    result = run([B_FILE_PATH], input='add', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_5():
    result = run([B_FILE_PATH], input='Add Something 444', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_exit_1():
    assert not os.path.isfile(DB_FILE_NAME)
    result = run([B_FILE_PATH], input='EXIT', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert os.path.getsize(DB_FILE_NAME) == 0
    assert result.stdout == ''

def test_simple_db_show_1():
    shutil.copy('./tests/data/simple_db_show_1.txt', DB_FILE_NAME)
    result = run([B_FILE_PATH], input='SHOW', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert os.path.getsize(DB_FILE_NAME) == 0
    assert result.stdout == ''

def test_simple_db_show_2():
    shutil.copy('./tests/data/simple_db_show_2.txt', DB_FILE_NAME)
    result = run([B_FILE_PATH], input='SHOW', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    with open(DB_FILE_NAME) as f:
        assert result.stdout == f.read()

def test_simple_db_add_1():
    SRC_DB_FILE_NAME = './tests/data/simple_db_show_2.txt'
    shutil.copy(SRC_DB_FILE_NAME, DB_FILE_NAME)
    result = run([B_FILE_PATH], input='ADD Water 123', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert not filecmp.cmp(SRC_DB_FILE_NAME, DB_FILE_NAME, shallow=False)

if __name__ == "__main__":
    pytest.main()

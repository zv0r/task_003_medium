from subprocess import run, PIPE
import os
import shutil
import pytest

B_FILE_PATH = './bin/not_simple_db'
DB_FILE_NAME = './database.txt'

def test_bin_folder_contains_not_simple_db():
    assert os.path.isfile(B_FILE_PATH)

def test_not_simple_db_not_correct_input_1():
    result = run([B_FILE_PATH], input='WRONG', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_not_simple_db_not_correct_input_2():
    result = run([B_FILE_PATH], input='max', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_not_simple_db_show_1():
    shutil.copy('./tests/data/not_simple_db.txt', DB_FILE_NAME)
    result = run([B_FILE_PATH], input='MAX', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert result.stdout == 'Whiskey 13500'

def test_not_simple_db_show_2():
    shutil.copy('./tests/data/simple_db_show_1.txt', DB_FILE_NAME)
    result = run([B_FILE_PATH], input='MAX', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert result.stdout == 'NO DATA'

if __name__ == "__main__":
    pytest.main()

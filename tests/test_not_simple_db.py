from subprocess import run, PIPE
import os
import shutil
import pytest

B_FILE_NAME = './not_simple_db'
B_FILE_DIR = './bin'
B_FILE_FULL_PATH = os.path.join(B_FILE_DIR, B_FILE_NAME)
DB_FILE_NAME = './data/database.txt'

if os.path.isfile(B_FILE_FULL_PATH):
    def test_bin_folder_contains_not_simple_db():
        assert os.path.isfile(B_FILE_FULL_PATH)

    def test_not_simple_db_not_correct_input_1():
        result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='WRONG', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_not_simple_db_not_correct_input_2():
        result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='max', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_not_simple_db_show_1():
        shutil.copy('./tests/data/not_simple_db.txt', './data/not_simple_db.txt')
        result = run([B_FILE_NAME, '../data/not_simple_db.txt'], cwd=B_FILE_DIR, input='MAX EXIT', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode == 0
        assert os.path.isfile('./data/not_simple_db.txt')
        assert result.stdout.strip() == 'Whiskey 13500'

    def test_not_simple_db_show_2():
        shutil.copy('./tests/data/simple_db_show_1.txt', DB_FILE_NAME)
        result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='MAX EXIT', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode == 0
        assert os.path.isfile(DB_FILE_NAME)
        assert result.stdout.strip() == 'NO DATA'

if __name__ == "__main__":
    pytest.main()

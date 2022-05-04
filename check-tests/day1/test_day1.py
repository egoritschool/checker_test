import filecmp
import os

import pytest


def not_changed(path):
    upstream_root = os.environ.get('CHECKER_SOURCE_DIR', os.getcwd())
    fork_root = os.environ.get('CHECKER_WORK_DIR', os.getcwd())
    upstream_path = os.path.join(upstream_root, path)
    fork_path = os.path.join(fork_root, path)
    if not os.path.exists(fork_path):
        return True
    if os.path.isdir(fork_path):
        dirs_cmp = filecmp.dircmp(upstream_path, fork_path)
        if dirs_cmp.right_only or dirs_cmp.diff_files or dirs_cmp.funny_files:
            return False
    else:
        return filecmp.cmp(upstream_path, fork_path)
    return True


@pytest.mark.skipif(not_changed('day1/task1.py'), reason='not updated')
def test_task1():
    from day1 import script
    with pytest.raises(ValueError):
        script.method()


@pytest.mark.skipif(not_changed('day1'), reason='not updated')
def test_task1_other_test():
    print('Output from the test')
    assert [1,2,3] == [1,2]
    pytest.fail('Should think before you type')


@pytest.mark.skipif(not_changed('day1'), reason='not updated')
def test_overall():
    from day1 import script
    print('Output from the test')
    with pytest.raises(ValueError):
        script.method()

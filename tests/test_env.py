from __future__ import annotations

from pathlib import Path
from unittest import mock

import pytest
from swerex.runtime.abstract import CommandTimeoutError

from sweagent.environment.hooks.abstract import EnvHook

from .conftest import swe_env_context


@pytest.mark.slow
def test_init_swe_env(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()


@pytest.mark.slow
def test_init_swe_env_conservative_clone(test_env_args):
    with mock.patch.dict("os.environ", {"SWE_AGENT_CLONE_METHOD": "full"}):
        with swe_env_context(test_env_args) as env:
            env.reset()


@pytest.mark.slow
def test_startup_commands(test_env_args):
    test_script = "echo 'hello world'"
    test_env_args.startup_commands = [test_script]
    with swe_env_context(test_env_args) as env:
        env.reset()


@pytest.mark.slow
def test_read_file(tmp_path, test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        content = env.read_file(Path("tests/filetoread.txt"))
        assert content.splitlines()[-1].strip() == "SWEEnv.read_file"


@pytest.mark.slow
def test_env_with_hook(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.add_hook(EnvHook())
        env.reset()


@pytest.mark.slow
def test_env_communicate_with_handling(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        env.communicate_with_handling("echo 'hello world'", error_msg="Failed to echo", timeout_duration=1)


@pytest.mark.slow
def test_env_communicate_with_handling_timeout(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        with pytest.raises(CommandTimeoutError):
            env.communicate_with_handling("sleep 10", error_msg="Failed to sleep", timeout_duration=0.2)


@pytest.mark.slow
def test_env_step(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        env.step(action="ls")


@pytest.mark.slow
def test_env_step_exit_forfeit(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        env.step(action="exit_forfeit")


@pytest.mark.slow
def test_env_step_exit_cost(test_env_args):
    with swe_env_context(test_env_args) as env:
        env.reset()
        env.step(action="exit_cost")

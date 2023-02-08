from __future__ import annotations

from pre_commit_hooks.hide_hassio_secrets import get_random_string
from pre_commit_hooks.hide_hassio_secrets import replace_hassio_secrets


def test_get_random_string():
    assert len(get_random_string()) == 12
    assert len(get_random_string(10)) == 10


def test_replace_hassio_secrets():
    secrets = {'internal_url': 'https://my.homeassistant.io'}
    fake_secrets = replace_hassio_secrets(secrets)
    assert fake_secrets['internal_url'] != 'https://my.homeassistant.io'

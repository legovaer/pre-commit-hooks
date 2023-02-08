from __future__ import annotations

from pre_commit_hooks.hide_hassio_secrets_test import replace_hassio_secrets


def test_hide_hassio_secrets():
    secrets = {'internal_url': 'https://my.homeassistant.io'}
    fake_secrets = replace_hassio_secrets(secrets)
    assert fake_secrets['internal_url'] != 'https://my.homeassistant.io'

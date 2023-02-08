from __future__ import annotations

import argparse
import random
import string
from typing import Sequence

import yaml


def get_random_string(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def replace_hassio_secrets(secrets: dict[str, str]) -> dict[str, str]:
    for secret in secrets:
        secrets[secret] = get_random_string()
    return secrets


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output', default='secrets-fake.yaml',
        help='Fake secrets filename.',
    )
    args = parser.parse_args(argv)

    retval = 0
    with open('secrets.yaml', encoding='utf8') as secrets:
        data = yaml.safe_load(secrets)

    with open(args.output, 'w', encoding='utf8') as fake_secrets:
        yaml.dump(
            replace_hassio_secrets(data),
            fake_secrets,
            default_flow_style=False,
            allow_unicode=True,
        )
        retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main())

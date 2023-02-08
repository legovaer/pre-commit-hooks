[![build status](https://github.com/legovaer/pre-commit-hooks/actions/workflows/main.yml/badge.svg)](https://github.com/legovaer/pre-commit-hooks/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/legovaer/pre-commit-hooks/main.svg)](https://results.pre-commit.ci/latest/github/legovaer/pre-commit-hooks/main)

pre-commit-hooks
================

Some custom hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/legovaer/pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: hide-hassio-secrets
    # -   id: ...
```

### Hooks available

#### `hide-hassio-secrets`
Generate a dummy secrets.yaml file.
  - Specify the name of the secrets file with `args: ['--output=fake-secrets.yaml']` (default=secrets-fake.yaml).

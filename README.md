# Ansible Role: sql_exporter

[![Build Status](https://travis-ci.com/cloudalchemy/ansible-sql_exporter.svg?branch=master)](https://travis-ci.com/cloudalchemy/ansible-sql_exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.sql_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/sql_exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-sql_exporter.svg)](https://github.com/cloudalchemy/ansible-sql_exporter/tags)

## Description

Deploy [sql_exporter](https://github.com/prometheus/sql_exporter) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `sql_exporter_web_listen_address` | "0.0.0.0:9399" | Address on which sql_exporter will listen |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - cloudalchemy.sql_exporter
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/ansible-community/molecule) (v3.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system. Running your tests is as simple as executing `molecule test`.

## Continuous Intergation

Combining molecule and circle CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which can take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

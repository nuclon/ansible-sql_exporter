# Ansible Role: sql_exporter

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-nuclon.sql_exporter-blue.svg)](https://galaxy.ansible.com/nuclon/sql_exporter/)
[![GitHub tag](https://img.shields.io/github/tag/nuclon/ansible-sql_exporter.svg)](https://github.com/nuclon/ansible-sql_exporter/tags)

## Description

Deploy [sql_exporter](https://github.com/free/sql_exporter) using ansible.

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
    - role: nuclon.sql_exporter
      sql_exporter_data_source_name: "mysql://user:password@tcp(mysql-host.corp.local:3306)/database_name"
      sql_exporter_collectors:
        - collector_name: service_data
          metrics:
            - metric_name: service_pending_events
              type: gauge
              help: "Not processed events count"
              values: [cnt]
              query: |
                SELECT count(*) as cnt
                FROM events
                WHERE status=0
            - metric_name: service_failed_events
              type: gauge
              help: "Failed events count"
              values: [cnt]
              query: |
                SELECT count(*) as cnt
                FROM events
                WHERE
                  failed = 1
```
The role will generate a file for every entry in sql_exporter_collectors.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/sql_exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/systemd/system/sql_exporter.service",
        "/usr/local/bin/sql_exporter",
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host):
    assert host.group("sql-exp").exists
    assert "sql-exp" in host.user("sql-exp").groups
    assert host.user("sql-exp").shell == "/usr/sbin/nologin"
    assert host.user("sql-exp").home == "/"


def test_service(host):
    s = host.service("sql_exporter")
    #    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://0.0.0.0:9399"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
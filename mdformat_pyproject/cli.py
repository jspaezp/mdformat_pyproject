import os
import sys
from typing import Any

from mdformat import _conf as mdconf
from mdformat._conf import _validate_keys, _validate_values

if sys.version_info <= (3, 11):
    import tomli as tomllib
else:
    import tomllib

from typing import NoReturn


def get_toml_file_tool(tool_name: str) -> dict[str, Any] | None:
    """See if there is a pyproject.toml and extract the correct section if it exists."""
    if os.path.isfile("pyproject.toml"):
        with open("pyproject.toml", "rb") as file:
            toml_dict = tomllib.load(file)
            if tool_section := toml_dict.get("tool", None):
                if tool_sect := tool_section.get(tool_name, None):
                    assert isinstance(tool_sect, dict)
                    return tool_sect
    return {}


def overwrite_toml_opts(*args, **kwargs):
    toml_opts = get_toml_file_tool("mdformat")
    conf_path = "pyproject.toml"
    print("READ THE pyproject.toml FILE!!!")
    _validate_keys(toml_opts, conf_path)
    _validate_values(toml_opts, conf_path)
    return toml_opts


mdconf.read_toml_opts = overwrite_toml_opts


def run() -> NoReturn:
    from mdformat import _cli as mdcli

    exit_code = mdcli.run(sys.argv[1:])
    sys.exit(exit_code)


if __name__ == "__main__":
    run()

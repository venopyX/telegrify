"""Base formatter implementation"""

from typing import Any

from telenotif.core.interfaces import IFormatter


class BaseFormatter(IFormatter):
    """Base class for formatters"""

    def format(self, payload: dict[str, Any]) -> str:
        return self._dict_to_string(payload)

    def _dict_to_string(self, data: dict[str, Any], indent: int = 0) -> str:
        lines = []
        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"{' ' * indent}{key}:")
                lines.append(self._dict_to_string(value, indent + 2))
            elif isinstance(value, list):
                lines.append(f"{' ' * indent}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        lines.append(self._dict_to_string(item, indent + 2))
                    else:
                        lines.append(f"{' ' * (indent + 2)}- {item}")
            else:
                lines.append(f"{' ' * indent}{key}: {value}")
        return "\n".join(lines)

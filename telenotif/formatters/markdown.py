"""Markdown formatter for Telegram"""

from typing import Any

from telenotif.formatters.base import BaseFormatter


class MarkdownFormatter(BaseFormatter):
    """Markdown formatter - converts payload to Telegram Markdown format"""

    def format(self, payload: dict[str, Any]) -> str:
        lines = []

        for key, value in payload.items():
            if key.lower() in ["title", "heading", "header"]:
                lines.append(f"*{value}*")
            elif isinstance(value, dict):
                lines.append(f"*{key}:*")
                for k, v in value.items():
                    lines.append(f"  {k}: {v}")
            elif isinstance(value, list):
                lines.append(f"*{key}:*")
                for item in value:
                    lines.append(f"  • {item}")
            else:
                lines.append(f"{key}: {value}")

        return "\n".join(lines)

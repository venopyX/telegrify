"""Markdown formatter for Telegram"""

from typing import Any

from telenotif.formatters.base import BaseFormatter


class MarkdownFormatter(BaseFormatter):
    """Markdown formatter - converts payload to Telegram Markdown format"""

    def _escape(self, text: str) -> str:
        """Escape special Markdown characters"""
        for char in ["_", "*", "[", "]", "(", ")", "~", "`", ">", "#", "+", "-", "=", "|", "{", "}", ".", "!"]:
            text = str(text).replace(char, f"\\{char}")
        return text

    def format(self, payload: dict[str, Any]) -> str:
        lines = []

        for key, value in payload.items():
            if key.lower() in ["title", "heading", "header"]:
                lines.append(f"*{self._escape(value)}*")
            elif isinstance(value, dict):
                lines.append(f"*{self._escape(key)}:*")
                for k, v in value.items():
                    lines.append(f"  {self._escape(k)}: {self._escape(v)}")
            elif isinstance(value, list):
                lines.append(f"*{self._escape(key)}:*")
                for item in value:
                    lines.append(f"  • {self._escape(item)}")
            else:
                lines.append(f"{self._escape(key)}: {self._escape(value)}")

        return "\n".join(lines)

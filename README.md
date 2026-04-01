# code-assist

AI-powered coding assistant - Python 3.13 implementation.

> Inspired by Claude Code. Pure research and experimentation purpose only. No enterprise use.

## Quick Start

```bash
# Install dependencies
uv sync

# Run
uv run code-assist --version

# Or via module
uv run python -m code_assist --version
```

## Development

```bash
# Install with dev dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Lint
uv run ruff check src/ tests/

# Type check
uv run mypy src/code_assist/
```

## Architecture

See `docs/architecture.md` for full system design with mermaid diagrams.

## License

MIT

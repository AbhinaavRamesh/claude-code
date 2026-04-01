"""Shared test fixtures for code-assist."""

import pytest


@pytest.fixture
def tmp_project(tmp_path: pytest.TempPathFactory) -> str:
    """Create a temporary project directory for testing."""
    project = tmp_path / "test-project"  # type: ignore[operator]
    project.mkdir()
    return str(project)

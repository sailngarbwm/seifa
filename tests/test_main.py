import unittest
import re
from unittest.mock import patch

from typer.testing import CliRunner

from seifa import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_version(self):
        result = self.runner.invoke(main.app, ["--version"])
        assert result.exit_code == 0
        assert re.match(r"\d+\.\d+\.\d+", result.stdout)

    @patch("typer.launch")
    def test_repo(self, mock_launch):
        result = self.runner.invoke(main.app, ["repo"])
        assert result.exit_code == 0
        mock_launch.assert_called_once()
        self.assertIn(
            "https://github.com/rbturnbull/ausdex", str(mock_launch.call_args)
        )

    @patch("subprocess.run")
    def test_docs_live(self, mock_subprocess):
        result = self.runner.invoke(main.app, ["docs"])
        assert result.exit_code == 0
        mock_subprocess.assert_called_once()
        self.assertIn("sphinx-autobuild", str(mock_subprocess.call_args))

    @patch("webbrowser.open_new")
    @patch("subprocess.run")
    def test_docs_static(self, mock_subprocess, mock_open_web):
        result = self.runner.invoke(main.app, ["docs", "--no-live"])
        assert result.exit_code == 0
        mock_subprocess.assert_called_once()
        self.assertIn("sphinx-build", str(mock_subprocess.call_args))
        mock_open_web.assert_called_once()


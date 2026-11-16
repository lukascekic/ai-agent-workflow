"""Check the installer against temporary workflow and target directories."""
import contextlib
import io
from pathlib import Path
import shutil
import tempfile
import unittest

from install import install


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'workflow'
        self.repo = self.base / 'code with spaces'
        self.repo.mkdir()
        shutil.copytree(Path(__file__).resolve().parents[1] / 'template', self.root / 'template')

    def run_install(self, project='demo', dry_run=False, repo=None):
        with contextlib.redirect_stdout(io.StringIO()):
            return install(self.root, repo or self.repo, project, dry_run)

    def test_dry_run_writes_nothing(self):
        self.assertGreater(self.run_install(dry_run=True), 0)
        self.assertEqual(list(self.repo.iterdir()), [])
        self.assertFalse((self.root / 'projects').exists())

    def test_config_paths_and_hidden_files(self):
        self.run_install()
        config = (self.repo / '.workflow/config.md').read_text(encoding='utf-8')
        self.assertIn('Projekat: demo', config)
        self.assertIn(self.root.as_posix(), config)
        self.assertNotIn('<workflow-root>', config)
        self.assertTrue((self.repo / '.workflow/prompts/sealed.md').is_file())
        self.assertTrue((self.root / 'projects/demo/tasks/_TEMPLATE/task.md').is_file())
        self.assertFalse((self.repo / '.workflow/tasks').exists())

    def test_existing_instructions_config_and_state_are_unchanged(self):
        self.run_install()
        files = [self.repo / 'AGENTS.md', self.repo / '.workflow/config.md',
                 self.root / 'projects/demo/TASKS.md']
        for file in files:
            file.write_text('preserve this <projekat>', encoding='utf-8')
        self.assertEqual(self.run_install(), 0)
        for file in files:
            self.assertEqual(file.read_text(encoding='utf-8'), 'preserve this <projekat>')

    def test_invalid_names(self):
        for project in ('..', '.hidden', '../escape', 'a/b', 'a\\b', 'a b', 'CON', 'demo.'):
            with self.subTest(project=project), self.assertRaises(ValueError):
                self.run_install(project=project)
        self.assertFalse((self.root / 'projects').exists())

    def test_nested_repositories_are_rejected(self):
        nested = self.root / 'nested'
        nested.mkdir()
        for repo in (self.root, nested, self.base):
            with self.subTest(repo=repo), self.assertRaises(ValueError):
                self.run_install(repo=repo)

    def test_directory_collision_fails_before_writing(self):
        (self.repo / 'CLAUDE.md').mkdir()
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertFalse((self.repo / 'AGENTS.md').exists())
        self.assertFalse((self.root / 'projects').exists())

    def test_linked_workflow_directory_is_rejected(self):
        outside = self.base / 'elsewhere'
        outside.mkdir()
        try:
            (self.repo / '.workflow').symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks is unavailable in this environment.')
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertEqual(list(outside.iterdir()), [])

    def test_linked_state_parent_is_rejected_before_writing(self):
        outside = self.base / 'external-state'
        outside.mkdir()
        try:
            (self.root / 'projects').symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks is unavailable in this environment.')
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(list(self.repo.iterdir()), [])


if __name__ == '__main__':
    unittest.main()

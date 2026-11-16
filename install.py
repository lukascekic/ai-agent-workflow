"""Install the public workflow template without overwriting existing files."""
import argparse
from pathlib import Path
import re
import sys


def within(path, parent):
    return path == parent or parent in path.parents


def install(root, repo, project, dry_run=False):
    root = Path(root).resolve()
    repo = Path(repo).resolve()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', project):
        raise ValueError('Project name must start with a letter or digit and use only letters, digits, ., _ and -.')
    # Windows ignores trailing dots and reserves some filenames on every volume.
    reserved = {'CON', 'PRN', 'AUX', 'NUL'}
    reserved.update('COM' + str(n) for n in range(1, 10))
    reserved.update('LPT' + str(n) for n in range(1, 10))
    if project.endswith('.') or project.split('.')[0].upper() in reserved:
        raise ValueError('Project name is not portable to Windows.')
    if not repo.is_dir():
        raise ValueError('Target repository must be an existing directory.')
    if within(repo, root) or within(root, repo):
        raise ValueError('The workflow checkout and target repository must be separate directories, not nested.')
    state = root / 'projects' / project
    plan = []
    # Inspect every destination before writing. Do not follow links out of either root.
    for source, destination, boundary in (
        (root / 'template/repo', repo, repo),
        (root / 'template/state', state, root),
    ):
        if not source.is_dir():
            raise ValueError('Missing template directory: ' + str(source))
        for entry in sorted(source.rglob('*')):
            if entry.is_symlink():
                raise ValueError('Template symlinks are not supported: ' + str(entry))
            if not entry.is_file():
                continue
            target = destination / entry.relative_to(source)
            if not within(target.resolve(), boundary):
                raise ValueError('Destination escapes its expected directory: ' + str(target))
            for part in (target, *target.parents):
                is_junction = getattr(part, 'is_junction', lambda: False)
                if part.is_symlink() or is_junction():
                    raise ValueError('Linked destinations are not supported: ' + str(part))
                if part == boundary:
                    break
            if target.exists():
                if not target.is_file():
                    raise ValueError('Expected a file at: ' + str(target))
                print('KEEP  ' + str(target))
                continue
            for parent in target.parents:
                if parent.exists() and not parent.is_dir():
                    raise ValueError('Expected a directory at: ' + str(parent))
            content = entry.read_text(encoding='utf-8')
            content = content.replace('<project>', project).replace('<workflow-root>', root.as_posix())
            plan.append((target, content))
    print('Workflow root: ' + str(root))
    print('Project state: ' + str(state))
    for target, content in plan:
        print(('WOULD ADD  ' if dry_run else 'ADD  ') + str(target))
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects existing files if another process writes first.
            with target.open('x', encoding='utf-8', newline='\n') as handle:
                handle.write(content)
    print('Existing instruction/config files are preserved. Merge and inspect them manually.')
    return len(plan)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('repo', type=Path)
    parser.add_argument('project')
    args = parser.parse_args()
    try:
        install(Path(__file__).resolve().parent, args.repo, args.project, args.dry_run)
    except (ValueError, OSError) as error:
        print('Installation failed: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

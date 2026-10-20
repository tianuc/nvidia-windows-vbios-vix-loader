"""Build a standalone Chinese Windows GUI and a redistributable license bundle."""
from importlib import metadata
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tkinter
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    version = json.loads((ROOT / 'upstream-version.json').read_text())
    name = 'vbios-loader-zh'
    subprocess.run([
        sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean', '--onefile',
        '--windowed', '--uac-admin', '--name', name,
        '--paths', str(ROOT / 'src'), '--distpath', str(ROOT / 'dist'),
        '--workpath', str(ROOT / 'build' / 'chinese'), '--specpath', str(ROOT / 'build'),
        str(ROOT / 'tools' / 'run_chinese.py'),
    ], cwd=ROOT, check=True)
    package = ROOT / 'dist' / 'chinese-package'
    package.mkdir(parents=True, exist_ok=True)
    for file in ('LICENSE', 'README_CN.md', 'THIRD_PARTY_NOTICES.md', 'THIRD_PARTY_NOTICES_ZH.md', 'upstream-version.json'):
        shutil.copy2(ROOT / file, package / file)
    shutil.copy2(ROOT / 'dist' / (name + '.exe'), package / (name + '.exe'))
    licenses = package / 'third_party'
    licenses.mkdir(exist_ok=True)
    shutil.copy2(Path(sys.base_prefix) / 'LICENSE.txt', licenses / 'CPython-LICENSE.txt')
    for source in (Path(sys.base_prefix) / 'tcl').rglob('license.terms'):
        shutil.copy2(source, licenses / (source.parent.name + '-license.terms'))
    distribution = metadata.distribution('pyinstaller')
    copies = 0
    for entry in distribution.files or ():
        if str(entry).endswith('licenses/COPYING.txt'):
            shutil.copy2(distribution.locate_file(entry), licenses / 'PyInstaller-COPYING.txt')
            copies += 1
    if not copies:
        raise RuntimeError('PyInstaller license missing')
    (package / 'BUILD-INFO.txt').write_text(
        f"Chinese release {version['tag']}-zh.{version['chinese_revision']}\n"
        f"Upstream commit {version['commit']}\n"
        f"CPython {sys.version.split()[0]}, Tcl/Tk {tkinter.Tcl().eval('info patchlevel')}\n"
        f"PyInstaller {distribution.version}; GPL bootloader with distribution exception\n"
        'Chinese GUI: community translation; upstream registry and NvAPI backend retained.\n', encoding='utf-8')
    archive = ROOT / 'dist' / f"{name}-{version['tag']}-zh.{version['chinese_revision']}-windows-x64.zip"
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zipped:
        for path in sorted(package.rglob('*')):
            if path.is_file():
                zipped.write(path, path.relative_to(package))
    sums = ROOT / 'dist' / 'SHA256SUMS-ZH'
    files = [ROOT / 'dist' / (name + '.exe'), archive]
    sums.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in files), encoding='ascii')
    print(sums.read_text())


if __name__ == '__main__':
    main()

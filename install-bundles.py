#!/usr/bin/env python3

from argparse import ArgumentParser, BooleanOptionalAction
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

java_pde_version = '0.8.0'
java_debug_version = '0.52.0'
java_test_version = '0.40.1'
# Microsoft has stopped releasing the vsix package for the test plugin.
# See https://github.com/mason-org/mason-registry/issues/3036
use_alternate_test_url = True

def download_and_unzip(url, output_directory):
    resp = urlopen(url)
    with ZipFile(BytesIO(resp.read())) as zipfile:
        extract_extensions_from(zipfile, output_directory)

def extract_extensions_from(zipfile, output_directory):
    bundle_files = [name for name in zipfile.namelist() if name.startswith("extension/server")]

    output_directory.mkdir(parents=True, exist_ok=True)

    for bundle_file in bundle_files:
        bs = zipfile.read(bundle_file)

        filename = Path(bundle_file).name
        with open(output_directory / filename, 'wb') as binary_file:
            binary_file.write(bs)

def rm_tree(path):
    if not path.is_dir():
        return

    path = Path(path)
    for child in path.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()

if __name__ == '__main__':
    parser = ArgumentParser(description="Install VSCode bundles for eclipes.jdt.ls (a.k.a. jdtls)")
    parser.add_argument("--java-debug", default=True, action=BooleanOptionalAction,
        help="A lightweight Java Debugger based on Java Debug Server which extends the Language Support for Java by Red Hat.")
    parser.add_argument("--java-test", default=True, action=BooleanOptionalAction,
        help="A lightweight extension to run and debug Java test cases.")
    parser.add_argument("--pde", default=False, action=BooleanOptionalAction,
        help=("This extension works as a plugin of Language Support for Java by Red Hat. "
            "It provides the ability to import Eclipse PDE projects and set up the correct target platforms."))

    args = parser.parse_args()

    bundles = Path('bundles')
    rm_tree(bundles)

    if args.java_debug:
        version = java_debug_version
        download_and_unzip(
            f'https://github.com/microsoft/vscode-java-debug/releases/download/{version}/vscjava.vscode-java-debug-{version}.vsix',
            bundles / 'java-debug'
        )
    if args.java_test:
        version = java_test_version
        url = f'https://github.com/microsoft/vscode-java-test/releases/download/{version}/vscjava.vscode-java-test-{version}.vsix'
        if use_alternate_test_url:
            url = f'https://github.com/nvim-java/vscode-java-test-releases/releases/download/{version}/artifacts.zip'
        download_and_unzip(
            url,
            bundles / 'java-test'
        )

    if args.pde:
        version = java_pde_version
        download_and_unzip(
            f'https://github.com/testforstephen/vscode-pde/releases/download/{version}/vscode-pde-{version}.vsix',
            bundles / 'pde'
        )

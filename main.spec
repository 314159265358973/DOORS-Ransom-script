# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['ransom.py'],          # script
    pathex=[],
    binaries=[],
    datas=[
        ('icon.webp', '.'),  # icon
        ('Ransom.png', '.'),  # ransom image
    ],
    hiddenimports=[
        'pygame'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main.RANSOM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # False = no console
    disable_windowed_traceback=False,
    icon='icon.webp',  # optional
)

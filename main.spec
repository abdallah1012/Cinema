# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import sys
sys.setrecursionlimit(100000)
a = Analysis(['main.py'],
             pathex=['C:\\Users\\user\\Desktop\\package'],
             binaries=[],
             datas=[("C:\\Users\\user\\Desktop\\package\\main.css","."),
			 ("C:\\Users\\user\\Desktop\\package\\token_youtube_v3.pickle","."), 
			 ("C:\\Users\\user\\Desktop\\package\\client_secret.json", "."),
			 ("C:\\Users\\user\\Desktop\\package\\cinema.ico", "."),
			 ("C:\\Users\\user\\Desktop\\package\\Images\\*.png", ".\\Images"),
			 ("C:\\Users\\user\\Anaconda3\\Lib\\site-packages\\google_api_python_client-1.12.8.dist-info/*", "google_api_python_client-1.12.8.dist-info")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Cinema',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
		  icon = '.\\cinema.ico')

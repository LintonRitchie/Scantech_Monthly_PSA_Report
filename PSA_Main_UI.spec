# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['PSA_Main_UI.py'],
             pathex=['C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\'],
             binaries=[],
             datas=[],
             hiddenimports=['pywin32', 'pywintypes', 'pkg_resources', 'win32com', 'pythoncom'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='PSA_Main_UI',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PSA_Main_UI')

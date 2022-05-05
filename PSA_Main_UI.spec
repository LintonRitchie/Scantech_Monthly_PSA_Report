# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['PSA_Main_UI.py'],
             pathex=['C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32\\', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32\\lib\\', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32com\\', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\pywin32', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\core\\ctypes', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\pywin32_system32'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
splash = Splash('C:\\PSAGen\\ScantechFullLogo.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=None,
                text_size=12,
                minify_script=True)

exe = EXE(pyz,
          a.scripts, 
          splash,
          [],
          exclude_binaries=True,
          name='PSA_Main_UI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               splash.binaries,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PSA_Main_UI')

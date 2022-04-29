# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['PSA_Main_UI.py'],
             pathex=['C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Scripts', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32com', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\pywin32', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\lib', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\fft', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\linalg', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\ma', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\array_api', 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\numpy\\typing'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
splash = Splash('C:\\PSAGen\\ScantechSqrLogo.PNG',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=None,
                text_size=12,
                minify_script=True)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas, 
          splash, 
          splash.binaries,
          [],
          name='PSA_Main_UI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

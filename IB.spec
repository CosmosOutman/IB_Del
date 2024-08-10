# main.spec
block_cipher = None

a = Analysis(['G:/1/IB.py'],
             pathex=['G:/1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='IB',
          debug=False,
          strip=False,
          upx=True,
          console=False,   # 设置为 False 以隐藏控制台窗口
          icon=None)
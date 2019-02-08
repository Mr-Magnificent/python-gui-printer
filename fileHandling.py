import os
import sys

# Since we are developing only for win32 hence
if sys.platform == 'win32':
    import winreg
    _registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    def get_runonce():
        return winreg.OpenKey(_registry,
                r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
        winreg.KEY_ALL_ACCESS)

    def add(name, application):
        """add a new autostart entry"""
        key = get_runonce()
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, application)
        winreg.CloseKey(key)

    def exists(name):
        """check if an autostart entry exists"""
        key = get_runonce()
        exists = True
        try:
            winreg.QueryValueEx(key, name)
        except WindowsError:
            exists = False
        winreg.CloseKey(key)
        return exists

    def remove(name):
        """delete an autostart entry"""
        key = get_runonce()
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)


def test():
    assert not exists("test_xxx")
    try:
        add("test_xxx", "test")
        assert exists("test_xxx")
    finally:
        remove("test_xxx")
    assert not exists("test_xxx")

if __name__ == "__main__":
    test()
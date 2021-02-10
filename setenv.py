import winreg

import click

system_hkey = (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
user_hkey = (winreg.HKEY_CURRENT_USER, r"Environment")

@click.command()
@click.option("--name", required=True,
              help="Variable name")
@click.option("-v", "--value", required=True,
              help="Variable value")
@click.option("-u", "-user", is_flag=True, required=False, default=True,
              help="Specifies if set user environment. Default: True")
def set_variable(name, value, user=True):
    """
    Creates/replaces environment variable
    """
    hkey = user_hkey if user else system_hkey
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        return True
    except WindowsError:
        return False


@click.command()
@click.option("--name", required=True,
              help="Variable name")
@click.option("-v", "--value", required=True,
              help="Variable value")
@click.option("-u", "-user", is_flag=True, required=False, default=True,
              help="Specifies if set user environment. Default: True")
def append_variable(name, value, user=True):
    """
    Creates/appends environment variable
    """
    new_val = get_variable(name=name, user=user) + ";" + value
    set_variable(name=name, value=new_val, user=user)


@click.command()
@click.option("--name", required=True,
              help="Variable name")
@click.option("-u", "-user", is_flag=True, required=False, default=True,
              help="Specifies if set user environment. Default: True")
def get_variable(name, user=True):
    """
    Gets the value of environment variable
    """
    hkey = user_hkey if user else system_hkey
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_READ) as key:
            value, regtype = winreg.QueryValueEx(key, name)
        return value
    except WindowsError:
        return None

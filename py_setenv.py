import winreg

import click

system_hkey = (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
user_hkey = (winreg.HKEY_CURRENT_USER, r"Environment")


@click.command()
@click.argument("name", required=True)
@click.option("-v", "--value", required=False, default=None,
              help="Variable value")
@click.option("-u", "--user", is_flag=True, required=False,
              help="Specifies if configure user environment")
@click.option("-a", "--append", is_flag=True, required=False,
              help="Appends to/Creates environment variable")
@click.option("-d", "--delete", is_flag=True, required=False,
              help="Deletes environment variable")
def click_command(name, value, user, append, delete):
    """
    Utility to set/get/modify/delete windows environment variables via registry

    Usage:

        -u, --user flag is optional to all following commands

        to get value: provide only variable name

        to set value: provide variable name, value

        to append to existing value: provide variable name, value and -a flag
    """
    setenv(name, value, user, append, delete)

def setenv(name, value=None, user=False, append=False, delete=False):
    if not name:
        click.echo("No variable name is provided", err=True)
        return

    if value:
        value = str(value).strip()

    if append:
        if value is not None:
            result = append_variable(name, value, user)
        else:
            click.echo("No value is provided in append mode", err=True)
            result = False

    elif value is not None:
        result = set_variable(name, value, user)
    elif delete:
        result = delete_variable(name, user)
    else:
        result = get_variable(name, user)

    click.echo(result)
    return result


def set_variable(name, value, user):
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


def append_variable(name, value, user):
    """
    Creates/appends environment variable
    """
    new_val = get_variable(name=name, user=user) + ";" + value
    result = set_variable(name=name, value=new_val, user=user)
    return result


def get_variable(name, user):
    """
    Gets the value of environment variable
    """
    hkey = user_hkey if user else system_hkey
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_READ) as key:
            value, regtype = winreg.QueryValueEx(key, name)
        return value
    except WindowsError:
        return "Variable {} does not exist".format(name)

def delete_variable(name, user):
    """
    Deletes environment variable
    """
    hkey = user_hkey if user else system_hkey
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteValue(key, name)
            return True
    except WindowsError:
        return False

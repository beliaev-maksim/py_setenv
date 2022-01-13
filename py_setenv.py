import winreg

import click

system_hkey = (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
user_hkey = (winreg.HKEY_CURRENT_USER, r"Environment")


@click.command()
@click.argument("name", required=False)
@click.option("-v", "--value", required=False, default=None, help="Variable value")
@click.option("-u", "--user", is_flag=True, required=False, help="Specifies if configure user environment")
@click.option("-a", "--append", is_flag=True, required=False, help="Appends to/Creates environment variable")
@click.option("-d", "--delete", is_flag=True, required=False, help="Deletes environment variable")
@click.option("-l", "--list-all", is_flag=True, required=False, help="Lists all environment variables")
def click_command(name, value, user, append, delete, list_all):
    """
    Utility to set/get/modify/delete windows environment variables via registry

    Usage:

        -u, --user flag is optional to all following commands

        to get value: provide only variable name

        to set value: provide variable name, value

        to append to existing value: provide variable name, value and -a flag
    """
    setenv(name, value, user, append, delete, list_all)


def setenv(name="", value=None, user=False, append=False, delete=False, list_all=False, suppress_echo=False):
    if list_all:
        result = list_all_variables(user)
        if not suppress_echo:
            for var, val in result.items():
                click.echo(f"{var}={val}")
        return result

    if not name:
        if not suppress_echo:
            click.echo("No variable name is provided", err=True)
        return

    if value:
        value = str(value).strip()

    if append:
        if value is not None:
            result = append_variable(name, value, user, suppress_echo)
        else:
            if not suppress_echo:
                click.echo("No value is provided in append mode", err=True)
            result = False

    elif value is not None:
        result = set_variable(name, value, user)
    elif delete:
        result = delete_variable(name, user)
    else:
        result = get_variable(name, user, suppress_echo)

    if not suppress_echo:
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


def append_variable(name, value, user, suppress_echo):
    """
    Creates/appends environment variable
    """
    new_val = get_variable(name, user, suppress_echo)
    if new_val:
        new_val += ";" + value
    else:
        new_val = value

    result = set_variable(name=name, value=new_val, user=user)
    return result


def get_variable(name, user, suppress_echo):
    """
    Gets the value of environment variable
    """
    hkey = user_hkey if user else system_hkey
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_READ) as key:
            value, regtype = winreg.QueryValueEx(key, name)
        return value
    except WindowsError:
        if not suppress_echo:
            click.echo("Environment Variable '{}' does not exist".format(name))
        raise KeyError


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


def list_all_variables(user):
    hkey = user_hkey if user else system_hkey
    all_vars = {}
    try:
        with winreg.OpenKey(*hkey, access=winreg.KEY_ALL_ACCESS) as key:
            for i in range(winreg.QueryInfoKey(key)[1]):
                var, val, var_type = winreg.EnumValue(key, i)
                all_vars[var] = val
    except WindowsError:
        pass

    return all_vars

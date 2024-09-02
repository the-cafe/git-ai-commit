import subprocess
import pkg_resources

# TODO - get repo root directory without using git command
def execute_cli_command(cmd_string_list, cwd=None, output=False):
    try:
        result = subprocess.run(
            cmd_string_list,
            cwd=cwd,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # timeout in 1m/60s
        )

        if output:
            print(result.stdout)

        return result
    except subprocess.CalledProcessError as e:
        cmd_string = " ".join(cmd_string_list)
        error_msg = f"🚨 Total failure to call: {cmd_string}\n{e.stderr}"
        raise Exception(error_msg)

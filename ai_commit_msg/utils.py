import subprocess

# TODO - get repo root directory without using git command
def execute_cli_command(cmd_string_list, cwd=None):
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
        return result
    except subprocess.CalledProcessError as e:
        cmd_string = " ".join(cmd_string_list)
        error_msg = f"🚨 Total failure to call: {cmd_string}\n{e.stderr}"
        raise Exception(error_msg)

def get_repo_root_directory():
    git_directory = execute_cli_command(['git', 'rev-parse', '--show-toplevel']).stdout.rstrip()

    return git_directory

def get_git_directory():
    script_directory= execute_cli_command(['git', 'rev-parse', '--git-dir']).stdout.rstrip()
    return script_directory


from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.model_error_handling import AIModelHandlerError

def prepare_commit_msg_hook():

    existing_content = GitService.read_commit_editmsg_file()

    filtered_content = "\n".join([line for line in existing_content.splitlines() if not line.strip().startswith('#')])

    if filtered_content != "":
        Logger().log("Commit message already exists, skipping AI commit message generation")
        return

    staged_diff = GitService.get_staged_diff()

    try:
        success_banner = GitService.get_success_banner()
        commit_message = generate_commit_message(staged_diff.stdout)
        GitService.update_commit_message(commit_message + "\n" + success_banner)
    except AIModelHandlerError as error:
        GitService.update_commit_message(GitService.get_error_banner(error))

    return

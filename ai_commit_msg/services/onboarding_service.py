import os
import sys
import time
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet
import inquirer
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.cli.hook_handler import setup_git_hook
from ai_commit_msg.utils.models import (
    OPEN_AI_MODEL_LIST,
    ANTHROPIC_MODEL_LIST,
    OLLAMA_MODEL_LIST,
)
from rich.panel import Panel
from rich.style import Style
from rich.console import Group
from rich import box

console = Console()


def animate_banner(text, duration=1):
    f = Figlet(font="slant")
    frames = []
    colors = ["yellow", "green", "blue", "magenta", "cyan"]
    for i in range(len(text) + 1):
        frame = f.renderText(text[:i])
        frames.append(frame)

    start_time = time.time()
    while time.time() - start_time < duration:
        for frame, color in zip(frames, colors * (len(frames) // len(colors) + 1)):
            console.clear()
            panel = Panel(
                Text(frame, style=f"bold {color}"),
                box=box.DOUBLE,
                expand=False,
                border_style=f"bold {color}",
            )
            console.print(panel)
            time.sleep(0.1)

    console.clear()
    final_colors = [
        "bold red",
        "bold yellow",
        "bold green",
        "bold cyan",
        "bold blue",
        "bold magenta",
    ]
    final_text = Text()
    for i, char in enumerate(frames[-1]):
        final_text.append(char, style=final_colors[i % len(final_colors)])

    final_panel = Panel(
        final_text, box=box.DOUBLE, expand=False, border_style="bold magenta"
    )
    console.print(final_panel)


def onboarding_flow():
    os.system("cls" if os.name == "nt" else "clear")
    animate_banner("Git AI Commit")

    print_formatted_text(
        HTML("\n<b>Welcome to AI Commit MSG! Let's get you set up.</b>\n")
    )

    if not GitService.is_git_installed() or not GitService.is_git_repository():
        console.print(
            "Please ensure Git is installed and you're in a Git repository.",
            style="bold red",
        )
        sys.exit(1)

    setup_git_hook()

    print_formatted_text(HTML("\n<b>Choose your preferred AI provider:</b>"))
    provider_choice = inquirer.prompt(
        [
            inquirer.List(
                "provider",
                message="Select AI Provider",
                choices=["OpenAI", "Anthropic", "Ollama"],
            )
        ]
    )["provider"].lower()

    default_models = {
        "openai": "gpt-4o-mini",
        "anthropic": "claude-3-sonnet-20240229",
        "ollama": "ollama/llama3",
    }

    model_choices = {
        "openai": OPEN_AI_MODEL_LIST,
        "anthropic": ANTHROPIC_MODEL_LIST,
        "ollama": OLLAMA_MODEL_LIST,
    }

    model_choice = inquirer.prompt(
        [
            inquirer.List(
                "model",
                message="Select Model",
                choices=model_choices[provider_choice],
                default=default_models[provider_choice],
            )
        ]
    )["model"]

    config_service = ConfigService()
    config_service.set_model(f"{model_choice}")

    if provider_choice in ["openai", "anthropic"]:
        print_formatted_text(
            HTML(f"\n<b>Let's set up your {provider_choice.capitalize()} API key.</b>")
        )
        api_key = input(f"[?] Enter your {provider_choice.capitalize()} API key: ")
        if api_key:
            getattr(config_service, f"set_{provider_choice}_api_key")(api_key)
            console.print(
                f"{provider_choice.capitalize()} API key set successfully!",
                style="bold green",
            )
        else:
            console.print(
                f"No API key provided. You'll need to set it later to use {provider_choice.capitalize()}.",
                style="bold yellow",
            )
    elif provider_choice == "ollama":
        ollama_url = inquirer.prompt(
            [
                inquirer.Text(
                    "url",
                    message="Enter your Ollama URL",
                    default="http://localhost:11434/api/chat",
                )
            ]
        )["url"]
        config_service.set_ollama_url(ollama_url)
        console.print("Ollama configured successfully!", style="bold green")

    enable_logging = inquirer.prompt(
        [
            inquirer.Confirm(
                "logging", message="Would you like to enable logging?", default=False
            )
        ]
    )["logging"]
    config_service.set_logger_enabled(enable_logging)

    print_formatted_text(
        HTML(
            "\n<b>Onboarding complete! 🎉 Congratulations on setting up AI Commit MSG!</b>"
        )
    )

    completion_message = Group(
        Text(
            "You're all set to revolutionize your commit messages!", style="bold green"
        ),
        Text("\nTo generate a commit message:", style="italic"),
        Text("1. Stage your changes", style="cyan"),
        Text("2. Run the command:", style="cyan"),
        Text("\n   git-ai-commit", style="yellow", justify="center"),
        Text("\n"),
        Text("\nFor more information:", style="italic"),
        Text("• Check our documentation", style="cyan"),
        Text("• Run the command:", style="cyan"),
        Text("\n   git-ai-commit help", style="yellow", justify="center"),
        Text("\n"),
    )

    panel = Panel(
        completion_message,
        title="Next Steps",
        subtitle="Happy Coding!",
        expand=False,
        border_style="bold magenta",
        box=box.ROUNDED,
    )

    ConfigService().set_last_updated_at()
    console.print(panel)

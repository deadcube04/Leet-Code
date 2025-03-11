import subprocess

def run_command(command: str):
    """Executa um comando no terminal e retorna a saída como string."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error at '{command}':\n -> {result.stderr}")
    return result.stdout.strip()  # Removendo quebras de linha extras

def add_and_commit(message: str):
    run_command("git add .")
    run_command(f'git commit -m "{message}"')

def check_pending_commits(branch: str) -> bool:
    pending_commits = run_command(f"git log origin/{branch}..HEAD --oneline")
    if pending_commits:
        print("commits to push: \n")
        print(pending_commits)
        return True
    return False

commit_message = input("Insira a mensagem do commit: ")

if commit_message:
    add_and_commit(commit_message)

branch = run_command("git branch --show-current")

if check_pending_commits(branch):
    print("to push type 1")
    if input('\n') == "1":
        run_command(f"git push origin {branch}") 

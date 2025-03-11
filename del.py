import git

# Проверяем работу GitPython
repo_path = "F:\\Dev\\_codewars"
if os.path.exists(repo_path):
    repo = git.Repo(repo_path)
    print(f"Репозиторий найден: {repo_path}")
else:
    print(f"Репозиторий не существует: {repo_path}")
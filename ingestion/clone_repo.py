from git import Repo

def clone_repo(repo_url: str, destination_path: str) -> str:
    try:
        print(f"Cloning {repo_url}...")
        Repo.clone_from(repo_url, destination_path)
        print(f"Repository cloned to {destination_path}")
        return destination_path

    except Exception as e:
        raise RuntimeError(
            f"Failed to clone repository {repo_url}: {e}"
        )
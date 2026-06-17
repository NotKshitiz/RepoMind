import subprocess

def clone_repo(repo_url: str, destination_path: str) -> str:
    try:
        print(f"Cloning {repo_url}...")
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, destination_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Repository cloned to {destination_path}")
        return destination_path

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Failed to clone repository {repo_url}: {e.stderr}"
        )
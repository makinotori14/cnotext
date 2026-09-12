from repo import make_repo
from agent import make_query

def main():
    repo_path = make_repo()
    make_query(repo_path)

if __name__ == "__main__":
    main()
import os

import git

repo = git.Repo(".", search_parent_directories=True)
main_head = repo.heads.main
logs = main_head.log()
print(logs[0])
print(logs[-1].message)


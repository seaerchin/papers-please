# useful commands
```bash
gh stack push

gh stack submit

gh stack sync
```

- `gh stack push` - pushes all branches upstream
- `gh stack submit` - pushes branches and creates or updates PRs, linking them as a Stack on GitHub.
- `gh stack sync` - all in one: - fetch, rebase, push, sync stack/PR state, link open PRs into a Stack on GitHub, and optionally prune local branches for merged PRs. If there is a divergence between local and remote stacks, you will be prompted to resolve.

# workflow

> [!NOTE] `Am` flag on `gs`
> For speed, use the `-Am` flags to fold staging, committing, and branch creation into a single command
> 
> `Am` is short for `--all --message`

- `gs init <name>`
- `gs add -Am <commit_msg>`
the `gs add -Am "..."` stages all files, commits and creates a new branch if the existing branch **already has commits**

# making mid-stack changes
```shell
# navigate and commit the fix
gh stack down # can also do gh stack checkout or gs checkout <branch>
git add users_api.go
git commit -m "Add get-user endpoint"

# rebase everything above to ensure nothing breaks
gh stack rebase --upstack

# back to base branch
gh stack top
```


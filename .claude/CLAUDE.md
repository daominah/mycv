# CV Workflow

`README.md` is the only source of truth edited by hand.
`readme.html` and `readme.pdf` are derived artifacts.

## Steps

1. **User:** edit `README.md`.
2. **Claude:** create a new branch from `master`,
   commit the `README.md` change with message `WIP ...`,
   and push the branch to GitHub.
3. **User (manual):** open the rendered README on GitHub for that branch,
   copy the `<article>` element source,
   and paste it into local `readme.html`
   (replacing the existing `<article>` content).
4. **Claude:** switch back to `master`
   (the pasted `readme.html` change carries over as unstaged);
   restore the `README.md` change onto master's working tree,
   for example `git checkout <wip-branch> -- README.md`;
   then run `.venv/bin/python html_to_pdf.py` to regenerate `readme.pdf`.
5. **Claude:** review the diff on master,
   commit `README.md`, `readme.html`, `readme.pdf` together
   with a proper (non-WIP) commit message,
   and push to `origin/master` directly.
   Direct commits to `master` are allowed for this workflow.

## Branch cleanup

After the master commit is pushed, delete the WIP branch
locally and on `origin`
(`git branch -D <wip>`, `git push origin --delete <wip>`).

## Rules

- Only `README.md` is edited by hand.
- **Do not** hand-edit `readme.html` to mirror `README.md` edits.
  The GitHub render is the canonical HTML; hand edits drift from it
  and the PDF preserves those drifts.
- The WIP branch exists only to trigger GitHub's render.
  Its `WIP ...` commits are disposable;
  only the final master commit matters.

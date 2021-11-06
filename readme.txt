---HOW TO PUSH ON BRANCH MASTER_--------

-- first pull the repo
git pull "repo-link"

--change the origin to the repo
git remote add origin "repo-link"

--add, commit etc.

--ex the main branch is called main
-- to switch to it use 
git checkout -b main

--for push
git push origin main 
:D


RUN WITH PARAMETERS 
KnightMain.py  -p 'dimension' 'finalX' 'finalY' 'algtype'
algtype= bfs, dfs, ass, ucs
dimension = 8, 12 16
finalx, finaly constrained by dimension (inside area)

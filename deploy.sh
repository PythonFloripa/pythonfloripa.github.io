echo "Updating local copy"
git pull origin master:master
echo "Running mkdocs gh-deploy"
mkdocs gh-deploy

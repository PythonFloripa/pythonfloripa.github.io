echo "Running mkdocs gh-deploy"
mkdocs gh-deploy -b master --clean
git push origin master

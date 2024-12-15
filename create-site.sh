hugo new site quickstart
mv quickstart/* .
rm -rf quickstart
git submodule add https://github.com/monkeyWzr/hugo-theme-cactus.git themes/cactus 
echo "theme = 'cactus'" >> hugo.toml
git add .
git commit -m "adding site"
git push

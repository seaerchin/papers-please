mkdir "$1"
cp "template.py" "$1/$1.py"
cd "$1"
sed -i '' "s/<FILE>/$1/" "$1.py"

touch "$1.in"
touch "$1.out"

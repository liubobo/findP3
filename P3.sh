# #!/bin/bash
# chmod +x ./P3.sh  #使脚本具有执行权限

echo "# findP3" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/liubobo/findP3.git
git push -u origin master

#!/bin/bash
echo "Hello World"
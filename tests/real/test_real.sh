#!/bin/sh

#test rider management tool
rider create project
# rider create project.app

#copy test project files into
cp -R template/* project/
cp -R tests.py project/

rider run project&
sleep 5

kill -9 `ps -Af | grep "rider run project" | grep -v 'grep' | awk '{print $2}'`
rm -rf project

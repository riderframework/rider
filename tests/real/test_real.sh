#!/bin/sh

#test rider management tool
rider create project
# rider create project.app

#copy test project files into
cp -R template/* project/
cp -R tests.py project/test_data.py

rider run project
#
cd project
coverage combine
#coverage report
cp .coverage ../
cd ..
rm -rf project

#!/usr/bin/env bash

set -x
BRANCH=master
TARGET_REPO=crazygit/crazygit.github.io
PELICAN_OUTPUT_FOLDER=output

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "lianglin999@gmail.com"
        git config --global user.name "crazygit"
    fi
    # using token to clone repo
    git clone --quiet --branch=$BRANCH --recursive https://${GH_TOKEN}@github.com/$TARGET_REPO blog-html > /dev/null
    # go into directory and copy data we're interested in to that directory
    cd blog-html
    rsync -avq --delete --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    echo "*.webassets-cache" > .gitignore
    #add, commit and push files
    git add -Af .
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    git push -fq origin $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi

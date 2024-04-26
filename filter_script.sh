git filter-branch --commit-filter '
if [ "$GIT_AUTHOR_NAME" = "UwaiseAlikhan" ]; then
    export GIT_AUTHOR_NAME="AbdulmalikKhouj";
    export GIT_AUTHOR_EMAIL="khoujabdulmalik919@gmail.com";
    git commit-tree "$@";
else
    git commit-tree "$@";
fi' HEAD

#!/usr/bin/env bash
cd ~
docopt-completion hey_dewey --manual-bash > /dev/null
if [ ! -f ./hey_dewey.sh ]; then
    sudo docopt-completion hey_dewey --manual-bash > /dev/null
    sudo mv /etc/bash_completion.d/hey_dewey.sh ~/.dewey_autocomplete.sh
    sudo chmod 777 ~/.dewey_autocomplete.sh
else
    mv hey_dewey.sh .dewey_autocomplete.sh
fi;

echo "" >> ~/.dewey_autocomplete.sh
echo "complete -F _hey_dewey hey_dewey" >> ~/.dewey_autocomplete.sh
echo "complete -F _hey_dewey dewey" >> .dewey_autocomplete.sh
echo "complete -F _hey_dewey d" >> .dewey_autocomplete.sh

source .dewey_autocomplete.sh

function _run_dewey() {
    eval "$(hey_dewey --pre $@)";
    hey_dewey $@;
    eval "$(hey_dewey --post $@)";
}

alias d="_run_dewey"
alias dewey="_run_dewey"

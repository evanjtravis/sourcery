#!/usr/bin/env python

import subprocess

def main():
    print "GIT ALIASES:"
    output = subprocess.check_output(
                "git config --get-regexp ^alias\.".split(" ")
            )
    output = output.split("\n")
    alias_dict = {}
    max_alias_len = 0;
    for x in range(len(output)):
        alias = ''
        row = output[x]
        # get rid of `alias.` prefix
        row = row.split('.', 1)[-1]
        # break up row into parts, separating out alias name
        row = row.split(' ', 1)
        alias = row.pop(0)
        # fill in alias:cmd key:value pairs
        if alias != '':
            alias_dict[alias] = row[0]
            # update longest alias name
            al_len = len(alias)
            if al_len > max_alias_len:
                max_alias_len = al_len
    al_keys = alias_dict.keys()
    al_keys.sort()
    for key in al_keys:
        buff = ''
        len_diff = max_alias_len - len(key)
        buff = " "*len_diff
        print "    %s:%s\t%s"%(key, buff, alias_dict[key])



if __name__ == "__main__":
    main()

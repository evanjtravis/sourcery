#!/usr/bin/env python
import os
import subprocess

DIR = os.path.abspath(os.path.dirname(__file__))
DOTFILE_DIR = os.path.abspath(os.path.normpath(os.path.join("../../home/")))

def main():
    dir_depth = 0
    for root,dirs,files in os.walk(DOTFILE_DIR):
        for fname in files:
            link_src = os.path.join(root, fname)
            if dir_depth < 1:
                link_dst = "~" + root.replace(DOTFILE_DIR, "")
                link_dst = os.path.join(link_dst, "." + fname)
            else:
                link_dst = "~/." + root.replace(DOTFILE_DIR, "")[1:]
                link_dst = os.path.join(link_dst, fname)

            link_dst = os.path.expanduser(link_dst)
            subprocess.run([
                "ln",
                "--force",
                "--symbolic",
                link_src,
                link_dst
            ])
        dir_depth += 1


if __name__ == "__main__":
    main()


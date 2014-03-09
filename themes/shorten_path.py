#!/usr/bin/python

# Copied from https://gist.github.com/seanh/5233082

import os
import os.path

def shorten_path(path, max_length=150):
    '''Return the given path, shortened if it's too long.

    Parent directories will be collapsed, fish-style. Examples:

    /home/seanh -> ~
    /home/seanh/Projects/ckan/ckan/ckan -> ~/P/c/c/ckan
    /home/seanh/Projects/ckan/ckan-> ~/Projects/ckan/ckan

    '''
    # Replace the user's homedir in path with ~
    homedir = os.path.expanduser('~')
    if path.startswith(homedir):
        path = '~' + path[len(homedir):]

    parts = path.split(os.sep)

    # Remove empty strings.
    parts = [part for part in parts if part]
    path = os.sep.join(parts)

    # Starting from the root dir, truncate each dir to just its first letter
    # until the full path is < max_length or all the dirs have already been
    # truncated. Never truncate the last dir.
    while len(path) > max_length:
        for i in range(0, len(parts) - 1):
            part = parts[i]
            if len(part) > 1:
                part = part[0]
                parts[i] = part
                path = os.sep.join(parts)
                continue
        break
    return path


def current_working_dir():
    '''Return the full absolute path to the current working directory.'''

    # Code for getting the current working directory, copied from
    # <https://github.com/Lokaltog/powerline/>.
    try:
        try:
            cwd = os.getcwdu()
        except AttributeError:
            cwd = os.getcwd()
    except OSError as e:
        if e.errno == 2:
            # User most probably deleted the directory, this happens when
            # removing files from Mercurial repos for example.
            cwd = "[not found]"
        else:
            raise
    return cwd

if __name__ == '__main__':
    print shorten_path(current_working_dir())

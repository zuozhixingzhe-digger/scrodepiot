#!/usr/bin/env python3
# --digger-created--20260725
#  zuozhixingzhe/digger/作止行者 (c) all rights reserved;
# Contact me at `321323006+zuozhixingzhe-digger@users.noreply.github.com`
# scrodepiot:main.py
# this is just the main process -- all the contents are here(except when we make it too huge to make it in a file )
# --!!!--GIT ENABLED --DO NOT put any sensitive (e.g. key) or non-plaintext (e.g. big photos) or excessive content(e.g. libraries) files here,even in an instant
# I-m a green hand,and this is just a play and clown project,do not use it in your production environment.
# If you are interested in who I am ,I-ll tell you that I am a Chinese.
# --!!!--the LICENCE has not been choosed, but probably `Apache 2.0 or MIT` license, for you to choose. If you see this line, please remind me to add the licence, thanks!
# only the that just compatible with both Apache 2.0 and MIT are allowed to use.
# e.g. PSFv2 MIT Public-Domain BSD-3-Clause-License,..., are allowed.
# e.g. GPLv2 GPLv3 LGPL AGPL Apache 2.0 ,..., these libraries and source codes are NOT allowed to use.

"""
```markdown
# DESIGN
### PINNED: refences, open source usage disclaiminer and acknowledgements
- ???[MUST add this!!!(:/licences)]
- licenses
    - .


### TODO LIST
- add the licenses of the library I have used.(IMPORTANT)

### dependences

### licence
- ???

###
- chain:
    - core (if-name-=-main -> router -> main -> core):
        -???




```
"""

################### BEGIN -ING of the code ###############################
"""
### global constants
"""
# metadata
PROGRAM_NAME = "scrodepiot" # do not delete;
VERSION = "v0.0.0.0" # do not delete;
AUTHOR = "zuozhixingzhe/digger/作止行者 (c) all rights reserved;" # do not delete;
LICENSE = "???" # do not delete;


"""
### import
"""

# `click`: BSD 3-Clause License; `click-help-colors`: MIT;
import click # BSD 3-Clause License; a command line arguments parser
from click_help_colors import HelpColorsGroup, HelpColorsCommand # MIT Licence

"""
### CoreProcesses
"""
class CoreProcesses:

    @click.group(
        cls=HelpColorsGroup,
        help_headers_color='magenta',  # title, e.g. `Options`
        help_options_color='cyan'    # options, e.g. `--help`
    )# generated-by-deepseek
    def clickDefaultGroup():
        pass # Just act as the group

    """
    the core task
    """
    @clickDefaultGroup.command()
    @click.argument('scriptpath', nargs = -1, type = click.Path(resolve_path = True)) # direct args; scriptpath ,filepath; we do not recieve more direct args; warning , many path args would come
    @click.option('--haha-h', is_flag = True, help = '???haha') #haha???
    @click.version_option(version = VERSION, prog_name = PROGRAM_NAME) # we need to use click-s own default method.
    @staticmethod
    def core(*,scriptpath,haha_h): # the key words must match the option name of `click`(`*`)
        """
        ???haha
        """
        """
        ### safety check
        """

        """
        ### check parameters
        """

        """
        ### ### ### ### ### ### ### ###
        THIS IS WHERE WE ARE
        """
        print(f'hello {scriptpath}')


def main():
    CoreProcesses.core()

def debug():
    print('PLEASE write your idea here \n:-)\n .')
    # write your idea here.

def router():
    # You could modify your own test or other logic or idea here, which would not easily break the main process of my program.
    # use `debug()` to switch to your debug content
    #main()
    # You could just use a single `main()` as default origin behavior.
    main()


if __name__ == '__main__':
    router()
################### END of the code ###############################

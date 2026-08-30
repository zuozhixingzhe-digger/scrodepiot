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
PROGRAM_HELP_DOC= f"""
        MANUAL:\n
        {PROGRAM_NAME}, {VERSION}, by {AUTHOR}. LICENSE:{LICENSE}\n
        ???haha\n
        You could use `./main.py --prompt-history-file=<histfilePath> -- <scriptPath> <args> ...` temporarily.
"""
# settings
ENCODING = "utf-8"
GRAMMER = r"""
    start: executable?            // beginning with a `?` makes the tree simple; `executable` is just a whole unit; only no or one `executable` is allowed.
    ?executable: statement+
    ?statement: debug
    ?debug: SYMBOL
    SYMBOL: /[A-Za-z_\-][A-Za-z0-9_\-]*/
    NUMERIC: /[0-9\-][A-Za-z0-9_\-]/
    KEYWORD: /\/[A-Za-z0-9_\-]*\/?/
    COMMENT: /#.*$/
    %ignore COMMENT
    //
    //
    //
    //
    //
    //
    ///////////////////////////////
""" ##############????????????FIXME TODO HACK
# The grammer just defines a `excutable`.



"""
### import
"""

try:
    # `click`: BSD 3-Clause License; `click-help-colors`: MIT;
    import click # BSD 3-Clause License; a command line arguments parser
    from click_help_colors import HelpColorsGroup, HelpColorsCommand # MIT Licence
    import prompt_toolkit # BSD 3-Clause License; interactive prompt tools
    from prompt_toolkit import prompt, PromptSession
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.formatted_text import ANSI
    import lark # ???HACK,LICENSE?!
    from lark import Lark, Tree, Token, Discard, Transformer
    from lark.exceptions import (
        UnexpectedToken,
        UnexpectedCharacters,
        UnexpectedEOF,
        VisitError,
        GrammarError,
        LarkError  # 所有异常的父类
    ) # --deepseekAI
    from lark.indenter import Indenter
    #
    import requests # ???HACK
    #import NoThisModule
except (ModuleNotFoundError, ImportError) as e:
    print(f"\x1b[0;31mError before start: Python Model may be not installed! Exited.({e})\x1b[0m")
    exit(1)


"""
### CoreProcesses
"""
class CoreProcesses:

    """
    ###
    """
    def corePositionDebugger():
        # Write what you want to test when `--debug` is added
        print("?????")
        print('PLEASE write your idea here \n:-)\n .')
        CoreProcesses.showSituation("haha???")
    """
    ### % Static Varibles
    """
    scriptContent = None # This may be VERY big, so solve it with caution, do not duplicate or do other things.CoreProcesses.scriptContent
    parser = None
    """
    ###
    """
    @click.group(
        cls=HelpColorsGroup,
        help_headers_color='magenta',  # title, e.g. `Options`
        help_options_color='cyan'    # options, e.g. `--help`
    )# generated-by-deepseek
    def clickDefaultGroup():
        pass # Just act as the group

    """
    ### % the core tasks
    """
    @clickDefaultGroup.command(help = PROGRAM_HELP_DOC)
    @click.argument('scriptpath', required = False, default = None, type = click.Path(resolve_path = True)) # direct args; scriptpath ,filepath; we do not recieve more direct args; warning , many path args would come
    @click.argument('argstoscript', nargs = -1, type = click.UNPROCESSED) # the args to throw to your own script to process
    @click.option('--prompt-history-file', type = click.Path(resolve_path = True), help = 'Specify the history IO file of interactive command prompt interface.Only the interactive prompt mode makes sense.')
    @click.option('--debug', is_flag = True, help = 'Toggle corePositionDebugger, as you could define whose action by modifying the Python source code.')
    @click.option('--haha-h', is_flag = True, help = '???haha') #haha???FIXME
    @click.version_option(version = VERSION, prog_name = PROGRAM_NAME) # we need to use click-s own default method.
    @staticmethod
    def distributor(*,scriptpath,argstoscript,prompt_history_file,debug,haha_h): # the key words must match the option name of `click`(`*`)
        """DO NOT USE THIS DOC!!!"""
        """
        ### %% FUNCTION:
            - This function will resolve args and allocate to interactive shell or script  reader
        """
        """
        ### %%% safety check TODO
        """
        """
        ### INIT
        """
        # Init lark
        CoreProcesses.parser = Lark(GRAMMER,parser = "lalr",)
        """
        ### %%% check parameters
            %%%% check script file and its arguments, route to interactive shell or a script reader(just execute).
                - Just as Deepseek said, the script file is normally in 200KiB, exceeeding is prohibited commonly. So, we assume the computer-s memory is enough to accomodate it. Thus we will take it all into the memory.
                -
                - TASKS:
                    - debugger
                    - file process
        """
        if debug:
            CoreProcesses.corePositionDebugger()
            return
        #print(scriptpath)
        if scriptpath is not None:
            try:
                with open(scriptpath, 'r', encoding=ENCODING) as f :
                    CoreProcesses.scriptContent = f.read()
                # release the file handler(maybe).
                CoreProcesses.scriptReader(argstoscript)
            except FileNotFoundError as e:
                CoreProcesses.showError(f"Sorry. The specified script is not found, and the program is terminated.～报告长官，没有发现命令信使，要开启雷达为您搜索一下吗？～({e})")
                return
            except IsADirectoryError as e:
                CoreProcesses.showError(f"Sorry. The specified script is not found, and the program is terminated. However, you have given me a boring directory and I was chuckling:)! ～朋友，咱们地球帝国这边再怎么有兵力，也奈何不了一个孤独的文件夹～({e})")
                return
            except PermissionError as e: # note: `click` has already solved this, and it is normally unable to reach now.
                CoreProcesses.showError(f"Sorry. You have no permission to get access to this script file, and the program is terminated. Maybe you could try `chmod +r ???(FIXME)` with CAUTION.～地球帝国紫禁城欢迎你的光临，请出示你的御制令牌～({e})") # FIXME
            finally:
                pass
        else: # Interactive
            CoreProcesses.interactiveCommandPrompt(historyPath=prompt_history_file)


    #
    #
    @staticmethod
    def interactiveCommandPrompt(historyPath:str):
        # TODO: histfile
        if historyPath is not None:
            try:
                session = PromptSession(history = FileHistory(historyPath), multiline=True)
            except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
                # Not as the script-file. The history-file is not important. We could run without it.
                CoreProcesses.showWarning(f"Could not open the prompt history file specified. Would run without it, and the history would not be saved. ({e})")
                session = PromptSession(multiline=True)
                # A little error, could not resolve the history file.
        else:
            session = PromptSession(multiline=True) # Common, the user just didn-t give us the history. So we do not bind to a history file.
        while True:
            try:
                userInput = session.prompt(
                    ANSI("\x1b[0;35m- \x1b[0m"),
                    rprompt = ANSI("\x1b[0;2mAlt-Enter:submit\x1b[0m"), # TODO: we could add more functions in the future
                )
                CoreProcesses.interpreter(userInput) # Send to interpreter.
                #
                """
                ### ### ### ### ### ### ### ### HACK TODO HACK HACK TODO HACK
                THIS IS WHERE WE ARE; WE TEST!
                """
            except EOFError: # Ctrl-D
                break # Will directly exit the program.
            except KeyboardInterrupt: # Ctrl-C
                CoreProcesses.showSituation("Python-KeyboardInterrupt-when-input")
                continue
    #
    @staticmethod
    def scriptReader(argstoscript):
        if CoreProcesses.scriptContent is None:
            raise NoScriptContentPot("") # FIXME ???
        else:
            print(CoreProcesses.scriptContent)
            CoreProcesses.showSituation(f"({argstoscript})") # TODO: args is not used.
            # We should pre-process the script first. TODO: But this is crazy, let-s throw it to interpreter now, fix it in the future.
            CoreProcesses.interpreter(CoreProcesses.scriptContent)

    #
    @staticmethod
    def interpreter(command:str): # Accept a `ExecutableBlock` once a time, which could be excuted independently.
        """
        ###
        .
        .
        - :
            - file/user-input > ExecutableBlock > Command
        """
        if CoreProcesses.parser is None: # Fix the situation when the parser is not initialised.
            CoreProcesses.parser = Lark(GRAMMER,parser = "lalr",)
        try:
            CoreProcesses.showSituation(f"(\n{CoreProcesses.parser.parse(command).pretty}\n)")
            #################?????????????????TODOCoreProcesses.parser = Lark(GRAMMER,parser = "lalr",)
        except (UnexpectedCharacters,UnexpectedToken,UnexpectedEOF) as e:
            raise CoreProcesses.TheAuthorIsAClownPot(e) #######???FIXIT
    #
    """
    ### % utilities
    """
    # `print()` is not allowed to use directly in this project, except debugging or specific methods.
    @staticmethod
    def showError(msg:str): # TODO: we could add logs in the future.Also clean control-chars.
        print(f"\x1b[0;31m[E: {msg}]\x1b[0m")
    @staticmethod
    def showWarning(msg:str):
        print(f"\x1b[0;33m[W: {msg}]\x1b[0m")
    @staticmethod
    def showSituation(msg:str): # show info
        print(f"\x1b[0;36m[S: {msg}]\x1b[0m")
    #
    class Pot(RuntimeError): # “甩锅”，raise pot :). the root Exception of mine.
        """ HACK """
        pass
    class TheAuthorIsAClownPot(Pot): # 作者就是个小丑！当你看到这个被抛出的时候，作者应该挨骂的，应该的。。。
        """ HACK """
        pass
    class NoScriptContentPot(Pot):
        """ HACK """
        pass



def main():
    CoreProcesses.distributor()

def starterDebug():
    print('PLEASE write your idea here \n:-)\n .')
    # write your idea here.

def starterRouter():
    # This is the router on which we start.
    # You could modify your own test or other logic or idea here, which would not easily break the main process of my program.
    #starterDebug
    # use `starterDebug()` to switch to your debug content
    #main()
    # You could just use a single `main()` as default origin behavior.
    main()


if __name__ == '__main__':
    starterRouter()
################### END of the code ###############################

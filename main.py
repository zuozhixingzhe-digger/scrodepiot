#!/usr/bin/env python3
# --digger-created--20260725
# zuozhixingzhe/digger/作止行者 (c) all rights reserved; LICENSE: `Apache 2.0 OR MIT`
# Contact me at `321323006+zuozhixingzhe-digger@users.noreply.github.com`
# scrodepiot:main.py
# this is just the main process -- all the contents are here(except when we make it too huge to make it in a file )
# --!!!--GIT ENABLED --DO NOT put any sensitive (e.g. key) or non-plaintext (e.g. big photos) or excessive content(e.g. libraries) files here,even in an instant
# I-m a green hand,and this is just a play and clown project,do not use it in your production environment.
# If you are interested in who I am, I-ll tell you that I am a Chinese.
# only the that just compatible with both Apache 2.0 and MIT are allowed to use.
# e.g. PSFv2 MIT Public-Domain BSD-3-Clause-License,..., are allowed.
# e.g. GPLv2 GPLv3 LGPL AGPL Apache 2.0(Cause Collision with GPLv2),..., these libraries and source codes are NOT allowed to use.

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
LICENSE = "Apache 2.0 OR MIT" # do not delete;
PROGRAM_HELP_DOC= f"""
        MANUAL:\n
        {PROGRAM_NAME}, {VERSION}, by {AUTHOR}. LICENSE:{LICENSE}\n
        ???haha\n
        You could use `./main.py --prompt-history-file=<histfilePath> -- <scriptPath> <args> ...` temporarily.
""" # do not delete;
# settings
ENCODING = "utf-8" # do not delete;
GRAMMAR = r"""
    //

    // --- declaration and import
    %import common.WS_INLINE
    %import common.END_OF_FILE -> EOF
    %declare _INDENT _DEDENT    // Virtual tags

    // --- syntax
    start: executable?            // beginning with a `?` makes the tree simple; `executable` is just a whole unit; only no or one `executable` is allowed.
    executable: statement+        // TODO: You could write ?excutable here(when the rules allows).
    statement: ((expression ASSIGNCOMMAND expression) | (CALL expression) | ("%" expression)) (_NL)   // ;. WARNING TODO: statement =/= expression; TODO `_NL` problem is to solve!
    debugthing: REGEXMATCHER|REGEXREPLACER|URL|TRUE|POWER|PLUS|MINUS|MULTIPLY|DEVIDE|COMMA|DOT|_INDENT|_DEDENT|_NL|integrated
    expression: debugthing       // |bracketexpression|(expression POWER expression)
    level: "-undefined-2389j38eh"      // TODO??????????
    comparechain: level comparer level (comparer level)*  // Like Python(`1 < x < 10`). Thank Python to give me the idea!

    // --- primary elements
    comparer: LESSTHAN | GREATERTHAN | LESSOREQUAL | GREATEROREQUAL | EQUAL | NOTEQUAL

    // --- integrated elements
    integrated: bracketexpression | symbol | string | NUMERIC
    bracketexpression: (LPAREN expression  RPAREN (COMMA expression)* (COMMA)?)
        | (LBRACKET expression RBRACKET (COMMA expression)* (COMMA)?)
        | (LBRACE expression RBRACE (COMMA expression)* (COMMA)?)  // That-s strange: the lark grammar, cannot be `xxx |` ,but `| xxx`.  ; Note: lark does not support`()*?` like regex; `()` is bad; `{a}` `(a,)` `(a,b)` `[a,b,c]`, ..., are good;
    //    the keyword is so many (and may increase in the future), that we use a `-` prefix to tell between symbols and keywords. Brackets are required to use when it-s not an obvious natural usage( `+` `*` `**` `==`, etc.);
    symbol: (TREATASSYMBOL string) | SYMBOL       // `$ "a" "b"` is ok ,just as `ab`
    string: (ESCAPEDSTRING | RAWSTRING)+          // `'...'`(simple) `'...' x '...'`(format) are both OK; Note: A “String” would directly eat a whole string list, including`ESCAPEDSTRING | RAWSTRING`;

    // --- TERMINALS
    CALL: "@" | "-call"| "-at"    // Special! `-call function` | `@function` | `function()`(`()`->`[ ]` `{}` is allowed) | `function(<args>)` | `function <args>` is allowed, but `function` is not allowed! Otherwise, the parser could not identify whether it is an expresssion(illeagal to be a statement) or a statement;
    TRY: "-try"          // try-but(`except`)-normally(`else`)-always(`finally`)
    BUT: "-but"
    NORMALLY: "-normally"
    ALWAYS: "-always"
    SHOCK: "-shock"  // (`raise`)You must catch a `shock`, otherwise, the program will terminate.
    SHOUT: "-shout"   // Special! You could choose not to solve `shout`, the program will continue; if you use `but` to catch it, then, if you already solve this, then you could choose `-next`(come back to the original position, default, nothing would happen, and `normally` is to be executed) or `-leave`(do not execute the `normally`, and `always` is the last what we do, before leave the block.).
    DISCUSS: "-discuss"   // discuss-case (is like C-s switch-case); `case` is thrown away;（case这个词不用写哦），注意不是when（if）语句，
    IF: "-if"   // You could get rid of `if`, `<condition><return><indented block>` is a condition(if) statement; like Python, there is `x -if y -else z`.
    ELSE: "-else"    // `-else` or `-else <condition>`(`elif <condition>:`)
    LOOP: "-loop"       // `<condition> -loop` or `-loop`(`while True:`)
    ITERATE: "-iterate"    // (`for`), `-iterate x-iterable -as y-new-var -when condition`.
    LABEL: "-label"    // `<condition> -label <label1>`(`-when` statement), `-next/-leave <label1>`;
    NEXT: "-next"  // (`continue`)
    LEAVE: "-leave"   // (`break`)   next and leave, just as the queue:).
    PASS: "-pass" | "-nothing-to-do"
    RETURN: "-return" | "-ret"
    WAIT: "-wait"  // Will wait until a condition(time or others), give out the CPU time.
    PUBLIC: "-public" | "-P"
    PRIVATE: "-private" | "-p"
    WRITABLE: "-writable" | "-R"
    READONLY: "-readonly" | "-read-only" | "-unwritable" | "-r"
    PROCESSTYPE: "-process" | "-proc"
    BOOLEANTYPE: "-boolean" | "-bool"
    INTEGERTYPE: "-integer" | "-int"
    REALTYPE: "-real"
    COMPLEXTYPE: "-complex" | "-cplx"
    CATALOGTYPE: "-catalog"    // (`dictionary` and `object`)
    CLUSTERTYPE: "-cluster"      // Js-s array
    TENSORTYPE: "-tensor"       // Special use for math-calculate arrays, must be in the same type.
    STRINGTYPE: "-string"
    NULL: "-null" | "-Null" | "-none" | "-None"
    TRUE: "-true" | "-True" | "-t" | "-yes" | "-y" | "-on" | "-v" | "-V"   // Victory(v)/Cross(x) is allowed
    FALSE: "-false" | "-False" | "-f" | "-no" | "-n" | "-off" | "-x" | "-X"
    EXACTDEVIDE: "-ed" "-exactly-devide-by"   // Python `//`.“整除”，不知道英文怎么说？
    MOD: "-mod"      // Python `%`
    ABS: "-abs"
    RE: "-Re" | "-re"
    IM: "-Im" | "-im"
    ARG: "-arg"     // 辐角主值
    SIN: "-sin" | "-sine"
    COS: "-cos" | "-cosine"
    TAN: "-tan" | "-tangent"
    // No `f"..."` as Python, we use `"..." expression "..."` instead; `="..."` is a raw String;
    RAWSTRING.4096: /=`[^`]*?`/          // Note: `XYZ.1234` is able to explictly define the priority, and in lark, a greater number means a prior order; Collision with `=`(!), TODO!; Non-Greedy(Lazy, (`*?`), Otherwise, will match until the last Quote, and the quote to close the string is of No Sense!),Important(!);
        | /='[^']*?'/
        | /="[^"]*?"/
        | /=```[\s\S]*?```/
        | /='''[\s\S]*?'''/
"""  r'''
        | /="""[\s\S]*?"""/
'''  r"""
    ESCAPEDSTRING.2560: /`(?:[^\\]|\\[^\n])*?[`$]/       // .;(`Shift/Reduce conflict` (maybe) with RAWSTRING if `[^=]` is not added; However, it would match and eat a char! so we do not use.);
        | /'(?:[^\\]|\\[^\n])*?['$]/
        | /"(?:[^\\]|\\[^\n])*?["$]/
        | /```(?:[^\\]|\\[^\n])*?```/
        | /'''(?:[^\\]|\\[^\n])*?'''/
"""  r'''
        | /"""(?:[^\\]|\\[^\n])*?"""/
'''  r"""
    SYMBOL: /[A-Za-z_][A-Za-z0-9_\-]*/
    NUMERIC: /[\-\+]?[0-9]\.?[A-Za-z0-9_\-\+]*\.?/      //maybe we should enhance it with `1e-3` `0.1` `.1`, `0date-2026-09-02` etc.Greedy?(TODO)
    // EXPANDEDKEYWORD: /-[A-Za-z0-9_\-]+/       // a single `-` is not included; the keywords are the additional, not the primary;
    URL: /\<?(?:https?|file|s?ftp):\/\/[^\(\)\[\]\{\}<>`"\|\s]*\>?/
        | /\<(?:https?|file|s?ftp):\/\/.*\>/
        // Special! Directly write your URL! You could write directly or put into `<>`, such as `<https://www.example.com>` (which would write your words more freely, such as `()[]...`).(No space(use `%20` instead), \n, tab, `()[]{}|\ <>"`, ..., are allowed; use `%` to escape instead). .
    REGEXMATCHER:  /\/(?:[^\/\\]|\\.)*\/[gimuy]*/             // to avoid colission with `/**/` & `//`, we need to take `*` away from the next from `/`(regex does not allow `*` to start, according to my knowledge(?)); Just tell the boarder of regex, do not check its grammar; `(?:)` does not catch the group in regex; Deepseek wrote it; regular expression matcher;
    REGEXREPLACER: /s\/.*\/.*\//   // ???????????TODO //replacer, like GNU sed.
    PLUS: "+" | "-plus" | "-add" | "-positive"       // Special! An operator could be replaced as a keyword.
    MINUS: "-" | "-minus" | "-sub" | "-negative"
    MULTIPLY: "*" | "-multiply" | "-star"
    DEVIDE: "/" | "-devide" | "-slash"
    POWER: "**" | "^" | "-power"
    LESSTHAN: "<" | "-less-than" | "-lt"
    GREATERTHAN: ">" | "-greater-than" | "-gt"
    LESSOREQUAL: "<=" | "-less-than-or-equal-to" | "-le"
    GREATEROREQUAL: ">=" | "-greater-than-or-equal-to" | "-ge"
    EQUAL: "==" | "-equal-to" | "-eq"
    NOTEQUAL: "=/=" | "-not-equal-to" | "-ne"
    ASSIGNINEXPRESSION: ":=" | "-gets-together"
    AND: "&" | "&&" | "-and" | "-And"
    OR:  "|" | "||" | "-or"  | "-Or"
    NOR: "-nor" | "-Nor"
    NOT: "~" | "-not" | "-Not"
    NAND: "-nand" | "-Nand"              //  `x -nand y` instead of `!(x & y)`
    XOR: "-xor" | "-Xor"
    EZ: "-ez" | "-Ez"        // Equals zero
    NEZ: "-nez" | "-Nez"     // Not euals zero
    DOT: "." | "-dot"
    COMMA: "," | "-comma"
    LPAREN: "(" | "-lparen"
    RPAREN: ")" | "-rparen"
    LBRACKET: "[" | "-lbracket"
    RBRACKET: "]" | "-rbracket"
    LBRACE: "{" | "-lbrace"
    RBRACE: "}" | "-rbrace"
    NEXTSTATEMENT: ";" | "-next-statement"      // `;` Force to make it to the next statement
    ASSIGNCOMMAND: "=" | ":" | "-gets"   // assign-command(`=`) and assign-operator(`:=`) is different.
    TRANSPORTTORIGHTCOMMAND: ">>>" | "-transports-to"  // Special!
    TRANSPORTTOLEFTCOMMAND: "<<<" | "-transports-from"
    TREATASSYMBOL: "$" | "-as-symbol"      // just as `$ "abc?xyz"`(the space between `$` and the string is a optional),will treat as a symbol
    COMMENT: /\/\/.*/ | /\/\*[\s\S]*\*\// | "!" | "?" | /#.*$/               // just bang(`#`)-comment, c-style (`//` , `/**/`), and single sign-comment-char(Special! A single `!` or `?` is a comment); (`x'''...'''`is not included(TODO: THIS could add directly!!!));

    // --- ignore and other definations
    %ignore COMMENT
    %ignore WS_INLINE
    CONTINUED_LINE: /\\\r?\n[\x20\t]*/               //   `\<next-line>` to ignore the new-line tag. Just eat the `\n` and the space and tab(space and tab are not resolved by WS_INLINE).
    %ignore CONTINUED_LINE
    _NL: /\r?\n[\x20]*/           // the new line without which would be treated as the next-statement token. Only space(`\x20`) is legal now.
    //
    //
    //
    //
    //
    //
    ///////////////////////////////
""" # do not delete; ##############????????????FIXME TODO HACK
# The grammer just defines a `executable`, one or zero `executable` is allowed.
#  （我自己的注释：见“test1.py”那个，可以进行严格的测试）
"""
TODO:my-logs:
    - a -calls adsfd
    .
    Unexpected token Token('MINUS', '-') at line 1, column 3.
    Expected one of:
            * ASSIGNCOMMAND
    Previous tokens: [Token('SYMBOL', 'a')]

"""
#########################################################################
"""
Terminals-  Order


"""


"""
### import
"""

try:
    import click # BSD 3-Clause "New" or "Revised" License, Copyright 2014 Pallets.; a command line arguments parser
    from click_help_colors import HelpColorsGroup, HelpColorsCommand # MIT Licence, Copyright (c) 2016 Roman Tonkonozhko.
    import prompt_toolkit # BSD 3-Clause "New" or "Revised" License, Copyright (c) 2014, Jonathan Slenders.; interactive prompt tools
    from prompt_toolkit import prompt, PromptSession
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.formatted_text import ANSI
    import lark # MIT License, Copyright © 2017 Erez Shinan.
    from lark import Lark, Tree, Token, Discard, Transformer
    from lark.exceptions import (
        UnexpectedToken,
        UnexpectedCharacters,
        UnexpectedEOF,
        VisitError,
        GrammarError,
        LarkError  # 所有异常的父类--deepseekAI
    ) # --deepseekAI
    from lark.indenter import Indenter  # Python-like Indention rules
    #
    import httpx # HACK LICENSE???
    #import NoThisModule
except (ModuleNotFoundError, ImportError) as e:
    print(f"\x1b[0;31mError before start: Python Module may be not installed! Exited.({e})\x1b[0m")
    exit(1)


"""
### CoreProcesses
"""
class CoreProcesses:

    """
    ###
    """
    @staticmethod
    def corePositionDebugger():
        # Write what you want to test when `--debug` is added
        print("?????")
        print('PLEASE write your idea here \n:-)\n .')
        CoreProcesses.showSituation("haha???")
    """
    ### % Static Varibles
    """
    scriptContent = None # This variable may be VERY big, so solve it with caution, do not duplicate or do other things.CoreProcesses.scriptContent
    parser = None

    """
    ###
    Indent solver
    """
    class UnifiedIndenter(Indenter):  # （统一的Unified）
        # TODO:（原则上不允许tab的，根本就不允许tab作为缩进）
        NL_type = '_NL'  # New Line（NL），defined in LARK GRAMMAR
        INDENT_type = '_INDENT'
        DEDENT_type = '_DEDENT'
        OPEN_PAREN_types = []   # TODO: 换行里的没有闭合的括号要处理哦,问问deepseek
        CLOSE_PAREN_types = []
        tab_len = 4
    """
    ###
    """
    @staticmethod
    def larkInit():
        CoreProcesses.parser = Lark(
            GRAMMAR,
            parser = "lalr",
            #strict = True,   # If there are ambigious grammar, the parser would reject parsing. However, without library `lark[interegular]`, it will not work!
            regex = False,   # For license reasons, regex(Apache2.0?) is not allowed to use.
            postlex = CoreProcesses.UnifiedIndenter(),
        )
    """
    ###
    """
    @click.group(
        cls=HelpColorsGroup,
        help_headers_color='magenta',  # title, e.g. `Options`
        help_options_color='cyan'    # options, e.g. `--help`
    )# generated-by-deepseek
    @staticmethod
    def clickDefaultGroup():
        pass # Just act as the group

    """
    ### % the core tasks
    """
    @clickDefaultGroup.command(help = PROGRAM_HELP_DOC)
    @click.argument('scriptpath', required = False, default = None, type = click.Path(resolve_path = True)) # direct args; scriptpath ,filepath; we do not recieve more direct args;
    @click.argument('argstoscript', nargs = -1, type = click.UNPROCESSED) # the args to throw to your own script to process
    @click.option('--prompt-history-file', type = click.Path(resolve_path = True), help = 'Specify the history IO file of interactive command prompt interface.Only the interactive prompt mode makes sense.')
    @click.option('--execute-directly', type = str, default = None, help = f'Directly execute the ({PROGRAM_NAME}) command after the option')
    @click.option('--debug', is_flag = True, help = 'Toggle corePositionDebugger, as you could define whose action by modifying the Python source code.')
    @click.option('--haha-h', is_flag = True, help = '???haha') #haha???FIXME
    @click.version_option(version = VERSION, prog_name = PROGRAM_NAME) # we need to use click-s own default method.
    @staticmethod
    def distributor(*,scriptpath,argstoscript,prompt_history_file,execute_directly,debug,haha_h): # the key words must match the option name of `click`(`*`)
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
        CoreProcesses.larkInit()
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
        # Priority: script > direct-execute-command > interactive
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
                CoreProcesses.showError(f"Sorry. You have no permission to get access to this script file, and the program is terminated. ???Maybe you could try `???chmod +r ???(FIXME)` with CAUTION.～地球帝国紫禁城欢迎你的光临，请出示你的御制令牌～({e})") # FIXME
            finally:
                pass
        elif execute_directly is not None:
            raise CoreProcesses.TheAuthorIsAClownPot("🤡")
            ...# TODO: add this
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
                if userInput and not userInput.endswith('\n'):
                    # The unix file standard and my grammar both requires a `\n` at the end, but the console does not.
                    sentCommand = userInput + '\n'
                else:
                    sentCommand = userInput
                CoreProcesses.interpreter(sentCommand) # Send to interpreter.
                #
                """
                ### ### ### ### ### ### ### ### HACK TODO HACK HACK TODO HACK
                THIS IS WHERE WE ARE; WE TEST!
                """
            except CoreProcesses.ScriptSyntaxErrorPot as e: # HACK! Just show the error now. Need to modify inthe future.
                CoreProcesses.showError(f"Syntax error.(\n{e}\n)")
                continue
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
    def interpreter(command:str): # Accept a `ExecutableBlock` once a time, which could be excuted independently. Interprete it, and execute it.
        """
        ###
        .
        .
        - :
            - file/user-input > ExecutableBlock > Command
        """
        if CoreProcesses.parser is None: # We fix the situation when the parser is not initialised.
            CoreProcesses.larkInit()
        try:
            CoreProcesses.showSituation(f"(\n{CoreProcesses.parser.parse(command).pretty()}\n)")
            #################?????????????????TODO
        except (UnexpectedCharacters,UnexpectedToken,UnexpectedEOF) as e:
            # TODO: We need to solve the grammar error, and show to the user friendly.
            raise CoreProcesses.ScriptSyntaxErrorPot(e)
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
    class ScriptSyntaxErrorPot(Pot):
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



"""
想法：
- 一切可变，不要束缚于形式，比如引号，括号，缩进，关键字的可扩展性等
"""

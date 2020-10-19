## Other, more comprehensive cheatsheets
http://www.unix-manuals.com/refs/vi-ref/vi-ref.htm

https://devhints.io/vim

## Observations
Lines starting with `:` require ESC

Lines starting with `^` require CTRL

## File
`:wq`	Save and exit

`:q!`	Exit without saving

## Search
`:/word`	Search a word

`:n` Search next occurrence

## Modes
`i`	insert mode

`v` visual mode

`V` visual line mode

`ESC`/`^c`/`^[` exit mode 

### Visual mode
`d`/`x` delete

`y` yank(copy)

`s` replace

## Cursor movement
### Line
`0` - beginning of the line

`$` - end of the line

`:0` - first line

`:<n>` - nth line, e.g.`:3` - 3rd line

`:$` - last line

### Screen
`^u` - up (half a screen)
`^d` - down (half a screen)
`^r` - redraw screen

## Clipboard
`dd`/`d<n>` delete (cut) one line/n lines

`yy`/`y<n>` yank (copy) one line/n lines
`p` paste

`P` paste before

## Editing
`:u` undo

`:s/find_text/replace_text/`	Find and replace a string ( only current occurence )

`%s/find_text/replace_text/g`	Replaces all occurrences of that string in the text

## Operators
`>` indent right

`<` indent left

## Misc
`:set ff=unix` Convert Windows line endings to Unix line ending

`.` repeat last command

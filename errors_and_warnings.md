# Windows git "warning: LF will be replaced by CRLF", is that warning tail backward?
warning: LF will be replaced by CRLF.

Depending on the editor you are using, a text file with LF wouldn't necessary be saved with CRLF: recent editors can preserve eol style. But that git config setting insists on changing those...

Simply make sure that (as I recommend here):

```
git config --global core.autocrlf false
```
That way, you avoid any automatic transformation, and can still specify them through a .gitattributes file and core.eol directives.
>source: https://stackoverflow.com/questions/17628305/windows-git-warning-lf-will-be-replaced-by-crlf-is-that-warning-tail-backwar

#   "Please enter a commit message for your changes"
The first line before

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
is precisely there for adding your commit message.

You press i, and you enter insert mode. You can navigate around the text and insert what ever you want. When done, press Esc. This makes you exit insert mode. Next you have to press :wq, which means to write and quit.

This will save your commit message.
>source:https://stackoverflow.com/questions/73012357/please-enter-a-commit-message-for-your-changes
>Note: I noticed that this error happen when you use git commit whithout adding a message
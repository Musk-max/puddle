# Windows git "warning: LF will be replaced by CRLF", is that warning tail backward?
warning: LF will be replaced by CRLF.

Depending on the editor you are using, a text file with LF wouldn't necessary be saved with CRLF: recent editors can preserve eol style. But that git config setting insists on changing those...

Simply make sure that (as I recommend here):

```
git config --global core.autocrlf false
```
That way, you avoid any automatic transformation, and can still specify them through a .gitattributes file and core.eol directives.
>source: https://stackoverflow.com/questions/17628305/windows-git-warning-lf-will-be-replaced-by-crlf-is-that-warning-tail-backwar

#

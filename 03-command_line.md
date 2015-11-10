# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

-pwd: print working directory
-hostname:	my computer's network name
-mkdir:	make directory
-cd:	change directory
-ls:	list directory
-rmdir:	remove directory
-rm: 	remove file
-pushd:	push directory
-popd:	pop directory
-cp:	copy a file or directory
-mv:	move a file or directory
-less:	look at contents of a file
-cat:	print the whole file
-xargs:	execute arguments
-find:	find files
-grep:	find things inside files
-man:	read a manual page
-apropos:	find what man page is appropriate
-env:	look at your environment
-echo:	print some arguments
-export:	export/set a new environment variable
-exit:	exit the shell

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

-"ls" lists the contents of  a directory. 
-"ls -a" includes entries in the directory beginning with "."
-"ls -l" lists the contents of a directory with each file in long format (file mode, number of
     links, owner name, group name, number of bytes in the file, abbreviated month, day-of-month file was
     last modified, hour file last modified, minute file last modified, and the pathname)
-"ls -lh" lists the contents of a directory in long format with the file size in Human readable format (e.g., 1K 234M 2G)
-"ls -al" is a meaningful command since it will output all files in long format, including those that begin with "."

---


---

What does `xargs` do? Give an example of how to use it.

"xargs" executes a command from standard input. 
-Example:
-$ echo Print two items on each line | xargs -n 2
-Print two
-items on
-each line


---


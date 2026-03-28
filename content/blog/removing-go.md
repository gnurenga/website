Title: Uninstalling go from Debian
Date: 2026-03-22 7:12 PM
Tags: Blog, Debian, go-lang

## Uninstalling go from the GNU/Linux system

1. We need to know binary path of `go`
~~~~
$ go version
go version go1.19.8 Linux/amd64
$ which go
/usr/bin/go
~~~~

2. We also need to know the linked libraries for go. Though below is a soft link to go binary. It gives where the libraries present.

~~~~
$ file /usr/bin/go
/usr/bin/go: symbolic link to ../lib/go-1.19/bin/go
~~~~

3. Above gives the symbolic link to go binaries but there is one more path also I found in the system

~~~~
$ cd /usr/lib/go
$ ls
api  bin  misc  pkg  src  test  VERSION
$ cat VERSION 
go1.19.8 $ cd ..
~~~~

4. we need to delete below paths

~~~~
/usr/lib/go
/usr/lib/go-1.19
~~~~

5. Final cleaning

~~~~
$ sudo rm -rf go/
$ sudo rm -rf go-1.19/
~~~~

## Conclusion

I want to upgrade to latest go version. Mine is pointing to older version. Above steps specific to my Debian system. Binaries and libraries path may vary according to the GNU/Linux distribution we use. We can start by using `which go` to understand what to clean.

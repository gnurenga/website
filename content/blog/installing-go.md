Title: Installing new go version
Date: 2026-03-22 7:26 PM
Tags: Blog, go, Installation 

## Installing go

In the previous article we removed GO from GNU/Linux Debian Distribution.
In this article we are going to see how we can Install new go version

1. The official document give below command. But that is not working in my system.

~~~~
$ rm -rf /usr/local/go && tar -C /usr/local -xzf go1.26.1.linux-amd64.tar.gz
~~~~

2. Because user doesn't have permission to remove /usr/local/go

3. I have modified the above command to use `sudo`.
Also you need to give the right download path in my case `~/Downloads/go1.26.1.linux-amd64.tar.gz`
~~~~
$ sudo  rm -rf /usr/local/go && sudo tar -C /usr/local -xzf ~/Downloads/go1.26.1.linux-amd64.tar.gz
~~~~

4. After running above command still I am not able to run `go`. why ?
Let me see the error. The error says go command not found.
Though we installed shell unable to detect the location of `go`.
i.e. go installation path or the go binary path is not visible to shell.
~~~~
$ go
bash: go: command not found
$ 
~~~~

5. How do we make shell to locate the go binaries ?. We need to add the go installation path to the
shell `PATH` environment variable.

~~~~
$ export PATH=$PATH:/usr/local/go/bin
~~~~

6. But it will be available only to the current shell session. That means after you close and reopen a terminal 
the environment will be loss-ed. We have to make it permanent by adding the above value to `$HOME/.profile`.
Then run,
 
~~~~
$ source $HOME/.profile
~~~~

From next login `go` will be available system wide. You can also add the command in step 5 in `.bashrc`.


Title: Yocoto Bitbake Cheat Sheet
Date: 2016-04-27 11:02
Tags: markdown, Blog 


## About Yocto
Yocto is an opensource embedded linux build system.
We can maintain software packages as layers in Yocto.
Yocto almost support all opensource build tools, download sources from
various version control repositories and ftps sites.
Yocto supports different packages used in linux distributions like deb,rpm,ipk,cpio.

## Bitbake
Bitbake is tool written in python, used in Yocoto build system.
Using bitbake we can build a custom Embedded Linux distro.
This article gives you some of the useful command we execised during
our project.

## The bitbake Useful commands

### Cleaning a build

~~~~
bitbake -c <package-name or recipe name>
bitbake -c cleansstate core-image-sato
~~~~

### Dependency explorer

~~~~
bitbake -g <core-image-sato> -u depexp
~~~~

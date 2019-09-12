# OpenGLTemplate
A cross-platform template for building a OpenGL program with SCons and Conan.

## Overview
The template uses GLEW and GLFW for OpenGL programming. Installations of these libraries is handled by Conan, a C++ package 
manager. The build system used is SCons. This setup allows users to utilize the template in various 
platforms with ease. On Windows, however, it works best with Cygwin or MinGW.

## Build Instructions
First of all, install [SCons](https://scons.org/) and [Conan](https://conan.io/) and any other softwares that they require 
to run. 

Create a build directory:
```
mkdir build
```

Download and install GLEW and GLFW with Conan:
```
cd build
conan install ..
cd ..
```

The steps above only need to be done once. To build your program, run:
```
scons
```
in the top directory, the one that contains `SConstruct`.

To clean, simply run:
```
scons -c
```

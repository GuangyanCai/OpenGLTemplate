from conans import ConanFile
import platform

class OpenGL(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'glfw/3.3@bincrafters/stable', 'glew/2.1.0@bincrafters/stable'
    generators = 'scons'
    if platform.system() == 'Windows':
        default_options = {'glfw:shared': True, 'glew:shared': False}

    def imports(self):
        if platform.system() == 'Windows':
            self.copy('*.dll', dst='..', src='bin')
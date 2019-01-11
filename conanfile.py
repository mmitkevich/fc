from conans import ConanFile, CMake, tools


class fcConan(ConanFile):
    name = "eos-fc"
    version = "master"
    license = "MIT"
    author = ""
    url = "git@github.com:mmitkevich/fc.git"
    description = ""
    topics = ("fc", "boost", "eos")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone -b eosio https://github.com/mmitkevich/fc.git")
        self.run("cd fc && git submodule init && git submodule update")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["TOOLCHAIN"] = "clang" 
        cmake.definitions["CMAKE_MODULE_PATH"] = "CMakeModules"
        cmake.configure(source_folder="fc")
        cmake.build()

        #Explicit way:
        
        #self.run('cmake %s %s'
        #          % (self.source_folder, cmake.command_line))
        #self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fc"]

    def requirements(self):
        self.requires("boost/1.67.0@conan/stable")
        self.requires("OpenSSL/1.0.2o@conan/stable")
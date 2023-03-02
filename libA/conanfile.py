from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class LibAConan(ConanFile):
    name = "libA"
    version = "1.0.0"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    
    requires = ("libX/1.0.0", "libY/1.0.0")
    generators = ("CMakeDeps", "CMakeToolchain")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libA"]

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class AppConan(ConanFile):
    name = "app"
    version = "1.0.0"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    requires = ("libA/1.0.0")
    generators = ("CMakeDeps", "CMakeToolchain")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

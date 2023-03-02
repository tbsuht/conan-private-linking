cmake_minimum_required(VERSION 3.15)
project(libA CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/generators)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/generators)

find_package(libX REQUIRED)
find_package(libY REQUIRED)

add_library(libA src/libA.cpp)

target_include_directories(libA PUBLIC include)

target_link_libraries(libA PRIVATE libX::libX libY::libY)

set_target_properties(libA PROPERTIES PUBLIC_HEADER "include/libA.h")

install(TARGETS libA)

cmake_minimum_required(VERSION 3.15)
project(libX CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/generators)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/generators)

add_library(libX src/libX.cpp)

target_include_directories(libX PUBLIC include)

set_target_properties(libX PROPERTIES PUBLIC_HEADER "include/libX.h")

install(TARGETS libX)

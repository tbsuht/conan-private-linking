cmake_minimum_required(VERSION 3.15)
project(libY CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/generators)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/generators)

add_library(libY src/libY.cpp)

target_include_directories(libY PUBLIC include)

set_target_properties(libY PROPERTIES PUBLIC_HEADER "include/libY.h")

install(TARGETS libY)

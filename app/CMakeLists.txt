cmake_minimum_required(VERSION 3.15)
project(app-overlay LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/generators)
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/generators)

add_subdirectory(src)

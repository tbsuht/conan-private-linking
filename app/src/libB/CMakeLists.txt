cmake_minimum_required(VERSION 3.15)
project(libB CXX)

find_package(libA REQUIRED)

add_library(libB SHARED libB.cpp)

target_include_directories(libB PUBLIC ../../include)

target_link_libraries(libB PRIVATE libA::libA)

set_target_properties(libB PROPERTIES PUBLIC_HEADER "include/libB.h")

install(TARGETS libB)

cmake_minimum_required(VERSION 3.15)
project(app CXX)

add_executable(app app.cpp main.cpp)

target_include_directories(app PUBLIC ../../include)

target_link_libraries(app PRIVATE libB)

install(TARGETS app)

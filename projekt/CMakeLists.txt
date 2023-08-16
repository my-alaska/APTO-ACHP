cmake_minimum_required(VERSION 3.19)
project(projekt C)

set(CMAKE_C_STANDARD 11)

add_executable(projekt solution1.c)
add_executable(projekt2 solution2.c)
add_executable(projekt3 main.c)
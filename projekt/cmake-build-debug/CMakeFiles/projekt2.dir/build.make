# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/projekt2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/projekt2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/projekt2.dir/flags.make

CMakeFiles/projekt2.dir/solution2.c.obj: CMakeFiles/projekt2.dir/flags.make
CMakeFiles/projekt2.dir/solution2.c.obj: ../solution2.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/projekt2.dir/solution2.c.obj"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\projekt2.dir\solution2.c.obj -c C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\solution2.c

CMakeFiles/projekt2.dir/solution2.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/projekt2.dir/solution2.c.i"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\solution2.c > CMakeFiles\projekt2.dir\solution2.c.i

CMakeFiles/projekt2.dir/solution2.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/projekt2.dir/solution2.c.s"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\solution2.c -o CMakeFiles\projekt2.dir\solution2.c.s

# Object files for target projekt2
projekt2_OBJECTS = \
"CMakeFiles/projekt2.dir/solution2.c.obj"

# External object files for target projekt2
projekt2_EXTERNAL_OBJECTS =

projekt2.exe: CMakeFiles/projekt2.dir/solution2.c.obj
projekt2.exe: CMakeFiles/projekt2.dir/build.make
projekt2.exe: CMakeFiles/projekt2.dir/linklibs.rsp
projekt2.exe: CMakeFiles/projekt2.dir/objects1.rsp
projekt2.exe: CMakeFiles/projekt2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable projekt2.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\projekt2.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/projekt2.dir/build: projekt2.exe

.PHONY : CMakeFiles/projekt2.dir/build

CMakeFiles/projekt2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\projekt2.dir\cmake_clean.cmake
.PHONY : CMakeFiles/projekt2.dir/clean

CMakeFiles/projekt2.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug C:\Users\Piotr\Desktop\zajecia\6_semestr\APTO\projekt\cmake-build-debug\CMakeFiles\projekt2.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/projekt2.dir/depend


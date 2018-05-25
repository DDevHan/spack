##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install blasr-libcpp
#
# You can edit this file again by typing:
#
#     spack edit blasr-libcpp
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import pdb

class BlasrLibcpp(CMakePackage):
    """Blasr_libcpp is a library used by blasr and other executables such as samtoh5, loadPulses for analyzing PacBio sequences."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/PacificBiosciences/blasr_libcpp"
    url      = "https://github.com/PacificBiosciences/blasr_libcpp/tarball/b038971c97eb5403b982c177eb44e488d25e9994"

    version('038971c97eb5403b982c177eb44e488d25e9994', 'bd75541ab5e0a53c62f534ee73746878')

    # FIXME: Add dependencies if required.
    depends_on('pbbam')
    depends_on('hdf5+cxx@1.8.19')
    depends_on('pkgconfig')

    #BUILD_TESTS = FALSE

    #if BUILD_TESTS = False
    def patch(self):    
        filter_file(r'^add_subdirectory', '#', 'CMakeLists.txt')
        filter_file(r'^enable_testing*', '#', 'CMakeLists.txt')
	filter_file(r'^file.GLOB_RECURSE TEST_CPP*', '#', 'CMakeLists.txt')
	filter_file(r'^add_executable.libcpptest ..TEST_CPP..*', '#', 'CMakeLists.txt')
	filter_file(r'^target_include_directories.libcpptest PUBLIC .{BLAS*', '#', 'CMakeLists.txt')
	filter_file(r'^target_link_libraries.libcpptest gtest_main libcpp*', '#', 'CMakeLists.txt')
	filter_file(r'^add_test.libcpptest*', '#', 'CMakeLists.txt')
	filter_file(r'^set_target_properties.libcpptest*', '#', 'CMakeLists.txt')
	#filter_file(r'^if .LOCAL_LINKER*', '#', 'CMakeLists.txt')
	filter_file(r'    set_target_properties.libcpptest*', '#', 'CMakeLists.txt')
	#filter_file(r'endif*', '#', 'CMakeLists.txt')
	filter_file(r'add_custom_target.check_lib*', '#', 'CMakeLists.txt')
	filter_file(r'    COMMAND libcpptest ..gtest*', '#', 'CMakeLists.txt')
	filter_file(r'    WORKING_DIRECTORY*', '#', 'CMakeLists.txt')
	    #pdb.set_trace()
        filter_file(r'    add_subdirectory.*', '#', 'cmake/blasrlibcpp-dependencies.cmake')
	    #pdb_break.py()
    def install(self, spec, prefix):
#       install('spack-build/liblibcpp.a', join_path(prefix.lib, 'liblibcpp.a'))
	install_tree('hdf', prefix.hdf)
	install_tree('alignment', prefix.alignment)
	install_tree('pbdata', prefix.pbdata)
    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
	spack_env.set('HDF5_INCLUDE_DIRS', self.prefix.hdf)
#	spack_env.set('HDF5_LIBRARIES', self.spec.lib)
        #install_tree('spack-build/lib', prefix.lib)
        #install_tree('include/pbbam', prefix.include.pbbam)


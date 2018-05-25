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
from spack import *


class Blasr(CMakePackage):
    """The PacBio long read aligner."""

    homepage = "https://github.com/PacificBiosciences/blasr/wiki"
    url      = "https://github.com/PacificBiosciences/blasr/tarball/eab53fd220a05dfd7290962360a6ccce55be9c7c"

    version('2018.04.11', '42b298230213928a43652db7981e82fe',
            url="https://github.com/PacificBiosciences/blasr/tarball/eab53fd220a05dfd7290962360a6ccce55be9c7c") 

    depends_on('ncurses')
    depends_on('hdf5')
    depends_on('htslib')
    depends_on('zlib')
    depends_on('boost')
    depends_on('pbbam')
    depends_on('pkgconfig')
    depends_on('ninja')
    depends_on('blasr-libcpp')
    
    def cmake_args(self):
	cmake_args = [
            "-DPacBioBAM_LIBRARIES={0}".format(self.spec['pbbam'].prefix.lib), 
	    "-DPacBioBAM_INCLUDE_DIRS={0}".format(self.spec['pbbam'].prefix.include),
	    "-DHDF5_CPP={0}".format(self.spec['blasr-libcpp'].prefix.hdf),
	    "-DHDF5_CPP={0}".format(self.spec['blasr-libcpp'].prefix.alignment),
	    "-DHDF5_CPP={0}".format(self.spec['blasr-libcpp'].prefix.pbdata),
	    "-DBLASR_SOURCE_DIR={0}".format(self.stage.source_path),
	    "-DHDF5_INCLUDE_DIRS={0}".format(self.spec['blasr-libcpp'].prefix.hdf),
	    "-DBoost_INCLUDE_DIRS={0}".format(self.spec['boost'].prefix)
		]
	cmake_args.append("-D__find_git_sha1=YES")
    		

        return cmake_args
    def patch(self):
	filter_file(r'^if...find_git_sha1.$', '#', 'cmake/blasr-gitsha1.cmake')
	filter_file(r'    return..$', '#', 'cmake/blasr-gitsha1.cmake')
	filter_file(r'^endif..$', '#', 'cmake/blasr-gitsha1.cmake')
	filter_file(r'^.*if .NOT res EQUAL 0.$', '#', 'cmake/blasr-gitsha1.cmake')
	filter_file(r'.*message.FATAL_ERROR .Could not determine git sha1 via .git describe ..always ..dirty....', '#', 'cmake/blasr-gitsha1.cmake')
	filter_file(r'    endif..$', '#', 'cmake/blasr-gitsha1.cmake')
#	filter_file(r'^.*blasr-config.*$', '#', 'CMakeLists.txt')
	filter_file(r'^file\(GLOB HDF5_CPP.*$', 'file(GLOB HDF5_CPP '+self.spec['blasr-libcpp'].prefix+'/hdf/*cpp)', 'CMakeLists.txt')
	filter_file(r'^file\(GLOB_RECURSE ALIGNMENT_CPP.*$', 'file(GLOB_RECURSE ALIGNMENT_CPP '+self.spec['blasr-libcpp'].prefix+'/alignment/*.cpp)', 'CMakeLists.txt')
	filter_file(r'^file\(GLOB_RECURSE PBDATA_CPP.*$', 'file(GLOB_RECURSE PBDATA_CPP '+self.spec['blasr-libcpp'].prefix+'/pbdata/*.cpp)', 'CMakeLists.txt')
	filter_file(r'    \${BLASR_RootDir}/libcpp/hdf.*$', self.spec['blasr-libcpp'].prefix+'/hdf', 'CMakeLists.txt')
	filter_file(r'    \${BLASR_RootDir}/libcpp/alignment$', self.spec['blasr-libcpp'].prefix+'/alignment', 'CMakeLists.txt')
	filter_file(r'    \${BLASR_RootDir}/libcpp/pbdata.*$', self.spec['blasr-libcpp'].prefix+'/pbdata', 'CMakeLists.txt')
        filter_file(r'    \${HDF5_INCLUDE_DIRS}$', self.spec['blasr-libcpp'].prefix+'/hdf', 'CMakeLists.txt')
	filter_file(r'^set.*find.git.sha1 YES.$', '#', 'cmake/blasr-gitsha1.cmake')

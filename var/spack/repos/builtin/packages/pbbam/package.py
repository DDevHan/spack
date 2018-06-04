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
#     spack install pbbam
#
# You can edit this file again by typing:
#
#     spack edit pbbam
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Pbbam(CMakePackage):
    """The pbbam software package provides components to create, query,
    & edit PacBio BAM files and associated indices.
    These components include a core C++ library,
    bindings for additional languages, and command-line utilities."""

    homepage = "https://github.com/PacificBiosciences/pbbam"
    url      = "https://github.com/PacificBiosciences/pbbam/tarball/b0f9993704f7e8572420c2d8febc92eaa9b6ba6e"

    version('2018.05.08', '7f322f6d47aa3a7da56c88edf51d8d8d',
            url="https://github.com/PacificBiosciences/pbbam/tarball/b0f9993704f7e8572420c2d8febc92eaa9b6ba6e")

    depends_on('zlib')
    depends_on('boost@1.55.0:')
    depends_on('htslib@1.3.1:')
    depends_on('doxygen+graphviz')

    def cmake_args(self):
        options = [
            '-DPacBioBAM_build_tests:BOOL=OFF'
        ]

        return options

    def install(self, spec, prefix):
        install_tree('spack-build/bin', prefix.bin)
        install_tree('spack-build/lib', prefix.lib)
        install_tree('include/pbbam', prefix.include.pbbam)

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('PacBioBAM_LIBRARIES', self.prefix.lib)
        spack_env.set('PacBioBAM_INCLUDE_DIRS', self.prefix.include)

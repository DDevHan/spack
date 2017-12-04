##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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
import distutils.dir_util


class Xmipp(Package):
    """Xmipp is a suite of image processing programs, primarily aimed at
       single-particle 3D electron microscopy."""

    homepage = "http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/WebHome"
    url      = "http://xmipp.cnb.csic.es/Downloads/Xmipp-3.1-src.tar.gz"

    version('3.1', '3926483aa4e0a29cf6fe435f2a858187')

    variant('nma', default=True, description='Build with NMA extension')
    variant('cltomo', default=True, description='Build with CLTOMO extension')

    depends_on('openmpi') # specifically asks for openmpi
    depends_on('java', type=('build', 'run'))
    depends_on('libpng')
    depends_on('freetype')
    depends_on('openssl')
    depends_on('ncurses')
    depends_on('readline')
    depends_on('libx11')

    if '+nma' or '+cltomo':
        depends_on('blas')
        depends_on('arpack-ng')
        conflicts('%cce')
        conflicts('%clang')
        conflicts('%intel')
        conflicts('%nag')
        conflicts('%pgi')
        conflicts('%xl')
        conflicts('%xl_r')

    phases = ['build', 'install']

    def build(self, spec, prefix):
        builder = Executable('./install.sh')
        builder('-j', '12')
        if '+nma' and '+cltomo':
            builder('--disable-all', '--cltomo', '--nma', '-j', '12')
        elif '+nma':
            builder('--disable-all', '--nma', '-j', '12')
        elif '+cltomo':
            builder('--disable-all', '--cltomo', '-j', '12')

    def install(self, spec, prefix):
        distutils.dir_util.copy_tree(".", prefix)

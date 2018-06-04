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


class PyPycf(PythonPackage):
    """Python access to the LibCF library"""

    homepage = "http://www.unidata.ucar.edu/software/libcf/"
    url      = "https://files.pythonhosted.org/packages/4c/ef/c3bcb5332038bfd531855414dec7027d2da7e71298e91d00f832e2d361ae/pycf-1.6.9.tar.gz"

    version('1.6.9', '97c583f727c165bae96cec5338c0add3')

    depends_on('py-setuptools', type='build')
    depends_on('netlib-lapack')
    depends_on('blas')
    depends_on('netcdf')

    phases = ['install']

    def setup_environment(self, spack_env, run_env):
        spack_env.set('LAPACK_LIBRARIES',
                      ''.join(self.spec['lapack'].libs.directories))
        spack_env.set('BLAS_LIBRARIES',
                      ''.join(self.spec['blas'].libs.directories))

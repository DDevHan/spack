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
import os
from distutils.dir_util import copy_tree
from shutil import copy


class Amber(Package):
    """Amber is a suite of biomolecular simulation programs."""

    homepage = "http://ambermd.org"
    url      = "file://{0}/Amber16.tar.bz2".format(os.getcwd())

    version('16', '2d52556093a8c878b64f35b2ac2aae20')

    depends_on('flex')
    depends_on('tcsh')
    depends_on('zlib')
    depends_on('bzip2')
    depends_on('libxt')
    depends_on('libx11')
    depends_on('libxext')
    depends_on('libxdmcp')
    # depends_on('tkinter') # not in spack yet
    depends_on('openmpi')
    depends_on('cuda', when='+cuda')
    depends_on('perl')
    depends_on('perl-extutils-makemaker')
    depends_on('patch')
    depends_on('bison')
    depends_on('boost')
    depends_on('fftw')

    resource(
        name='ambertools',
        url="file://{0}/AmberTools16.tar.bz2".format(os.getcwd()),
        md5='ca723e6780f70f46497282c9ea6645a3', placement = 'ambertools'
    )

    variant('cuda', default=False, description='Build with cuda support')
    variant('mpi', default=False, description='Use MPI for parallelization')

    def patch(self):
        copy_tree(join_path(self.stage.source_path, 'ambertools'), self.stage.source_path)
        filter_file('check_amberhome $ambhome', '', 'AmberTools/src/configure2', string=True)
#        filter_file(r'XHOME=', 'XHOME={0}'.format(self.spec['libxt'].prefix), 'AmberTools/src/config.h')

    def install(self, spec, prefix):
#        copy_tree(join_path(self.stage.source_path, 'ambertools'), self.stage.source_path)
#        export AMBERHOME=self.stage.source_path
        install_answer = ['N']
        install_answer_input = 'spack-config.in'
        with open(install_answer_input, 'w') as f:
            f.writelines(install_answer)
        with open(install_answer_input, 'r') as f:
            configure = Executable('./configure')
            configure('gnu', input=f)
            make()
            make('install')
            make('test')
            if '+cuda' in spec:
                configure('-cuda', 'gnu')
                make()

            if '+mpi' in spec:
                configure('-mpi', 'gnu')
                make()

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('AMBERHOME', self.spec.prefix)
        spack_env.set('AMBERHOME', self.spec.prefix)
        spack_env.set('XHOME', self.spec['libxt'].prefix)
        spack_env.set('XLIBS', self.spec['libxt'].prefix.lib)

##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
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

class Scipion(Package):
    """Scipion is an image processing framework to obtain 3D models of
       macromolecular complexes using Electron Microscopy."""

    homepage = "http://scipion.cnb.csic.es/m/home/"
    url      = "https://github.com/I2PC/scipion/archive/v1.1.tar.gz"

    version('1.1', 'a2ec547a57f56d648826f900fee9f418')

    variant('matlab', default=False, description='Compile with Matlab dependency')
    variant('cuda', default=False, description='Compile with cuda dependency')
    
    depends_on('cmake', type='build')
    depends_on('jdk', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('libxft')
    depends_on('openssl')
    depends_on('libxext')
    depends_on('libxml2')
    depends_on('readline')
    depends_on('libxscrnsaver')
    depends_on('gsl')
    depends_on('libx11')
    depends_on('freetype')
    depends_on('mpi')
    depends_on('opencv', when='+opencv')
    depends_on('matlab', when='+matlab')
    depends_on('cuda', when='+cuda')

    phases = ['configure', 'edit', 'install']
    
    def configure(self, spec, prefix):
        scipion = Executable('./scipion')
        scipion('config')
    
    def edit(self, spec, prefix):
        with working_dir('config'):
            config = FileFilter('scipion.conf')
            config.filter('CC = .*', 'CC = %s' % spack_cc)
            config.filter('CXX = .*', 'CXX = %s' % spack_cxx)
            config.filter('LINKERFORPROGRAMS = .*', 'LINKERFORPROGRAMS = %s' % spack_cxx)
            config.filter('MPI_CC = .*', 'MPI_CC = %s' % self.spec['mpi'].mpicc)
            config.filter('MPI_CXX = .*', 'MPI_CXX = %s' % self.spec['mpi'].mpicxx)
            config.filter('MPI_LINKERFORPROGRAMS = .*', 'MPI_LINKERFORPROGRAMS = %s' % self.spec['mpi'].mpicxx)
            config.filter('MPI_LIBDIR = .*', 'MPI_LIBDIR = %s' % self.spec['mpi'].prefix.lib)
            config.filter('MPI_INCLUDE = .*', 'MPI_INCLUDE = %s' % self.spec['mpi'].prefix.include)
            config.filter('MPI_BINDIR = .*', 'MPI_BINDIR = %s' % self.spec['mpi'].prefix.bin)
            config.filter('JAVA_HOME = .*', 'JAVA_HOME = %s' % self.spec['jdk'].prefix)
            if '+cuda' in self.spec:
                config.filter('CUDA_LIB = .*', 'CUDA_LIB = %s' % self.spec['cuda'].prefix.lib)
                config.filter('CUDA_BIN = .*', 'CUDA_BIN = %s' % self.spec['cuda'].prefix.bin)
                config.filter('CUDA = .*', 'CUDA = TRUE')
            if '+matlab' in self.spec:
                confif.filter('MATLAB_DIR = .*', 'MATLAB = %s' % self.spec['matlab'].prefix)
                config.filter('MATLAB = .*', 'MATLAB = TRUE')

    def install(self, spec, prefix):
        # The --no-opencv and --no-scipy arguments just means we will be using
        # our own opencv and scipy installation.
        with working_dir(self.stage.source_path):
            installer = Executable('./scipion')
            installer('install', '--no-scipy', '--no-opencv')
            distutils.dir_util.copy_tree(".", prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.spec.prefix)

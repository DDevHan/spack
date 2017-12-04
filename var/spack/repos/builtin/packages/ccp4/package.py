##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
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
import distutils.dir_util
import os


class Ccp4(Package):
    """CCP4 exists to produce and support a world-leading, integrated suite of
       programs that allows researchers to determine macromolecular structures
       by X-ray crystallography, and other biophysical techniques.

       Note: A manual download is required for CCP4.
       Spack will search your current directory for the download file.
       Alternatively, add this file to a mirror so that Spack can find it.
       For instructions on how to set up a mirror, see
       http://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "http://www.ccp4.ac.uk/"
    url      = "file://{0}/ccp4-7.0-src.tar.bz2".format(os.getcwd())

    version('7.0', '3f4020fab9c7e45145a9e67fc009cb05')

    variant('coot', default=True, description='Include coot')

    depends_on('m4', type='build')
    depends_on('python@:2.999', type=('build', 'run'))
    depends_on('java', type=('build', 'run'))
    depends_on('cmake', type='build')
    depends_on('qt')
    depends_on('libxml2')
    depends_on('libxt')
    depends_on('fontconfig')
    depends_on('libxrender')
    depends_on('libxinerama')
    depends_on('libxaw')
    depends_on('swig')
    depends_on('xz', when='+coot')
    depends_on('intltool', when='+coot')
    depends_on('mesa-glu', when='+coot')
    depends_on('libxmu', when='+coot')
    depends_on('gtkplus+X', when='+coot')
    depends_on('glib', when='+coot')

    def install(self, spec, prefix):
        build = Executable('./build')
        if self.spec.satisfies('platform=dariwn'):
            build('ccp4-osx')
        else:
            build('ccp4-linux')
        if '+coot' in self.spec:
            build('coot')
        with working_dir('ccp4-{0}'.format(version)):
            setup = Executable('./BINARY.setup')
            setup()
        distutils.dir_util.copy_tree('ccp4-{0}'.format(version), prefix)

    def setup_environment(self, spack_env, run_env):
        run_vars = join_path(self.prefix.bin, 'ccp4.setup-sh')
        if os.path.isfile(run_vars):
            run__env.extend(EnvironmentModifications.from_sourcing_file(
                            run_vars))

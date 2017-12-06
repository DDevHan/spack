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


class Circos(Package):
    """Circos is a software package for visualizing data and information. It
       visualizes data in a circular layout, this makes Circos ideal for
       exploring relationships between objects or positions."""

    homepage = "http://circos.ca/"
    url      = "http://circos.ca/distribution/circos-0.69-5.tgz"

    version('0.69-5', '49b4c467ba871fa416013c47d69db9e6')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-font-ttf', type=('build', 'run'))
    depends_on('perl-config-general@2.50:', type=('build', 'run'))
    depends_on('perl-gd', type=('build', 'run'))
    depends_on('perl-list-moreutils', type=('build', 'run'))
    depends_on('perl-math-bezier', type=('build', 'run'))
    depends_on('perl-math-round', type=('build', 'run'))
    depends_on('perl-math-vecstat', type=('build', 'run'))
    depends_on('perl-params-validate', type=('build', 'run'))
    depends_on('perl-readonly', type=('build', 'run'))
    depends_on('perl-regexp-common', type=('build', 'run'))
    depends_on('perl-set-intspan@1.16:', type=('build', 'run'))
    depends_on('perl-text-format', type=('build', 'run'))
    depends_on('freetype')
    depends_on('libpng')
    depends_on('zlib')
    depends_on('libgd')

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
        install_tree('data', prefix.data)
        install_tree('error', prefix.error)
        install_tree('etc', prefix.etc)
        install_tree('example', prefix.example)
        install_tree('fonts', prefix.fonts)
        install_tree('lib', prefix.lib)
        install_tree('tiles', prefix.tiles)
        install('gddiag.png', prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix)
        run_env.set('PERL5LIB', prefix.lib)

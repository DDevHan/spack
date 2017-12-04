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


class Pagan(MakefilePackage):
    """PAGAN is a general-purpose method for the alignment of sequence graphs.
    """

    homepage = "http://wasabiapp.org/software/pagan/"
    url      = "http://wasabiapp.org/download/pagan/pagan.src.20150723.tgz"

    version('20150723', '138ee18942c4baa5157c1e06b995f908')

    depends_on('raxml')
    depends_on('mafft')
    depends_on('exonerate')
    depends_on('boost')
    depends_on('curl', type='build')

    def edit(self, spec, prefix):
        with working_dir('src'):
            makefile = FileFilter('Makefile.no_Qt')
            makefile.filter('-I../boost/include', '-I%s' % self.spec['boost'].prefix.include)
            makefile.filter('INCPATH  =' , 'INCPATH  = -I%s ' % self.spec['curl'].prefix.include)
            makefile.filter('-lcurl', '-L%s' % self.spec['curl'].prefix.lib)
            makefile.filter('CC       =', 'CC = %s\n#CC =' % spack_cc)
            makefile.filter('CXX      =', 'CXX = %s\n#CXX =' % spack_cxx)

    def build(self, spec, prefix):
        with working_dir('src'):
            make('-f', 'Makefile.no_Qt')

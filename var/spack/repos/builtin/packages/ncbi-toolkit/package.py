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


class NcbiToolkit(AutotoolsPackage):
    """NCBI C++ Toolkit"""

    homepage = "https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/"
    url      = "ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools++/CURRENT/ncbi_cxx--18_0_0.tar.gz"

    version('18_0_0', '3835305bb47f7f3dc88ebb2ff4ded240')

    depends_on('samtools')

    def url_for_version(self, version):
        url = 'ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools++/CURRENT/ncbi_cxx--{0}.tar.gz'
        return url.format(version.underscored)

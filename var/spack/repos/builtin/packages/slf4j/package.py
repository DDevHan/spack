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


class Slf4j(Package):
    """The Simple Logging Facade for Java (SLF4J) serves as a simple facade
    or abstraction for various logging frameworks (e.g. java.util.logging,
    logback, log4j) allowing the end user to plug in the desired logging
    framework at deployment time."""

    homepage = "https://www.slf4j.org/"
    url      = "https://www.slf4j.org/dist/slf4j-1.7.25.tar.gz"

    version('1.8.0-beta2',  '75cb7e1bd12f3ed60eb976613f5efddb')
    version('1.8.0-beta1',  'fdf1d147672071d986b8c82fa1bd2e96')
    version('1.8.0-beta0',  '93c982570e08754e6da155e6eb55e947')
    version('1.8.0-bata2',  'b63f26be375353e2e033be689415baa0')
    version('1.8.0-alpha2', '260cb8e9abf2101554402e59bdcf47a9')
    version('1.8.0-alpha1', 'c586040c2f03dd24544382c95cafcbcc')
    version('1.8.0-alpha0', '6bf097e3f30331ebf7f678d7a034ac47')
    version('1.7.25',       '259f9845b34cdd82909cb7a6982668f5', preferred=True)

    depends_on('java', type='run')

    def install(self, spec, prefix):
        install_tree('.', prefix.bin)

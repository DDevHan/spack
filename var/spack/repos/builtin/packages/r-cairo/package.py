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


class RCairo(RPackage):
    """R graphics device using cairo graphics library for creating high-quality
       bitmap (PNG, JPEG, TIFF), vector (PDF, SVG, PostScript) and display
       (X11 and Win32) output"""

    homepage = "https://cran.r-project.org/web/packages/Cairo/index.html"
    url      = "https://cran.r-project.org/src/contrib/Cairo_1.5-9.tar.gz"

    version('1.5-9', 'f9deac4d1b1a58fbae96ab60ee27a739')

    depends_on('cairo')


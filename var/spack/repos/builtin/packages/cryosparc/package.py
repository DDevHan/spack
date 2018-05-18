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
from spack.error import SpackError


class Cryosparc(Package):
    """CryoSPARC is a software package for processing single-particle electron
    cryo-microscopy (cryo-EM) data.
    
    Note: cryoSPARC is a licensed software. You will need to get a license on
    cryoSPARC homepage and download the tar file yourself. Use 
    `curl $(curl -H "cryoSPARC-License: <CRYOSPARC_LICENSE_ID>" 
    "https://cryosparc.download/get/<VERSION>" ) > cryosparc-<VERSION>` 
    to download the tar file to your current directory. Alternatively, add this
    file to a mirror so that Spack can find it. For instructions on how to set
    up a mirror, see http://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://cryosparc.com/"

    version('0.6.5', '14b84dd78fbc558601be85d17cacb287')

    variant('license',
            default='',
            values=lambda x: True, # Anything goes as a key
            description='The license ID.'
            )

    def url_for_version(self, version):
        return "file://{0}/cryosparc-{1}.tar.gz".format(os.getcwd(), version)

    depends_on('cuda@8:')

    def install(self, spec, prefix):
        if not which('nvidia-smi'):
            raise SpackError('Need nvidia-smi. Installation terminated.')
        run_install = Executable('./install.sh')
        run_install('--license-id='+spec.variants['license'].values)

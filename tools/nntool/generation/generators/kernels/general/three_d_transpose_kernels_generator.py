# Copyright (C) 2020  GreenWaves Technologies, SAS

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

from generation.at_types.gen_ctrl import GenCtrl
from generation.code_block import CodeBlock
from generation.generator_decorators import generation_function, QREC_MULT8, QREC_POW2, QREC_FLOAT
from generation.gen_utils import at_bits
from graph.types import TransposeParameters

from ..autotiler_kernel import AutotilerKernel

LOG = logging.getLogger("nntool." + __name__)


@generation_function("kernels", (TransposeParameters, ), qrec_types=(QREC_MULT8, QREC_FLOAT, QREC_POW2))
def three_d_transpose_kernels_generator(gen, node, qrec, in_eparams, out_eparams, cname):
    del in_eparams, out_eparams
    real_in_shape, real_transpose = node.real_shape()
    if len(real_transpose) <= 1:
        return True
    if len(real_transpose) == 2:
        gen.kernels.append(TwoDTransposeKernel(cname, node, real_in_shape,
                                                  real_transpose, qrec, at_ver=gen.opts['at_ver']))
    elif len(real_transpose) == 3:
        gen.kernels.append(ThreeDTransposeKernel(cname, node, real_in_shape,
                                                    real_transpose, qrec, at_ver=gen.opts['at_ver']))
    else:
        raise NotImplementedError("only 2D or 3D transposes are currently supported")
    LOG.info("generating for transpose in %s out %s trans %s",
             node.in_dims[0], node.out_dims[0], node.transpose)
    return True

# extern int CNN_MatTranspose(
#         char *Name,
#         CNN_GenControl_T *Ctrl,
#         int DataSize,
#         int InFeat,
#         int Width,
#         int Height,
# 	KernelOper_T MatTransOper
# );
def gen_at_2d_transpose(code_block, name, datasize,
                        in_shape, gen_ctrl=None,
                        at_ver=3):
    code_block.write('CNN_MatTranspose("{}", {}, {}, 1, {}, {}, KOP_MATTRANSP);',
                     name, gen_ctrl, datasize, in_shape[1], in_shape[0])


class TwoDTransposeKernel(AutotilerKernel):
    def __init__(self, cname, params, real_in_shape, real_transpose, qrec, gen_ctrl=None, at_ver=3):
        if gen_ctrl is None:
            self.gen_ctrl = GenCtrl(None, cname=cname)
        else:
            gen_ctrl.cname = cname
            self.gen_ctrl = gen_ctrl

        if qrec.out_qs[0].is_floating:
            self.gen_ctrl.float_dump = 1

        self.in_q = qrec.in_qs[0]
        self.out_q = qrec.out_qs[0]
        self.in_shape = real_in_shape
        self.in_dim = params.in_dims[0]
        self.out_dim = params.out_dims[0]
        self.real_transpose = real_transpose
        self.cname = cname
        self.node_name = params.name
        self.at_ver = at_ver

    def code(self, code_block=None):
        if code_block is None:
            code_block = CodeBlock()

        code_block.comment("generator for {}", self.node_name)
        code_block.comment("transpose from {} to {} ({})", self.in_dim,
                           self.out_dim, self.real_transpose)

        if not self.gen_ctrl.is_unmodified:
            self.gen_ctrl.gen_ctrl_decl(code_block)
            gen_ctrl = self.gen_ctrl.ctrl_name
        else:
            gen_ctrl = "0"

        gen_at_2d_transpose(code_block, self.cname,
                            abs(at_bits(self.in_q)), self.in_shape, gen_ctrl=gen_ctrl)
        return code_block


# extern int CNN_3DTensorPermute(
# 	char *Name,
# 	CNN_GenControl_T *Ctrl,
# 	int Size,
# 	int InFeat,
# 	int Width,
# 	int Height,
#  	KernelOper_T MatPermOper
# );

def gen_at_3d_transpose(code_block, name, datasize,
                        in_shape, permop, gen_ctrl=None,
                        at_ver=3):

    code_block.write('CNN_3DTensorPermute("{}", {}, {}, {}, {}, {}, {});',
                     name, gen_ctrl, datasize, in_shape[0], in_shape[2], in_shape[1],
                     permop)


class ThreeDTransposeKernel(AutotilerKernel):
    def __init__(self, cname, params, real_in_shape, real_transpose, qrec, gen_ctrl=None, at_ver=3):
        if gen_ctrl is None:
            self.gen_ctrl = GenCtrl(None, cname=cname)
        else:
            gen_ctrl.cname = cname
            self.gen_ctrl = gen_ctrl

        if qrec.out_qs[0].is_floating:
            self.gen_ctrl.float_dump = 1

        self.in_shape = real_in_shape
        dim_names = ['C', 'H', 'W']
        perm = [dim_names[i] for i in real_transpose]
        self.permop = "KOP_MATPERM_CHW2{}".format("".join(perm))
        self.real_transpose = real_transpose

        self.in_q = qrec.in_qs[0]
        self.out_q = qrec.out_qs[0]
        self.in_dim = params.in_dims[0]
        self.out_dim = params.out_dims[0]
        self.cname = cname
        self.node_name = params.name
        self.at_ver = at_ver

    def code(self, code_block=None):
        if code_block is None:
            code_block = CodeBlock()


        code_block.comment("generator for {}", self.node_name)
        code_block.comment("transpose from {} to {} ({})", self.in_dim,
                           self.out_dim, self.real_transpose)

        if not self.gen_ctrl.is_unmodified:
            self.gen_ctrl.gen_ctrl_decl(code_block)
            gen_ctrl = self.gen_ctrl.ctrl_name
        else:
            gen_ctrl = "0"

        gen_at_3d_transpose(code_block, self.cname, abs(at_bits(self.in_q)),
                            self.in_shape, self.permop, gen_ctrl=gen_ctrl)
        return code_block

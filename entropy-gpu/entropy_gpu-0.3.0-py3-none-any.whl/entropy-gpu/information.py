import sys
import numpy as np
import ctypes as ct
# Stub code for OpenCL setup.

import pyopencl as cl
import numpy as np
import sys

if cl.version.VERSION < (2015,2):
    raise Exception('Futhark requires at least PyOpenCL version 2015.2.  Installed version is %s.' %
                    cl.version.VERSION_TEXT)

def parse_preferred_device(s):
    pref_num = 0
    if len(s) > 1 and s[0] == '#':
        i = 1
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                pref_num = pref_num * 10 + int(s[i])
            i += 1
        while i < len(s) and s[i].isspace():
            i += 1
        return (s[i:], pref_num)
    else:
        return (s, 0)

def get_prefered_context(interactive=False, platform_pref=None, device_pref=None):
    if device_pref != None:
        (device_pref, device_num) = parse_preferred_device(device_pref)
    else:
        device_num = 0

    if interactive:
        return cl.create_some_context(interactive=True)

    def blacklisted(p, d):
        return platform_pref == None and device_pref == None and \
            p.name == "Apple" and d.name.find("Intel(R) Core(TM)") >= 0
    def platform_ok(p):
        return not platform_pref or p.name.find(platform_pref) >= 0
    def device_ok(d):
        return not device_pref or d.name.find(device_pref) >= 0

    device_matches = 0

    for p in cl.get_platforms():
        if not platform_ok(p):
            continue
        for d in p.get_devices():
            if blacklisted(p,d) or not device_ok(d):
                continue
            if device_matches == device_num:
                return cl.Context(devices=[d])
            else:
                device_matches += 1
    raise Exception('No OpenCL platform and device matching constraints found.')

def size_assignment(s):
    name, value = s.split('=')
    return (name, int(value))

def check_types(self, required_types):
    if 'f64' in required_types:
        if self.device.get_info(cl.device_info.PREFERRED_VECTOR_WIDTH_DOUBLE) == 0:
            raise Exception('Program uses double-precision floats, but this is not supported on chosen device: %s' % self.device.name)

def apply_size_heuristics(self, size_heuristics, sizes):
    for (platform_name, device_type, size, value) in size_heuristics:
        if sizes[size] == None \
           and self.platform.name.find(platform_name) >= 0 \
           and self.device.type == device_type:
               if type(value) == str:
                   sizes[size] = self.device.get_info(getattr(cl.device_info,value))
               else:
                   sizes[size] = value
    return sizes

def initialise_opencl_object(self,
                             program_src='',
                             command_queue=None,
                             interactive=False,
                             platform_pref=None,
                             device_pref=None,
                             default_group_size=None,
                             default_num_groups=None,
                             default_tile_size=None,
                             default_threshold=None,
                             size_heuristics=[],
                             required_types=[],
                             all_sizes={},
                             user_sizes={}):
    if command_queue is None:
        self.ctx = get_prefered_context(interactive, platform_pref, device_pref)
        self.queue = cl.CommandQueue(self.ctx)
    else:
        self.ctx = command_queue.context
        self.queue = command_queue
    self.device = self.queue.device
    self.platform = self.device.platform
    self.pool = cl.tools.MemoryPool(cl.tools.ImmediateAllocator(self.queue))
    device_type = self.device.type

    check_types(self, required_types)

    max_group_size = int(self.device.max_work_group_size)
    max_tile_size = int(np.sqrt(self.device.max_work_group_size))

    self.max_group_size = max_group_size
    self.max_tile_size = max_tile_size
    self.max_threshold = 0
    self.max_num_groups = 0
    self.max_local_memory = int(self.device.local_mem_size)
    self.free_list = {}

    if 'default_group_size' in sizes:
        default_group_size = sizes['default_group_size']
        del sizes['default_group_size']

    if 'default_num_groups' in sizes:
        default_num_groups = sizes['default_num_groups']
        del sizes['default_num_groups']

    if 'default_tile_size' in sizes:
        default_tile_size = sizes['default_tile_size']
        del sizes['default_tile_size']

    if 'default_threshold' in sizes:
        default_threshold = sizes['default_threshold']
        del sizes['default_threshold']

    default_group_size_set = default_group_size != None
    default_tile_size_set = default_tile_size != None
    default_sizes = apply_size_heuristics(self, size_heuristics,
                                          {'group_size': default_group_size,
                                           'tile_size': default_tile_size,
                                           'num_groups': default_num_groups,
                                           'lockstep_width': None,
                                           'threshold': default_threshold})
    default_group_size = default_sizes['group_size']
    default_num_groups = default_sizes['num_groups']
    default_threshold = default_sizes['threshold']
    default_tile_size = default_sizes['tile_size']
    lockstep_width = default_sizes['lockstep_width']

    if default_group_size > max_group_size:
        if default_group_size_set:
            sys.stderr.write('Note: Device limits group size to {} (down from {})\n'.
                             format(max_tile_size, default_group_size))
        default_group_size = max_group_size

    if default_tile_size > max_tile_size:
        if default_tile_size_set:
            sys.stderr.write('Note: Device limits tile size to {} (down from {})\n'.
                             format(max_tile_size, default_tile_size))
        default_tile_size = max_tile_size

    for (k,v) in user_sizes.items():
        if k in all_sizes:
            all_sizes[k]['value'] = v
        else:
            raise Exception('Unknown size: {}\nKnown sizes: {}'.format(k, ' '.join(all_sizes.keys())))

    self.sizes = {}
    for (k,v) in all_sizes.items():
        if v['class'] == 'group_size':
            max_value = max_group_size
            default_value = default_group_size
        elif v['class'] == 'num_groups':
            max_value = max_group_size # Intentional!
            default_value = default_num_groups
        elif v['class'] == 'tile_size':
            max_value = max_tile_size
            default_value = default_tile_size
        elif v['class'].startswith('threshold'):
            max_value = None
            default_value = default_threshold
        else:
            # Bespoke sizes have no limit or default.
            max_value = None
        if v['value'] == None:
            self.sizes[k] = default_value
        elif max_value != None and v['value'] > max_value:
            sys.stderr.write('Note: Device limits {} to {} (down from {}\n'.
                             format(k, max_value, v['value']))
            self.sizes[k] = max_value
        else:
            self.sizes[k] = v['value']

    # XXX: we perform only a subset of z-encoding here.  Really, the
    # compiler should provide us with the variables to which
    # parameters are mapped.
    if (len(program_src) >= 0):
        return cl.Program(self.ctx, program_src).build(
            ["-DLOCKSTEP_WIDTH={}".format(lockstep_width)]
            + ["-D{}={}".format(s.replace('z', 'zz').replace('.', 'zi'),v) for (s,v) in self.sizes.items()])

def opencl_alloc(self, min_size, tag):
    min_size = 1 if min_size == 0 else min_size
    assert min_size > 0
    return self.pool.allocate(min_size)

def opencl_free_all(self):
    self.pool.free_held()
import pyopencl.array
import time
import argparse
sizes = {}
synchronous = False
preferred_platform = None
preferred_device = None
default_threshold = None
default_group_size = None
default_num_groups = None
default_tile_size = None
fut_opencl_src = """#ifdef cl_clang_storage_class_specifiers
#pragma OPENCL EXTENSION cl_clang_storage_class_specifiers : enable
#endif
#pragma OPENCL EXTENSION cl_khr_byte_addressable_store : enable
#pragma OPENCL EXTENSION cl_khr_fp64 : enable
__kernel void dummy_kernel(__global unsigned char *dummy, int n)
{
    const int thread_gid = get_global_id(0);
    
    if (thread_gid >= n)
        return;
}
typedef char int8_t;
typedef short int16_t;
typedef int int32_t;
typedef long int64_t;
typedef uchar uint8_t;
typedef ushort uint16_t;
typedef uint uint32_t;
typedef ulong uint64_t;
#ifdef cl_nv_pragma_unroll
static inline void mem_fence_global()
{
    asm("membar.gl;");
}
#else
static inline void mem_fence_global()
{
    mem_fence(CLK_LOCAL_MEM_FENCE | CLK_GLOBAL_MEM_FENCE);
}
#endif
static inline void mem_fence_local()
{
    mem_fence(CLK_LOCAL_MEM_FENCE);
}
static inline int8_t add8(int8_t x, int8_t y)
{
    return x + y;
}
static inline int16_t add16(int16_t x, int16_t y)
{
    return x + y;
}
static inline int32_t add32(int32_t x, int32_t y)
{
    return x + y;
}
static inline int64_t add64(int64_t x, int64_t y)
{
    return x + y;
}
static inline int8_t sub8(int8_t x, int8_t y)
{
    return x - y;
}
static inline int16_t sub16(int16_t x, int16_t y)
{
    return x - y;
}
static inline int32_t sub32(int32_t x, int32_t y)
{
    return x - y;
}
static inline int64_t sub64(int64_t x, int64_t y)
{
    return x - y;
}
static inline int8_t mul8(int8_t x, int8_t y)
{
    return x * y;
}
static inline int16_t mul16(int16_t x, int16_t y)
{
    return x * y;
}
static inline int32_t mul32(int32_t x, int32_t y)
{
    return x * y;
}
static inline int64_t mul64(int64_t x, int64_t y)
{
    return x * y;
}
static inline uint8_t udiv8(uint8_t x, uint8_t y)
{
    return x / y;
}
static inline uint16_t udiv16(uint16_t x, uint16_t y)
{
    return x / y;
}
static inline uint32_t udiv32(uint32_t x, uint32_t y)
{
    return x / y;
}
static inline uint64_t udiv64(uint64_t x, uint64_t y)
{
    return x / y;
}
static inline uint8_t umod8(uint8_t x, uint8_t y)
{
    return x % y;
}
static inline uint16_t umod16(uint16_t x, uint16_t y)
{
    return x % y;
}
static inline uint32_t umod32(uint32_t x, uint32_t y)
{
    return x % y;
}
static inline uint64_t umod64(uint64_t x, uint64_t y)
{
    return x % y;
}
static inline int8_t sdiv8(int8_t x, int8_t y)
{
    int8_t q = x / y;
    int8_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int16_t sdiv16(int16_t x, int16_t y)
{
    int16_t q = x / y;
    int16_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int32_t sdiv32(int32_t x, int32_t y)
{
    int32_t q = x / y;
    int32_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int64_t sdiv64(int64_t x, int64_t y)
{
    int64_t q = x / y;
    int64_t r = x % y;
    
    return q - ((r != 0 && r < 0 != y < 0) ? 1 : 0);
}
static inline int8_t smod8(int8_t x, int8_t y)
{
    int8_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int16_t smod16(int16_t x, int16_t y)
{
    int16_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int32_t smod32(int32_t x, int32_t y)
{
    int32_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int64_t smod64(int64_t x, int64_t y)
{
    int64_t r = x % y;
    
    return r + (r == 0 || (x > 0 && y > 0) || (x < 0 && y < 0) ? 0 : y);
}
static inline int8_t squot8(int8_t x, int8_t y)
{
    return x / y;
}
static inline int16_t squot16(int16_t x, int16_t y)
{
    return x / y;
}
static inline int32_t squot32(int32_t x, int32_t y)
{
    return x / y;
}
static inline int64_t squot64(int64_t x, int64_t y)
{
    return x / y;
}
static inline int8_t srem8(int8_t x, int8_t y)
{
    return x % y;
}
static inline int16_t srem16(int16_t x, int16_t y)
{
    return x % y;
}
static inline int32_t srem32(int32_t x, int32_t y)
{
    return x % y;
}
static inline int64_t srem64(int64_t x, int64_t y)
{
    return x % y;
}
static inline int8_t smin8(int8_t x, int8_t y)
{
    return x < y ? x : y;
}
static inline int16_t smin16(int16_t x, int16_t y)
{
    return x < y ? x : y;
}
static inline int32_t smin32(int32_t x, int32_t y)
{
    return x < y ? x : y;
}
static inline int64_t smin64(int64_t x, int64_t y)
{
    return x < y ? x : y;
}
static inline uint8_t umin8(uint8_t x, uint8_t y)
{
    return x < y ? x : y;
}
static inline uint16_t umin16(uint16_t x, uint16_t y)
{
    return x < y ? x : y;
}
static inline uint32_t umin32(uint32_t x, uint32_t y)
{
    return x < y ? x : y;
}
static inline uint64_t umin64(uint64_t x, uint64_t y)
{
    return x < y ? x : y;
}
static inline int8_t smax8(int8_t x, int8_t y)
{
    return x < y ? y : x;
}
static inline int16_t smax16(int16_t x, int16_t y)
{
    return x < y ? y : x;
}
static inline int32_t smax32(int32_t x, int32_t y)
{
    return x < y ? y : x;
}
static inline int64_t smax64(int64_t x, int64_t y)
{
    return x < y ? y : x;
}
static inline uint8_t umax8(uint8_t x, uint8_t y)
{
    return x < y ? y : x;
}
static inline uint16_t umax16(uint16_t x, uint16_t y)
{
    return x < y ? y : x;
}
static inline uint32_t umax32(uint32_t x, uint32_t y)
{
    return x < y ? y : x;
}
static inline uint64_t umax64(uint64_t x, uint64_t y)
{
    return x < y ? y : x;
}
static inline uint8_t shl8(uint8_t x, uint8_t y)
{
    return x << y;
}
static inline uint16_t shl16(uint16_t x, uint16_t y)
{
    return x << y;
}
static inline uint32_t shl32(uint32_t x, uint32_t y)
{
    return x << y;
}
static inline uint64_t shl64(uint64_t x, uint64_t y)
{
    return x << y;
}
static inline uint8_t lshr8(uint8_t x, uint8_t y)
{
    return x >> y;
}
static inline uint16_t lshr16(uint16_t x, uint16_t y)
{
    return x >> y;
}
static inline uint32_t lshr32(uint32_t x, uint32_t y)
{
    return x >> y;
}
static inline uint64_t lshr64(uint64_t x, uint64_t y)
{
    return x >> y;
}
static inline int8_t ashr8(int8_t x, int8_t y)
{
    return x >> y;
}
static inline int16_t ashr16(int16_t x, int16_t y)
{
    return x >> y;
}
static inline int32_t ashr32(int32_t x, int32_t y)
{
    return x >> y;
}
static inline int64_t ashr64(int64_t x, int64_t y)
{
    return x >> y;
}
static inline uint8_t and8(uint8_t x, uint8_t y)
{
    return x & y;
}
static inline uint16_t and16(uint16_t x, uint16_t y)
{
    return x & y;
}
static inline uint32_t and32(uint32_t x, uint32_t y)
{
    return x & y;
}
static inline uint64_t and64(uint64_t x, uint64_t y)
{
    return x & y;
}
static inline uint8_t or8(uint8_t x, uint8_t y)
{
    return x | y;
}
static inline uint16_t or16(uint16_t x, uint16_t y)
{
    return x | y;
}
static inline uint32_t or32(uint32_t x, uint32_t y)
{
    return x | y;
}
static inline uint64_t or64(uint64_t x, uint64_t y)
{
    return x | y;
}
static inline uint8_t xor8(uint8_t x, uint8_t y)
{
    return x ^ y;
}
static inline uint16_t xor16(uint16_t x, uint16_t y)
{
    return x ^ y;
}
static inline uint32_t xor32(uint32_t x, uint32_t y)
{
    return x ^ y;
}
static inline uint64_t xor64(uint64_t x, uint64_t y)
{
    return x ^ y;
}
static inline bool ult8(uint8_t x, uint8_t y)
{
    return x < y;
}
static inline bool ult16(uint16_t x, uint16_t y)
{
    return x < y;
}
static inline bool ult32(uint32_t x, uint32_t y)
{
    return x < y;
}
static inline bool ult64(uint64_t x, uint64_t y)
{
    return x < y;
}
static inline bool ule8(uint8_t x, uint8_t y)
{
    return x <= y;
}
static inline bool ule16(uint16_t x, uint16_t y)
{
    return x <= y;
}
static inline bool ule32(uint32_t x, uint32_t y)
{
    return x <= y;
}
static inline bool ule64(uint64_t x, uint64_t y)
{
    return x <= y;
}
static inline bool slt8(int8_t x, int8_t y)
{
    return x < y;
}
static inline bool slt16(int16_t x, int16_t y)
{
    return x < y;
}
static inline bool slt32(int32_t x, int32_t y)
{
    return x < y;
}
static inline bool slt64(int64_t x, int64_t y)
{
    return x < y;
}
static inline bool sle8(int8_t x, int8_t y)
{
    return x <= y;
}
static inline bool sle16(int16_t x, int16_t y)
{
    return x <= y;
}
static inline bool sle32(int32_t x, int32_t y)
{
    return x <= y;
}
static inline bool sle64(int64_t x, int64_t y)
{
    return x <= y;
}
static inline int8_t pow8(int8_t x, int8_t y)
{
    int8_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int16_t pow16(int16_t x, int16_t y)
{
    int16_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int32_t pow32(int32_t x, int32_t y)
{
    int32_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline int64_t pow64(int64_t x, int64_t y)
{
    int64_t res = 1, rem = y;
    
    while (rem != 0) {
        if (rem & 1)
            res *= x;
        rem >>= 1;
        x *= x;
    }
    return res;
}
static inline bool itob_i8_bool(int8_t x)
{
    return x;
}
static inline bool itob_i16_bool(int16_t x)
{
    return x;
}
static inline bool itob_i32_bool(int32_t x)
{
    return x;
}
static inline bool itob_i64_bool(int64_t x)
{
    return x;
}
static inline int8_t btoi_bool_i8(bool x)
{
    return x;
}
static inline int16_t btoi_bool_i16(bool x)
{
    return x;
}
static inline int32_t btoi_bool_i32(bool x)
{
    return x;
}
static inline int64_t btoi_bool_i64(bool x)
{
    return x;
}
#define sext_i8_i8(x) ((int8_t) (int8_t) x)
#define sext_i8_i16(x) ((int16_t) (int8_t) x)
#define sext_i8_i32(x) ((int32_t) (int8_t) x)
#define sext_i8_i64(x) ((int64_t) (int8_t) x)
#define sext_i16_i8(x) ((int8_t) (int16_t) x)
#define sext_i16_i16(x) ((int16_t) (int16_t) x)
#define sext_i16_i32(x) ((int32_t) (int16_t) x)
#define sext_i16_i64(x) ((int64_t) (int16_t) x)
#define sext_i32_i8(x) ((int8_t) (int32_t) x)
#define sext_i32_i16(x) ((int16_t) (int32_t) x)
#define sext_i32_i32(x) ((int32_t) (int32_t) x)
#define sext_i32_i64(x) ((int64_t) (int32_t) x)
#define sext_i64_i8(x) ((int8_t) (int64_t) x)
#define sext_i64_i16(x) ((int16_t) (int64_t) x)
#define sext_i64_i32(x) ((int32_t) (int64_t) x)
#define sext_i64_i64(x) ((int64_t) (int64_t) x)
#define zext_i8_i8(x) ((uint8_t) (uint8_t) x)
#define zext_i8_i16(x) ((uint16_t) (uint8_t) x)
#define zext_i8_i32(x) ((uint32_t) (uint8_t) x)
#define zext_i8_i64(x) ((uint64_t) (uint8_t) x)
#define zext_i16_i8(x) ((uint8_t) (uint16_t) x)
#define zext_i16_i16(x) ((uint16_t) (uint16_t) x)
#define zext_i16_i32(x) ((uint32_t) (uint16_t) x)
#define zext_i16_i64(x) ((uint64_t) (uint16_t) x)
#define zext_i32_i8(x) ((uint8_t) (uint32_t) x)
#define zext_i32_i16(x) ((uint16_t) (uint32_t) x)
#define zext_i32_i32(x) ((uint32_t) (uint32_t) x)
#define zext_i32_i64(x) ((uint64_t) (uint32_t) x)
#define zext_i64_i8(x) ((uint8_t) (uint64_t) x)
#define zext_i64_i16(x) ((uint16_t) (uint64_t) x)
#define zext_i64_i32(x) ((uint32_t) (uint64_t) x)
#define zext_i64_i64(x) ((uint64_t) (uint64_t) x)
#if defined(__OPENCL_VERSION__)
int32_t futrts_popc8(int8_t x)
{
    return popcount(x);
}
int32_t futrts_popc16(int16_t x)
{
    return popcount(x);
}
int32_t futrts_popc32(int32_t x)
{
    return popcount(x);
}
int32_t futrts_popc64(int64_t x)
{
    return popcount(x);
}
#elif defined(__CUDA_ARCH__)
int32_t futrts_popc8(int8_t x)
{
    return __popc(zext_i8_i32(x));
}
int32_t futrts_popc16(int16_t x)
{
    return __popc(zext_i16_i32(x));
}
int32_t futrts_popc32(int32_t x)
{
    return __popc(x);
}
int32_t futrts_popc64(int64_t x)
{
    return __popcll(x);
}
#else
int32_t futrts_popc8(int8_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc16(int16_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc32(int32_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
int32_t futrts_popc64(int64_t x)
{
    int c = 0;
    
    for (; x; ++c)
        x &= x - 1;
    return c;
}
#endif
#if defined(__OPENCL_VERSION__)
int32_t futrts_clzz8(int8_t x)
{
    return clz(x);
}
int32_t futrts_clzz16(int16_t x)
{
    return clz(x);
}
int32_t futrts_clzz32(int32_t x)
{
    return clz(x);
}
int32_t futrts_clzz64(int64_t x)
{
    return clz(x);
}
#elif defined(__CUDA_ARCH__)
int32_t futrts_clzz8(int8_t x)
{
    return __clz(zext_i8_i32(x)) - 24;
}
int32_t futrts_clzz16(int16_t x)
{
    return __clz(zext_i16_i32(x)) - 16;
}
int32_t futrts_clzz32(int32_t x)
{
    return __clz(x);
}
int32_t futrts_clzz64(int64_t x)
{
    return __clzll(x);
}
#else
int32_t futrts_clzz8(int8_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz16(int16_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz32(int32_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
int32_t futrts_clzz64(int64_t x)
{
    int n = 0;
    int bits = sizeof(x) * 8;
    
    for (int i = 0; i < bits; i++) {
        if (x < 0)
            break;
        n++;
        x <<= 1;
    }
    return n;
}
#endif
static inline float fdiv32(float x, float y)
{
    return x / y;
}
static inline float fadd32(float x, float y)
{
    return x + y;
}
static inline float fsub32(float x, float y)
{
    return x - y;
}
static inline float fmul32(float x, float y)
{
    return x * y;
}
static inline float fmin32(float x, float y)
{
    return fmin(x, y);
}
static inline float fmax32(float x, float y)
{
    return fmax(x, y);
}
static inline float fpow32(float x, float y)
{
    return pow(x, y);
}
static inline bool cmplt32(float x, float y)
{
    return x < y;
}
static inline bool cmple32(float x, float y)
{
    return x <= y;
}
static inline float sitofp_i8_f32(int8_t x)
{
    return (float) x;
}
static inline float sitofp_i16_f32(int16_t x)
{
    return (float) x;
}
static inline float sitofp_i32_f32(int32_t x)
{
    return (float) x;
}
static inline float sitofp_i64_f32(int64_t x)
{
    return (float) x;
}
static inline float uitofp_i8_f32(uint8_t x)
{
    return (float) x;
}
static inline float uitofp_i16_f32(uint16_t x)
{
    return (float) x;
}
static inline float uitofp_i32_f32(uint32_t x)
{
    return (float) x;
}
static inline float uitofp_i64_f32(uint64_t x)
{
    return (float) x;
}
static inline int8_t fptosi_f32_i8(float x)
{
    return (int8_t) x;
}
static inline int16_t fptosi_f32_i16(float x)
{
    return (int16_t) x;
}
static inline int32_t fptosi_f32_i32(float x)
{
    return (int32_t) x;
}
static inline int64_t fptosi_f32_i64(float x)
{
    return (int64_t) x;
}
static inline uint8_t fptoui_f32_i8(float x)
{
    return (uint8_t) x;
}
static inline uint16_t fptoui_f32_i16(float x)
{
    return (uint16_t) x;
}
static inline uint32_t fptoui_f32_i32(float x)
{
    return (uint32_t) x;
}
static inline uint64_t fptoui_f32_i64(float x)
{
    return (uint64_t) x;
}
static inline float futrts_log32(float x)
{
    return log(x);
}
static inline float futrts_log2_32(float x)
{
    return log2(x);
}
static inline float futrts_log10_32(float x)
{
    return log10(x);
}
static inline float futrts_sqrt32(float x)
{
    return sqrt(x);
}
static inline float futrts_exp32(float x)
{
    return exp(x);
}
static inline float futrts_cos32(float x)
{
    return cos(x);
}
static inline float futrts_sin32(float x)
{
    return sin(x);
}
static inline float futrts_tan32(float x)
{
    return tan(x);
}
static inline float futrts_acos32(float x)
{
    return acos(x);
}
static inline float futrts_asin32(float x)
{
    return asin(x);
}
static inline float futrts_atan32(float x)
{
    return atan(x);
}
static inline float futrts_atan2_32(float x, float y)
{
    return atan2(x, y);
}
static inline float futrts_gamma32(float x)
{
    return tgamma(x);
}
static inline float futrts_lgamma32(float x)
{
    return lgamma(x);
}
static inline bool futrts_isnan32(float x)
{
    return isnan(x);
}
static inline bool futrts_isinf32(float x)
{
    return isinf(x);
}
static inline int32_t futrts_to_bits32(float x)
{
    union {
        float f;
        int32_t t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline float futrts_from_bits32(int32_t x)
{
    union {
        int32_t f;
        float t;
    } p;
    
    p.f = x;
    return p.t;
}
#ifdef __OPENCL_VERSION__
static inline float fmod32(float x, float y)
{
    return fmod(x, y);
}
static inline float futrts_round32(float x)
{
    return rint(x);
}
static inline float futrts_floor32(float x)
{
    return floor(x);
}
static inline float futrts_ceil32(float x)
{
    return ceil(x);
}
static inline float futrts_lerp32(float v0, float v1, float t)
{
    return mix(v0, v1, t);
}
#else
static inline float fmod32(float x, float y)
{
    return fmodf(x, y);
}
static inline float futrts_round32(float x)
{
    return rintf(x);
}
static inline float futrts_floor32(float x)
{
    return floorf(x);
}
static inline float futrts_ceil32(float x)
{
    return ceilf(x);
}
static inline float futrts_lerp32(float v0, float v1, float t)
{
    return v0 + (v1 - v0) * t;
}
#endif
static inline double fdiv64(double x, double y)
{
    return x / y;
}
static inline double fadd64(double x, double y)
{
    return x + y;
}
static inline double fsub64(double x, double y)
{
    return x - y;
}
static inline double fmul64(double x, double y)
{
    return x * y;
}
static inline double fmin64(double x, double y)
{
    return fmin(x, y);
}
static inline double fmax64(double x, double y)
{
    return fmax(x, y);
}
static inline double fpow64(double x, double y)
{
    return pow(x, y);
}
static inline bool cmplt64(double x, double y)
{
    return x < y;
}
static inline bool cmple64(double x, double y)
{
    return x <= y;
}
static inline double sitofp_i8_f64(int8_t x)
{
    return (double) x;
}
static inline double sitofp_i16_f64(int16_t x)
{
    return (double) x;
}
static inline double sitofp_i32_f64(int32_t x)
{
    return (double) x;
}
static inline double sitofp_i64_f64(int64_t x)
{
    return (double) x;
}
static inline double uitofp_i8_f64(uint8_t x)
{
    return (double) x;
}
static inline double uitofp_i16_f64(uint16_t x)
{
    return (double) x;
}
static inline double uitofp_i32_f64(uint32_t x)
{
    return (double) x;
}
static inline double uitofp_i64_f64(uint64_t x)
{
    return (double) x;
}
static inline int8_t fptosi_f64_i8(double x)
{
    return (int8_t) x;
}
static inline int16_t fptosi_f64_i16(double x)
{
    return (int16_t) x;
}
static inline int32_t fptosi_f64_i32(double x)
{
    return (int32_t) x;
}
static inline int64_t fptosi_f64_i64(double x)
{
    return (int64_t) x;
}
static inline uint8_t fptoui_f64_i8(double x)
{
    return (uint8_t) x;
}
static inline uint16_t fptoui_f64_i16(double x)
{
    return (uint16_t) x;
}
static inline uint32_t fptoui_f64_i32(double x)
{
    return (uint32_t) x;
}
static inline uint64_t fptoui_f64_i64(double x)
{
    return (uint64_t) x;
}
static inline double futrts_log64(double x)
{
    return log(x);
}
static inline double futrts_log2_64(double x)
{
    return log2(x);
}
static inline double futrts_log10_64(double x)
{
    return log10(x);
}
static inline double futrts_sqrt64(double x)
{
    return sqrt(x);
}
static inline double futrts_exp64(double x)
{
    return exp(x);
}
static inline double futrts_cos64(double x)
{
    return cos(x);
}
static inline double futrts_sin64(double x)
{
    return sin(x);
}
static inline double futrts_tan64(double x)
{
    return tan(x);
}
static inline double futrts_acos64(double x)
{
    return acos(x);
}
static inline double futrts_asin64(double x)
{
    return asin(x);
}
static inline double futrts_atan64(double x)
{
    return atan(x);
}
static inline double futrts_atan2_64(double x, double y)
{
    return atan2(x, y);
}
static inline double futrts_gamma64(double x)
{
    return tgamma(x);
}
static inline double futrts_lgamma64(double x)
{
    return lgamma(x);
}
static inline double futrts_round64(double x)
{
    return rint(x);
}
static inline double futrts_ceil64(double x)
{
    return ceil(x);
}
static inline double futrts_floor64(double x)
{
    return floor(x);
}
static inline bool futrts_isnan64(double x)
{
    return isnan(x);
}
static inline bool futrts_isinf64(double x)
{
    return isinf(x);
}
static inline int64_t futrts_to_bits64(double x)
{
    union {
        double f;
        int64_t t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline double futrts_from_bits64(int64_t x)
{
    union {
        int64_t f;
        double t;
    } p;
    
    p.f = x;
    return p.t;
}
static inline float fmod64(float x, float y)
{
    return fmod(x, y);
}
#ifdef __OPENCL_VERSION__
static inline double futrts_lerp64(double v0, double v1, double t)
{
    return mix(v0, v1, t);
}
#else
static inline double futrts_lerp64(double v0, double v1, double t)
{
    return v0 + (v1 - v0) * t;
}
#endif
static inline float fpconv_f32_f32(float x)
{
    return (float) x;
}
static inline double fpconv_f32_f64(float x)
{
    return (double) x;
}
static inline float fpconv_f64_f32(double x)
{
    return (float) x;
}
static inline double fpconv_f64_f64(double x)
{
    return (double) x;
}
__kernel void segred_nonseg_10036(__local volatile
                                  int64_t *sync_arr_mem_10289_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10291_backing_aligned_1,
                                  int32_t sizze_9764, int32_t num_groups_10031,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10231, __global
                                  unsigned char *counter_mem_10279, __global
                                  unsigned char *group_res_arr_mem_10281,
                                  int32_t num_threads_10283)
{
    const int32_t segred_group_sizze_10029 =
                  entropy_f64zisegred_group_sizze_10028;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10289_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10289_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10291_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10291_backing_aligned_1;
    int32_t global_tid_10284;
    int32_t local_tid_10285;
    int32_t group_sizze_10288;
    int32_t wave_sizze_10287;
    int32_t group_tid_10286;
    
    global_tid_10284 = get_global_id(0);
    local_tid_10285 = get_local_id(0);
    group_sizze_10288 = get_local_size(0);
    wave_sizze_10287 = LOCKSTEP_WIDTH;
    group_tid_10286 = get_group_id(0);
    
    int32_t phys_tid_10036 = global_tid_10284;
    __local char *sync_arr_mem_10289;
    
    sync_arr_mem_10289 = (__local char *) sync_arr_mem_10289_backing_0;
    
    __local char *red_arr_mem_10291;
    
    red_arr_mem_10291 = (__local char *) red_arr_mem_10291_backing_1;
    
    int32_t dummy_10034 = 0;
    int32_t gtid_10035;
    
    gtid_10035 = 0;
    
    double x_acc_10293;
    int32_t chunk_sizze_10294 = smin32(squot32(sizze_9764 +
                                               segred_group_sizze_10029 *
                                               num_groups_10031 - 1,
                                               segred_group_sizze_10029 *
                                               num_groups_10031),
                                       squot32(sizze_9764 - phys_tid_10036 +
                                               num_threads_10283 - 1,
                                               num_threads_10283));
    double x_9767;
    double x_9768;
    
    // neutral-initialise the accumulators
    {
        x_acc_10293 = 0.0;
    }
    for (int32_t i_10298 = 0; i_10298 < chunk_sizze_10294; i_10298++) {
        gtid_10035 = phys_tid_10036 + num_threads_10283 * i_10298;
        // apply map function
        {
            double x_9770 = ((__global double *) x_mem_10227)[gtid_10035];
            double res_9771;
            
            res_9771 = futrts_log64(x_9770);
            
            double res_9772 = x_9770 * res_9771;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9767 = x_acc_10293;
            }
            // load new values
            {
                x_9768 = res_9772;
            }
            // apply reduction operator
            {
                double res_9769 = x_9767 + x_9768;
                
                // store in accumulator
                {
                    x_acc_10293 = res_9769;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9767 = x_acc_10293;
        ((__local double *) red_arr_mem_10291)[local_tid_10285] = x_9767;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10299;
    int32_t skip_waves_10300;
    double x_10295;
    double x_10296;
    
    offset_10299 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10285, segred_group_sizze_10029)) {
            x_10295 = ((__local double *) red_arr_mem_10291)[local_tid_10285 +
                                                             offset_10299];
        }
    }
    offset_10299 = 1;
    while (slt32(offset_10299, wave_sizze_10287)) {
        if (slt32(local_tid_10285 + offset_10299, segred_group_sizze_10029) &&
            ((local_tid_10285 - squot32(local_tid_10285, wave_sizze_10287) *
              wave_sizze_10287) & (2 * offset_10299 - 1)) == 0) {
            // read array element
            {
                x_10296 = ((volatile __local
                            double *) red_arr_mem_10291)[local_tid_10285 +
                                                         offset_10299];
            }
            // apply reduction operation
            {
                double res_10297 = x_10295 + x_10296;
                
                x_10295 = res_10297;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10291)[local_tid_10285] = x_10295;
            }
        }
        offset_10299 *= 2;
    }
    skip_waves_10300 = 1;
    while (slt32(skip_waves_10300, squot32(segred_group_sizze_10029 +
                                           wave_sizze_10287 - 1,
                                           wave_sizze_10287))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10299 = skip_waves_10300 * wave_sizze_10287;
        if (slt32(local_tid_10285 + offset_10299, segred_group_sizze_10029) &&
            ((local_tid_10285 - squot32(local_tid_10285, wave_sizze_10287) *
              wave_sizze_10287) == 0 && (squot32(local_tid_10285,
                                                 wave_sizze_10287) & (2 *
                                                                      skip_waves_10300 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10296 = ((__local
                            double *) red_arr_mem_10291)[local_tid_10285 +
                                                         offset_10299];
            }
            // apply reduction operation
            {
                double res_10297 = x_10295 + x_10296;
                
                x_10295 = res_10297;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10291)[local_tid_10285] =
                    x_10295;
            }
        }
        skip_waves_10300 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10285 == 0) {
            x_acc_10293 = x_10295;
        }
    }
    
    int32_t old_counter_10301;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10285 == 0) {
            ((__global double *) group_res_arr_mem_10281)[group_tid_10286 *
                                                          segred_group_sizze_10029] =
                x_acc_10293;
            mem_fence_global();
            old_counter_10301 = atomic_add(&((volatile __global
                                              int *) counter_mem_10279)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10289)[0] = old_counter_10301 ==
                num_groups_10031 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10302 = ((__local bool *) sync_arr_mem_10289)[0];
    
    if (is_last_group_10302) {
        if (local_tid_10285 == 0) {
            old_counter_10301 = atomic_add(&((volatile __global
                                              int *) counter_mem_10279)[0],
                                           (int) (0 - num_groups_10031));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10285, num_groups_10031)) {
                x_9767 = ((__global
                           double *) group_res_arr_mem_10281)[local_tid_10285 *
                                                              segred_group_sizze_10029];
            } else {
                x_9767 = 0.0;
            }
            ((__local double *) red_arr_mem_10291)[local_tid_10285] = x_9767;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10303;
            int32_t skip_waves_10304;
            double x_10295;
            double x_10296;
            
            offset_10303 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10285, segred_group_sizze_10029)) {
                    x_10295 = ((__local
                                double *) red_arr_mem_10291)[local_tid_10285 +
                                                             offset_10303];
                }
            }
            offset_10303 = 1;
            while (slt32(offset_10303, wave_sizze_10287)) {
                if (slt32(local_tid_10285 + offset_10303,
                          segred_group_sizze_10029) && ((local_tid_10285 -
                                                         squot32(local_tid_10285,
                                                                 wave_sizze_10287) *
                                                         wave_sizze_10287) &
                                                        (2 * offset_10303 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10296 = ((volatile __local
                                    double *) red_arr_mem_10291)[local_tid_10285 +
                                                                 offset_10303];
                    }
                    // apply reduction operation
                    {
                        double res_10297 = x_10295 + x_10296;
                        
                        x_10295 = res_10297;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10291)[local_tid_10285] =
                            x_10295;
                    }
                }
                offset_10303 *= 2;
            }
            skip_waves_10304 = 1;
            while (slt32(skip_waves_10304, squot32(segred_group_sizze_10029 +
                                                   wave_sizze_10287 - 1,
                                                   wave_sizze_10287))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10303 = skip_waves_10304 * wave_sizze_10287;
                if (slt32(local_tid_10285 + offset_10303,
                          segred_group_sizze_10029) && ((local_tid_10285 -
                                                         squot32(local_tid_10285,
                                                                 wave_sizze_10287) *
                                                         wave_sizze_10287) ==
                                                        0 &&
                                                        (squot32(local_tid_10285,
                                                                 wave_sizze_10287) &
                                                         (2 * skip_waves_10304 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10296 = ((__local
                                    double *) red_arr_mem_10291)[local_tid_10285 +
                                                                 offset_10303];
                    }
                    // apply reduction operation
                    {
                        double res_10297 = x_10295 + x_10296;
                        
                        x_10295 = res_10297;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10291)[local_tid_10285] =
                            x_10295;
                    }
                }
                skip_waves_10304 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10285 == 0) {
                    ((__global double *) mem_10231)[0] = x_10295;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10047(__local volatile
                                  int64_t *sync_arr_mem_10317_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10319_backing_aligned_1,
                                  int32_t sizze_9774, int32_t num_groups_10042,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10231, __global
                                  unsigned char *counter_mem_10307, __global
                                  unsigned char *group_res_arr_mem_10309,
                                  int32_t num_threads_10311)
{
    const int32_t segred_group_sizze_10040 =
                  entropy_f32zisegred_group_sizze_10039;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10317_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10317_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10319_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10319_backing_aligned_1;
    int32_t global_tid_10312;
    int32_t local_tid_10313;
    int32_t group_sizze_10316;
    int32_t wave_sizze_10315;
    int32_t group_tid_10314;
    
    global_tid_10312 = get_global_id(0);
    local_tid_10313 = get_local_id(0);
    group_sizze_10316 = get_local_size(0);
    wave_sizze_10315 = LOCKSTEP_WIDTH;
    group_tid_10314 = get_group_id(0);
    
    int32_t phys_tid_10047 = global_tid_10312;
    __local char *sync_arr_mem_10317;
    
    sync_arr_mem_10317 = (__local char *) sync_arr_mem_10317_backing_0;
    
    __local char *red_arr_mem_10319;
    
    red_arr_mem_10319 = (__local char *) red_arr_mem_10319_backing_1;
    
    int32_t dummy_10045 = 0;
    int32_t gtid_10046;
    
    gtid_10046 = 0;
    
    float x_acc_10321;
    int32_t chunk_sizze_10322 = smin32(squot32(sizze_9774 +
                                               segred_group_sizze_10040 *
                                               num_groups_10042 - 1,
                                               segred_group_sizze_10040 *
                                               num_groups_10042),
                                       squot32(sizze_9774 - phys_tid_10047 +
                                               num_threads_10311 - 1,
                                               num_threads_10311));
    float x_9777;
    float x_9778;
    
    // neutral-initialise the accumulators
    {
        x_acc_10321 = 0.0F;
    }
    for (int32_t i_10326 = 0; i_10326 < chunk_sizze_10322; i_10326++) {
        gtid_10046 = phys_tid_10047 + num_threads_10311 * i_10326;
        // apply map function
        {
            float x_9780 = ((__global float *) x_mem_10227)[gtid_10046];
            float res_9781;
            
            res_9781 = futrts_log32(x_9780);
            
            float res_9782 = x_9780 * res_9781;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9777 = x_acc_10321;
            }
            // load new values
            {
                x_9778 = res_9782;
            }
            // apply reduction operator
            {
                float res_9779 = x_9777 + x_9778;
                
                // store in accumulator
                {
                    x_acc_10321 = res_9779;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9777 = x_acc_10321;
        ((__local float *) red_arr_mem_10319)[local_tid_10313] = x_9777;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10327;
    int32_t skip_waves_10328;
    float x_10323;
    float x_10324;
    
    offset_10327 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10313, segred_group_sizze_10040)) {
            x_10323 = ((__local float *) red_arr_mem_10319)[local_tid_10313 +
                                                            offset_10327];
        }
    }
    offset_10327 = 1;
    while (slt32(offset_10327, wave_sizze_10315)) {
        if (slt32(local_tid_10313 + offset_10327, segred_group_sizze_10040) &&
            ((local_tid_10313 - squot32(local_tid_10313, wave_sizze_10315) *
              wave_sizze_10315) & (2 * offset_10327 - 1)) == 0) {
            // read array element
            {
                x_10324 = ((volatile __local
                            float *) red_arr_mem_10319)[local_tid_10313 +
                                                        offset_10327];
            }
            // apply reduction operation
            {
                float res_10325 = x_10323 + x_10324;
                
                x_10323 = res_10325;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10319)[local_tid_10313] = x_10323;
            }
        }
        offset_10327 *= 2;
    }
    skip_waves_10328 = 1;
    while (slt32(skip_waves_10328, squot32(segred_group_sizze_10040 +
                                           wave_sizze_10315 - 1,
                                           wave_sizze_10315))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10327 = skip_waves_10328 * wave_sizze_10315;
        if (slt32(local_tid_10313 + offset_10327, segred_group_sizze_10040) &&
            ((local_tid_10313 - squot32(local_tid_10313, wave_sizze_10315) *
              wave_sizze_10315) == 0 && (squot32(local_tid_10313,
                                                 wave_sizze_10315) & (2 *
                                                                      skip_waves_10328 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10324 = ((__local
                            float *) red_arr_mem_10319)[local_tid_10313 +
                                                        offset_10327];
            }
            // apply reduction operation
            {
                float res_10325 = x_10323 + x_10324;
                
                x_10323 = res_10325;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10319)[local_tid_10313] =
                    x_10323;
            }
        }
        skip_waves_10328 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10313 == 0) {
            x_acc_10321 = x_10323;
        }
    }
    
    int32_t old_counter_10329;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10313 == 0) {
            ((__global float *) group_res_arr_mem_10309)[group_tid_10314 *
                                                         segred_group_sizze_10040] =
                x_acc_10321;
            mem_fence_global();
            old_counter_10329 = atomic_add(&((volatile __global
                                              int *) counter_mem_10307)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10317)[0] = old_counter_10329 ==
                num_groups_10042 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10330 = ((__local bool *) sync_arr_mem_10317)[0];
    
    if (is_last_group_10330) {
        if (local_tid_10313 == 0) {
            old_counter_10329 = atomic_add(&((volatile __global
                                              int *) counter_mem_10307)[0],
                                           (int) (0 - num_groups_10042));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10313, num_groups_10042)) {
                x_9777 = ((__global
                           float *) group_res_arr_mem_10309)[local_tid_10313 *
                                                             segred_group_sizze_10040];
            } else {
                x_9777 = 0.0F;
            }
            ((__local float *) red_arr_mem_10319)[local_tid_10313] = x_9777;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10331;
            int32_t skip_waves_10332;
            float x_10323;
            float x_10324;
            
            offset_10331 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10313, segred_group_sizze_10040)) {
                    x_10323 = ((__local
                                float *) red_arr_mem_10319)[local_tid_10313 +
                                                            offset_10331];
                }
            }
            offset_10331 = 1;
            while (slt32(offset_10331, wave_sizze_10315)) {
                if (slt32(local_tid_10313 + offset_10331,
                          segred_group_sizze_10040) && ((local_tid_10313 -
                                                         squot32(local_tid_10313,
                                                                 wave_sizze_10315) *
                                                         wave_sizze_10315) &
                                                        (2 * offset_10331 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10324 = ((volatile __local
                                    float *) red_arr_mem_10319)[local_tid_10313 +
                                                                offset_10331];
                    }
                    // apply reduction operation
                    {
                        float res_10325 = x_10323 + x_10324;
                        
                        x_10323 = res_10325;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10319)[local_tid_10313] =
                            x_10323;
                    }
                }
                offset_10331 *= 2;
            }
            skip_waves_10332 = 1;
            while (slt32(skip_waves_10332, squot32(segred_group_sizze_10040 +
                                                   wave_sizze_10315 - 1,
                                                   wave_sizze_10315))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10331 = skip_waves_10332 * wave_sizze_10315;
                if (slt32(local_tid_10313 + offset_10331,
                          segred_group_sizze_10040) && ((local_tid_10313 -
                                                         squot32(local_tid_10313,
                                                                 wave_sizze_10315) *
                                                         wave_sizze_10315) ==
                                                        0 &&
                                                        (squot32(local_tid_10313,
                                                                 wave_sizze_10315) &
                                                         (2 * skip_waves_10332 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10324 = ((__local
                                    float *) red_arr_mem_10319)[local_tid_10313 +
                                                                offset_10331];
                    }
                    // apply reduction operation
                    {
                        float res_10325 = x_10323 + x_10324;
                        
                        x_10323 = res_10325;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10319)[local_tid_10313] =
                            x_10323;
                    }
                }
                skip_waves_10332 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10313 == 0) {
                    ((__global float *) mem_10231)[0] = x_10323;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10058(__local volatile
                                  int64_t *sync_arr_mem_10345_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10347_backing_aligned_1,
                                  int32_t sizze_9784, int32_t num_groups_10053,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10231, __global
                                  unsigned char *counter_mem_10335, __global
                                  unsigned char *group_res_arr_mem_10337,
                                  int32_t num_threads_10339)
{
    const int32_t segred_group_sizze_10051 =
                  entropy_scaled_f64zisegred_group_sizze_10050;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10345_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10345_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10347_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10347_backing_aligned_1;
    int32_t global_tid_10340;
    int32_t local_tid_10341;
    int32_t group_sizze_10344;
    int32_t wave_sizze_10343;
    int32_t group_tid_10342;
    
    global_tid_10340 = get_global_id(0);
    local_tid_10341 = get_local_id(0);
    group_sizze_10344 = get_local_size(0);
    wave_sizze_10343 = LOCKSTEP_WIDTH;
    group_tid_10342 = get_group_id(0);
    
    int32_t phys_tid_10058 = global_tid_10340;
    __local char *sync_arr_mem_10345;
    
    sync_arr_mem_10345 = (__local char *) sync_arr_mem_10345_backing_0;
    
    __local char *red_arr_mem_10347;
    
    red_arr_mem_10347 = (__local char *) red_arr_mem_10347_backing_1;
    
    int32_t dummy_10056 = 0;
    int32_t gtid_10057;
    
    gtid_10057 = 0;
    
    double x_acc_10349;
    int32_t chunk_sizze_10350 = smin32(squot32(sizze_9784 +
                                               segred_group_sizze_10051 *
                                               num_groups_10053 - 1,
                                               segred_group_sizze_10051 *
                                               num_groups_10053),
                                       squot32(sizze_9784 - phys_tid_10058 +
                                               num_threads_10339 - 1,
                                               num_threads_10339));
    double x_9787;
    double x_9788;
    
    // neutral-initialise the accumulators
    {
        x_acc_10349 = 0.0;
    }
    for (int32_t i_10354 = 0; i_10354 < chunk_sizze_10350; i_10354++) {
        gtid_10057 = phys_tid_10058 + num_threads_10339 * i_10354;
        // apply map function
        {
            double x_9790 = ((__global double *) x_mem_10227)[gtid_10057];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9787 = x_acc_10349;
            }
            // load new values
            {
                x_9788 = x_9790;
            }
            // apply reduction operator
            {
                double res_9789 = x_9787 + x_9788;
                
                // store in accumulator
                {
                    x_acc_10349 = res_9789;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9787 = x_acc_10349;
        ((__local double *) red_arr_mem_10347)[local_tid_10341] = x_9787;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10355;
    int32_t skip_waves_10356;
    double x_10351;
    double x_10352;
    
    offset_10355 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10341, segred_group_sizze_10051)) {
            x_10351 = ((__local double *) red_arr_mem_10347)[local_tid_10341 +
                                                             offset_10355];
        }
    }
    offset_10355 = 1;
    while (slt32(offset_10355, wave_sizze_10343)) {
        if (slt32(local_tid_10341 + offset_10355, segred_group_sizze_10051) &&
            ((local_tid_10341 - squot32(local_tid_10341, wave_sizze_10343) *
              wave_sizze_10343) & (2 * offset_10355 - 1)) == 0) {
            // read array element
            {
                x_10352 = ((volatile __local
                            double *) red_arr_mem_10347)[local_tid_10341 +
                                                         offset_10355];
            }
            // apply reduction operation
            {
                double res_10353 = x_10351 + x_10352;
                
                x_10351 = res_10353;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10347)[local_tid_10341] = x_10351;
            }
        }
        offset_10355 *= 2;
    }
    skip_waves_10356 = 1;
    while (slt32(skip_waves_10356, squot32(segred_group_sizze_10051 +
                                           wave_sizze_10343 - 1,
                                           wave_sizze_10343))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10355 = skip_waves_10356 * wave_sizze_10343;
        if (slt32(local_tid_10341 + offset_10355, segred_group_sizze_10051) &&
            ((local_tid_10341 - squot32(local_tid_10341, wave_sizze_10343) *
              wave_sizze_10343) == 0 && (squot32(local_tid_10341,
                                                 wave_sizze_10343) & (2 *
                                                                      skip_waves_10356 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10352 = ((__local
                            double *) red_arr_mem_10347)[local_tid_10341 +
                                                         offset_10355];
            }
            // apply reduction operation
            {
                double res_10353 = x_10351 + x_10352;
                
                x_10351 = res_10353;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10347)[local_tid_10341] =
                    x_10351;
            }
        }
        skip_waves_10356 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10341 == 0) {
            x_acc_10349 = x_10351;
        }
    }
    
    int32_t old_counter_10357;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10341 == 0) {
            ((__global double *) group_res_arr_mem_10337)[group_tid_10342 *
                                                          segred_group_sizze_10051] =
                x_acc_10349;
            mem_fence_global();
            old_counter_10357 = atomic_add(&((volatile __global
                                              int *) counter_mem_10335)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10345)[0] = old_counter_10357 ==
                num_groups_10053 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10358 = ((__local bool *) sync_arr_mem_10345)[0];
    
    if (is_last_group_10358) {
        if (local_tid_10341 == 0) {
            old_counter_10357 = atomic_add(&((volatile __global
                                              int *) counter_mem_10335)[0],
                                           (int) (0 - num_groups_10053));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10341, num_groups_10053)) {
                x_9787 = ((__global
                           double *) group_res_arr_mem_10337)[local_tid_10341 *
                                                              segred_group_sizze_10051];
            } else {
                x_9787 = 0.0;
            }
            ((__local double *) red_arr_mem_10347)[local_tid_10341] = x_9787;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10359;
            int32_t skip_waves_10360;
            double x_10351;
            double x_10352;
            
            offset_10359 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10341, segred_group_sizze_10051)) {
                    x_10351 = ((__local
                                double *) red_arr_mem_10347)[local_tid_10341 +
                                                             offset_10359];
                }
            }
            offset_10359 = 1;
            while (slt32(offset_10359, wave_sizze_10343)) {
                if (slt32(local_tid_10341 + offset_10359,
                          segred_group_sizze_10051) && ((local_tid_10341 -
                                                         squot32(local_tid_10341,
                                                                 wave_sizze_10343) *
                                                         wave_sizze_10343) &
                                                        (2 * offset_10359 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10352 = ((volatile __local
                                    double *) red_arr_mem_10347)[local_tid_10341 +
                                                                 offset_10359];
                    }
                    // apply reduction operation
                    {
                        double res_10353 = x_10351 + x_10352;
                        
                        x_10351 = res_10353;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10347)[local_tid_10341] =
                            x_10351;
                    }
                }
                offset_10359 *= 2;
            }
            skip_waves_10360 = 1;
            while (slt32(skip_waves_10360, squot32(segred_group_sizze_10051 +
                                                   wave_sizze_10343 - 1,
                                                   wave_sizze_10343))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10359 = skip_waves_10360 * wave_sizze_10343;
                if (slt32(local_tid_10341 + offset_10359,
                          segred_group_sizze_10051) && ((local_tid_10341 -
                                                         squot32(local_tid_10341,
                                                                 wave_sizze_10343) *
                                                         wave_sizze_10343) ==
                                                        0 &&
                                                        (squot32(local_tid_10341,
                                                                 wave_sizze_10343) &
                                                         (2 * skip_waves_10360 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10352 = ((__local
                                    double *) red_arr_mem_10347)[local_tid_10341 +
                                                                 offset_10359];
                    }
                    // apply reduction operation
                    {
                        double res_10353 = x_10351 + x_10352;
                        
                        x_10351 = res_10353;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10347)[local_tid_10341] =
                            x_10351;
                    }
                }
                skip_waves_10360 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10341 == 0) {
                    ((__global double *) mem_10231)[0] = x_10351;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10069(__local volatile
                                  int64_t *sync_arr_mem_10372_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10374_backing_aligned_1,
                                  int32_t sizze_9784, double res_9786,
                                  int32_t num_groups_10064, __global
                                  unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10235, __global
                                  unsigned char *counter_mem_10362, __global
                                  unsigned char *group_res_arr_mem_10364,
                                  int32_t num_threads_10366)
{
    const int32_t segred_group_sizze_10062 =
                  entropy_scaled_f64zisegred_group_sizze_10061;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10372_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10372_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10374_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10374_backing_aligned_1;
    int32_t global_tid_10367;
    int32_t local_tid_10368;
    int32_t group_sizze_10371;
    int32_t wave_sizze_10370;
    int32_t group_tid_10369;
    
    global_tid_10367 = get_global_id(0);
    local_tid_10368 = get_local_id(0);
    group_sizze_10371 = get_local_size(0);
    wave_sizze_10370 = LOCKSTEP_WIDTH;
    group_tid_10369 = get_group_id(0);
    
    int32_t phys_tid_10069 = global_tid_10367;
    __local char *sync_arr_mem_10372;
    
    sync_arr_mem_10372 = (__local char *) sync_arr_mem_10372_backing_0;
    
    __local char *red_arr_mem_10374;
    
    red_arr_mem_10374 = (__local char *) red_arr_mem_10374_backing_1;
    
    int32_t dummy_10067 = 0;
    int32_t gtid_10068;
    
    gtid_10068 = 0;
    
    double x_acc_10376;
    int32_t chunk_sizze_10377 = smin32(squot32(sizze_9784 +
                                               segred_group_sizze_10062 *
                                               num_groups_10064 - 1,
                                               segred_group_sizze_10062 *
                                               num_groups_10064),
                                       squot32(sizze_9784 - phys_tid_10069 +
                                               num_threads_10366 - 1,
                                               num_threads_10366));
    double x_9792;
    double x_9793;
    
    // neutral-initialise the accumulators
    {
        x_acc_10376 = 0.0;
    }
    for (int32_t i_10381 = 0; i_10381 < chunk_sizze_10377; i_10381++) {
        gtid_10068 = phys_tid_10069 + num_threads_10366 * i_10381;
        // apply map function
        {
            double x_9795 = ((__global double *) x_mem_10227)[gtid_10068];
            double res_9796 = x_9795 / res_9786;
            double res_9797;
            
            res_9797 = futrts_log64(res_9796);
            
            double res_9798 = res_9796 * res_9797;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9792 = x_acc_10376;
            }
            // load new values
            {
                x_9793 = res_9798;
            }
            // apply reduction operator
            {
                double res_9794 = x_9792 + x_9793;
                
                // store in accumulator
                {
                    x_acc_10376 = res_9794;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9792 = x_acc_10376;
        ((__local double *) red_arr_mem_10374)[local_tid_10368] = x_9792;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10382;
    int32_t skip_waves_10383;
    double x_10378;
    double x_10379;
    
    offset_10382 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10368, segred_group_sizze_10062)) {
            x_10378 = ((__local double *) red_arr_mem_10374)[local_tid_10368 +
                                                             offset_10382];
        }
    }
    offset_10382 = 1;
    while (slt32(offset_10382, wave_sizze_10370)) {
        if (slt32(local_tid_10368 + offset_10382, segred_group_sizze_10062) &&
            ((local_tid_10368 - squot32(local_tid_10368, wave_sizze_10370) *
              wave_sizze_10370) & (2 * offset_10382 - 1)) == 0) {
            // read array element
            {
                x_10379 = ((volatile __local
                            double *) red_arr_mem_10374)[local_tid_10368 +
                                                         offset_10382];
            }
            // apply reduction operation
            {
                double res_10380 = x_10378 + x_10379;
                
                x_10378 = res_10380;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10374)[local_tid_10368] = x_10378;
            }
        }
        offset_10382 *= 2;
    }
    skip_waves_10383 = 1;
    while (slt32(skip_waves_10383, squot32(segred_group_sizze_10062 +
                                           wave_sizze_10370 - 1,
                                           wave_sizze_10370))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10382 = skip_waves_10383 * wave_sizze_10370;
        if (slt32(local_tid_10368 + offset_10382, segred_group_sizze_10062) &&
            ((local_tid_10368 - squot32(local_tid_10368, wave_sizze_10370) *
              wave_sizze_10370) == 0 && (squot32(local_tid_10368,
                                                 wave_sizze_10370) & (2 *
                                                                      skip_waves_10383 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10379 = ((__local
                            double *) red_arr_mem_10374)[local_tid_10368 +
                                                         offset_10382];
            }
            // apply reduction operation
            {
                double res_10380 = x_10378 + x_10379;
                
                x_10378 = res_10380;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10374)[local_tid_10368] =
                    x_10378;
            }
        }
        skip_waves_10383 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10368 == 0) {
            x_acc_10376 = x_10378;
        }
    }
    
    int32_t old_counter_10384;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10368 == 0) {
            ((__global double *) group_res_arr_mem_10364)[group_tid_10369 *
                                                          segred_group_sizze_10062] =
                x_acc_10376;
            mem_fence_global();
            old_counter_10384 = atomic_add(&((volatile __global
                                              int *) counter_mem_10362)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10372)[0] = old_counter_10384 ==
                num_groups_10064 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10385 = ((__local bool *) sync_arr_mem_10372)[0];
    
    if (is_last_group_10385) {
        if (local_tid_10368 == 0) {
            old_counter_10384 = atomic_add(&((volatile __global
                                              int *) counter_mem_10362)[0],
                                           (int) (0 - num_groups_10064));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10368, num_groups_10064)) {
                x_9792 = ((__global
                           double *) group_res_arr_mem_10364)[local_tid_10368 *
                                                              segred_group_sizze_10062];
            } else {
                x_9792 = 0.0;
            }
            ((__local double *) red_arr_mem_10374)[local_tid_10368] = x_9792;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10386;
            int32_t skip_waves_10387;
            double x_10378;
            double x_10379;
            
            offset_10386 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10368, segred_group_sizze_10062)) {
                    x_10378 = ((__local
                                double *) red_arr_mem_10374)[local_tid_10368 +
                                                             offset_10386];
                }
            }
            offset_10386 = 1;
            while (slt32(offset_10386, wave_sizze_10370)) {
                if (slt32(local_tid_10368 + offset_10386,
                          segred_group_sizze_10062) && ((local_tid_10368 -
                                                         squot32(local_tid_10368,
                                                                 wave_sizze_10370) *
                                                         wave_sizze_10370) &
                                                        (2 * offset_10386 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10379 = ((volatile __local
                                    double *) red_arr_mem_10374)[local_tid_10368 +
                                                                 offset_10386];
                    }
                    // apply reduction operation
                    {
                        double res_10380 = x_10378 + x_10379;
                        
                        x_10378 = res_10380;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10374)[local_tid_10368] =
                            x_10378;
                    }
                }
                offset_10386 *= 2;
            }
            skip_waves_10387 = 1;
            while (slt32(skip_waves_10387, squot32(segred_group_sizze_10062 +
                                                   wave_sizze_10370 - 1,
                                                   wave_sizze_10370))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10386 = skip_waves_10387 * wave_sizze_10370;
                if (slt32(local_tid_10368 + offset_10386,
                          segred_group_sizze_10062) && ((local_tid_10368 -
                                                         squot32(local_tid_10368,
                                                                 wave_sizze_10370) *
                                                         wave_sizze_10370) ==
                                                        0 &&
                                                        (squot32(local_tid_10368,
                                                                 wave_sizze_10370) &
                                                         (2 * skip_waves_10387 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10379 = ((__local
                                    double *) red_arr_mem_10374)[local_tid_10368 +
                                                                 offset_10386];
                    }
                    // apply reduction operation
                    {
                        double res_10380 = x_10378 + x_10379;
                        
                        x_10378 = res_10380;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10374)[local_tid_10368] =
                            x_10378;
                    }
                }
                skip_waves_10387 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10368 == 0) {
                    ((__global double *) mem_10235)[0] = x_10378;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10080(__local volatile
                                  int64_t *sync_arr_mem_10400_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10402_backing_aligned_1,
                                  int32_t sizze_9800, int32_t num_groups_10075,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10231, __global
                                  unsigned char *counter_mem_10390, __global
                                  unsigned char *group_res_arr_mem_10392,
                                  int32_t num_threads_10394)
{
    const int32_t segred_group_sizze_10073 =
                  entropy_scaled_f32zisegred_group_sizze_10072;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10400_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10400_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10402_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10402_backing_aligned_1;
    int32_t global_tid_10395;
    int32_t local_tid_10396;
    int32_t group_sizze_10399;
    int32_t wave_sizze_10398;
    int32_t group_tid_10397;
    
    global_tid_10395 = get_global_id(0);
    local_tid_10396 = get_local_id(0);
    group_sizze_10399 = get_local_size(0);
    wave_sizze_10398 = LOCKSTEP_WIDTH;
    group_tid_10397 = get_group_id(0);
    
    int32_t phys_tid_10080 = global_tid_10395;
    __local char *sync_arr_mem_10400;
    
    sync_arr_mem_10400 = (__local char *) sync_arr_mem_10400_backing_0;
    
    __local char *red_arr_mem_10402;
    
    red_arr_mem_10402 = (__local char *) red_arr_mem_10402_backing_1;
    
    int32_t dummy_10078 = 0;
    int32_t gtid_10079;
    
    gtid_10079 = 0;
    
    float x_acc_10404;
    int32_t chunk_sizze_10405 = smin32(squot32(sizze_9800 +
                                               segred_group_sizze_10073 *
                                               num_groups_10075 - 1,
                                               segred_group_sizze_10073 *
                                               num_groups_10075),
                                       squot32(sizze_9800 - phys_tid_10080 +
                                               num_threads_10394 - 1,
                                               num_threads_10394));
    float x_9803;
    float x_9804;
    
    // neutral-initialise the accumulators
    {
        x_acc_10404 = 0.0F;
    }
    for (int32_t i_10409 = 0; i_10409 < chunk_sizze_10405; i_10409++) {
        gtid_10079 = phys_tid_10080 + num_threads_10394 * i_10409;
        // apply map function
        {
            float x_9806 = ((__global float *) x_mem_10227)[gtid_10079];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9803 = x_acc_10404;
            }
            // load new values
            {
                x_9804 = x_9806;
            }
            // apply reduction operator
            {
                float res_9805 = x_9803 + x_9804;
                
                // store in accumulator
                {
                    x_acc_10404 = res_9805;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9803 = x_acc_10404;
        ((__local float *) red_arr_mem_10402)[local_tid_10396] = x_9803;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10410;
    int32_t skip_waves_10411;
    float x_10406;
    float x_10407;
    
    offset_10410 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10396, segred_group_sizze_10073)) {
            x_10406 = ((__local float *) red_arr_mem_10402)[local_tid_10396 +
                                                            offset_10410];
        }
    }
    offset_10410 = 1;
    while (slt32(offset_10410, wave_sizze_10398)) {
        if (slt32(local_tid_10396 + offset_10410, segred_group_sizze_10073) &&
            ((local_tid_10396 - squot32(local_tid_10396, wave_sizze_10398) *
              wave_sizze_10398) & (2 * offset_10410 - 1)) == 0) {
            // read array element
            {
                x_10407 = ((volatile __local
                            float *) red_arr_mem_10402)[local_tid_10396 +
                                                        offset_10410];
            }
            // apply reduction operation
            {
                float res_10408 = x_10406 + x_10407;
                
                x_10406 = res_10408;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10402)[local_tid_10396] = x_10406;
            }
        }
        offset_10410 *= 2;
    }
    skip_waves_10411 = 1;
    while (slt32(skip_waves_10411, squot32(segred_group_sizze_10073 +
                                           wave_sizze_10398 - 1,
                                           wave_sizze_10398))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10410 = skip_waves_10411 * wave_sizze_10398;
        if (slt32(local_tid_10396 + offset_10410, segred_group_sizze_10073) &&
            ((local_tid_10396 - squot32(local_tid_10396, wave_sizze_10398) *
              wave_sizze_10398) == 0 && (squot32(local_tid_10396,
                                                 wave_sizze_10398) & (2 *
                                                                      skip_waves_10411 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10407 = ((__local
                            float *) red_arr_mem_10402)[local_tid_10396 +
                                                        offset_10410];
            }
            // apply reduction operation
            {
                float res_10408 = x_10406 + x_10407;
                
                x_10406 = res_10408;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10402)[local_tid_10396] =
                    x_10406;
            }
        }
        skip_waves_10411 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10396 == 0) {
            x_acc_10404 = x_10406;
        }
    }
    
    int32_t old_counter_10412;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10396 == 0) {
            ((__global float *) group_res_arr_mem_10392)[group_tid_10397 *
                                                         segred_group_sizze_10073] =
                x_acc_10404;
            mem_fence_global();
            old_counter_10412 = atomic_add(&((volatile __global
                                              int *) counter_mem_10390)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10400)[0] = old_counter_10412 ==
                num_groups_10075 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10413 = ((__local bool *) sync_arr_mem_10400)[0];
    
    if (is_last_group_10413) {
        if (local_tid_10396 == 0) {
            old_counter_10412 = atomic_add(&((volatile __global
                                              int *) counter_mem_10390)[0],
                                           (int) (0 - num_groups_10075));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10396, num_groups_10075)) {
                x_9803 = ((__global
                           float *) group_res_arr_mem_10392)[local_tid_10396 *
                                                             segred_group_sizze_10073];
            } else {
                x_9803 = 0.0F;
            }
            ((__local float *) red_arr_mem_10402)[local_tid_10396] = x_9803;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10414;
            int32_t skip_waves_10415;
            float x_10406;
            float x_10407;
            
            offset_10414 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10396, segred_group_sizze_10073)) {
                    x_10406 = ((__local
                                float *) red_arr_mem_10402)[local_tid_10396 +
                                                            offset_10414];
                }
            }
            offset_10414 = 1;
            while (slt32(offset_10414, wave_sizze_10398)) {
                if (slt32(local_tid_10396 + offset_10414,
                          segred_group_sizze_10073) && ((local_tid_10396 -
                                                         squot32(local_tid_10396,
                                                                 wave_sizze_10398) *
                                                         wave_sizze_10398) &
                                                        (2 * offset_10414 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10407 = ((volatile __local
                                    float *) red_arr_mem_10402)[local_tid_10396 +
                                                                offset_10414];
                    }
                    // apply reduction operation
                    {
                        float res_10408 = x_10406 + x_10407;
                        
                        x_10406 = res_10408;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10402)[local_tid_10396] =
                            x_10406;
                    }
                }
                offset_10414 *= 2;
            }
            skip_waves_10415 = 1;
            while (slt32(skip_waves_10415, squot32(segred_group_sizze_10073 +
                                                   wave_sizze_10398 - 1,
                                                   wave_sizze_10398))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10414 = skip_waves_10415 * wave_sizze_10398;
                if (slt32(local_tid_10396 + offset_10414,
                          segred_group_sizze_10073) && ((local_tid_10396 -
                                                         squot32(local_tid_10396,
                                                                 wave_sizze_10398) *
                                                         wave_sizze_10398) ==
                                                        0 &&
                                                        (squot32(local_tid_10396,
                                                                 wave_sizze_10398) &
                                                         (2 * skip_waves_10415 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10407 = ((__local
                                    float *) red_arr_mem_10402)[local_tid_10396 +
                                                                offset_10414];
                    }
                    // apply reduction operation
                    {
                        float res_10408 = x_10406 + x_10407;
                        
                        x_10406 = res_10408;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10402)[local_tid_10396] =
                            x_10406;
                    }
                }
                skip_waves_10415 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10396 == 0) {
                    ((__global float *) mem_10231)[0] = x_10406;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10091(__local volatile
                                  int64_t *sync_arr_mem_10427_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10429_backing_aligned_1,
                                  int32_t sizze_9800, float res_9802,
                                  int32_t num_groups_10086, __global
                                  unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10235, __global
                                  unsigned char *counter_mem_10417, __global
                                  unsigned char *group_res_arr_mem_10419,
                                  int32_t num_threads_10421)
{
    const int32_t segred_group_sizze_10084 =
                  entropy_scaled_f32zisegred_group_sizze_10083;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10427_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10427_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10429_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10429_backing_aligned_1;
    int32_t global_tid_10422;
    int32_t local_tid_10423;
    int32_t group_sizze_10426;
    int32_t wave_sizze_10425;
    int32_t group_tid_10424;
    
    global_tid_10422 = get_global_id(0);
    local_tid_10423 = get_local_id(0);
    group_sizze_10426 = get_local_size(0);
    wave_sizze_10425 = LOCKSTEP_WIDTH;
    group_tid_10424 = get_group_id(0);
    
    int32_t phys_tid_10091 = global_tid_10422;
    __local char *sync_arr_mem_10427;
    
    sync_arr_mem_10427 = (__local char *) sync_arr_mem_10427_backing_0;
    
    __local char *red_arr_mem_10429;
    
    red_arr_mem_10429 = (__local char *) red_arr_mem_10429_backing_1;
    
    int32_t dummy_10089 = 0;
    int32_t gtid_10090;
    
    gtid_10090 = 0;
    
    float x_acc_10431;
    int32_t chunk_sizze_10432 = smin32(squot32(sizze_9800 +
                                               segred_group_sizze_10084 *
                                               num_groups_10086 - 1,
                                               segred_group_sizze_10084 *
                                               num_groups_10086),
                                       squot32(sizze_9800 - phys_tid_10091 +
                                               num_threads_10421 - 1,
                                               num_threads_10421));
    float x_9808;
    float x_9809;
    
    // neutral-initialise the accumulators
    {
        x_acc_10431 = 0.0F;
    }
    for (int32_t i_10436 = 0; i_10436 < chunk_sizze_10432; i_10436++) {
        gtid_10090 = phys_tid_10091 + num_threads_10421 * i_10436;
        // apply map function
        {
            float x_9811 = ((__global float *) x_mem_10227)[gtid_10090];
            float res_9812 = x_9811 / res_9802;
            float res_9813;
            
            res_9813 = futrts_log32(res_9812);
            
            float res_9814 = res_9812 * res_9813;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9808 = x_acc_10431;
            }
            // load new values
            {
                x_9809 = res_9814;
            }
            // apply reduction operator
            {
                float res_9810 = x_9808 + x_9809;
                
                // store in accumulator
                {
                    x_acc_10431 = res_9810;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9808 = x_acc_10431;
        ((__local float *) red_arr_mem_10429)[local_tid_10423] = x_9808;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10437;
    int32_t skip_waves_10438;
    float x_10433;
    float x_10434;
    
    offset_10437 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10423, segred_group_sizze_10084)) {
            x_10433 = ((__local float *) red_arr_mem_10429)[local_tid_10423 +
                                                            offset_10437];
        }
    }
    offset_10437 = 1;
    while (slt32(offset_10437, wave_sizze_10425)) {
        if (slt32(local_tid_10423 + offset_10437, segred_group_sizze_10084) &&
            ((local_tid_10423 - squot32(local_tid_10423, wave_sizze_10425) *
              wave_sizze_10425) & (2 * offset_10437 - 1)) == 0) {
            // read array element
            {
                x_10434 = ((volatile __local
                            float *) red_arr_mem_10429)[local_tid_10423 +
                                                        offset_10437];
            }
            // apply reduction operation
            {
                float res_10435 = x_10433 + x_10434;
                
                x_10433 = res_10435;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10429)[local_tid_10423] = x_10433;
            }
        }
        offset_10437 *= 2;
    }
    skip_waves_10438 = 1;
    while (slt32(skip_waves_10438, squot32(segred_group_sizze_10084 +
                                           wave_sizze_10425 - 1,
                                           wave_sizze_10425))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10437 = skip_waves_10438 * wave_sizze_10425;
        if (slt32(local_tid_10423 + offset_10437, segred_group_sizze_10084) &&
            ((local_tid_10423 - squot32(local_tid_10423, wave_sizze_10425) *
              wave_sizze_10425) == 0 && (squot32(local_tid_10423,
                                                 wave_sizze_10425) & (2 *
                                                                      skip_waves_10438 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10434 = ((__local
                            float *) red_arr_mem_10429)[local_tid_10423 +
                                                        offset_10437];
            }
            // apply reduction operation
            {
                float res_10435 = x_10433 + x_10434;
                
                x_10433 = res_10435;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10429)[local_tid_10423] =
                    x_10433;
            }
        }
        skip_waves_10438 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10423 == 0) {
            x_acc_10431 = x_10433;
        }
    }
    
    int32_t old_counter_10439;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10423 == 0) {
            ((__global float *) group_res_arr_mem_10419)[group_tid_10424 *
                                                         segred_group_sizze_10084] =
                x_acc_10431;
            mem_fence_global();
            old_counter_10439 = atomic_add(&((volatile __global
                                              int *) counter_mem_10417)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10427)[0] = old_counter_10439 ==
                num_groups_10086 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10440 = ((__local bool *) sync_arr_mem_10427)[0];
    
    if (is_last_group_10440) {
        if (local_tid_10423 == 0) {
            old_counter_10439 = atomic_add(&((volatile __global
                                              int *) counter_mem_10417)[0],
                                           (int) (0 - num_groups_10086));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10423, num_groups_10086)) {
                x_9808 = ((__global
                           float *) group_res_arr_mem_10419)[local_tid_10423 *
                                                             segred_group_sizze_10084];
            } else {
                x_9808 = 0.0F;
            }
            ((__local float *) red_arr_mem_10429)[local_tid_10423] = x_9808;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10441;
            int32_t skip_waves_10442;
            float x_10433;
            float x_10434;
            
            offset_10441 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10423, segred_group_sizze_10084)) {
                    x_10433 = ((__local
                                float *) red_arr_mem_10429)[local_tid_10423 +
                                                            offset_10441];
                }
            }
            offset_10441 = 1;
            while (slt32(offset_10441, wave_sizze_10425)) {
                if (slt32(local_tid_10423 + offset_10441,
                          segred_group_sizze_10084) && ((local_tid_10423 -
                                                         squot32(local_tid_10423,
                                                                 wave_sizze_10425) *
                                                         wave_sizze_10425) &
                                                        (2 * offset_10441 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10434 = ((volatile __local
                                    float *) red_arr_mem_10429)[local_tid_10423 +
                                                                offset_10441];
                    }
                    // apply reduction operation
                    {
                        float res_10435 = x_10433 + x_10434;
                        
                        x_10433 = res_10435;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10429)[local_tid_10423] =
                            x_10433;
                    }
                }
                offset_10441 *= 2;
            }
            skip_waves_10442 = 1;
            while (slt32(skip_waves_10442, squot32(segred_group_sizze_10084 +
                                                   wave_sizze_10425 - 1,
                                                   wave_sizze_10425))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10441 = skip_waves_10442 * wave_sizze_10425;
                if (slt32(local_tid_10423 + offset_10441,
                          segred_group_sizze_10084) && ((local_tid_10423 -
                                                         squot32(local_tid_10423,
                                                                 wave_sizze_10425) *
                                                         wave_sizze_10425) ==
                                                        0 &&
                                                        (squot32(local_tid_10423,
                                                                 wave_sizze_10425) &
                                                         (2 * skip_waves_10442 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10434 = ((__local
                                    float *) red_arr_mem_10429)[local_tid_10423 +
                                                                offset_10441];
                    }
                    // apply reduction operation
                    {
                        float res_10435 = x_10433 + x_10434;
                        
                        x_10433 = res_10435;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10429)[local_tid_10423] =
                            x_10433;
                    }
                }
                skip_waves_10442 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10423 == 0) {
                    ((__global float *) mem_10235)[0] = x_10433;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10102(__local volatile
                                  int64_t *sync_arr_mem_10455_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10457_backing_aligned_1,
                                  int32_t sizze_9816, int32_t num_groups_10097,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10445, __global
                                  unsigned char *group_res_arr_mem_10447,
                                  int32_t num_threads_10449)
{
    const int32_t segred_group_sizze_10095 =
                  kullback_liebler_f64zisegred_group_sizze_10094;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10455_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10455_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10457_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10457_backing_aligned_1;
    int32_t global_tid_10450;
    int32_t local_tid_10451;
    int32_t group_sizze_10454;
    int32_t wave_sizze_10453;
    int32_t group_tid_10452;
    
    global_tid_10450 = get_global_id(0);
    local_tid_10451 = get_local_id(0);
    group_sizze_10454 = get_local_size(0);
    wave_sizze_10453 = LOCKSTEP_WIDTH;
    group_tid_10452 = get_group_id(0);
    
    int32_t phys_tid_10102 = global_tid_10450;
    __local char *sync_arr_mem_10455;
    
    sync_arr_mem_10455 = (__local char *) sync_arr_mem_10455_backing_0;
    
    __local char *red_arr_mem_10457;
    
    red_arr_mem_10457 = (__local char *) red_arr_mem_10457_backing_1;
    
    int32_t dummy_10100 = 0;
    int32_t gtid_10101;
    
    gtid_10101 = 0;
    
    double x_acc_10459;
    int32_t chunk_sizze_10460 = smin32(squot32(sizze_9816 +
                                               segred_group_sizze_10095 *
                                               num_groups_10097 - 1,
                                               segred_group_sizze_10095 *
                                               num_groups_10097),
                                       squot32(sizze_9816 - phys_tid_10102 +
                                               num_threads_10449 - 1,
                                               num_threads_10449));
    double x_9828;
    double x_9829;
    
    // neutral-initialise the accumulators
    {
        x_acc_10459 = 0.0;
    }
    for (int32_t i_10464 = 0; i_10464 < chunk_sizze_10460; i_10464++) {
        gtid_10101 = phys_tid_10102 + num_threads_10449 * i_10464;
        // apply map function
        {
            double x_9831 = ((__global double *) x_mem_10227)[gtid_10101];
            double x_9832 = ((__global double *) x_mem_10228)[gtid_10101];
            double res_9833 = x_9831 / x_9832;
            double res_9834;
            
            res_9834 = futrts_log64(res_9833);
            
            double res_9835 = x_9831 * res_9834;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9828 = x_acc_10459;
            }
            // load new values
            {
                x_9829 = res_9835;
            }
            // apply reduction operator
            {
                double res_9830 = x_9828 + x_9829;
                
                // store in accumulator
                {
                    x_acc_10459 = res_9830;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9828 = x_acc_10459;
        ((__local double *) red_arr_mem_10457)[local_tid_10451] = x_9828;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10465;
    int32_t skip_waves_10466;
    double x_10461;
    double x_10462;
    
    offset_10465 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10451, segred_group_sizze_10095)) {
            x_10461 = ((__local double *) red_arr_mem_10457)[local_tid_10451 +
                                                             offset_10465];
        }
    }
    offset_10465 = 1;
    while (slt32(offset_10465, wave_sizze_10453)) {
        if (slt32(local_tid_10451 + offset_10465, segred_group_sizze_10095) &&
            ((local_tid_10451 - squot32(local_tid_10451, wave_sizze_10453) *
              wave_sizze_10453) & (2 * offset_10465 - 1)) == 0) {
            // read array element
            {
                x_10462 = ((volatile __local
                            double *) red_arr_mem_10457)[local_tid_10451 +
                                                         offset_10465];
            }
            // apply reduction operation
            {
                double res_10463 = x_10461 + x_10462;
                
                x_10461 = res_10463;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10457)[local_tid_10451] = x_10461;
            }
        }
        offset_10465 *= 2;
    }
    skip_waves_10466 = 1;
    while (slt32(skip_waves_10466, squot32(segred_group_sizze_10095 +
                                           wave_sizze_10453 - 1,
                                           wave_sizze_10453))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10465 = skip_waves_10466 * wave_sizze_10453;
        if (slt32(local_tid_10451 + offset_10465, segred_group_sizze_10095) &&
            ((local_tid_10451 - squot32(local_tid_10451, wave_sizze_10453) *
              wave_sizze_10453) == 0 && (squot32(local_tid_10451,
                                                 wave_sizze_10453) & (2 *
                                                                      skip_waves_10466 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10462 = ((__local
                            double *) red_arr_mem_10457)[local_tid_10451 +
                                                         offset_10465];
            }
            // apply reduction operation
            {
                double res_10463 = x_10461 + x_10462;
                
                x_10461 = res_10463;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10457)[local_tid_10451] =
                    x_10461;
            }
        }
        skip_waves_10466 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10451 == 0) {
            x_acc_10459 = x_10461;
        }
    }
    
    int32_t old_counter_10467;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10451 == 0) {
            ((__global double *) group_res_arr_mem_10447)[group_tid_10452 *
                                                          segred_group_sizze_10095] =
                x_acc_10459;
            mem_fence_global();
            old_counter_10467 = atomic_add(&((volatile __global
                                              int *) counter_mem_10445)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10455)[0] = old_counter_10467 ==
                num_groups_10097 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10468 = ((__local bool *) sync_arr_mem_10455)[0];
    
    if (is_last_group_10468) {
        if (local_tid_10451 == 0) {
            old_counter_10467 = atomic_add(&((volatile __global
                                              int *) counter_mem_10445)[0],
                                           (int) (0 - num_groups_10097));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10451, num_groups_10097)) {
                x_9828 = ((__global
                           double *) group_res_arr_mem_10447)[local_tid_10451 *
                                                              segred_group_sizze_10095];
            } else {
                x_9828 = 0.0;
            }
            ((__local double *) red_arr_mem_10457)[local_tid_10451] = x_9828;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10469;
            int32_t skip_waves_10470;
            double x_10461;
            double x_10462;
            
            offset_10469 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10451, segred_group_sizze_10095)) {
                    x_10461 = ((__local
                                double *) red_arr_mem_10457)[local_tid_10451 +
                                                             offset_10469];
                }
            }
            offset_10469 = 1;
            while (slt32(offset_10469, wave_sizze_10453)) {
                if (slt32(local_tid_10451 + offset_10469,
                          segred_group_sizze_10095) && ((local_tid_10451 -
                                                         squot32(local_tid_10451,
                                                                 wave_sizze_10453) *
                                                         wave_sizze_10453) &
                                                        (2 * offset_10469 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10462 = ((volatile __local
                                    double *) red_arr_mem_10457)[local_tid_10451 +
                                                                 offset_10469];
                    }
                    // apply reduction operation
                    {
                        double res_10463 = x_10461 + x_10462;
                        
                        x_10461 = res_10463;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10457)[local_tid_10451] =
                            x_10461;
                    }
                }
                offset_10469 *= 2;
            }
            skip_waves_10470 = 1;
            while (slt32(skip_waves_10470, squot32(segred_group_sizze_10095 +
                                                   wave_sizze_10453 - 1,
                                                   wave_sizze_10453))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10469 = skip_waves_10470 * wave_sizze_10453;
                if (slt32(local_tid_10451 + offset_10469,
                          segred_group_sizze_10095) && ((local_tid_10451 -
                                                         squot32(local_tid_10451,
                                                                 wave_sizze_10453) *
                                                         wave_sizze_10453) ==
                                                        0 &&
                                                        (squot32(local_tid_10451,
                                                                 wave_sizze_10453) &
                                                         (2 * skip_waves_10470 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10462 = ((__local
                                    double *) red_arr_mem_10457)[local_tid_10451 +
                                                                 offset_10469];
                    }
                    // apply reduction operation
                    {
                        double res_10463 = x_10461 + x_10462;
                        
                        x_10461 = res_10463;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10457)[local_tid_10451] =
                            x_10461;
                    }
                }
                skip_waves_10470 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10451 == 0) {
                    ((__global double *) mem_10232)[0] = x_10461;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10113(__local volatile
                                  int64_t *sync_arr_mem_10483_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10485_backing_aligned_1,
                                  int32_t sizze_9836, int32_t num_groups_10108,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10473, __global
                                  unsigned char *group_res_arr_mem_10475,
                                  int32_t num_threads_10477)
{
    const int32_t segred_group_sizze_10106 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_10105;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10483_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10483_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10485_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10485_backing_aligned_1;
    int32_t global_tid_10478;
    int32_t local_tid_10479;
    int32_t group_sizze_10482;
    int32_t wave_sizze_10481;
    int32_t group_tid_10480;
    
    global_tid_10478 = get_global_id(0);
    local_tid_10479 = get_local_id(0);
    group_sizze_10482 = get_local_size(0);
    wave_sizze_10481 = LOCKSTEP_WIDTH;
    group_tid_10480 = get_group_id(0);
    
    int32_t phys_tid_10113 = global_tid_10478;
    __local char *sync_arr_mem_10483;
    
    sync_arr_mem_10483 = (__local char *) sync_arr_mem_10483_backing_0;
    
    __local char *red_arr_mem_10485;
    
    red_arr_mem_10485 = (__local char *) red_arr_mem_10485_backing_1;
    
    int32_t dummy_10111 = 0;
    int32_t gtid_10112;
    
    gtid_10112 = 0;
    
    double x_acc_10487;
    int32_t chunk_sizze_10488 = smin32(squot32(sizze_9836 +
                                               segred_group_sizze_10106 *
                                               num_groups_10108 - 1,
                                               segred_group_sizze_10106 *
                                               num_groups_10108),
                                       squot32(sizze_9836 - phys_tid_10113 +
                                               num_threads_10477 - 1,
                                               num_threads_10477));
    double x_9841;
    double x_9842;
    
    // neutral-initialise the accumulators
    {
        x_acc_10487 = 0.0;
    }
    for (int32_t i_10492 = 0; i_10492 < chunk_sizze_10488; i_10492++) {
        gtid_10112 = phys_tid_10113 + num_threads_10477 * i_10492;
        // apply map function
        {
            double x_9844 = ((__global double *) x_mem_10227)[gtid_10112];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9841 = x_acc_10487;
            }
            // load new values
            {
                x_9842 = x_9844;
            }
            // apply reduction operator
            {
                double res_9843 = x_9841 + x_9842;
                
                // store in accumulator
                {
                    x_acc_10487 = res_9843;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9841 = x_acc_10487;
        ((__local double *) red_arr_mem_10485)[local_tid_10479] = x_9841;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10493;
    int32_t skip_waves_10494;
    double x_10489;
    double x_10490;
    
    offset_10493 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10479, segred_group_sizze_10106)) {
            x_10489 = ((__local double *) red_arr_mem_10485)[local_tid_10479 +
                                                             offset_10493];
        }
    }
    offset_10493 = 1;
    while (slt32(offset_10493, wave_sizze_10481)) {
        if (slt32(local_tid_10479 + offset_10493, segred_group_sizze_10106) &&
            ((local_tid_10479 - squot32(local_tid_10479, wave_sizze_10481) *
              wave_sizze_10481) & (2 * offset_10493 - 1)) == 0) {
            // read array element
            {
                x_10490 = ((volatile __local
                            double *) red_arr_mem_10485)[local_tid_10479 +
                                                         offset_10493];
            }
            // apply reduction operation
            {
                double res_10491 = x_10489 + x_10490;
                
                x_10489 = res_10491;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10485)[local_tid_10479] = x_10489;
            }
        }
        offset_10493 *= 2;
    }
    skip_waves_10494 = 1;
    while (slt32(skip_waves_10494, squot32(segred_group_sizze_10106 +
                                           wave_sizze_10481 - 1,
                                           wave_sizze_10481))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10493 = skip_waves_10494 * wave_sizze_10481;
        if (slt32(local_tid_10479 + offset_10493, segred_group_sizze_10106) &&
            ((local_tid_10479 - squot32(local_tid_10479, wave_sizze_10481) *
              wave_sizze_10481) == 0 && (squot32(local_tid_10479,
                                                 wave_sizze_10481) & (2 *
                                                                      skip_waves_10494 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10490 = ((__local
                            double *) red_arr_mem_10485)[local_tid_10479 +
                                                         offset_10493];
            }
            // apply reduction operation
            {
                double res_10491 = x_10489 + x_10490;
                
                x_10489 = res_10491;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10485)[local_tid_10479] =
                    x_10489;
            }
        }
        skip_waves_10494 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10479 == 0) {
            x_acc_10487 = x_10489;
        }
    }
    
    int32_t old_counter_10495;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10479 == 0) {
            ((__global double *) group_res_arr_mem_10475)[group_tid_10480 *
                                                          segred_group_sizze_10106] =
                x_acc_10487;
            mem_fence_global();
            old_counter_10495 = atomic_add(&((volatile __global
                                              int *) counter_mem_10473)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10483)[0] = old_counter_10495 ==
                num_groups_10108 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10496 = ((__local bool *) sync_arr_mem_10483)[0];
    
    if (is_last_group_10496) {
        if (local_tid_10479 == 0) {
            old_counter_10495 = atomic_add(&((volatile __global
                                              int *) counter_mem_10473)[0],
                                           (int) (0 - num_groups_10108));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10479, num_groups_10108)) {
                x_9841 = ((__global
                           double *) group_res_arr_mem_10475)[local_tid_10479 *
                                                              segred_group_sizze_10106];
            } else {
                x_9841 = 0.0;
            }
            ((__local double *) red_arr_mem_10485)[local_tid_10479] = x_9841;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10497;
            int32_t skip_waves_10498;
            double x_10489;
            double x_10490;
            
            offset_10497 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10479, segred_group_sizze_10106)) {
                    x_10489 = ((__local
                                double *) red_arr_mem_10485)[local_tid_10479 +
                                                             offset_10497];
                }
            }
            offset_10497 = 1;
            while (slt32(offset_10497, wave_sizze_10481)) {
                if (slt32(local_tid_10479 + offset_10497,
                          segred_group_sizze_10106) && ((local_tid_10479 -
                                                         squot32(local_tid_10479,
                                                                 wave_sizze_10481) *
                                                         wave_sizze_10481) &
                                                        (2 * offset_10497 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10490 = ((volatile __local
                                    double *) red_arr_mem_10485)[local_tid_10479 +
                                                                 offset_10497];
                    }
                    // apply reduction operation
                    {
                        double res_10491 = x_10489 + x_10490;
                        
                        x_10489 = res_10491;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10485)[local_tid_10479] =
                            x_10489;
                    }
                }
                offset_10497 *= 2;
            }
            skip_waves_10498 = 1;
            while (slt32(skip_waves_10498, squot32(segred_group_sizze_10106 +
                                                   wave_sizze_10481 - 1,
                                                   wave_sizze_10481))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10497 = skip_waves_10498 * wave_sizze_10481;
                if (slt32(local_tid_10479 + offset_10497,
                          segred_group_sizze_10106) && ((local_tid_10479 -
                                                         squot32(local_tid_10479,
                                                                 wave_sizze_10481) *
                                                         wave_sizze_10481) ==
                                                        0 &&
                                                        (squot32(local_tid_10479,
                                                                 wave_sizze_10481) &
                                                         (2 * skip_waves_10498 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10490 = ((__local
                                    double *) red_arr_mem_10485)[local_tid_10479 +
                                                                 offset_10497];
                    }
                    // apply reduction operation
                    {
                        double res_10491 = x_10489 + x_10490;
                        
                        x_10489 = res_10491;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10485)[local_tid_10479] =
                            x_10489;
                    }
                }
                skip_waves_10498 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10479 == 0) {
                    ((__global double *) mem_10232)[0] = x_10489;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10124(__local volatile
                                  int64_t *sync_arr_mem_10510_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10512_backing_aligned_1,
                                  int32_t sizze_9837, int32_t num_groups_10119,
                                  __global unsigned char *y_mem_10228, __global
                                  unsigned char *mem_10236, __global
                                  unsigned char *counter_mem_10500, __global
                                  unsigned char *group_res_arr_mem_10502,
                                  int32_t num_threads_10504)
{
    const int32_t segred_group_sizze_10117 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_10116;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10510_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10510_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10512_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10512_backing_aligned_1;
    int32_t global_tid_10505;
    int32_t local_tid_10506;
    int32_t group_sizze_10509;
    int32_t wave_sizze_10508;
    int32_t group_tid_10507;
    
    global_tid_10505 = get_global_id(0);
    local_tid_10506 = get_local_id(0);
    group_sizze_10509 = get_local_size(0);
    wave_sizze_10508 = LOCKSTEP_WIDTH;
    group_tid_10507 = get_group_id(0);
    
    int32_t phys_tid_10124 = global_tid_10505;
    __local char *sync_arr_mem_10510;
    
    sync_arr_mem_10510 = (__local char *) sync_arr_mem_10510_backing_0;
    
    __local char *red_arr_mem_10512;
    
    red_arr_mem_10512 = (__local char *) red_arr_mem_10512_backing_1;
    
    int32_t dummy_10122 = 0;
    int32_t gtid_10123;
    
    gtid_10123 = 0;
    
    double x_acc_10514;
    int32_t chunk_sizze_10515 = smin32(squot32(sizze_9837 +
                                               segred_group_sizze_10117 *
                                               num_groups_10119 - 1,
                                               segred_group_sizze_10117 *
                                               num_groups_10119),
                                       squot32(sizze_9837 - phys_tid_10124 +
                                               num_threads_10504 - 1,
                                               num_threads_10504));
    double x_9846;
    double x_9847;
    
    // neutral-initialise the accumulators
    {
        x_acc_10514 = 0.0;
    }
    for (int32_t i_10519 = 0; i_10519 < chunk_sizze_10515; i_10519++) {
        gtid_10123 = phys_tid_10124 + num_threads_10504 * i_10519;
        // apply map function
        {
            double x_9849 = ((__global double *) y_mem_10228)[gtid_10123];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9846 = x_acc_10514;
            }
            // load new values
            {
                x_9847 = x_9849;
            }
            // apply reduction operator
            {
                double res_9848 = x_9846 + x_9847;
                
                // store in accumulator
                {
                    x_acc_10514 = res_9848;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9846 = x_acc_10514;
        ((__local double *) red_arr_mem_10512)[local_tid_10506] = x_9846;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10520;
    int32_t skip_waves_10521;
    double x_10516;
    double x_10517;
    
    offset_10520 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10506, segred_group_sizze_10117)) {
            x_10516 = ((__local double *) red_arr_mem_10512)[local_tid_10506 +
                                                             offset_10520];
        }
    }
    offset_10520 = 1;
    while (slt32(offset_10520, wave_sizze_10508)) {
        if (slt32(local_tid_10506 + offset_10520, segred_group_sizze_10117) &&
            ((local_tid_10506 - squot32(local_tid_10506, wave_sizze_10508) *
              wave_sizze_10508) & (2 * offset_10520 - 1)) == 0) {
            // read array element
            {
                x_10517 = ((volatile __local
                            double *) red_arr_mem_10512)[local_tid_10506 +
                                                         offset_10520];
            }
            // apply reduction operation
            {
                double res_10518 = x_10516 + x_10517;
                
                x_10516 = res_10518;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10512)[local_tid_10506] = x_10516;
            }
        }
        offset_10520 *= 2;
    }
    skip_waves_10521 = 1;
    while (slt32(skip_waves_10521, squot32(segred_group_sizze_10117 +
                                           wave_sizze_10508 - 1,
                                           wave_sizze_10508))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10520 = skip_waves_10521 * wave_sizze_10508;
        if (slt32(local_tid_10506 + offset_10520, segred_group_sizze_10117) &&
            ((local_tid_10506 - squot32(local_tid_10506, wave_sizze_10508) *
              wave_sizze_10508) == 0 && (squot32(local_tid_10506,
                                                 wave_sizze_10508) & (2 *
                                                                      skip_waves_10521 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10517 = ((__local
                            double *) red_arr_mem_10512)[local_tid_10506 +
                                                         offset_10520];
            }
            // apply reduction operation
            {
                double res_10518 = x_10516 + x_10517;
                
                x_10516 = res_10518;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10512)[local_tid_10506] =
                    x_10516;
            }
        }
        skip_waves_10521 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10506 == 0) {
            x_acc_10514 = x_10516;
        }
    }
    
    int32_t old_counter_10522;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10506 == 0) {
            ((__global double *) group_res_arr_mem_10502)[group_tid_10507 *
                                                          segred_group_sizze_10117] =
                x_acc_10514;
            mem_fence_global();
            old_counter_10522 = atomic_add(&((volatile __global
                                              int *) counter_mem_10500)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10510)[0] = old_counter_10522 ==
                num_groups_10119 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10523 = ((__local bool *) sync_arr_mem_10510)[0];
    
    if (is_last_group_10523) {
        if (local_tid_10506 == 0) {
            old_counter_10522 = atomic_add(&((volatile __global
                                              int *) counter_mem_10500)[0],
                                           (int) (0 - num_groups_10119));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10506, num_groups_10119)) {
                x_9846 = ((__global
                           double *) group_res_arr_mem_10502)[local_tid_10506 *
                                                              segred_group_sizze_10117];
            } else {
                x_9846 = 0.0;
            }
            ((__local double *) red_arr_mem_10512)[local_tid_10506] = x_9846;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10524;
            int32_t skip_waves_10525;
            double x_10516;
            double x_10517;
            
            offset_10524 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10506, segred_group_sizze_10117)) {
                    x_10516 = ((__local
                                double *) red_arr_mem_10512)[local_tid_10506 +
                                                             offset_10524];
                }
            }
            offset_10524 = 1;
            while (slt32(offset_10524, wave_sizze_10508)) {
                if (slt32(local_tid_10506 + offset_10524,
                          segred_group_sizze_10117) && ((local_tid_10506 -
                                                         squot32(local_tid_10506,
                                                                 wave_sizze_10508) *
                                                         wave_sizze_10508) &
                                                        (2 * offset_10524 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10517 = ((volatile __local
                                    double *) red_arr_mem_10512)[local_tid_10506 +
                                                                 offset_10524];
                    }
                    // apply reduction operation
                    {
                        double res_10518 = x_10516 + x_10517;
                        
                        x_10516 = res_10518;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10512)[local_tid_10506] =
                            x_10516;
                    }
                }
                offset_10524 *= 2;
            }
            skip_waves_10525 = 1;
            while (slt32(skip_waves_10525, squot32(segred_group_sizze_10117 +
                                                   wave_sizze_10508 - 1,
                                                   wave_sizze_10508))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10524 = skip_waves_10525 * wave_sizze_10508;
                if (slt32(local_tid_10506 + offset_10524,
                          segred_group_sizze_10117) && ((local_tid_10506 -
                                                         squot32(local_tid_10506,
                                                                 wave_sizze_10508) *
                                                         wave_sizze_10508) ==
                                                        0 &&
                                                        (squot32(local_tid_10506,
                                                                 wave_sizze_10508) &
                                                         (2 * skip_waves_10525 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10517 = ((__local
                                    double *) red_arr_mem_10512)[local_tid_10506 +
                                                                 offset_10524];
                    }
                    // apply reduction operation
                    {
                        double res_10518 = x_10516 + x_10517;
                        
                        x_10516 = res_10518;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10512)[local_tid_10506] =
                            x_10516;
                    }
                }
                skip_waves_10525 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10506 == 0) {
                    ((__global double *) mem_10236)[0] = x_10516;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10135(__local volatile
                                  int64_t *sync_arr_mem_10537_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10539_backing_aligned_1,
                                  int32_t sizze_9836, double res_9840,
                                  double res_9845, int32_t num_groups_10130,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *y_mem_10228, __global
                                  unsigned char *mem_10240, __global
                                  unsigned char *counter_mem_10527, __global
                                  unsigned char *group_res_arr_mem_10529,
                                  int32_t num_threads_10531)
{
    const int32_t segred_group_sizze_10128 =
                  kullback_liebler_scaled_f64zisegred_group_sizze_10127;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10537_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10537_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10539_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10539_backing_aligned_1;
    int32_t global_tid_10532;
    int32_t local_tid_10533;
    int32_t group_sizze_10536;
    int32_t wave_sizze_10535;
    int32_t group_tid_10534;
    
    global_tid_10532 = get_global_id(0);
    local_tid_10533 = get_local_id(0);
    group_sizze_10536 = get_local_size(0);
    wave_sizze_10535 = LOCKSTEP_WIDTH;
    group_tid_10534 = get_group_id(0);
    
    int32_t phys_tid_10135 = global_tid_10532;
    __local char *sync_arr_mem_10537;
    
    sync_arr_mem_10537 = (__local char *) sync_arr_mem_10537_backing_0;
    
    __local char *red_arr_mem_10539;
    
    red_arr_mem_10539 = (__local char *) red_arr_mem_10539_backing_1;
    
    int32_t dummy_10133 = 0;
    int32_t gtid_10134;
    
    gtid_10134 = 0;
    
    double x_acc_10541;
    int32_t chunk_sizze_10542 = smin32(squot32(sizze_9836 +
                                               segred_group_sizze_10128 *
                                               num_groups_10130 - 1,
                                               segred_group_sizze_10128 *
                                               num_groups_10130),
                                       squot32(sizze_9836 - phys_tid_10135 +
                                               num_threads_10531 - 1,
                                               num_threads_10531));
    double x_9858;
    double x_9859;
    
    // neutral-initialise the accumulators
    {
        x_acc_10541 = 0.0;
    }
    for (int32_t i_10546 = 0; i_10546 < chunk_sizze_10542; i_10546++) {
        gtid_10134 = phys_tid_10135 + num_threads_10531 * i_10546;
        // apply map function
        {
            double x_9861 = ((__global double *) x_mem_10227)[gtid_10134];
            double x_9862 = ((__global double *) y_mem_10228)[gtid_10134];
            double res_9863 = x_9861 / res_9840;
            double res_9864 = x_9862 / res_9845;
            double res_9865 = res_9863 / res_9864;
            double res_9866;
            
            res_9866 = futrts_log64(res_9865);
            
            double res_9867 = res_9863 * res_9866;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9858 = x_acc_10541;
            }
            // load new values
            {
                x_9859 = res_9867;
            }
            // apply reduction operator
            {
                double res_9860 = x_9858 + x_9859;
                
                // store in accumulator
                {
                    x_acc_10541 = res_9860;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9858 = x_acc_10541;
        ((__local double *) red_arr_mem_10539)[local_tid_10533] = x_9858;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10547;
    int32_t skip_waves_10548;
    double x_10543;
    double x_10544;
    
    offset_10547 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10533, segred_group_sizze_10128)) {
            x_10543 = ((__local double *) red_arr_mem_10539)[local_tid_10533 +
                                                             offset_10547];
        }
    }
    offset_10547 = 1;
    while (slt32(offset_10547, wave_sizze_10535)) {
        if (slt32(local_tid_10533 + offset_10547, segred_group_sizze_10128) &&
            ((local_tid_10533 - squot32(local_tid_10533, wave_sizze_10535) *
              wave_sizze_10535) & (2 * offset_10547 - 1)) == 0) {
            // read array element
            {
                x_10544 = ((volatile __local
                            double *) red_arr_mem_10539)[local_tid_10533 +
                                                         offset_10547];
            }
            // apply reduction operation
            {
                double res_10545 = x_10543 + x_10544;
                
                x_10543 = res_10545;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10539)[local_tid_10533] = x_10543;
            }
        }
        offset_10547 *= 2;
    }
    skip_waves_10548 = 1;
    while (slt32(skip_waves_10548, squot32(segred_group_sizze_10128 +
                                           wave_sizze_10535 - 1,
                                           wave_sizze_10535))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10547 = skip_waves_10548 * wave_sizze_10535;
        if (slt32(local_tid_10533 + offset_10547, segred_group_sizze_10128) &&
            ((local_tid_10533 - squot32(local_tid_10533, wave_sizze_10535) *
              wave_sizze_10535) == 0 && (squot32(local_tid_10533,
                                                 wave_sizze_10535) & (2 *
                                                                      skip_waves_10548 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10544 = ((__local
                            double *) red_arr_mem_10539)[local_tid_10533 +
                                                         offset_10547];
            }
            // apply reduction operation
            {
                double res_10545 = x_10543 + x_10544;
                
                x_10543 = res_10545;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10539)[local_tid_10533] =
                    x_10543;
            }
        }
        skip_waves_10548 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10533 == 0) {
            x_acc_10541 = x_10543;
        }
    }
    
    int32_t old_counter_10549;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10533 == 0) {
            ((__global double *) group_res_arr_mem_10529)[group_tid_10534 *
                                                          segred_group_sizze_10128] =
                x_acc_10541;
            mem_fence_global();
            old_counter_10549 = atomic_add(&((volatile __global
                                              int *) counter_mem_10527)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10537)[0] = old_counter_10549 ==
                num_groups_10130 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10550 = ((__local bool *) sync_arr_mem_10537)[0];
    
    if (is_last_group_10550) {
        if (local_tid_10533 == 0) {
            old_counter_10549 = atomic_add(&((volatile __global
                                              int *) counter_mem_10527)[0],
                                           (int) (0 - num_groups_10130));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10533, num_groups_10130)) {
                x_9858 = ((__global
                           double *) group_res_arr_mem_10529)[local_tid_10533 *
                                                              segred_group_sizze_10128];
            } else {
                x_9858 = 0.0;
            }
            ((__local double *) red_arr_mem_10539)[local_tid_10533] = x_9858;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10551;
            int32_t skip_waves_10552;
            double x_10543;
            double x_10544;
            
            offset_10551 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10533, segred_group_sizze_10128)) {
                    x_10543 = ((__local
                                double *) red_arr_mem_10539)[local_tid_10533 +
                                                             offset_10551];
                }
            }
            offset_10551 = 1;
            while (slt32(offset_10551, wave_sizze_10535)) {
                if (slt32(local_tid_10533 + offset_10551,
                          segred_group_sizze_10128) && ((local_tid_10533 -
                                                         squot32(local_tid_10533,
                                                                 wave_sizze_10535) *
                                                         wave_sizze_10535) &
                                                        (2 * offset_10551 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10544 = ((volatile __local
                                    double *) red_arr_mem_10539)[local_tid_10533 +
                                                                 offset_10551];
                    }
                    // apply reduction operation
                    {
                        double res_10545 = x_10543 + x_10544;
                        
                        x_10543 = res_10545;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10539)[local_tid_10533] =
                            x_10543;
                    }
                }
                offset_10551 *= 2;
            }
            skip_waves_10552 = 1;
            while (slt32(skip_waves_10552, squot32(segred_group_sizze_10128 +
                                                   wave_sizze_10535 - 1,
                                                   wave_sizze_10535))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10551 = skip_waves_10552 * wave_sizze_10535;
                if (slt32(local_tid_10533 + offset_10551,
                          segred_group_sizze_10128) && ((local_tid_10533 -
                                                         squot32(local_tid_10533,
                                                                 wave_sizze_10535) *
                                                         wave_sizze_10535) ==
                                                        0 &&
                                                        (squot32(local_tid_10533,
                                                                 wave_sizze_10535) &
                                                         (2 * skip_waves_10552 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10544 = ((__local
                                    double *) red_arr_mem_10539)[local_tid_10533 +
                                                                 offset_10551];
                    }
                    // apply reduction operation
                    {
                        double res_10545 = x_10543 + x_10544;
                        
                        x_10543 = res_10545;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10539)[local_tid_10533] =
                            x_10543;
                    }
                }
                skip_waves_10552 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10533 == 0) {
                    ((__global double *) mem_10240)[0] = x_10543;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10146(__local volatile
                                  int64_t *sync_arr_mem_10565_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10567_backing_aligned_1,
                                  int32_t sizze_9868, int32_t num_groups_10141,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10555, __global
                                  unsigned char *group_res_arr_mem_10557,
                                  int32_t num_threads_10559)
{
    const int32_t segred_group_sizze_10139 =
                  kullback_liebler_f32zisegred_group_sizze_10138;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10565_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10565_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10567_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10567_backing_aligned_1;
    int32_t global_tid_10560;
    int32_t local_tid_10561;
    int32_t group_sizze_10564;
    int32_t wave_sizze_10563;
    int32_t group_tid_10562;
    
    global_tid_10560 = get_global_id(0);
    local_tid_10561 = get_local_id(0);
    group_sizze_10564 = get_local_size(0);
    wave_sizze_10563 = LOCKSTEP_WIDTH;
    group_tid_10562 = get_group_id(0);
    
    int32_t phys_tid_10146 = global_tid_10560;
    __local char *sync_arr_mem_10565;
    
    sync_arr_mem_10565 = (__local char *) sync_arr_mem_10565_backing_0;
    
    __local char *red_arr_mem_10567;
    
    red_arr_mem_10567 = (__local char *) red_arr_mem_10567_backing_1;
    
    int32_t dummy_10144 = 0;
    int32_t gtid_10145;
    
    gtid_10145 = 0;
    
    float x_acc_10569;
    int32_t chunk_sizze_10570 = smin32(squot32(sizze_9868 +
                                               segred_group_sizze_10139 *
                                               num_groups_10141 - 1,
                                               segred_group_sizze_10139 *
                                               num_groups_10141),
                                       squot32(sizze_9868 - phys_tid_10146 +
                                               num_threads_10559 - 1,
                                               num_threads_10559));
    float x_9880;
    float x_9881;
    
    // neutral-initialise the accumulators
    {
        x_acc_10569 = 0.0F;
    }
    for (int32_t i_10574 = 0; i_10574 < chunk_sizze_10570; i_10574++) {
        gtid_10145 = phys_tid_10146 + num_threads_10559 * i_10574;
        // apply map function
        {
            float x_9883 = ((__global float *) x_mem_10227)[gtid_10145];
            float x_9884 = ((__global float *) x_mem_10228)[gtid_10145];
            float res_9885 = x_9883 / x_9884;
            float res_9886;
            
            res_9886 = futrts_log32(res_9885);
            
            float res_9887 = x_9883 * res_9886;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9880 = x_acc_10569;
            }
            // load new values
            {
                x_9881 = res_9887;
            }
            // apply reduction operator
            {
                float res_9882 = x_9880 + x_9881;
                
                // store in accumulator
                {
                    x_acc_10569 = res_9882;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9880 = x_acc_10569;
        ((__local float *) red_arr_mem_10567)[local_tid_10561] = x_9880;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10575;
    int32_t skip_waves_10576;
    float x_10571;
    float x_10572;
    
    offset_10575 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10561, segred_group_sizze_10139)) {
            x_10571 = ((__local float *) red_arr_mem_10567)[local_tid_10561 +
                                                            offset_10575];
        }
    }
    offset_10575 = 1;
    while (slt32(offset_10575, wave_sizze_10563)) {
        if (slt32(local_tid_10561 + offset_10575, segred_group_sizze_10139) &&
            ((local_tid_10561 - squot32(local_tid_10561, wave_sizze_10563) *
              wave_sizze_10563) & (2 * offset_10575 - 1)) == 0) {
            // read array element
            {
                x_10572 = ((volatile __local
                            float *) red_arr_mem_10567)[local_tid_10561 +
                                                        offset_10575];
            }
            // apply reduction operation
            {
                float res_10573 = x_10571 + x_10572;
                
                x_10571 = res_10573;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10567)[local_tid_10561] = x_10571;
            }
        }
        offset_10575 *= 2;
    }
    skip_waves_10576 = 1;
    while (slt32(skip_waves_10576, squot32(segred_group_sizze_10139 +
                                           wave_sizze_10563 - 1,
                                           wave_sizze_10563))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10575 = skip_waves_10576 * wave_sizze_10563;
        if (slt32(local_tid_10561 + offset_10575, segred_group_sizze_10139) &&
            ((local_tid_10561 - squot32(local_tid_10561, wave_sizze_10563) *
              wave_sizze_10563) == 0 && (squot32(local_tid_10561,
                                                 wave_sizze_10563) & (2 *
                                                                      skip_waves_10576 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10572 = ((__local
                            float *) red_arr_mem_10567)[local_tid_10561 +
                                                        offset_10575];
            }
            // apply reduction operation
            {
                float res_10573 = x_10571 + x_10572;
                
                x_10571 = res_10573;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10567)[local_tid_10561] =
                    x_10571;
            }
        }
        skip_waves_10576 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10561 == 0) {
            x_acc_10569 = x_10571;
        }
    }
    
    int32_t old_counter_10577;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10561 == 0) {
            ((__global float *) group_res_arr_mem_10557)[group_tid_10562 *
                                                         segred_group_sizze_10139] =
                x_acc_10569;
            mem_fence_global();
            old_counter_10577 = atomic_add(&((volatile __global
                                              int *) counter_mem_10555)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10565)[0] = old_counter_10577 ==
                num_groups_10141 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10578 = ((__local bool *) sync_arr_mem_10565)[0];
    
    if (is_last_group_10578) {
        if (local_tid_10561 == 0) {
            old_counter_10577 = atomic_add(&((volatile __global
                                              int *) counter_mem_10555)[0],
                                           (int) (0 - num_groups_10141));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10561, num_groups_10141)) {
                x_9880 = ((__global
                           float *) group_res_arr_mem_10557)[local_tid_10561 *
                                                             segred_group_sizze_10139];
            } else {
                x_9880 = 0.0F;
            }
            ((__local float *) red_arr_mem_10567)[local_tid_10561] = x_9880;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10579;
            int32_t skip_waves_10580;
            float x_10571;
            float x_10572;
            
            offset_10579 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10561, segred_group_sizze_10139)) {
                    x_10571 = ((__local
                                float *) red_arr_mem_10567)[local_tid_10561 +
                                                            offset_10579];
                }
            }
            offset_10579 = 1;
            while (slt32(offset_10579, wave_sizze_10563)) {
                if (slt32(local_tid_10561 + offset_10579,
                          segred_group_sizze_10139) && ((local_tid_10561 -
                                                         squot32(local_tid_10561,
                                                                 wave_sizze_10563) *
                                                         wave_sizze_10563) &
                                                        (2 * offset_10579 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10572 = ((volatile __local
                                    float *) red_arr_mem_10567)[local_tid_10561 +
                                                                offset_10579];
                    }
                    // apply reduction operation
                    {
                        float res_10573 = x_10571 + x_10572;
                        
                        x_10571 = res_10573;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10567)[local_tid_10561] =
                            x_10571;
                    }
                }
                offset_10579 *= 2;
            }
            skip_waves_10580 = 1;
            while (slt32(skip_waves_10580, squot32(segred_group_sizze_10139 +
                                                   wave_sizze_10563 - 1,
                                                   wave_sizze_10563))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10579 = skip_waves_10580 * wave_sizze_10563;
                if (slt32(local_tid_10561 + offset_10579,
                          segred_group_sizze_10139) && ((local_tid_10561 -
                                                         squot32(local_tid_10561,
                                                                 wave_sizze_10563) *
                                                         wave_sizze_10563) ==
                                                        0 &&
                                                        (squot32(local_tid_10561,
                                                                 wave_sizze_10563) &
                                                         (2 * skip_waves_10580 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10572 = ((__local
                                    float *) red_arr_mem_10567)[local_tid_10561 +
                                                                offset_10579];
                    }
                    // apply reduction operation
                    {
                        float res_10573 = x_10571 + x_10572;
                        
                        x_10571 = res_10573;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10567)[local_tid_10561] =
                            x_10571;
                    }
                }
                skip_waves_10580 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10561 == 0) {
                    ((__global float *) mem_10232)[0] = x_10571;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10157(__local volatile
                                  int64_t *sync_arr_mem_10593_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10595_backing_aligned_1,
                                  int32_t sizze_9888, int32_t num_groups_10152,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10583, __global
                                  unsigned char *group_res_arr_mem_10585,
                                  int32_t num_threads_10587)
{
    const int32_t segred_group_sizze_10150 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_10149;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10593_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10593_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10595_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10595_backing_aligned_1;
    int32_t global_tid_10588;
    int32_t local_tid_10589;
    int32_t group_sizze_10592;
    int32_t wave_sizze_10591;
    int32_t group_tid_10590;
    
    global_tid_10588 = get_global_id(0);
    local_tid_10589 = get_local_id(0);
    group_sizze_10592 = get_local_size(0);
    wave_sizze_10591 = LOCKSTEP_WIDTH;
    group_tid_10590 = get_group_id(0);
    
    int32_t phys_tid_10157 = global_tid_10588;
    __local char *sync_arr_mem_10593;
    
    sync_arr_mem_10593 = (__local char *) sync_arr_mem_10593_backing_0;
    
    __local char *red_arr_mem_10595;
    
    red_arr_mem_10595 = (__local char *) red_arr_mem_10595_backing_1;
    
    int32_t dummy_10155 = 0;
    int32_t gtid_10156;
    
    gtid_10156 = 0;
    
    float x_acc_10597;
    int32_t chunk_sizze_10598 = smin32(squot32(sizze_9888 +
                                               segred_group_sizze_10150 *
                                               num_groups_10152 - 1,
                                               segred_group_sizze_10150 *
                                               num_groups_10152),
                                       squot32(sizze_9888 - phys_tid_10157 +
                                               num_threads_10587 - 1,
                                               num_threads_10587));
    float x_9893;
    float x_9894;
    
    // neutral-initialise the accumulators
    {
        x_acc_10597 = 0.0F;
    }
    for (int32_t i_10602 = 0; i_10602 < chunk_sizze_10598; i_10602++) {
        gtid_10156 = phys_tid_10157 + num_threads_10587 * i_10602;
        // apply map function
        {
            float x_9896 = ((__global float *) x_mem_10227)[gtid_10156];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9893 = x_acc_10597;
            }
            // load new values
            {
                x_9894 = x_9896;
            }
            // apply reduction operator
            {
                float res_9895 = x_9893 + x_9894;
                
                // store in accumulator
                {
                    x_acc_10597 = res_9895;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9893 = x_acc_10597;
        ((__local float *) red_arr_mem_10595)[local_tid_10589] = x_9893;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10603;
    int32_t skip_waves_10604;
    float x_10599;
    float x_10600;
    
    offset_10603 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10589, segred_group_sizze_10150)) {
            x_10599 = ((__local float *) red_arr_mem_10595)[local_tid_10589 +
                                                            offset_10603];
        }
    }
    offset_10603 = 1;
    while (slt32(offset_10603, wave_sizze_10591)) {
        if (slt32(local_tid_10589 + offset_10603, segred_group_sizze_10150) &&
            ((local_tid_10589 - squot32(local_tid_10589, wave_sizze_10591) *
              wave_sizze_10591) & (2 * offset_10603 - 1)) == 0) {
            // read array element
            {
                x_10600 = ((volatile __local
                            float *) red_arr_mem_10595)[local_tid_10589 +
                                                        offset_10603];
            }
            // apply reduction operation
            {
                float res_10601 = x_10599 + x_10600;
                
                x_10599 = res_10601;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10595)[local_tid_10589] = x_10599;
            }
        }
        offset_10603 *= 2;
    }
    skip_waves_10604 = 1;
    while (slt32(skip_waves_10604, squot32(segred_group_sizze_10150 +
                                           wave_sizze_10591 - 1,
                                           wave_sizze_10591))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10603 = skip_waves_10604 * wave_sizze_10591;
        if (slt32(local_tid_10589 + offset_10603, segred_group_sizze_10150) &&
            ((local_tid_10589 - squot32(local_tid_10589, wave_sizze_10591) *
              wave_sizze_10591) == 0 && (squot32(local_tid_10589,
                                                 wave_sizze_10591) & (2 *
                                                                      skip_waves_10604 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10600 = ((__local
                            float *) red_arr_mem_10595)[local_tid_10589 +
                                                        offset_10603];
            }
            // apply reduction operation
            {
                float res_10601 = x_10599 + x_10600;
                
                x_10599 = res_10601;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10595)[local_tid_10589] =
                    x_10599;
            }
        }
        skip_waves_10604 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10589 == 0) {
            x_acc_10597 = x_10599;
        }
    }
    
    int32_t old_counter_10605;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10589 == 0) {
            ((__global float *) group_res_arr_mem_10585)[group_tid_10590 *
                                                         segred_group_sizze_10150] =
                x_acc_10597;
            mem_fence_global();
            old_counter_10605 = atomic_add(&((volatile __global
                                              int *) counter_mem_10583)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10593)[0] = old_counter_10605 ==
                num_groups_10152 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10606 = ((__local bool *) sync_arr_mem_10593)[0];
    
    if (is_last_group_10606) {
        if (local_tid_10589 == 0) {
            old_counter_10605 = atomic_add(&((volatile __global
                                              int *) counter_mem_10583)[0],
                                           (int) (0 - num_groups_10152));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10589, num_groups_10152)) {
                x_9893 = ((__global
                           float *) group_res_arr_mem_10585)[local_tid_10589 *
                                                             segred_group_sizze_10150];
            } else {
                x_9893 = 0.0F;
            }
            ((__local float *) red_arr_mem_10595)[local_tid_10589] = x_9893;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10607;
            int32_t skip_waves_10608;
            float x_10599;
            float x_10600;
            
            offset_10607 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10589, segred_group_sizze_10150)) {
                    x_10599 = ((__local
                                float *) red_arr_mem_10595)[local_tid_10589 +
                                                            offset_10607];
                }
            }
            offset_10607 = 1;
            while (slt32(offset_10607, wave_sizze_10591)) {
                if (slt32(local_tid_10589 + offset_10607,
                          segred_group_sizze_10150) && ((local_tid_10589 -
                                                         squot32(local_tid_10589,
                                                                 wave_sizze_10591) *
                                                         wave_sizze_10591) &
                                                        (2 * offset_10607 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10600 = ((volatile __local
                                    float *) red_arr_mem_10595)[local_tid_10589 +
                                                                offset_10607];
                    }
                    // apply reduction operation
                    {
                        float res_10601 = x_10599 + x_10600;
                        
                        x_10599 = res_10601;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10595)[local_tid_10589] =
                            x_10599;
                    }
                }
                offset_10607 *= 2;
            }
            skip_waves_10608 = 1;
            while (slt32(skip_waves_10608, squot32(segred_group_sizze_10150 +
                                                   wave_sizze_10591 - 1,
                                                   wave_sizze_10591))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10607 = skip_waves_10608 * wave_sizze_10591;
                if (slt32(local_tid_10589 + offset_10607,
                          segred_group_sizze_10150) && ((local_tid_10589 -
                                                         squot32(local_tid_10589,
                                                                 wave_sizze_10591) *
                                                         wave_sizze_10591) ==
                                                        0 &&
                                                        (squot32(local_tid_10589,
                                                                 wave_sizze_10591) &
                                                         (2 * skip_waves_10608 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10600 = ((__local
                                    float *) red_arr_mem_10595)[local_tid_10589 +
                                                                offset_10607];
                    }
                    // apply reduction operation
                    {
                        float res_10601 = x_10599 + x_10600;
                        
                        x_10599 = res_10601;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10595)[local_tid_10589] =
                            x_10599;
                    }
                }
                skip_waves_10608 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10589 == 0) {
                    ((__global float *) mem_10232)[0] = x_10599;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10168(__local volatile
                                  int64_t *sync_arr_mem_10620_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10622_backing_aligned_1,
                                  int32_t sizze_9889, int32_t num_groups_10163,
                                  __global unsigned char *y_mem_10228, __global
                                  unsigned char *mem_10236, __global
                                  unsigned char *counter_mem_10610, __global
                                  unsigned char *group_res_arr_mem_10612,
                                  int32_t num_threads_10614)
{
    const int32_t segred_group_sizze_10161 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_10160;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10620_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10620_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10622_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10622_backing_aligned_1;
    int32_t global_tid_10615;
    int32_t local_tid_10616;
    int32_t group_sizze_10619;
    int32_t wave_sizze_10618;
    int32_t group_tid_10617;
    
    global_tid_10615 = get_global_id(0);
    local_tid_10616 = get_local_id(0);
    group_sizze_10619 = get_local_size(0);
    wave_sizze_10618 = LOCKSTEP_WIDTH;
    group_tid_10617 = get_group_id(0);
    
    int32_t phys_tid_10168 = global_tid_10615;
    __local char *sync_arr_mem_10620;
    
    sync_arr_mem_10620 = (__local char *) sync_arr_mem_10620_backing_0;
    
    __local char *red_arr_mem_10622;
    
    red_arr_mem_10622 = (__local char *) red_arr_mem_10622_backing_1;
    
    int32_t dummy_10166 = 0;
    int32_t gtid_10167;
    
    gtid_10167 = 0;
    
    float x_acc_10624;
    int32_t chunk_sizze_10625 = smin32(squot32(sizze_9889 +
                                               segred_group_sizze_10161 *
                                               num_groups_10163 - 1,
                                               segred_group_sizze_10161 *
                                               num_groups_10163),
                                       squot32(sizze_9889 - phys_tid_10168 +
                                               num_threads_10614 - 1,
                                               num_threads_10614));
    float x_9898;
    float x_9899;
    
    // neutral-initialise the accumulators
    {
        x_acc_10624 = 0.0F;
    }
    for (int32_t i_10629 = 0; i_10629 < chunk_sizze_10625; i_10629++) {
        gtid_10167 = phys_tid_10168 + num_threads_10614 * i_10629;
        // apply map function
        {
            float x_9901 = ((__global float *) y_mem_10228)[gtid_10167];
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9898 = x_acc_10624;
            }
            // load new values
            {
                x_9899 = x_9901;
            }
            // apply reduction operator
            {
                float res_9900 = x_9898 + x_9899;
                
                // store in accumulator
                {
                    x_acc_10624 = res_9900;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9898 = x_acc_10624;
        ((__local float *) red_arr_mem_10622)[local_tid_10616] = x_9898;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10630;
    int32_t skip_waves_10631;
    float x_10626;
    float x_10627;
    
    offset_10630 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10616, segred_group_sizze_10161)) {
            x_10626 = ((__local float *) red_arr_mem_10622)[local_tid_10616 +
                                                            offset_10630];
        }
    }
    offset_10630 = 1;
    while (slt32(offset_10630, wave_sizze_10618)) {
        if (slt32(local_tid_10616 + offset_10630, segred_group_sizze_10161) &&
            ((local_tid_10616 - squot32(local_tid_10616, wave_sizze_10618) *
              wave_sizze_10618) & (2 * offset_10630 - 1)) == 0) {
            // read array element
            {
                x_10627 = ((volatile __local
                            float *) red_arr_mem_10622)[local_tid_10616 +
                                                        offset_10630];
            }
            // apply reduction operation
            {
                float res_10628 = x_10626 + x_10627;
                
                x_10626 = res_10628;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10622)[local_tid_10616] = x_10626;
            }
        }
        offset_10630 *= 2;
    }
    skip_waves_10631 = 1;
    while (slt32(skip_waves_10631, squot32(segred_group_sizze_10161 +
                                           wave_sizze_10618 - 1,
                                           wave_sizze_10618))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10630 = skip_waves_10631 * wave_sizze_10618;
        if (slt32(local_tid_10616 + offset_10630, segred_group_sizze_10161) &&
            ((local_tid_10616 - squot32(local_tid_10616, wave_sizze_10618) *
              wave_sizze_10618) == 0 && (squot32(local_tid_10616,
                                                 wave_sizze_10618) & (2 *
                                                                      skip_waves_10631 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10627 = ((__local
                            float *) red_arr_mem_10622)[local_tid_10616 +
                                                        offset_10630];
            }
            // apply reduction operation
            {
                float res_10628 = x_10626 + x_10627;
                
                x_10626 = res_10628;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10622)[local_tid_10616] =
                    x_10626;
            }
        }
        skip_waves_10631 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10616 == 0) {
            x_acc_10624 = x_10626;
        }
    }
    
    int32_t old_counter_10632;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10616 == 0) {
            ((__global float *) group_res_arr_mem_10612)[group_tid_10617 *
                                                         segred_group_sizze_10161] =
                x_acc_10624;
            mem_fence_global();
            old_counter_10632 = atomic_add(&((volatile __global
                                              int *) counter_mem_10610)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10620)[0] = old_counter_10632 ==
                num_groups_10163 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10633 = ((__local bool *) sync_arr_mem_10620)[0];
    
    if (is_last_group_10633) {
        if (local_tid_10616 == 0) {
            old_counter_10632 = atomic_add(&((volatile __global
                                              int *) counter_mem_10610)[0],
                                           (int) (0 - num_groups_10163));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10616, num_groups_10163)) {
                x_9898 = ((__global
                           float *) group_res_arr_mem_10612)[local_tid_10616 *
                                                             segred_group_sizze_10161];
            } else {
                x_9898 = 0.0F;
            }
            ((__local float *) red_arr_mem_10622)[local_tid_10616] = x_9898;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10634;
            int32_t skip_waves_10635;
            float x_10626;
            float x_10627;
            
            offset_10634 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10616, segred_group_sizze_10161)) {
                    x_10626 = ((__local
                                float *) red_arr_mem_10622)[local_tid_10616 +
                                                            offset_10634];
                }
            }
            offset_10634 = 1;
            while (slt32(offset_10634, wave_sizze_10618)) {
                if (slt32(local_tid_10616 + offset_10634,
                          segred_group_sizze_10161) && ((local_tid_10616 -
                                                         squot32(local_tid_10616,
                                                                 wave_sizze_10618) *
                                                         wave_sizze_10618) &
                                                        (2 * offset_10634 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10627 = ((volatile __local
                                    float *) red_arr_mem_10622)[local_tid_10616 +
                                                                offset_10634];
                    }
                    // apply reduction operation
                    {
                        float res_10628 = x_10626 + x_10627;
                        
                        x_10626 = res_10628;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10622)[local_tid_10616] =
                            x_10626;
                    }
                }
                offset_10634 *= 2;
            }
            skip_waves_10635 = 1;
            while (slt32(skip_waves_10635, squot32(segred_group_sizze_10161 +
                                                   wave_sizze_10618 - 1,
                                                   wave_sizze_10618))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10634 = skip_waves_10635 * wave_sizze_10618;
                if (slt32(local_tid_10616 + offset_10634,
                          segred_group_sizze_10161) && ((local_tid_10616 -
                                                         squot32(local_tid_10616,
                                                                 wave_sizze_10618) *
                                                         wave_sizze_10618) ==
                                                        0 &&
                                                        (squot32(local_tid_10616,
                                                                 wave_sizze_10618) &
                                                         (2 * skip_waves_10635 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10627 = ((__local
                                    float *) red_arr_mem_10622)[local_tid_10616 +
                                                                offset_10634];
                    }
                    // apply reduction operation
                    {
                        float res_10628 = x_10626 + x_10627;
                        
                        x_10626 = res_10628;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10622)[local_tid_10616] =
                            x_10626;
                    }
                }
                skip_waves_10635 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10616 == 0) {
                    ((__global float *) mem_10236)[0] = x_10626;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10179(__local volatile
                                  int64_t *sync_arr_mem_10647_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10649_backing_aligned_1,
                                  int32_t sizze_9888, float res_9892,
                                  float res_9897, int32_t num_groups_10174,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *y_mem_10228, __global
                                  unsigned char *mem_10240, __global
                                  unsigned char *counter_mem_10637, __global
                                  unsigned char *group_res_arr_mem_10639,
                                  int32_t num_threads_10641)
{
    const int32_t segred_group_sizze_10172 =
                  kullback_liebler_scaled_f32zisegred_group_sizze_10171;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10647_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10647_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10649_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10649_backing_aligned_1;
    int32_t global_tid_10642;
    int32_t local_tid_10643;
    int32_t group_sizze_10646;
    int32_t wave_sizze_10645;
    int32_t group_tid_10644;
    
    global_tid_10642 = get_global_id(0);
    local_tid_10643 = get_local_id(0);
    group_sizze_10646 = get_local_size(0);
    wave_sizze_10645 = LOCKSTEP_WIDTH;
    group_tid_10644 = get_group_id(0);
    
    int32_t phys_tid_10179 = global_tid_10642;
    __local char *sync_arr_mem_10647;
    
    sync_arr_mem_10647 = (__local char *) sync_arr_mem_10647_backing_0;
    
    __local char *red_arr_mem_10649;
    
    red_arr_mem_10649 = (__local char *) red_arr_mem_10649_backing_1;
    
    int32_t dummy_10177 = 0;
    int32_t gtid_10178;
    
    gtid_10178 = 0;
    
    float x_acc_10651;
    int32_t chunk_sizze_10652 = smin32(squot32(sizze_9888 +
                                               segred_group_sizze_10172 *
                                               num_groups_10174 - 1,
                                               segred_group_sizze_10172 *
                                               num_groups_10174),
                                       squot32(sizze_9888 - phys_tid_10179 +
                                               num_threads_10641 - 1,
                                               num_threads_10641));
    float x_9910;
    float x_9911;
    
    // neutral-initialise the accumulators
    {
        x_acc_10651 = 0.0F;
    }
    for (int32_t i_10656 = 0; i_10656 < chunk_sizze_10652; i_10656++) {
        gtid_10178 = phys_tid_10179 + num_threads_10641 * i_10656;
        // apply map function
        {
            float x_9913 = ((__global float *) x_mem_10227)[gtid_10178];
            float x_9914 = ((__global float *) y_mem_10228)[gtid_10178];
            float res_9915 = x_9913 / res_9892;
            float res_9916 = x_9914 / res_9897;
            float res_9917 = res_9915 / res_9916;
            float res_9918;
            
            res_9918 = futrts_log32(res_9917);
            
            float res_9919 = res_9915 * res_9918;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9910 = x_acc_10651;
            }
            // load new values
            {
                x_9911 = res_9919;
            }
            // apply reduction operator
            {
                float res_9912 = x_9910 + x_9911;
                
                // store in accumulator
                {
                    x_acc_10651 = res_9912;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9910 = x_acc_10651;
        ((__local float *) red_arr_mem_10649)[local_tid_10643] = x_9910;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10657;
    int32_t skip_waves_10658;
    float x_10653;
    float x_10654;
    
    offset_10657 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10643, segred_group_sizze_10172)) {
            x_10653 = ((__local float *) red_arr_mem_10649)[local_tid_10643 +
                                                            offset_10657];
        }
    }
    offset_10657 = 1;
    while (slt32(offset_10657, wave_sizze_10645)) {
        if (slt32(local_tid_10643 + offset_10657, segred_group_sizze_10172) &&
            ((local_tid_10643 - squot32(local_tid_10643, wave_sizze_10645) *
              wave_sizze_10645) & (2 * offset_10657 - 1)) == 0) {
            // read array element
            {
                x_10654 = ((volatile __local
                            float *) red_arr_mem_10649)[local_tid_10643 +
                                                        offset_10657];
            }
            // apply reduction operation
            {
                float res_10655 = x_10653 + x_10654;
                
                x_10653 = res_10655;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10649)[local_tid_10643] = x_10653;
            }
        }
        offset_10657 *= 2;
    }
    skip_waves_10658 = 1;
    while (slt32(skip_waves_10658, squot32(segred_group_sizze_10172 +
                                           wave_sizze_10645 - 1,
                                           wave_sizze_10645))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10657 = skip_waves_10658 * wave_sizze_10645;
        if (slt32(local_tid_10643 + offset_10657, segred_group_sizze_10172) &&
            ((local_tid_10643 - squot32(local_tid_10643, wave_sizze_10645) *
              wave_sizze_10645) == 0 && (squot32(local_tid_10643,
                                                 wave_sizze_10645) & (2 *
                                                                      skip_waves_10658 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10654 = ((__local
                            float *) red_arr_mem_10649)[local_tid_10643 +
                                                        offset_10657];
            }
            // apply reduction operation
            {
                float res_10655 = x_10653 + x_10654;
                
                x_10653 = res_10655;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10649)[local_tid_10643] =
                    x_10653;
            }
        }
        skip_waves_10658 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10643 == 0) {
            x_acc_10651 = x_10653;
        }
    }
    
    int32_t old_counter_10659;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10643 == 0) {
            ((__global float *) group_res_arr_mem_10639)[group_tid_10644 *
                                                         segred_group_sizze_10172] =
                x_acc_10651;
            mem_fence_global();
            old_counter_10659 = atomic_add(&((volatile __global
                                              int *) counter_mem_10637)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10647)[0] = old_counter_10659 ==
                num_groups_10174 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10660 = ((__local bool *) sync_arr_mem_10647)[0];
    
    if (is_last_group_10660) {
        if (local_tid_10643 == 0) {
            old_counter_10659 = atomic_add(&((volatile __global
                                              int *) counter_mem_10637)[0],
                                           (int) (0 - num_groups_10174));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10643, num_groups_10174)) {
                x_9910 = ((__global
                           float *) group_res_arr_mem_10639)[local_tid_10643 *
                                                             segred_group_sizze_10172];
            } else {
                x_9910 = 0.0F;
            }
            ((__local float *) red_arr_mem_10649)[local_tid_10643] = x_9910;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10661;
            int32_t skip_waves_10662;
            float x_10653;
            float x_10654;
            
            offset_10661 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10643, segred_group_sizze_10172)) {
                    x_10653 = ((__local
                                float *) red_arr_mem_10649)[local_tid_10643 +
                                                            offset_10661];
                }
            }
            offset_10661 = 1;
            while (slt32(offset_10661, wave_sizze_10645)) {
                if (slt32(local_tid_10643 + offset_10661,
                          segred_group_sizze_10172) && ((local_tid_10643 -
                                                         squot32(local_tid_10643,
                                                                 wave_sizze_10645) *
                                                         wave_sizze_10645) &
                                                        (2 * offset_10661 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10654 = ((volatile __local
                                    float *) red_arr_mem_10649)[local_tid_10643 +
                                                                offset_10661];
                    }
                    // apply reduction operation
                    {
                        float res_10655 = x_10653 + x_10654;
                        
                        x_10653 = res_10655;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10649)[local_tid_10643] =
                            x_10653;
                    }
                }
                offset_10661 *= 2;
            }
            skip_waves_10662 = 1;
            while (slt32(skip_waves_10662, squot32(segred_group_sizze_10172 +
                                                   wave_sizze_10645 - 1,
                                                   wave_sizze_10645))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10661 = skip_waves_10662 * wave_sizze_10645;
                if (slt32(local_tid_10643 + offset_10661,
                          segred_group_sizze_10172) && ((local_tid_10643 -
                                                         squot32(local_tid_10643,
                                                                 wave_sizze_10645) *
                                                         wave_sizze_10645) ==
                                                        0 &&
                                                        (squot32(local_tid_10643,
                                                                 wave_sizze_10645) &
                                                         (2 * skip_waves_10662 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10654 = ((__local
                                    float *) red_arr_mem_10649)[local_tid_10643 +
                                                                offset_10661];
                    }
                    // apply reduction operation
                    {
                        float res_10655 = x_10653 + x_10654;
                        
                        x_10653 = res_10655;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10649)[local_tid_10643] =
                            x_10653;
                    }
                }
                skip_waves_10662 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10643 == 0) {
                    ((__global float *) mem_10240)[0] = x_10653;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10190(__local volatile
                                  int64_t *sync_arr_mem_10675_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10677_backing_aligned_1,
                                  int32_t sizze_9920, int32_t num_groups_10185,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10665, __global
                                  unsigned char *group_res_arr_mem_10667,
                                  int32_t num_threads_10669)
{
    const int32_t segred_group_sizze_10183 =
                  hellinger_f32zisegred_group_sizze_10182;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10675_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10675_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10677_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10677_backing_aligned_1;
    int32_t global_tid_10670;
    int32_t local_tid_10671;
    int32_t group_sizze_10674;
    int32_t wave_sizze_10673;
    int32_t group_tid_10672;
    
    global_tid_10670 = get_global_id(0);
    local_tid_10671 = get_local_id(0);
    group_sizze_10674 = get_local_size(0);
    wave_sizze_10673 = LOCKSTEP_WIDTH;
    group_tid_10672 = get_group_id(0);
    
    int32_t phys_tid_10190 = global_tid_10670;
    __local char *sync_arr_mem_10675;
    
    sync_arr_mem_10675 = (__local char *) sync_arr_mem_10675_backing_0;
    
    __local char *red_arr_mem_10677;
    
    red_arr_mem_10677 = (__local char *) red_arr_mem_10677_backing_1;
    
    int32_t dummy_10188 = 0;
    int32_t gtid_10189;
    
    gtid_10189 = 0;
    
    float x_acc_10679;
    int32_t chunk_sizze_10680 = smin32(squot32(sizze_9920 +
                                               segred_group_sizze_10183 *
                                               num_groups_10185 - 1,
                                               segred_group_sizze_10183 *
                                               num_groups_10185),
                                       squot32(sizze_9920 - phys_tid_10190 +
                                               num_threads_10669 - 1,
                                               num_threads_10669));
    float x_9932;
    float x_9933;
    
    // neutral-initialise the accumulators
    {
        x_acc_10679 = 0.0F;
    }
    for (int32_t i_10684 = 0; i_10684 < chunk_sizze_10680; i_10684++) {
        gtid_10189 = phys_tid_10190 + num_threads_10669 * i_10684;
        // apply map function
        {
            float x_9935 = ((__global float *) x_mem_10227)[gtid_10189];
            float x_9936 = ((__global float *) x_mem_10228)[gtid_10189];
            float res_9937;
            
            res_9937 = futrts_sqrt32(x_9935);
            
            float res_9938;
            
            res_9938 = futrts_sqrt32(x_9936);
            
            float res_9939 = res_9937 - res_9938;
            float res_9940 = fpow32(res_9939, 2.0F);
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9932 = x_acc_10679;
            }
            // load new values
            {
                x_9933 = res_9940;
            }
            // apply reduction operator
            {
                float res_9934 = x_9932 + x_9933;
                
                // store in accumulator
                {
                    x_acc_10679 = res_9934;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9932 = x_acc_10679;
        ((__local float *) red_arr_mem_10677)[local_tid_10671] = x_9932;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10685;
    int32_t skip_waves_10686;
    float x_10681;
    float x_10682;
    
    offset_10685 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10671, segred_group_sizze_10183)) {
            x_10681 = ((__local float *) red_arr_mem_10677)[local_tid_10671 +
                                                            offset_10685];
        }
    }
    offset_10685 = 1;
    while (slt32(offset_10685, wave_sizze_10673)) {
        if (slt32(local_tid_10671 + offset_10685, segred_group_sizze_10183) &&
            ((local_tid_10671 - squot32(local_tid_10671, wave_sizze_10673) *
              wave_sizze_10673) & (2 * offset_10685 - 1)) == 0) {
            // read array element
            {
                x_10682 = ((volatile __local
                            float *) red_arr_mem_10677)[local_tid_10671 +
                                                        offset_10685];
            }
            // apply reduction operation
            {
                float res_10683 = x_10681 + x_10682;
                
                x_10681 = res_10683;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10677)[local_tid_10671] = x_10681;
            }
        }
        offset_10685 *= 2;
    }
    skip_waves_10686 = 1;
    while (slt32(skip_waves_10686, squot32(segred_group_sizze_10183 +
                                           wave_sizze_10673 - 1,
                                           wave_sizze_10673))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10685 = skip_waves_10686 * wave_sizze_10673;
        if (slt32(local_tid_10671 + offset_10685, segred_group_sizze_10183) &&
            ((local_tid_10671 - squot32(local_tid_10671, wave_sizze_10673) *
              wave_sizze_10673) == 0 && (squot32(local_tid_10671,
                                                 wave_sizze_10673) & (2 *
                                                                      skip_waves_10686 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10682 = ((__local
                            float *) red_arr_mem_10677)[local_tid_10671 +
                                                        offset_10685];
            }
            // apply reduction operation
            {
                float res_10683 = x_10681 + x_10682;
                
                x_10681 = res_10683;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10677)[local_tid_10671] =
                    x_10681;
            }
        }
        skip_waves_10686 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10671 == 0) {
            x_acc_10679 = x_10681;
        }
    }
    
    int32_t old_counter_10687;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10671 == 0) {
            ((__global float *) group_res_arr_mem_10667)[group_tid_10672 *
                                                         segred_group_sizze_10183] =
                x_acc_10679;
            mem_fence_global();
            old_counter_10687 = atomic_add(&((volatile __global
                                              int *) counter_mem_10665)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10675)[0] = old_counter_10687 ==
                num_groups_10185 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10688 = ((__local bool *) sync_arr_mem_10675)[0];
    
    if (is_last_group_10688) {
        if (local_tid_10671 == 0) {
            old_counter_10687 = atomic_add(&((volatile __global
                                              int *) counter_mem_10665)[0],
                                           (int) (0 - num_groups_10185));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10671, num_groups_10185)) {
                x_9932 = ((__global
                           float *) group_res_arr_mem_10667)[local_tid_10671 *
                                                             segred_group_sizze_10183];
            } else {
                x_9932 = 0.0F;
            }
            ((__local float *) red_arr_mem_10677)[local_tid_10671] = x_9932;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10689;
            int32_t skip_waves_10690;
            float x_10681;
            float x_10682;
            
            offset_10689 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10671, segred_group_sizze_10183)) {
                    x_10681 = ((__local
                                float *) red_arr_mem_10677)[local_tid_10671 +
                                                            offset_10689];
                }
            }
            offset_10689 = 1;
            while (slt32(offset_10689, wave_sizze_10673)) {
                if (slt32(local_tid_10671 + offset_10689,
                          segred_group_sizze_10183) && ((local_tid_10671 -
                                                         squot32(local_tid_10671,
                                                                 wave_sizze_10673) *
                                                         wave_sizze_10673) &
                                                        (2 * offset_10689 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10682 = ((volatile __local
                                    float *) red_arr_mem_10677)[local_tid_10671 +
                                                                offset_10689];
                    }
                    // apply reduction operation
                    {
                        float res_10683 = x_10681 + x_10682;
                        
                        x_10681 = res_10683;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10677)[local_tid_10671] =
                            x_10681;
                    }
                }
                offset_10689 *= 2;
            }
            skip_waves_10690 = 1;
            while (slt32(skip_waves_10690, squot32(segred_group_sizze_10183 +
                                                   wave_sizze_10673 - 1,
                                                   wave_sizze_10673))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10689 = skip_waves_10690 * wave_sizze_10673;
                if (slt32(local_tid_10671 + offset_10689,
                          segred_group_sizze_10183) && ((local_tid_10671 -
                                                         squot32(local_tid_10671,
                                                                 wave_sizze_10673) *
                                                         wave_sizze_10673) ==
                                                        0 &&
                                                        (squot32(local_tid_10671,
                                                                 wave_sizze_10673) &
                                                         (2 * skip_waves_10690 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10682 = ((__local
                                    float *) red_arr_mem_10677)[local_tid_10671 +
                                                                offset_10689];
                    }
                    // apply reduction operation
                    {
                        float res_10683 = x_10681 + x_10682;
                        
                        x_10681 = res_10683;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10677)[local_tid_10671] =
                            x_10681;
                    }
                }
                skip_waves_10690 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10671 == 0) {
                    ((__global float *) mem_10232)[0] = x_10681;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10201(__local volatile
                                  int64_t *sync_arr_mem_10703_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10705_backing_aligned_1,
                                  int32_t sizze_9943, int32_t num_groups_10196,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10693, __global
                                  unsigned char *group_res_arr_mem_10695,
                                  int32_t num_threads_10697)
{
    const int32_t segred_group_sizze_10194 =
                  hellinger_f64zisegred_group_sizze_10193;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10703_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10703_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10705_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10705_backing_aligned_1;
    int32_t global_tid_10698;
    int32_t local_tid_10699;
    int32_t group_sizze_10702;
    int32_t wave_sizze_10701;
    int32_t group_tid_10700;
    
    global_tid_10698 = get_global_id(0);
    local_tid_10699 = get_local_id(0);
    group_sizze_10702 = get_local_size(0);
    wave_sizze_10701 = LOCKSTEP_WIDTH;
    group_tid_10700 = get_group_id(0);
    
    int32_t phys_tid_10201 = global_tid_10698;
    __local char *sync_arr_mem_10703;
    
    sync_arr_mem_10703 = (__local char *) sync_arr_mem_10703_backing_0;
    
    __local char *red_arr_mem_10705;
    
    red_arr_mem_10705 = (__local char *) red_arr_mem_10705_backing_1;
    
    int32_t dummy_10199 = 0;
    int32_t gtid_10200;
    
    gtid_10200 = 0;
    
    double x_acc_10707;
    int32_t chunk_sizze_10708 = smin32(squot32(sizze_9943 +
                                               segred_group_sizze_10194 *
                                               num_groups_10196 - 1,
                                               segred_group_sizze_10194 *
                                               num_groups_10196),
                                       squot32(sizze_9943 - phys_tid_10201 +
                                               num_threads_10697 - 1,
                                               num_threads_10697));
    double x_9955;
    double x_9956;
    
    // neutral-initialise the accumulators
    {
        x_acc_10707 = 0.0;
    }
    for (int32_t i_10712 = 0; i_10712 < chunk_sizze_10708; i_10712++) {
        gtid_10200 = phys_tid_10201 + num_threads_10697 * i_10712;
        // apply map function
        {
            double x_9958 = ((__global double *) x_mem_10227)[gtid_10200];
            double x_9959 = ((__global double *) x_mem_10228)[gtid_10200];
            double res_9960;
            
            res_9960 = futrts_sqrt64(x_9958);
            
            double res_9961;
            
            res_9961 = futrts_sqrt64(x_9959);
            
            double res_9962 = res_9960 - res_9961;
            double res_9963 = fpow64(res_9962, 2.0);
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9955 = x_acc_10707;
            }
            // load new values
            {
                x_9956 = res_9963;
            }
            // apply reduction operator
            {
                double res_9957 = x_9955 + x_9956;
                
                // store in accumulator
                {
                    x_acc_10707 = res_9957;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9955 = x_acc_10707;
        ((__local double *) red_arr_mem_10705)[local_tid_10699] = x_9955;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10713;
    int32_t skip_waves_10714;
    double x_10709;
    double x_10710;
    
    offset_10713 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10699, segred_group_sizze_10194)) {
            x_10709 = ((__local double *) red_arr_mem_10705)[local_tid_10699 +
                                                             offset_10713];
        }
    }
    offset_10713 = 1;
    while (slt32(offset_10713, wave_sizze_10701)) {
        if (slt32(local_tid_10699 + offset_10713, segred_group_sizze_10194) &&
            ((local_tid_10699 - squot32(local_tid_10699, wave_sizze_10701) *
              wave_sizze_10701) & (2 * offset_10713 - 1)) == 0) {
            // read array element
            {
                x_10710 = ((volatile __local
                            double *) red_arr_mem_10705)[local_tid_10699 +
                                                         offset_10713];
            }
            // apply reduction operation
            {
                double res_10711 = x_10709 + x_10710;
                
                x_10709 = res_10711;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10705)[local_tid_10699] = x_10709;
            }
        }
        offset_10713 *= 2;
    }
    skip_waves_10714 = 1;
    while (slt32(skip_waves_10714, squot32(segred_group_sizze_10194 +
                                           wave_sizze_10701 - 1,
                                           wave_sizze_10701))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10713 = skip_waves_10714 * wave_sizze_10701;
        if (slt32(local_tid_10699 + offset_10713, segred_group_sizze_10194) &&
            ((local_tid_10699 - squot32(local_tid_10699, wave_sizze_10701) *
              wave_sizze_10701) == 0 && (squot32(local_tid_10699,
                                                 wave_sizze_10701) & (2 *
                                                                      skip_waves_10714 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10710 = ((__local
                            double *) red_arr_mem_10705)[local_tid_10699 +
                                                         offset_10713];
            }
            // apply reduction operation
            {
                double res_10711 = x_10709 + x_10710;
                
                x_10709 = res_10711;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10705)[local_tid_10699] =
                    x_10709;
            }
        }
        skip_waves_10714 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10699 == 0) {
            x_acc_10707 = x_10709;
        }
    }
    
    int32_t old_counter_10715;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10699 == 0) {
            ((__global double *) group_res_arr_mem_10695)[group_tid_10700 *
                                                          segred_group_sizze_10194] =
                x_acc_10707;
            mem_fence_global();
            old_counter_10715 = atomic_add(&((volatile __global
                                              int *) counter_mem_10693)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10703)[0] = old_counter_10715 ==
                num_groups_10196 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10716 = ((__local bool *) sync_arr_mem_10703)[0];
    
    if (is_last_group_10716) {
        if (local_tid_10699 == 0) {
            old_counter_10715 = atomic_add(&((volatile __global
                                              int *) counter_mem_10693)[0],
                                           (int) (0 - num_groups_10196));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10699, num_groups_10196)) {
                x_9955 = ((__global
                           double *) group_res_arr_mem_10695)[local_tid_10699 *
                                                              segred_group_sizze_10194];
            } else {
                x_9955 = 0.0;
            }
            ((__local double *) red_arr_mem_10705)[local_tid_10699] = x_9955;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10717;
            int32_t skip_waves_10718;
            double x_10709;
            double x_10710;
            
            offset_10717 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10699, segred_group_sizze_10194)) {
                    x_10709 = ((__local
                                double *) red_arr_mem_10705)[local_tid_10699 +
                                                             offset_10717];
                }
            }
            offset_10717 = 1;
            while (slt32(offset_10717, wave_sizze_10701)) {
                if (slt32(local_tid_10699 + offset_10717,
                          segred_group_sizze_10194) && ((local_tid_10699 -
                                                         squot32(local_tid_10699,
                                                                 wave_sizze_10701) *
                                                         wave_sizze_10701) &
                                                        (2 * offset_10717 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10710 = ((volatile __local
                                    double *) red_arr_mem_10705)[local_tid_10699 +
                                                                 offset_10717];
                    }
                    // apply reduction operation
                    {
                        double res_10711 = x_10709 + x_10710;
                        
                        x_10709 = res_10711;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10705)[local_tid_10699] =
                            x_10709;
                    }
                }
                offset_10717 *= 2;
            }
            skip_waves_10718 = 1;
            while (slt32(skip_waves_10718, squot32(segred_group_sizze_10194 +
                                                   wave_sizze_10701 - 1,
                                                   wave_sizze_10701))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10717 = skip_waves_10718 * wave_sizze_10701;
                if (slt32(local_tid_10699 + offset_10717,
                          segred_group_sizze_10194) && ((local_tid_10699 -
                                                         squot32(local_tid_10699,
                                                                 wave_sizze_10701) *
                                                         wave_sizze_10701) ==
                                                        0 &&
                                                        (squot32(local_tid_10699,
                                                                 wave_sizze_10701) &
                                                         (2 * skip_waves_10718 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10710 = ((__local
                                    double *) red_arr_mem_10705)[local_tid_10699 +
                                                                 offset_10717];
                    }
                    // apply reduction operation
                    {
                        double res_10711 = x_10709 + x_10710;
                        
                        x_10709 = res_10711;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10705)[local_tid_10699] =
                            x_10709;
                    }
                }
                skip_waves_10718 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10699 == 0) {
                    ((__global double *) mem_10232)[0] = x_10709;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10212(__local volatile
                                  int64_t *sync_arr_mem_10731_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10733_backing_aligned_1,
                                  int32_t sizze_9966, float res_9981,
                                  float res_9983, int32_t num_groups_10207,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10721, __global
                                  unsigned char *group_res_arr_mem_10723,
                                  int32_t num_threads_10725)
{
    const int32_t segred_group_sizze_10205 =
                  alpha_divergence_f32zisegred_group_sizze_10204;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10731_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10731_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10733_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10733_backing_aligned_1;
    int32_t global_tid_10726;
    int32_t local_tid_10727;
    int32_t group_sizze_10730;
    int32_t wave_sizze_10729;
    int32_t group_tid_10728;
    
    global_tid_10726 = get_global_id(0);
    local_tid_10727 = get_local_id(0);
    group_sizze_10730 = get_local_size(0);
    wave_sizze_10729 = LOCKSTEP_WIDTH;
    group_tid_10728 = get_group_id(0);
    
    int32_t phys_tid_10212 = global_tid_10726;
    __local char *sync_arr_mem_10731;
    
    sync_arr_mem_10731 = (__local char *) sync_arr_mem_10731_backing_0;
    
    __local char *red_arr_mem_10733;
    
    red_arr_mem_10733 = (__local char *) red_arr_mem_10733_backing_1;
    
    int32_t dummy_10210 = 0;
    int32_t gtid_10211;
    
    gtid_10211 = 0;
    
    float x_acc_10735;
    int32_t chunk_sizze_10736 = smin32(squot32(sizze_9966 +
                                               segred_group_sizze_10205 *
                                               num_groups_10207 - 1,
                                               segred_group_sizze_10205 *
                                               num_groups_10207),
                                       squot32(sizze_9966 - phys_tid_10212 +
                                               num_threads_10725 - 1,
                                               num_threads_10725));
    float x_9986;
    float x_9987;
    
    // neutral-initialise the accumulators
    {
        x_acc_10735 = 0.0F;
    }
    for (int32_t i_10740 = 0; i_10740 < chunk_sizze_10736; i_10740++) {
        gtid_10211 = phys_tid_10212 + num_threads_10725 * i_10740;
        // apply map function
        {
            float x_9989 = ((__global float *) x_mem_10227)[gtid_10211];
            float x_9990 = ((__global float *) x_mem_10228)[gtid_10211];
            float res_9991 = fpow32(x_9989, res_9981);
            float res_9992 = fpow32(x_9990, res_9983);
            float res_9993 = res_9991 * res_9992;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_9986 = x_acc_10735;
            }
            // load new values
            {
                x_9987 = res_9993;
            }
            // apply reduction operator
            {
                float res_9988 = x_9986 + x_9987;
                
                // store in accumulator
                {
                    x_acc_10735 = res_9988;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_9986 = x_acc_10735;
        ((__local float *) red_arr_mem_10733)[local_tid_10727] = x_9986;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10741;
    int32_t skip_waves_10742;
    float x_10737;
    float x_10738;
    
    offset_10741 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10727, segred_group_sizze_10205)) {
            x_10737 = ((__local float *) red_arr_mem_10733)[local_tid_10727 +
                                                            offset_10741];
        }
    }
    offset_10741 = 1;
    while (slt32(offset_10741, wave_sizze_10729)) {
        if (slt32(local_tid_10727 + offset_10741, segred_group_sizze_10205) &&
            ((local_tid_10727 - squot32(local_tid_10727, wave_sizze_10729) *
              wave_sizze_10729) & (2 * offset_10741 - 1)) == 0) {
            // read array element
            {
                x_10738 = ((volatile __local
                            float *) red_arr_mem_10733)[local_tid_10727 +
                                                        offset_10741];
            }
            // apply reduction operation
            {
                float res_10739 = x_10737 + x_10738;
                
                x_10737 = res_10739;
            }
            // write result of operation
            {
                ((volatile __local
                  float *) red_arr_mem_10733)[local_tid_10727] = x_10737;
            }
        }
        offset_10741 *= 2;
    }
    skip_waves_10742 = 1;
    while (slt32(skip_waves_10742, squot32(segred_group_sizze_10205 +
                                           wave_sizze_10729 - 1,
                                           wave_sizze_10729))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10741 = skip_waves_10742 * wave_sizze_10729;
        if (slt32(local_tid_10727 + offset_10741, segred_group_sizze_10205) &&
            ((local_tid_10727 - squot32(local_tid_10727, wave_sizze_10729) *
              wave_sizze_10729) == 0 && (squot32(local_tid_10727,
                                                 wave_sizze_10729) & (2 *
                                                                      skip_waves_10742 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10738 = ((__local
                            float *) red_arr_mem_10733)[local_tid_10727 +
                                                        offset_10741];
            }
            // apply reduction operation
            {
                float res_10739 = x_10737 + x_10738;
                
                x_10737 = res_10739;
            }
            // write result of operation
            {
                ((__local float *) red_arr_mem_10733)[local_tid_10727] =
                    x_10737;
            }
        }
        skip_waves_10742 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10727 == 0) {
            x_acc_10735 = x_10737;
        }
    }
    
    int32_t old_counter_10743;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10727 == 0) {
            ((__global float *) group_res_arr_mem_10723)[group_tid_10728 *
                                                         segred_group_sizze_10205] =
                x_acc_10735;
            mem_fence_global();
            old_counter_10743 = atomic_add(&((volatile __global
                                              int *) counter_mem_10721)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10731)[0] = old_counter_10743 ==
                num_groups_10207 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10744 = ((__local bool *) sync_arr_mem_10731)[0];
    
    if (is_last_group_10744) {
        if (local_tid_10727 == 0) {
            old_counter_10743 = atomic_add(&((volatile __global
                                              int *) counter_mem_10721)[0],
                                           (int) (0 - num_groups_10207));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10727, num_groups_10207)) {
                x_9986 = ((__global
                           float *) group_res_arr_mem_10723)[local_tid_10727 *
                                                             segred_group_sizze_10205];
            } else {
                x_9986 = 0.0F;
            }
            ((__local float *) red_arr_mem_10733)[local_tid_10727] = x_9986;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10745;
            int32_t skip_waves_10746;
            float x_10737;
            float x_10738;
            
            offset_10745 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10727, segred_group_sizze_10205)) {
                    x_10737 = ((__local
                                float *) red_arr_mem_10733)[local_tid_10727 +
                                                            offset_10745];
                }
            }
            offset_10745 = 1;
            while (slt32(offset_10745, wave_sizze_10729)) {
                if (slt32(local_tid_10727 + offset_10745,
                          segred_group_sizze_10205) && ((local_tid_10727 -
                                                         squot32(local_tid_10727,
                                                                 wave_sizze_10729) *
                                                         wave_sizze_10729) &
                                                        (2 * offset_10745 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10738 = ((volatile __local
                                    float *) red_arr_mem_10733)[local_tid_10727 +
                                                                offset_10745];
                    }
                    // apply reduction operation
                    {
                        float res_10739 = x_10737 + x_10738;
                        
                        x_10737 = res_10739;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          float *) red_arr_mem_10733)[local_tid_10727] =
                            x_10737;
                    }
                }
                offset_10745 *= 2;
            }
            skip_waves_10746 = 1;
            while (slt32(skip_waves_10746, squot32(segred_group_sizze_10205 +
                                                   wave_sizze_10729 - 1,
                                                   wave_sizze_10729))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10745 = skip_waves_10746 * wave_sizze_10729;
                if (slt32(local_tid_10727 + offset_10745,
                          segred_group_sizze_10205) && ((local_tid_10727 -
                                                         squot32(local_tid_10727,
                                                                 wave_sizze_10729) *
                                                         wave_sizze_10729) ==
                                                        0 &&
                                                        (squot32(local_tid_10727,
                                                                 wave_sizze_10729) &
                                                         (2 * skip_waves_10746 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10738 = ((__local
                                    float *) red_arr_mem_10733)[local_tid_10727 +
                                                                offset_10745];
                    }
                    // apply reduction operation
                    {
                        float res_10739 = x_10737 + x_10738;
                        
                        x_10737 = res_10739;
                    }
                    // write result of operation
                    {
                        ((__local float *) red_arr_mem_10733)[local_tid_10727] =
                            x_10737;
                    }
                }
                skip_waves_10746 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10727 == 0) {
                    ((__global float *) mem_10232)[0] = x_10737;
                }
            }
        }
    }
}
__kernel void segred_nonseg_10223(__local volatile
                                  int64_t *sync_arr_mem_10759_backing_aligned_0,
                                  __local volatile
                                  int64_t *red_arr_mem_10761_backing_aligned_1,
                                  int32_t sizze_9996, double res_10011,
                                  double res_10013, int32_t num_groups_10218,
                                  __global unsigned char *x_mem_10227, __global
                                  unsigned char *x_mem_10228, __global
                                  unsigned char *mem_10232, __global
                                  unsigned char *counter_mem_10749, __global
                                  unsigned char *group_res_arr_mem_10751,
                                  int32_t num_threads_10753)
{
    const int32_t segred_group_sizze_10216 =
                  alpha_divergence_f64zisegred_group_sizze_10215;
    const int block_dim0 = 0;
    const int block_dim1 = 1;
    const int block_dim2 = 2;
    __local volatile char *restrict sync_arr_mem_10759_backing_0 =
                          (__local volatile
                           char *) sync_arr_mem_10759_backing_aligned_0;
    __local volatile char *restrict red_arr_mem_10761_backing_1 =
                          (__local volatile
                           char *) red_arr_mem_10761_backing_aligned_1;
    int32_t global_tid_10754;
    int32_t local_tid_10755;
    int32_t group_sizze_10758;
    int32_t wave_sizze_10757;
    int32_t group_tid_10756;
    
    global_tid_10754 = get_global_id(0);
    local_tid_10755 = get_local_id(0);
    group_sizze_10758 = get_local_size(0);
    wave_sizze_10757 = LOCKSTEP_WIDTH;
    group_tid_10756 = get_group_id(0);
    
    int32_t phys_tid_10223 = global_tid_10754;
    __local char *sync_arr_mem_10759;
    
    sync_arr_mem_10759 = (__local char *) sync_arr_mem_10759_backing_0;
    
    __local char *red_arr_mem_10761;
    
    red_arr_mem_10761 = (__local char *) red_arr_mem_10761_backing_1;
    
    int32_t dummy_10221 = 0;
    int32_t gtid_10222;
    
    gtid_10222 = 0;
    
    double x_acc_10763;
    int32_t chunk_sizze_10764 = smin32(squot32(sizze_9996 +
                                               segred_group_sizze_10216 *
                                               num_groups_10218 - 1,
                                               segred_group_sizze_10216 *
                                               num_groups_10218),
                                       squot32(sizze_9996 - phys_tid_10223 +
                                               num_threads_10753 - 1,
                                               num_threads_10753));
    double x_10016;
    double x_10017;
    
    // neutral-initialise the accumulators
    {
        x_acc_10763 = 0.0;
    }
    for (int32_t i_10768 = 0; i_10768 < chunk_sizze_10764; i_10768++) {
        gtid_10222 = phys_tid_10223 + num_threads_10753 * i_10768;
        // apply map function
        {
            double x_10019 = ((__global double *) x_mem_10227)[gtid_10222];
            double x_10020 = ((__global double *) x_mem_10228)[gtid_10222];
            double res_10021 = fpow64(x_10019, res_10011);
            double res_10022 = fpow64(x_10020, res_10013);
            double res_10023 = res_10021 * res_10022;
            
            // save map-out results
            { }
            // load accumulator
            {
                x_10016 = x_acc_10763;
            }
            // load new values
            {
                x_10017 = res_10023;
            }
            // apply reduction operator
            {
                double res_10018 = x_10016 + x_10017;
                
                // store in accumulator
                {
                    x_acc_10763 = res_10018;
                }
            }
        }
    }
    // to reduce current chunk, first store our result in memory
    {
        x_10016 = x_acc_10763;
        ((__local double *) red_arr_mem_10761)[local_tid_10755] = x_10016;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    
    int32_t offset_10769;
    int32_t skip_waves_10770;
    double x_10765;
    double x_10766;
    
    offset_10769 = 0;
    // participating threads read initial accumulator
    {
        if (slt32(local_tid_10755, segred_group_sizze_10216)) {
            x_10765 = ((__local double *) red_arr_mem_10761)[local_tid_10755 +
                                                             offset_10769];
        }
    }
    offset_10769 = 1;
    while (slt32(offset_10769, wave_sizze_10757)) {
        if (slt32(local_tid_10755 + offset_10769, segred_group_sizze_10216) &&
            ((local_tid_10755 - squot32(local_tid_10755, wave_sizze_10757) *
              wave_sizze_10757) & (2 * offset_10769 - 1)) == 0) {
            // read array element
            {
                x_10766 = ((volatile __local
                            double *) red_arr_mem_10761)[local_tid_10755 +
                                                         offset_10769];
            }
            // apply reduction operation
            {
                double res_10767 = x_10765 + x_10766;
                
                x_10765 = res_10767;
            }
            // write result of operation
            {
                ((volatile __local
                  double *) red_arr_mem_10761)[local_tid_10755] = x_10765;
            }
        }
        offset_10769 *= 2;
    }
    skip_waves_10770 = 1;
    while (slt32(skip_waves_10770, squot32(segred_group_sizze_10216 +
                                           wave_sizze_10757 - 1,
                                           wave_sizze_10757))) {
        barrier(CLK_LOCAL_MEM_FENCE);
        offset_10769 = skip_waves_10770 * wave_sizze_10757;
        if (slt32(local_tid_10755 + offset_10769, segred_group_sizze_10216) &&
            ((local_tid_10755 - squot32(local_tid_10755, wave_sizze_10757) *
              wave_sizze_10757) == 0 && (squot32(local_tid_10755,
                                                 wave_sizze_10757) & (2 *
                                                                      skip_waves_10770 -
                                                                      1)) ==
             0)) {
            // read array element
            {
                x_10766 = ((__local
                            double *) red_arr_mem_10761)[local_tid_10755 +
                                                         offset_10769];
            }
            // apply reduction operation
            {
                double res_10767 = x_10765 + x_10766;
                
                x_10765 = res_10767;
            }
            // write result of operation
            {
                ((__local double *) red_arr_mem_10761)[local_tid_10755] =
                    x_10765;
            }
        }
        skip_waves_10770 *= 2;
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    // first thread saves the result in accumulator
    {
        if (local_tid_10755 == 0) {
            x_acc_10763 = x_10765;
        }
    }
    
    int32_t old_counter_10771;
    
    // first thread in group saves group result to global memory
    {
        if (local_tid_10755 == 0) {
            ((__global double *) group_res_arr_mem_10751)[group_tid_10756 *
                                                          segred_group_sizze_10216] =
                x_acc_10763;
            mem_fence_global();
            old_counter_10771 = atomic_add(&((volatile __global
                                              int *) counter_mem_10749)[0],
                                           (int) 1);
            ((__local bool *) sync_arr_mem_10759)[0] = old_counter_10771 ==
                num_groups_10218 - 1;
        }
    }
    barrier(CLK_LOCAL_MEM_FENCE);
    barrier(CLK_GLOBAL_MEM_FENCE);
    
    bool is_last_group_10772 = ((__local bool *) sync_arr_mem_10759)[0];
    
    if (is_last_group_10772) {
        if (local_tid_10755 == 0) {
            old_counter_10771 = atomic_add(&((volatile __global
                                              int *) counter_mem_10749)[0],
                                           (int) (0 - num_groups_10218));
        }
        // read in the per-group-results
        {
            if (slt32(local_tid_10755, num_groups_10218)) {
                x_10016 = ((__global
                            double *) group_res_arr_mem_10751)[local_tid_10755 *
                                                               segred_group_sizze_10216];
            } else {
                x_10016 = 0.0;
            }
            ((__local double *) red_arr_mem_10761)[local_tid_10755] = x_10016;
        }
        barrier(CLK_LOCAL_MEM_FENCE);
        // reduce the per-group results
        {
            int32_t offset_10773;
            int32_t skip_waves_10774;
            double x_10765;
            double x_10766;
            
            offset_10773 = 0;
            // participating threads read initial accumulator
            {
                if (slt32(local_tid_10755, segred_group_sizze_10216)) {
                    x_10765 = ((__local
                                double *) red_arr_mem_10761)[local_tid_10755 +
                                                             offset_10773];
                }
            }
            offset_10773 = 1;
            while (slt32(offset_10773, wave_sizze_10757)) {
                if (slt32(local_tid_10755 + offset_10773,
                          segred_group_sizze_10216) && ((local_tid_10755 -
                                                         squot32(local_tid_10755,
                                                                 wave_sizze_10757) *
                                                         wave_sizze_10757) &
                                                        (2 * offset_10773 -
                                                         1)) == 0) {
                    // read array element
                    {
                        x_10766 = ((volatile __local
                                    double *) red_arr_mem_10761)[local_tid_10755 +
                                                                 offset_10773];
                    }
                    // apply reduction operation
                    {
                        double res_10767 = x_10765 + x_10766;
                        
                        x_10765 = res_10767;
                    }
                    // write result of operation
                    {
                        ((volatile __local
                          double *) red_arr_mem_10761)[local_tid_10755] =
                            x_10765;
                    }
                }
                offset_10773 *= 2;
            }
            skip_waves_10774 = 1;
            while (slt32(skip_waves_10774, squot32(segred_group_sizze_10216 +
                                                   wave_sizze_10757 - 1,
                                                   wave_sizze_10757))) {
                barrier(CLK_LOCAL_MEM_FENCE);
                offset_10773 = skip_waves_10774 * wave_sizze_10757;
                if (slt32(local_tid_10755 + offset_10773,
                          segred_group_sizze_10216) && ((local_tid_10755 -
                                                         squot32(local_tid_10755,
                                                                 wave_sizze_10757) *
                                                         wave_sizze_10757) ==
                                                        0 &&
                                                        (squot32(local_tid_10755,
                                                                 wave_sizze_10757) &
                                                         (2 * skip_waves_10774 -
                                                          1)) == 0)) {
                    // read array element
                    {
                        x_10766 = ((__local
                                    double *) red_arr_mem_10761)[local_tid_10755 +
                                                                 offset_10773];
                    }
                    // apply reduction operation
                    {
                        double res_10767 = x_10765 + x_10766;
                        
                        x_10765 = res_10767;
                    }
                    // write result of operation
                    {
                        ((__local
                          double *) red_arr_mem_10761)[local_tid_10755] =
                            x_10765;
                    }
                }
                skip_waves_10774 *= 2;
            }
            // and back to memory with the final result
            {
                if (local_tid_10755 == 0) {
                    ((__global double *) mem_10232)[0] = x_10765;
                }
            }
        }
    }
}
"""
# Start of values.py.

# Hacky parser/reader/writer for values written in Futhark syntax.
# Used for reading stdin when compiling standalone programs with the
# Python code generator.

import numpy as np
import string
import struct
import sys

class ReaderInput:
    def __init__(self, f):
        self.f = f
        self.lookahead_buffer = []

    def get_char(self):
        if len(self.lookahead_buffer) == 0:
            return self.f.read(1)
        else:
            c = self.lookahead_buffer[0]
            self.lookahead_buffer = self.lookahead_buffer[1:]
            return c

    def unget_char(self, c):
        self.lookahead_buffer = [c] + self.lookahead_buffer

    def get_chars(self, n):
        n1 = min(n, len(self.lookahead_buffer))
        s = b''.join(self.lookahead_buffer[:n1])
        self.lookahead_buffer = self.lookahead_buffer[n1:]
        n2 = n - n1
        if n2 > 0:
            s += self.f.read(n2)
        return s

    def peek_char(self):
        c = self.get_char()
        if c:
            self.unget_char(c)
        return c

def skip_spaces(f):
    c = f.get_char()
    while c != None:
        if c.isspace():
            c = f.get_char()
        elif c == b'-':
          # May be line comment.
          if f.peek_char() == b'-':
            # Yes, line comment. Skip to end of line.
            while (c != b'\n' and c != None):
              c = f.get_char()
          else:
            break
        else:
          break
    if c:
        f.unget_char(c)

def parse_specific_char(f, expected):
    got = f.get_char()
    if got != expected:
        f.unget_char(got)
        raise ValueError
    return True

def parse_specific_string(f, s):
    # This funky mess is intended, and is caused by the fact that if `type(b) ==
    # bytes` then `type(b[0]) == int`, but we need to match each element with a
    # `bytes`, so therefore we make each character an array element
    b = s.encode('utf8')
    bs = [b[i:i+1] for i in range(len(b))]
    read = []
    try:
        for c in bs:
            parse_specific_char(f, c)
            read.append(c)
        return True
    except ValueError:
        for c in read[::-1]:
            f.unget_char(c)
        raise

def optional(p, *args):
    try:
        return p(*args)
    except ValueError:
        return None

def optional_specific_string(f, s):
    c = f.peek_char()
    # This funky mess is intended, and is caused by the fact that if `type(b) ==
    # bytes` then `type(b[0]) == int`, but we need to match each element with a
    # `bytes`, so therefore we make each character an array element
    b = s.encode('utf8')
    bs = [b[i:i+1] for i in range(len(b))]
    if c == bs[0]:
        return parse_specific_string(f, s)
    else:
        return False

def sepBy(p, sep, *args):
    elems = []
    x = optional(p, *args)
    if x != None:
        elems += [x]
        while optional(sep, *args) != None:
            x = p(*args)
            elems += [x]
    return elems

# Assumes '0x' has already been read
def parse_hex_int(f):
    s = b''
    c = f.get_char()
    while c != None:
        if c in b'01234556789ABCDEFabcdef':
            s += c
            c = f.get_char()
        elif c == b'_':
            c = f.get_char() # skip _
        else:
            f.unget_char(c)
            break
    return str(int(s, 16)).encode('utf8') # ugh

def parse_int(f):
    s = b''
    c = f.get_char()
    if c == b'0' and f.peek_char() in b'xX':
        c = f.get_char() # skip X
        return parse_hex_int(f)
    else:
        while c != None:
            if c.isdigit():
                s += c
                c = f.get_char()
            elif c == b'_':
                c = f.get_char() # skip _
            else:
                f.unget_char(c)
                break
        if len(s) == 0:
            raise ValueError
        return s

def parse_int_signed(f):
    s = b''
    c = f.get_char()

    if c == b'-' and f.peek_char().isdigit():
      return c + parse_int(f)
    else:
      if c != b'+':
          f.unget_char(c)
      return parse_int(f)

def read_str_comma(f):
    skip_spaces(f)
    parse_specific_char(f, b',')
    return b','

def read_str_int(f, s):
    skip_spaces(f)
    x = int(parse_int_signed(f))
    optional_specific_string(f, s)
    return x

def read_str_uint(f, s):
    skip_spaces(f)
    x = int(parse_int(f))
    optional_specific_string(f, s)
    return x

def read_str_i8(f):
    return np.int8(read_str_int(f, 'i8'))
def read_str_i16(f):
    return np.int16(read_str_int(f, 'i16'))
def read_str_i32(f):
    return np.int32(read_str_int(f, 'i32'))
def read_str_i64(f):
    return np.int64(read_str_int(f, 'i64'))

def read_str_u8(f):
    return np.uint8(read_str_int(f, 'u8'))
def read_str_u16(f):
    return np.uint16(read_str_int(f, 'u16'))
def read_str_u32(f):
    return np.uint32(read_str_int(f, 'u32'))
def read_str_u64(f):
    return np.uint64(read_str_int(f, 'u64'))

def read_char(f):
    skip_spaces(f)
    parse_specific_char(f, b'\'')
    c = f.get_char()
    parse_specific_char(f, b'\'')
    return c

def read_str_hex_float(f, sign):
    int_part = parse_hex_int(f)
    parse_specific_char(f, b'.')
    frac_part = parse_hex_int(f)
    parse_specific_char(f, b'p')
    exponent = parse_int(f)

    int_val = int(int_part, 16)
    frac_val = float(int(frac_part, 16)) / (16 ** len(frac_part))
    exp_val = int(exponent)

    total_val = (int_val + frac_val) * (2.0 ** exp_val)
    if sign == b'-':
        total_val = -1 * total_val

    return float(total_val)


def read_str_decimal(f):
    skip_spaces(f)
    c = f.get_char()
    if (c == b'-'):
      sign = b'-'
    else:
      f.unget_char(c)
      sign = b''

    # Check for hexadecimal float
    c = f.get_char()
    if (c == '0' and (f.peek_char() in ['x', 'X'])):
        f.get_char()
        return read_str_hex_float(f, sign)
    else:
        f.unget_char(c)

    bef = optional(parse_int, f)
    if bef == None:
        bef = b'0'
        parse_specific_char(f, b'.')
        aft = parse_int(f)
    elif optional(parse_specific_char, f, b'.'):
        aft = parse_int(f)
    else:
        aft = b'0'
    if (optional(parse_specific_char, f, b'E') or
        optional(parse_specific_char, f, b'e')):
        expt = parse_int_signed(f)
    else:
        expt = b'0'
    return float(sign + bef + b'.' + aft + b'E' + expt)

def read_str_f32(f):
    skip_spaces(f)
    try:
        parse_specific_string(f, 'f32.nan')
        return np.float32(np.nan)
    except ValueError:
        try:
            parse_specific_string(f, 'f32.inf')
            return np.float32(np.inf)
        except ValueError:
            try:
               parse_specific_string(f, '-f32.inf')
               return np.float32(-np.inf)
            except ValueError:
               x = read_str_decimal(f)
               optional_specific_string(f, 'f32')
               return x

def read_str_f64(f):
    skip_spaces(f)
    try:
        parse_specific_string(f, 'f64.nan')
        return np.float64(np.nan)
    except ValueError:
        try:
            parse_specific_string(f, 'f64.inf')
            return np.float64(np.inf)
        except ValueError:
            try:
               parse_specific_string(f, '-f64.inf')
               return np.float64(-np.inf)
            except ValueError:
               x = read_str_decimal(f)
               optional_specific_string(f, 'f64')
               return x

def read_str_bool(f):
    skip_spaces(f)
    if f.peek_char() == b't':
        parse_specific_string(f, 'true')
        return True
    elif f.peek_char() == b'f':
        parse_specific_string(f, 'false')
        return False
    else:
        raise ValueError

def read_str_empty_array(f, type_name, rank):
    parse_specific_string(f, 'empty')
    parse_specific_char(f, b'(')
    dims = []
    for i in range(rank):
        parse_specific_string(f, '[')
        dims += [int(parse_int(f))]
        parse_specific_string(f, ']')
    if np.product(dims) != 0:
        raise ValueError
    parse_specific_string(f, type_name)
    parse_specific_char(f, b')')

    return tuple(dims)

def read_str_array_elems(f, elem_reader, type_name, rank):
    skip_spaces(f)
    try:
        parse_specific_char(f, b'[')
    except ValueError:
        return read_str_empty_array(f, type_name, rank)
    else:
        xs = sepBy(elem_reader, read_str_comma, f)
        skip_spaces(f)
        parse_specific_char(f, b']')
        return xs

def read_str_array_helper(f, elem_reader, type_name, rank):
    def nested_row_reader(_):
        return read_str_array_helper(f, elem_reader, type_name, rank-1)
    if rank == 1:
        row_reader = elem_reader
    else:
        row_reader = nested_row_reader
    return read_str_array_elems(f, row_reader, type_name, rank)

def expected_array_dims(l, rank):
  if rank > 1:
      n = len(l)
      if n == 0:
          elem = []
      else:
          elem = l[0]
      return [n] + expected_array_dims(elem, rank-1)
  else:
      return [len(l)]

def verify_array_dims(l, dims):
    if dims[0] != len(l):
        raise ValueError
    if len(dims) > 1:
        for x in l:
            verify_array_dims(x, dims[1:])

def read_str_array(f, elem_reader, type_name, rank, bt):
    elems = read_str_array_helper(f, elem_reader, type_name, rank)
    if type(elems) == tuple:
        # Empty array
        return np.empty(elems, dtype=bt)
    else:
        dims = expected_array_dims(elems, rank)
        verify_array_dims(elems, dims)
        return np.array(elems, dtype=bt)

################################################################################

READ_BINARY_VERSION = 2

# struct format specified at
# https://docs.python.org/2/library/struct.html#format-characters

def mk_bin_scalar_reader(t):
    def bin_reader(f):
        fmt = FUTHARK_PRIMTYPES[t]['bin_format']
        size = FUTHARK_PRIMTYPES[t]['size']
        return struct.unpack('<' + fmt, f.get_chars(size))[0]
    return bin_reader

read_bin_i8 = mk_bin_scalar_reader('i8')
read_bin_i16 = mk_bin_scalar_reader('i16')
read_bin_i32 = mk_bin_scalar_reader('i32')
read_bin_i64 = mk_bin_scalar_reader('i64')

read_bin_u8 = mk_bin_scalar_reader('u8')
read_bin_u16 = mk_bin_scalar_reader('u16')
read_bin_u32 = mk_bin_scalar_reader('u32')
read_bin_u64 = mk_bin_scalar_reader('u64')

read_bin_f32 = mk_bin_scalar_reader('f32')
read_bin_f64 = mk_bin_scalar_reader('f64')

read_bin_bool = mk_bin_scalar_reader('bool')

def read_is_binary(f):
    skip_spaces(f)
    c = f.get_char()
    if c == b'b':
        bin_version = read_bin_u8(f)
        if bin_version != READ_BINARY_VERSION:
            panic(1, "binary-input: File uses version %i, but I only understand version %i.\n",
                  bin_version, READ_BINARY_VERSION)
        return True
    else:
        f.unget_char(c)
        return False

FUTHARK_PRIMTYPES = {
    'i8':  {'binname' : b"  i8",
            'size' : 1,
            'bin_reader': read_bin_i8,
            'str_reader': read_str_i8,
            'bin_format': 'b',
            'numpy_type': np.int8 },

    'i16': {'binname' : b" i16",
            'size' : 2,
            'bin_reader': read_bin_i16,
            'str_reader': read_str_i16,
            'bin_format': 'h',
            'numpy_type': np.int16 },

    'i32': {'binname' : b" i32",
            'size' : 4,
            'bin_reader': read_bin_i32,
            'str_reader': read_str_i32,
            'bin_format': 'i',
            'numpy_type': np.int32 },

    'i64': {'binname' : b" i64",
            'size' : 8,
            'bin_reader': read_bin_i64,
            'str_reader': read_str_i64,
            'bin_format': 'q',
            'numpy_type': np.int64},

    'u8':  {'binname' : b"  u8",
            'size' : 1,
            'bin_reader': read_bin_u8,
            'str_reader': read_str_u8,
            'bin_format': 'B',
            'numpy_type': np.uint8 },

    'u16': {'binname' : b" u16",
            'size' : 2,
            'bin_reader': read_bin_u16,
            'str_reader': read_str_u16,
            'bin_format': 'H',
            'numpy_type': np.uint16 },

    'u32': {'binname' : b" u32",
            'size' : 4,
            'bin_reader': read_bin_u32,
            'str_reader': read_str_u32,
            'bin_format': 'I',
            'numpy_type': np.uint32 },

    'u64': {'binname' : b" u64",
            'size' : 8,
            'bin_reader': read_bin_u64,
            'str_reader': read_str_u64,
            'bin_format': 'Q',
            'numpy_type': np.uint64 },

    'f32': {'binname' : b" f32",
            'size' : 4,
            'bin_reader': read_bin_f32,
            'str_reader': read_str_f32,
            'bin_format': 'f',
            'numpy_type': np.float32 },

    'f64': {'binname' : b" f64",
            'size' : 8,
            'bin_reader': read_bin_f64,
            'str_reader': read_str_f64,
            'bin_format': 'd',
            'numpy_type': np.float64 },

    'bool': {'binname' : b"bool",
             'size' : 1,
             'bin_reader': read_bin_bool,
             'str_reader': read_str_bool,
             'bin_format': 'b',
             'numpy_type': np.bool }
}

def read_bin_read_type(f):
    read_binname = f.get_chars(4)

    for (k,v) in FUTHARK_PRIMTYPES.items():
        if v['binname'] == read_binname:
            return k
    panic(1, "binary-input: Did not recognize the type '%s'.\n", read_binname)

def numpy_type_to_type_name(t):
    for (k,v) in FUTHARK_PRIMTYPES.items():
        if v['numpy_type'] == t:
            return k
    raise Exception('Unknown Numpy type: {}'.format(t))

def read_bin_ensure_scalar(f, expected_type):
  dims = read_bin_i8(f)

  if dims != 0:
      panic(1, "binary-input: Expected scalar (0 dimensions), but got array with %i dimensions.\n", dims)

  bin_type = read_bin_read_type(f)
  if bin_type != expected_type:
      panic(1, "binary-input: Expected scalar of type %s but got scalar of type %s.\n",
            expected_type, bin_type)

# ------------------------------------------------------------------------------
# General interface for reading Primitive Futhark Values
# ------------------------------------------------------------------------------

def read_scalar(f, ty):
    if read_is_binary(f):
        read_bin_ensure_scalar(f, ty)
        return FUTHARK_PRIMTYPES[ty]['bin_reader'](f)
    return FUTHARK_PRIMTYPES[ty]['str_reader'](f)

def read_array(f, expected_type, rank):
    if not read_is_binary(f):
        str_reader = FUTHARK_PRIMTYPES[expected_type]['str_reader']
        return read_str_array(f, str_reader, expected_type, rank,
                              FUTHARK_PRIMTYPES[expected_type]['numpy_type'])

    bin_rank = read_bin_u8(f)

    if bin_rank != rank:
        panic(1, "binary-input: Expected %i dimensions, but got array with %i dimensions.\n",
              rank, bin_rank)

    bin_type_enum = read_bin_read_type(f)
    if expected_type != bin_type_enum:
        panic(1, "binary-input: Expected %iD-array with element type '%s' but got %iD-array with element type '%s'.\n",
              rank, expected_type, bin_rank, bin_type_enum)

    shape = []
    elem_count = 1
    for i in range(rank):
        bin_size = read_bin_u64(f)
        elem_count *= bin_size
        shape.append(bin_size)

    bin_fmt = FUTHARK_PRIMTYPES[bin_type_enum]['bin_format']

    # We first read the expected number of types into a bytestring,
    # then use np.fromstring.  This is because np.fromfile does not
    # work on things that are insufficiently file-like, like a network
    # stream.
    bytes = f.get_chars(elem_count * FUTHARK_PRIMTYPES[expected_type]['size'])
    arr = np.fromstring(bytes, dtype=FUTHARK_PRIMTYPES[bin_type_enum]['numpy_type'])
    arr.shape = shape

    return arr

if sys.version_info >= (3,0):
    input_reader = ReaderInput(sys.stdin.buffer)
else:
    input_reader = ReaderInput(sys.stdin)

import re

def read_value(type_desc, reader=input_reader):
    """Read a value of the given type.  The type is a string
representation of the Futhark type."""
    m = re.match(r'((?:\[\])*)([a-z0-9]+)$', type_desc)
    if m:
        dims = int(len(m.group(1))/2)
        basetype = m.group(2)
        assert basetype in FUTHARK_PRIMTYPES, "Unknown type: {}".format(type_desc)
        if dims > 0:
            return read_array(reader, basetype, dims)
        else:
            return read_scalar(reader, basetype)
        return (dims, basetype)

def write_value_text(v, out=sys.stdout):
    if type(v) == np.uint8:
        out.write("%uu8" % v)
    elif type(v) == np.uint16:
        out.write("%uu16" % v)
    elif type(v) == np.uint32:
        out.write("%uu32" % v)
    elif type(v) == np.uint64:
        out.write("%uu64" % v)
    elif type(v) == np.int8:
        out.write("%di8" % v)
    elif type(v) == np.int16:
        out.write("%di16" % v)
    elif type(v) == np.int32:
        out.write("%di32" % v)
    elif type(v) == np.int64:
        out.write("%di64" % v)
    elif type(v) in [np.bool, np.bool_]:
        if v:
            out.write("true")
        else:
            out.write("false")
    elif type(v) == np.float32:
        if np.isnan(v):
            out.write('f32.nan')
        elif np.isinf(v):
            if v >= 0:
                out.write('f32.inf')
            else:
                out.write('-f32.inf')
        else:
            out.write("%.6ff32" % v)
    elif type(v) == np.float64:
        if np.isnan(v):
            out.write('f64.nan')
        elif np.isinf(v):
            if v >= 0:
                out.write('f64.inf')
            else:
                out.write('-f64.inf')
        else:
            out.write("%.6ff64" % v)
    elif type(v) == np.ndarray:
        if np.product(v.shape) == 0:
            tname = numpy_type_to_type_name(v.dtype)
            out.write('empty({}{})'.format(''.join(['[{}]'.format(d)
                                                    for d in v.shape]), tname))
        else:
            first = True
            out.write('[')
            for x in v:
                if not first: out.write(', ')
                first = False
                write_value(x, out=out)
            out.write(']')
    else:
        raise Exception("Cannot print value of type {}: {}".format(type(v), v))

type_strs = { np.dtype('int8'): b'  i8',
              np.dtype('int16'): b' i16',
              np.dtype('int32'): b' i32',
              np.dtype('int64'): b' i64',
              np.dtype('uint8'): b'  u8',
              np.dtype('uint16'): b' u16',
              np.dtype('uint32'): b' u32',
              np.dtype('uint64'): b' u64',
              np.dtype('float32'): b' f32',
              np.dtype('float64'): b' f64',
              np.dtype('bool'): b'bool'}

def construct_binary_value(v):
    t = v.dtype
    shape = v.shape

    elems = 1
    for d in shape:
        elems *= d

    num_bytes = 1 + 1 + 1 + 4 + len(shape) * 8 + elems * t.itemsize
    bytes = bytearray(num_bytes)
    bytes[0] = np.int8(ord('b'))
    bytes[1] = 2
    bytes[2] = np.int8(len(shape))
    bytes[3:7] = type_strs[t]

    for i in range(len(shape)):
        bytes[7+i*8:7+(i+1)*8] = np.int64(shape[i]).tostring()

    bytes[7+len(shape)*8:] = np.ascontiguousarray(v).tostring()

    return bytes

def write_value_binary(v, out=sys.stdout):
    if sys.version_info >= (3,0):
        out = out.buffer
    out.write(construct_binary_value(v))

def write_value(v, out=sys.stdout, binary=False):
    if binary:
        return write_value_binary(v, out=out)
    else:
        return write_value_text(v, out=out)

# End of values.py.
# Start of memory.py.

import ctypes as ct

def addressOffset(x, offset, bt):
  return ct.cast(ct.addressof(x.contents)+int(offset), ct.POINTER(bt))

def allocateMem(size):
  return ct.cast((ct.c_byte * max(0,size))(), ct.POINTER(ct.c_byte))

# Copy an array if its is not-None.  This is important for treating
# Numpy arrays as flat memory, but has some overhead.
def normaliseArray(x):
  if (x.base is x) or (x.base is None):
    return x
  else:
    return x.copy()

def unwrapArray(x):
  return normaliseArray(x).ctypes.data_as(ct.POINTER(ct.c_byte))

def createArray(x, shape):
  # HACK: np.ctypeslib.as_array may fail if the shape contains zeroes,
  # for some reason.
  if any(map(lambda x: x == 0, shape)):
      return np.ndarray(shape, dtype=x._type_)
  else:
      return np.ctypeslib.as_array(x, shape=shape)

def indexArray(x, offset, bt, nptype):
  return nptype(addressOffset(x, offset*ct.sizeof(bt), bt)[0])

def writeScalarArray(x, offset, v):
  ct.memmove(ct.addressof(x.contents)+int(offset)*ct.sizeof(v), ct.addressof(v), ct.sizeof(v))

# An opaque Futhark value.
class opaque(object):
  def __init__(self, desc, *payload):
    self.data = payload
    self.desc = desc

  def __repr__(self):
    return "<opaque Futhark value of type {}>".format(self.desc)

# End of memory.py.
# Start of panic.py.

def panic(exitcode, fmt, *args):
    sys.stderr.write('%s: ' % sys.argv[0])
    sys.stderr.write(fmt % args)
    sys.exit(exitcode)

# End of panic.py.
# Start of tuning.py

def read_tuning_file(kvs, f):
    for line in f.read().splitlines():
        size, value = line.split('=')
        kvs[size] = int(value)
    return kvs

# End of tuning.py.
# Start of scalar.py.

import numpy as np
import math
import struct

def signed(x):
  if type(x) == np.uint8:
    return np.int8(x)
  elif type(x) == np.uint16:
    return np.int16(x)
  elif type(x) == np.uint32:
    return np.int32(x)
  else:
    return np.int64(x)

def unsigned(x):
  if type(x) == np.int8:
    return np.uint8(x)
  elif type(x) == np.int16:
    return np.uint16(x)
  elif type(x) == np.int32:
    return np.uint32(x)
  else:
    return np.uint64(x)

def shlN(x,y):
  return x << y

def ashrN(x,y):
  return x >> y

def sdivN(x,y):
  return x // y

def smodN(x,y):
  return x % y

def udivN(x,y):
  return signed(unsigned(x) // unsigned(y))

def umodN(x,y):
  return signed(unsigned(x) % unsigned(y))

def squotN(x,y):
  return np.floor_divide(np.abs(x), np.abs(y)) * np.sign(x) * np.sign(y)

def sremN(x,y):
  return np.remainder(np.abs(x), np.abs(y)) * np.sign(x)

def sminN(x,y):
  return min(x,y)

def smaxN(x,y):
  return max(x,y)

def uminN(x,y):
  return signed(min(unsigned(x),unsigned(y)))

def umaxN(x,y):
  return signed(max(unsigned(x),unsigned(y)))

def fminN(x,y):
  return min(x,y)

def fmaxN(x,y):
  return max(x,y)

def powN(x,y):
  return x ** y

def fpowN(x,y):
  return x ** y

def sleN(x,y):
  return x <= y

def sltN(x,y):
  return x < y

def uleN(x,y):
  return unsigned(x) <= unsigned(y)

def ultN(x,y):
  return unsigned(x) < unsigned(y)

def lshr8(x,y):
  return np.int8(np.uint8(x) >> np.uint8(y))

def lshr16(x,y):
  return np.int16(np.uint16(x) >> np.uint16(y))

def lshr32(x,y):
  return np.int32(np.uint32(x) >> np.uint32(y))

def lshr64(x,y):
  return np.int64(np.uint64(x) >> np.uint64(y))

def sext_T_i8(x):
  return np.int8(x)

def sext_T_i16(x):
  return np.int16(x)

def sext_T_i32(x):
  return np.int32(x)

def sext_T_i64(x):
  return np.int64(x)

def itob_T_bool(x):
  return np.bool(x)

def btoi_bool_i8(x):
  return np.int8(x)

def btoi_bool_i16(x):
  return np.int8(x)

def btoi_bool_i32(x):
  return np.int8(x)

def btoi_bool_i64(x):
  return np.int8(x)

def zext_i8_i8(x):
  return np.int8(np.uint8(x))

def zext_i8_i16(x):
  return np.int16(np.uint8(x))

def zext_i8_i32(x):
  return np.int32(np.uint8(x))

def zext_i8_i64(x):
  return np.int64(np.uint8(x))

def zext_i16_i8(x):
  return np.int8(np.uint16(x))

def zext_i16_i16(x):
  return np.int16(np.uint16(x))

def zext_i16_i32(x):
  return np.int32(np.uint16(x))

def zext_i16_i64(x):
  return np.int64(np.uint16(x))

def zext_i32_i8(x):
  return np.int8(np.uint32(x))

def zext_i32_i16(x):
  return np.int16(np.uint32(x))

def zext_i32_i32(x):
  return np.int32(np.uint32(x))

def zext_i32_i64(x):
  return np.int64(np.uint32(x))

def zext_i64_i8(x):
  return np.int8(np.uint64(x))

def zext_i64_i16(x):
  return np.int16(np.uint64(x))

def zext_i64_i32(x):
  return np.int32(np.uint64(x))

def zext_i64_i64(x):
  return np.int64(np.uint64(x))

shl8 = shl16 = shl32 = shl64 = shlN
ashr8 = ashr16 = ashr32 = ashr64 = ashrN
sdiv8 = sdiv16 = sdiv32 = sdiv64 = sdivN
smod8 = smod16 = smod32 = smod64 = smodN
udiv8 = udiv16 = udiv32 = udiv64 = udivN
umod8 = umod16 = umod32 = umod64 = umodN
squot8 = squot16 = squot32 = squot64 = squotN
srem8 = srem16 = srem32 = srem64 = sremN
smax8 = smax16 = smax32 = smax64 = smaxN
smin8 = smin16 = smin32 = smin64 = sminN
umax8 = umax16 = umax32 = umax64 = umaxN
umin8 = umin16 = umin32 = umin64 = uminN
pow8 = pow16 = pow32 = pow64 = powN
fpow32 = fpow64 = fpowN
fmax32 = fmax64 = fmaxN
fmin32 = fmin64 = fminN
sle8 = sle16 = sle32 = sle64 = sleN
slt8 = slt16 = slt32 = slt64 = sltN
ule8 = ule16 = ule32 = ule64 = uleN
ult8 = ult16 = ult32 = ult64 = ultN
sext_i8_i8 = sext_i16_i8 = sext_i32_i8 = sext_i64_i8 = sext_T_i8
sext_i8_i16 = sext_i16_i16 = sext_i32_i16 = sext_i64_i16 = sext_T_i16
sext_i8_i32 = sext_i16_i32 = sext_i32_i32 = sext_i64_i32 = sext_T_i32
sext_i8_i64 = sext_i16_i64 = sext_i32_i64 = sext_i64_i64 = sext_T_i64
itob_i8_bool = itob_i16_bool = itob_i32_bool = itob_i64_bool = itob_T_bool

def clz_T(x):
  n = np.int32(0)
  bits = x.itemsize * 8
  for i in range(bits):
    if x < 0:
      break
    n += 1
    x <<= np.int8(1)
  return n

def popc_T(x):
  c = np.int32(0)
  while x != 0:
    x &= x - np.int8(1)
    c += np.int8(1)
  return c

futhark_popc8 = futhark_popc16 = futhark_popc32 = futhark_popc64 = popc_T
futhark_clzz8 = futhark_clzz16 = futhark_clzz32 = futhark_clzz64 = clz_T

def ssignum(x):
  return np.sign(x)

def usignum(x):
  if x < 0:
    return ssignum(-x)
  else:
    return ssignum(x)

def sitofp_T_f32(x):
  return np.float32(x)
sitofp_i8_f32 = sitofp_i16_f32 = sitofp_i32_f32 = sitofp_i64_f32 = sitofp_T_f32

def sitofp_T_f64(x):
  return np.float64(x)
sitofp_i8_f64 = sitofp_i16_f64 = sitofp_i32_f64 = sitofp_i64_f64 = sitofp_T_f64

def uitofp_T_f32(x):
  return np.float32(unsigned(x))
uitofp_i8_f32 = uitofp_i16_f32 = uitofp_i32_f32 = uitofp_i64_f32 = uitofp_T_f32

def uitofp_T_f64(x):
  return np.float64(unsigned(x))
uitofp_i8_f64 = uitofp_i16_f64 = uitofp_i32_f64 = uitofp_i64_f64 = uitofp_T_f64

def fptosi_T_i8(x):
  return np.int8(np.trunc(x))
fptosi_f32_i8 = fptosi_f64_i8 = fptosi_T_i8

def fptosi_T_i16(x):
  return np.int16(np.trunc(x))
fptosi_f32_i16 = fptosi_f64_i16 = fptosi_T_i16

def fptosi_T_i32(x):
  return np.int32(np.trunc(x))
fptosi_f32_i32 = fptosi_f64_i32 = fptosi_T_i32

def fptosi_T_i64(x):
  return np.int64(np.trunc(x))
fptosi_f32_i64 = fptosi_f64_i64 = fptosi_T_i64

def fptoui_T_i8(x):
  return np.uint8(np.trunc(x))
fptoui_f32_i8 = fptoui_f64_i8 = fptoui_T_i8

def fptoui_T_i16(x):
  return np.uint16(np.trunc(x))
fptoui_f32_i16 = fptoui_f64_i16 = fptoui_T_i16

def fptoui_T_i32(x):
  return np.uint32(np.trunc(x))
fptoui_f32_i32 = fptoui_f64_i32 = fptoui_T_i32

def fptoui_T_i64(x):
  return np.uint64(np.trunc(x))
fptoui_f32_i64 = fptoui_f64_i64 = fptoui_T_i64

def fpconv_f32_f64(x):
  return np.float64(x)

def fpconv_f64_f32(x):
  return np.float32(x)

def futhark_log64(x):
  return np.float64(np.log(x))

def futhark_log2_64(x):
  return np.float64(np.log2(x))

def futhark_log10_64(x):
  return np.float64(np.log10(x))

def futhark_sqrt64(x):
  return np.sqrt(x)

def futhark_exp64(x):
  return np.exp(x)

def futhark_cos64(x):
  return np.cos(x)

def futhark_sin64(x):
  return np.sin(x)

def futhark_tan64(x):
  return np.tan(x)

def futhark_acos64(x):
  return np.arccos(x)

def futhark_asin64(x):
  return np.arcsin(x)

def futhark_atan64(x):
  return np.arctan(x)

def futhark_atan2_64(x, y):
  return np.arctan2(x, y)

def futhark_gamma64(x):
  return np.float64(math.gamma(x))

def futhark_lgamma64(x):
  return np.float64(math.lgamma(x))

def futhark_round64(x):
  return np.round(x)

def futhark_ceil64(x):
  return np.ceil(x)

def futhark_floor64(x):
  return np.floor(x)

def futhark_isnan64(x):
  return np.isnan(x)

def futhark_isinf64(x):
  return np.isinf(x)

def futhark_to_bits64(x):
  s = struct.pack('>d', x)
  return np.int64(struct.unpack('>q', s)[0])

def futhark_from_bits64(x):
  s = struct.pack('>q', x)
  return np.float64(struct.unpack('>d', s)[0])

def futhark_log32(x):
  return np.float32(np.log(x))

def futhark_log2_32(x):
  return np.float32(np.log2(x))

def futhark_log10_32(x):
  return np.float32(np.log10(x))

def futhark_sqrt32(x):
  return np.float32(np.sqrt(x))

def futhark_exp32(x):
  return np.exp(x)

def futhark_cos32(x):
  return np.cos(x)

def futhark_sin32(x):
  return np.sin(x)

def futhark_tan32(x):
  return np.tan(x)

def futhark_acos32(x):
  return np.arccos(x)

def futhark_asin32(x):
  return np.arcsin(x)

def futhark_atan32(x):
  return np.arctan(x)

def futhark_atan2_32(x, y):
  return np.arctan2(x, y)

def futhark_gamma32(x):
  return np.float32(math.gamma(x))

def futhark_lgamma32(x):
  return np.float32(math.lgamma(x))

def futhark_round32(x):
  return np.round(x)

def futhark_ceil32(x):
  return np.ceil(x)

def futhark_floor32(x):
  return np.floor(x)

def futhark_isnan32(x):
  return np.isnan(x)

def futhark_isinf32(x):
  return np.isinf(x)

def futhark_to_bits32(x):
  s = struct.pack('>f', x)
  return np.int32(struct.unpack('>l', s)[0])

def futhark_from_bits32(x):
  s = struct.pack('>l', x)
  return np.float32(struct.unpack('>f', s)[0])

def futhark_lerp32(v0, v1, t):
  return v0 + (v1-v0)*t

def futhark_lerp64(v0, v1, t):
  return v0 + (v1-v0)*t

# End of scalar.py.
class information:
  entry_points = {"alpha_divergence_f64": (["f64", "[]f64", "[]f64"], ["f64"]),
                  "alpha_divergence_f32": (["f32", "[]f32", "[]f32"], ["f32"]),
                  "hellinger_f64": (["[]f64", "[]f64"], ["f64"]),
                  "hellinger_f32": (["[]f32", "[]f32"], ["f32"]),
                  "kullback_liebler_scaled_f32": (["[]f32", "[]f32"], ["f32"]),
                  "kullback_liebler_f32": (["[]f32", "[]f32"], ["f32"]),
                  "kullback_liebler_scaled_f64": (["[]f64", "[]f64"], ["f64"]),
                  "kullback_liebler_f64": (["[]f64", "[]f64"], ["f64"]),
                  "entropy_scaled_f32": (["[]f32"], ["f32"]),
                  "entropy_scaled_f64": (["[]f64"], ["f64"]),
                  "entropy_f32": (["[]f32"], ["f32"]),
                  "entropy_f64": (["[]f64"], ["f64"])}
  def __init__(self, command_queue=None, interactive=False,
               platform_pref=preferred_platform, device_pref=preferred_device,
               default_group_size=default_group_size,
               default_num_groups=default_num_groups,
               default_tile_size=default_tile_size,
               default_threshold=default_threshold, sizes=sizes):
    size_heuristics=[("NVIDIA CUDA", cl.device_type.GPU, "lockstep_width", 32),
     ("AMD Accelerated Parallel Processing", cl.device_type.GPU, "lockstep_width",
      32), ("", cl.device_type.GPU, "lockstep_width", 1), ("", cl.device_type.GPU,
                                                           "num_groups", 256), ("",
                                                                                cl.device_type.GPU,
                                                                                "group_size",
                                                                                256),
     ("", cl.device_type.GPU, "tile_size", 32), ("", cl.device_type.GPU,
                                                 "threshold", 32768), ("",
                                                                       cl.device_type.CPU,
                                                                       "lockstep_width",
                                                                       1), ("",
                                                                            cl.device_type.CPU,
                                                                            "num_groups",
                                                                            "MAX_COMPUTE_UNITS"),
     ("", cl.device_type.CPU, "group_size", 32), ("", cl.device_type.CPU,
                                                  "tile_size", 4), ("",
                                                                    cl.device_type.CPU,
                                                                    "threshold",
                                                                    "MAX_COMPUTE_UNITS")]
    program = initialise_opencl_object(self,
                                       program_src=fut_opencl_src,
                                       command_queue=command_queue,
                                       interactive=interactive,
                                       platform_pref=platform_pref,
                                       device_pref=device_pref,
                                       default_group_size=default_group_size,
                                       default_num_groups=default_num_groups,
                                       default_tile_size=default_tile_size,
                                       default_threshold=default_threshold,
                                       size_heuristics=size_heuristics,
                                       required_types=["i32", "f32", "f64", "bool"],
                                       user_sizes=sizes,
                                       all_sizes={"alpha_divergence_f32.segred_group_size_10204": {"class": "group_size",
                                                                                         "value": None},
                                        "alpha_divergence_f32.segred_num_groups_10206": {"class": "num_groups",
                                                                                         "value": None},
                                        "alpha_divergence_f64.segred_group_size_10215": {"class": "group_size",
                                                                                         "value": None},
                                        "alpha_divergence_f64.segred_num_groups_10217": {"class": "num_groups",
                                                                                         "value": None},
                                        "entropy_f32.segred_group_size_10039": {"class": "group_size", "value": None},
                                        "entropy_f32.segred_num_groups_10041": {"class": "num_groups", "value": None},
                                        "entropy_f64.segred_group_size_10028": {"class": "group_size", "value": None},
                                        "entropy_f64.segred_num_groups_10030": {"class": "num_groups", "value": None},
                                        "entropy_scaled_f32.segred_group_size_10072": {"class": "group_size",
                                                                                       "value": None},
                                        "entropy_scaled_f32.segred_group_size_10083": {"class": "group_size",
                                                                                       "value": None},
                                        "entropy_scaled_f32.segred_num_groups_10074": {"class": "num_groups",
                                                                                       "value": None},
                                        "entropy_scaled_f32.segred_num_groups_10085": {"class": "num_groups",
                                                                                       "value": None},
                                        "entropy_scaled_f64.segred_group_size_10050": {"class": "group_size",
                                                                                       "value": None},
                                        "entropy_scaled_f64.segred_group_size_10061": {"class": "group_size",
                                                                                       "value": None},
                                        "entropy_scaled_f64.segred_num_groups_10052": {"class": "num_groups",
                                                                                       "value": None},
                                        "entropy_scaled_f64.segred_num_groups_10063": {"class": "num_groups",
                                                                                       "value": None},
                                        "hellinger_f32.segred_group_size_10182": {"class": "group_size",
                                                                                  "value": None},
                                        "hellinger_f32.segred_num_groups_10184": {"class": "num_groups",
                                                                                  "value": None},
                                        "hellinger_f64.segred_group_size_10193": {"class": "group_size",
                                                                                  "value": None},
                                        "hellinger_f64.segred_num_groups_10195": {"class": "num_groups",
                                                                                  "value": None},
                                        "kullback_liebler_f32.segred_group_size_10138": {"class": "group_size",
                                                                                         "value": None},
                                        "kullback_liebler_f32.segred_num_groups_10140": {"class": "num_groups",
                                                                                         "value": None},
                                        "kullback_liebler_f64.segred_group_size_10094": {"class": "group_size",
                                                                                         "value": None},
                                        "kullback_liebler_f64.segred_num_groups_10096": {"class": "num_groups",
                                                                                         "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_10149": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_10160": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f32.segred_group_size_10171": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_10151": {"class": "num_groups",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_10162": {"class": "num_groups",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f32.segred_num_groups_10173": {"class": "num_groups",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_10105": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_10116": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_group_size_10127": {"class": "group_size",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_10107": {"class": "num_groups",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_10118": {"class": "num_groups",
                                                                                                "value": None},
                                        "kullback_liebler_scaled_f64.segred_num_groups_10129": {"class": "num_groups",
                                                                                                "value": None}})
    self.segred_nonseg_10036_var = program.segred_nonseg_10036
    self.segred_nonseg_10047_var = program.segred_nonseg_10047
    self.segred_nonseg_10058_var = program.segred_nonseg_10058
    self.segred_nonseg_10069_var = program.segred_nonseg_10069
    self.segred_nonseg_10080_var = program.segred_nonseg_10080
    self.segred_nonseg_10091_var = program.segred_nonseg_10091
    self.segred_nonseg_10102_var = program.segred_nonseg_10102
    self.segred_nonseg_10113_var = program.segred_nonseg_10113
    self.segred_nonseg_10124_var = program.segred_nonseg_10124
    self.segred_nonseg_10135_var = program.segred_nonseg_10135
    self.segred_nonseg_10146_var = program.segred_nonseg_10146
    self.segred_nonseg_10157_var = program.segred_nonseg_10157
    self.segred_nonseg_10168_var = program.segred_nonseg_10168
    self.segred_nonseg_10179_var = program.segred_nonseg_10179
    self.segred_nonseg_10190_var = program.segred_nonseg_10190
    self.segred_nonseg_10201_var = program.segred_nonseg_10201
    self.segred_nonseg_10212_var = program.segred_nonseg_10212
    self.segred_nonseg_10223_var = program.segred_nonseg_10223
    counter_mem_10749 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10775 = opencl_alloc(self, 40, "static_mem_10775")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10775,
                      normaliseArray(counter_mem_10749),
                      is_blocking=synchronous)
    self.counter_mem_10749 = static_mem_10775
    counter_mem_10721 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10777 = opencl_alloc(self, 40, "static_mem_10777")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10777,
                      normaliseArray(counter_mem_10721),
                      is_blocking=synchronous)
    self.counter_mem_10721 = static_mem_10777
    counter_mem_10693 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10779 = opencl_alloc(self, 40, "static_mem_10779")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10779,
                      normaliseArray(counter_mem_10693),
                      is_blocking=synchronous)
    self.counter_mem_10693 = static_mem_10779
    counter_mem_10665 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10781 = opencl_alloc(self, 40, "static_mem_10781")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10781,
                      normaliseArray(counter_mem_10665),
                      is_blocking=synchronous)
    self.counter_mem_10665 = static_mem_10781
    counter_mem_10583 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10783 = opencl_alloc(self, 40, "static_mem_10783")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10783,
                      normaliseArray(counter_mem_10583),
                      is_blocking=synchronous)
    self.counter_mem_10583 = static_mem_10783
    counter_mem_10610 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10785 = opencl_alloc(self, 40, "static_mem_10785")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10785,
                      normaliseArray(counter_mem_10610),
                      is_blocking=synchronous)
    self.counter_mem_10610 = static_mem_10785
    counter_mem_10637 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10787 = opencl_alloc(self, 40, "static_mem_10787")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10787,
                      normaliseArray(counter_mem_10637),
                      is_blocking=synchronous)
    self.counter_mem_10637 = static_mem_10787
    counter_mem_10555 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10789 = opencl_alloc(self, 40, "static_mem_10789")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10789,
                      normaliseArray(counter_mem_10555),
                      is_blocking=synchronous)
    self.counter_mem_10555 = static_mem_10789
    counter_mem_10473 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10791 = opencl_alloc(self, 40, "static_mem_10791")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10791,
                      normaliseArray(counter_mem_10473),
                      is_blocking=synchronous)
    self.counter_mem_10473 = static_mem_10791
    counter_mem_10500 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10793 = opencl_alloc(self, 40, "static_mem_10793")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10793,
                      normaliseArray(counter_mem_10500),
                      is_blocking=synchronous)
    self.counter_mem_10500 = static_mem_10793
    counter_mem_10527 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10795 = opencl_alloc(self, 40, "static_mem_10795")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10795,
                      normaliseArray(counter_mem_10527),
                      is_blocking=synchronous)
    self.counter_mem_10527 = static_mem_10795
    counter_mem_10445 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10797 = opencl_alloc(self, 40, "static_mem_10797")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10797,
                      normaliseArray(counter_mem_10445),
                      is_blocking=synchronous)
    self.counter_mem_10445 = static_mem_10797
    counter_mem_10390 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10799 = opencl_alloc(self, 40, "static_mem_10799")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10799,
                      normaliseArray(counter_mem_10390),
                      is_blocking=synchronous)
    self.counter_mem_10390 = static_mem_10799
    counter_mem_10417 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10801 = opencl_alloc(self, 40, "static_mem_10801")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10801,
                      normaliseArray(counter_mem_10417),
                      is_blocking=synchronous)
    self.counter_mem_10417 = static_mem_10801
    counter_mem_10335 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10803 = opencl_alloc(self, 40, "static_mem_10803")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10803,
                      normaliseArray(counter_mem_10335),
                      is_blocking=synchronous)
    self.counter_mem_10335 = static_mem_10803
    counter_mem_10362 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10805 = opencl_alloc(self, 40, "static_mem_10805")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10805,
                      normaliseArray(counter_mem_10362),
                      is_blocking=synchronous)
    self.counter_mem_10362 = static_mem_10805
    counter_mem_10307 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10807 = opencl_alloc(self, 40, "static_mem_10807")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10807,
                      normaliseArray(counter_mem_10307),
                      is_blocking=synchronous)
    self.counter_mem_10307 = static_mem_10807
    counter_mem_10279 = np.array([np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0), np.int32(0), np.int32(0),
                                  np.int32(0)], dtype=np.int32)
    static_mem_10809 = opencl_alloc(self, 40, "static_mem_10809")
    if (40 != 0):
      cl.enqueue_copy(self.queue, static_mem_10809,
                      normaliseArray(counter_mem_10279),
                      is_blocking=synchronous)
    self.counter_mem_10279 = static_mem_10809
  def futhark_alpha_divergence_f64(self, x_mem_10227, x_mem_10228, sizze_9996,
                                   sizze_9997, x_9998):
    res_10001 = fpow64(x_9998, np.float64(2.0))
    res_10002 = (np.float64(1.0) - res_10001)
    res_10003 = (np.float64(4.0) / res_10002)
    dim_zzero_10004 = (np.int32(0) == sizze_9997)
    dim_zzero_10005 = (np.int32(0) == sizze_9996)
    both_empty_10006 = (dim_zzero_10004 and dim_zzero_10005)
    dim_match_10007 = (sizze_9996 == sizze_9997)
    empty_or_match_10008 = (both_empty_10006 or dim_match_10007)
    empty_or_match_cert_10009 = True
    assert empty_or_match_10008, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:46:12-81\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:84:1-61\n" % ("function arguments of wrong shape",))
    res_10010 = (np.float64(1.0) - x_9998)
    res_10011 = (res_10010 / np.float64(2.0))
    res_10012 = (np.float64(1.0) + x_9998)
    res_10013 = (res_10012 / np.float64(2.0))
    sizze_10213 = sext_i32_i64(sizze_9996)
    segred_group_sizze_10216 = self.sizes["alpha_divergence_f64.segred_group_size_10215"]
    max_num_groups_10748 = self.sizes["alpha_divergence_f64.segred_num_groups_10217"]
    num_groups_10218 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10213 + sext_i32_i64(segred_group_sizze_10216)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10216)),
                                                  sext_i32_i64(max_num_groups_10748))))
    mem_10232 = opencl_alloc(self, np.int64(8), "mem_10232")
    counter_mem_10749 = self.counter_mem_10749
    group_res_arr_mem_10751 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10216 * num_groups_10218)),
                                           "group_res_arr_mem_10751")
    num_threads_10753 = (num_groups_10218 * segred_group_sizze_10216)
    if ((1 * (np.long(num_groups_10218) * np.long(segred_group_sizze_10216))) != 0):
      self.segred_nonseg_10223_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10216))),
                                            np.int32(sizze_9996),
                                            np.float64(res_10011),
                                            np.float64(res_10013),
                                            np.int32(num_groups_10218),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10749,
                                            group_res_arr_mem_10751,
                                            np.int32(num_threads_10753))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10223_var,
                                 ((np.long(num_groups_10218) * np.long(segred_group_sizze_10216)),),
                                 (np.long(segred_group_sizze_10216),))
      if synchronous:
        self.queue.finish()
    read_res_10776 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10776, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_10015 = read_res_10776[0]
    mem_10232 = None
    res_10024 = (np.float64(1.0) - res_10015)
    res_10025 = (res_10003 * res_10024)
    scalar_out_10747 = res_10025
    return scalar_out_10747
  def futhark_alpha_divergence_f32(self, x_mem_10227, x_mem_10228, sizze_9966,
                                   sizze_9967, x_9968):
    res_9971 = fpow32(x_9968, np.float32(2.0))
    res_9972 = (np.float32(1.0) - res_9971)
    res_9973 = (np.float32(4.0) / res_9972)
    dim_zzero_9974 = (np.int32(0) == sizze_9967)
    dim_zzero_9975 = (np.int32(0) == sizze_9966)
    both_empty_9976 = (dim_zzero_9974 and dim_zzero_9975)
    dim_match_9977 = (sizze_9966 == sizze_9967)
    empty_or_match_9978 = (both_empty_9976 or dim_match_9977)
    empty_or_match_cert_9979 = True
    assert empty_or_match_9978, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:46:12-81\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:83:1-61\n" % ("function arguments of wrong shape",))
    res_9980 = (np.float32(1.0) - x_9968)
    res_9981 = (res_9980 / np.float32(2.0))
    res_9982 = (np.float32(1.0) + x_9968)
    res_9983 = (res_9982 / np.float32(2.0))
    sizze_10202 = sext_i32_i64(sizze_9966)
    segred_group_sizze_10205 = self.sizes["alpha_divergence_f32.segred_group_size_10204"]
    max_num_groups_10720 = self.sizes["alpha_divergence_f32.segred_num_groups_10206"]
    num_groups_10207 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10202 + sext_i32_i64(segred_group_sizze_10205)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10205)),
                                                  sext_i32_i64(max_num_groups_10720))))
    mem_10232 = opencl_alloc(self, np.int64(4), "mem_10232")
    counter_mem_10721 = self.counter_mem_10721
    group_res_arr_mem_10723 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10205 * num_groups_10207)),
                                           "group_res_arr_mem_10723")
    num_threads_10725 = (num_groups_10207 * segred_group_sizze_10205)
    if ((1 * (np.long(num_groups_10207) * np.long(segred_group_sizze_10205))) != 0):
      self.segred_nonseg_10212_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10205))),
                                            np.int32(sizze_9966),
                                            np.float32(res_9981),
                                            np.float32(res_9983),
                                            np.int32(num_groups_10207),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10721,
                                            group_res_arr_mem_10723,
                                            np.int32(num_threads_10725))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10212_var,
                                 ((np.long(num_groups_10207) * np.long(segred_group_sizze_10205)),),
                                 (np.long(segred_group_sizze_10205),))
      if synchronous:
        self.queue.finish()
    read_res_10778 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10778, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9985 = read_res_10778[0]
    mem_10232 = None
    res_9994 = (np.float32(1.0) - res_9985)
    res_9995 = (res_9973 * res_9994)
    scalar_out_10719 = res_9995
    return scalar_out_10719
  def futhark_hellinger_f64(self, x_mem_10227, x_mem_10228, sizze_9943,
                            sizze_9944):
    dim_zzero_9947 = (np.int32(0) == sizze_9944)
    dim_zzero_9948 = (np.int32(0) == sizze_9943)
    both_empty_9949 = (dim_zzero_9947 and dim_zzero_9948)
    dim_match_9950 = (sizze_9943 == sizze_9944)
    empty_or_match_9951 = (both_empty_9949 or dim_match_9950)
    empty_or_match_cert_9952 = True
    assert empty_or_match_9951, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:50:13-55\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:82:1-47\n" % ("function arguments of wrong shape",))
    sizze_10191 = sext_i32_i64(sizze_9943)
    segred_group_sizze_10194 = self.sizes["hellinger_f64.segred_group_size_10193"]
    max_num_groups_10692 = self.sizes["hellinger_f64.segred_num_groups_10195"]
    num_groups_10196 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10191 + sext_i32_i64(segred_group_sizze_10194)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10194)),
                                                  sext_i32_i64(max_num_groups_10692))))
    mem_10232 = opencl_alloc(self, np.int64(8), "mem_10232")
    counter_mem_10693 = self.counter_mem_10693
    group_res_arr_mem_10695 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10194 * num_groups_10196)),
                                           "group_res_arr_mem_10695")
    num_threads_10697 = (num_groups_10196 * segred_group_sizze_10194)
    if ((1 * (np.long(num_groups_10196) * np.long(segred_group_sizze_10194))) != 0):
      self.segred_nonseg_10201_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10194))),
                                            np.int32(sizze_9943),
                                            np.int32(num_groups_10196),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10693,
                                            group_res_arr_mem_10695,
                                            np.int32(num_threads_10697))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10201_var,
                                 ((np.long(num_groups_10196) * np.long(segred_group_sizze_10194)),),
                                 (np.long(segred_group_sizze_10194),))
      if synchronous:
        self.queue.finish()
    read_res_10780 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10780, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9954 = read_res_10780[0]
    mem_10232 = None
    res_9964 = (np.float64(2.0) * res_9954)
    res_9965 = futhark_sqrt64(res_9964)
    scalar_out_10691 = res_9965
    return scalar_out_10691
  def futhark_hellinger_f32(self, x_mem_10227, x_mem_10228, sizze_9920,
                            sizze_9921):
    dim_zzero_9924 = (np.int32(0) == sizze_9921)
    dim_zzero_9925 = (np.int32(0) == sizze_9920)
    both_empty_9926 = (dim_zzero_9924 and dim_zzero_9925)
    dim_match_9927 = (sizze_9920 == sizze_9921)
    empty_or_match_9928 = (both_empty_9926 or dim_match_9927)
    empty_or_match_cert_9929 = True
    assert empty_or_match_9928, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:50:13-55\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:81:1-47\n" % ("function arguments of wrong shape",))
    sizze_10180 = sext_i32_i64(sizze_9920)
    segred_group_sizze_10183 = self.sizes["hellinger_f32.segred_group_size_10182"]
    max_num_groups_10664 = self.sizes["hellinger_f32.segred_num_groups_10184"]
    num_groups_10185 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10180 + sext_i32_i64(segred_group_sizze_10183)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10183)),
                                                  sext_i32_i64(max_num_groups_10664))))
    mem_10232 = opencl_alloc(self, np.int64(4), "mem_10232")
    counter_mem_10665 = self.counter_mem_10665
    group_res_arr_mem_10667 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10183 * num_groups_10185)),
                                           "group_res_arr_mem_10667")
    num_threads_10669 = (num_groups_10185 * segred_group_sizze_10183)
    if ((1 * (np.long(num_groups_10185) * np.long(segred_group_sizze_10183))) != 0):
      self.segred_nonseg_10190_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10183))),
                                            np.int32(sizze_9920),
                                            np.int32(num_groups_10185),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10665,
                                            group_res_arr_mem_10667,
                                            np.int32(num_threads_10669))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10190_var,
                                 ((np.long(num_groups_10185) * np.long(segred_group_sizze_10183)),),
                                 (np.long(segred_group_sizze_10183),))
      if synchronous:
        self.queue.finish()
    read_res_10782 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10782, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9931 = read_res_10782[0]
    mem_10232 = None
    res_9941 = (np.float32(2.0) * res_9931)
    res_9942 = futhark_sqrt32(res_9941)
    scalar_out_10663 = res_9942
    return scalar_out_10663
  def futhark_kullback_liebler_scaled_f32(self, x_mem_10227, y_mem_10228,
                                          sizze_9888, sizze_9889):
    sizze_10147 = sext_i32_i64(sizze_9888)
    segred_group_sizze_10150 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_10149"]
    max_num_groups_10582 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_10151"]
    num_groups_10152 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10147 + sext_i32_i64(segred_group_sizze_10150)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10150)),
                                                  sext_i32_i64(max_num_groups_10582))))
    mem_10232 = opencl_alloc(self, np.int64(4), "mem_10232")
    counter_mem_10583 = self.counter_mem_10583
    group_res_arr_mem_10585 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10150 * num_groups_10152)),
                                           "group_res_arr_mem_10585")
    num_threads_10587 = (num_groups_10152 * segred_group_sizze_10150)
    if ((1 * (np.long(num_groups_10152) * np.long(segred_group_sizze_10150))) != 0):
      self.segred_nonseg_10157_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10150))),
                                            np.int32(sizze_9888),
                                            np.int32(num_groups_10152),
                                            x_mem_10227, mem_10232,
                                            counter_mem_10583,
                                            group_res_arr_mem_10585,
                                            np.int32(num_threads_10587))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10157_var,
                                 ((np.long(num_groups_10152) * np.long(segred_group_sizze_10150)),),
                                 (np.long(segred_group_sizze_10150),))
      if synchronous:
        self.queue.finish()
    read_res_10784 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10784, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9892 = read_res_10784[0]
    mem_10232 = None
    sizze_10158 = sext_i32_i64(sizze_9889)
    segred_group_sizze_10161 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_10160"]
    max_num_groups_10609 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_10162"]
    num_groups_10163 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10158 + sext_i32_i64(segred_group_sizze_10161)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10161)),
                                                  sext_i32_i64(max_num_groups_10609))))
    mem_10236 = opencl_alloc(self, np.int64(4), "mem_10236")
    counter_mem_10610 = self.counter_mem_10610
    group_res_arr_mem_10612 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10161 * num_groups_10163)),
                                           "group_res_arr_mem_10612")
    num_threads_10614 = (num_groups_10163 * segred_group_sizze_10161)
    if ((1 * (np.long(num_groups_10163) * np.long(segred_group_sizze_10161))) != 0):
      self.segred_nonseg_10168_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10161))),
                                            np.int32(sizze_9889),
                                            np.int32(num_groups_10163),
                                            y_mem_10228, mem_10236,
                                            counter_mem_10610,
                                            group_res_arr_mem_10612,
                                            np.int32(num_threads_10614))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10168_var,
                                 ((np.long(num_groups_10163) * np.long(segred_group_sizze_10161)),),
                                 (np.long(segred_group_sizze_10161),))
      if synchronous:
        self.queue.finish()
    read_res_10786 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10786, mem_10236,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9897 = read_res_10786[0]
    mem_10236 = None
    dim_zzero_9902 = (np.int32(0) == sizze_9889)
    dim_zzero_9903 = (np.int32(0) == sizze_9888)
    both_empty_9904 = (dim_zzero_9902 and dim_zzero_9903)
    dim_match_9905 = (sizze_9888 == sizze_9889)
    empty_or_match_9906 = (both_empty_9904 or dim_match_9905)
    empty_or_match_cert_9907 = True
    assert empty_or_match_9906, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:38:10-43\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:79:3-86\n   #2  lib/github.com/vmchale/kullback-liebler/information.fut:78:1-79:86\n" % ("function arguments of wrong shape",))
    segred_group_sizze_10172 = self.sizes["kullback_liebler_scaled_f32.segred_group_size_10171"]
    max_num_groups_10636 = self.sizes["kullback_liebler_scaled_f32.segred_num_groups_10173"]
    num_groups_10174 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10147 + sext_i32_i64(segred_group_sizze_10172)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10172)),
                                                  sext_i32_i64(max_num_groups_10636))))
    mem_10240 = opencl_alloc(self, np.int64(4), "mem_10240")
    counter_mem_10637 = self.counter_mem_10637
    group_res_arr_mem_10639 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10172 * num_groups_10174)),
                                           "group_res_arr_mem_10639")
    num_threads_10641 = (num_groups_10174 * segred_group_sizze_10172)
    if ((1 * (np.long(num_groups_10174) * np.long(segred_group_sizze_10172))) != 0):
      self.segred_nonseg_10179_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10172))),
                                            np.int32(sizze_9888),
                                            np.float32(res_9892),
                                            np.float32(res_9897),
                                            np.int32(num_groups_10174),
                                            x_mem_10227, y_mem_10228, mem_10240,
                                            counter_mem_10637,
                                            group_res_arr_mem_10639,
                                            np.int32(num_threads_10641))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10179_var,
                                 ((np.long(num_groups_10174) * np.long(segred_group_sizze_10172)),),
                                 (np.long(segred_group_sizze_10172),))
      if synchronous:
        self.queue.finish()
    read_res_10788 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10788, mem_10240,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9909 = read_res_10788[0]
    mem_10240 = None
    scalar_out_10581 = res_9909
    return scalar_out_10581
  def futhark_kullback_liebler_f32(self, x_mem_10227, x_mem_10228, sizze_9868,
                                   sizze_9869):
    dim_zzero_9872 = (np.int32(0) == sizze_9869)
    dim_zzero_9873 = (np.int32(0) == sizze_9868)
    both_empty_9874 = (dim_zzero_9872 and dim_zzero_9873)
    dim_match_9875 = (sizze_9868 == sizze_9869)
    empty_or_match_9876 = (both_empty_9874 or dim_match_9875)
    empty_or_match_cert_9877 = True
    assert empty_or_match_9876, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:38:10-43\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:75:1-76:34\n" % ("function arguments of wrong shape",))
    sizze_10136 = sext_i32_i64(sizze_9868)
    segred_group_sizze_10139 = self.sizes["kullback_liebler_f32.segred_group_size_10138"]
    max_num_groups_10554 = self.sizes["kullback_liebler_f32.segred_num_groups_10140"]
    num_groups_10141 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10136 + sext_i32_i64(segred_group_sizze_10139)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10139)),
                                                  sext_i32_i64(max_num_groups_10554))))
    mem_10232 = opencl_alloc(self, np.int64(4), "mem_10232")
    counter_mem_10555 = self.counter_mem_10555
    group_res_arr_mem_10557 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10139 * num_groups_10141)),
                                           "group_res_arr_mem_10557")
    num_threads_10559 = (num_groups_10141 * segred_group_sizze_10139)
    if ((1 * (np.long(num_groups_10141) * np.long(segred_group_sizze_10139))) != 0):
      self.segred_nonseg_10146_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10139))),
                                            np.int32(sizze_9868),
                                            np.int32(num_groups_10141),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10555,
                                            group_res_arr_mem_10557,
                                            np.int32(num_threads_10559))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10146_var,
                                 ((np.long(num_groups_10141) * np.long(segred_group_sizze_10139)),),
                                 (np.long(segred_group_sizze_10139),))
      if synchronous:
        self.queue.finish()
    read_res_10790 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10790, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9879 = read_res_10790[0]
    mem_10232 = None
    scalar_out_10553 = res_9879
    return scalar_out_10553
  def futhark_kullback_liebler_scaled_f64(self, x_mem_10227, y_mem_10228,
                                          sizze_9836, sizze_9837):
    sizze_10103 = sext_i32_i64(sizze_9836)
    segred_group_sizze_10106 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_10105"]
    max_num_groups_10472 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_10107"]
    num_groups_10108 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10103 + sext_i32_i64(segred_group_sizze_10106)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10106)),
                                                  sext_i32_i64(max_num_groups_10472))))
    mem_10232 = opencl_alloc(self, np.int64(8), "mem_10232")
    counter_mem_10473 = self.counter_mem_10473
    group_res_arr_mem_10475 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10106 * num_groups_10108)),
                                           "group_res_arr_mem_10475")
    num_threads_10477 = (num_groups_10108 * segred_group_sizze_10106)
    if ((1 * (np.long(num_groups_10108) * np.long(segred_group_sizze_10106))) != 0):
      self.segred_nonseg_10113_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10106))),
                                            np.int32(sizze_9836),
                                            np.int32(num_groups_10108),
                                            x_mem_10227, mem_10232,
                                            counter_mem_10473,
                                            group_res_arr_mem_10475,
                                            np.int32(num_threads_10477))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10113_var,
                                 ((np.long(num_groups_10108) * np.long(segred_group_sizze_10106)),),
                                 (np.long(segred_group_sizze_10106),))
      if synchronous:
        self.queue.finish()
    read_res_10792 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10792, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9840 = read_res_10792[0]
    mem_10232 = None
    sizze_10114 = sext_i32_i64(sizze_9837)
    segred_group_sizze_10117 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_10116"]
    max_num_groups_10499 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_10118"]
    num_groups_10119 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10114 + sext_i32_i64(segred_group_sizze_10117)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10117)),
                                                  sext_i32_i64(max_num_groups_10499))))
    mem_10236 = opencl_alloc(self, np.int64(8), "mem_10236")
    counter_mem_10500 = self.counter_mem_10500
    group_res_arr_mem_10502 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10117 * num_groups_10119)),
                                           "group_res_arr_mem_10502")
    num_threads_10504 = (num_groups_10119 * segred_group_sizze_10117)
    if ((1 * (np.long(num_groups_10119) * np.long(segred_group_sizze_10117))) != 0):
      self.segred_nonseg_10124_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10117))),
                                            np.int32(sizze_9837),
                                            np.int32(num_groups_10119),
                                            y_mem_10228, mem_10236,
                                            counter_mem_10500,
                                            group_res_arr_mem_10502,
                                            np.int32(num_threads_10504))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10124_var,
                                 ((np.long(num_groups_10119) * np.long(segred_group_sizze_10117)),),
                                 (np.long(segred_group_sizze_10117),))
      if synchronous:
        self.queue.finish()
    read_res_10794 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10794, mem_10236,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9845 = read_res_10794[0]
    mem_10236 = None
    dim_zzero_9850 = (np.int32(0) == sizze_9837)
    dim_zzero_9851 = (np.int32(0) == sizze_9836)
    both_empty_9852 = (dim_zzero_9850 and dim_zzero_9851)
    dim_match_9853 = (sizze_9836 == sizze_9837)
    empty_or_match_9854 = (both_empty_9852 or dim_match_9853)
    empty_or_match_cert_9855 = True
    assert empty_or_match_9854, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:38:10-43\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:67:3-86\n   #2  lib/github.com/vmchale/kullback-liebler/information.fut:66:1-67:86\n" % ("function arguments of wrong shape",))
    segred_group_sizze_10128 = self.sizes["kullback_liebler_scaled_f64.segred_group_size_10127"]
    max_num_groups_10526 = self.sizes["kullback_liebler_scaled_f64.segred_num_groups_10129"]
    num_groups_10130 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10103 + sext_i32_i64(segred_group_sizze_10128)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10128)),
                                                  sext_i32_i64(max_num_groups_10526))))
    mem_10240 = opencl_alloc(self, np.int64(8), "mem_10240")
    counter_mem_10527 = self.counter_mem_10527
    group_res_arr_mem_10529 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10128 * num_groups_10130)),
                                           "group_res_arr_mem_10529")
    num_threads_10531 = (num_groups_10130 * segred_group_sizze_10128)
    if ((1 * (np.long(num_groups_10130) * np.long(segred_group_sizze_10128))) != 0):
      self.segred_nonseg_10135_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10128))),
                                            np.int32(sizze_9836),
                                            np.float64(res_9840),
                                            np.float64(res_9845),
                                            np.int32(num_groups_10130),
                                            x_mem_10227, y_mem_10228, mem_10240,
                                            counter_mem_10527,
                                            group_res_arr_mem_10529,
                                            np.int32(num_threads_10531))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10135_var,
                                 ((np.long(num_groups_10130) * np.long(segred_group_sizze_10128)),),
                                 (np.long(segred_group_sizze_10128),))
      if synchronous:
        self.queue.finish()
    read_res_10796 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10796, mem_10240,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9857 = read_res_10796[0]
    mem_10240 = None
    scalar_out_10471 = res_9857
    return scalar_out_10471
  def futhark_kullback_liebler_f64(self, x_mem_10227, x_mem_10228, sizze_9816,
                                   sizze_9817):
    dim_zzero_9820 = (np.int32(0) == sizze_9817)
    dim_zzero_9821 = (np.int32(0) == sizze_9816)
    both_empty_9822 = (dim_zzero_9820 and dim_zzero_9821)
    dim_match_9823 = (sizze_9816 == sizze_9817)
    empty_or_match_9824 = (both_empty_9822 or dim_match_9823)
    empty_or_match_cert_9825 = True
    assert empty_or_match_9824, ("Error: %s\n\nBacktrace:\n-> #0  lib/github.com/vmchale/kullback-liebler/information.fut:38:10-43\n   #1  lib/github.com/vmchale/kullback-liebler/information.fut:63:1-64:34\n" % ("function arguments of wrong shape",))
    sizze_10092 = sext_i32_i64(sizze_9816)
    segred_group_sizze_10095 = self.sizes["kullback_liebler_f64.segred_group_size_10094"]
    max_num_groups_10444 = self.sizes["kullback_liebler_f64.segred_num_groups_10096"]
    num_groups_10097 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10092 + sext_i32_i64(segred_group_sizze_10095)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10095)),
                                                  sext_i32_i64(max_num_groups_10444))))
    mem_10232 = opencl_alloc(self, np.int64(8), "mem_10232")
    counter_mem_10445 = self.counter_mem_10445
    group_res_arr_mem_10447 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10095 * num_groups_10097)),
                                           "group_res_arr_mem_10447")
    num_threads_10449 = (num_groups_10097 * segred_group_sizze_10095)
    if ((1 * (np.long(num_groups_10097) * np.long(segred_group_sizze_10095))) != 0):
      self.segred_nonseg_10102_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10095))),
                                            np.int32(sizze_9816),
                                            np.int32(num_groups_10097),
                                            x_mem_10227, x_mem_10228, mem_10232,
                                            counter_mem_10445,
                                            group_res_arr_mem_10447,
                                            np.int32(num_threads_10449))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10102_var,
                                 ((np.long(num_groups_10097) * np.long(segred_group_sizze_10095)),),
                                 (np.long(segred_group_sizze_10095),))
      if synchronous:
        self.queue.finish()
    read_res_10798 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10798, mem_10232,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9827 = read_res_10798[0]
    mem_10232 = None
    scalar_out_10443 = res_9827
    return scalar_out_10443
  def futhark_entropy_scaled_f32(self, x_mem_10227, sizze_9800):
    sizze_10070 = sext_i32_i64(sizze_9800)
    segred_group_sizze_10073 = self.sizes["entropy_scaled_f32.segred_group_size_10072"]
    max_num_groups_10389 = self.sizes["entropy_scaled_f32.segred_num_groups_10074"]
    num_groups_10075 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10070 + sext_i32_i64(segred_group_sizze_10073)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10073)),
                                                  sext_i32_i64(max_num_groups_10389))))
    mem_10231 = opencl_alloc(self, np.int64(4), "mem_10231")
    counter_mem_10390 = self.counter_mem_10390
    group_res_arr_mem_10392 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10073 * num_groups_10075)),
                                           "group_res_arr_mem_10392")
    num_threads_10394 = (num_groups_10075 * segred_group_sizze_10073)
    if ((1 * (np.long(num_groups_10075) * np.long(segred_group_sizze_10073))) != 0):
      self.segred_nonseg_10080_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10073))),
                                            np.int32(sizze_9800),
                                            np.int32(num_groups_10075),
                                            x_mem_10227, mem_10231,
                                            counter_mem_10390,
                                            group_res_arr_mem_10392,
                                            np.int32(num_threads_10394))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10080_var,
                                 ((np.long(num_groups_10075) * np.long(segred_group_sizze_10073)),),
                                 (np.long(segred_group_sizze_10073),))
      if synchronous:
        self.queue.finish()
    read_res_10800 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10800, mem_10231,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9802 = read_res_10800[0]
    mem_10231 = None
    segred_group_sizze_10084 = self.sizes["entropy_scaled_f32.segred_group_size_10083"]
    max_num_groups_10416 = self.sizes["entropy_scaled_f32.segred_num_groups_10085"]
    num_groups_10086 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10070 + sext_i32_i64(segred_group_sizze_10084)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10084)),
                                                  sext_i32_i64(max_num_groups_10416))))
    mem_10235 = opencl_alloc(self, np.int64(4), "mem_10235")
    counter_mem_10417 = self.counter_mem_10417
    group_res_arr_mem_10419 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10084 * num_groups_10086)),
                                           "group_res_arr_mem_10419")
    num_threads_10421 = (num_groups_10086 * segred_group_sizze_10084)
    if ((1 * (np.long(num_groups_10086) * np.long(segred_group_sizze_10084))) != 0):
      self.segred_nonseg_10091_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10084))),
                                            np.int32(sizze_9800),
                                            np.float32(res_9802),
                                            np.int32(num_groups_10086),
                                            x_mem_10227, mem_10235,
                                            counter_mem_10417,
                                            group_res_arr_mem_10419,
                                            np.int32(num_threads_10421))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10091_var,
                                 ((np.long(num_groups_10086) * np.long(segred_group_sizze_10084)),),
                                 (np.long(segred_group_sizze_10084),))
      if synchronous:
        self.queue.finish()
    read_res_10802 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10802, mem_10235,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9807 = read_res_10802[0]
    mem_10235 = None
    res_9815 = (np.float32(0.0) - res_9807)
    scalar_out_10388 = res_9815
    return scalar_out_10388
  def futhark_entropy_scaled_f64(self, x_mem_10227, sizze_9784):
    sizze_10048 = sext_i32_i64(sizze_9784)
    segred_group_sizze_10051 = self.sizes["entropy_scaled_f64.segred_group_size_10050"]
    max_num_groups_10334 = self.sizes["entropy_scaled_f64.segred_num_groups_10052"]
    num_groups_10053 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10048 + sext_i32_i64(segred_group_sizze_10051)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10051)),
                                                  sext_i32_i64(max_num_groups_10334))))
    mem_10231 = opencl_alloc(self, np.int64(8), "mem_10231")
    counter_mem_10335 = self.counter_mem_10335
    group_res_arr_mem_10337 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10051 * num_groups_10053)),
                                           "group_res_arr_mem_10337")
    num_threads_10339 = (num_groups_10053 * segred_group_sizze_10051)
    if ((1 * (np.long(num_groups_10053) * np.long(segred_group_sizze_10051))) != 0):
      self.segred_nonseg_10058_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10051))),
                                            np.int32(sizze_9784),
                                            np.int32(num_groups_10053),
                                            x_mem_10227, mem_10231,
                                            counter_mem_10335,
                                            group_res_arr_mem_10337,
                                            np.int32(num_threads_10339))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10058_var,
                                 ((np.long(num_groups_10053) * np.long(segred_group_sizze_10051)),),
                                 (np.long(segred_group_sizze_10051),))
      if synchronous:
        self.queue.finish()
    read_res_10804 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10804, mem_10231,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9786 = read_res_10804[0]
    mem_10231 = None
    segred_group_sizze_10062 = self.sizes["entropy_scaled_f64.segred_group_size_10061"]
    max_num_groups_10361 = self.sizes["entropy_scaled_f64.segred_num_groups_10063"]
    num_groups_10064 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10048 + sext_i32_i64(segred_group_sizze_10062)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10062)),
                                                  sext_i32_i64(max_num_groups_10361))))
    mem_10235 = opencl_alloc(self, np.int64(8), "mem_10235")
    counter_mem_10362 = self.counter_mem_10362
    group_res_arr_mem_10364 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10062 * num_groups_10064)),
                                           "group_res_arr_mem_10364")
    num_threads_10366 = (num_groups_10064 * segred_group_sizze_10062)
    if ((1 * (np.long(num_groups_10064) * np.long(segred_group_sizze_10062))) != 0):
      self.segred_nonseg_10069_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10062))),
                                            np.int32(sizze_9784),
                                            np.float64(res_9786),
                                            np.int32(num_groups_10064),
                                            x_mem_10227, mem_10235,
                                            counter_mem_10362,
                                            group_res_arr_mem_10364,
                                            np.int32(num_threads_10366))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10069_var,
                                 ((np.long(num_groups_10064) * np.long(segred_group_sizze_10062)),),
                                 (np.long(segred_group_sizze_10062),))
      if synchronous:
        self.queue.finish()
    read_res_10806 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10806, mem_10235,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9791 = read_res_10806[0]
    mem_10235 = None
    res_9799 = (np.float64(0.0) - res_9791)
    scalar_out_10333 = res_9799
    return scalar_out_10333
  def futhark_entropy_f32(self, x_mem_10227, sizze_9774):
    sizze_10037 = sext_i32_i64(sizze_9774)
    segred_group_sizze_10040 = self.sizes["entropy_f32.segred_group_size_10039"]
    max_num_groups_10306 = self.sizes["entropy_f32.segred_num_groups_10041"]
    num_groups_10042 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10037 + sext_i32_i64(segred_group_sizze_10040)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10040)),
                                                  sext_i32_i64(max_num_groups_10306))))
    mem_10231 = opencl_alloc(self, np.int64(4), "mem_10231")
    counter_mem_10307 = self.counter_mem_10307
    group_res_arr_mem_10309 = opencl_alloc(self,
                                           (np.int32(4) * (segred_group_sizze_10040 * num_groups_10042)),
                                           "group_res_arr_mem_10309")
    num_threads_10311 = (num_groups_10042 * segred_group_sizze_10040)
    if ((1 * (np.long(num_groups_10042) * np.long(segred_group_sizze_10040))) != 0):
      self.segred_nonseg_10047_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(4) * segred_group_sizze_10040))),
                                            np.int32(sizze_9774),
                                            np.int32(num_groups_10042),
                                            x_mem_10227, mem_10231,
                                            counter_mem_10307,
                                            group_res_arr_mem_10309,
                                            np.int32(num_threads_10311))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10047_var,
                                 ((np.long(num_groups_10042) * np.long(segred_group_sizze_10040)),),
                                 (np.long(segred_group_sizze_10040),))
      if synchronous:
        self.queue.finish()
    read_res_10808 = np.empty(1, dtype=ct.c_float)
    cl.enqueue_copy(self.queue, read_res_10808, mem_10231,
                    device_offset=(np.long(np.int32(0)) * 4), is_blocking=True)
    res_9776 = read_res_10808[0]
    mem_10231 = None
    res_9783 = (np.float32(0.0) - res_9776)
    scalar_out_10305 = res_9783
    return scalar_out_10305
  def futhark_entropy_f64(self, x_mem_10227, sizze_9764):
    sizze_10026 = sext_i32_i64(sizze_9764)
    segred_group_sizze_10029 = self.sizes["entropy_f64.segred_group_size_10028"]
    max_num_groups_10278 = self.sizes["entropy_f64.segred_num_groups_10030"]
    num_groups_10031 = sext_i64_i32(smax64(np.int32(1),
                                           smin64(squot64(((sizze_10026 + sext_i32_i64(segred_group_sizze_10029)) - np.int64(1)),
                                                          sext_i32_i64(segred_group_sizze_10029)),
                                                  sext_i32_i64(max_num_groups_10278))))
    mem_10231 = opencl_alloc(self, np.int64(8), "mem_10231")
    counter_mem_10279 = self.counter_mem_10279
    group_res_arr_mem_10281 = opencl_alloc(self,
                                           (np.int32(8) * (segred_group_sizze_10029 * num_groups_10031)),
                                           "group_res_arr_mem_10281")
    num_threads_10283 = (num_groups_10031 * segred_group_sizze_10029)
    if ((1 * (np.long(num_groups_10031) * np.long(segred_group_sizze_10029))) != 0):
      self.segred_nonseg_10036_var.set_args(cl.LocalMemory(np.long(np.int32(1))),
                                            cl.LocalMemory(np.long((np.int32(8) * segred_group_sizze_10029))),
                                            np.int32(sizze_9764),
                                            np.int32(num_groups_10031),
                                            x_mem_10227, mem_10231,
                                            counter_mem_10279,
                                            group_res_arr_mem_10281,
                                            np.int32(num_threads_10283))
      cl.enqueue_nd_range_kernel(self.queue, self.segred_nonseg_10036_var,
                                 ((np.long(num_groups_10031) * np.long(segred_group_sizze_10029)),),
                                 (np.long(segred_group_sizze_10029),))
      if synchronous:
        self.queue.finish()
    read_res_10810 = np.empty(1, dtype=ct.c_double)
    cl.enqueue_copy(self.queue, read_res_10810, mem_10231,
                    device_offset=(np.long(np.int32(0)) * 8), is_blocking=True)
    res_9766 = read_res_10810[0]
    mem_10231 = None
    res_9773 = (np.float64(0.0) - res_9766)
    scalar_out_10277 = res_9773
    return scalar_out_10277
  def alpha_divergence_f64(self, x_9998_ext, x_mem_10227_ext, x_mem_10228_ext):
    try:
      x_9998 = np.float64(ct.c_double(x_9998_ext))
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("f64",
                                                                                                                            type(x_9998_ext),
                                                                                                                            x_9998_ext))
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9996 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9997 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #2 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10747 = self.futhark_alpha_divergence_f64(x_mem_10227,
                                                         x_mem_10228,
                                                         sizze_9996, sizze_9997,
                                                         x_9998)
    return np.float64(scalar_out_10747)
  def alpha_divergence_f32(self, x_9968_ext, x_mem_10227_ext, x_mem_10228_ext):
    try:
      x_9968 = np.float32(ct.c_float(x_9968_ext))
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("f32",
                                                                                                                            type(x_9968_ext),
                                                                                                                            x_9968_ext))
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9966 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9967 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #2 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10719 = self.futhark_alpha_divergence_f32(x_mem_10227,
                                                         x_mem_10228,
                                                         sizze_9966, sizze_9967,
                                                         x_9968)
    return np.float32(scalar_out_10719)
  def hellinger_f64(self, x_mem_10227_ext, x_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9943 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9944 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10691 = self.futhark_hellinger_f64(x_mem_10227, x_mem_10228,
                                                  sizze_9943, sizze_9944)
    return np.float64(scalar_out_10691)
  def hellinger_f32(self, x_mem_10227_ext, x_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9920 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9921 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10663 = self.futhark_hellinger_f32(x_mem_10227, x_mem_10228,
                                                  sizze_9920, sizze_9921)
    return np.float32(scalar_out_10663)
  def kullback_liebler_scaled_f32(self, x_mem_10227_ext, y_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9888 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(y_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (y_mem_10228_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9889 = np.int32(y_mem_10228_ext.shape[0])
      if (type(y_mem_10228_ext) == cl.array.Array):
        y_mem_10228 = y_mem_10228_ext.data
      else:
        y_mem_10228 = opencl_alloc(self, np.int64(y_mem_10228_ext.nbytes),
                                   "y_mem_10228")
        if (np.int64(y_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, y_mem_10228,
                          normaliseArray(y_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(y_mem_10228_ext),
                                                                                                                            y_mem_10228_ext))
    scalar_out_10581 = self.futhark_kullback_liebler_scaled_f32(x_mem_10227,
                                                                y_mem_10228,
                                                                sizze_9888,
                                                                sizze_9889)
    return np.float32(scalar_out_10581)
  def kullback_liebler_f32(self, x_mem_10227_ext, x_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9868 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9869 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10553 = self.futhark_kullback_liebler_f32(x_mem_10227,
                                                         x_mem_10228,
                                                         sizze_9868, sizze_9869)
    return np.float32(scalar_out_10553)
  def kullback_liebler_scaled_f64(self, x_mem_10227_ext, y_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9836 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(y_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (y_mem_10228_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9837 = np.int32(y_mem_10228_ext.shape[0])
      if (type(y_mem_10228_ext) == cl.array.Array):
        y_mem_10228 = y_mem_10228_ext.data
      else:
        y_mem_10228 = opencl_alloc(self, np.int64(y_mem_10228_ext.nbytes),
                                   "y_mem_10228")
        if (np.int64(y_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, y_mem_10228,
                          normaliseArray(y_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(y_mem_10228_ext),
                                                                                                                            y_mem_10228_ext))
    scalar_out_10471 = self.futhark_kullback_liebler_scaled_f64(x_mem_10227,
                                                                y_mem_10228,
                                                                sizze_9836,
                                                                sizze_9837)
    return np.float64(scalar_out_10471)
  def kullback_liebler_f64(self, x_mem_10227_ext, x_mem_10228_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9816 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    try:
      assert ((type(x_mem_10228_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10228_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9817 = np.int32(x_mem_10228_ext.shape[0])
      if (type(x_mem_10228_ext) == cl.array.Array):
        x_mem_10228 = x_mem_10228_ext.data
      else:
        x_mem_10228 = opencl_alloc(self, np.int64(x_mem_10228_ext.nbytes),
                                   "x_mem_10228")
        if (np.int64(x_mem_10228_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10228,
                          normaliseArray(x_mem_10228_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #1 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10228_ext),
                                                                                                                            x_mem_10228_ext))
    scalar_out_10443 = self.futhark_kullback_liebler_f64(x_mem_10227,
                                                         x_mem_10228,
                                                         sizze_9816, sizze_9817)
    return np.float64(scalar_out_10443)
  def entropy_scaled_f32(self, x_mem_10227_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9800 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    scalar_out_10388 = self.futhark_entropy_scaled_f32(x_mem_10227, sizze_9800)
    return np.float32(scalar_out_10388)
  def entropy_scaled_f64(self, x_mem_10227_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9784 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    scalar_out_10333 = self.futhark_entropy_scaled_f64(x_mem_10227, sizze_9784)
    return np.float64(scalar_out_10333)
  def entropy_f32(self, x_mem_10227_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float32)), "Parameter has unexpected type"
      sizze_9774 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f32",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    scalar_out_10305 = self.futhark_entropy_f32(x_mem_10227, sizze_9774)
    return np.float32(scalar_out_10305)
  def entropy_f64(self, x_mem_10227_ext):
    try:
      assert ((type(x_mem_10227_ext) in [np.ndarray,
                                         cl.array.Array]) and (x_mem_10227_ext.dtype == np.float64)), "Parameter has unexpected type"
      sizze_9764 = np.int32(x_mem_10227_ext.shape[0])
      if (type(x_mem_10227_ext) == cl.array.Array):
        x_mem_10227 = x_mem_10227_ext.data
      else:
        x_mem_10227 = opencl_alloc(self, np.int64(x_mem_10227_ext.nbytes),
                                   "x_mem_10227")
        if (np.int64(x_mem_10227_ext.nbytes) != 0):
          cl.enqueue_copy(self.queue, x_mem_10227,
                          normaliseArray(x_mem_10227_ext),
                          is_blocking=synchronous)
    except (TypeError, AssertionError) as e:
      raise TypeError("Argument #0 has invalid value\nFuthark type: {}\nArgument has Python type {} and value: {}\n".format("[]f64",
                                                                                                                            type(x_mem_10227_ext),
                                                                                                                            x_mem_10227_ext))
    scalar_out_10277 = self.futhark_entropy_f64(x_mem_10227, sizze_9764)
    return np.float64(scalar_out_10277)
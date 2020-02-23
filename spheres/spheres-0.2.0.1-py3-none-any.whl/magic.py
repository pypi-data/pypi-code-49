import math
import sympy
import numpy as np
import functools
import qutip as qt
import itertools

####################################################################

def d_j(d):
    return (d-1)/2

def j_d(j):
    return 2*j + 1

####################################################################

def normalize(v):
    n = np.linalg.norm(v)
    if n != 0:
        return v/n
    else:
        return v

def get_phase(v):
    c = None
    if isinstance(v, qt.Qobj):
        v = v.full().T[0]
    i = (v!=0).argmax(axis=0)
    c = v[i]
    return np.exp(1j*np.angle(c))

def normalize_phase(v):
    return v/get_phase(v)

####################################################################

def random_complex_unit_vector(d):
	v = np.random.randn(d) + 1j*np.random.randn(d)
	return v/np.linalg.norm(v)

def random_hermitian_matrix(d):
	H = np.random.randn(d,d) + 1j*np.random.randn(d, d)
	return H + H.T.conj()

####################################################################

def c_xyz(c, pole="south"):
    if(pole == "south"):
        if c == float("Inf"):
            return np.array([0,0,-1])
        else:
            x, y = c.real, c.imag
            return np.array([2*x/(1 + x**2 + y**2),\
                             2*y/(1 + x**2 + y**2),\
                   (1-x**2-y**2)/(1 + x**2 + y**2)])
    elif (pole == "north"):
        if c == float("Inf"):
            return np.array([0,0,1])
        else:
            x, y = c.real, c.imag
            return np.array([2*x/(1 + x**2 + y**2),\
                             2*y/(1 + x**2 + y**2),\
                   (-1+x**2+y**2)/(1 + x**2 + y**2)])

def xyz_c(xyz, pole="south"):
    x, y, z = xyz
    if (pole=="south"):
        if z == -1:
            return float("Inf")
        else:
            return x/(1+z) + 1j*y/(1+z)
    elif (pole=="north"):
        if z == 1:
            return float("Inf")
        else:
            return x/(1-z) + 1j*y/(1-z)

####################################################################

def spinor_xyz(spinor):
    if isinstance(spinor, np.ndarray):
        spinor = qt.Qobj(spinor)
    return np.array([qt.expect(qt.sigmax(), spinor),\
                     qt.expect(qt.sigmay(), spinor),\
                     qt.expect(qt.sigmaz(), spinor)])

def xyz_spinor(xyz):
    return c_spinor(xyz_c(xyz))

def spin_xyz(spin):
    if isinstance(spinor, np.ndarray):
        spinor = qt.Qobj(spinor)
    j = d_j(spin.shape[0])
    return np.array([qt.expect(qt.jmat(j, 'x'), spinor),\
                     qt.expect(qt.jmat(j, 'y'), spinor),\
                     qt.expect(qt.jmat(j, 'z'), spinor)])

####################################################################

def spinor_c(spinor):
    a, b = None, None
    if isinstance(spinor, qt.Qobj):
        a, b = spinor.full().T[0]
    else:
        a, b = spinor
    if a == 0:
        return float('Inf')
    else:
        return b/a

def c_spinor(c):
    if c == float('Inf'):
        return np.array([0,1])
    else:
        return normalize(np.array([1, c]))

####################################################################

def spin_poly(spin):
    if isinstance(spin, qt.Qobj):
        spin = spin.full().T[0]
    j = (spin.shape[0]-1)/2.
    v = spin
    poly = []
    for m in np.arange(-j, j+1, 1):
        i = int(m+j)
        poly.append(v[i]*\
            (((-1)**(i))*math.sqrt(math.factorial(2*j)/\
                        (math.factorial(j-m)*math.factorial(j+m)))))
    return poly

def poly_spin(poly):
    j = (len(poly)-1)/2.
    spin = []
    for m in np.arange(-j, j+1):
        i = int(m+j)
        spin.append(poly[i]/\
            (((-1)**(i))*math.sqrt(math.factorial(2*j)/\
                        (math.factorial(j-m)*math.factorial(j+m)))))
    aspin = np.array(spin)
    return aspin/np.linalg.norm(aspin)

####################################################################

def poly_roots(poly):
    head_zeros = 0
    for c in poly:
        if c == 0:
            head_zeros += 1 
        else:
            break
    return [float("Inf")]*head_zeros + [complex(root) for root in np.roots(poly)]

def roots_coeffs(roots):
    n = len(roots)
    coeffs = np.array([((-1)**(-i))*sum([np.prod(term) for term in itertools.combinations(roots, i)]) for i in range(0, len(roots)+1)])
    return coeffs/coeffs[0]
        
def roots_poly(roots):
    zeros = roots.count(0j)
    if zeros == len(roots):
        return [1j] + [0j]*len(roots)
    poles = roots.count(float("Inf"))
    roots = [root for root in roots if root != float('Inf')]
    if len(roots) == 0:
        return [0j]*poles + [1j]
    #Z = sympy.symbols("Z")
    #Poly = sympy.Poly(functools.reduce(lambda a, b: a*b, [Z-root for root in roots]), domain="CC")
    #return [0j]*poles + [complex(c) for c in Poly.all_coeffs()] + [0j]*zeros
    return [0j]*poles + roots_coeffs(roots).tolist() + [0j]*(zeros-1)

####################################################################

def spin_roots(spin):
    if isinstance(spin, qt.Qobj):
        spin = spin.full().T[0]
    return poly_roots(spin_poly(spin))

def roots_spin(roots):
    return poly_spin(roots_poly(roots))

####################################################################

def spin_XYZ(spin):
    if isinstance(spin, qt.Qobj):
        spin = spin.full().T[0]
    return [c_xyz(root).tolist() for root in poly_roots(spin_poly(spin))]

def XYZ_spin(XYZ):
    return qt.Qobj(poly_spin(roots_poly([xyz_c(xyz) for xyz in XYZ])))

####################################################################

def differentiate_spin(spin, times=1):
    def _differentiate_spin_(spin):
        n = len(spin)-1
        for i in range(len(spin)):
            spin[i] *= n
            n -= 1;
        return normalize(spin[:-1])
    spin = spin.copy()
    for t in range(times):
        spin = _differentiate_spin_(spin)
    return spin

def integrate_spin(spin, times=1):
    def _integrate_spin_(spin):
        return np.array(spin.tolist()+[0j])
    spin = spin.copy()
    for t in range(times):
        spin = _integrate_spin_(spin)
    return spin    

####################################################################

def sph_xyz(sph):
    r, theta, phi = sph;
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    return np.array([x,y,z])

def xyz_sph(xyz):
    x, y, z = xyz
    r =  np.sqrt(x*x + y*y + z*z)
    theta =  np.arccos(z/r)
    phi =  np.arctan2(y,x)
    return np.array([r,theta,phi])

####################################################################

def eval_spin_at_c(spin, at):
    if at == float("Inf"):
        return eval_spin_at_c(XYZ_spin([c_xyz(xyz_c(xyz, pole="north")) for xyz in spin_XYZ(spin)]), 0)
    if isinstance(spin, qt.Qobj):
        spin = spin.full().T[0]
    normalized = spin/spin[0]
    poly = spin_poly(normalized)
    n = len(poly)
    return sum([poly[i]*(np.power(at,(n-i-1))) for i in range(n)])

def eval_spin_at(spin, at):
    return eval_spin_at_c(spin, xyz_c(at))

def eval_spin(spin, n=50, a=0.6):
    n=20
    theta, phi = np.linspace(0, 2*np.pi, 2*n), np.linspace(0, np.pi, n/2)
    points = []
    for t in theta:
        for p in phi:
            xyz = sph_xyz(np.array([1,t,p]))
            c = eval_spin_at(spin, xyz)
            points.append([xyz.tolist(), [c.real, c.imag], np.abs(c), np.angle(c)/(2*np.pi), c_xyz(c).tolist(), [((np.angle(c)/(np.pi))+1)/2, (1-np.power(a, np.abs(c))), 0.5]])
    return points

####################################################################

def husimi(spin, at):
    if isinstance(spin, qt.Qobj):
        spin = spin.full().T[0]
    n_stars = int(2*d_j(len(spin)))
    coherent = XYZ_spin([at]*n_stars)
    return np.vdot(spin, coherent)

def coherent(at, n):
    return XYZ_spin([at]*n)

def husimi_snapshot(spin, n=30):
    theta, phi = np.linspace(0, 2*np.pi, 16), np.linspace(0, np.pi, 16)
    points = []
    for t in theta:
        points_row = []
        for p in phi:
            #points.append([xyz.tolist(), [c.real, c.imag], np.abs(c), np.angle(c)/(2*np.pi), c_xyz(c).tolist(), [((np.angle(c)/(np.pi))+1)/2, (1-np.power(a, np.abs(c))), 0.5]])
            xyz = sph_xyz(np.array([1,t,p]))           
            h = husimi(spin, xyz)
            a = np.angle(h)
            points_row.append([xyz.tolist(), [np.abs(h), [np.cos(a), np.sin(a)]]])
        points.append(points_row)
    return points


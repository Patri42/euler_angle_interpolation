# Euler angle interpolation

import numpy as np

def rotationX(theta):
    """
    Rotation matrix for rotation about X-axis by angle theta (radians).
    """
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta),  np.cos(theta)]])

def rotationY(theta):
    """
    Rotation matrix for rotation about Y-axis by angle theta (radians).
    """
    return np.array([[ np.cos(theta), 0, np.sin(theta)],
                     [ 0,            1, 0           ],
                     [-np.sin(theta), 0, np.cos(theta)]])

def rotationZ(theta):
    """
    Rotation matrix for rotation about Z-axis by angle theta (radians).
    """
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta),  np.cos(theta), 0],
                     [0,              0,             1]])

def rotationEulerZXZ(attitude_zxz):
    """
    Rotation matrix from ZXZ Euler angles [phi, theta, psi] (radians).
    Sequence: Rz(phi) * Rx(theta) * Rz(psi).
    Note: This function is defined but not used in the interpolation below.
    """
    phi, theta, psi = attitude_zxz
    Rz1 = rotationZ(phi)
    Rx  = rotationX(theta)
    Rz2 = rotationZ(psi)
    R   = Rz1 @ Rx @ Rz2
    return R

def radToDeg(rad):
    """Convert radians to degrees (works on scalars or arrays)."""
    return np.array(rad) * (180.0 / np.pi)

def degToRad(deg):
    """Convert degrees to radians (works on scalars or arrays)."""
    return np.array(deg) * (np.pi / 180.0)

def printEulerAngles(title, attitude_deg):
    """
    Print Euler angles in degrees with a title.
    attitude_deg is expected to be an iterable [phi, theta, psi] in degrees.
    """
    print("Euler Angles {} [{:.2f}, {:.2f}, {:.2f}]".format(
        title, attitude_deg[0], attitude_deg[1], attitude_deg[2]))

def linearInterpolate(v0, v1, t):
    """
    Linear interpolation between two vectors v0 and v1.
    v(t) = (1 - t) * v0 + t * v1, where t in [0, 1].
    Here used to interpolate Euler angles component-wise.
    """
    return v0 * (1 - t) + v1 * t

# Start and end Euler angles (in degrees): [phi, theta, psi]
attitude0 = degToRad([0, 0, 0])
attitude1 = degToRad([-30, 45, 135])

printEulerAngles("Start", radToDeg(attitude0))
printEulerAngles("End",   radToDeg(attitude1))

# Interpolation parameter t in [0, 1]
t = 0.5

# Simple linear interpolation of Euler angles
attitude_interp = linearInterpolate(attitude0, attitude1, t)

printEulerAngles("Interpolated", radToDeg(attitude_interp))
